from __future__ import annotations

import argparse
import csv
from collections import defaultdict, deque
from pathlib import Path

import dependency_graph


ROOT = Path(__file__).resolve().parents[2]
PROOF_TASK_KINDS = {"thm", "lem", "prop", "cor"}
FORMAL_KINDS = {"def", "ax", "thm", "lem", "prop", "cor"}


def chapter_from_file(file: str) -> str:
    parts = Path(file).parts
    if len(parts) >= 2 and parts[0] == "volume-i":
        return parts[1]
    return ""


def chapter_order(repo_root: Path) -> dict[str, int]:
    index = repo_root / "volume-i" / "index.tex"
    if not index.exists():
        return {}
    order: dict[str, int] = {}
    for line in index.read_text(encoding="utf-8", errors="replace").splitlines():
        line = line.strip()
        if not line.startswith(r"\input{volume-i/"):
            continue
        chapter = line.removeprefix(r"\input{volume-i/").removesuffix("}").split("/", 1)[0]
        if chapter not in order:
            order[chapter] = len(order)
    return order


def proof_label(label: str) -> str:
    return f"prf:{label.split(':', 1)[1]}"


def proof_file_map(repo_root: Path) -> dict[str, str]:
    mapping: dict[str, str] = {}
    for path in (repo_root / "volume-i").glob("**/proofs/**/prf-*.tex"):
        key = path.stem.removeprefix("prf-").casefold()
        mapping.setdefault(key, path.relative_to(repo_root).as_posix())
    return mapping


def proof_file_for_label(proofs: dict[str, str], label: str) -> str:
    stem = label.split(":", 1)[1]
    return proofs.get(stem.casefold(), "")


def build_order(repo_root: Path) -> tuple[list[dict[str, object]], list[list[str]], list[str]]:
    universe = dependency_graph.build_universe(repo_root.parent, "lra-volume-*")
    edge_report = dependency_graph.extract_edges_from_universe(repo_root, universe, "in-memory")
    chapter_rank = chapter_order(repo_root)
    proofs = proof_file_map(repo_root)

    nodes = {
        node.id: node
        for node in universe.nodes
        if node.repo == repo_root.name and node.kind in FORMAL_KINDS
    }

    def node_sort_key(node_id: str) -> tuple[int, str, int, str]:
        node = nodes[node_id]
        chapter = chapter_from_file(node.file)
        return (chapter_rank.get(chapter, 999), node.file, node.line, node.label)

    dependents: dict[str, set[str]] = defaultdict(set)
    dependencies: dict[str, set[str]] = defaultdict(set)
    external_dependency_count: dict[str, int] = defaultdict(int)
    dependency_labels: dict[str, set[str]] = defaultdict(set)

    for edge in edge_report.edges:
        if edge.status != "ok" or not edge.source_id or not edge.target_id:
            continue
        if edge.source_id not in nodes:
            continue
        if edge.target_id in nodes:
            dependencies[edge.source_id].add(edge.target_id)
            dependents[edge.target_id].add(edge.source_id)
            dependency_labels[edge.source_id].add(nodes[edge.target_id].label)
        else:
            external_dependency_count[edge.source_id] += 1

    indegree = {node_id: len(dependencies.get(node_id, set())) for node_id in nodes}
    ready = (node_id for node_id, degree in indegree.items() if degree == 0)
    queue = deque(sorted(ready, key=node_sort_key))
    ordered: list[str] = []

    while queue:
        node_id = queue.popleft()
        ordered.append(node_id)
        for dependent in sorted(dependents.get(node_id, set()), key=node_sort_key):
            indegree[dependent] -= 1
            if indegree[dependent] == 0:
                queue.append(dependent)
        queue = deque(sorted(queue, key=node_sort_key))

    remaining = [node_id for node_id, degree in indegree.items() if degree > 0]
    cycles: list[list[str]] = []
    if remaining:
        cycles.append(
            sorted(
                (nodes[node_id].label for node_id in remaining),
                key=lambda label: node_sort_key(f"{repo_root.name}:{label}"),
            )
        )
        ordered.extend(sorted(remaining, key=node_sort_key))

    rows: list[dict[str, object]] = []
    for index, node_id in enumerate(ordered, start=1):
        node = nodes[node_id]
        is_proof_task = node.kind in PROOF_TASK_KINDS
        rows.append(
            {
                "order": index,
                "label": node.label,
                "kind": node.kind,
                "title": node.title,
                "chapter": chapter_from_file(node.file),
                "file": node.file,
                "line": node.line,
                "action": "prove" if is_proof_task else "prerequisite",
                "proof_label": proof_label(node.label) if is_proof_task else "",
                "proof_file": proof_file_for_label(proofs, node.label) if is_proof_task else "",
                "formal_dependencies": len(dependencies.get(node_id, set())),
                "formal_dependents": len(dependents.get(node_id, set())),
                "immediate_formal_dependencies": "; ".join(sorted(dependency_labels.get(node_id, set()))),
                "external_dependencies": external_dependency_count.get(node_id, 0),
            }
        )
    covered = {str(row["proof_file"]).casefold() for row in rows if row["proof_file"]}
    orphans = sorted(path for path in proofs.values() if path.casefold() not in covered)
    return rows, cycles, orphans


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()) if rows else ["order"])
        writer.writeheader()
        writer.writerows(rows)


