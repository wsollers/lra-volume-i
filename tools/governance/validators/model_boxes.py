from __future__ import annotations

import re
from pathlib import Path

from core.finding import Finding, finding
from core.tex import line_at, read_text, strip_latex_comments


CHAPTER_REL = Path("volume-i/propositional-logic")
NOTES_INDEX_REL = CHAPTER_REL / "notes/index.tex"
MODEL_INDEX_REL = CHAPTER_REL / "notes/model/index.tex"
MODEL_FILE_REL = CHAPTER_REL / "notes/model/model-propositional-logic.tex"

MODEL_LABEL = "model:classical-propositional-logic"

REQUIRED_DEPENDS = {
    "Propositional Language",
    "Truth Value",
    "Truth Assignment",
    "Extension of a Truth Assignment to Formulas",
    "Satisfaction of a Formula",
    "Satisfaction of a Set of Formulas",
    "Logical Consequence",
    "Unique Extension of a Truth Assignment",
}

REQUIRED_ENVIRONMENTS = {
    "modelsorts",
    "modelconstants",
    "modelarity",
    "modelfunctions",
    "modelrelations",
    "modelsemantics",
    "modelbridge",
    "modelaxioms",
    "modelconsequences",
}

REQUIRED_MACROS = {
    r"\modelsort": 3,
    r"\modelconstant": 2,
    r"\arity": 5,
    r"\modelfunction": 5,
    r"\modelrelation": 3,
    r"\modelclause": 4,
    r"\bridgeclause": 6,
    r"\modelaxiom": 1,
    r"\modelconsequence": 1,
}

REQUIRED_TOKENS = {
    r"\Prop",
    r"\WFF",
    r"\mathbb{B}",
    r"\False",
    r"\True",
    r"\neg_{\WFF}",
    r"\land_{\WFF}",
    r"\lor_{\WFF}",
    r"\to_{\WFF}",
    r"\leftrightarrow_{\WFF}",
    r"\neg^{\mathbb{B}}",
    r"\land^{\mathbb{B}}",
    r"\lor^{\mathbb{B}}",
    r"\to^{\mathbb{B}}",
    r"\leftrightarrow^{\mathbb{B}}",
    r"\widehat v",
    r"\Gamma\models\varphi",
}

MODEL_BLOCK_RE = re.compile(
    r"\\begin\{modelbox\}\{[^{}]*\}\s*"
    r"\\begin\{model\}\[Classical Propositional Logic\]\\label\{"
    + re.escape(MODEL_LABEL)
    + r"\}"
    r"(?P<body>[\s\S]*?)"
    r"\\end\{model\}\s*\\end\{modelbox\}",
)
DEPENDS_RE = re.compile(r"\\modeldepends\{(?P<body>[\s\S]*?)\}", re.MULTILINE)
MODEL_CONSTANT_RE = re.compile(r"\\modelconstant\{[^{}]*\}\{(?P<name>[^{}]*)\}")
LABEL_ID_RE = re.compile(r"\b(?:def|thm|lem|prop|cor|ax|model):[A-Za-z0-9_.:-]+")


def validate(volume_root: Path) -> list[Finding]:
    findings: list[Finding] = []
    chapter_root = volume_root / CHAPTER_REL
    if not chapter_root.exists():
        return findings

    _validate_routing(volume_root, findings)
    model_file = volume_root / MODEL_FILE_REL
    if not model_file.exists():
        findings.append(
            finding(
                "missing_propositional_logic_model_file",
                "Propositional logic must include a first model-theoretic model-box document.",
                model_file,
                volume_root,
            )
        )
        return findings

    raw_text = read_text(model_file)
    text = strip_latex_comments(raw_text)
    _validate_model_file(volume_root, model_file, text, findings)
    return findings


def _validate_routing(volume_root: Path, findings: list[Finding]) -> None:
    notes_index = volume_root / NOTES_INDEX_REL
    model_index = volume_root / MODEL_INDEX_REL

    if not notes_index.exists():
        return
    notes_text = strip_latex_comments(read_text(notes_index))
    route = r"\input{volume-i/propositional-logic/notes/model/index}"
    if route not in notes_text:
        findings.append(
            finding(
                "propositional_logic_model_not_routed",
                "Route the propositional-logic model section from notes/index.tex.",
                notes_index,
                volume_root,
            )
        )
    first_input = re.search(r"\\input\{[^{}]+\}", notes_text)
    if first_input and first_input.group(0) != route:
        findings.append(
            finding(
                "propositional_logic_model_not_first",
                "The model-theoretic section must be the first routed propositional-logic notes section.",
                notes_index,
                volume_root,
                line_at(notes_text, first_input.start()),
            )
        )

    if not model_index.exists():
        findings.append(
            finding(
                "missing_propositional_logic_model_index",
                "Create notes/model/index.tex to route the model-box document.",
                model_index,
                volume_root,
            )
        )
        return

    model_index_text = strip_latex_comments(read_text(model_index))
    if r"\section{Model-Theoretic View}" not in model_index_text:
        findings.append(
            finding(
                "propositional_logic_model_section_title",
                r"Use \section{Model-Theoretic View} for the model section.",
                model_index,
                volume_root,
            )
        )
    if r"\input{volume-i/propositional-logic/notes/model/model-propositional-logic}" not in model_index_text:
        findings.append(
            finding(
                "propositional_logic_model_file_not_routed",
                "Route model-propositional-logic.tex from notes/model/index.tex.",
                model_index,
                volume_root,
            )
        )


