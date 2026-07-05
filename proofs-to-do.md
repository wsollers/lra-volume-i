# Volume I - Logic, Sets, and Proof Proofs To Do

Proof-writing order is dependency-first among active TODO proof labels, with the generated knowledge graph order used as the stable tie-breaker.
Use `✅` to record completion after the canonical proof file has both proof bodies populated and validated.

Open proofs to do: 131
Completed in this tracker: 11

1. () `thm:logical-equivalence-equivalence-relation` — **Logical Equivalence is an Equivalence Relation**
   > **Statement.**
   > Logical equivalence is reflexive, symmetric, and transitive on \(\WFF\):
   > \[
   > \varphi\equiv\varphi,
   > \qquad
   > \varphi\equiv\psi\Longrightarrow\psi\equiv\varphi,
   > \]
   > and
   > \[
   > (\varphi\equiv\psi\land\psi\equiv\chi)
   > \Longrightarrow
   > \varphi\equiv\chi.
   > \]

2. () `thm:structural-induction-propositional-formulas` — **Structural Induction for Propositional Formulas**
   > **Statement.**
   > Let \(A(\varphi)\) be a property of well-formed formulas. Suppose:
   > - \(A(P)\) holds for every \(P\in\Prop\);
   > - if \(A(\varphi)\) holds, then \(A(\neg\varphi)\) holds;
   > - if \(A(\varphi)\) and \(A(\psi)\) hold, then \(A((\varphi\circ\psi))\) holds for every \(\circ\in\{\land,\lor,\to,\leftrightarrow\}\).
   > Then \(A(\theta)\) holds for every \(\theta\in\WFF\).

3. () `thm:structural-recursion-propositional-formulas` — **Structural Recursion for Propositional Formulas**
   > **Statement.**
   > To define a function \(F\) on \(\WFF\), it suffices to specify:
   > - \(F(P)\) for every \(P\in\Prop\);
   > - \(F(\neg\varphi)\) in terms of \(F(\varphi)\);
   > - \(F((\varphi\circ\psi))\) in terms of \(F(\varphi)\), \(F(\psi)\), and \(\circ\).
   > When these clauses respect the formation rules, they determine a unique function on \(\WFF\).

4. () `lem:constructor-disjointness-propositional-formulas` — **Constructor Disjointness for Propositional Formulas**
   > **Statement.**
   > The three outer formation cases for propositional formulas are disjoint:
   > - no propositional variable is a negation formula;
   > - no propositional variable is a binary formula;
   > - no negation formula is a binary formula.

5. () `lem:constructor-injectivity-propositional-formulas` — **Constructor Injectivity for Propositional Formulas**
   > **Statement.**
   > The propositional formula constructors are injective:
   > - if \(\neg\varphi=\neg\psi\), then \(\varphi=\psi\);
   > - if \((\varphi\circ\psi)=(\alpha\star\beta)\), then \(\varphi=\alpha\), \(\psi=\beta\), and \(\circ=\star\).

6. () `thm:unique-decomposition-propositional-formulas` — **Unique Decomposition for Propositional Formulas**
   > **Statement.**
   > Every \(\varphi\in\WFF\) has exactly one outermost form:
   > - \(\varphi=P\) for a unique \(P\in\Prop\);
   > - \(\varphi=\neg\psi\) for a unique \(\psi\in\WFF\);
   > - \(\varphi=(\psi\circ\chi)\) for unique \(\psi,\chi\in\WFF\) and a unique binary connective \(\circ\in\{\land,\lor,\to,\leftrightarrow\}\).

7. () `thm:unique-extension-truth-assignment-propositional-logic` — **Unique Extension of a Truth Assignment**
   > **Statement.**
   > Every truth assignment
   > \[
   > v:\Prop\to\mathbb{B}
   > \]
   > has a unique extension
   > \[
   > \widehat v:\WFF\to\mathbb{B}
   > \]
   > satisfying the recursive truth clauses for propositional variables and the
   > primitive connectives.

8. () `thm:basic-boolean-equivalence-laws-propositional-logic` — **Basic Boolean Equivalence Laws**
   > **Statement.**
   > For all formulas \(\varphi,\psi,\chi\in\WFF\), the following logical equivalences hold.
   >
   > Commutativity:
   > \[
   > \varphi\land\psi\equiv\psi\land\varphi,
   > \qquad
   > \varphi\lor\psi\equiv\psi\lor\varphi.
   > \]
   >
   > Associativity:
   > \[
   > (\varphi\land\psi)\land\chi
   > \equiv
   > \varphi\land(\psi\land\chi),
   > \qquad
   > (\varphi\lor\psi)\lor\chi
   > \equiv
   > \varphi\lor(\psi\lor\chi).
   > \]
   >
   > Idempotence:
   > \[
   > \varphi\land\varphi\equiv\varphi,
   > \qquad
   > \varphi\lor\varphi\equiv\varphi.
   > \]
   >
   > Double negation:
   > \[
   > \neg\neg\varphi\equiv\varphi.
   > \]

9. () `thm:identity-domination-laws-propositional-logic` — **Identity and Domination Laws**
   > **Statement.**
   > Let \(\top\) be any tautological formula and let \(\bot\) be any contradictory formula. Then for every \(\varphi\in\WFF\):
   > \[
   > \varphi\land\top\equiv\varphi,
   > \qquad
   > \varphi\lor\bot\equiv\varphi,
   > \]
   > and
   > \[
   > \varphi\land\bot\equiv\bot,
   > \qquad
   > \varphi\lor\top\equiv\top.
   > \]

10. () `thm:de-morgan-laws-propositional-logic` — **De Morgan Laws for Propositional Logic**
   > **Statement.**
   > For all \(\varphi,\psi\in\WFF\),
   > \[
   > \neg(\varphi\land\psi)
   > \equiv
   > \neg\varphi\lor\neg\psi,
   > \]
   > and
   > \[
   > \neg(\varphi\lor\psi)
   > \equiv
   > \neg\varphi\land\neg\psi.
   > \]

11. () `thm:distributive-laws-propositional-logic` — **Distributive Laws for Propositional Logic**
   > **Statement.**
   > For all \(\varphi,\psi,\chi\in\WFF\),
   > \[
   > \varphi\land(\psi\lor\chi)
   > \equiv
   > (\varphi\land\psi)\lor(\varphi\land\chi),
   > \]
   > and
   > \[
   > \varphi\lor(\psi\land\chi)
   > \equiv
   > (\varphi\lor\psi)\land(\varphi\lor\chi).
   > \]

