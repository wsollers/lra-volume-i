#!/usr/bin/env python3
"""Import ordered artifact payloads into appendable chapter registries."""

from __future__ import annotations

import argparse
import base64
import json
import re
import subprocess
import sys
from copy import deepcopy
from datetime import datetime
from pathlib import Path
from typing import Any

import yaml

import chapter_artifact


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS_ROOT = REPO_ROOT / "artifacts"
REPORTS_ROOT = REPO_ROOT / "reports"

TEXT_FIELDS = (
    "body",
    "quantified_form",
    "standard_quantified_statement",
    "predicate_reading",
    "negated_quantified_statement",
    "negation_predicate_reading",
    "interpretation",
    "readable_decomposition",
    "failure_mode_decomposition",
    "examples",
    "non_examples",
    "contrapositive",
    "negated_form",
    "proof_sketch",
)
FIELD_ALIASES = {
    "standard_quantified_statement": "quantified_form",
    "negated_quantified_statement": "negated_form",
}
VALID_KINDS = set(chapter_artifact.KIND_TO_ENV)
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
NOTATION_REGISTRY_BY_SYMBOL = {
    r"\mathbb B": "propositional_logic.truth_values",
    r"\mathbb{B}": "propositional_logic.truth_values",
    r"\Prop": "propositional_logic.variable_set",
    r"\WFF": "propositional_logic.formula_set",
    r"P,Q,R": "propositional_logic.propositional_variables",
    r"P_1,\ldots,P_n": "propositional_logic.propositional_variable_list",
    r"\varphi": "propositional_logic.formula",
    r"\psi": "propositional_logic.second_formula",
    r"\chi": "propositional_logic.third_formula",
    r"\theta": "propositional_logic.fourth_formula",
    r"\varphi,\psi": "propositional_logic.formula_metavariables",
    r"\varphi,\psi,\chi,\theta": "propositional_logic.formula_metavariables",
    r"\neg": "propositional_logic.negation",
    r"\land": "propositional_logic.conjunction",
    r"\lor": "propositional_logic.disjunction",
    r"\to": "propositional_logic.conditional",
    r"\leftrightarrow": "propositional_logic.biconditional",
    r"\circ": "propositional_logic.generic_binary_connective",
    r"\operatorname{Tree}(\varphi)": "propositional_logic.syntax_tree",
    r"\operatorname{Var}(\varphi)": "propositional_logic.formula_variable_set",
    r"\operatorname{Sub}(\varphi)": "propositional_logic.subformula_set",
    r"\operatorname{depth}(\varphi)": "propositional_logic.formula_depth",
    r"\operatorname{conn}(\varphi)": "propositional_logic.connective_count",
    r"v": "propositional_logic.truth_assignment",
    r"w": "propositional_logic.second_truth_assignment",
    r"v,w": "propositional_logic.truth_assignment",
    r"\widehat v": "propositional_logic.extended_truth_assignment",
    r"\widehat w": "propositional_logic.second_extended_truth_assignment",
    r"\widehat v,\widehat w": "propositional_logic.extended_truth_assignment",
    r"v\models\varphi": "propositional_logic.satisfaction_formula",
    r"v\models\Gamma": "propositional_logic.satisfaction_set",
    r"\models\varphi": "propositional_logic.validity_formula",
    r"\Gamma": "propositional_logic.premise_set",
    r"\Gamma\models\varphi": "propositional_logic.semantic_consequence_formula",
    r"\varphi\equiv\psi": "propositional_logic.logical_equivalence_formula",
    r"\equiv": "propositional_logic.logical_equivalence",
    r"\top": "propositional_logic.truth_constant_top",
    r"\bot": "propositional_logic.truth_constant_bottom",
    r"C[-]": "propositional_logic.formula_context",
    r"C[\varphi]": "propositional_logic.formula_context_substitution",
    r"f:\mathbb{B}^n\to\mathbb{B}": "propositional_logic.boolean_function",
    r"f_\varphi": "propositional_logic.truth_function_formula",
    r"\neg,\land,\lor,\to,\leftrightarrow": "propositional_logic.standard_connectives",
}
NOTATION_NAMES = {
    r"\mathbb B": ("truth-value set", "the set of truth values"),
    r"\mathbb{B}": ("truth-value set", "the set of truth values"),
    r"\Prop": ("propositional variable set", "the set of propositional variables"),
    r"\WFF": ("well-formed formula set", "the set of propositional well-formed formulas"),
    r"\varphi": ("formula metavariable", "a metavariable ranging over formulas"),
    r"\psi": ("second formula metavariable", "a metavariable ranging over formulas"),
    r"\chi": ("third formula metavariable", "a metavariable ranging over formulas"),
    r"\theta": ("fourth formula metavariable", "a metavariable ranging over formulas"),
    r"\neg": ("negation", "unary propositional connective"),
    r"\land": ("conjunction", "binary propositional connective"),
    r"\lor": ("disjunction", "binary propositional connective"),
    r"\to": ("conditional", "binary propositional connective"),
    r"\leftrightarrow": ("biconditional", "binary propositional connective"),
    r"\circ": ("generic binary connective", "an arbitrary primitive binary propositional connective"),
    r"v": ("truth assignment", "truth assignment on propositional variables"),
    r"w": ("second truth assignment", "truth assignment on propositional variables"),
    r"\widehat v": ("extended truth assignment", "unique extension to formulas"),
    r"\widehat w": ("second extended truth assignment", "unique extension to formulas"),
    r"\Gamma": ("set of premise formulas", "a set of propositional formulas"),
    r"\models\varphi": ("tautology notation", "formula valid under every truth assignment"),
    r"v\models\varphi": ("satisfaction of a formula", "truth assignment satisfies a formula"),
    r"v\models\Gamma": ("satisfaction of a set", "truth assignment satisfies each formula in a set"),
    r"\Gamma\models\varphi": ("semantic consequence", "semantic consequence from premises to conclusion"),
    r"\varphi\equiv\psi": ("logical equivalence", "same truth value under every truth assignment"),
    r"\equiv": ("logical equivalence symbol", "logical equivalence relation between formulas"),
    r"\top": ("tautological formula", "a formula chosen as a true constant"),
    r"\bot": ("contradictory formula", "a formula chosen as a false constant"),
    r"C[-]": ("formula context", "a one-hole propositional formula context"),
    r"C[\varphi]": ("context substitution", "formula obtained by filling a context with a formula"),
    r"f:\mathbb{B}^n\to\mathbb{B}": ("n-ary Boolean function", "function from truth-value tuples to a truth value"),
    r"f_\varphi": ("truth function induced by a formula", "Boolean function represented by a formula"),
}


