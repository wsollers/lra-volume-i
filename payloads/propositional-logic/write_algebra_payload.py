from __future__ import annotations

import base64
import json
import re
from pathlib import Path
from typing import Any


PREDICATE_NAMES = (
    "PropositionalVariable",
    "WellFormedFormula",
    "LogicalEquivalence",
    "PropositionalEquivalenceLaw",
    "TruthAssignment",
    "Tautology",
    "Contradiction",
    "FormulaContext",
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


def notation(
    symbol: str,
    name: str,
    meaning: str,
    scope: str = "chapter",
    status: str = "canonical",
    introduced_by: str | None = None,
    registry_id: str | None = None,
):
    row = {"symbol": symbol, "name": name, "meaning": meaning, "scope": scope, "status": status}
    if introduced_by:
        row["introduced_by"] = introduced_by
    if registry_id:
        row["registry_id"] = registry_id
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
    readable_decomposition: str | None = None,
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
        "readable_decomposition": readable_decomposition,
        "proof_sketch": proof_sketch,
    }.items():
        if value is not None:
            obj[f"{key}_b64"] = b64(value)
    return obj


WFF = notation(r"\WFF", "well-formed formula set", "the set of propositional well-formed formulas", "chapter", "canonical")
FORMULAS = notation(r"\varphi,\psi,\chi,\theta", "formula metavariables", "metavariables ranging over propositional well-formed formulas", "global", "canonical")
EQUIV_FORMULA = notation(r"\varphi\equiv\psi", "logical equivalence", "same truth value under every truth assignment", "chapter", "canonical")
EQUIV = notation(r"\equiv", "logical equivalence symbol", "logical equivalence relation between formulas", "chapter", "canonical")
NEG = notation(r"\neg", "negation", "unary propositional connective", "global", "canonical")
AND = notation(r"\land", "conjunction", "binary propositional connective", "global", "canonical")
OR = notation(r"\lor", "disjunction", "binary propositional connective", "global", "canonical")
COND = notation(r"\to", "conditional", "binary propositional connective", "global", "canonical")
BICOND = notation(r"\leftrightarrow", "biconditional", "binary propositional connective", "global", "canonical")
TOP = notation(r"\top", "tautological formula", "a formula chosen as a true constant", "chapter", "canonical", "thm:identity-domination-laws-propositional-logic", "propositional_logic.truth_constant_top")
BOT = notation(r"\bot", "contradictory formula", "a formula chosen as a false constant", "chapter", "canonical", "thm:identity-domination-laws-propositional-logic", "propositional_logic.truth_constant_bottom")
CONTEXT = notation(r"C[-]", "formula context", "a one-hole propositional formula context", "chapter", "canonical", "def:formula-context-propositional-logic", "propositional_logic.formula_context")
CONTEXT_SUB = notation(r"C[\varphi]", "context substitution", "formula obtained by filling a context with a formula", "chapter", "canonical", "def:formula-context-propositional-logic", "propositional_logic.formula_context_substitution")