12. () `thm:absorption-laws-propositional-logic` — **Absorption Laws**
   > **Statement.**
   > For all \(\varphi,\psi\in\WFF\),
   > \[
   > \varphi\land(\varphi\lor\psi)\equiv\varphi,
   > \]
   > and
   > \[
   > \varphi\lor(\varphi\land\psi)\equiv\varphi.
   > \]

13. () `thm:conditional-equivalence-laws-propositional-logic` — **Conditional Equivalence Laws**
   > **Statement.**
   > For all \(\varphi,\psi\in\WFF\),
   > \[
   > \varphi\to\psi
   > \equiv
   > \neg\varphi\lor\psi,
   > \]
   > and
   > \[
   > \neg(\varphi\to\psi)
   > \equiv
   > \varphi\land\neg\psi.
   > \]

14. () `thm:biconditional-equivalence-laws-propositional-logic` — **Biconditional Equivalence Laws**
   > **Statement.**
   > For all \(\varphi,\psi\in\WFF\),
   > \[
   > \varphi\leftrightarrow\psi
   > \equiv
   > (\varphi\to\psi)\land(\psi\to\varphi),
   > \]
   > and
   > \[
   > \varphi\leftrightarrow\psi
   > \equiv
   > (\varphi\land\psi)\lor(\neg\varphi\land\neg\psi).
   > \]

15. () `lem:coincidence-lemma-propositional-logic` — **Coincidence Lemma for Propositional Logic**
   > **Statement.**
   > Let \(v,w:\Prop\to\mathbb{B}\) be truth assignments. If \(v\) and \(w\) agree on every propositional variable occurring in \(\varphi\), then they assign the same truth value to \(\varphi\):
   > \[
   > v|_{\operatorname{Var}(\varphi)}
   > =
   > w|_{\operatorname{Var}(\varphi)}
   > \Longrightarrow
   > \widehat v(\varphi)=\widehat w(\varphi).
   > \]

16. () `thm:replacement-of-logical-equivalents-propositional-logic` — **Replacement of Logical Equivalents**
   > **Statement.**
   > Replacing logically equivalent formulas inside a formula context preserves logical equivalence:
   > \[
   > \varphi\equiv\psi
   > \Longrightarrow
   > C[\varphi]\equiv C[\psi].
   > \]

17. () `lem:finiteness-of-variables-propositional-formulas` — **Finiteness of Variables in a Formula**
   > **Statement.**
   > For every \(\varphi\in\WFF\), the set \(\operatorname{Var}(\varphi)\) is finite.

18. () `thm:finite-truth-table-propositional-logic` — **Finite Truth-Table Theorem**
   > **Statement.**
   > Every propositional formula has a finite truth table. More precisely, if \(\operatorname{Var}(\varphi)\) has \(n\) elements, then \(\varphi\) has a truth table with \(2^n\) rows.

19. () `thm:truth-table-validity-test-argument-forms-propositional-logic` — **Truth-Table Validity Test for Argument Forms**
   > **Statement.**
   > An argument form \((\Gamma,\varphi)\) is valid if and only if no row of its truth
   > table makes every formula in \(\Gamma\) true and \(\varphi\) false.

20. () `thm:affirming-consequent-invalid-propositional-logic` — **Affirming the Consequent is Invalid**
   > **Statement.**
   > The argument form
   > \[
   > \varphi\to\psi,\qquad \psi \quad\therefore\quad \varphi
   > \]
   > is invalid.

21. () `thm:denying-antecedent-invalid-propositional-logic` — **Denying the Antecedent is Invalid**
   > **Statement.**
   > The argument form
   > \[
   > \varphi\to\psi,\qquad \neg\varphi \quad\therefore\quad \neg\psi
   > \]
   > is invalid.

22. () `thm:replacement-rules-preserve-logical-equivalence-propositional-logic` — **Replacement Rules Preserve Logical Equivalence**
   > **Statement.**
   > If a formula \(\psi\) is obtained from a formula \(\varphi\) by finitely many
   > applications of rules of replacement, then \(\varphi\equiv\psi\).

23. () `thm:tautological-implication-valid-argument-form-propositional-logic` — **Tautological Implication Gives a Valid Argument Form**
   > **Statement.**
   > Let \(\Gamma=\{\gamma_1,\ldots,\gamma_n\}\subseteq\WFF\) and let
   > \(\varphi\in\WFF\). If
   > \[
   > (\gamma_1\land\cdots\land\gamma_n)\to\varphi
   > \]
   > is a tautology, then the argument form \((\Gamma,\varphi)\) is valid.

24. () `thm:modus-ponens-validity-propositional-logic` — **Modus Ponens is Valid**
   > **Statement.**
   > The argument form
   > \[
   > \varphi,\qquad \varphi\to\psi \quad\therefore\quad \psi
   > \]
   > is valid.

25. () `thm:modus-tollens-validity-propositional-logic` — **Modus Tollens is Valid**
   > **Statement.**
   > The argument form
   > \[
   > \varphi\to\psi,\qquad \neg\psi \quad\therefore\quad \neg\varphi
   > \]
   > is valid.

26. () `thm:hypothetical-syllogism-validity-propositional-logic` — **Hypothetical Syllogism is Valid**
   > **Statement.**
   > The argument form
   > \[
   > \varphi\to\psi,\qquad \psi\to\chi \quad\therefore\quad \varphi\to\chi
   > \]
   > is valid.

27. () `thm:disjunctive-syllogism-validity-propositional-logic` — **Disjunctive Syllogism is Valid**
   > **Statement.**
   > The argument form
   > \[
   > \varphi\lor\psi,\qquad \neg\varphi \quad\therefore\quad \psi
   > \]
   > is valid.

28. () `thm:addition-validity-propositional-logic` — **Addition is Valid**
   > **Statement.**
   > The argument form
   > \[
   > \varphi \quad\therefore\quad \varphi\lor\psi
   > \]
   > is valid.

29. () `thm:simplification-validity-propositional-logic` — **Simplification is Valid**
   > **Statement.**
   > The argument form
   > \[
   > \varphi\land\psi \quad\therefore\quad \varphi
   > \]
   > is valid.

30. () `thm:conjunction-introduction-validity-propositional-logic` — **Conjunction Introduction is Valid**
   > **Statement.**
   > The argument form
   > \[
   > \varphi,\qquad \psi \quad\therefore\quad \varphi\land\psi
   > \]
   > is valid.