def canonical_notation_symbol(symbol: str) -> str:
    return symbol.replace(r"\mathbb B", r"\mathbb{B}")


def format_predicate_names(text: str) -> str:
    for name in PREDICATE_NAMES:
        text = re.sub(
            rf"(?<!operatorname{{)\b{name}\s*\(",
            rf"\\operatorname{{{name}}}(",
            text,
        )
    return text


def read_payload(path: Path, chapter: str | None, topic: str | None) -> tuple[str, str, list[dict[str, Any]]]:
    text = path.read_text(encoding="utf-8")
    if path.suffix.lower() == ".jsonl":
        artifacts = [json.loads(line) for line in text.splitlines() if line.strip()]
        inferred_chapter = chapter or first_value(artifacts, "chapter")
        inferred_topic = topic or first_value(artifacts, "topic")
        if not inferred_chapter or not inferred_topic:
            raise ValueError("JSONL payloads require --chapter/--topic or per-artifact chapter/topic fields.")
        return inferred_chapter, inferred_topic, artifacts

    data = json.loads(text)
    if not isinstance(data, dict):
        raise ValueError("JSON payload must be an object.")
    inferred_chapter = chapter or data.get("chapter")
    inferred_topic = topic or data.get("topic")
    artifacts = data.get("artifacts")
    if not inferred_chapter or not inferred_topic:
        raise ValueError("JSON payload must provide chapter and topic, or use --chapter/--topic.")
    if not isinstance(artifacts, list):
        raise ValueError("JSON payload must contain an artifacts list.")
    return str(inferred_chapter), str(inferred_topic), artifacts


