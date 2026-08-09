from __future__ import annotations

import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "output" / "pdf"
TEX_PATH = OUT_DIR / "set-theory-proof-restart.tex"
PDF_PATH = OUT_DIR / "set-theory-proof-restart.pdf"

STUDY_SEQUENCE = [
    ("axiom", "ax:axiomatic-equality-reflexivity"),
    ("axiom", "ax:axiomatic-equality-substitution"),
    ("axiom", "ax:extensionality"),
    ("axiom", "ax:empty-set"),
    ("axiom", "ax:pairing"),
    ("axiom", "ax:union"),
    ("axiom", "ax:power-set"),
    ("axiom", "ax:infinity"),
    ("axiom", "ax:separation"),
    ("axiom", "ax:replacement"),
    ("axiom", "ax:foundation"),
    ("axiom", "ax:choice"),
    ("definition", "def:set-membership"),
    ("definition", "def:subset"),
    ("definition", "def:proper-subset"),
    ("definition", "def:set-equality"),
    ("theorem", "thm:empty-set-exists-unique"),
    ("definition", "def:empty-set"),
    ("theorem", "thm:pairing-output-exists-unique"),
    ("theorem", "thm:union-output-exists-unique"),
    ("theorem", "cor:binary-union-exists-unique"),
    ("definition", "def:union"),
    ("theorem", "thm:separation-output-exists-unique"),
    ("theorem", "cor:intersection-exists-unique"),
    ("definition", "def:intersection"),
    ("theorem", "cor:set-difference-exists-unique"),
    ("definition", "def:set-difference"),
    ("theorem", "cor:symmetric-difference-exists-unique"),
    ("definition", "def:sym-diff"),
    ("theorem", "cor:relative-complement-exists-unique"),
    ("definition", "def:complement"),
    ("theorem", "thm:power-set-output-exists-unique"),
    ("definition", "def:power-set"),
    ("definition", "def:cartesian-product"),
    ("definition", "def:inclusion-monotone-set-operation"),
    ("definition", "def:inclusion-antitone-set-operation"),
    ("theorem", "thm:union-monotone-inclusion"),
    ("theorem", "thm:intersection-monotone-inclusion"),
    ("theorem", "thm:power-set-monotone-inclusion"),
    ("theorem", "thm:complement-antitone-inclusion"),
    ("theorem", "thm:set-difference-monotone-left"),
    ("theorem", "thm:set-difference-antitone-right"),
    ("definition", "def:indexed-family"),
    ("definition", "def:indexed-union"),
    ("definition", "def:indexed-intersection"),
    ("theorem", "thm:de-morgan"),
    ("theorem", "thm:indexed-de-morgan"),
    ("definition", "def:set-duality"),
    ("theorem", "cor:set-duality"),
    ("theorem", "thm:commutativity"),
    ("theorem", "thm:associativity"),
    ("theorem", "thm:distributivity"),
    ("theorem", "thm:indexed-distributivity"),
    ("theorem", "thm:identity-absorption"),
    ("theorem", "thm:involution"),
    ("definition", "def:cover-full"),
    ("definition", "def:subcover"),
    ("definition", "def:finite-cover"),
    ("definition", "def:fip"),
    ("theorem", "prop:fip-duality"),
]

DEFINITION_SOURCES = [
    ROOT / "volume-i" / "book-logic" / "axiomatic-equality" / "notes" / "logic-with-equality" / "notes-logic-with-equality.tex",
    ROOT / "volume-i" / "book-sets" / "set-theory" / "notes" / "sets" / "notes-foundations.tex",
    ROOT / "volume-i" / "book-sets" / "set-theory" / "notes" / "sets" / "notes-set-operations.tex",
    ROOT / "volume-i" / "book-sets" / "set-theory" / "notes" / "families" / "notes-families.tex",
    ROOT / "volume-i" / "book-sets" / "set-theory" / "notes" / "families" / "notes-set-duality.tex",
    ROOT / "volume-i" / "book-sets" / "set-theory" / "notes" / "families" / "notes-covers-fip.tex",
]

AXIOM_SOURCES = [
    ROOT / "volume-i" / "book-logic" / "axiomatic-equality" / "notes" / "logic-with-equality" / "notes-logic-with-equality.tex",
    ROOT / "volume-i" / "book-sets" / "set-theory" / "notes" / "sets" / "notes-foundations.tex",
]

PROOF_INDEXES = [
    ROOT / "volume-i" / "book-sets" / "set-theory" / "proofs" / "sets" / "index.tex",
    ROOT / "volume-i" / "book-sets" / "set-theory" / "proofs" / "families" / "index.tex",
]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def clean_body(body: str) -> str:
    body = re.sub(r"\\label\{[^}]+\}", "", body)
    body = re.sub(r"\\hyperref\[[^\]]+\]\{(?:Go to proof\.|\\textit\{Go to proof\.\})\}", "", body)
    body = re.sub(r"\n{3,}", "\n\n", body)
    return body.strip()


def latex_text(value: str) -> str:
    return value.replace("_", r"\_")


def find_definition(label: str) -> tuple[str, str]:
    pattern = re.compile(
        r"\\begin\{definition\}\[([^\]]+)\](?P<body>.*?)\\end\{definition\}",
        re.DOTALL,
    )
    for source in DEFINITION_SOURCES:
        text = read(source)
        for match in pattern.finditer(text):
            body = match.group("body")
            if f"\\label{{{label}}}" in body:
                return match.group(1), clean_body(body)
    raise ValueError(f"Definition label not found: {label}")