31. () `thm:constructive-dilemma-validity-propositional-logic` — **Constructive Dilemma is Valid**
   > **Statement.**
   > The argument form
   > \[
   > \varphi\to\chi,\qquad \psi\to\theta,\qquad \varphi\lor\psi
   > \quad\therefore\quad
   > \chi\lor\theta
   > \]
   > is valid.

32. () `thm:destructive-dilemma-validity-propositional-logic` — **Destructive Dilemma is Valid**
   > **Statement.**
   > The argument form
   > \[
   > \varphi\to\chi,\qquad \psi\to\theta,\qquad \neg\chi\lor\neg\theta
   > \quad\therefore\quad
   > \neg\varphi\lor\neg\psi
   > \]
   > is valid.

33. () `thm:finite-unsatisfiability-witness-propositional-logic` — **Finite Unsatisfiability Witness**
   > **Statement.**
   > Let \(\Gamma\subseteq\WFF\). If there exists a finite
   > \(\Delta\subseteq\Gamma\) such that \(\Delta\) is unsatisfiable, then
   > \(\Gamma\) is unsatisfiable.

34. () `cor:finite-unsatisfiability-witness-contrapositive-propositional-logic` — **Finite Witness Contrapositive**
   > **Statement.**
   > Let \(\Gamma\subseteq\WFF\). If \(\Gamma\) is satisfiable, then every finite
   > subset of \(\Gamma\) is satisfiable.

35. () `thm:propositional-compactness` — **Propositional Compactness**
   > **Statement.**
   > Let \(\Gamma\subseteq\WFF\). If every finite subset of \(\Gamma\) is
   > satisfiable, then \(\Gamma\) is satisfiable.

36. () `thm:canonical-disjunctive-normal-form-propositional-logic` — **Canonical Disjunctive Normal Form Theorem**
   > **Statement.**
   > Every formula \(\varphi\in\WFF\) is
   >
   > to its
   >
   > relative to a fixed ordering of its finitely many variables.
   > \[
   > \varphi\equiv \operatorname{CDNF}_{P_1,\ldots,P_n}(\varphi).
   > \]

37. () `thm:dnf-representation-of-boolean-functions-propositional-logic` — **DNF Representation of Boolean Functions**
   > **Statement.**
   > Every Boolean function \(f:\mathbb{B}^n\to\mathbb{B}\) is represented by a
   > formula in disjunctive normal form using variables \(P_1,\ldots,P_n\).

38. () `thm:conjunction-disjunction-not-functionally-complete-propositional-logic` — **Conjunction and Disjunction are not Functionally Complete**
   > **Statement.**
   > The connective basis \(\{\land,\lor\}\) is not functionally complete.

39. () `thm:standard-connectives-functionally-complete-propositional-logic` — **Standard Connectives are Functionally Complete**
   > **Statement.**
   > The connective basis
   > \[
   > \{\neg,\land,\lor\}
   > \]
   > is functionally complete.

40. () `thm:negation-conjunction-functionally-complete-propositional-logic` — **Negation and Conjunction are Functionally Complete**
   > **Statement.**
   > The connective basis
   > \[
   > \{\neg,\land\}
   > \]
   > is functionally complete.

41. () `thm:nand-functionally-complete-propositional-logic` — **NAND is Functionally Complete**
   > **Statement.**
   > The one-connective basis \(\{\uparrow\}\) is functionally complete.

42. () `thm:negation-disjunction-functionally-complete-propositional-logic` — **Negation and Disjunction are Functionally Complete**
   > **Statement.**
   > The connective basis
   > \[
   > \{\neg,\lor\}
   > \]
   > is functionally complete.

43. () `thm:nor-functionally-complete-propositional-logic` — **NOR is Functionally Complete**
   > **Statement.**
   > The one-connective basis \(\{\downarrow\}\) is functionally complete.

44. () `thm:nand-nor-minimal-complete-bases-propositional-logic` — **NAND and NOR are Minimal Complete Bases**
   > **Statement.**
   > The one-connective bases \(\{\uparrow\}\) and \(\{\downarrow\}\) are minimal
   > complete bases.

45. () `thm:canonical-conjunctive-normal-form-propositional-logic` — **Canonical Conjunctive Normal Form Theorem**
   > **Statement.**
   > Every formula \(\varphi\in\WFF\) is
   >
   > to its
   >
   > relative to a fixed ordering of its finitely many variables.
   > \[
   > \varphi\equiv \operatorname{CCNF}_{P_1,\ldots,P_n}(\varphi).
   > \]

46. () `thm:existence-negation-normal-form-propositional-logic` — **Existence of Negation Normal Form**
   > **Statement.**
   > For every formula \(\varphi\in\WFF\), there exists a formula \(\psi\in\WFF\)
   > such that \(\psi\) is in negation normal form and
   > \[
   > \varphi\equiv\psi.
   > \]

47. () `thm:existence-conjunctive-normal-form-propositional-logic` — **Existence of Conjunctive Normal Form**
   > **Statement.**
   > For every formula \(\varphi\in\WFF\), there exists a formula
   > \(\psi\in\WFF\) such that \(\psi\) is in
   >
   > and
   > \[
   > \varphi\equiv\psi.
   > \]

48. () `thm:existence-disjunctive-normal-form-propositional-logic` — **Existence of Disjunctive Normal Form**
   > **Statement.**
   > For every formula \(\varphi\in\WFF\), there exists a formula
   > \(\psi\in\WFF\) such that \(\psi\) is in
   >
   > and
   > \[
   > \varphi\equiv\psi.
   > \]

49. () `thm:dnf-satisfiability-criterion-propositional-logic` — **DNF Satisfiability Criterion**
   > **Statement.**
   > Let \(\psi\) be a formula in

50. () `thm:normal-form-semantic-classification-propositional-logic` — **Semantic Classification by Normal Forms**
   > **Statement.**
   > Normal forms give finite certificates for semantic classification. For any
   > formula \(\varphi\in\WFF\):
   > \begin{enumerate}
   >  \item \(\varphi\) is

51. () `thm:counting-boolean-functions` — **Counting Boolean Functions**
   > **Statement.**
   > There are exactly
   > \[
   > 2^{2^n}
   > \]
   > Boolean functions \(\mathbb{B}^n\to\mathbb{B}\).