def first_value(items: list[dict[str, Any]], key: str) -> str | None:
    for item in items:
        value = item.get(key)
        if value:
            return str(value)
    return None


def decode_text_fields(artifact: dict[str, Any], prefer_b64: bool) -> dict[str, Any]:
    decoded = deepcopy(artifact)
    for source in TEXT_FIELDS:
        target = FIELD_ALIASES.get(source, source)
        plain_present = source in decoded
        b64_key = f"{source}_b64"
        b64_present = b64_key in decoded
        if plain_present and b64_present and not prefer_b64:
            raise ValueError(f"{artifact_label(artifact)}: both {source} and {b64_key} are present.")
        if b64_present and (prefer_b64 or not plain_present):
            decoded[target] = format_predicate_names(base64.b64decode(str(decoded[b64_key])).decode("utf-8"))
        elif plain_present and source != target:
            decoded[target] = format_predicate_names(str(decoded[source]))
        elif plain_present and isinstance(decoded.get(source), str):
            decoded[source] = format_predicate_names(str(decoded[source]))
        decoded.pop(b64_key, None)
        if source != target:
            decoded.pop(source, None)
    return decoded


def artifact_label(artifact: dict[str, Any]) -> str:
    return str(artifact.get("label") or "<unlabeled>")


def normalize_metadata(artifact: dict[str, Any]) -> None:
    for section in ("predicates", "notations", "relations"):
        value = artifact.setdefault(section, {})
        if value is None:
            artifact[section] = {"defines": [], "uses": []}
            continue
        if not isinstance(value, dict):
            raise ValueError(f"{artifact_label(artifact)}: {section} metadata must be an object.")
        value.setdefault("defines", [])
        value.setdefault("uses", [])
        for role in ("defines", "uses"):
            if not isinstance(value[role], list):
                raise ValueError(f"{artifact_label(artifact)}: {section}.{role} must be a list.")
            for item in value[role]:
                if not isinstance(item, (dict, str)):
                    raise ValueError(f"{artifact_label(artifact)}: {section}.{role} entries must be objects or strings.")
                if isinstance(item, dict):
                    enrich_metadata_item(section, item)


def enrich_metadata_item(section: str, item: dict[str, Any]) -> None:
    if section == "notations":
        symbol = str(item.get("symbol") or item.get("latex") or "")
        normalized = canonical_notation_symbol(symbol)
        if symbol and normalized != symbol:
            if item.get("symbol") == symbol:
                item["symbol"] = normalized
            if item.get("latex") == symbol:
                item["latex"] = normalized
        if item.get("registry_id"):
            return
        registry_id = NOTATION_REGISTRY_BY_SYMBOL.get(symbol)
        registry_id = registry_id or NOTATION_REGISTRY_BY_SYMBOL.get(normalized)
        if registry_id:
            item["registry_id"] = registry_id
    if section == "relations" and not item.get("registry_id"):
        item.setdefault("status", "local")


