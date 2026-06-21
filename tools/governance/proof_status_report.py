from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path

from core.file_inventory import files_to_validate


ROOT = Path(__file__).resolve().parents[2]
PROOF_FOR_RE = re.compile(r"\\LRAProofFor\{(?P<label>(?:thm|lem|prop|cor):[A-Za-z0-9-]+)\}")
PROOF_RE = re.compile(r"\\begin\{proof\}\[(?P<title>[^\]]+)\](?P<body>.*?)\\end\{proof\}", re.DOTALL)
TODO_RE = re.compile(
    r"\bTODO\b|MIGRATION TODO|professional standard proof for|detailed learning proof for",
    re.IGNORECASE,
)


def chapter_from_path(path: Path, repo_root: Path) -> str:
    rel = path.relative_to(repo_root)
    parts = rel.parts
    if len(parts) >= 2 and parts[0] == "volume-i":
        return parts[1]
    return ""


def proof_bodies(text: str) -> dict[str, str]:
    bodies: dict[str, str] = {}
    for match in PROOF_RE.finditer(text):
        title = match.group("title")
        body = match.group("body")
        if "Professional Standard Proof" in title:
            bodies["professional"] = body
        elif "Detailed Learning Proof" in title:
            bodies["detailed"] = body
    return bodies


def classify_proof(path: Path, repo_root: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8", errors="replace")
    proof_for = PROOF_FOR_RE.search(text)
    bodies = proof_bodies(text)
    missing_layers = [name for name in ("professional", "detailed") if name not in bodies]
    todo_layers = [name for name, body in bodies.items() if TODO_RE.search(body)]
    status = "done"
    if missing_layers:
        status = "invalid"
    elif todo_layers:
        status = "todo"

    return {
        "status": status,
        "label": proof_for.group("label") if proof_for else "",
        "chapter": chapter_from_path(path, repo_root),
        "proof_file": path.relative_to(repo_root).as_posix(),
        "todo_layers": "; ".join(todo_layers),
        "missing_layers": "; ".join(missing_layers),
    }


def collect_rows(repo_root: Path) -> list[dict[str, str]]:
    volume_root = repo_root / "volume-i"
    paths = [
        path
        for path in files_to_validate(volume_root, only_reachable=True)
        if path.name.startswith("prf-") and "proofs" in path.relative_to(volume_root).parts
    ]
    return [classify_proof(path, repo_root) for path in paths]


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = ["status", "label", "chapter", "proof_file", "todo_layers", "missing_layers"]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_markdown(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    done = [row for row in rows if row["status"] == "done"]
    todo = [row for row in rows if row["status"] == "todo"]
    invalid = [row for row in rows if row["status"] == "invalid"]
    lines = [
        "# Volume I Proof Status",
        "",
        f"- Total proof files: {len(rows)}",
        f"- Done: {len(done)}",
        f"- TODO: {len(todo)}",
        f"- Invalid proof-layer shape: {len(invalid)}",
        "",
        "| Status | Label | Chapter | Proof file | TODO layers |",
        "|---|---|---|---|---|",
    ]
    for row in rows:
        lines.append(
            f"| {row['status']} | `{row['label']}` | `{row['chapter']}` | "
            f"`{row['proof_file']}` | {row['todo_layers']} |"
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Report Volume I proof files done versus TODO.")
    parser.add_argument("--repo-root", type=Path, default=ROOT)
    parser.add_argument("--csv", type=Path, default=ROOT / "build" / "reports" / "volume-i-proof-status.csv")
    parser.add_argument("--markdown", type=Path, default=ROOT / "build" / "reports" / "volume-i-proof-status.md")
    args = parser.parse_args()

    rows = collect_rows(args.repo_root.resolve())
    write_csv(args.csv, rows)
    write_markdown(args.markdown, rows)

    counts = {status: sum(1 for row in rows if row["status"] == status) for status in ("done", "todo", "invalid")}
    print(f"total proof files: {len(rows)}")
    print(f"done: {counts['done']}")
    print(f"todo: {counts['todo']}")
    print(f"invalid: {counts['invalid']}")
    print(f"csv: {args.csv}")
    print(f"markdown: {args.markdown}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
