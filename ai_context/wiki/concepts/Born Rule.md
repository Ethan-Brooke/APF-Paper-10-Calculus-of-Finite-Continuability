---
type: concept
domain: apf
layer: 5-quantum
created: 2026-04-14
updated: 2026-04-26 (Phase 19l-tail [P+IJC] tagging)
sources: []
---

# Born Rule
## "The Probability Postulate of Quantum Mechanics"

**Standard statement:** If a quantum system is in state $|\psi\rangle$ and we measure observable $A$, the probability of finding outcome $a_n$ is $p_n = |\langle a_n | \psi \rangle|^2$.

**In APF:** The Born rule is not postulated; it is derived from [[Axiom A1]] and the operability constraint.

> **Phase 19 update (2026-04-26):** the Born rule's derivation chain inherits the **[P+IJC]** epistemic tag through L_Pi → T_alg → T2 → T_Born.  At quantum-capable interfaces (where some pair of distinctions satisfies the [[Irreducible Joint Constraint]] dichotomy's branch (IJC)), the noncommutative algebra licenses Gleason's theorem to produce the Born rule.  At classically separable interfaces (branch (Sep)), the algebra is commutative and Gleason's theorem is replaced by classical probability theory; no Born rule applies.  PLEC's four constitutive features (A1, MD, A2, BW) alone do not produce the Born rule; the regime-classifier IJC is what selects the quantum regime.  See [[Irreducible Joint Constraint]] for the dichotomy theorem + three lemmas + bank-check coderefs.

**Derivation (sketch):**
- Cost of maintaining a pure state $|\psi\rangle$ grows with the number of superposed terms
- Cost of measurement is minimized when probabilities follow $|\psi_n|^2$
- Any other weighting would require higher enforcement cost
- Therefore, the Born rule is the unique cost-minimizing measurement rule
- T_Born (`check_T_Born` in core.py) — formal proof

**Key implications:**
- Indeterminism emerges from cost-finiteness, not as a fundamental mystery
- The $|\cdot|^2$ weighting is necessary, not contingent
- Mixed states arise naturally from information loss under enforcement bounds
- Entanglement is cost-efficient encoding (not a puzzle)

**Connection to other rules:**
- Reduces to [[Born Rule]] when strong measurement occurs
- Extends to [[Non-Closure Theorem|non-closure]] state spaces
- Predicts Tsirelson bound (`check_T_Tsirelson`) on non-local correlations

**Experimental status:** 
- Born rule confirmed to >10 decimal places in quantum optics, atomic physics, particle physics
- No known violations under admissible measurement scenarios
- APF predicts this is necessary, not contingent

**Open questions:**
- Can measurement geometry (angle, context) be derived from cost?
- How does measurement cost vary with observable?

## See also
- [[Axiom A1]]
- [[Paper 5 - Quantum]]
- [[Tensor Product Structure]]
