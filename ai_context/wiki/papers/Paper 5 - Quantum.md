---
type: paper
domain: apf
layer: 5-quantum
created: 2026-04-14
updated: 2026-05-03
sources: []
---

# Paper 5 - Quantum
## "Hilbert Space, the Born Rule, and Tensor Products"

**Status:** **Main body v2.4 (14pp) + Technical Supplement v5.97 (157pp, 'Public Formal Core, compressed and polished')** (Paper 5 publication cycle, 2026-04-29 evening).  Supplement spine: Quantum Admissibility Condition (QAC), SepStr/SepAdm/IJCStr/IJCAdm/IJCPres/SepPres branch taxonomy, operational radical + faithful semisimple quotient via no-phantom-record quotient, finite matrix-sector representation, interface-complete composition, master finite APF quantum representation theorem, field selection by **split** closed-world composite gates (tensor closure rules out ℍ; finite tomographic locality rules out ℝ — Wootters-Hardy local-marginals argument), Hilbert representation, Born trace rule, gate-certification layer, real/quaternionic nonzero-defect rescues, public certificate schema, illustrative end-to-end finite-data certificate, structurally-classical-but-locally-inadmissible finite branch, public algorithmic performance envelope.  36 sections, 235 theorem envs, 59 bibitems.  Reviewer-response unbundling at v5.43 derives the three formerly-axiom-class regime gates (reciprocal calibration → self-duality + adjoint; stable simple-record completeness; APF-complete composite closure) from a deeper APF primitive: closed-world ledger conservation + no-phantom-records.  Engineering content (CHSH/Fine/Boole frontiers, witness lower bounds, classical-embedding audits, reproducibility artifacts, anytime-valid runtime monitoring) lives in the separate Engineering Companion v1.0 at `Admissible Technologies/Patents/AT-005 .../05 - Engineering Companion v1.0.{tex,pdf}` (IP-gated pending AT-005 provisional filing).  Paper 5's Hilbert space is the quantum-regime reading $\pi_Q(\mathrm{acc}_{\mathrm{quantum}}(d))$ of the T_ACC ledger; measurement is a Sector A ↔ Sector B crossing via the interface-sector bridge theorem.  Earlier: v2.0-PLEC/v1.0 (2026-04-19); v2.1/v1.1 (2026-04-21 Phase 12.3); v2.4/v5.15 (2026-04-29 morning Phase 23.3); v5.23 → v5.34 (2026-04-29 morning publication-readiness cycle); v5.34 → v5.97 (2026-04-29 evening public-release-polish + reviewer-response unbundling).

**Changelog:**
- **v5.97 supplement (2026-04-29 evening, 13 landings v5.34 → v5.97):** Public formal core, compressed and polished; 157pp, 8291 lines, 36 sections, 235 theorem envs, 59 bibitems.  Workstream broke into three phases: (1) **Certification-toolchain + gate-lock** (v5.35–v5.42) — `\SepPres` macro added; `Certification toolchain map for defender tests` proposition; `Final gate-lock audit` section; +7 theorems including positive-cone product compatibility, preservation-IJC obstruction, reciprocity→adjoint, closed-world completeness derives gates.  (2) **Reviewer-response unbundling** (v5.43–v5.45) — external reviewer flagged three "regime gates" as Barnum-Wilce/Hardy-class axioms; framework response derives all three from closed-world ledger conservation + no-phantom-records.  v5.43 lands closed-ledger reciprocity + no-phantom-record quotient + operational radical = Jacobson + closed-world composition splits "APF-complete composite closure" into tensor closure (rules out ℍ) + finite tomographic locality (rules out ℝ).  v5.44 strengthens with read/write self-duality and zero-defect dimension theorem.  v5.45 consolidates — v5.44's strengthening section absorbed; many `[P_regime]` items promoted to `[P_APF + P_math]` or `[definition + finite test]` epistemic status; "Field selection by APF-complete composite accounting" → "Field selection by **split** closed-world composite gates".  (3) **Public-release polish** (v5.55–v5.97) — reconstruction-literature related-work compression; gate-certification layer; real/quaternionic nonzero-defect composite rescues; *Constructive* upgrade to finite commuting-realization theorem; "Operational companion" retitled to "Public certificate schema and implementation-independent scope"; new sections *Illustrative end-to-end finite-data certificate*, *A structurally classical but locally inadmissible finite branch*, *Public algorithmic performance envelope*.  Each landing archived predecessor to `Old/`; pdflatex×3 compile clean.  Phase 22x codebase scope: ~14-16 new bank checks queued for follow-on session, candidate new module `apf/closed_world_completeness.py`.

