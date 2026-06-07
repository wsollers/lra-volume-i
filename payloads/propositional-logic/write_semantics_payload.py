from __future__ import annotations

import base64
import json
import re
from pathlib import Path
from typing import Any


TEXT_FIELDS = {
    "body",
    "quantified_form",
    "predicate_reading",
    "negated_form",
    "negation_predicate_reading",
    "interpretation",
    "proof_sketch",
}

PREDICATE_NAMES = (
    "PropositionalVariable",
    "WellFormedFormula",
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
    "FormulaVariableSet",
    "BooleanFunction",
    "TruthFunctionOfFormula",
)


def format_predicate_names(text: str) -> str:
    for name in PREDICATE_NAMES:
        text = re.sub(
            rf"(?<!operatorname{{)\b{name}\s*\(",
            rf"\\operatorname{{{name}}}(",
            text,
        )
    return text


def b64(text: str) -> str:
    return base64.b64encode(format_predicate_names(text.strip()).encode("utf-8")).decode("ascii")


def pred(defines=None, uses=None):
    return {"defines": defines or [], "uses": uses or []}


def notation(symbol: str, name: str, meaning: str, scope: str = "chapter", status: str = "canonical", introduced_by: str | None = None):
    row = {"symbol": symbol, "name": name, "meaning": meaning, "scope": scope, "status": status}
    if introduced_by:
        row["introduced_by"] = introduced_by
    return row


def rel(defines=None, uses=None):
    return {"defines": defines or [], "uses": uses or []}


def A(
    *,
    label: str,
    kind: str,
    title: str,
    body: str,
    interpretation: str,
    quantified_form: str | None = None,
    predicate_reading: str | None = None,
    negated_form: str | None = None,
    negation_predicate_reading: str | None = None,
    dependencies=None,
    predicates=None,
    notations=None,
    relations=None,
    proof_required: bool = False,
    proof_sketch: str | None = None,
):
    obj: dict[str, Any] = {
        "label": label,
        "kind": kind,
        "title": title,
        "body_b64": b64(body),
        "interpretation_b64": b64(interpretation),
        "dependencies": dependencies or [],
        "predicates": predicates or pred(),
        "notations": notations or {"defines": [], "uses": []},
        "relations": relations or rel(),
        "proof_required": proof_required,
    }
    for key, value in {
        "quantified_form": quantified_form,
        "predicate_reading": predicate_reading,
        "negated_form": negated_form,
        "negation_predicate_reading": negation_predicate_reading,
        "proof_sketch": proof_sketch,
    }.items():
        if value is not None:
            obj[f"{key}_b64"] = b64(value)
    return obj


TRUTH_VALUE = notation(r"\mathbb{B}", "truth-value set", "the set of truth values", "global", "canonical")
PROP = notation(r"\Prop", "propositional variable set", "the set of propositional variables", "global", "canonical")
WFF = notation(r"\WFF", "well-formed formula set", "the set of propositional well-formed formulas", "chapter", "canonical")
FORMULAS = notation(r"\varphi,\psi,\chi,\theta", "formula metavariables", "metavariables ranging over propositional well-formed formulas", "global", "canonical")
CONNECTIVES = notation(r"\neg,\land,\lor,\to,\leftrightarrow", "standard connectives", "standard propositional connectives", "global", "canonical")
TRUTH_ASSIGNMENT = notation(r"v,w", "truth assignments", "truth assignments for propositional variables", "chapter", "canonical")
EXTENDED_VALUATION = notation(r"\widehat v,\widehat w", "extended truth assignments", "unique extensions of truth assignments to formulas", "chapter", "canonical")
SAT_FORMULA = notation(r"v\models\varphi", "satisfaction of a formula", "truth assignment satisfies a formula", "chapter", "canonical")
SAT_SET = notation(r"v\models\Gamma", "satisfaction of a set", "truth assignment satisfies each formula in a set", "chapter", "canonical")
GAMMA = notation(r"\Gamma", "set of premise formulas", "a set of propositional formulas", "chapter", "canonical")
VALIDITY = notation(r"\models\varphi", "tautology notation", "formula valid under every truth assignment", "chapter", "canonical")
CONSEQUENCE = notation(r"\Gamma\models\varphi", "semantic consequence", "semantic consequence from premises to conclusion", "chapter", "canonical")
EQUIV = notation(r"\varphi\equiv\psi", "logical equivalence", "same truth value under every truth assignment", "chapter", "canonical")
VARS = notation(r"\operatorname{Var}(\varphi)", "variable set of a formula", "the set of propositional variables occurring in a formula", "chapter", "canonical")
FINITE_VARS = notation(r"P_1,\ldots,P_n", "finite list of propositional variables", "a finite schematic list of propositional variables", "chapter", "local")
BOOLEAN_FUNCTION = notation(r"f:\mathbb{B}^n\to\mathbb{B}", "n-ary Boolean function", "function from truth-value tuples to a truth value", "chapter", "canonical")
INDUCED_FUNCTION = notation(r"f_\varphi", "truth function induced by a formula", "Boolean function represented by a formula", "chapter", "canonical")