artifacts = [
    A(
        label="def:propositional-equivalence-law",
        kind="definition",
        title="Propositional Equivalence Law",
        body=r"""
A propositional equivalence law is a valid schema of the form
\[
\varphi\equiv\psi,
\]
with \(\varphi,\psi\in\WFF\). Each instance of the schema says that the two formulas have the same truth value under every truth assignment.
""",
        quantified_form=r"""
\[
\operatorname{PropositionalEquivalenceLaw}(\varphi,\psi)
\Longleftrightarrow
\varphi,\psi\in\WFF
\land
\varphi\equiv\psi.
\]
""",
        predicate_reading=r"""
\[
\operatorname{PropositionalEquivalenceLaw}(\varphi,\psi)
\]
means that \(\varphi\equiv\psi\) is a valid logical-equivalence schema.
""",
        interpretation="Equivalence laws are the algebraic rewrite rules of propositional logic. They allow formulas to be transformed without changing truth conditions.",
        dependencies=["def:logical-equivalence-propositional-logic", "def:well-formed-formula"],
        predicates=pred(defines=["PropositionalEquivalenceLaw"], uses=["LogicalEquivalence", "WellFormedFormula"]),
        notations={"defines": [], "uses": [EQUIV_FORMULA, WFF]},
    ),
    A(
        label="thm:logical-equivalence-equivalence-relation",
        kind="theorem",
        title="Logical Equivalence is an Equivalence Relation",
        body=r"""
Logical equivalence is reflexive, symmetric, and transitive on \(\WFF\):
\[
\varphi\equiv\varphi,
\qquad
\varphi\equiv\psi\Longrightarrow\psi\equiv\varphi,
\]
and
\[
(\varphi\equiv\psi\land\psi\equiv\chi)
\Longrightarrow
\varphi\equiv\chi.
\]
""",
        quantified_form=r"""
\[
\begin{aligned}
&(\forall\varphi\in\WFF)(\varphi\equiv\varphi),\\
&(\forall\varphi,\psi\in\WFF)(\varphi\equiv\psi\to\psi\equiv\varphi),\\
&(\forall\varphi,\psi,\chi\in\WFF)
((\varphi\equiv\psi\land\psi\equiv\chi)\to\varphi\equiv\chi).
\end{aligned}
\]
""",
        interpretation="Logical equivalence behaves like equality at the semantic level.",
        dependencies=["def:logical-equivalence-propositional-logic"],
        predicates=pred(uses=["LogicalEquivalence", "WellFormedFormula"]),
        notations={"defines": [], "uses": [EQUIV_FORMULA, WFF, FORMULAS]},
        proof_required=True,
        proof_sketch="Unfold logical equivalence as equality of truth values under every truth assignment.",
    ),
    A(
        label="thm:basic-boolean-equivalence-laws-propositional-logic",
        kind="theorem",
        title="Basic Boolean Equivalence Laws",
        body=r"""
For all formulas \(\varphi,\psi,\chi\in\WFF\), the following logical equivalences hold.

Commutativity:
\[
\varphi\land\psi\equiv\psi\land\varphi,
\qquad
\varphi\lor\psi\equiv\psi\lor\varphi.
\]

Associativity:
\[
(\varphi\land\psi)\land\chi
\equiv
\varphi\land(\psi\land\chi),
\qquad
(\varphi\lor\psi)\lor\chi
\equiv
\varphi\lor(\psi\lor\chi).
\]

Idempotence:
\[
\varphi\land\varphi\equiv\varphi,
\qquad
\varphi\lor\varphi\equiv\varphi.
\]

Double negation:
\[
\neg\neg\varphi\equiv\varphi.
\]
""",
        quantified_form=r"""
\[
(\forall\varphi,\psi,\chi\in\WFF)
\left[
\begin{gathered}
\varphi\land\psi\equiv\psi\land\varphi,\quad
\varphi\lor\psi\equiv\psi\lor\varphi,\\
(\varphi\land\psi)\land\chi\equiv\varphi\land(\psi\land\chi),\quad
(\varphi\lor\psi)\lor\chi\equiv\varphi\lor(\psi\lor\chi),\\
\varphi\land\varphi\equiv\varphi,\quad
\varphi\lor\varphi\equiv\varphi,\quad
\neg\neg\varphi\equiv\varphi
\end{gathered}
\right].
\]
""",
        interpretation="These are the basic algebraic laws for conjunction, disjunction, and negation.",
        dependencies=["def:logical-equivalence-propositional-logic", "thm:unique-extension-truth-assignment-propositional-logic"],
        predicates=pred(uses=["LogicalEquivalence", "WellFormedFormula"]),
        notations={"defines": [], "uses": [EQUIV, AND, OR, NEG, FORMULAS, WFF]},
        proof_required=True,
        proof_sketch=r"Prove each equivalence by truth-table calculation or by unfolding the semantic clauses for \(\widehat v\).",
    ),
    A(
        label="thm:identity-domination-laws-propositional-logic",
        kind="theorem",
        title="Identity and Domination Laws",
        body=r"""
Let \(\top\) be any tautological formula and let \(\bot\) be any contradictory formula. Then for every \(\varphi\in\WFF\):
\[
\varphi\land\top\equiv\varphi,
\qquad
\varphi\lor\bot\equiv\varphi,
\]
and
\[
\varphi\land\bot\equiv\bot,
\qquad
\varphi\lor\top\equiv\top.
\]
""",
        quantified_form=r"""
\[
\begin{aligned}
&(\operatorname{Tautology}(\top)\land \operatorname{Contradiction}(\bot))
\to
(\forall\varphi\in\WFF)\\
&\quad
\left[
(\varphi\land\top\equiv\varphi)
\land
(\varphi\lor\bot\equiv\varphi)
\land
(\varphi\land\bot\equiv\bot)
\land
(\varphi\lor\top\equiv\top)
\right].
\end{aligned}
\]
""",
        interpretation="Tautologies act like true constants; contradictions act like false constants.",
        dependencies=["def:tautology-propositional-logic", "def:contradiction-propositional-logic", "def:logical-equivalence-propositional-logic"],
        predicates=pred(uses=["Tautology", "Contradiction", "LogicalEquivalence", "WellFormedFormula"]),
        notations={"defines": [TOP, BOT], "uses": [AND, OR, EQUIV, WFF]},
        proof_required=True,
        proof_sketch="Evaluate both sides under an arbitrary truth assignment.",
    ),
    A(
        label="thm:de-morgan-laws-propositional-logic",
        kind="theorem",
        title="De Morgan Laws for Propositional Logic",
        body=r"""
For all \(\varphi,\psi\in\WFF\),
\[
\neg(\varphi\land\psi)
\equiv
\neg\varphi\lor\neg\psi,
\]
and
\[
\neg(\varphi\lor\psi)
\equiv
\neg\varphi\land\neg\psi.
\]
""",
        quantified_form=r"""
\[
\begin{gathered}
(\forall\varphi,\psi\in\WFF)
\left[
\neg(\varphi\land\psi)
\equiv
\neg\varphi\lor\neg\psi
\right],\\
(\forall\varphi,\psi\in\WFF)
\left[
\neg(\varphi\lor\psi)
\equiv
\neg\varphi\land\neg\psi
\right].
\end{gathered}
\]
""",
        readable_decomposition=r"""
\[
\underbrace{\neg(\varphi\land\psi)}_{\text{not both}}
\equiv
\underbrace{\neg\varphi\lor\neg\psi}_{\text{at least one fails}},
\qquad
\underbrace{\neg(\varphi\lor\psi)}_{\text{neither}}
\equiv
\underbrace{\neg\varphi\land\neg\psi}_{\text{both fail}}.
\]
""",
        interpretation="Negation swaps conjunction with disjunction when pushed inward.",
        dependencies=["def:logical-equivalence-propositional-logic", "thm:unique-extension-truth-assignment-propositional-logic"],
        predicates=pred(uses=["LogicalEquivalence", "WellFormedFormula"]),
        notations={"defines": [], "uses": [NEG, AND, OR, EQUIV, WFF, FORMULAS]},
        proof_required=True,
        proof_sketch=r"Use a two-variable truth table or unfold the semantic clauses for \(\neg,\land,\lor\).",
    ),
    A(
        label="thm:distributive-laws-propositional-logic",
        kind="theorem",
        title="Distributive Laws for Propositional Logic",
        body=r"""
For all \(\varphi,\psi,\chi\in\WFF\),
\[
\varphi\land(\psi\lor\chi)
\equiv
(\varphi\land\psi)\lor(\varphi\land\chi),
\]
and
\[
\varphi\lor(\psi\land\chi)
\equiv
(\varphi\lor\psi)\land(\varphi\lor\chi).
\]
""",
        quantified_form=r"""
\[
\begin{gathered}
(\forall\varphi,\psi,\chi\in\WFF)
\left[
\varphi\land(\psi\lor\chi)
\equiv
(\varphi\land\psi)\lor(\varphi\land\chi)
\right],\\
(\forall\varphi,\psi,\chi\in\WFF)
\left[
\varphi\lor(\psi\land\chi)
\equiv
(\varphi\lor\psi)\land(\varphi\lor\chi)
\right].
\end{gathered}
\]
""",
        interpretation="Conjunction distributes over disjunction, and disjunction distributes over conjunction. These laws are the main algebraic engine behind CNF and DNF conversion.",
        dependencies=["def:logical-equivalence-propositional-logic", "thm:unique-extension-truth-assignment-propositional-logic"],
        predicates=pred(uses=["LogicalEquivalence", "WellFormedFormula"]),
        notations={"defines": [], "uses": [AND, OR, EQUIV, WFF, FORMULAS]},
        proof_required=True,
        proof_sketch="Use a three-variable truth table or semantic case analysis.",
    ),
    A(
        label="thm:absorption-laws-propositional-logic",
        kind="theorem",
        title="Absorption Laws",
        body=r"""
For all \(\varphi,\psi\in\WFF\),
\[
\varphi\land(\varphi\lor\psi)\equiv\varphi,
\]
and
\[
\varphi\lor(\varphi\land\psi)\equiv\varphi.
\]
""",
        quantified_form=r"""
\[
\begin{gathered}
(\forall\varphi,\psi\in\WFF)
\left[
\varphi\land(\varphi\lor\psi)\equiv\varphi
\right],\\
(\forall\varphi,\psi\in\WFF)
\left[
\varphi\lor(\varphi\land\psi)\equiv\varphi
\right].
\end{gathered}
\]
""",
        interpretation="Once \\(\\varphi\\) is already required, adding \\(\\varphi\\lor\\psi\\) contributes no additional constraint. Dually, once \\(\\varphi\\) is already allowed, adding \\(\\varphi\\land\\psi\\) contributes no additional possibility.",
        dependencies=["def:logical-equivalence-propositional-logic", "thm:basic-boolean-equivalence-laws-propositional-logic", "thm:distributive-laws-propositional-logic"],
        predicates=pred(uses=["LogicalEquivalence", "WellFormedFormula"]),
        notations={"defines": [], "uses": [AND, OR, EQUIV, WFF, FORMULAS]},
        proof_required=True,
        proof_sketch="Prove by truth table or derive algebraically from distributivity, idempotence, and identity laws.",
    ),
    A(
        label="thm:conditional-equivalence-laws-propositional-logic",
        kind="theorem",
        title="Conditional Equivalence Laws",
        body=r"""
For all \(\varphi,\psi\in\WFF\),
\[
\varphi\to\psi
\equiv
\neg\varphi\lor\psi,
\]
and
\[
\neg(\varphi\to\psi)
\equiv
\varphi\land\neg\psi.
\]
""",
        quantified_form=r"""
\[
\begin{gathered}
(\forall\varphi,\psi\in\WFF)
\left[
\varphi\to\psi
\equiv
\neg\varphi\lor\psi
\right],\\
(\forall\varphi,\psi\in\WFF)
\left[
\neg(\varphi\to\psi)
\equiv
\varphi\land\neg\psi
\right].
\end{gathered}
\]
""",
        readable_decomposition=r"""
\[
\underbrace{\varphi\to\psi}_{\text{no counterexample}}
\equiv
\underbrace{\neg\varphi\lor\psi}_{\text{premise false or conclusion true}},
\qquad
\underbrace{\neg(\varphi\to\psi)}_{\text{counterexample}}
\equiv
\underbrace{\varphi\land\neg\psi}_{\text{premise true and conclusion false}}.
\]
""",
        interpretation="A conditional fails exactly when the antecedent is true and the consequent is false.",
        dependencies=["def:logical-equivalence-propositional-logic", "thm:unique-extension-truth-assignment-propositional-logic"],
        predicates=pred(uses=["LogicalEquivalence", "WellFormedFormula"]),
        notations={"defines": [], "uses": [COND, NEG, OR, AND, EQUIV, WFF, FORMULAS]},
        proof_required=True,
        proof_sketch="Use the semantic truth clause for implication.",
    ),
    A(
        label="thm:biconditional-equivalence-laws-propositional-logic",
        kind="theorem",
        title="Biconditional Equivalence Laws",
        body=r"""
For all \(\varphi,\psi\in\WFF\),
\[
\varphi\leftrightarrow\psi
\equiv
(\varphi\to\psi)\land(\psi\to\varphi),
\]
and
\[
\varphi\leftrightarrow\psi
\equiv
(\varphi\land\psi)\lor(\neg\varphi\land\neg\psi).
\]
""",
        quantified_form=r"""
\[
\begin{gathered}
(\forall\varphi,\psi\in\WFF)
\left[
\varphi\leftrightarrow\psi
\equiv
(\varphi\to\psi)\land(\psi\to\varphi)
\right],\\
(\forall\varphi,\psi\in\WFF)
\left[
\varphi\leftrightarrow\psi
\equiv
(\varphi\land\psi)\lor(\neg\varphi\land\neg\psi)
\right].
\end{gathered}
\]
""",
        interpretation="A biconditional says that two formulas have the same truth value: both true or both false.",
        dependencies=["def:logical-equivalence-propositional-logic", "thm:conditional-equivalence-laws-propositional-logic"],
        predicates=pred(uses=["LogicalEquivalence", "WellFormedFormula"]),
        notations={"defines": [], "uses": [BICOND, COND, AND, OR, NEG, EQUIV, WFF, FORMULAS]},
        proof_required=True,
        proof_sketch="Use the truth clause for biconditional, or rewrite using the conditional equivalence laws.",
    ),
    A(
        label="def:formula-context-propositional-logic",
        kind="definition",
        title="Formula Context",
        body=r"""
A formula context \(C[-]\) is a well-formed formula with one distinguished placeholder occurrence \([-]\). For each well-formed formula \(\varphi\), the expression \(C[\varphi]\) denotes the formula obtained by replacing the placeholder with \(\varphi\).
""",
        quantified_form=r"""
\[
\operatorname{FormulaContext}(C[-])
\Longrightarrow
(\forall\varphi\in\WFF)(C[\varphi]\in\WFF).
\]
""",
        predicate_reading=r"""
\[
\operatorname{FormulaContext}(C[-])
\]
means that \(C[-]\) is a one-hole propositional formula context.
""",
        interpretation="A formula context is a syntactic environment into which a formula can be inserted. Contexts make precise the idea of replacing a subformula inside a larger formula.",
        dependencies=["def:well-formed-formula", "def:subformula-propositional-logic"],
        predicates=pred(defines=["FormulaContext"], uses=["WellFormedFormula", "Subformula"]),
        notations={"defines": [CONTEXT, CONTEXT_SUB], "uses": [WFF]},
    ),
    A(
        label="thm:replacement-of-logical-equivalents-propositional-logic",
        kind="theorem",
        title="Replacement of Logical Equivalents",
        body=r"""
Replacing logically equivalent formulas inside a formula context preserves logical equivalence:
\[
\varphi\equiv\psi
\Longrightarrow
C[\varphi]\equiv C[\psi].
\]
""",
        quantified_form=r"""
\[
(\forall\varphi,\psi\in\WFF)
(\forall C[-])
\left[
\operatorname{FormulaContext}(C[-])
\land
\varphi\equiv\psi
\to
C[\varphi]\equiv C[\psi]
\right].
\]
""",
        interpretation="Logical equivalence is substitutive: equivalent formulas may be replaced inside larger formulas without changing truth behavior.",
        dependencies=["def:formula-context-propositional-logic", "def:logical-equivalence-propositional-logic", "lem:coincidence-lemma-propositional-logic", "thm:unique-extension-truth-assignment-propositional-logic"],
        predicates=pred(uses=["FormulaContext", "LogicalEquivalence", "WellFormedFormula"]),
        notations={"defines": [], "uses": [CONTEXT, CONTEXT_SUB, EQUIV_FORMULA, WFF]},
        proof_required=True,
        proof_sketch=r"Prove by structural induction on the context \(C[-]\). The placeholder case uses \(\varphi\equiv\psi\). The connective cases follow from the semantic truth clauses.",
    ),
    A(
        label="rem:algebraic-role-of-propositional-laws",
        kind="remark",
        title="Algebraic Role of Propositional Laws",
        body="The laws in this section allow formulas to be manipulated algebraically. They are not new formation rules; they are semantic equivalences. Later sections use these laws to transform formulas into normal forms and to reduce the set of primitive connectives.",
        interpretation="The algebra of propositions is the bridge from semantics to computation: once formulas are equivalent, they can be rewritten without changing truth behavior.",
        dependencies=["def:logical-equivalence-propositional-logic", "thm:replacement-of-logical-equivalents-propositional-logic"],
        predicates=pred(uses=["LogicalEquivalence"]),
        notations={"defines": [], "uses": [EQUIV]},
    ),
]


payload = {
    "schema_version": 1,
    "chapter": "propositional-logic",
    "topic": "algebra",
    "artifacts": artifacts,
}

out = Path("payloads/propositional-logic/algebra.full.json")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Wrote {out} with {len(artifacts)} artifacts.")