- **v5.34 supplement (2026-04-29 publication cycle, 4 landings):** v5.23 (formal-only split, engineering content extracted to companion v1.0; internal v5.22→v5.23 mismatch fixed) → v5.25 (polished formal core; anytime-valid / TARA / martingale references entirely removed from formal supplement; 62pp, 38 bibitems) → v5.30 (related-work compression + new §"Core record calculus" formalization; 70pp, 28 sections) → v5.34 (regime-gate-closure formal core; 77pp, 29 sections, 38 bibitems).  IP-strategic significance: by v5.25 the formal supplement was free of all anytime-valid runtime-monitoring infrastructure, decoupling the formal physics academic timeline from the AT-005 patent timeline.  Each predecessor archived to `Old/`.  Top folder: main-body v2.4 + supplement v5.34.

- **v2.1 main + Supplement v1.1 (2026-04-21):** Phase 12.3 I3 + quantum-horizon coupling ingest. Supplement: new §sec:hilbert_acc_quantum Proposition tying the `acc_quantum(d)` factory to the Paper-5 Hilbert-space construction ($\mathcal{H} = \pi_Q(\mathrm{acc}_{\mathrm{quantum}}(d))$, $\dim\mathcal{H} = d = \pi_Q$, $\mathrm{ACC} = \ln d$, Born rule as $\pi_Q$-consistent probability assignment); new §sec:I3_thermo_quantum Theorem stating $I3$ on the Paper-5 Hilbert space ($S_{\mathrm{vN}}(\rho_{\mathrm{max-mixed}}) = \ln\dim\mathcal{H} = \mathrm{ACC}$) with two remarks (thermo-quantum content; entropy ≤ ACC bound reading); new §sec:sectors_and_measurement Corollary "Sector A ↔ Sector B crossings as measurement" framing unitary evolution as Sector-A-preserving target re-pointing and measurement as Sector A → Sector B crossing, with the record register identified at the interface-capacity level with $V_{\mathrm{global}}$ (epistemic tag [P + framing] — not a new proof, a new reading of existing $T_{\mathrm{decoherence}} + T_{\mathrm{interface\,sector\,bridge}}$ content); theorem index extended with 4 new rows. Main: new §sec:summary_TACC "Paper 5 inside the T_ACC ledger" paragraph in Summary; coderefs to $I3$ + bridge theorem + lemma. Archive: `Old/Paper_5_*_pre-Phase12.3.{tex,pdf}`. Upstream reference: Three-Layer Ontology doc §6.

**Core claim:** [[Axiom A1]] forces quantum mechanics from first principles. The structure of admissible distinction-enforcement necessarily gives rise to complex Hilbert space, the [[Born Rule]], and entanglement via tensor products. Not assumed; derived.

**Key theorems:**
- T2 (`check_T2`) — Hilbert space forced by operability constraints
- T3 (`check_T3`) — Noncommutativity of operators is necessary
- T_Born (`check_T_Born`) — [[Born Rule]] probability formula
- T_Tsirelson (`check_T_Tsirelson`) — Tsirelson bound on correlations
- T_CPTP (`check_T_CPTP`) — Completely positive, trace-preserving maps
- [[Tensor Product Structure]] — Multi-particle Hilbert spaces

**Content:**
- Operability bound → Hilbert space structure
- Why complex numbers, not real or quaternionic
- Proof of the Born rule from enforcement cost
- Superposition and entanglement as cost-efficient encodings
- Quantum non-locality without action-at-a-distance
- CPTP maps and the arrow from pure to mixed states
- Connection to quantum information and von Neumann algebras

**Implementation:** `core.py` (48 checks)

**Status notes:**
- Fully implemented in v6.9
- v2.0-PLEC main paper stable; Technical Supplement v1.0 built fresh 2026-04-19 evening as 31pp self-contained formal companion.
- Supplement contents: PLEC + imported lemma restatements; linearity proof from coherence closure; complex Hilbert via Frobenius trichotomy (R ruled out by Regime-R R4, H ruled out by L_loc commutativity); T_tensor; T_Born via Gleason; T_Hermitian + T_CPTP with Stinespring-dilation interface-mediator interpretation; T_decoherence via record-locking channels (Type III regime exit); L_spectral_action_internal with full Boltzmann-cutoff derivation and SM Lagrangian coefficients (a_0=61, a_2≈21.985, a_4≈87.201) from Seeley–DeWitt; L_QG_P1_closure UV completion as Type IV exit; six countermodels; red-team on H1/H2/H3 + Gleason meta-attack; theorem index + dependency diagram.
- **Phase 10 status:** supplement present, pending Stanford agentic review cycle.

## See also
- [[Born Rule]]
- [[Axiom A1]]
- [[Paper 1 - Spine]]
- [[T_ACC Unification]] — Paper 5 Hilbert space = $\pi_Q(\mathrm{acc}_{\mathrm{quantum}})$; $I3$ thermo-quantum realized here
- [[Interface-Sector Bridge]] — measurement as Sector A ↔ Sector B crossing
- [[Paper 3 - Ledgers]] — ACC formalization home (Supplement v1.2 §7)
