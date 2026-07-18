# The Calculus of Finite Continuability

### Interactive Mathematical Appendix to Paper 10 of the Admissibility Physics Framework

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20041680.svg)](https://doi.org/10.5281/zenodo.20041680) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Ethan-Brooke/APF-Paper-10-Calculus-of-Finite-Continuability/blob/main/APF_Reviewer_Walkthrough.ipynb)

[Interactive Derivation DAG](https://ethan-brooke.github.io/APF-Paper-10-Calculus-of-Finite-Continuability/) · [Theorem Map](#theorem-mapping-table) · [Reviewers' Guide](REVIEWERS_GUIDE.md) · [The full APF corpus](#the-full-apf-corpus) · [Citation](#citation)

> **AI agents:** start with [`START_HERE.md`](START_HERE.md) — operational checklist that loads the framework context in 5–10 minutes. The corpus inventory and full file map are in [`ai_context/repo_map.json`](ai_context/repo_map.json).

---

## Why this codebase exists

Continuation-first re-foundation of APF.  The primitive judgment Γ ⊨_C D ⇝ E (in context Γ, distinction-expression D can continue as E using capacity at most C) is bedrock; enforcement, cost, BCD, recruitment profiles, fields, radiation, quantum anchors, gauge, conservation, geometry, entropy, time, action all become specializations or downstream readings of the continuation calculus.  Continuation/Dynamics separation as central simplification: continuation defines admissible possibility; dynamics is a further selection rule.  PLEC's four features (A1, MD, A2, BW) collapse to one continuation primitive + one capacity-monotonicity axiom + one finite-physical-regime hypothesis + two derived lemmas (Lemma A2 for argmin, Lemma BW for cost-spectrum non-degeneracy).

This repository is the executable audit layer for the symbolic proofs in this paper.  Every theorem in the manuscript traces to a named `check_*` function that exercises the claim at concrete representative values; the symbolic proof itself lives in the manuscript and its Technical Supplement.  Numerical agreement at concrete values is a sanity check, not a proof — see Paper~0 v4.4 §`sec:codebase` for the canonical trust-control discipline.

The codebase is a faithful subset of the canonical APF codebase v24.3.427 (frozen 2026-05-04; 3918 verify_all checks, 3918 bank-registered theorems across 25 modules + `apf/standalone/`; canonical Phase-18 baseline). Each theorem in the manuscript traces to a named `check_*` function in `apf/core.py`, which can be called independently and returns a structured result.

The codebase requires Python 3.8+ and NumPy / SciPy (some numerical lemmas use them; see `pyproject.toml`).

## How to verify

Three paths, in order of increasing friction:

**1. Colab notebook — zero install.** [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Ethan-Brooke/APF-Paper-10-Calculus-of-Finite-Continuability/blob/main/APF_Reviewer_Walkthrough.ipynb) Every key theorem is derived inline, with annotated cells you can inspect and modify. Run all cells — the full verification takes under a minute.

**2. Browser — zero install.** Open the [Interactive Derivation DAG](https://ethan-brooke.github.io/APF-Paper-10-Calculus-of-Finite-Continuability/). Explore the dependency graph. Hover any node for its mathematical statement, key result, and shortest derivation chain to A1. Click **Run Checks** to watch all theorems verify in topological order.

**3. Local execution.**

```bash
git clone https://github.com/Ethan-Brooke/APF-Paper-10-Calculus-of-Finite-Continuability.git
cd APF-Paper-10-Calculus-of-Finite-Continuability
pip install -e .
python run_checks.py
```

Expected output:

```
      Paper 10 (The Calculus of Finite Continuability): 3 passed, 0 failed, 3 total — verified in <minutes>
```

**4. Individual inspection.**

```python
from apf.bank import get_check
r = get_check('check_T_finite_operational_basis_scope_contract')()
print(r['key_result'])
```

For reviewers, a [dedicated guide](REVIEWERS_GUIDE.md) walks through the logical architecture, the structural assumptions, and the anticipated objections.

---

## Theorem mapping table

This table maps every result in the manuscript to its executable verification.

| Check | Type | Summary |
|-------|------|---------|
| `check_T_finite_operational_basis_scope_contract` | Theorem | Scope guard and exact-arithmetic contract for the Paper 10/Paper 9 node. |
| `check_T_finite_operational_basis` | Theorem | Exact finite atom-cover model witness for the finite basis mechanism. |
| `check_T_finite_minimal_joint_realization_atom_cover` | Theorem | Concrete compatible joint-realization corollary on the atom-cover model. |

All check functions reside in `apf/core.py`. Every function listed above can be called independently and returns a structured result including its logical dependencies and the mathematical content it verifies.

---

## The derivation chain

```
  Level 0: T_finite_operational_basis_scope_contract · T_finite_operational_basis · T_finite_minimal_joint_realization_atom_cover
```

The [interactive DAG](https://ethan-brooke.github.io/APF-Paper-10-Calculus-of-Finite-Continuability/) shows the full graph with hover details and animated verification.

---

## Repository structure

```
├── README.md                              ← you are here
├── START_HERE.md                          ← AI operational checklist; read-first for AI agents
├── REVIEWERS_GUIDE.md                     ← physics-first walkthrough for peer reviewers
├── interactive_dag.html                   ← interactive D3.js derivation DAG (also served at docs/ via GitHub Pages)
├── repo_map.json                          ← machine-readable map of this repo (root copy of ai_context/repo_map.json)
├── theorems.json                          ← theorem catalog (root copy of ai_context/theorems.json)
├── derivation_graph.json                  ← theorem DAG as JSON (root copy of ai_context/derivation_graph.json)
├── ai_context/                            ← AI onboarding pack (corpus map, theorems, glossary, etc.)
│   ├── AGENTS.md                          ← authoritative entry point for AI agents
│   ├── FRAMEWORK_OVERVIEW.md              ← APF in 5 minutes
│   ├── GLOSSARY.md                        ← axioms, PLEC primitives, epistemic tags
│   ├── AUDIT_DISCIPLINE.md                ← engagement posture for critique/proposal
│   ├── OPEN_PROBLEMS.md                   ← catalog of open problems + verdicts
│   ├── repo_map.json                      ← machine-readable map of this repo
│   ├── theorems.json                      ← machine-readable theorem catalog
│   ├── derivation_graph.json              ← theorem DAG as JSON
│   └── wiki/                              ← bundled APF wiki (concepts, papers, codebase)
├── apf/
│   ├── core.py                            ← 3 theorem check functions
│   ├── apf_utils.py                       ← exact arithmetic + helpers
│   └── bank.py                            ← registry and runner
├── docs/
│   └── index.html                         ← interactive derivation DAG (GitHub Pages)
├── APF_Reviewer_Walkthrough.ipynb         ← Colab notebook
├── run_checks.py                          ← convenience entry point
├── pyproject.toml                         ← package metadata
├── zenodo.json                            ← archival metadata
├── Paper_10_Calculus_of_Finite_Continuability_v1.21.tex                ← the paper

└── LICENSE                                ← MIT
```

---

## What this paper derives and what it does not

**Derived:** (see Theorem mapping table above)

**Not derived here:** Specific results outside this paper's scope live in companion papers — see the corpus table below for the full 9-paper series.

---

## Citation

```bibtex
@software{apf-paper10,
  title   = {The Calculus of Finite Continuability},
  author  = {Brooke, Ethan},
  year    = {2026},
  doi     = {10.5281/zenodo.20041680},
  url     = {https://github.com/Ethan-Brooke/APF-Paper-10-Calculus-of-Finite-Continuability}
}
```

For the full citation lineage (concept-DOI vs version-DOI, related identifiers, bibtex for all corpus papers), see [`ai_context/CITING.md`](ai_context/CITING.md).

---

<!-- FOOTER:start -->
---

## About the APF series

The Admissibility Physics Framework is a constraint-first derivation of the Standard Model and cosmological structure from a single primitive — finite enforcement capacity. The corpus runs from the foundational papers through the gauge sector, the quantum formalism, Lorentzian spacetime and the Einstein field equations, the cosmological constant, the electroweak and dark sectors, and the lattice Yang-Mills program. Each paper's main text and Technical Supplement is deposited separately on Zenodo and collected in the **[admissibility_physics](https://zenodo.org/communities/admissibility_physics)** community. The engine repository is the machine-verifiable companion to all of it (v24.3.427 — 3,918 bank-registered theorems across 481 modules, 48 quantitative predictions).

| # | Title | Concept DOI | Code |
|---|---|---|---|
| Engine | Admissibility Physics — Unified Theorem Bank & Verification Engine | [10.5281/zenodo.18529115](https://doi.org/10.5281/zenodo.18529115) | [GitHub](https://github.com/Ethan-Brooke/APF-Codebase) |
| 0 | What Physics Permits: A Constraint-First Framework for Physics | [10.5281/zenodo.18439523](https://doi.org/10.5281/zenodo.18439523) | [GitHub](https://github.com/Ethan-Brooke/APF-Paper-0-What-Physics-Permits) |
| 1 | The Enforceability of Distinction | [10.5281/zenodo.18439200](https://doi.org/10.5281/zenodo.18439200) | [GitHub](https://github.com/Ethan-Brooke/APF-Paper-1-The-Enforceability-of-Distinction) |
| 2 | Finite Admissibility and the Failure of Global Description | [10.5281/zenodo.18439274](https://doi.org/10.5281/zenodo.18439274) | [GitHub](https://github.com/Ethan-Brooke/APF-Paper-2-The-Structure-of-Admissible-Physics) |
| 3 | Entropy, Time, and Accumulated Cost | [10.5281/zenodo.18439363](https://doi.org/10.5281/zenodo.18439363) | [GitHub](https://github.com/Ethan-Brooke/APF-Paper-3-Ledgers-Entropy-Time-Cost) |
| 4 | Admissibility Constraints and Structural Saturation | [10.5281/zenodo.18439397](https://doi.org/10.5281/zenodo.18439397) | [GitHub](https://github.com/Ethan-Brooke/APF-Paper-4-Admissibility-Constraints-Field-Content) |
| 5 | Quantum Structure from Finite Enforceability | [10.5281/zenodo.18439433](https://doi.org/10.5281/zenodo.18439433) | [GitHub](https://github.com/Ethan-Brooke/APF-Paper-5-Quantum-Structure-Hilbert-Born) |
| 6 | Dynamics and Geometry as Optimal Admissible Reallocation | [10.5281/zenodo.18439445](https://doi.org/10.5281/zenodo.18439445) | [GitHub](https://github.com/Ethan-Brooke/APF-Paper-6-Dynamics-Geometry-Spacetime-Gravity) |
| 7 | A Minimal Quantum of Action from Finite Admissibility | [10.5281/zenodo.18439513](https://doi.org/10.5281/zenodo.18439513) | [GitHub](https://github.com/Ethan-Brooke/APF-Paper-7-Action-Internalization-Lagrangian) |
| 8 | The Admissibility-Capacity Ledger | [10.5281/zenodo.19721384](https://doi.org/10.5281/zenodo.19721384) | [GitHub](https://github.com/Ethan-Brooke/APF-Paper-8-Admissibility-Capacity-Ledger) |
| 9 | The Geometric Substrate as Cost Structure of Comparison Continuations | [10.5281/zenodo.20041675](https://doi.org/10.5281/zenodo.20041675) | [GitHub](https://github.com/Ethan-Brooke/APF-Paper-9-Geometric-Substrate) |
| 10 | The Calculus of Finite Continuability | [10.5281/zenodo.20041680](https://doi.org/10.5281/zenodo.20041680) | [GitHub](https://github.com/Ethan-Brooke/APF-Paper-10-Calculus-of-Finite-Continuability) |
| 11 | Forced Universality from Capacity-Bounded Admissibility | [10.5281/zenodo.20684198](https://doi.org/10.5281/zenodo.20684198) | — |
| 13 | The Minimal Admissibility Core | [10.5281/zenodo.18361446](https://doi.org/10.5281/zenodo.18361446) | [GitHub](https://github.com/Ethan-Brooke/APF-Paper-13-The-Minimal-Admissibility-Core) |
| 16 | Markov Breakdown and the Hard Problems | [10.5281/zenodo.20684207](https://doi.org/10.5281/zenodo.20684207) | — |
| 18 | The Electroweak Sector as a Capacity Equilibrium | [10.5281/zenodo.20684209](https://doi.org/10.5281/zenodo.20684209) | — |
| 20 | The Enforcement Crystal | [10.5281/zenodo.18531732](https://doi.org/10.5281/zenodo.18531732) | — |
| 21 | APF Engine — Unified Theorem Bank and Verification Engine | [10.5281/zenodo.18529115](https://doi.org/10.5281/zenodo.18529115) | [GitHub](https://github.com/Ethan-Brooke/APF-Codebase) |
| 24 | The Recruitment-Radius Extension — Foundations | [10.5281/zenodo.20684211](https://doi.org/10.5281/zenodo.20684211) | — |
| 28 | Absolute Mass Scales from Electroweak Capacity Saturation | [10.5281/zenodo.20684215](https://doi.org/10.5281/zenodo.20684215) | — |
| 29 | Plaquette Representation Dominance and Confinement | [10.5281/zenodo.20684218](https://doi.org/10.5281/zenodo.20684218) | — |
| 30 | A Tube Mechanism for the Lattice Mass Gap | [10.5281/zenodo.20684220](https://doi.org/10.5281/zenodo.20684220) | — |
| 31 | Osterwalder-Schrader Structure of Lattice Yang-Mills | [10.5281/zenodo.20684222](https://doi.org/10.5281/zenodo.20684222) | — |
| 33 | Trace-to-Scheme Export Architecture | [10.5281/zenodo.20684224](https://doi.org/10.5281/zenodo.20684224) | — |
| 35 | The Dark Sector as a Two-Role Capacity Decomposition | [10.5281/zenodo.20684228](https://doi.org/10.5281/zenodo.20684228) | — |
| 40 | Between Symmetry and the Void — The Thermodynamics of Finite Distinction | [10.5281/zenodo.20684235](https://doi.org/10.5281/zenodo.20684235) | — |
| 41 | The Horizon as a Continuation Ledger | [10.5281/zenodo.20684241](https://doi.org/10.5281/zenodo.20684241) | — |
| 42 | The Weak Mixing Angle Is Not Free | [10.5281/zenodo.20684245](https://doi.org/10.5281/zenodo.20684245) | — |

Concept DOIs always resolve to the latest version. Technical Supplements are deposited as linked records — `isSupplementTo` the main paper, `isDocumentedBy` the companion repository.

## Author

Ethan Brooke — Independent Researcher, San Anselmo, California, USA.

- ORCID: [0009-0001-2261-4682](https://orcid.org/0009-0001-2261-4682)
- LinkedIn: [linkedin.com/in/ethanbrooke](https://www.linkedin.com/in/ethanbrooke/)
- GitHub: [github.com/Ethan-Brooke](https://github.com/Ethan-Brooke)
- Contact: brooke.ethan@gmail.com

MIT — see [LICENSE](LICENSE).
<!-- FOOTER:end -->