artifacts = [
    A(
        label="def:truth-assignment-propositional-logic",
        kind="definition",
        title="Truth Assignment",
        body=r"""
A truth assignment for propositional logic is a function
\[
v:\Prop\to\mathbb{B}.
\]
Thus a truth assignment assigns either \(\mathrm{False}\) or \(\mathrm{True}\) to each propositional variable.
""",
        quantified_form=r"""
\[
TruthAssignment(v)
\Longleftrightarrow
v:\Prop\to\mathbb{B}.
\]
""",
        predicate_reading=r"""
\[
TruthAssignment(v)
\]
means that \(v\) assigns a truth value to every propositional variable.
""",
        interpretation="A truth assignment fixes the truth values of atomic formulas. The recursive semantics of the connectives then determines the truth value of each molecular formula.",
        dependencies=["def:truth-value-propositional-logic", "def:propositional-variable", "def:well-formed-formula"],
        predicates=pred(defines=["TruthAssignment"], uses=["PropositionalVariable", "WellFormedFormula"]),
        notations={"defines": [notation(r"v", "truth assignment", "a truth assignment on propositional variables", "chapter", "canonical", "def:truth-assignment-propositional-logic")], "uses": [PROP, TRUTH_VALUE, WFF]},
    ),
    A(
        label="thm:unique-extension-truth-assignment-propositional-logic",
        kind="theorem",
        title="Unique Extension of a Truth Assignment",
        body=r"""
Every truth assignment \(v:\Prop\to\mathbb{B}\) extends uniquely to a function
\[
\widehat v:\WFF\to\mathbb{B}
\]
satisfying the following clauses:
\[
\widehat v(P)=v(P)\quad(P\in\Prop),
\]
\[
\widehat v(\neg\varphi)=\mathrm{True}
\Longleftrightarrow
\widehat v(\varphi)=\mathrm{False},
\]
\[
\widehat v(\varphi\land\psi)=\mathrm{True}
\Longleftrightarrow
\widehat v(\varphi)=\mathrm{True}
\text{ and }
\widehat v(\psi)=\mathrm{True},
\]
\[
\widehat v(\varphi\lor\psi)=\mathrm{True}
\Longleftrightarrow
\widehat v(\varphi)=\mathrm{True}
\text{ or }
\widehat v(\psi)=\mathrm{True},
\]
\[
\widehat v(\varphi\to\psi)=\mathrm{True}
\Longleftrightarrow
\widehat v(\varphi)=\mathrm{False}
\text{ or }
\widehat v(\psi)=\mathrm{True},
\]
and
\[
\widehat v(\varphi\leftrightarrow\psi)=\mathrm{True}
\Longleftrightarrow
\widehat v(\varphi)=\widehat v(\psi).
\]
""",
        quantified_form=r"""
\[
\begin{aligned}
&(\forall v:\Prop\to\mathbb{B})(\exists!\widehat v:\WFF\to\mathbb{B})\\
&\quad\text{such that, for all }P\in\Prop\text{ and }\varphi,\psi\in\WFF,\\
&\quad \widehat v(P)=v(P),\\
&\quad \widehat v(\neg\varphi)=\mathrm{True}
   \Longleftrightarrow \widehat v(\varphi)=\mathrm{False},\\
&\quad \widehat v(\varphi\land\psi)=\mathrm{True}
   \Longleftrightarrow
   (\widehat v(\varphi)=\mathrm{True}\land \widehat v(\psi)=\mathrm{True}),\\
&\quad \widehat v(\varphi\lor\psi)=\mathrm{True}
   \Longleftrightarrow
   (\widehat v(\varphi)=\mathrm{True}\lor \widehat v(\psi)=\mathrm{True}),\\
&\quad \widehat v(\varphi\to\psi)=\mathrm{True}
   \Longleftrightarrow
   (\widehat v(\varphi)=\mathrm{False}\lor \widehat v(\psi)=\mathrm{True}),\\
&\quad \widehat v(\varphi\leftrightarrow\psi)=\mathrm{True}
   \Longleftrightarrow
   \widehat v(\varphi)=\widehat v(\psi).
\end{aligned}
\]
""",
        interpretation="A valuation on variables determines exactly one truth value for every formula. This theorem is the semantic counterpart of structural recursion and unique decomposition.",
        dependencies=["def:truth-assignment-propositional-logic", "def:well-formed-formula", "thm:structural-recursion-propositional-formulas", "thm:unique-decomposition-propositional-formulas"],
        predicates=pred(uses=["TruthAssignment", "WellFormedFormula"]),
        notations={"defines": [notation(r"\widehat v", "extended truth assignment", "unique extension of a truth assignment to formulas", "chapter", "canonical", "thm:unique-extension-truth-assignment-propositional-logic")], "uses": [notation(r"v", "truth assignment", "truth assignment on propositional variables"), PROP, TRUTH_VALUE, WFF, CONNECTIVES, FORMULAS]},
        proof_required=True,
        proof_sketch=r"Use structural recursion to define \(\widehat v\). Use structural induction or uniqueness of recursive definitions to prove uniqueness.",
    ),
    A(
        label="def:satisfaction-propositional-formula",
        kind="definition",
        title="Satisfaction of a Formula",
        body=r"""
Let \(v\) be a truth assignment and let \(\varphi\in\WFF\). We say that \(v\) satisfies \(\varphi\), written
\[
v\models\varphi,
\]
if
\[
\widehat v(\varphi)=\mathrm{True}.
\]
""",
        quantified_form=r"""
\[
v\models\varphi
\Longleftrightarrow
TruthAssignment(v)
\land
\varphi\in\WFF
\land
\widehat v(\varphi)=\mathrm{True}.
\]
""",
        predicate_reading=r"""
\[
SatisfiesFormula(v,\varphi)
\]
means \(v\models\varphi\).
""",
        negated_form=r"""
\[
v\not\models\varphi
\Longleftrightarrow
\widehat v(\varphi)=\mathrm{False}.
\]
""",
        interpretation=r"The notation \(v\models\varphi\) means that the formula \(\varphi\) is true under the truth assignment \(v\).",
        dependencies=["def:truth-assignment-propositional-logic", "thm:unique-extension-truth-assignment-propositional-logic", "def:well-formed-formula"],
        predicates=pred(defines=["SatisfiesFormula"], uses=["TruthAssignment", "WellFormedFormula"]),
        notations={"defines": [SAT_FORMULA], "uses": [notation(r"v", "truth assignment", "truth assignment on propositional variables"), notation(r"\widehat v", "extended truth assignment", "unique extension to formulas"), WFF, FORMULAS]},
    ),
    A(
        label="def:satisfaction-set-propositional-logic",
        kind="definition",
        title="Satisfaction of a Set of Formulas",
        body=r"""
Let \(\Gamma\subseteq\WFF\). A truth assignment \(v\) satisfies \(\Gamma\), written
\[
v\models\Gamma,
\]
if \(v\models\gamma\) for every \(\gamma\in\Gamma\).
""",
        quantified_form=r"""
\[
v\models\Gamma
\Longleftrightarrow
TruthAssignment(v)
\land
\Gamma\subseteq\WFF
\land
(\forall\gamma\in\Gamma)(v\models\gamma).
\]
""",
        predicate_reading=r"""
\[
SatisfiesSet(v,\Gamma)
\]
means \(v\) satisfies every formula in \(\Gamma\).
""",
        negated_form=r"""
\[
v\not\models\Gamma
\Longleftrightarrow
\exists\gamma\in\Gamma\text{ such that }v\not\models\gamma.
\]
""",
        interpretation="Satisfaction of a set means simultaneous satisfaction of every formula in the set.",
        dependencies=["def:satisfaction-propositional-formula", "def:truth-assignment-propositional-logic"],
        predicates=pred(defines=["SatisfiesSet"], uses=["TruthAssignment", "SatisfiesFormula", "WellFormedFormula"]),
        notations={"defines": [SAT_SET, GAMMA], "uses": [SAT_FORMULA, WFF]},
    ),
    A(
        label="def:truth-table-propositional-logic",
        kind="definition",
        title="Truth Table",
        body=r"""
Let \(\varphi\in\WFF\) and suppose the variables occurring in \(\varphi\) are among \(P_1,\ldots,P_n\). A truth table for \(\varphi\) is a finite table with one row for each assignment
\[
a:\{P_1,\ldots,P_n\}\to\mathbb{B}
\]
and a final column recording the value of \(\widehat v(\varphi)\) for any truth assignment \(v\) extending \(a\).
""",
        quantified_form=r"""
\[
TruthTable(\varphi)
\Longleftrightarrow
\varphi\in\WFF
\land
\operatorname{Var}(\varphi)=\{P_1,\ldots,P_n\}
\land
\text{the table has }2^n\text{ assignment rows}.
\]
""",
        interpretation="A truth table is finite because every formula contains only finitely many variables. It records the complete truth behavior of a formula.",
        dependencies=["def:formula-variable-set-propositional-logic", "lem:finiteness-of-variables-propositional-formulas", "thm:unique-extension-truth-assignment-propositional-logic"],
        predicates=pred(defines=["TruthTable"], uses=["WellFormedFormula", "FormulaVariableSet", "TruthAssignment"]),
        notations={"defines": [], "uses": [VARS, FINITE_VARS, TRUTH_VALUE, notation(r"\widehat v", "extended truth assignment", "unique extension to formulas")]},
    ),
    A(
        label="def:tautology-propositional-logic",
        kind="definition",
        title="Tautology",
        body=r"""
A formula \(\varphi\in\WFF\) is a tautology, written
\[
\models\varphi,
\]
if every truth assignment satisfies \(\varphi\).
""",
        quantified_form=r"""
\[
\models\varphi
\Longleftrightarrow
\varphi\in\WFF
\land
(\forall v:\Prop\to\mathbb{B})(v\models\varphi).
\]
""",
        predicate_reading=r"""
\[
Tautology(\varphi)
\]
means \(\models\varphi\).
""",
        interpretation="A tautology is true under every possible assignment of truth values to propositional variables.",
        dependencies=["def:satisfaction-propositional-formula", "def:truth-assignment-propositional-logic"],
        predicates=pred(defines=["Tautology"], uses=["TruthAssignment", "SatisfiesFormula", "WellFormedFormula"]),
        notations={"defines": [VALIDITY], "uses": [SAT_FORMULA, PROP, TRUTH_VALUE]},
    ),
    A(
        label="def:contradiction-propositional-logic",
        kind="definition",
        title="Contradiction",
        body=r"A formula \(\varphi\in\WFF\) is a contradiction if no truth assignment satisfies \(\varphi\).",
        quantified_form=r"""
\[
Contradiction(\varphi)
\Longleftrightarrow
\varphi\in\WFF
\land
(\forall v:\Prop\to\mathbb{B})(v\not\models\varphi).
\]
""",
        predicate_reading=r"""
\[
Contradiction(\varphi)
\]
means that \(\varphi\) is false under every truth assignment.
""",
        interpretation="A contradiction has no true row in its truth table.",
        dependencies=["def:satisfaction-propositional-formula", "def:truth-assignment-propositional-logic"],
        predicates=pred(defines=["Contradiction"], uses=["TruthAssignment", "SatisfiesFormula", "WellFormedFormula"]),
        notations={"defines": [], "uses": [SAT_FORMULA, WFF]},
    ),
    A(
        label="def:satisfiable-formula-propositional-logic",
        kind="definition",
        title="Satisfiable Formula",
        body=r"A formula \(\varphi\in\WFF\) is satisfiable if at least one truth assignment satisfies it.",
        quantified_form=r"""
\[
SatisfiableFormula(\varphi)
\Longleftrightarrow
\varphi\in\WFF
\land
\exists v:\Prop\to\mathbb{B}\text{ such that }v\models\varphi.
\]
""",
        predicate_reading=r"""
\[
SatisfiableFormula(\varphi)
\]
means that \(\varphi\) is true under at least one truth assignment.
""",
        interpretation="A satisfiable formula has at least one true row in its truth table.",
        dependencies=["def:satisfaction-propositional-formula", "def:truth-assignment-propositional-logic"],
        predicates=pred(defines=["SatisfiableFormula"], uses=["TruthAssignment", "SatisfiesFormula", "WellFormedFormula"]),
        notations={"defines": [], "uses": [SAT_FORMULA, PROP, TRUTH_VALUE]},
    ),
    A(
        label="def:contingency-propositional-logic",
        kind="definition",
        title="Contingency",
        body=r"A formula \(\varphi\in\WFF\) is a contingency if it is satisfiable but not a tautology.",
        quantified_form=r"""
\[
Contingency(\varphi)
\Longleftrightarrow
SatisfiableFormula(\varphi)
\land
\neg Tautology(\varphi).
\]
""",
        predicate_reading=r"""
\[
Contingency(\varphi)
\]
means that \(\varphi\) is true under some truth assignments and false under others.
""",
        interpretation="A contingency has at least one true row and at least one false row in its truth table.",
        dependencies=["def:satisfiable-formula-propositional-logic", "def:tautology-propositional-logic"],
        predicates=pred(defines=["Contingency"], uses=["SatisfiableFormula", "Tautology", "WellFormedFormula"]),
    ),
    A(
        label="def:logical-consequence-propositional-logic",
        kind="definition",
        title="Logical Consequence",
        body=r"""
Let \(\Gamma\subseteq\WFF\) and \(\varphi\in\WFF\). The formula \(\varphi\) is a logical consequence of \(\Gamma\), written
\[
\Gamma\models\varphi,
\]
if every truth assignment satisfying \(\Gamma\) also satisfies \(\varphi\).
""",
        quantified_form=r"""
\[
\Gamma\models\varphi
\Longleftrightarrow
\Gamma\subseteq\WFF
\land
\varphi\in\WFF
\land
(\forall v:\Prop\to\mathbb{B})
\left[
v\models\Gamma\to v\models\varphi
\right].
\]
""",
        predicate_reading=r"""
\[
LogicalConsequence(\Gamma,\varphi)
\]
means \(\Gamma\models\varphi\).
""",
        negated_form=r"""
\[
\Gamma\not\models\varphi
\Longleftrightarrow
\exists v:\Prop\to\mathbb{B}
\left[
v\models\Gamma
\land
v\not\models\varphi
\right].
\]
""",
        interpretation="Logical consequence means truth preservation from premises to conclusion. There is no truth assignment under which all premises are true and the conclusion is false.",
        dependencies=["def:satisfaction-set-propositional-logic", "def:satisfaction-propositional-formula"],
        predicates=pred(defines=["LogicalConsequence"], uses=["TruthAssignment", "SatisfiesSet", "SatisfiesFormula", "WellFormedFormula"]),
        notations={"defines": [CONSEQUENCE], "uses": [SAT_SET, SAT_FORMULA, GAMMA, WFF]},
    ),
    A(
        label="def:logical-equivalence-propositional-logic",
        kind="definition",
        title="Logical Equivalence",
        body=r"""
Formulas \(\varphi,\psi\in\WFF\) are logically equivalent, written
\[
\varphi\equiv\psi,
\]
if they have the same truth value under every truth assignment.
""",
        quantified_form=r"""
\[
\varphi\equiv\psi
\Longleftrightarrow
\varphi,\psi\in\WFF
\land
(\forall v:\Prop\to\mathbb{B})
\left[
\widehat v(\varphi)=\widehat v(\psi)
\right].
\]
""",
        predicate_reading=r"""
\[
LogicalEquivalence(\varphi,\psi)
\]
means \(\varphi\equiv\psi\).
""",
        interpretation="Logically equivalent formulas have identical truth-table columns. They are interchangeable for semantic purposes.",
        dependencies=["thm:unique-extension-truth-assignment-propositional-logic", "def:truth-assignment-propositional-logic"],
        predicates=pred(defines=["LogicalEquivalence"], uses=["TruthAssignment", "WellFormedFormula"]),
        notations={"defines": [EQUIV], "uses": [notation(r"\widehat v", "extended truth assignment", "unique extension to formulas"), WFF, PROP, TRUTH_VALUE]},
    ),
    A(
        label="lem:coincidence-lemma-propositional-logic",
        kind="lemma",
        title="Coincidence Lemma for Propositional Logic",
        body=r"""
Let \(v,w:\Prop\to\mathbb{B}\) be truth assignments. If \(v\) and \(w\) agree on every propositional variable occurring in \(\varphi\), then they assign the same truth value to \(\varphi\):
\[
v|_{\operatorname{Var}(\varphi)}
=
w|_{\operatorname{Var}(\varphi)}
\Longrightarrow
\widehat v(\varphi)=\widehat w(\varphi).
\]
""",
        quantified_form=r"""
\[
(\forall\varphi\in\WFF)
(\forall v,w:\Prop\to\mathbb{B})
\left[
(\forall P\in\operatorname{Var}(\varphi))(v(P)=w(P))
\to
\widehat v(\varphi)=\widehat w(\varphi)
\right].
\]
""",
        interpretation="The truth value of a formula depends only on the variables actually occurring in that formula.",
        dependencies=["def:formula-variable-set-propositional-logic", "thm:unique-extension-truth-assignment-propositional-logic", "thm:structural-induction-propositional-formulas"],
        predicates=pred(uses=["TruthAssignment", "FormulaVariableSet", "WellFormedFormula"]),
        notations={"defines": [], "uses": [VARS, EXTENDED_VALUATION, WFF, PROP, TRUTH_VALUE]},
        proof_required=True,
        proof_sketch=r"Prove by structural induction on \(\varphi\). Atomic case follows from agreement on variables. Negation and binary connective cases follow from the induction hypothesis and the recursive truth clauses.",
    ),
    A(
        label="thm:finite-truth-table-propositional-logic",
        kind="theorem",
        title="Finite Truth-Table Theorem",
        body=r"Every propositional formula has a finite truth table. More precisely, if \(\operatorname{Var}(\varphi)\) has \(n\) elements, then \(\varphi\) has a truth table with \(2^n\) rows.",
        quantified_form=r"""
\[
(\forall\varphi\in\WFF)
\left[
|\operatorname{Var}(\varphi)|=n
\to
TruthTable(\varphi)\text{ has }2^n\text{ rows}
\right].
\]
""",
        interpretation="Truth tables are finite because every formula contains only finitely many propositional variables.",
        dependencies=["def:truth-table-propositional-logic", "lem:finiteness-of-variables-propositional-formulas"],
        predicates=pred(uses=["TruthTable", "FormulaVariableSet", "WellFormedFormula"]),
        notations={"defines": [], "uses": [VARS, WFF]},
        proof_required=True,
        proof_sketch=r"Use finiteness of \(\operatorname{Var}(\varphi)\). If there are \(n\) variables, then there are \(2^n\) functions from that finite variable set to \(\mathbb{B}\).",
    ),
    A(
        label="def:boolean-function-propositional-logic",
        kind="definition",
        title="Boolean Function",
        body=r"""
An \(n\)-ary Boolean function is a function
\[
f:\mathbb{B}^n\to\mathbb{B}.
\]
""",
        quantified_form=r"""
\[
BooleanFunction_n(f)
\Longleftrightarrow
f:\mathbb{B}^n\to\mathbb{B}.
\]
""",
        predicate_reading=r"""
\[
BooleanFunction_n(f)
\]
means that \(f\) takes \(n\) truth values as input and returns one truth value.
""",
        interpretation="Boolean functions are the abstract truth-functions that formulas may represent.",
        dependencies=["def:truth-value-propositional-logic"],
        predicates=pred(defines=["BooleanFunction"], uses=[]),
        notations={"defines": [BOOLEAN_FUNCTION], "uses": [TRUTH_VALUE]},
    ),
    A(
        label="def:truth-function-induced-by-formula",
        kind="definition",
        title="Truth Function Induced by a Formula",
        body=r"""
Let \(\varphi\in\WFF\), and suppose \(\operatorname{Var}(\varphi)\subseteq\{P_1,\ldots,P_n\}\). The truth function induced by \(\varphi\) is the Boolean function
\[
f_\varphi:\mathbb{B}^n\to\mathbb{B}
\]
defined by
\[
f_\varphi(b_1,\ldots,b_n)=\widehat v(\varphi),
\]
where \(v(P_i)=b_i\) for each \(i\).
""",
        quantified_form=r"""
\[
f_\varphi(b_1,\ldots,b_n)=\widehat v(\varphi)
\quad
\text{whenever }
v(P_i)=b_i\text{ for }1\le i\le n.
\]
""",
        predicate_reading=r"""
\[
TruthFunctionOfFormula(f_\varphi,\varphi)
\]
means that \(f_\varphi\) records the truth behavior of \(\varphi\).
""",
        interpretation="The induced truth function packages the truth table of a formula as a Boolean function.",
        dependencies=["def:boolean-function-propositional-logic", "def:formula-variable-set-propositional-logic", "thm:unique-extension-truth-assignment-propositional-logic", "lem:coincidence-lemma-propositional-logic"],
        predicates=pred(defines=["TruthFunctionOfFormula"], uses=["BooleanFunction", "WellFormedFormula", "FormulaVariableSet"]),
        notations={"defines": [INDUCED_FUNCTION], "uses": [TRUTH_VALUE, notation(r"\widehat v", "extended truth assignment", "unique extension to formulas"), VARS, FINITE_VARS]},
    ),
    A(
        label="thm:counting-boolean-functions",
        kind="theorem",
        title="Counting Boolean Functions",
        body=r"""
There are exactly
\[
2^{2^n}
\]
Boolean functions \(\mathbb{B}^n\to\mathbb{B}\).
""",
        quantified_form=r"""
\[
\left|\{f:\mathbb{B}^n\to\mathbb{B}\}\right|=2^{2^n}.
\]
""",
        interpretation=r"The domain \(\mathbb{B}^n\) has \(2^n\) elements. A Boolean function chooses one of two truth values for each input row.",
        dependencies=["def:boolean-function-propositional-logic"],
        predicates=pred(uses=["BooleanFunction"]),
        notations={"defines": [], "uses": [TRUTH_VALUE]},
        proof_required=True,
        proof_sketch=r"Count functions from a \(2^n\)-element set to a \(2\)-element set.",
    ),
]


payload = {
    "schema_version": 1,
    "chapter": "propositional-logic",
    "topic": "semantics",
    "artifacts": artifacts,
}

out = Path("payloads/propositional-logic/semantics.full.json")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Wrote {out} with {len(artifacts)} artifacts.")