def write_markdown(path: Path, rows: list[dict[str, object]], cycles: list[list[str]], orphans: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Volume I Formal Prerequisite and Proof Order",
        "",
        "Order is topological with formal dependencies first and dependents later.",
        "Definitions and axioms are listed as prerequisites; theorems, lemmas, propositions, and corollaries are proof tasks.",
        "",
        f"- Formal artifacts listed: {len(rows)}",
        f"- Proof tasks: {sum(1 for row in rows if row['action'] == 'prove')}",
        f"- Prerequisite-only rows: {sum(1 for row in rows if row['action'] == 'prerequisite')}",
        f"- Cyclic groups detected: {len(cycles)}",
        f"- Orphan proof files without a matching theorem-like source: {len(orphans)}",
        "",
        "| # | Action | Kind | Label | Chapter | Formal deps | Immediate formal dependencies | Formal dependents | Proof file |",
        "|---:|---|---|---|---|---:|---|---:|---|",
    ]
    for row in rows:
        proof_file = row["proof_file"] or ""
        lines.append(
            f"| {row['order']} | {row['action']} | `{row['kind']}` | `{row['label']}` | `{row['chapter']}` | "
            f"{row['formal_dependencies']} | {row['immediate_formal_dependencies']} | "
            f"{row['formal_dependents']} | `{proof_file}` |"
        )
    if cycles:
        lines += ["", "## Cycles", ""]
        for index, cycle in enumerate(cycles, start=1):
            lines.append(f"{index}. " + ", ".join(f"`{label}`" for label in cycle))
    if orphans:
        lines += ["", "## Orphan Proof Files", ""]
        for orphan in orphans:
            lines.append(f"- `{orphan}`")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate Volume I formal prerequisite and proof order.")
    parser.add_argument("--repo-root", type=Path, default=ROOT)
    parser.add_argument("--csv", type=Path, default=ROOT / "build" / "reports" / "volume-i-proof-order.csv")
    parser.add_argument("--markdown", type=Path, default=ROOT / "build" / "reports" / "volume-i-proof-order.md")
    args = parser.parse_args()

    rows, cycles, orphans = build_order(args.repo_root.resolve())
    write_csv(args.csv, rows)
    write_markdown(args.markdown, rows, cycles, orphans)
    print(f"wrote {len(rows)} formal artifacts")
    print(f"proof tasks: {sum(1 for row in rows if row['action'] == 'prove')}")
    print(f"prerequisite-only rows: {sum(1 for row in rows if row['action'] == 'prerequisite')}")
    print(f"csv: {args.csv}")
    print(f"markdown: {args.markdown}")
    if cycles:
        print(f"cycles: {len(cycles)}")
    if orphans:
        print(f"orphan proof files: {len(orphans)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