def _validate_model_file(volume_root: Path, path: Path, text: str, findings: list[Finding]) -> None:
    if r"\begin{tcolorbox}" in text:
        findings.append(
            finding(
                "raw_model_tcolorbox",
                r"Use \begin{modelbox} and model component macros; do not hand-roll model boxes with tcolorbox.",
                path,
                volume_root,
                line_at(text, text.find(r"\begin{tcolorbox}")),
            )
        )

    matches = list(MODEL_BLOCK_RE.finditer(text))
    if len(matches) != 1:
        findings.append(
            finding(
                "invalid_propositional_logic_model_box_shape",
                "The propositional-logic model document must contain exactly one modelbox wrapping exactly one labeled model environment.",
                path,
                volume_root,
            )
        )
        return

    body = matches[0].group("body")
    _validate_depends(volume_root, path, body, findings)
    _validate_required_environments(volume_root, path, body, findings)
    _validate_required_macros(volume_root, path, body, findings)
    _validate_required_tokens(volume_root, path, body, findings)
    _validate_visible_names(volume_root, path, body, findings)


def _validate_depends(volume_root: Path, path: Path, body: str, findings: list[Finding]) -> None:
    match = DEPENDS_RE.search(body)
    if not match:
        findings.append(
            finding(
                "missing_model_depends",
                r"Model boxes must declare dependencies with \modeldepends{...}.",
                path,
                volume_root,
            )
        )
        return
    declared = {part.strip() for part in match.group("body").replace("\n", " ").split(",") if part.strip()}
    missing = sorted(REQUIRED_DEPENDS - declared)
    if missing:
        findings.append(
            finding(
                "incomplete_model_depends",
                "The propositional-logic model is missing dependency term names: " + ", ".join(missing),
                path,
                volume_root,
                line_at(body, match.start()),
            )
        )


def _validate_visible_names(volume_root: Path, path: Path, body: str, findings: list[Finding]) -> None:
    depends = DEPENDS_RE.search(body)
    if depends and LABEL_ID_RE.search(depends.group("body")):
        findings.append(
            finding(
                "model_depends_uses_label_ids",
                r"\modeldepends must render term/result names, not def:/thm: label ids.",
                path,
                volume_root,
                line_at(body, depends.start()),
            )
        )

    for match in MODEL_CONSTANT_RE.finditer(body):
        if LABEL_ID_RE.search(match.group("name")):
            findings.append(
                finding(
                    "model_constant_uses_label_id",
                    r"\modelconstant provenance must render a term name, not a def: label id.",
                    path,
                    volume_root,
                    line_at(body, match.start()),
                )
            )


def _validate_required_environments(volume_root: Path, path: Path, body: str, findings: list[Finding]) -> None:
    for env in sorted(REQUIRED_ENVIRONMENTS):
        begin = rf"\begin{{{env}}}"
        end = rf"\end{{{env}}}"
        if begin not in body or end not in body:
            findings.append(
                finding(
                    "missing_model_component_environment",
                    f"Model box is missing required component environment {env}.",
                    path,
                    volume_root,
                )
            )


def _validate_required_macros(volume_root: Path, path: Path, body: str, findings: list[Finding]) -> None:
    for macro, minimum in sorted(REQUIRED_MACROS.items()):
        count = body.count(macro)
        if count < minimum:
            findings.append(
                finding(
                    "insufficient_model_component_macro_usage",
                    f"Model box must use {macro} at least {minimum} time(s); found {count}.",
                    path,
                    volume_root,
                )
            )


def _validate_required_tokens(volume_root: Path, path: Path, body: str, findings: list[Finding]) -> None:
    missing = sorted(token for token in REQUIRED_TOKENS if token not in body)
    if missing:
        findings.append(
            finding(
                "missing_model_required_content",
                "Model box is missing required syntax/semantics content: " + ", ".join(missing),
                path,
                volume_root,
            )
        )