52. (✅) `lem:closure-under-formation-propositional-formulas` — **Closure Under Formation**
   > **Statement.**
   > The set \(\WFF\) is closed under the propositional formation rules.
   >
   > That is, if \(\varphi\in\WFF\), then
   > \[
   > \neg\varphi\in\WFF.
   > \]
   > If \(\varphi,\psi\in\WFF\) and
   > \[
   > \circ\in\{\land,\lor,\to,\leftrightarrow\},
   > \]
   > then
   > \[
   > (\varphi\circ\psi)\in\WFF.
   > \]

53. (✅) `thm:minimality-of-well-formed-formulas` — **Minimality of Well-Formed Formulas**
   > **Statement.**
   > Let \(S\) be a set of strings over the propositional alphabet. Suppose:
   > - \(\Prop\subseteq S\);
   > - if \(\varphi\in S\), then \(\neg\varphi\in S\);
   > - if \(\varphi,\psi\in S\) and
   >  \(\circ\in\{\land,\lor,\to,\leftrightarrow\}\), then
   >  \((\varphi\circ\psi)\in S\).
   > Then
   > \[
   > \WFF\subseteq S.
   > \]

54. () `thm:unique-syntax-tree-propositional-formulas` — **Unique Syntax Tree for Propositional Formulas**
   > **Statement.**
   > Every propositional well-formed formula has a unique parse tree.

55. () `lem:proper-subformula-depth-propositional-logic` — **Proper Subformula Depth**
   > **Statement.**
   > If \(\psi\) is a proper subformula of \(\varphi\), then
   > \[
   > \operatorname{depth}(\psi)<\operatorname{depth}(\varphi).
   > \]

56. () `lem:finiteness-of-subformulas-propositional-formulas` — **Finiteness of Subformulas**
   > **Statement.**
   > For every \(\varphi\in\WFF\), the set \(\operatorname{Sub}(\varphi)\) is finite.

57. () `thm:eq-sym` — **Symmetry of Equality**
   > **Statement.**
   > From $t_1 = t_2$, one may infer $t_2 = t_1$.

58. () `thm:eq-trans` — **Transitivity of Equality**
   > **Statement.**
   > From $t_1 = t_2$ and $t_2 = t_3$, one may infer $t_1 = t_3$.

59. () `thm:eq-term` — **Term Substitution under Equality**
   > **Statement.**
   > If $t_1 = t_2$, then for any function symbol $f$,
   > $f(\dots,t_1,\dots) = f(\dots,t_2,\dots)$.

60. () `thm:eq-pred` — **Predicate Substitution under Equality**
   > **Statement.**
   > If $t_1 = t_2$ and $P$ is an $n$-ary predicate symbol, then
   > $P(\dots,t_1,\dots) \;\Leftrightarrow\; P(\dots,t_2,\dots)$.

61. () `thm:fol-sound` — **Soundness of First-Order Logic**
   > **Statement.**
   > The standard inference rules for first-order logic (UI, UG, EI, EG, and the
   > propositional rules) are sound: they preserve truth in all structures.
   >
   > If $\Gamma \vdash \varphi$, then $\Gamma \models \varphi$.

62. () `thm:qneg` — **Quantifier Negation Laws**
   > **Statement.**
   > For every formula \(\varphi\),
   > \[
   > \neg\forall x\,\varphi \equiv \exists x\,\neg\varphi,
   > \qquad
   > \neg\exists x\,\varphi \equiv \forall x\,\neg\varphi.
   > \]

63. () `thm:neg-bounded` — **Negation of Bounded Quantifiers**
   > **Statement.**
   > Let \(A\) be a set and let \(\varphi\) be a formula. Then
   > \[
   > \neg(\forall x\in A\,\varphi)\equiv \exists x\in A\,\neg\varphi,
   > \qquad
   > \neg(\exists x\in A\,\varphi)\equiv \forall x\in A\,\neg\varphi.
   > \]

64. () `thm:universal-implies-existential` — **Universal Implies Existential**
   > **Statement.**
   > Over nonempty domains,
   > \[
   > \forall x\,\varphi(x)\models \exists x\,\varphi(x).
   > \]

65. () `thm:existential-not-universal` — **Existential Does Not Imply Universal**
   > **Statement.**
   > In general,
   > \[
   > \exists x\,\varphi(x)\not\models \forall x\,\varphi(x).
   > \]

66. () `thm:uniform-witness-implies-dependent-witness` — **Uniform Witness Implies Dependent Witness**
   > **Statement.**
   > For every formula \(\varphi(x,y)\),
   > \[
   > \exists y\,\forall x\,\varphi(x,y)
   > \models
   > \forall x\,\exists y\,\varphi(x,y).
   > \]

67. () `thm:dependent-witness-not-uniform` — **Dependent Witness Need Not Be Uniform**
   > **Statement.**
   > In general,
   > \[
   > \forall x\,\exists y\,\varphi(x,y)
   > \not\models
   > \exists y\,\forall x\,\varphi(x,y).
   > \]

68. () `thm:qdist` — **Valid Quantifier Distribution**
   > **Statement.**
   > For all formulas \(\varphi,\psi\),
   > \[
   > \forall x\,(\varphi\land\psi)
   > \equiv
   > (\forall x\,\varphi)\land(\forall x\,\psi),
   > \]
   > \[
   > \exists x\,(\varphi\lor\psi)
   > \equiv
   > (\exists x\,\varphi)\lor(\exists x\,\psi).
   > \]

69. () `thm:rename` — **Renaming Bound Variables**
   > **Statement.**
   > If \(y\) is free for \(x\) in \(\varphi\) and no capture is introduced, then
   > \[
   > \forall x\,\varphi\equiv\forall y\,\varphi[y/x],
   > \qquad
   > \exists x\,\varphi\equiv\exists y\,\varphi[y/x].
   > \]

70. () `thm:pnf` — **Existence of Prenex Normal Form**
   > **Statement.**
   > Every first-order formula is logically equivalent to some formula in prenex
   > normal form.

71. () `thm:quantifier-double-negation` — **Double Negation and Quantifiers**
   > **Statement.**
   > For every formula \(\varphi\),
   > \[
   > \neg\neg\forall x\,\varphi \equiv \forall x\,\varphi,
   > \qquad
   > \neg\neg\exists x\,\varphi \equiv \exists x\,\varphi.
   > \]