def find_axiom(label: str) -> tuple[str, str]:
    pattern = re.compile(
        r"\\begin\{axiom\}\[([^\]]+)\](?P<body>.*?)\\end\{axiom\}",
        re.DOTALL,
    )
    for source in AXIOM_SOURCES:
        text = read(source)
        for match in pattern.finditer(text):
            body = match.group("body")
            if f"\\label{{{label}}}" in body:
                return match.group(1), clean_body(body)
    raise ValueError(f"Axiom label not found: {label}")


def proof_files_in_order() -> list[Path]:
    files: list[Path] = []
    for index in PROOF_INDEXES:
        text = read(index)
        for route in re.findall(r"\\input\{([^}]+)\}", text):
            files.append(ROOT / f"{route}.tex")
    return files


def theorem_statement(path: Path) -> tuple[str, str, str, str]:
    text = read(path)
    target = re.search(r"\\LRAProofFor\{([^}]+)\}", text)
    if not target:
        raise ValueError(f"Missing LRAProofFor in {path}")
    env = re.search(
        r"\\begin\{(theorem|corollary|proposition)\*\}\[([^\]]+)\](?P<body>.*?)\\end\{\1\*\}",
        text,
        re.DOTALL,
    )
    if not env:
        raise ValueError(f"Missing theorem-like restatement in {path}")
    kind = env.group(1).capitalize()
    return kind, env.group(2), target.group(1), clean_body(env.group("body"))


def theorem_map() -> dict[str, tuple[str, str, str]]:
    mapped: dict[str, tuple[str, str, str]] = {}
    for path in proof_files_in_order():
        try:
            kind, title, label, body = theorem_statement(path)
        except ValueError:
            continue
        mapped[label] = (kind, title, body)
    return mapped


def build_tex() -> str:
    theorems = theorem_map()
    sequence_blocks = []
    theorem_number = 1
    for item_kind, label in STUDY_SEQUENCE:
        if item_kind == "axiom":
            title, body = find_axiom(label)
            sequence_blocks.append(
                rf"""\begin{{studyblock}}{{Axiom}}{{{title}}}{{{latex_text(label)}}}
{body}
\end{{studyblock}}
"""
            )
        elif item_kind == "definition":
            title, body = find_definition(label)
            sequence_blocks.append(
                rf"""\begin{{studyblock}}{{Definition}}{{{title}}}{{{latex_text(label)}}}
{body}
\end{{studyblock}}
"""
            )
        elif item_kind == "theorem":
            kind, title, body = theorems[label]
            sequence_blocks.append(
                rf"""\begin{{studyblock}}{{{theorem_number}. {kind}}}{{{title}}}{{{latex_text(label)}}}
{body}
\end{{studyblock}}
"""
            )
            theorem_number += 1
        else:
            raise ValueError(f"Unknown study sequence item kind: {item_kind}")

    return rf"""\documentclass[11pt]{{article}}
\usepackage[letterpaper,margin=0.72in]{{geometry}}
\usepackage{{amsmath,amssymb}}
\usepackage{{enumitem}}
\usepackage{{hyperref}}
\usepackage{{xcolor}}
\usepackage[most]{{tcolorbox}}
\setlength{{\parindent}}{{0pt}}
\setlength{{\parskip}}{{0.55em}}
\definecolor{{LRAInk}}{{HTML}}{{1F2937}}
\definecolor{{LRABlue}}{{HTML}}{{2563EB}}
\definecolor{{LRABg}}{{HTML}}{{F8FAFC}}
\definecolor{{LRABorder}}{{HTML}}{{CBD5E1}}
\hypersetup{{colorlinks=true,linkcolor=LRABlue,urlcolor=LRABlue}}
\newtcolorbox{{studyblock}}[3]{{
  enhanced,
  breakable,
  colback=LRABg,
  colframe=LRABorder,
  boxrule=0.45pt,
  arc=1.5mm,
  left=7pt,
  right=7pt,
  top=6pt,
  bottom=6pt,
  before skip=8pt,
  after skip=8pt,
  title={{\textbf{{#1: #2}}\hfill\texttt{{#3}}}},
  coltitle=LRAInk,
  colbacktitle=white,
  fonttitle=\small,
}}
\begin{{document}}
\begin{{center}}
{{\LARGE Set Theory Proof Restart Packet}}\\[0.35em]
{{\large Definitions and theorem statements in prerequisite order}}\\[0.45em]
{{\small Generated from Volume I, Book II, Chapter 8 source files.}}
\end{{center}}

\tableofcontents
\newpage

\section{{Definition-Theorem Study Order}}
The sequence below places each theorem as close as possible to the definitions and earlier results it needs.

{''.join(sequence_blocks)}

\end{{document}}
"""


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    TEX_PATH.write_text(build_tex(), encoding="utf-8")
    cmd = [
        "lualatex",
        "-interaction=nonstopmode",
        "-halt-on-error",
        f"-output-directory={OUT_DIR}",
        str(TEX_PATH),
    ]
    subprocess.run(cmd, cwd=ROOT, check=True)
    subprocess.run(cmd, cwd=ROOT, check=True)
    if not PDF_PATH.exists():
        raise FileNotFoundError(PDF_PATH)


if __name__ == "__main__":
    main()