def add_detected_notation_uses(artifact: dict[str, Any]) -> None:
    text = "\n".join(str(artifact.get(field, "")) for field in TEXT_FIELDS)
    notations = artifact.setdefault("notations", {"defines": [], "uses": []})
    declared: set[str] = set()
    for role in ("defines", "uses"):
        for item in notations.get(role, []) or []:
            if not isinstance(item, dict):
                continue
            symbol = str(item.get("symbol") or item.get("latex") or "")
            normalized = canonical_notation_symbol(symbol)
            declared.add(normalized)
            for part in normalized.split(","):
                if part.strip():
                    declared.add(part.strip())

    for symbol, registry_id in NOTATION_REGISTRY_BY_SYMBOL.items():
        normalized = canonical_notation_symbol(symbol)
        if normalized in declared or symbol in declared:
            continue
        if symbol in {r"P,Q,R", r"P_1,\ldots,P_n", r"\varphi,\psi", r"\varphi,\psi,\chi,\theta"}:
            continue
        if symbol not in text and normalized not in text:
            continue
        name, meaning = NOTATION_NAMES.get(symbol, (symbol, symbol))
        notations.setdefault("uses", []).append({
            "symbol": normalized,
            "name": name,
            "meaning": meaning,
            "scope": "global",
            "status": "canonical",
            "registry_id": registry_id,
        })
        declared.add(normalized)


def validate_artifacts(chapter: str, topic: str, artifacts: list[dict[str, Any]]) -> None:
    seen: set[str] = set()
    for artifact in artifacts:
        if not isinstance(artifact, dict):
            raise ValueError("Each artifact must be an object.")
        for field in ("label", "kind", "title"):
            if not artifact.get(field):
                raise ValueError(f"{artifact_label(artifact)}: missing required field {field}.")
        label = str(artifact["label"])
        if label in seen:
            raise ValueError(f"Duplicate label in payload: {label}")
        seen.add(label)
        if artifact["kind"] not in VALID_KINDS:
            raise ValueError(f"{label}: invalid kind {artifact['kind']!r}.")
        if not isinstance(artifact.get("proof_required"), bool):
            raise ValueError(f"{label}: proof_required must be boolean.")
        if artifact.get("chapter") and artifact["chapter"] != chapter:
            raise ValueError(f"{label}: artifact chapter does not match payload chapter.")
        if artifact.get("topic") and artifact["topic"] != topic:
            raise ValueError(f"{label}: artifact topic does not match payload topic.")
        normalize_metadata(artifact)
        add_detected_notation_uses(artifact)


def registry_path(chapter: str, topic: str) -> Path:
    return ARTIFACTS_ROOT / chapter / f"{topic}.yaml"


def default_registry(chapter: str, topic: str) -> dict[str, Any]:
    return {
        "schema_version": 1,
        "chapter": chapter,
        "topic": topic,
        "encoding": "utf-8",
        "content_format": "latex",
        "artifacts": [],
    }


def read_registry(path: Path, chapter: str, topic: str) -> dict[str, Any]:
    if not path.exists():
        return default_registry(chapter, topic)
    data = chapter_artifact.safe_read_yaml(path) or default_registry(chapter, topic)
    if data.get("chapter") != chapter or data.get("topic") != topic:
        raise ValueError(f"{path}: chapter/topic does not match import target.")
    data.setdefault("schema_version", 1)
    data.setdefault("encoding", "utf-8")
    data.setdefault("content_format", "latex")
    data.setdefault("artifacts", [])
    return data


def merge_artifacts(
    existing: list[dict[str, Any]],
    incoming: list[dict[str, Any]],
    update: bool,
    move_to_input_order: bool,
) -> list[dict[str, Any]]:
    existing_by_label = {artifact.get("label"): artifact for artifact in existing}
    incoming_labels = [artifact["label"] for artifact in incoming]
    collisions = [label for label in incoming_labels if label in existing_by_label]
    if collisions and not update:
        raise ValueError("Artifact label(s) already exist: " + ", ".join(collisions))

    if move_to_input_order:
        incoming_by_label = {artifact["label"]: artifact for artifact in incoming}
        merged = [incoming_by_label[label] for label in incoming_labels]
        merged.extend(artifact for artifact in existing if artifact.get("label") not in incoming_by_label)
        return merged

    incoming_by_label = {artifact["label"]: artifact for artifact in incoming}
    merged: list[dict[str, Any]] = []
    replaced: set[str] = set()
    for artifact in existing:
        label = artifact.get("label")
        if label in incoming_by_label:
            merged.append(incoming_by_label[label])
            replaced.add(str(label))
        else:
            merged.append(artifact)
    merged.extend(artifact for artifact in incoming if artifact["label"] not in replaced and artifact["label"] not in existing_by_label)
    return merged