72. () `thm:qcomm` — **Same-Type Quantifier Commutation**
   > **Statement.**
   > Quantifiers of the same type commute:
   > \[
   > \forall x\,\forall y\,\varphi \equiv \forall y\,\forall x\,\varphi,
   > \qquad
   > \exists x\,\exists y\,\varphi \equiv \exists y\,\exists x\,\varphi.
   > \]

73. () `thm:mixed-quantifiers-do-not-commute` — **Mixed Quantifiers Do Not Commute**
   > **Statement.**
   > In general,
   > \[
   > \forall x\,\exists y\,\varphi
   > \not\equiv
   > \exists y\,\forall x\,\varphi.
   > \]

74. () `thm:invalid-quantifier-distribution` — **Invalid Quantifier Distribution**
   > **Statement.**
   > In general,
   > \[
   > \forall x\,(\varphi\lor\psi)
   > \not\equiv
   > (\forall x\,\varphi)\lor(\forall x\,\psi),
   > \]
   > \[
   > \exists x\,(\varphi\land\psi)
   > \not\equiv
   > (\exists x\,\varphi)\land(\exists x\,\psi).
   > \]

75. () `thm:vacuous` — **Vacuous Quantification**
   > **Statement.**
   > If \(x\) does not occur free in \(\varphi\), then
   > \[
   > \forall x\,\varphi\equiv\varphi,
   > \qquad
   > \exists x\,\varphi\equiv\varphi.
   > \]

76. () `lem:subst-terms` — **Substitution Lemma for Terms**
   > **Statement.**
   > Let \(\mathcal M\) be a structure, let \(s\) be a variable assignment, let
   > \(x\) be a variable, and let \(t\) and \(u\) be terms. Then
   > \[
   > \llbracket t[u/x]\rrbracket_{\mathcal M,s}
   > =
   > \llbracket t\rrbracket_{\mathcal M,\,
   > s[x\mapsto\llbracket u\rrbracket_{\mathcal M,s}]}.
   > \]

77. () `lem:subst-formulas` — **Substitution Lemma for Formulas**
   > **Statement.**
   > Let \(\varphi\) be a formula and let \(u\) be a term free for \(x\) in
   > \(\varphi\). For every structure \(\mathcal M\) and assignment \(s\),
   > \[
   > \mathcal M,s\models\varphi[u/x]
   > \Longleftrightarrow
   > \mathcal M,s[x\mapsto\llbracket u\rrbracket_{\mathcal M,s}]\models\varphi.
   > \]

78. () `prop:universal-translation-pattern` — **Universal Translation Pattern**
   > **Statement.**
   > In a broad domain, an English statement of the form ``All \(A\) are \(B\)''
   > is translated by
   > \[
   > \forall x\,(A(x)\to B(x)).
   > \]

79. () `prop:existential-translation-pattern` — **Existential Translation Pattern**
   > **Statement.**
   > In a broad domain, an English statement of the form ``Some \(A\) are \(B\)''
   > is translated by
   > \[
   > \exists x\,(A(x)\land B(x)).
   > \]

80. () `prop:conditional-translation-pattern` — **Conditional Translation Pattern**
   > **Statement.**
   > An English statement of the form ``If \(A\), then \(B\)'' is translated by
   > \[
   > A\to B,
   > \]
   > with quantifiers placed according to the variables occurring in \(A\) and \(B\).

81. () `prop:negation-translation-pattern` — **Negation Translation Pattern**
   > **Statement.**
   > The negation of a translated quantified statement is obtained by negating the
   > whole formula and then pushing the negation inward using the quantifier
   > negation laws.

82. () `prop:a-o-contradictory-predicate-logic` — **A-O Contradiction**
   > **Statement.**
   > The \(A\)-form \(\forall x\,(A(x)\to B(x))\) and the \(O\)-form
   > \(\exists x\,(A(x)\land \neg B(x))\) are contradictory: exactly one of them is
   > true.

83. () `prop:e-i-contradictory-predicate-logic` — **E-I Contradiction**
   > **Statement.**
   > The \(E\)-form \(\forall x\,(A(x)\to \neg B(x))\) and the \(I\)-form
   > \(\exists x\,(A(x)\land B(x))\) are contradictory: exactly one of them is true.

84. () `prop:existential-import-contrariety-predicate-logic` — **Contrariety Requires Existential Import**
   > **Statement.**
   > If \(\exists x\,A(x)\), then the \(A\)-form and \(E\)-form cannot both be true.

85. () `prop:fip-duality` — **FIP--Cover Duality**
   > **Statement.**
   > Let $X$ be a set, $A \subseteq X$, and $\{U_\alpha\}_{\alpha \in I}$ a
   > family of subsets of $X$. Let $F_\alpha = U_\alpha^c = X \setminus U_\alpha$.
   > Then:
   > \[
   > \{U_\alpha\} \text{ covers } A
   > \;\;\Longleftrightarrow\;\;
   > \{F_\alpha \cap A\}_{\alpha \in I} \text{ does \emph{not} have the FIP}.
   > \]
   > More precisely: the family $\{U_\alpha\}$ does \emph{not} cover $A$ if and
   > only if the family of closed complements $\{F_\alpha\}$ has the FIP relative
   > to $A$.

86. () `thm:indexed-de-morgan` — **De Morgan's Laws for Indexed Families**
   > **Statement.**
   > Let $\{A_i\}_{i\in I}$ be an indexed family of subsets of a universe $U$.
   > Then
   > \[
   > U\setminus\bigcup_{i\in I}A_i
   > =
   > \bigcap_{i\in I}(U\setminus A_i).
   > \]
   > If $I\neq\varnothing$, then
   > \[
   > U\setminus\bigcap_{i\in I}A_i
   > =
   > \bigcup_{i\in I}(U\setminus A_i).
   > \]

87. () `thm:commutativity` — **Commutativity of Union and Intersection**
   > **Statement.**
   > Let $A,B$ be sets. Then
   > \[
   > A \cup B = B \cup A
   > \quad\text{and}\quad
   > A \cap B = B \cap A.
   > \]

88. () `thm:associativity` — **Associativity of Union and Intersection**
   > **Statement.**
   > Let $A,B,C$ be sets. Then
   > \[
   > (A \cup B) \cup C = A \cup (B \cup C)
   > \quad\text{and}\quad
   > (A \cap B) \cap C = A \cap (B \cap C).
   > \]

89. () `thm:distributivity` — **Distributive Laws**
   > **Statement.**
   > Let $A,B,C$ be sets. Then
   > \[
   > A \cap (B \cup C) = (A \cap B) \cup (A \cap C),
   > \]
   > \[
   > A \cup (B \cap C) = (A \cup B) \cap (A \cup C).
   > \]

