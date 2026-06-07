#!/usr/bin/env python3
"""Appendable chapter artifact registry and LaTeX generator.

The registry is the source of truth. Generated LaTeX is wrapped in stable
artifact markers so single artifacts can be replaced without touching nearby
hand-authored material.
"""

from __future__ import annotations

import argparse
import base64
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

import yaml


REPO_ROOT = Path(__file__).resolve().parents[1]
VOLUME_ROOT = REPO_ROOT / "volume-i"
ARTIFACTS_ROOT = REPO_ROOT / "artifacts"
REPORTS_ROOT = REPO_ROOT / "reports"
GENERATED_BEGIN = "% BEGIN GENERATED ARTIFACT: {label}"
GENERATED_END = "% END GENERATED ARTIFACT: {label}"

THEOREM_LIKE = {"theorem", "lemma", "proposition", "corollary"}
CONTENT_FIELDS = (
    "body",
    "quantified_form",
    "interpretation",
    "predicate_reading",
    "examples",
    "non_examples",
    "contrapositive",
    "contrapositive_predicate_reading",
    "negated_form",
    "negation_predicate_reading",
    "failure_modes",
    "readable_decomposition",
    "failure_mode_decomposition",
    "proof_sketch",
)
SECTION_ORDER = [
    "notation",
    "syntax",
    "semantics",
    "algebra",
    "algebra-of-propositions",
    "duality",
    "normal-forms",
    "functional-completeness",
    "proof-systems",
    "metatheory",
    "reference",
    "reference-tables-and-fallacies",
    "exercises",
    "capstone",
]
SECTION_TITLES = {
    "notation": "Notation and Conventions",
    "syntax": "Syntax",
    "semantics": "Semantics",
    "algebra": "Algebra of Propositions",
    "algebra-of-propositions": "Algebra of Propositions",
    "duality": "Duality",
    "normal-forms": "Normal Forms",
    "functional-completeness": "Functional Completeness",
    "proof-systems": "Proof Systems",
    "metatheory": "Metatheory",
    "reference": "Reference Tables and Fallacies",
    "reference-tables-and-fallacies": "Reference Tables and Fallacies",
    "exercises": "Exercises",
    "capstone": "Capstone",
}
KNOWN_NOTATION_PATTERNS = {
    r"\mathbb{B}": "propositional_logic.truth_values",
    r"\Bool": "propositional_logic.truth_values",
    r"\WFF": "propositional_logic.formula_set",
    r"\Prop": "propositional_logic.variable_set",
    r"\widehat v": "propositional_logic.extended_truth_assignment",
    r"\models": "propositional_logic.semantic_consequence",
    r"\equiv": "propositional_logic.logical_equivalence",
    r"\NAND": "propositional_logic.nand",
    r"\NOR": "propositional_logic.nor",
    r"\Gamma": "propositional_logic.premise_set",
    r"\varphi": "propositional_logic.formula",
    r"\psi": "propositional_logic.second_formula",
    r"\chi": "propositional_logic.third_formula",
    r"\circ": "propositional_logic.generic_binary_connective",
    r"\neg": "propositional_logic.negation",
    r"\land": "propositional_logic.conjunction",
    r"\lor": "propositional_logic.disjunction",
    r"\to": "propositional_logic.conditional",
    r"\leftrightarrow": "propositional_logic.biconditional",
    r"\top": "propositional_logic.truth_constant_top",
    r"\bot": "propositional_logic.truth_constant_bottom",
    r"C[-]": "propositional_logic.formula_context",
    r"C[\varphi]": "propositional_logic.formula_context_substitution",
}
PREDICATE_NAMES = (
    "PropositionalVariable",
    "WellFormedFormula",
    "AtomicFormula",
    "MolecularFormula",
    "MainConnective",
    "LogicalConnective",
    "UnaryConnective",
    "BinaryConnective",
    "ParseTree",
    "FormulaVariableSet",
    "Subformula",
    "FormulaDepth",
    "ConnectiveCount",
    "Satisfiable",
    "TruthAssignment",
    "SatisfiesFormula",
    "SatisfiesSet",
    "TruthTable",
    "Tautology",
    "Contradiction",
    "SatisfiableFormula",
    "Contingency",
    "LogicalConsequence",
    "LogicalEquivalence",
    "PropositionalEquivalenceLaw",
    "FormulaContext",
    "BooleanFunction",
    "TruthFunctionOfFormula",
)
KIND_TO_ENV = {
    "definition": "definition",
    "theorem": "theorem",
    "lemma": "lemma",
    "proposition": "proposition",
    "corollary": "corollary",
    "axiom": "axiom",
    "remark": "remark",
}
KIND_TO_TYPE = {
    "definition": "def",
    "theorem": "thm",
    "lemma": "lem",
    "proposition": "prop",
    "corollary": "cor",
    "axiom": "ax",
    "remark": "rem",
}
TYPE_TO_KIND = {v: k for k, v in KIND_TO_TYPE.items()}


@dataclass
class LoadedArtifact:
    registry_path: Path
    chapter: str
    topic: str
    data: dict[str, Any]
    order: int = 0


