---
type: synthesis
domain: apf
layer: cross-cutting
created: 2026-04-14
updated: 2026-04-26 (Phase 19 IJC regime classifier inserted between PLEC and quantum-sector layers)
sources: []
---

# Derivation Chain
## "The Logical Architecture of APF"

**Overview:** APF is built in seven nested layers, each building on the previous. This map shows the dependencies and key theorems at each step. Since the PLEC consolidation (April 2026), the Layer 0 foundation is presented as the *Principle of Least Enforcement Cost* — reality as the minimum-cost expression of distinction compatible with finite capacity — decomposed into four structurally necessary components: **A1** (finite capacity; upper bound), **MD** (positive cost floor), **A2** (argmin selection), **BW** (budget-window / non-degeneracy). Each is essential: Paper 1 v4.0-PLEC and its Technical Supplement §1 give countermodels showing no three of the four imply the fourth.

**2026-04-26: regime-classifier addition (Phase 19).**  Between PLEC's four constitutive features and the quantum-sector results (Layer~3 onward), the framework inserts a regime classifier: **[[Irreducible Joint Constraint|IJC]]**.  At quantum-capable interfaces (pairs of distinctions in branch (IJC) of the IJC Dichotomy Theorem), the bridge from PLEC to noncommutativity runs.  At classically separable interfaces (branch (Sep)), the algebra is commutative and the bridge is vacuous.  IJC is not a fifth PLEC component; it is the criterion that selects quantum-capable interfaces from the broader admissibility-space ontology, parallel to KMS at thermodynamic interfaces and A9/Lovelock at gravitational interfaces.  Every quantum-sector result downstream of L_Pi inherits the **[P+IJC]** epistemic tag.  See [[Irreducible Joint Constraint]] for the dichotomy theorem + three lemmas + 8-check bank-anchor table; canonical four-line statement at top of that page is the corpus voice anchor.

**2026-04-24: meta-level additions.** Sitting *above* the seven-layer stack is a meta-level structure — four theorems that organise the bank as a whole, each derived from A1:

- **[[Capacity Ontology]]** — what capacity *is*. Regime-stratified four-level hierarchy at finite volume + Araki-Woods factor grid in thermodynamic limits.
- **[[Geometry-Content Partition]]** — what capacity *does*. Two kinds of physics (geometry = arrangement; content = intra-arrangement correlation), paralleling GR's geometry↔matter split, both derived from A1.
- **[[Capacity Redistribution Meta-Theorem]]** [P$_{\rm comp}$] — how capacity *moves*. Three dynamical categories (Flow / Commitment / Saturation) exhaustive + forcing per category.
- **[[T_ACC Unification]]** — how capacity *agrees across regimes*. Four identities I1–I4 linking integer + scalar levels across six projections.

These are not a new layer — they are a meta-structural organisation of the existing seven-layer derivation chain. Reading them explains what the bank *is*; the seven layers explain how it *derives*.

**Layer 0: Admissibility Geometry (PLEC four components)**
- [[Axiom A1]] — finite enforcement capacity (upper bound)
- MD — minimum cost floor (positive floor; makes "minimum" well-posed)
- A2 — argmin selection (picks realised structure from admissible set)
- BW — budget-window non-degeneracy (distinct-cost alternatives exist)
- L_epsilon_star — operability bound
- L_NZ, L_loc, L_cost, L_irr — lemmas on cost structure

**Layer I: Quantum Mechanics** (derives from L0)
- T2 → complex Hilbert space forced
- T3 → noncommutativity necessary
- T_Born → [[Born Rule]] derived
- T_Tsirelson → Bell inequality bound
- T_CPTP → quantum evolution as cost-preserving maps

**Layer II: Standard Model** (derives from I)
- [[Non-Closure Theorem]] (L_NZ) blocks classical gauge closure
- Theorem_R (R1/R2/R3) → representation constraints
- L_gauge_template_uniqueness → [[Gauge Uniqueness]]
- T_gauge → $SU(3) \times SU(2) \times U(1)$ forced, $N_c=3$
- T_field → 45 fermions necessary, no exotics
- L_count → exactly 61 effective degrees of freedom

**Layer III: Mass and Mixing** (derives from II)
- [[Gram Matrix]] — capacity structure determines spectrum
- L_multiplicative_amplitude → Feynman amplitude form
- T27c (x = 1/2) → binds exactly 3 generations
- L_mass_from_capacity → fermionic masses from cost topology
- T_CKM, T_PMNS → quark and lepton mixing angles

**Layer IV: Cosmology** (derives from I, II, III)
- L_equip → energy equipartition across sectors
- L_dark_budget → cosmological constant explained
- L_N_eff_prediction → neutrino family count
- L_equation_of_state → dark energy equation of state

**Layer V: Gravity and Spacetime** (derives from all)
- Internalization → Yang-Mills structure → Einstein equations (conjectured)
- Spacetime metric from cost topology
- Open: full derivation of Riemannian geometry from A1

**Interdependencies:**
- Layers I-II are logically tight; predictions follow deterministically
- Layers III-IV refine mass/cosmology predictions
- Layer V extends to gravity (partially complete)

**Implementation:** v6.9 codebase — 34 modules, 420 bank-registered theorems, 437 verify_all checks, 48 quantitative predictions.

## See also
- [[Paper 13 - Minimal Admissibility Core]]
- [[What Physics Permits]]
- [[Predictions Catalog]]
- [[Capacity Ontology]]
- [[Geometry-Content Partition]]
- [[Capacity Redistribution Meta-Theorem]]
- [[T_ACC Unification]]