90. () `thm:identity-absorption` — **Identity and Absorption Laws**
   > **Statement.**
   > Let $A,B$ be sets and $U$ a universe with $A \subseteq U$. Then
   > \[
   > A \cup \varnothing = A,
   > \qquad
   > A \cap U = A,
   > \]
   > \[
   > A \cup (A \cap B) = A,
   > \qquad
   > A \cap (A \cup B) = A.
   > \]

91. () `thm:involution` — **Involution of Complement**
   > **Statement.**
   > For any $A \subseteq U$,
   > \[
   > (A^c)^c = A.
   > \]

92. () `thm:de-morgan` — **De Morgan's Laws**
   > **Statement.**
   > Let $U$ be a universe and $A,B \subseteq U$. Then
   > \[
   > (A \cup B)^c = A^c \cap B^c
   > \quad\text{and}\quad
   > (A \cap B)^c = A^c \cup B^c.
   > \]

93. () `cor:set-duality` — **Principle of Set Duality**
   > **Statement.**
   > Any identity involving $\cup$, $\cap$, $\varnothing$, and $U$ that holds for
   > all subsets of a universe remains valid when each operation and constant is
   > replaced by its dual.

94. () `lem:rep-independence` — **Representative Independence Lemma**
   > **Statement.**
   > Let $R$ be an equivalence relation on $A$. For any $a,b \in A$,
   > \[
   > [a] = [b]
   > \;\;\Longleftrightarrow\;\;
   > (a,b) \in R.
   > \]

95. () `thm:equiv-partition` — **Equivalence Relations and Partitions**
   > **Statement.**
   > Let $A$ be a set.
   > - [label=(\roman*)]
   > - If $R$ is an equivalence relation on $A$, then $A/R$ is a partition of $A$.
   > - If $\mathcal{P}$ is a partition of $A$, then the relation
   > $R_{\mathcal{P}}$ defined by
   > \[
   > (a,b) \in R_{\mathcal{P}} \;\Longleftrightarrow\;
   > \exists P \in \mathcal{P} \text{ with } a \in P \text{ and } b \in P
   > \]
   > is an equivalence relation on $A$.
   > - These constructions are inverse: $R_{A/R} = R$ and $A/R_{\mathcal{P}} = \mathcal{P}$.

96. () `thm:quotient-universal` — **Universal Property of the Quotient Map**
   > **Statement.**
   > Let $R$ be an equivalence relation on $A$, let $\pi : A \to A/R$ be the
   > canonical surjection, and let $f : A \to B$ be any function. Then $f$ is
   > \emph{constant on equivalence classes} --- meaning $(a,b) \in R$ implies
   > $f(a) = f(b)$ --- if and only if there exists a unique function
   > $\bar{f} : A/R \to B$ such that
   > \[
   > f = \bar{f} \circ \pi.
   > \]
   > When it exists, $\bar{f}$ is defined by $\bar{f}([a]) = f(a)$.

97. () `thm:ordered-pair-unique` — **Uniqueness of Ordered Pairs**
   > **Statement.**
   > For any sets $a,b,c,d$,
   > \[
   > (a,b) = (c,d)
   > \;\;\Longleftrightarrow\;\;
   > (a = c \land b = d).
   > \]

98. () `thm:relation-composition-assoc` — **Associativity of Relation Composition**
   > **Statement.**
   > Let $R\subseteq A\times B$, $S\subseteq B\times C$, and
   > $T\subseteq C\times D$. Then
   > \[
   > T\circ(S\circ R)=(T\circ S)\circ R.
   > \]

99. () `thm:relation-composition-id` — **Identity Laws for Relation Composition**
   > **Statement.**
   > Let $R\subseteq A\times B$. Then
   > \[
   > R\circ\Delta_A=R
   > \quad\text{and}\quad
   > \Delta_B\circ R=R.
   > \]

100. () `thm:relation-converse-laws` — **Converse Laws for Relation Operations**
   > **Statement.**
   > Let $R,S\subseteq A\times B$, let $T\subseteq B\times C$, and take complements
   > relative to the indicated Cartesian products. Then
   > \[
   > (R^{-1})^{-1}=R,\qquad
   > (T\circ R)^{-1}=R^{-1}\circ T^{-1},
   > \]
   > \[
   > (R\cup S)^{-1}=R^{-1}\cup S^{-1},\qquad
   > (R\cap S)^{-1}=R^{-1}\cap S^{-1},
   > \]
   > \[
   > (R\setminus S)^{-1}=R^{-1}\setminus S^{-1},\qquad
   > ((A\times B)\setminus R)^{-1}=(B\times A)\setminus R^{-1}.
   > \]

101. () `thm:relation-composition-boolean` — **Relation Composition and Boolean Operations**
   > **Statement.**
   > Let $P,Q\subseteq A\times B$, $R\subseteq B\times C$, and
   > $S,T\subseteq B\times C$. Then
   > \[
   > R\circ(P\cup Q)=(R\circ P)\cup(R\circ Q),
   > \qquad
   > (S\cup T)\circ P=(S\circ P)\cup(T\circ P).
   > \]
   > Also,
   > \[
   > R\circ(P\cap Q)\subseteq(R\circ P)\cap(R\circ Q),
   > \qquad
   > (S\cap T)\circ P\subseteq(S\circ P)\cap(T\circ P).
   > \]
   > The analogous formulas for difference and complement hold only as inclusions
   > or under extra hypotheses; they are not general distributive laws.

102. () `thm:comp-assoc` — **Associativity of Composition**
   > **Statement.**
   > For $f : A \to B$, $g : B \to C$, $h : C \to D$:
   > \[
   > h \circ (g \circ f) = (h \circ g) \circ f.
   > \]

103. () `thm:comp-id` — **Identity and Composition**
   > **Statement.**
   > For any $f : A \to B$:
   > \[
   > f \circ \id_A = f
   > \quad\text{and}\quad
   > \id_B \circ f = f.
   > \]

104. () `thm:comp-inj-surj` — **Injectivity and Surjectivity Under Composition**
   > **Statement.**
   > Let $f : A \to B$ and $g : B \to C$.
   > - [label=(\roman*)]
   > - If $f$ and $g$ are injective, then $g \circ f$ is injective.
   > - If $f$ and $g$ are surjective, then $g \circ f$ is surjective.
   > - If $g \circ f$ is injective, then $f$ is injective.
   > - If $g \circ f$ is surjective, then $g$ is surjective.