def safe_read_yaml(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    try:
        with path.open(encoding="utf-8") as f:
            return yaml.safe_load(f) or {}
    except yaml.YAMLError:
        return {}


def write_yaml(path: Path, data: dict[str, Any]) -> None:
    class LiteralDumper(yaml.SafeDumper):
        pass

    def str_representer(dumper: yaml.Dumper, value: str) -> yaml.nodes.ScalarNode:
        style = "|" if "\n" in value else None
        return dumper.represent_scalar("tag:yaml.org,2002:str", value, style=style)

    LiteralDumper.add_representer(str, str_representer)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as f:
        yaml.dump(data, f, Dumper=LiteralDumper, sort_keys=False, allow_unicode=False, width=100)


def infer_kind(label: str) -> str:
    prefix = label.split(":", 1)[0]
    if prefix not in TYPE_TO_KIND:
        raise ValueError(f"Cannot infer kind from label prefix in {label!r}.")
    return TYPE_TO_KIND[prefix]


def title_from_label(label: str) -> str:
    root = label.split(":", 1)[1]
    return " ".join(part.capitalize() for part in root.split("-"))


def default_registry(chapter: str, topic: str) -> dict[str, Any]:
    return {
        "schema_version": 1,
        "chapter": chapter,
        "topic": topic,
        "encoding": "utf-8",
        "content_format": "latex",
        "artifacts": [],
    }


def ensure_registry(path: Path, chapter: str | None = None, topic: str | None = None) -> dict[str, Any]:
    if path.exists():
        data = safe_read_yaml(path)
        data.setdefault("schema_version", 1)
        data.setdefault("chapter", chapter or path.parent.name)
        data.setdefault("topic", topic or path.stem)
        data.setdefault("encoding", "utf-8")
        data.setdefault("content_format", "latex")
        data.setdefault("artifacts", [])
        return data
    chapter = chapter or path.parent.name
    topic = topic or path.stem
    data = default_registry(chapter, topic)
    write_yaml(path, data)
    return data


def normalize_content(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value.rstrip()
    if isinstance(value, dict):
        encoding = str(value.get("encoding", "plain")).lower()
        text = value.get("text", "")
        if encoding == "plain":
            return str(text).rstrip()
        if encoding == "base64":
            return base64.b64decode(str(text)).decode("utf-8").rstrip()
        raise ValueError(f"Unsupported structured content encoding: {encoding}")
    raise TypeError(f"Unsupported content value type: {type(value).__name__}")


def content_field(text: str) -> str:
    return text.rstrip() if text else ""


def sort_key_for_loaded(loaded: LoadedArtifact) -> tuple[int, str, int, str]:
    try:
        topic_index = SECTION_ORDER.index(loaded.topic)
    except ValueError:
        topic_index = len(SECTION_ORDER)
    return topic_index, loaded.topic, loaded.order, str(loaded.data.get("label", ""))


def artifact_defaults(label: str, kind: str, title: str) -> dict[str, Any]:
    proof_required = kind in THEOREM_LIKE
    return {
        "label": label,
        "kind": kind,
        "title": title,
        "body": f"TODO: write the {kind} body for {title}.",
        "quantified_form": "TODO: provide the fully quantified or recursive form.",
        "interpretation": "TODO: explain the mathematical role of this artifact.",
        "predicate_reading": "",
        "examples": "",
        "non_examples": "",
        "contrapositive": "",
        "contrapositive_predicate_reading": "",
        "negated_form": "",
        "negation_predicate_reading": "",
        "failure_modes": "",
        "readable_decomposition": "",
        "failure_mode_decomposition": "",
        "proof_required": proof_required,
        "proof_sketch": "TODO: record the intended proof strategy.",
        "dependencies": [],
        "predicates": {"defines": [], "uses": []},
        "notations": {"defines": [], "uses": []},
        "relations": {"defines": [], "uses": []},
    }


def cmd_append(args: argparse.Namespace) -> int:
    registry_path = Path(args.registry).resolve()
    data = ensure_registry(registry_path)
    artifacts = data.setdefault("artifacts", [])
    label = args.label
    existing = next((a for a in artifacts if a.get("label") == label), None)
    if existing and not args.update:
        print(f"Artifact {label} already exists in {registry_path}. Use --update to modify it.", file=sys.stderr)
        return 2
    kind = args.kind or infer_kind(label)
    title = args.title or title_from_label(label)
    specified = {
        "label": label,
        "kind": kind,
        "title": title,
    }
    for field in (
        "body",
        "quantified_form",
        "interpretation",
        "predicate_reading",
        "examples",
        "non_examples",
        "contrapositive",
        "contrapositive_predicate_reading",
        "negated_form",
        "negation_predicate_reading",
        "failure_modes",
        "readable_decomposition",
        "failure_mode_decomposition",
        "proof_sketch",
    ):
        value = getattr(args, field, None)
        if value is not None:
            specified[field] = value
    if args.proof_required is not None:
        specified["proof_required"] = args.proof_required

    if existing:
        for key, value in specified.items():
            existing[key] = value
    else:
        art = artifact_defaults(label, kind, title)
        art.update(specified)
        artifacts.append(art)
    write_yaml(registry_path, data)
    print(f"{'Updated' if existing else 'Appended'} {label} in {registry_path}")
    return 0


def registry_paths_for_chapter(chapter: str) -> list[Path]:
    root = ARTIFACTS_ROOT / chapter
    if root.exists():
        return sorted(root.glob("*.yaml"))
    chapter_file = ARTIFACTS_ROOT / f"{chapter}.yaml"
    return [chapter_file] if chapter_file.exists() else []


def load_registry(path: Path) -> list[LoadedArtifact]:
    data = safe_read_yaml(path)
    chapter = data.get("chapter") or path.parent.name
    topic = data.get("topic") or path.stem
    return [
        LoadedArtifact(path, chapter, topic, artifact, order)
        for order, artifact in enumerate(data.get("artifacts", []))
    ]


def load_artifacts(chapter: str, topic: str | None = None) -> list[LoadedArtifact]:
    loaded: list[LoadedArtifact] = []
    for path in registry_paths_for_chapter(chapter):
        data = safe_read_yaml(path)
        if topic and data.get("topic", path.stem) != topic:
            continue
        loaded.extend(load_registry(path))
    return sorted(loaded, key=sort_key_for_loaded)


def parse_artifact_key(key: str) -> tuple[str, str, str]:
    parts = key.split("|")
    if len(parts) != 3:
        raise ValueError("Artifact key must have form chapter|topic|label.")
    return parts[0], parts[1], parts[2]


def chapter_root(chapter: str) -> Path:
    return VOLUME_ROOT / chapter


def topic_notes_path(chapter: str, topic: str) -> Path:
    return chapter_root(chapter) / "notes" / topic / f"notes-{topic}.tex"


def proof_path(chapter: str, topic: str, label: str) -> Path:
    root = label.split(":", 1)[1]
    return chapter_root(chapter) / "proofs" / topic / f"prf-{root}.tex"


def index_path_for_topic(chapter: str, topic: str, kind: str) -> Path:
    return chapter_root(chapter) / kind / topic / "index.tex"


def notation_page_path(chapter: str) -> Path:
    return chapter_root(chapter) / "notes" / "notation" / "index.tex"


def latex_input(abs_path: Path) -> str:
    rel = abs_path.resolve().relative_to(REPO_ROOT).as_posix()
    return rel.removesuffix(".tex")


def scanner_rel(path: Path, root: Path) -> str:
    return str(path.relative_to(root))


def marker_pattern(label: str) -> re.Pattern[str]:
    begin = re.escape(GENERATED_BEGIN.format(label=label))
    end = re.escape(GENERATED_END.format(label=label))
    return re.compile(begin + r".*?" + end, re.DOTALL)


def replace_or_append_generated_block(path: Path, label: str, block: str, section_heading: str | None = None) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    wrapped = f"{GENERATED_BEGIN.format(label=label)}\n{block.rstrip()}\n{GENERATED_END.format(label=label)}\n"
    if not path.exists():
        prefix = f"{section_heading}\n\n" if section_heading else ""
        path.write_text(prefix + wrapped, encoding="utf-8", newline="\n")
        return
    text = path.read_text(encoding="utf-8")
    text = "\n".join(
        line for line in text.splitlines()
        if not line.startswith("\\providecommand{\\")
    )
    if text:
        text += "\n"
    pattern = marker_pattern(label)
    if pattern.search(text):
        path.write_text(
            pattern.sub(lambda _m: wrapped.rstrip(), text)
            + ("\n" if not text.endswith("\n") else ""),
            encoding="utf-8",
            newline="\n",
        )
        return
    non_comment = "\n".join(
        line for line in text.splitlines()
        if line.strip() and not line.lstrip().startswith("%") and not line.lstrip().startswith("\\section")
    )
    if non_comment and "BEGIN GENERATED ARTIFACT:" not in text:
        raise RuntimeError(f"Drift: {path} has hand-authored content and no generated artifact block for {label}.")
    sep = "" if text.endswith("\n") or not text else "\n"
    path.write_text(text + sep + wrapped, encoding="utf-8", newline="\n")


def ensure_input(index_path: Path, target: Path, heading: str | None = None) -> None:
    index_path.parent.mkdir(parents=True, exist_ok=True)
    line = f"\\input{{{latex_input(target)}}}"
    if index_path.exists():
        text = index_path.read_text(encoding="utf-8")
    else:
        text = f"{heading}\n" if heading else ""
    if line not in text:
        if text and not text.endswith("\n"):
            text += "\n"
        text += line + "\n"
        index_path.write_text(text, encoding="utf-8", newline="\n")


def render_support_remarks(artifact: dict[str, Any]) -> str:
    chunks: list[str] = []
    quantified = canonicalize_generated_text(normalize_content(artifact.get("quantified_form")))
    if quantified:
        chunks.append(f"\\begin{{remark*}}[Standard quantified statement]\n{quantified}\n\\end{{remark*}}")
    predicate = canonicalize_generated_text(normalize_content(artifact.get("predicate_reading")))
    if predicate:
        title = "Definition predicate reading" if artifact.get("kind") == "definition" else "Predicate reading"
        chunks.append(f"\\begin{{remark*}}[{title}]\n{predicate}\n\\end{{remark*}}")
    contrapositive = canonicalize_generated_text(normalize_content(artifact.get("contrapositive")))
    if contrapositive:
        chunks.append(f"\\begin{{remark*}}[Contrapositive quantified statement]\n{contrapositive}\n\\end{{remark*}}")
    contra_predicate = canonicalize_generated_text(normalize_content(artifact.get("contrapositive_predicate_reading")))
    if contra_predicate:
        chunks.append(f"\\begin{{remark*}}[Contrapositive predicate reading]\n{contra_predicate}\n\\end{{remark*}}")
    negated = canonicalize_generated_text(normalize_content(artifact.get("negated_form")))
    if negated:
        chunks.append(f"\\begin{{remark*}}[Negated quantified statement]\n{negated}\n\\end{{remark*}}")
    negation_predicate = canonicalize_generated_text(normalize_content(artifact.get("negation_predicate_reading")))
    if negation_predicate:
        chunks.append(f"\\begin{{remark*}}[Negation predicate reading]\n{negation_predicate}\n\\end{{remark*}}")
    failure_modes = canonicalize_generated_text(normalize_content(artifact.get("failure_modes")))
    if failure_modes:
        chunks.append(f"\\begin{{remark*}}[Failure modes]\n{failure_modes}\n\\end{{remark*}}")
    readable_decomposition = canonicalize_generated_text(normalize_content(artifact.get("readable_decomposition")))
    if readable_decomposition:
        chunks.append(f"\\begin{{remark*}}[Readable decomposition]\n{readable_decomposition}\n\\end{{remark*}}")
    failure_decomposition = canonicalize_generated_text(normalize_content(artifact.get("failure_mode_decomposition")))
    if failure_decomposition:
        chunks.append(f"\\begin{{remark*}}[Failure mode decomposition]\n{failure_decomposition}\n\\end{{remark*}}")
    interpretation = canonicalize_generated_text(normalize_content(artifact.get("interpretation")))
    if interpretation:
        chunks.append(f"\\begin{{remark*}}[Interpretation]\n{interpretation}\n\\end{{remark*}}")
    examples = canonicalize_generated_text(normalize_content(artifact.get("examples")))
    if examples:
        if artifact.get("kind") == "definition":
            chunks.append(f"\\begin{{remark*}}[Examples]\n{examples}\n\\end{{remark*}}")
    non_examples = canonicalize_generated_text(normalize_content(artifact.get("non_examples")))
    if non_examples:
        chunks.append(f"\\begin{{remark*}}[Non-examples]\n{non_examples}\n\\end{{remark*}}")
    deps = artifact.get("dependencies") or []
    if deps:
        items = "\n".join(f"  \\item \\hyperref[{dep}]{{{dep}}}" for dep in deps)
        chunks.append(f"\\begin{{dependencies}}\n\\begin{{itemize}}\n{items}\n\\end{{itemize}}\n\\end{{dependencies}}")
    else:
        chunks.append("\\begin{dependencies}\n\\NoLocalDependencies\n\\end{dependencies}")
    return "\n\n".join(chunks)


def canonicalize_generated_text(text: str) -> str:
    text = text.replace(r"\mathbb B", r"\mathbb{B}")
    text = text.replace(r"\Bool", r"\mathbb{B}")
    text = text.replace(r"\WFF_{\NAND}", r"\WFF_{\{\uparrow\}}")
    text = text.replace(r"\mathbin{\dot\lor}", r"\text{ and exactly one of }")
    for name in PREDICATE_NAMES:
        text = re.sub(
            rf"(?<!operatorname{{)\b{name}\s*\(",
            rf"\\operatorname{{{name}}}(",
            text,
        )
    return text


def render_statement(loaded: LoadedArtifact) -> str:
    art = loaded.data
    kind = art["kind"]
    env = KIND_TO_ENV[kind]
    label = art["label"]
    title = art.get("title") or title_from_label(label)
    body = canonicalize_generated_text(normalize_content(art.get("body")))
    proof_link = ""
    if kind in THEOREM_LIKE and art.get("proof_required", True):
        proof_link = f"\n\n\\noindent\\hyperref[prf:{label.split(':', 1)[1]}]{{Go to proof.}}"
    body_with_link = body.rstrip() + proof_link
    box_colors = {
        "definition": ("propbox", "propborder"),
        "axiom": ("axiombox", "axiomborder"),
        "theorem": ("thmbox", "thmborder"),
        "lemma": ("lembox", "lemborder"),
        "proposition": ("propbox", "propborder"),
        "corollary": ("corbox", "corborder"),
        "remark": ("propbox", "propborder"),
    }[kind]
    heading = f"{kind.capitalize()} ({title})" if kind != "axiom" else f"Axiom ({title})"
    return f"""\\begin{{tcolorbox}}[colback={box_colors[0]}, colframe={box_colors[1]}, arc=2pt,
  left=6pt, right=6pt, top=4pt, bottom=4pt,
  title={{\\small\\textbf{{{heading}}}}},
  fonttitle=\\small\\bfseries]
\\begin{{{env}}}[{title}]
\\label{{{label}}}
{body_with_link}
\\end{{{env}}}
\\end{{tcolorbox}}

{render_support_remarks(art)}"""


def artifact_content_text(artifact: dict[str, Any]) -> str:
    return "\n".join(
        canonicalize_generated_text(normalize_content(artifact.get(field)))
        for field in CONTENT_FIELDS
    )


def declared_notation_symbols(artifact: dict[str, Any]) -> set[str]:
    symbols: set[str] = set()
    for item in artifact.get("notations", {}).get("defines", []) + artifact.get("notations", {}).get("uses", []):
        if isinstance(item, dict):
            for key in ("symbol", "latex"):
                value = item.get(key)
                if value:
                    add_declared_symbol(symbols, str(value))
        elif item:
            add_declared_symbol(symbols, str(item))
    return symbols


def add_declared_symbol(symbols: set[str], value: str) -> None:
    normalized = value.replace(r"\mathbb B", r"\mathbb{B}")
    symbols.add(normalized)
    for part in normalized.split(","):
        part = part.strip()
        if part:
            symbols.add(part)
    if r"\varphi,\psi" in normalized:
        symbols.update({r"\varphi", r"\psi"})
    if r"\varphi,\psi,\chi,\theta" in normalized:
        symbols.update({r"\varphi", r"\psi", r"\chi", r"\theta"})
    if r"\models" in normalized:
        symbols.add(r"\models")
    if r"\equiv" in normalized:
        symbols.add(r"\equiv")
    if r"\widehat v" in normalized:
        symbols.add(r"\widehat v")


def detect_notation_drift(loaded: LoadedArtifact) -> list[str]:
    text = artifact_content_text(loaded.data)
    declared = declared_notation_symbols(loaded.data)
    drift: list[str] = []
    for symbol in sorted(KNOWN_NOTATION_PATTERNS, key=len, reverse=True):
        if symbol in text and symbol not in declared:
            drift.append(
                f"{loaded.registry_path}: {loaded.data.get('label')}: emitted notation {symbol} "
                "is not declared in notations.defines or notations.uses"
            )
    if r"\Bool" in text:
        drift.append(f"{loaded.registry_path}: {loaded.data.get('label')}: use \\mathbb{{B}}, not \\Bool")
    if r"\WFF_{\NAND}" in text:
        drift.append(f"{loaded.registry_path}: {loaded.data.get('label')}: use \\WFF_{{\\{{\\uparrow\\}}}}, not \\WFF_{{\\NAND}}")
    if r"\mathbin{\dot\lor}" in text:
        drift.append(f"{loaded.registry_path}: {loaded.data.get('label')}: avoid \\mathbin{{\\dot\\lor}}")
    return drift


def metadata_items(artifact: dict[str, Any], section: str) -> list[dict[str, Any]]:
    raw = artifact.get(section, {}) or {}
    items: list[dict[str, Any]] = []
    for role in ("defines", "uses"):
        for item in raw.get(role, []) or []:
            if isinstance(item, dict):
                copy = dict(item)
            else:
                copy = {"registry_id": str(item)}
            copy["_role"] = role
            items.append(copy)
    return items


def registry_key(item: dict[str, Any]) -> str:
    return str(item.get("registry_id") or item.get("name") or item.get("symbol") or item.get("label") or "")


def notation_dedupe_key(symbol: str, item: dict[str, Any]) -> str:
    key = registry_key(item)
    return key or symbol


def notation_specificity(symbol: str, item: dict[str, Any]) -> int:
    key = registry_key(item)
    if key == "propositional_logic.formula_metavariables":
        return len([part for part in symbol.split(",") if part.strip()])
    return 1


def is_local_metadata(item: dict[str, Any]) -> bool:
    return str(item.get("status", "")).lower() == "local"


def is_proposed_definition(item: dict[str, Any]) -> bool:
    return str(item.get("status", "")).lower() == "proposed"


def section_title(topic: str) -> str:
    return SECTION_TITLES.get(topic, topic.replace("-", " ").title())


def render_notation_page(chapter: str, artifacts: list[LoadedArtifact]) -> Path:
    rows: list[dict[str, Any]] = []
    row_by_key: dict[str, int] = {}
    loaded_ordered = sorted(artifacts, key=sort_key_for_loaded)
    has_formula_metavariable_row = any(
        str(item.get("registry_id") or "") == "propositional_logic.formula_metavariables"
        or str(item.get("symbol") or item.get("latex") or "").strip() == r"\varphi,\psi,\chi,\theta"
        for loaded in loaded_ordered
        for item in metadata_items(loaded.data, "notations")
    )
    for loaded in loaded_ordered:
        label = str(loaded.data.get("label", ""))
        for item in metadata_items(loaded.data, "notations"):
            symbol = str(item.get("symbol") or item.get("latex") or "").strip().replace(r"\mathbb B", r"\mathbb{B}")
            if not symbol:
                continue
            if has_formula_metavariable_row and symbol in {r"\varphi", r"\psi", r"\chi", r"\theta", r"\varphi,\psi"}:
                continue
            key = notation_dedupe_key(symbol, item)
            row = {
                "symbol": symbol,
                "name": item.get("name", ""),
                "meaning": item.get("meaning", ""),
                "introduced_by": item.get("introduced_by") or label,
                "scope": item.get("scope", "chapter" if item.get("_role") == "defines" else "global"),
                "status": item.get("status", "canonical" if item.get("registry_id") else "local"),
                "_specificity": notation_specificity(symbol, item),
            }
            if key in row_by_key:
                index = row_by_key[key]
                if row["_specificity"] > rows[index].get("_specificity", 0):
                    rows[index] = row
                continue
            row_by_key[key] = len(rows)
            rows.append(row)
    path = notation_page_path(chapter)
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "\\section{Notation and Conventions}",
        "",
        "% BEGIN GENERATED ARTIFACT: notation-page",
        "\\begin{longtable}{p{0.16\\textwidth}p{0.20\\textwidth}p{0.34\\textwidth}p{0.16\\textwidth}}",
        "\\textbf{Symbol} & \\textbf{Name} & \\textbf{Meaning} & \\textbf{Introduced by}\\\\",
        "\\hline",
    ]
    for row in rows:
        introduced = row["introduced_by"]
        lines.append(
            f"\\({row['symbol']}\\) & {row['name']} & {row['meaning']} "
            f"({row['scope']}, {row['status']}) & \\hyperref[{introduced}]{{{introduced}}}\\\\"
        )
    lines.extend([
        "\\end{longtable}",
        "% END GENERATED ARTIFACT: notation-page",
        "",
    ])
    path.write_text("\n".join(lines), encoding="utf-8", newline="\n")
    return path


def rewrite_notes_index(chapter: str, topics: set[str]) -> None:
    root = chapter_root(chapter)
    lines = ["% Notes index generated by artifact registry.", ""]
    notation = notation_page_path(chapter)
    if notation.exists():
        lines.append(f"\\input{{{latex_input(notation)}}}")
        lines.append("")
    for topic in sorted(topics, key=lambda name: (SECTION_ORDER.index(name) if name in SECTION_ORDER else len(SECTION_ORDER), name)):
        topic_index = index_path_for_topic(chapter, topic, "notes")
        if topic_index.exists():
            lines.append(f"\\input{{{latex_input(topic_index)}}}")
    (root / "notes" / "index.tex").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8", newline="\n")


def restatement_env(kind: str) -> str:
    return "theorem*"


def render_proof_stub(loaded: LoadedArtifact) -> str:
    art = loaded.data
    label = art["label"]
    root = label.split(":", 1)[1]
    proof_label = f"prf:{root}"
    title = art.get("title") or title_from_label(label)
    kind_name = art["kind"].capitalize()
    body = canonicalize_generated_text(normalize_content(art.get("body")))
    sketch = normalize_content(art.get("proof_sketch")) or "TODO: record the intended proof structure."
    deps = art.get("dependencies") or []
    if deps:
        deps_items = "\n".join(f"  \\item \\hyperref[{dep}]{{{dep}}}" for dep in deps)
        deps_text = f"\\begin{{itemize}}\n{deps_items}\n\\end{{itemize}}"
    else:
        deps_text = "\\NoLocalDependencies"
    return f"""\\newpage
\\phantomsection
\\label{{{proof_label}}}
\\LRAProofFor{{{label}}}

\\begin{{remark*}}[Return]
\\hyperref[{label}]{{Return to {kind_name} ({title}).}}
\\end{{remark*}}

\\begin{{{restatement_env(art['kind'])}}}[{title}]
{body}
\\end{{{restatement_env(art['kind'])}}}

\\begin{{proof}}
\\textbf{{Professional Standard Proof.}}~
TODO: supply the compact proof.
\\end{{proof}}

\\begin{{proof}}
\\textbf{{Detailed Learning Proof.}}~
TODO: supply the detailed learning proof.
\\end{{proof}}

\\begin{{remark*}}[Proof structure]
{sketch}
\\end{{remark*}}

\\begin{{dependencies}}
{deps_text}
\\end{{dependencies}}

\\clearpage
"""


def build_artifacts(artifacts: list[LoadedArtifact]) -> dict[str, Any]:
    result = {"statements": [], "proofs": []}
    by_chapter_topic: set[tuple[str, str]] = set()
    for loaded in artifacts:
        art = loaded.data
        chapter = loaded.chapter
        topic = loaded.topic
        by_chapter_topic.add((chapter, topic))
        notes_path = topic_notes_path(chapter, topic)
        prelude = ""
        replace_or_append_generated_block(
            notes_path,
            art["label"],
            render_statement(loaded),
            section_heading=prelude + f"\\section{{{section_title(topic)}}}",
        )
        ensure_input(
            index_path_for_topic(chapter, topic, "notes"),
            notes_path,
            heading=f"\\subsection*{{{section_title(topic)}}}",
        )
        result["statements"].append(str(notes_path))
        if art["kind"] in THEOREM_LIKE and art.get("proof_required", True):
            pf = proof_path(chapter, topic, art["label"])
            replace_or_append_generated_block(pf, f"prf:{art['label'].split(':', 1)[1]}", render_proof_stub(loaded))
            ensure_input(
                index_path_for_topic(chapter, topic, "proofs"),
                pf,
                heading=f"\\subsection*{{{section_title(topic)} Proofs}}",
            )
            ensure_input(chapter_root(chapter) / "proofs" / "index.tex", index_path_for_topic(chapter, topic, "proofs"))
            result["proofs"].append(str(pf))
    for chapter, _topic in by_chapter_topic:
        ensure_base_chapter(chapter)
        all_for_chapter = load_artifacts(chapter)
        notation_path = render_notation_page(chapter, all_for_chapter)
        rewrite_notes_index(chapter, {loaded.topic for loaded in all_for_chapter})
        sync_chapter_yaml(chapter)
    return result


def ensure_base_chapter(chapter: str) -> None:
    root = chapter_root(chapter)
    (root / "notes").mkdir(parents=True, exist_ok=True)
    (root / "proofs" / "notes").mkdir(parents=True, exist_ok=True)
    (root / "exercises").mkdir(parents=True, exist_ok=True)
    for path, text in [
        (root / "index.tex", "\\chapter{Propositional Logic}\n\n\\input{volume-i/propositional-logic/notes/index}\n\n\\clearpage\n\\section*{Proofs}\n\\input{volume-i/propositional-logic/proofs/index}\n\n\\clearpage\n\\input{volume-i/propositional-logic/exercises/index}\n\n\\clearpage\n\\input{volume-i/propositional-logic/capstone}\n"),
        (root / "notes" / "index.tex", "% Notes index generated by artifact registry.\n"),
        (root / "proofs" / "index.tex", "% Proof index generated by artifact registry.\n"),
        (root / "proofs" / "notes" / "index.tex", "% Compatibility index for legacy proof scanner.\n"),
        (root / "exercises" / "index.tex", "% Exercises will be generated separately.\n"),
        (root / "capstone.tex", "% Capstone will be generated separately.\n"),
    ]:
        if not path.exists():
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8", newline="\n")


def sync_chapter_yaml(chapter: str) -> None:
    artifacts = load_artifacts(chapter)
    root = chapter_root(chapter)
    envs = []
    proofs = []
    for loaded in artifacts:
        art = loaded.data
        label = art["label"]
        kind = art["kind"]
        if kind == "remark":
            continue
        proof_file = None
        if kind in THEOREM_LIKE and art.get("proof_required", True):
            proof_file = scanner_rel(proof_path(chapter, loaded.topic, label), root)
            proofs.append({
                "label": f"prf:{label.split(':', 1)[1]}",
                "file": proof_file,
                "theorem_label": label,
            })
        envs.append({
            "label": label,
            "type": KIND_TO_TYPE[kind],
            "file": scanner_rel(topic_notes_path(chapter, loaded.topic), root),
            "display_title": art.get("title") or label,
            "proof_file": proof_file,
        })
    data = safe_read_yaml(root / "chapter.yaml") or {}
    data.update({
        "subject": chapter,
        "display_title": "Propositional Logic" if chapter == "propositional-logic" else chapter,
        "volume": "volume-i",
        "status": "generated-from-artifact-registry",
        "layout": {
            "section_directories": "semantic",
            "ordering": "artifact-registry",
            "proof_layout": "topic-mirrored",
        },
        "environments": envs,
        "proof_files": proofs,
    })
    write_yaml(root / "chapter.yaml", data)


def flatten_registry_ids(data: Any, prefix: str = "") -> set[str]:
    ids: set[str] = set()
    if isinstance(data, dict):
        for key, value in data.items():
            cur = f"{prefix}.{key}" if prefix else str(key)
            ids.add(cur)
            ids.update(flatten_registry_ids(value, cur))
    elif isinstance(data, list):
        for item in data:
            if isinstance(item, dict):
                for key in ("id", "label", "name", "predicate", "symbol"):
                    if key in item:
                        ids.add(str(item[key]))
            ids.update(flatten_registry_ids(item, prefix))
    return ids


def canonical_ids(path: Path) -> set[str]:
    data = safe_read_yaml(path)
    ids = flatten_registry_ids(data)
    if ids or not path.exists():
        return ids
    text = path.read_text(encoding="utf-8", errors="ignore")
    for pattern in (
        r"^\s*-?\s*id:\s*([^\s#]+)",
        r"^\s*-?\s*name:\s*([^\n#]+)",
        r"^\s*([A-Za-z0-9_.-]+):\s*(?:\\|[^\s#]+)",
    ):
        for match in re.finditer(pattern, text, re.MULTILINE):
            ids.add(match.group(1).strip().strip("'\""))
    return ids


def canonical_root() -> Path:
    sibling = REPO_ROOT.parent / "Learning-Real-Analysis"
    return sibling if sibling.exists() else REPO_ROOT


def validate_registries(artifacts: list[LoadedArtifact], strict: bool, allow_new: bool) -> dict[str, Any]:
    root = canonical_root()
    canonical = {
        "predicates": canonical_ids(root / "predicates.yaml"),
        "notation": canonical_ids(root / "notation.yaml"),
        "relations": canonical_ids(root / "relations.yaml"),
    }
    missing = {"predicates": [], "notation": [], "relations": []}
    proposed = {"predicates": [], "notation": [], "relations": []}
    for loaded in artifacts:
        art = loaded.data
        for section in ("predicates", "notations", "relations"):
            target_name = "notation" if section == "notations" else section
            for item in metadata_items(art, section):
                rid = registry_key(item)
                entry = {"artifact": art["label"], **{k: v for k, v in item.items() if not k.startswith("_")}}
                if is_local_metadata(item):
                    continue
                if is_proposed_definition(item):
                    if rid and rid not in canonical[target_name]:
                        proposed[target_name].append(entry)
                    continue
                if rid and rid not in canonical[target_name]:
                    missing[target_name].append(entry)
    if allow_new:
        REPORTS_ROOT.mkdir(exist_ok=True)
        patch_items = {
            name: missing[name] + proposed[name]
            for name in missing
        }
        for name, items in patch_items.items():
            if items:
                write_yaml(REPORTS_ROOT / f"registry_patch.{name}.yaml", {"missing": items})
    if strict and any(missing.values()):
        raise RuntimeError(f"Missing canonical registry entries: {missing}")
    return missing


def cmd_build(args: argparse.Namespace) -> int:
    if args.artifact:
        chapter, topic, label = parse_artifact_key(args.artifact)
        artifacts = [a for a in load_artifacts(chapter, topic) if a.data.get("label") == label]
        if not artifacts:
            raise SystemExit(f"No artifact found for {args.artifact}")
    else:
        artifacts = load_artifacts(args.chapter, args.topic)
    if not artifacts:
        print("No artifacts found to build.", file=sys.stderr)
        return 1
    validate_registries(artifacts, args.strict_registry, args.allow_new_registry_items)
    result = build_artifacts(artifacts)
    print(yaml.safe_dump(result, sort_keys=False))
    return 0


def validate_artifact_shape(loaded: LoadedArtifact) -> list[str]:
    errors = []
    art = loaded.data
    for field in ("label", "kind", "title", "body"):
        if not art.get(field):
            errors.append(f"{loaded.registry_path}: artifact missing {field}")
    if art.get("kind") not in KIND_TO_ENV:
        errors.append(f"{art.get('label')}: unknown kind {art.get('kind')}")
    for section in ("predicates", "notations", "relations"):
        if section not in art:
            errors.append(f"{art.get('label')}: missing {section} metadata")
    errors.extend(detect_notation_drift(loaded))
    return errors


def cmd_validate(args: argparse.Namespace) -> int:
    artifacts = load_artifacts(args.chapter, args.topic)
    errors: list[str] = []
    for loaded in artifacts:
        errors.extend(validate_artifact_shape(loaded))
    missing = validate_registries(artifacts, args.strict_registry, args.allow_new_registry_items)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"Validated {len(artifacts)} artifact(s).")
    if any(missing.values()):
        print("Missing registry entries:")
        print(yaml.safe_dump(missing, sort_keys=False))
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    append = sub.add_parser("append")
    append.add_argument("--registry", required=True)
    append.add_argument("--label", required=True)
    append.add_argument("--kind", choices=sorted(KIND_TO_ENV))
    append.add_argument("--title")
    append.add_argument("--update", action="store_true")
    append.add_argument("--proof-required", dest="proof_required", action=argparse.BooleanOptionalAction)
    for field in ("body", "quantified_form", "interpretation", "predicate_reading", "examples", "non_examples", "contrapositive", "contrapositive_predicate_reading", "negated_form", "negation_predicate_reading", "failure_modes", "readable_decomposition", "failure_mode_decomposition", "proof_sketch"):
        append.add_argument(f"--{field.replace('_', '-')}", dest=field)
    append.set_defaults(func=cmd_append)

    build = sub.add_parser("build")
    build.add_argument("--chapter")
    build.add_argument("--topic")
    build.add_argument("--artifact")
    build.add_argument("--strict-registry", action="store_true")
    build.add_argument("--allow-new-registry-items", action="store_true")
    build.set_defaults(func=cmd_build)

    validate = sub.add_parser("validate")
    validate.add_argument("--chapter", required=True)
    validate.add_argument("--topic")
    validate.add_argument("--strict-registry", action="store_true")
    validate.add_argument("--allow-new-registry-items", action="store_true")
    validate.set_defaults(func=cmd_validate)

    args = parser.parse_args(argv)
    if args.command == "build" and not args.artifact and not args.chapter:
        parser.error("build requires --chapter or --artifact")
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
