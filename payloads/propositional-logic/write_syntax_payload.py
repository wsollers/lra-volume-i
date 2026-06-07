from __future__ import annotations

import base64
import json
import re
from pathlib import Path
from typing import Any


TEXT_FIELDS = {
    "body",
    "quantified_form",
    "standard_quantified_statement",
    "predicate_reading",
    "negated_form",
    "negation_predicate_reading",
    "interpretation",
    "examples",
    "non_examples",
    "readable_decomposition",
    "failure_mode_decomposition",
    "proof_sketch",
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
)


def format_predicate_names(text: str) -> str:
    for name in PREDICATE_NAMES:
        text = re.sub(
            rf"(?<!operatorname{{)\b{name}\s*\(",
            rf"\\operatorname{{{name}}}(",
            text,
        )
    return text


def b64(s: str) -> str:
    return base64.b64encode(s.encode("utf-8")).decode("ascii")


def encode_text_fields(obj: dict[str, Any]) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for k, v in obj.items():
        if k in TEXT_FIELDS and isinstance(v, str):
            out[f"{k}_b64"] = b64(format_predicate_names(v))
        else:
            out[k] = v
    return out


def pred(defines=None, uses=None):
    return {
        "defines": defines or [],
        "uses": uses or [],
    }


def notation(symbol: str, name: str, meaning: str, scope: str = "chapter", status: str = "canonical", introduced_by: str | None = None):
    row = {
        "symbol": symbol,
        "name": name,
        "meaning": meaning,
        "scope": scope,
        "status": status,
    }
    if introduced_by:
        row["introduced_by"] = introduced_by
    return row


def rel(defines=None, uses=None):
    return {
        "defines": defines or [],
        "uses": uses or [],
    }


def A(
    *,
    label: str,
    kind: str,
    title: str,
    body: str,
    quantified_form: str | None = None,
    predicate_reading: str | None = None,
    negated_form: str | None = None,
    negation_predicate_reading: str | None = None,
    interpretation: str,
    examples: str | None = None,
    non_examples: str | None = None,
    readable_decomposition: str | None = None,
    failure_mode_decomposition: str | None = None,
    dependencies=None,
    predicates=None,
    notations=None,
    relations=None,
    proof_required: bool = False,
):
    obj: dict[str, Any] = {
        "label": label,
        "kind": kind,
        "title": title,
        "body": body.strip(),
        "interpretation": interpretation.strip(),
        "dependencies": dependencies or [],
        "predicates": predicates or pred(),
        "notations": notations or {"defines": [], "uses": []},
        "relations": relations or rel(),
        "proof_required": proof_required,
    }
    optional = {
        "quantified_form": quantified_form,
        "predicate_reading": predicate_reading,
        "negated_form": negated_form,
        "negation_predicate_reading": negation_predicate_reading,
        "examples": examples,
        "non_examples": non_examples,
        "readable_decomposition": readable_decomposition,
        "failure_mode_decomposition": failure_mode_decomposition,
    }
    for k, v in optional.items():
        if v is not None:
            obj[k] = v.strip()
    return encode_text_fields(obj)


COMMON_FORMULA_NOTATION = [
    notation(r"\varphi,\psi,\chi,\theta", "formula metavariables", "metavariables ranging over propositional well-formed formulas", "global", "canonical"),
    notation(r"\neg", "negation", "unary propositional connective", "global", "canonical"),
    notation(r"\land", "conjunction", "binary propositional connective", "global", "canonical"),
    notation(r"\lor", "disjunction", "binary propositional connective", "global", "canonical"),
    notation(r"\to", "conditional", "binary propositional connective", "global", "canonical"),
    notation(r"\leftrightarrow", "biconditional", "binary propositional connective", "global", "canonical"),
    notation(r"\circ", "generic binary connective", r"an arbitrary member of \(\{\land,\lor,\to,\leftrightarrow\}\)", "global", "canonical"),
]