105. () `thm:inverse-char` — **Characterization of Inverse Functions**
   > **Statement.**
   > Let $f : A \to B$ be bijective. Then
   > \[
   > f^{-1} \circ f = \id_A
   > \quad\text{and}\quad
   > f \circ f^{-1} = \id_B.
   > \]
   > Conversely, a function admits an inverse iff it is bijective.

106. () `thm:inverse-comp` — **Inverse of a Composition**
   > **Statement.**
   > Let $f : A \to B$ and $g : B \to C$ be bijective. Then $g \circ f$ is
   > bijective and
   > \[
   > (g \circ f)^{-1} = f^{-1} \circ g^{-1}.
   > \]

107. () `thm:one-sided` — **One-Sided Inverses and Function Properties**
   > **Statement.**
   > Let $f : A \to B$.
   > - [label=(\roman*)]
   > - $f$ has a left inverse $\iff$ $f$ is injective (and $A \neq \varnothing$ or $A=B=\varnothing$).
   > - $f$ has a right inverse $\iff$ $f$ is surjective.
   > - If $f$ has both a left inverse $g$ and a right inverse $h$, then $g = h$
   > and $f$ is bijective.

108. () `thm:preimage-ops` — **Preimages Preserve Set Operations**
   > **Statement.**
   > Let $f : A \to B$ and $S, T \subseteq B$. Then
   > - [label=(\roman*)]
   > - $f^{-1}(S \cup T) = f^{-1}(S) \cup f^{-1}(T)$,
   > - $f^{-1}(S \cap T) = f^{-1}(S) \cap f^{-1}(T)$,
   > - $f^{-1}(S \setminus T) = f^{-1}(S) \setminus f^{-1}(T)$,
   > - $f^{-1}(S^c) = (f^{-1}(S))^c$.

109. () `thm:image-ops` — **Images and Set Operations**
   > **Statement.**
   > Let $f : A \to B$ and $S, T \subseteq A$. Then
   > - [label=(\roman*)]
   > - $f(S \cup T) = f(S) \cup f(T)$,
   > - $f(S \cap T) \subseteq f(S) \cap f(T)$,
   > - $f(S \setminus T) \supseteq f(S) \setminus f(T)$.
   > Equality holds in (ii) and (iii) for all $S,T$ iff $f$ is injective.

110. () `thm:image-preimage-adjunction` — **Image--Preimage Adjunction**
   > **Statement.**
   > Let $f:A\to B$, let $S\subseteq A$, and let $T\subseteq B$. Then
   > \[
   > S\subseteq f^{-1}(f(S)),
   > \qquad
   > f(f^{-1}(T))\subseteq T.
   > \]
   > Moreover, $S=f^{-1}(f(S))$ for every $S\subseteq A$ iff $f$ is injective, and
   > $f(f^{-1}(T))=T$ for every $T\subseteq B$ iff $f$ is surjective.

111. () `thm:function-total-functional-characterization` — **Functional Relation Characterization of Functions**
   > **Statement.**
   > Let $A$ and $B$ be sets, and let $R\subseteq A\times B$. Then $R$ is a
   > function from $A$ to $B$ if and only if
   > \[
   > \forall a\in A\,\exists! b\in B,\quad (a,b)\in R.
   > \]
   > Equivalently, $R$ is a function from $A$ to $B$ if and only if $R$ is total
   > on $A$ and functional from $A$ to $B$.

112. () `prop:partial-function-functional-relation` — **Partial Functions Are Functional Relations**
   > **Statement.**
   > For sets $A$ and $B$ and a relation $R\subseteq A\times B$, $R$ is a partial
   > function from $A$ to $B$ if and only if $R$ is functional from $A$ to $B$.

113. () `prop:one-to-many-not-functional` — **One-to-Many Relations Are Not Functional**
   > **Statement.**
   > If $R\subseteq A\times B$ is one-to-many, then $R$ is not functional from $A$
   > to $B$. Consequently, $R$ is not a function from $A$ to $B$.

114. () `prop:one-to-one-converse-functional` — **One-One Relations and Converse Functionality**
   > **Statement.**
   > Let $f:A\to B$ be a function, identified with its graph
   > $G_f\subseteq A\times B$. Then $f$ is injective if and only if the converse
   > relation $G_f^{-1}\subseteq B\times A$ is functional from $B$ to $A$.

115. () `prop:bijection-unique-both-directions` — **Bijections Have Unique Correspondence Both Ways**
   > **Statement.**
   > Let $f:A\to B$ be a function. Then $f$ is bijective if and only if
   > \[
   > \forall a\in A\,\exists! b\in B,\quad f(a)=b,
   > \]
   > and
   > \[
   > \forall b\in B\,\exists! a\in A,\quad f(a)=b.
   > \]

116. () `cor:complete-preorder-extension` — **Complete preorder extension**
   > **Statement.**
   > For any nonempty set $X$ and preorder $\succsim$ on $X$, there exists a
   > complete preorder that is an extension of $\succsim$.

117. () `prop:order-duality` — **Duality Principle for Posets**
   > **Statement.**
   > Let $\Phi$ be any first-order statement about a poset $(A, \leq)$ expressed
   > using only the relation $\leq$. Let $\Phi^*$ be the statement obtained from
   > $\Phi$ by replacing every occurrence of $\leq$ with $\geq$ (equivalently,
   > working in the dual poset). Then:
   > \[
   >  (A, \leq) \models \Phi
   >  \;\;\Longleftrightarrow\;\;
   >  (A, \geq) \models \Phi.
   > \]
   > In particular, if $\Phi$ is a theorem about all posets, then so is $\Phi^*$.

