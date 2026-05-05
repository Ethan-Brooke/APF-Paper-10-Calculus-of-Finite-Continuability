---
type: concept
domain: apf
layer: 1-spine
created: 2026-04-14
updated: 2026-04-26 (Phase 19l-tail IJC regime-classifier banner added)
sources: []
---

# Axiom A1
## "Any physical distinction that can be maintained must be maintainable by a process with finite operational cost."

> **Admissibility-space reframing (2026-04-25 evening, Paper 0 v4.1):** A1 is *the substantive finiteness claim about [[Admissibility Space|admissibility space]]* — the explicit mathematical structure at every interface (per Paper 1 Supplement FD1: enforcement-interface triple S_Γ + 𝒟(Γ) + C(Γ)). At every causally connected region, admissibility space's capacity is finite. A1 is the first quantitative claim about admissibility space, not the framework's foundation. Earlier framings calling A1 "the framework's first formal axiom" or labelling APF a "single-axiom framework" are retired; the canonical statement of A1's role is Paper 0 v4.1 Ch 3 (formerly Ch 2): *"A1: Admissibility Space's Finiteness Clause."* See [[Admissibility Space]] for the canonical structural commitment, [[Paper 1 - Spine]] for FD1 (canonical bedrock), and [[Derivation Chain]] for how A1 sits within admissibility space's coherence conditions alongside the structural closure (MD + BW) and selection principle (A2). The "referent" handle from Paper 0 v4.0 is superseded; see [[The Referent]] for historical context.

> **PLEC note (2026-04-17):** As of the PLEC consolidation (Papers 1 v4.0-PLEC and 2 v5.3-PLEC), A1 is one of **four structurally necessary components** of the *Principle of Least Enforcement Cost* (PLEC): A1 (finite capacity; upper bound), **MD** (positive cost floor), **A2** (argmin selection), **BW** (budget-window / non-degeneracy). PLEC is the canonical variational formulation of the enforceability-of-distinction foundation; it does not replace the locked claim that physical meaning is grounded in enforceable distinction. Each component has an explicit countermodel / essentiality proof in the Paper 1 Technical Supplement showing it is not implied by the other three.

> **Phase 19 IJC routing (2026-04-26):** PLEC's four features (A1, MD, A2, BW) define [[Admissibility Space|admissibility space]] universally, but they alone do not force noncommutativity.  Different regimes commit to different additional structural features: KMS at thermodynamic interfaces, A9/Lovelock at gravitational interfaces, **[[Irreducible Joint Constraint|IJC]]** at quantum-capable interfaces.  IJC is not a fifth PLEC component; it is a regime classifier.  The earlier corpus claim ``finite capacity forces noncommutativity'' was structurally false (admits a spectator countermodel) and is retired; the corrected claim is ``A1+MD+A2+BW + IJC at quantum-capable interfaces forces noncommutativity.''  See [[Irreducible Joint Constraint]] for the IJC Dichotomy Theorem + three lemmas + 8-check bank-anchor table.  Canonical four-line statement: A1/MD/A2/BW define admissibility space and its cost logic; within that space, separable joint threat structures yield classical commutative behavior; nonseparable joint threat structures yield IJC; IJC plus minimal sharp enforcement yields noncommutativity.

> **Two-axiom history (2026-04-16, superseded by PLEC framing):** Before the PLEC consolidation, A1 and A2 were presented as two named axioms. Post-PLEC, A1 and A2 are both components of a single variational principle. The "A1 admits / A2 selects" distinction remains correct as a description of which component does which work: A1 defines the admissible set $\mathcal{A}(\rho, R)$ of configurations satisfying $\Sigma\varepsilon \le C$; A2 picks the min-cost member as the realised structure. MD is the floor that makes "minimum" well-posed; BW is the non-degeneracy ensuring distinct-cost alternatives exist.

**Statement:** Let $D$ be a physical distinction (a difference between two possible states of a system). If $D$ can be maintained indefinitely by some operational process, then that process must have finite cost (in the sense of resources, energy, or work required per unit time).

**Interpretation:**
- "Physical distinction" — a state difference that (a) can be prepared, (b) can be measured, (c) has physical consequences
- "Maintained" — the distinction persists or can be repeatedly enforced
- "Operational process" — an implementable, repeatable algorithm or natural law
- "Finite cost" — the resource requirement (energy, work, logical operations) is bounded per cycle

**Consequences:**

From PLEC (A1 + MD + A2 + BW), APF derives:
1. Complex Hilbert space structure (not real or quaternionic) — A1
2. The [[Born Rule]] probability formula — A1
3. $SU(3) \times SU(2) \times U(1)$ gauge group uniquely — A1 admits the gauge templates; A2 selects $N_c = 3$ as the min-cost member
4. 45 fermions in 3 families — A1 + A2 (1-of-4680 enumeration; A2 picks the min-cost survivor)
5. Exact mass ratios and mixing angles
6. Dark energy and cosmological density fractions
7. 47+ quantitative predictions with zero free parameters
8. $\theta_{QCD} = 0$ — A2 selects $\theta = 0$ over $\theta \ne 0$ (both admissible under A1; A2 picks zero-maintenance-cost value)

**Comparison to other axioms:**
- Not a variational principle (doesn't assume least-action)
- Not tied to symmetry (does not assume gauge invariance)
- Precedes and forces gauge structure (gates the latter)
- Ground-level: applies to any system maintaining distinguishability

**Key lemmas (from [[Paper 1 - Spine]]):**
- L_epsilon_star — operability bound on cost
- L_NZ — non-closure of state spaces
- L_loc — locality from finiteness
- L_cost — cost scaling with ensemble size
- L_irr — irreversibility from cost asymmetry

**Status:** Foundational; fully formalized in `core.py` (48 checks)

## Meta-level structure produced by A1 (2026-04-24)

A1's finiteness does not just gate individual theorems. Three **meta-level results** organise the v6.9 bank at the level above individual theorems, all derived from A1:

- **[[Capacity Ontology]]** — what capacity *is*. Regime-stratified: four-level hierarchy (integer / scalar / subspace / operator-algebra) at finite volume; Araki-Woods factor grid (Type I / II$_1$ / III$_\lambda$ / III$_1$) in thermodynamic limits; unified by inductive-limit completion. [P] at every load-bearing claim.
- **[[Geometry-Content Partition]]** — what capacity *does*. Two kinds of physics — capacity geometry (arrangement: where/when/how much capacity is committed) and capacity content (intra-arrangement correlation structure) — both derived from A1, paralleling GR's geometry↔matter split. Classifier verdict: 22% geometry, 44% content, 30% scaffolding, 4% cross-cutting across 420 theorems.
- **[[Capacity Redistribution Meta-Theorem]]** — how capacity *moves*. Three dynamical categories (Flow / Commitment / Saturation) exhaustive + forcing per category, via A9.3 Lovelock + T_CPTP + partition rigidity. [P$_{\rm comp}$] FORMALISED.

Plus the static cross-regime consistency layer:

- **[[T_ACC Unification]]** — how capacity *agrees across regimes*. Four identities I1–I4 link integer + scalar levels across six projections ($\pi_T, \pi_G, \pi_Q, \pi_F, \pi_C, \pi_A$). [P] composed.

Together these four meta-theorems organise v6.9 along four axes: ontology, structure, dynamics, static consistency. Each is derived from A1.

## See also
- [[Enforcement Budget]]
- [[Paper 1 - Spine]]
- [[Non-Closure Theorem]]
- [[Capacity Ontology]]
- [[Geometry-Content Partition]]
- [[Capacity Redistribution Meta-Theorem]]
- [[T_ACC Unification]]