def write_registry(path: Path, chapter: str, topic: str, artifacts: list[dict[str, Any]]) -> None:
    data = default_registry(chapter, topic)
    data["artifacts"] = artifacts
    chapter_artifact.write_yaml(path, data)


def loaded_for_registry(path: Path, chapter: str, topic: str, artifacts: list[dict[str, Any]]) -> list[chapter_artifact.LoadedArtifact]:
    return [
        chapter_artifact.LoadedArtifact(path, chapter, topic, artifact, order)
        for order, artifact in enumerate(artifacts)
    ]


def run_command(command: list[str], output_file: Path) -> int:
    output_file.parent.mkdir(parents=True, exist_ok=True)
    with output_file.open("w", encoding="utf-8", newline="\n") as f:
        f.write("COMMAND: " + " ".join(command) + "\n\n")
        proc = subprocess.run(
            command,
            cwd=REPO_ROOT,
            text=True,
            encoding="utf-8",
            errors="replace",
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
        f.write(proc.stdout)
        return proc.returncode


def write_skip(output_file: Path, reason: str) -> None:
    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(f"SKIPPED: {reason}\n", encoding="utf-8", newline="\n")


def run_build(chapter: str, topic: str, allow_new: bool, strict: bool) -> int:
    cmd = [sys.executable, "tools/chapter_artifact.py", "build", "--chapter", chapter, "--topic", topic]
    if allow_new:
        cmd.append("--allow-new-registry-items")
    if strict:
        cmd.append("--strict-registry")
    return subprocess.run(cmd, cwd=REPO_ROOT).returncode


def run_validate(chapter: str, allow_new: bool, strict: bool) -> int:
    cmd = [sys.executable, "tools/chapter_artifact.py", "validate", "--chapter", chapter]
    if allow_new:
        cmd.append("--allow-new-registry-items")
    if strict:
        cmd.append("--strict-registry")
    return subprocess.run(cmd, cwd=REPO_ROOT).returncode


def run_audit_local(chapter: str) -> Path:
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    report_dir = REPORTS_ROOT / "propositional-logic-generation-audit" / timestamp
    target = str(REPO_ROOT / "volume-i" / chapter)
    commands = [
        ("01-artifact-validate", [sys.executable, "tools/chapter_artifact.py", "validate", "--chapter", chapter, "--strict-registry", "--allow-new-registry-items"]),
        ("02-trueup", [sys.executable, "-m", "constitution.auditor", "--repoDir", r"F:\repos\Learning-Real-Analysis", "trueup", "chapter", target]),
        ("04-box-color-audit", [sys.executable, "-m", "constitution.auditor", "--repoDir", str(REPO_ROOT), "audit", "box-colors", target]),
        ("05-proof-layout-audit", [sys.executable, r"F:\repos\lra-governance\tools\governance\audit_proof_layout.py", "--root", target, "--format", "text"]),
        ("06-latexmk", ["latexmk", "-lualatex", "-interaction=nonstopmode", "-halt-on-error", "main.tex"]),
    ]
    summary = []
    for name, command in commands:
        if name == "04-box-color-audit":
            write_skip(
                report_dir / "03-symbol-audit-local.txt",
                "constitution.auditor audit symbols is AI-backed in this checkout even without -ai codex; "
                "local deterministic registry coverage is provided by 01-artifact-validate --strict-registry.",
            )
            summary.append({
                "name": "03-symbol-audit-local",
                "status": "skipped",
                "reason": "No deterministic/local symbol audit is available without invoking an AI provider.",
            })
        code = run_command(command, report_dir / f"{name}.txt")
        summary.append({"name": name, "exit_code": code, "command": command})
    (report_dir / "summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8", newline="\n")
    return report_dir


def run_audit_ai(chapter: str) -> Path:
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S-ai")
    report_dir = REPORTS_ROOT / "propositional-logic-generation-audit" / timestamp
    target = str(REPO_ROOT / "volume-i" / chapter)
    commands = [
        ("01-symbol-audit-ai", [sys.executable, "-m", "constitution.auditor", "--repoDir", r"F:\repos\Learning-Real-Analysis", "-ai", "codex", "audit", "symbols", target]),
        ("02-chapter-audit-ai", [sys.executable, "-m", "constitution.auditor", "--repoDir", r"F:\repos\Learning-Real-Analysis", "-ai", "codex", "audit", "chapter", target]),
    ]
    summary = []
    for name, command in commands:
        code = run_command(command, report_dir / f"{name}.txt")
        summary.append({"name": name, "exit_code": code, "command": command})
    (report_dir / "summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8", newline="\n")
    return report_dir


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("payload")
    parser.add_argument("--chapter")
    parser.add_argument("--topic")
    parser.add_argument("--prefer-b64", action="store_true")
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--update", action="store_true")
    parser.add_argument("--move-to-input-order", action="store_true")
    parser.add_argument("--strict-registry", action="store_true")
    parser.add_argument("--allow-new-registry-items", action="store_true")
    parser.add_argument("--build", action="store_true")
    parser.add_argument("--validate", action="store_true")
    parser.add_argument("--audit", action="store_true", help="Deprecated alias for --audit-local.")
    parser.add_argument("--audit-local", action="store_true", help="Run deterministic local audits only.")
    parser.add_argument("--audit-ai", action="store_true", help="Run optional AI-backed audits.")
    parser.add_argument("--audit-full", action="store_true", help="Run local audits followed by optional AI-backed audits.")
    args = parser.parse_args(argv)

    payload_path = Path(args.payload).resolve()
    chapter, topic, raw_artifacts = read_payload(payload_path, args.chapter, args.topic)
    artifacts = [decode_text_fields(artifact, args.prefer_b64) for artifact in raw_artifacts]
    for artifact in artifacts:
        artifact.pop("chapter", None)
        artifact.pop("topic", None)
    validate_artifacts(chapter, topic, artifacts)

    target = registry_path(chapter, topic)
    loaded_incoming = loaded_for_registry(target, chapter, topic, artifacts)
    if args.dry_run or not args.write:
        missing = chapter_artifact.validate_registries(
            loaded_incoming,
            args.strict_registry,
            args.allow_new_registry_items,
        )
        print(f"Target registry: {target}")
        print("Artifacts:")
        for artifact in artifacts:
            print(f"- {artifact['label']}")
        if any(missing.values()):
            print("Missing registry entries:")
            print(yaml.safe_dump(missing, sort_keys=False))
        print("Dry run: no files written.")
        return 0

    registry = read_registry(target, chapter, topic)
    merged = merge_artifacts(registry.get("artifacts", []), artifacts, args.update, args.move_to_input_order)
    loaded = loaded_for_registry(target, chapter, topic, merged)
    missing = chapter_artifact.validate_registries(loaded, args.strict_registry, args.allow_new_registry_items)

    print(f"Target registry: {target}")
    print("Artifacts:")
    for artifact in artifacts:
        print(f"- {artifact['label']}")
    if any(missing.values()):
        print("Missing registry entries:")
        print(yaml.safe_dump(missing, sort_keys=False))

    write_registry(target, chapter, topic, merged)
    print(f"Wrote {target}")

    if args.build and run_build(chapter, topic, args.allow_new_registry_items, args.strict_registry) != 0:
        return 1
    if args.validate and run_validate(chapter, args.allow_new_registry_items, args.strict_registry) != 0:
        return 1
    if args.audit or args.audit_local or args.audit_full:
        report_dir = run_audit_local(chapter)
        print(f"Local audit reports: {report_dir}")
    if args.audit_ai or args.audit_full:
        report_dir = run_audit_ai(chapter)
        print(f"AI audit reports: {report_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