artifacts = [
    A(
        label="def:truth-value-propositional-logic",
        kind="definition",
        title="Truth Value",
        body=r"""
The set of truth values is
\[
\mathbb B := \{\mathrm{False},\mathrm{True}\}.
\]
Some sources identify this set with \(\{0,1\}\), with \(0\) read as false and \(1\) read as true.
""",
        quantified_form=r"""
\[
\mathbb B=\{\mathrm{False},\mathrm{True}\}.
\]
""",
        interpretation=r"""
Truth values are the semantic targets of propositional formulas. Syntax determines which strings are formulas; semantics later assigns elements of \(\mathbb B\) to formulas.
""",
        dependencies=[],
        predicates=pred(),
        notations={
            "defines": [
                notation(r"\mathbb B", "truth-value set", "the set of truth values", "global", "canonical", "def:truth-value-propositional-logic"),
            ],
            "uses": [],
        },
        proof_required=False,
    ),

    A(
        label="def:propositional-language",
        kind="definition",
        title="Propositional Language",
        body=r"""
A propositional language consists of:
\begin{enumerate}
\item a set \(\Prop\) of propositional variables;
\item logical connectives;
\item punctuation symbols such as parentheses;
\item recursive formation rules specifying the well-formed formulas.
\end{enumerate}
""",
        quantified_form=r"""
\[
\mathcal L_{\mathrm{prop}}
=
(\Prop,\{\neg,\land,\lor,\to,\leftrightarrow\},\text{punctuation},\text{formation rules}).
\]
""",
        interpretation=r"""
The language supplies symbols and grammar. It does not yet assign truth values, truth conditions, or logical consequence.
""",
        dependencies=["def:truth-value-propositional-logic"],
        predicates=pred(defines=["PropositionalLanguage"], uses=[]),
        notations={
            "defines": [
                notation(r"\Prop", "propositional variable set", "the set of propositional variables", "global", "canonical", "def:propositional-language"),
            ],
            "uses": [
                notation(r"\mathbb B", "truth-value set", "the set of truth values", "global", "canonical"),
            ],
        },
        proof_required=False,
    ),

    A(
        label="def:propositional-variable",
        kind="definition",
        title="Propositional Variable",
        body=r"""
A propositional variable is an atomic symbol intended to stand for a proposition. A standard supply of variables is
\[
\Prop=\{P_1,P_2,P_3,\ldots\}.
\]
Informally, variables are often written \(P,Q,R,S,\ldots\).
""",
        quantified_form=r"""
\[
PropositionalVariable(P)\Longleftrightarrow P\in\Prop.
\]
""",
        predicate_reading=r"""
\(PropositionalVariable(P)\) means \(P\in\Prop\).
""",
        interpretation=r"""
A propositional variable has no internal syntactic structure in propositional logic. It is a basic symbol from which more complex formulas are formed.
""",
        examples=r"""
\(P,Q,R,P_1,P_2\) are propositional variables when they belong to \(\Prop\).
""",
        non_examples=r"""
\(\neg P\), \(P\land Q\), and \((P\to Q)\) are not propositional variables; they are compound formulas.
""",
        dependencies=["def:propositional-language"],
        predicates=pred(defines=["PropositionalVariable"], uses=["PropositionalLanguage"]),
        notations={
            "defines": [
                notation(r"P,Q,R", "propositional variables", "schematic propositional variables", "chapter", "canonical", "def:propositional-variable"),
                notation(r"P_1,\ldots,P_n", "finite list of propositional variables", "a finite schematic list of propositional variables", "chapter", "local", "def:propositional-variable"),
            ],
            "uses": [
                notation(r"\Prop", "propositional variable set", "the set of propositional variables", "global", "canonical"),
            ],
        },
        proof_required=False,
    ),

    A(
        label="def:logical-connective",
        kind="definition",
        title="Logical Connective",
        body=r"""
The standard primitive propositional connectives are
\[
\neg,\qquad \land,\qquad \lor,\qquad \to,\qquad \leftrightarrow.
\]
The connective \(\neg\) is unary. The connectives \(\land,\lor,\to,\leftrightarrow\) are binary.

\[
\begin{array}{c|c|c|c|c}
\text{Symbol} & \text{Name} & \text{Arity} & \text{Formation pattern} & \text{Reading}\\
\hline
\neg & \text{negation} & \text{unary} & \neg\varphi & \text{not }\varphi\\
\land & \text{conjunction} & \text{binary} & (\varphi\land\psi) & \varphi\text{ and }\psi\\
\lor & \text{disjunction} & \text{binary} & (\varphi\lor\psi) & \varphi\text{ or }\psi\\
\to & \text{conditional} & \text{binary} & (\varphi\to\psi) & \text{if }\varphi,\text{ then }\psi\\
\leftrightarrow & \text{biconditional} & \text{binary} & (\varphi\leftrightarrow\psi) & \varphi\text{ iff }\psi
\end{array}
\]
""",
        quantified_form=r"""
\[
UnaryConnective(\neg)
\quad\text{and}\quad
BinaryConnective(\land)\land BinaryConnective(\lor)\land BinaryConnective(\to)\land BinaryConnective(\leftrightarrow).
\]
""",
        interpretation=r"""
Arity records how many formulas a connective uses to form a new formula. The truth behavior of these connectives belongs to semantics, not to the syntactic definition.
""",
        dependencies=["def:propositional-language"],
        predicates=pred(defines=["LogicalConnective", "UnaryConnective", "BinaryConnective"], uses=["PropositionalLanguage"]),
        notations={
            "defines": [
                notation(r"\neg", "negation", "unary propositional connective", "global", "canonical", "def:logical-connective"),
                notation(r"\land", "conjunction", "binary propositional connective", "global", "canonical", "def:logical-connective"),
                notation(r"\lor", "disjunction", "binary propositional connective", "global", "canonical", "def:logical-connective"),
                notation(r"\to", "conditional", "binary propositional connective", "global", "canonical", "def:logical-connective"),
                notation(r"\leftrightarrow", "biconditional", "binary propositional connective", "global", "canonical", "def:logical-connective"),
                notation(r"\circ", "generic binary connective", r"an arbitrary member of \(\{\land,\lor,\to,\leftrightarrow\}\)", "global", "canonical", "def:logical-connective"),
            ],
            "uses": [
                notation(r"\varphi,\psi", "formula metavariables", "metavariables ranging over formulas", "global", "canonical"),
            ],
        },
        proof_required=False,
    ),

    A(
        label="def:well-formed-formula",
        kind="definition",
        title="Well-Formed Formula",
        body=r"""
The set \(\WFF\) of well-formed formulas is the smallest set of strings satisfying the following formation rules:
\begin{enumerate}
\item Every propositional variable \(P\in\Prop\) belongs to \(\WFF\).
\item If \(\varphi\in\WFF\), then \(\neg\varphi\in\WFF\).
\item If \(\varphi,\psi\in\WFF\) and \(\circ\in\{\land,\lor,\to,\leftrightarrow\}\), then \((\varphi\circ\psi)\in\WFF\).
\item No string is a well-formed formula unless it is obtained by finitely many applications of the previous clauses.
\end{enumerate}
""",
        quantified_form=r"""
\[
\WFF
=
\bigcap
\left\{
S :
\Prop\subseteq S,\;
(\forall\varphi\in S)(\neg\varphi\in S),\;
(\forall\varphi,\psi\in S)
(\forall\circ\in\{\land,\lor,\to,\leftrightarrow\})
\bigl((\varphi\circ\psi)\in S\bigr)
\right\}.
\]
""",
        predicate_reading=r"""
\(WellFormedFormula(\varphi)\) means \(\varphi\in\WFF\), read as “\(\varphi\) is a well-formed formula.”
""",
        negated_form=r"""
\[
\sigma\notin\WFF
\Longleftrightarrow
\exists S
\left[
\Prop\subseteq S
\land
(\forall\varphi\in S)(\neg\varphi\in S)
\land
(\forall\varphi,\psi\in S)
(\forall\circ\in\{\land,\lor,\to,\leftrightarrow\})
((\varphi\circ\psi)\in S)
\land
\sigma\notin S
\right].
\]
""",
        negation_predicate_reading=r"""
\(\neg WellFormedFormula(\sigma)\) means the string \(\sigma\) is excluded by at least one formation-closed set containing \(\Prop\); equivalently, it is not generated by finitely many applications of the formation rules.
""",
        failure_mode_decomposition=r"""
\[
\underbrace{P\land}_{\text{missing right operand}}
\qquad
\underbrace{(P\ Q)}_{\text{missing binary connective}}
\qquad
\underbrace{\neg\lor P}_{\text{negation applied to a non-formula}}.
\]
""",
        interpretation=r"""
Well-formed formulas are exactly the strings to which the semantic and proof-theoretic machinery of propositional logic applies.
""",
        examples=r"""
\(P\), \(\neg P\), \((P\to Q)\), and \((P\to(Q\lor R))\) are well-formed formulas.
""",
        non_examples=r"""
\(P\land\), \((P Q)\), and \(\neg\lor P\) are not well-formed formulas.
""",
        dependencies=["def:propositional-variable", "def:logical-connective"],
        predicates=pred(defines=["WellFormedFormula"], uses=["PropositionalVariable", "LogicalConnective"]),
        notations={
            "defines": [
                notation(r"\WFF", "well-formed formula set", "the set of propositional well-formed formulas", "chapter", "canonical", "def:well-formed-formula"),
            ],
            "uses": [
                notation(r"\Prop", "propositional variable set", "the set of propositional variables", "global", "canonical"),
                *COMMON_FORMULA_NOTATION,
            ],
        },
        relations=rel(uses=[{"label": "rel:generated-by-formation-rules", "meaning": "generated by recursive formation rules"}]),
        proof_required=False,
    ),

    A(
        label="def:atomic-formula-propositional-logic",
        kind="definition",
        title="Atomic Formula",
        body=r"""
An atomic formula is a well-formed formula that is a propositional variable.
""",
        quantified_form=r"""
\[
AtomicFormula(\varphi)
\Longleftrightarrow
\varphi\in\WFF\land\varphi\in\Prop.
\]
""",
        predicate_reading=r"""
\(AtomicFormula(\varphi)\) means that \(\varphi\) is a propositional variable viewed as a well-formed formula.
""",
        interpretation=r"""
Atomic formulas are the base cases of the recursive grammar. They contain no connective structure.
""",
        dependencies=["def:well-formed-formula", "def:propositional-variable"],
        predicates=pred(defines=["AtomicFormula"], uses=["WellFormedFormula", "PropositionalVariable"]),
        notations={"defines": [], "uses": [notation(r"\WFF", "well-formed formula set", "the set of propositional well-formed formulas"), notation(r"\Prop", "propositional variable set", "the set of propositional variables"), notation(r"\varphi", "formula metavariable", "a metavariable ranging over formulas")]},
        proof_required=False,
    ),

    A(
        label="def:molecular-formula-propositional-logic",
        kind="definition",
        title="Molecular Formula",
        body=r"""
A molecular formula is a well-formed formula that is not atomic. Equivalently, it is a well-formed formula formed using at least one logical connective.
""",
        quantified_form=r"""
\[
MolecularFormula(\varphi)
\Longleftrightarrow
\varphi\in\WFF\land\neg AtomicFormula(\varphi).
\]
""",
        predicate_reading=r"""
\(MolecularFormula(\varphi)\) means that \(\varphi\) has nontrivial connective structure.
""",
        interpretation=r"""
Molecular formulas are exactly the formulas obtained by applying negation or a binary connective at least once.
""",
        dependencies=["def:well-formed-formula", "def:atomic-formula-propositional-logic", "def:logical-connective"],
        predicates=pred(defines=["MolecularFormula"], uses=["WellFormedFormula", "AtomicFormula", "LogicalConnective"]),
        notations={"defines": [], "uses": [notation(r"\WFF", "well-formed formula set", "the set of propositional well-formed formulas"), notation(r"\varphi", "formula metavariable", "a metavariable ranging over formulas")]},
        proof_required=False,
    ),

    A(
        label="def:main-connective-propositional-logic",
        kind="definition",
        title="Main Connective",
        body=r"""
The main connective of a molecular formula is the connective introduced at the final formation step:
\begin{enumerate}
\item for \(\neg\varphi\), the main connective is \(\neg\);
\item for \((\varphi\circ\psi)\), the main connective is \(\circ\).
\end{enumerate}
Atomic formulas have no main connective.
""",
        quantified_form=r"""
\[
MainConnective(\neg\varphi,\neg)
\quad\text{and}\quad
MainConnective((\varphi\circ\psi),\circ).
\]
""",
        predicate_reading=r"""
\(MainConnective(\varphi,c)\) means that \(c\) is the outermost connective introduced in the final formation step of \(\varphi\).
""",
        interpretation=r"""
The main connective identifies the outermost syntactic operation. It is the first connective used when analyzing a formula from the outside inward.
""",
        dependencies=["def:well-formed-formula", "def:molecular-formula-propositional-logic", "def:logical-connective"],
        predicates=pred(defines=["MainConnective"], uses=["MolecularFormula", "LogicalConnective"]),
        notations={"defines": [], "uses": COMMON_FORMULA_NOTATION},
        proof_required=False,
    ),

    A(
        label="thm:structural-induction-propositional-formulas",
        kind="theorem",
        title="Structural Induction for Propositional Formulas",
        body=r"""
Let \(A(\varphi)\) be a property of well-formed formulas. Suppose:
\begin{enumerate}
\item \(A(P)\) holds for every \(P\in\Prop\);
\item if \(A(\varphi)\) holds, then \(A(\neg\varphi)\) holds;
\item if \(A(\varphi)\) and \(A(\psi)\) hold, then \(A((\varphi\circ\psi))\) holds for every \(\circ\in\{\land,\lor,\to,\leftrightarrow\}\).
\end{enumerate}
Then \(A(\theta)\) holds for every \(\theta\in\WFF\).
""",
        quantified_form=r"""
\[
\left[
(\forall P\in\Prop)A(P)
\land
(\forall\varphi\in\WFF)(A(\varphi)\to A(\neg\varphi))
\land
(\forall\varphi,\psi\in\WFF)
(\forall\circ\in\{\land,\lor,\to,\leftrightarrow\})
\bigl((A(\varphi)\land A(\psi))\to A((\varphi\circ\psi))\bigr)
\right]
\to
(\forall\theta\in\WFF)A(\theta).
\]
""",
        interpretation=r"""
To prove a statement for all formulas, it suffices to prove it for propositional variables and show it is preserved by each formula-forming operation.
""",
        dependencies=["def:well-formed-formula"],
        predicates=pred(uses=["WellFormedFormula", "PropositionalVariable"]),
        notations={"defines": [], "uses": [notation(r"\WFF", "well-formed formula set", "the set of propositional well-formed formulas"), notation(r"\Prop", "propositional variable set", "the set of propositional variables"), *COMMON_FORMULA_NOTATION]},
        proof_required=True,
    ),

    A(
        label="thm:structural-recursion-propositional-formulas",
        kind="theorem",
        title="Structural Recursion for Propositional Formulas",
        body=r"""
To define a function \(F\) on \(\WFF\), it suffices to specify:
\begin{enumerate}
\item \(F(P)\) for every \(P\in\Prop\);
\item \(F(\neg\varphi)\) in terms of \(F(\varphi)\);
\item \(F((\varphi\circ\psi))\) in terms of \(F(\varphi)\), \(F(\psi)\), and \(\circ\).
\end{enumerate}
When these clauses respect the formation rules, they determine a unique function on \(\WFF\).
""",
        quantified_form=r"""
\[
\text{recursive data on the formation clauses of }\WFF
\Longrightarrow
\exists!F:\WFF\to X
\text{ satisfying those clauses}.
\]
""",
        interpretation=r"""
Structural recursion justifies recursive definitions such as variables of a formula, subformulas, depth, connective count, syntax tree, and truth evaluation.
""",
        dependencies=["def:well-formed-formula", "thm:structural-induction-propositional-formulas"],
        predicates=pred(uses=["WellFormedFormula"]),
        notations={"defines": [], "uses": [notation(r"\WFF", "well-formed formula set", "the set of propositional well-formed formulas"), *COMMON_FORMULA_NOTATION]},
        proof_required=True,
    ),

    A(
        label="lem:constructor-disjointness-propositional-formulas",
        kind="lemma",
        title="Constructor Disjointness for Propositional Formulas",
        body=r"""
The three outer formation cases for propositional formulas are disjoint:
\begin{enumerate}
\item no propositional variable is a negation formula;
\item no propositional variable is a binary formula;
\item no negation formula is a binary formula.
\end{enumerate}
""",
        readable_decomposition=r"""
\[
\underbrace{P}_{\text{atomic}}
\qquad
\underbrace{\neg\varphi}_{\text{negation case}}
\qquad
\underbrace{(\varphi\circ\psi)}_{\text{binary case}}
\]
belong to three distinct outer-form classes.
""",
        quantified_form=r"""
\[
P\in\Prop\Rightarrow
\left[
(\forall\varphi\in\WFF)(P\ne\neg\varphi)
\land
(\forall\varphi,\psi\in\WFF)(\forall\circ)(P\ne(\varphi\circ\psi))
\right]
\]
and
\[
(\forall\varphi,\psi,\chi\in\WFF)(\forall\circ)
\bigl(\neg\varphi\ne(\psi\circ\chi)\bigr).
\]
""",
        interpretation=r"""
A formula cannot be parsed as two different outer formation types.
""",
        dependencies=["def:well-formed-formula", "def:atomic-formula-propositional-logic", "def:main-connective-propositional-logic"],
        predicates=pred(uses=["WellFormedFormula", "AtomicFormula", "MolecularFormula"]),
        notations={"defines": [], "uses": [notation(r"\WFF", "well-formed formula set", "the set of propositional well-formed formulas"), notation(r"\Prop", "propositional variable set", "the set of propositional variables"), *COMMON_FORMULA_NOTATION]},
        proof_required=True,
    ),

    A(
        label="lem:constructor-injectivity-propositional-formulas",
        kind="lemma",
        title="Constructor Injectivity for Propositional Formulas",
        body=r"""
The propositional formula constructors are injective:
\begin{enumerate}
\item if \(\neg\varphi=\neg\psi\), then \(\varphi=\psi\);
\item if \((\varphi\circ\psi)=(\alpha\star\beta)\), then \(\varphi=\alpha\), \(\psi=\beta\), and \(\circ=\star\).
\end{enumerate}
""",
        quantified_form=r"""
\[
(\forall\varphi,\psi\in\WFF)
(\neg\varphi=\neg\psi\to\varphi=\psi)
\]
and
\[
(\forall\varphi,\psi,\alpha,\beta\in\WFF)
(\forall\circ,\star\in\{\land,\lor,\to,\leftrightarrow\})
\left[
(\varphi\circ\psi)=(\alpha\star\beta)
\to
(\varphi=\alpha\land\psi=\beta\land\circ=\star)
\right].
\]
""",
        interpretation=r"""
If two formulas are built by the same outer constructor and are equal as strings, then their immediate constituents are equal.
""",
        dependencies=["def:well-formed-formula", "def:logical-connective"],
        predicates=pred(uses=["WellFormedFormula", "LogicalConnective"]),
        notations={"defines": [], "uses": [notation(r"\WFF", "well-formed formula set", "the set of propositional well-formed formulas"), *COMMON_FORMULA_NOTATION, notation(r"\alpha,\beta", "additional formula metavariables", "formula metavariables used in comparison statements", "chapter", "local")]},
        proof_required=True,
    ),

    A(
        label="thm:unique-decomposition-propositional-formulas",
        kind="theorem",
        title="Unique Decomposition for Propositional Formulas",
        body=r"""
Every \(\varphi\in\WFF\) has exactly one outermost form:
\begin{enumerate}
\item \(\varphi=P\) for a unique \(P\in\Prop\);
\item \(\varphi=\neg\psi\) for a unique \(\psi\in\WFF\);
\item \(\varphi=(\psi\circ\chi)\) for unique \(\psi,\chi\in\WFF\) and a unique binary connective \(\circ\in\{\land,\lor,\to,\leftrightarrow\}\).
\end{enumerate}
""",
        readable_decomposition=r"""
\[
\varphi
\in
\underbrace{\Prop}_{\text{atomic case}}
\quad\text{or}\quad
\varphi=
\underbrace{\neg\psi}_{\text{negation case}}
\quad\text{or}\quad
\varphi=
\underbrace{(\psi\circ\chi)}_{\text{binary case}},
\]
and exactly one of these alternatives holds.
""",
        quantified_form=r"""
\[
\forall\varphi\in\WFF,\quad
\text{exactly one of the following holds:}
\]
\[
\varphi\in\Prop,\qquad
\exists!\psi\in\WFF\,(\varphi=\neg\psi),\qquad
\exists!\psi,\chi\in\WFF\;\exists!\circ\in\{\land,\lor,\to,\leftrightarrow\}\,(\varphi=(\psi\circ\chi)).
\]
""",
        interpretation=r"""
Unique decomposition makes recursive definitions and induction on formulas unambiguous.
""",
        dependencies=["def:well-formed-formula", "lem:constructor-disjointness-propositional-formulas", "lem:constructor-injectivity-propositional-formulas"],
        predicates=pred(uses=["WellFormedFormula", "PropositionalVariable", "AtomicFormula", "MolecularFormula"]),
        notations={"defines": [], "uses": [notation(r"\WFF", "well-formed formula set", "the set of propositional well-formed formulas"), notation(r"\Prop", "propositional variable set", "the set of propositional variables"), *COMMON_FORMULA_NOTATION]},
        proof_required=True,
    ),

    A(
        label="def:parse-tree-propositional-logic",
        kind="definition",
        title="Parse Tree",
        body=r"""
The parse tree, or syntax tree, of a well-formed formula is the tree representation of its recursive construction:
\begin{enumerate}
\item a propositional variable is represented by a single leaf;
\item a formula \(\neg\varphi\) is represented by a root labeled \(\neg\) with one child, the parse tree of \(\varphi\);
\item a formula \((\varphi\circ\psi)\) is represented by a root labeled \(\circ\) with two children, the parse trees of \(\varphi\) and \(\psi\).
\end{enumerate}
""",
        quantified_form=r"""
\[
\operatorname{Tree}:\WFF\to\{\text{finite rooted labeled trees}\}
\]
is defined recursively by the three formation clauses for propositional formulas.
""",
        interpretation=r"""
The parse tree records the same structure described by unique decomposition. It turns the recursive construction of a formula into a visible tree.
""",
        dependencies=["def:well-formed-formula", "thm:unique-decomposition-propositional-formulas"],
        predicates=pred(defines=["ParseTree"], uses=["WellFormedFormula"]),
        notations={
            "defines": [
                notation(r"\operatorname{Tree}(\varphi)", "syntax tree", "parse tree or formation tree of a formula", "chapter", "canonical", "def:parse-tree-propositional-logic"),
            ],
            "uses": [notation(r"\WFF", "well-formed formula set", "the set of propositional well-formed formulas"), *COMMON_FORMULA_NOTATION],
        },
        proof_required=False,
    ),

    A(
        label="thm:unique-syntax-tree-propositional-formulas",
        kind="theorem",
        title="Unique Syntax Tree for Propositional Formulas",
        body=r"""
Every propositional well-formed formula has a unique parse tree.
""",
        quantified_form=r"""
\[
\forall\varphi\in\WFF,\quad \exists!T\; (T=\operatorname{Tree}(\varphi)).
\]
""",
        interpretation=r"""
A formula has exactly one tree representation of its recursive construction. This is the tree form of unique decomposition.
""",
        dependencies=["def:parse-tree-propositional-logic", "thm:unique-decomposition-propositional-formulas"],
        predicates=pred(uses=["WellFormedFormula", "ParseTree"]),
        notations={"defines": [], "uses": [notation(r"\operatorname{Tree}(\varphi)", "syntax tree", "parse tree or formation tree of a formula"), notation(r"\WFF", "well-formed formula set", "the set of propositional well-formed formulas")]},
        proof_required=True,
    ),

    A(
        label="def:formula-variable-set-propositional-logic",
        kind="definition",
        title="Variable Set of a Formula",
        body=r"""
The variable set \(\operatorname{Var}(\varphi)\) of a formula \(\varphi\) is defined recursively:
\begin{enumerate}
\item if \(\varphi=P\in\Prop\), then \(\operatorname{Var}(\varphi)=\{P\}\);
\item if \(\varphi=\neg\psi\), then \(\operatorname{Var}(\varphi)=\operatorname{Var}(\psi)\);
\item if \(\varphi=(\psi\circ\chi)\), then
\[
\operatorname{Var}(\varphi)=\operatorname{Var}(\psi)\cup\operatorname{Var}(\chi).
\]
\end{enumerate}
""",
        quantified_form=r"""
\[
\operatorname{Var}(P)=\{P\},\qquad
\operatorname{Var}(\neg\psi)=\operatorname{Var}(\psi),\qquad
\operatorname{Var}((\psi\circ\chi))=\operatorname{Var}(\psi)\cup\operatorname{Var}(\chi).
\]
""",
        interpretation=r"""
The variable set records exactly which propositional variables occur in a formula.
""",
        dependencies=["def:well-formed-formula", "thm:structural-recursion-propositional-formulas"],
        predicates=pred(defines=["FormulaVariableSet"], uses=["WellFormedFormula"]),
        notations={
            "defines": [
                notation(r"\operatorname{Var}(\varphi)", "variable set of a formula", "the set of propositional variables occurring in a formula", "chapter", "canonical", "def:formula-variable-set-propositional-logic"),
            ],
            "uses": [notation(r"\WFF", "well-formed formula set", "the set of propositional well-formed formulas"), notation(r"\Prop", "propositional variable set", "the set of propositional variables"), *COMMON_FORMULA_NOTATION],
        },
        proof_required=False,
    ),

    A(
        label="def:subformula-propositional-logic",
        kind="definition",
        title="Subformula",
        body=r"""
The set \(\operatorname{Sub}(\varphi)\) of subformulas of a formula \(\varphi\) is defined recursively:
\begin{enumerate}
\item if \(\varphi\) is atomic, then \(\operatorname{Sub}(\varphi)=\{\varphi\}\);
\item if \(\varphi=\neg\psi\), then
\[
\operatorname{Sub}(\varphi)=\{\varphi\}\cup\operatorname{Sub}(\psi);
\]
\item if \(\varphi=(\psi\circ\chi)\), then
\[
\operatorname{Sub}(\varphi)=\{\varphi\}\cup\operatorname{Sub}(\psi)\cup\operatorname{Sub}(\chi).
\]
\end{enumerate}
A proper subformula is a subformula other than \(\varphi\) itself.
""",
        quantified_form=r"""
\[
\operatorname{Sub}(P)=\{P\},\qquad
\operatorname{Sub}(\neg\psi)=\{\neg\psi\}\cup\operatorname{Sub}(\psi),
\]
\[
\operatorname{Sub}((\psi\circ\chi))
=
\{(\psi\circ\chi)\}\cup\operatorname{Sub}(\psi)\cup\operatorname{Sub}(\chi).
\]
""",
        interpretation=r"""
Subformulas are the formulas that occur at nodes of the parse tree.
""",
        dependencies=["def:well-formed-formula", "thm:unique-decomposition-propositional-formulas"],
        predicates=pred(defines=["Subformula"], uses=["WellFormedFormula"]),
        notations={
            "defines": [
                notation(r"\operatorname{Sub}(\varphi)", "subformula set", "the set of subformulas of a formula", "chapter", "canonical", "def:subformula-propositional-logic"),
            ],
            "uses": [notation(r"\WFF", "well-formed formula set", "the set of propositional well-formed formulas"), *COMMON_FORMULA_NOTATION],
        },
        proof_required=False,
    ),

    A(
        label="def:formula-depth-propositional-logic",
        kind="definition",
        title="Formula Depth",
        body=r"""
The depth of a formula \(\varphi\), denoted \(\operatorname{depth}(\varphi)\), is defined recursively:
\begin{enumerate}
\item if \(\varphi\) is atomic, then \(\operatorname{depth}(\varphi)=0\);
\item if \(\varphi=\neg\psi\), then \(\operatorname{depth}(\varphi)=\operatorname{depth}(\psi)+1\);
\item if \(\varphi=(\psi\circ\chi)\), then
\[
\operatorname{depth}(\varphi)=\max\{\operatorname{depth}(\psi),\operatorname{depth}(\chi)\}+1.
\]
\end{enumerate}
""",
        quantified_form=r"""
\[
\operatorname{depth}(P)=0,\qquad
\operatorname{depth}(\neg\psi)=\operatorname{depth}(\psi)+1,
\]
\[
\operatorname{depth}((\psi\circ\chi))
=
\max\{\operatorname{depth}(\psi),\operatorname{depth}(\chi)\}+1.
\]
""",
        interpretation=r"""
Formula depth measures the height of the syntax tree. Some authors call this the rank, complexity, or formation depth of the formula.
""",
        dependencies=["def:well-formed-formula", "def:parse-tree-propositional-logic"],
        predicates=pred(defines=["FormulaDepth"], uses=["WellFormedFormula", "ParseTree"]),
        notations={
            "defines": [
                notation(r"\operatorname{depth}(\varphi)", "formula depth", "height, rank, or complexity of the formula formation tree", "chapter", "canonical", "def:formula-depth-propositional-logic"),
            ],
            "uses": [notation(r"\WFF", "well-formed formula set", "the set of propositional well-formed formulas"), *COMMON_FORMULA_NOTATION],
        },
        proof_required=False,
    ),

    A(
        label="def:connective-count-propositional-logic",
        kind="definition",
        title="Connective Count",
        body=r"""
The connective count of a formula \(\varphi\), denoted \(\operatorname{conn}(\varphi)\), is defined recursively:
\begin{enumerate}
\item if \(\varphi\) is atomic, then \(\operatorname{conn}(\varphi)=0\);
\item if \(\varphi=\neg\psi\), then \(\operatorname{conn}(\varphi)=\operatorname{conn}(\psi)+1\);
\item if \(\varphi=(\psi\circ\chi)\), then
\[
\operatorname{conn}(\varphi)=\operatorname{conn}(\psi)+\operatorname{conn}(\chi)+1.
\]
\end{enumerate}
""",
        quantified_form=r"""
\[
\operatorname{conn}(P)=0,\qquad
\operatorname{conn}(\neg\psi)=\operatorname{conn}(\psi)+1,
\]
\[
\operatorname{conn}((\psi\circ\chi))
=
\operatorname{conn}(\psi)+\operatorname{conn}(\chi)+1.
\]
""",
        interpretation=r"""
Formula depth measures the height of the syntax tree. Connective count measures the number of connective nodes in the syntax tree.
""",
        dependencies=["def:well-formed-formula", "def:parse-tree-propositional-logic"],
        predicates=pred(defines=["ConnectiveCount"], uses=["WellFormedFormula", "ParseTree"]),
        notations={
            "defines": [
                notation(r"\operatorname{conn}(\varphi)", "connective count", "the number of connective occurrences in a formula", "chapter", "canonical", "def:connective-count-propositional-logic"),
            ],
            "uses": [notation(r"\WFF", "well-formed formula set", "the set of propositional well-formed formulas"), *COMMON_FORMULA_NOTATION],
        },
        proof_required=False,
    ),

    A(
        label="lem:proper-subformula-depth-propositional-logic",
        kind="lemma",
        title="Proper Subformula Depth",
        body=r"""
If \(\psi\) is a proper subformula of \(\varphi\), then
\[
\operatorname{depth}(\psi)<\operatorname{depth}(\varphi).
\]
""",
        quantified_form=r"""
\[
(\forall\varphi,\psi\in\WFF)
\left[
\psi\in\operatorname{Sub}(\varphi)\land \psi\ne\varphi
\to
\operatorname{depth}(\psi)<\operatorname{depth}(\varphi)
\right].
\]
""",
        interpretation=r"""
Every descent into a proper subformula lowers formula depth. This justifies induction on formula depth and recursive proofs over subformulas.
""",
        dependencies=["def:subformula-propositional-logic", "def:formula-depth-propositional-logic"],
        predicates=pred(uses=["Subformula", "FormulaDepth", "WellFormedFormula"]),
        notations={"defines": [], "uses": [notation(r"\operatorname{Sub}(\varphi)", "subformula set", "the set of subformulas of a formula"), notation(r"\operatorname{depth}(\varphi)", "formula depth", "height of the formula tree"), notation(r"\WFF", "well-formed formula set", "the set of propositional well-formed formulas")]},
        proof_required=True,
    ),

    A(
        label="lem:finiteness-of-variables-propositional-formulas",
        kind="lemma",
        title="Finiteness of Variables in a Formula",
        body=r"""
For every \(\varphi\in\WFF\), the set \(\operatorname{Var}(\varphi)\) is finite.
""",
        quantified_form=r"""
\[
(\forall\varphi\in\WFF)\quad
\operatorname{Var}(\varphi)\text{ is finite}.
\]
""",
        interpretation=r"""
Every formula depends on only finitely many propositional variables, even though the language may contain infinitely many variables.
""",
        dependencies=["def:formula-variable-set-propositional-logic", "thm:structural-induction-propositional-formulas"],
        predicates=pred(uses=["WellFormedFormula", "FormulaVariableSet"]),
        notations={"defines": [], "uses": [notation(r"\operatorname{Var}(\varphi)", "variable set of a formula", "the set of variables occurring in a formula"), notation(r"\WFF", "well-formed formula set", "the set of propositional well-formed formulas")]},
        proof_required=True,
    ),

    A(
        label="lem:finiteness-of-subformulas-propositional-formulas",
        kind="lemma",
        title="Finiteness of Subformulas",
        body=r"""
For every \(\varphi\in\WFF\), the set \(\operatorname{Sub}(\varphi)\) is finite.
""",
        quantified_form=r"""
\[
(\forall\varphi\in\WFF)\quad
\operatorname{Sub}(\varphi)\text{ is finite}.
\]
""",
        interpretation=r"""
Every formula has only finitely many syntactic parts.
""",
        dependencies=["def:subformula-propositional-logic", "thm:structural-induction-propositional-formulas"],
        predicates=pred(uses=["WellFormedFormula", "Subformula"]),
        notations={"defines": [], "uses": [notation(r"\operatorname{Sub}(\varphi)", "subformula set", "the set of subformulas of a formula"), notation(r"\WFF", "well-formed formula set", "the set of propositional well-formed formulas")]},
        proof_required=True,
    ),
]


payload = {
    "schema_version": 1,
    "chapter": "propositional-logic",
    "topic": "syntax",
    "encoding": "utf-8",
    "content_format": "latex",
    "artifacts": artifacts,
}

out = Path("payloads/propositional-logic/syntax.full.json")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Wrote {out} with {len(artifacts)} artifacts.")