118. () `prop:induced-preorder` — **$\leq_f$ is always a preorder**
   > **Statement.**
   > For any function $f : A \to B$ and partial order $(B, \leq')$, the relation
   > $\leq_f$ is a preorder on $A$: it is reflexive and transitive.

119. () `prop:induced-poset` — **$\leq_f$ is a partial order iff $f$ is injective**
   > **Statement.**
   > Let $(B, \leq')$ be a partially ordered set and $f : A \to B$.
   > The induced order $\leq_f$ is a partial order on $A$ if and only if
   > $f$ is injective.

120. () `prop:embedding-injective` — **Order embeddings are injective**
   > **Statement.**
   > Every order embedding $f : (A, \leq) \to (B, \leq')$ is injective.

121. () `prop:embedding-iso` — **Order embedding is isomorphism onto image**
   > **Statement.**
   > If $f : (A, \leq) \to (B, \leq')$ is an order embedding, then $f$ is an
   > order isomorphism from $(A, \leq)$ to the suborder $(f(A), \leq'_{f(A)})$.

122. () `prop:sup-unique` — **Uniqueness of Supremum and Infimum**
   > **Statement.**
   > Let $(A, \leq)$ be a poset and $S \subseteq A$. If $\sup S$ exists, it is
   > unique. If $\inf S$ exists, it is unique.

123. () `prop:sup-char` — **Characterisation of Supremum**
   > **Statement.**
   > Let $(A, \leq)$ be a poset, $S \subseteq A$, and $u^* \in A$. Then
   > $u^* = \sup S$ if and only if:
   > - [label=(\roman*)]
   > - $u^*$ is an upper bound of $S$; and
   > - for every $v \in A$ with $v < u^*$, there exists $s \in S$ with
   >  $v < s$.

124. () `prop:sup-inf-duality` — **Duality of Supremum and Infimum**
   > **Statement.**
   > Let $(A, \leq)$ be a poset and $S \subseteq A$. Then
   > $\inf_{(A,\leq)} S = \sup_{(A,\geq)} S$,
   > where $(A,\geq)$ denotes the dual poset.
   >
   > In particular: if every nonempty bounded-above subset of $(A,\leq)$ has a
   > supremum, then every nonempty bounded-below subset of $(A,\leq)$ has an
   > infimum.

125. () `thm:strict-order-induced-by-linear-order` — **Strict Order Induced by a Linear Order**
   > **Statement.**
   > If $\leq$ is a linear order on $S$ and
   > \[
   > x<y \;\Longleftrightarrow\; (x\leq y\land x\neq y),
   > \]
   > then $<$ is a strict linear order on $S$.

126. () `thm:linear-order-induced-by-strict-linear-order` — **Linear Order Induced by a Strict Linear Order**
   > **Statement.**
   > If $<$ is a strict linear order on $S$ and
   > \[
   > x\leq y \;\Longleftrightarrow\; (x<y\lor x=y),
   > \]
   > then $\leq$ is a linear order on $S$.

127. () `thm:trichotomy-for-linear-orders` — **Trichotomy for Linear Orders**
   > **Statement.**
   > If $\leq$ is a linear order on $S$, then for all $x,y\in S$, exactly one of
   > the following holds:
   > \[
   > x<y,\qquad x=y,\qquad y<x.
   > \]

128. () `thm:order-isomorphisms-preserve-and-reflect-order` — **Order Isomorphisms Preserve and Reflect Order**
   > **Statement.**
   > Let $(A,\leq_A)$ and $(B,\leq_B)$ be ordered sets. If $f:A\to B$ is an order
   > isomorphism, then for all $x,y\in A$,
   > \[
   > x\leq_A y \;\Longleftrightarrow\; f(x)\leq_B f(y).
   > \]

129. () `thm:Q-countable` — **$\mathbb{Q}$ is countable**
   > **Statement.**
   > The set $\mathbb{Q}$ of rational numbers is countable.

130. () `thm:countable-union` — **Countable union of countable sets is countable**
   > **Statement.**
   > Let $\{A_n\}_{n \in \mathbb{N}}$ be a countable family of countable sets.
   > Then $\bigcup_{n=1}^{\infty} A_n$ is countable.

131. () `thm:R-uncountable` — **$\mathbb{R}$ is uncountable**
   > **Statement.**
   > The set $\mathbb{R}$ of real numbers is not countable.

132. () `thm:cantor` — **Cantor's Theorem**
   > **Statement.**
   > For any set $A$, there is no surjection $A \to \mathcal{P}(A)$. In
   > particular, $|A| < |\mathcal{P}(A)|$.

133. () `thm:schroder-bernstein` — **Schr\"{o}der--Bernstein Theorem**
   > **Statement.**
   > If $|A| \leq |B|$ and $|B| \leq |A|$, then $A \sim B$.
   >
   > Equivalently: if there exist injections $f : A \hookrightarrow B$ and
   > $g : B \hookrightarrow A$, then there exists a bijection $h : A \to B$.

134. (✅) `thm:euclid-i-1` — **Euclid I.1: Constructing an equilateral triangle**
   > **Statement.**
   > Given a finite straight line segment $AB$, there exists an equilateral
   > triangle $ABC$ constructed on $AB$.

135. (✅) `thm:euclid-i-2` — **Euclid I.2: Copying a segment from a given point**
   > **Statement.**
   > Given a point $A$ and a finite straight line segment $BC$, there exists a
   > straight line segment beginning at $A$ and equal to $BC$.

136. (✅) `thm:euclid-i-3` — **Euclid I.3: Cutting off an equal segment**
   > **Statement.**
   > Given two unequal finite straight line segments, there exists a construction
   > which cuts off from the greater a straight line segment equal to the less.

137. (✅) `thm:euclid-i-4` — **Euclid I.4: Side-angle-side congruence**
   > **Statement.**
   > If two triangles have two sides equal to two sides respectively, and have the
   > angles contained by the equal straight lines equal, then they also have the
   > base equal to the base, the triangle equal to the triangle, and the remaining
   > angles equal to the remaining angles respectively.

138. (✅) `thm:euclid-i-31` — **Euclid I.31: Drawing a parallel through a point**
   > **Statement.**
   > Through a given point, to draw a straight line parallel to a given straight
   > line.

139. (✅) `thm:euclid-i-32` — **Euclid I.32: Triangle angle sum**
   > **Statement.**
   > In any triangle, if one of the sides is produced, then the exterior angle is
   > equal to the two interior and opposite angles, and the three interior angles of
   > the triangle are equal to two right angles.

140. (✅) `thm:euclid-i-41` — **Euclid I.41: Triangle and parallelogram on the same base**
   > **Statement.**
   > If a parallelogram has the same base with a triangle and is in the same
   > parallels, then the parallelogram is double the triangle.

141. (✅) `thm:euclid-i-46` — **Euclid I.46: Constructing a square on a segment**
   > **Statement.**
   > On a given straight line, to describe a square.

142. (✅) `thm:euclid-i-47` — **Euclid I.47: Pythagorean theorem**
   > **Statement.**
   > In right-angled triangles, the square on the side subtending the right angle is
   > equal to the squares on the sides containing the right angle.
