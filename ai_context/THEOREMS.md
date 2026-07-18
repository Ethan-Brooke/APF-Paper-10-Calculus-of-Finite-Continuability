# THEOREMS.md — Full Bank Catalog

Full catalog of **3918** bank-registered theorems in the canonical APF codebase (at the time of this release).

**Bundled in this Paper 10 repo:** 3 of 3918. Bundled checks are runnable locally via `python run_checks.py`; non-bundled checks are referenced by name only and require the full canonical codebase at `__APF Library/Codebase/APF_Codebase_v<version>/` to execute.

## Legend

**Epistemic tags:**

- `P` — [P] internally derived
- `P+I` — [P]+[I] derived + external closure
- `P_structural` — [P_structural] structural identification
- `Pred` — [Pred] phenomenological prediction
- `C` — [C] conjecture (unproved)
- `P+lattice` — [P+lattice] uses lattice QCD input
- `(untagged)` — (untagged)

**Bundled column:** `✓` = runnable in this repo; `·` = referenced but not bundled.

**Kind column:** `theorem` (T_*), `lemma` (L_*, Delta_*), `red_team` (RT_*), `regime` (Regime_*), `closure` (A9_*), `other`.

---

## `apf/core.py` — 62 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `A1` | other | `AXIOM` | THE foundational axiom. Admissibility capacity C is finite and positive: sum epsilon(d) <= C < infinity for all enforceable distinctions d. Not derived. Framework-independent of the specific value of C ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â only finiteness and positivity matter. |
| · | `A1_disjoint_scope` | other | `AXIOM_COROLLARY` | A1 sum_d epsilon(d) <= C is always a valid budget bound. It is an EXACT accounting of capacity consumed iff all M_d are pairwise disjoint. Overlapping mechanisms cause double-counting of shared substrate: sum > actual capacity consumed (overcount = shared_cap). T_sep (disjoint-mechanism condition... |
| · | `D_quotient_forced` | other | `P` | Omega = D-quotient is uniquely forced: no finer (zero-cost DOF inert), no coarser (positive-cost DOF operationally real). |
| · | `L_MD_extension` | lemma | `P_structural` | Lemma 1 of the IJC reference doc: any nonempty perturbation class T admitting a minimal defense act delta_T has cost kappa(delta_T) >= mu* > 0.  Route A selected (FD5 covers threat-defense acts directly; MD applies to delta_T without mediation).  Closes the zero-cost-joint-defense smuggle: withou... |
| · | `L_M_derived` | lemma | `P` | M derived: A1 -> T_field [P] -> C_total = 61 types. 61 >= 2 -> M. MECE partition [3, 16, 42]. Postulate count reduced: {A1, M, NT} -> {A1}. |
| · | `L_NT_derived` | lemma | `P` | NT derived from field content: gauge dimensions 8, 3, 1 give realignment costs 8, 3, 1 (all distinct). Therefore exists d_i, d_j in D with eps(d_i) != eps(d_j). NT holds. |
| · | `L_NZ` | lemma | `P` | No admissible admissibility history contains a Zeno sequence. After L_eps*: at most n_max=10 acts per interface. Admissibility is a realizable commitment process (A1 Aspect 3). |
| · | `L_Omega_sign` | lemma | `P` | First quantitative test of the canonical object. ÃƒÅ½Ã‚Â©_inter = ÃƒÂ¢Ã‹â€ Ã¢â‚¬â„¢I(A:B) (negative mutual information) in the quantum-admissible regime. For pure states: \|ÃƒÅ½Ã‚Â©_inter\| = 2Ãƒâ€šÃ‚Â·S_ent. Sign dichotomy: ÃƒÅ½Ã‚Â©_local ÃƒÂ¢Ã¢â‚¬Â°Ã‚Â¥ 0 generically (L_nc, composition costs more... |
| · | `L_Pi` | lemma | `P+IJC` | GIVEN the IJC premise (branch-(IJC) interface: T(d1,d2) ⊋ T(d1) U T(d2)), Delta(d1,d2) > 0 follows from Lemma 1 (L_MD_extension), and the joint admissibility generator E_{d1,d2} cannot lie in the diagonal subalgebra A_diag = span{E_d}.  Proof by contradiction: A_diag forces cost-additivity, but D... |
| · | `L_T2` | lemma | `P` | Finite non-commuting Hermitian witness (sigma_x, sigma_z) generates concrete matrix *-algebra M_2(C). Concrete state omega=Tr/2 exists constructively. Concrete GNS: H=M_2(C), <a,b>=omega(a*b), pi(x)b=xb. Gram matrix verified PSD with eigenvalues > 0. No C*-completion, no Hahn-Banach, no Kadison n... |
| · | `L_col` | lemma | `P` | Founding-chain lemma (A1 -> {L_nc, L_irr, L_col} -> Theorem_R). Structural content: under A1 the admissibility set is an argmin of the derived cost functional dim(G) (Paper 13 v8.22 App. A.4); process reading: A1 + L_irr force bounded refinement to terminate (Paper 18 v3.20 collapse sketch). Witn... |
| · | `L_cost` | lemma | `P` | A1 cardinality bound + Cauchy functional equation -> the UNIQUE realignment cost is C(E) = n(E)*epsilon. Functional-form rival defeated: n^alpha (C2 additivity). The gauge clause n(G) = dim(G) and the generator-primitivity proofs live in L_cost_gauge (v24.3.404 split); gauge-invariant rivals are ... |
| · | `L_cost_gauge` | lemma | `P` | For a gauge group G the channel count is the group dimension: n(G) = dim(G) (generator primitivity -- Proof A: orbit-separation + Brouwer invariance of domain on Aut(M_n) [T3]; Proof B: L_nc bracket-closure + L_epsilon* marginal cost; either suffices). With L_cost's unique functional: C(G) = dim(... |
| · | `L_epsilon*` | lemma | `P` | No infinitesimal meaningful distinctions. Proof: if eps_Gamma = 0, could pack arbitrarily many independent meaningful distinctions into admissibility physics at vanishing total cost -> admissible perturbations reshuffle at zero cost -> distinctions not robust -> not meaningful. Contradiction. Pre... |
| · | `L_irr` | lemma | `P` | A1 + occupancy + L_loc + L_cost ==> A4. Mechanism: the joint-distinction cost (Delta>0, L_cost form + occupancy input) commits capacity to cross-interface correlations. Locality (L_loc) prevents any single observer from recovering this capacity. Result: irreversibility under local observation. Ve... |
| · | `L_irr_uniform` | lemma | `P` | If gravity is irreversible, any non-trivially coupled gauge-matter sector inherits irreversibility at shared interfaces. Proof: (1) records are local interface objects (L_loc), (2) gauge-gravity coupling via shared enforcement interfaces (T7B), (3) L_nc superadditivity at shared interfaces makes ... |
| · | `L_loc` | lemma | `P` | A1 + M + NT ==> A3. Chain: admissibility physics (floor(C/epsilon) bound) + sufficient richness (N_phys > C/epsilon) -> admissibility must distribute over multiple independent loci -> locality. Verified: 6 distinctions with epsilon=2 fail at single interface (cost 19.5 > C=10) but succeed distrib... |
| · | `L_nc` | lemma | `P` | Non-closure witness: E_1=6, E_2=6 each <= C=10, but E_1+E_2=12 > 10. L_loc (admissibility factorization) guarantees distributed interfaces; A1 (admissibility physics) bounds each. Composition at shared cut-sets exceeds local budgets. Formerly axiom A2; now derived from A1+L_loc. |
| · | `L_threat_substrate_realization` | lemma | `P_structural_reading` | Lemma 2 of the IJC reference doc: under sharp admissibility at a finite-capacity interface satisfying A1+MD+A2+BW, if a pair {d1, d2} is in branch (IJC), then the minimal joint defender W_{12} is NOT contained in M_{d1} (+) M_{d2}.  Equivalently, there exists Pi_{12} ⊆ V_Gamma with Pi_{12} ∩ (M_{... |
| · | `M` | other | `P` | At least 2 distinguishable subsystems exist. The weakest possible non-triviality claim. Without M, A1 is trivially satisfied by a single subsystem. Used only in L_loc derivation. DERIVED from A1 via L_M_derived [P] (v5.3.4): T_field → 61 types. |
| · | `M_Omega` | other | `P` | At full saturation (Bekenstein limit), non-uniform measure over microstates requires extra distinctions (Step 1) that cost admissibility capacity (Step 2, L_epsilon*) unavailable at saturation (Step 3). Uniformity is the unique permutation-invariant assignment introducing no extra distinctions (S... |
| · | `NT` | other | `P` | NT: there exist distinctions d_i, d_j with eps(d_i) != eps(d_j). Witness: eps(d_1)=2, eps(d_2)=3, C=5 -> residual budgets 3 vs 2 differ. Without NT all costs equal eps*, residual budgets C-eps* identical, T1 Step 2 produces no asymmetry and order-dependence fails. DERIVED from A1 via L_NT_derived... |
| · | `OR2_repetition` | other | `P` | 3-bit repetition code: destruction = detection = d_min = 2 bit-flips. Per-event maintenance cost in [1, 4/3] for all p in (0, 1/2). OR2-strong holds at code-distance scale. Time-averaged maintenance -> 0 as p -> 0 is a rate phenomenon, not a per-event cost failure. |
| · | `OR2_spin` | other | `P` | For spin-1/2 in Zeeman field Delta_E coupled to thermal bath: destruction cost = maintenance cost per event = detection cost (WAY bound) = Delta_E. OR2-strong holds in strong-gap regime (Delta_E >> k_BT). Gap-collapse limit Delta_E -> 0 causes d to exit D (APF inapplicable by design), not an OR2 ... |
| · | `OR2_steane` | other | `P` | Steane [[7,1,3]] code: destruction = d_min = 3 Paulis. Detection (bare logical qubit) = 30 ops; OR2-strong fails for bare logical. Resolution (L_loc): ancilla syndrome apparatus is co-located with logical qubit and must be included in the enforcement interface. Composite interface maintenance ~ 1... |
| · | `P4_IMP` | other | `P` | Interface Maintenance Principle: two distinctions sharing interface Gamma require maintaining d_Gamma (the interface capacity itself) in D. Robustness gives c_Gamma >= epsilon(d_Gamma) > 0. LP with cross-talk kappa: D_joint = eps1+eps2+c_Gamma*(1-2*kappa). Strict inequality holds for kappa < 1/2 ... |
| · | `P_cls` | other | `P` | Over C: tensor product stays in complex matrix class. Over H: composite exits quaternionic class (Adler 1995). L_loc forbids the new DOF this would require. |
| · | `P_exhaust` | other | `P` | Two mechanism predicates -- Q1 (gauge addressability, from T3) and Q2 (SU(3) confinement) -- are the ONLY independent mechanism-level partition criteria at Bekenstein saturation. Proof by sector-by-sector exhaustion: vacuum cannot split (contradiction with Q1=0 definition), dark cannot split (no ... |
| · | `P_tom` | other | `P` | Layer 1: L_loc gives surplus=0. Layer 2: exhaustion excludes zero-cost antisymmetric correlator. K_joint(C)=16=K_local; K_joint(R)=10>9=K_local. |
| · | `T0` | theorem | `P` | Axiom satisfiability witnesses: (A1) 4-node ledger with superadditivity Delta=4; (L_irr) monotone 2-interface world with 3 distinctions -- correlation c spans both interfaces, locally unrecoverable (Delta_S(s,c)=3, costs 8 at Gamma_S and 8 at Gamma_E); (L_nc) sigma_x, sigma_z non-commuting admiss... |
| · | `T1` | theorem | `P` | Non-closure of distinction set under admissibility composition implies existence of incompatible observable pairs. Witness: sigma_x and sigma_z are each Hermitian (observable) but [sigma_x, sigma_z] != 0 and their product is not Hermitian. Therefore no common eigenbasis exists -- they cannot be j... |
| · | `T1b` | theorem | `P` | T1 gives E_d1 != E_d2 on Omega. OR2/T_adj gives self-adjointness. T1b: Alg_R{E_d} is a real *-algebra. The sector projections commute; noncommutativity is introduced by F_Pi (L_Pi -> T_alg). |
| · | `T2` | theorem | `P` | Non-closure (L_nc) forces non-commutative *-algebra. CORE CLAIM [P]: L_T2 proves constructively that M_2(C) with trace state gives a concrete 4-dim GNS Hilbert space representation -- no C*-completion, no Hahn-Banach needed. This finite witness is all the derivation chain requires. Extension to f... |
| · | `T2b` | theorem | `P` | Paper 1 spine (archived 180p supplement, T2b): the enforcement algebra -- finite-dimensional real *-algebra with faithful positive state omega (O4) and *-involution (OR2) -- complexifies to a semisimple complex *-algebra; Wedderburn--Artin gives A_C ~= (+)_k M_{n_k}(C) acting faithfully on (+)_k ... |
| · | `T3` | theorem | `P` | Local admissibility at each point -> local automorphism group. Skolem-Noether: Aut*(M_n) ~= PU(n). Continuity over base space -> principal G-bundle. Gauge connection = parallel transport of admissibility frames. Yang-Mills dynamics requires additional assumptions (stated explicitly). v5.3.5: Dopl... |
| · | `T_Born` | theorem | `P` | Born rule p(E) = Tr(rhoE) is the UNIQUE probability assignment satisfying positivity, additivity, normalization, and admissibility invariance in dim >= 3 (Gleason's theorem). Verified on 3D witness with projective and non-projective POVMs, plus unitary invariance check. |
| · | `T_CPTP` | theorem | `P` | CPTP maps are the unique admissibility-preserving evolution channels. Verified: amplitude damping channel with Kraus operators satisfies TP (Sigma K+K = I), CP ((PhiI) preserves PSD on extended system), and outputs valid density matrices. Transpose shown NOT CP via Peres criterion (negative parti... |
| · | `T_Hermitian` | theorem | `P` | In the T2 Hilbert-space representation, observable sector is A_sa. Self-adjoint elements have real spectrum by spectral theorem. This is a representation convention (real eigenvalues <=> real realignment costs from A1), not derived from L_irr or decoherence. Verified: sigma_x, sigma_z in A_sa wit... |
| · | `T_IJC_dichotomy` | theorem | `P_structural` | Theorem 1 of the IJC reference doc: for any pair {d1, d2} of jointly meaningful distinctions at an interface, exactly one of (Sep) T(d1,d2) = T(d1) U T(d2) or (IJC) T(d1,d2) ⊋ T(d1) U T(d2) holds. Structurally a tautology (logical exhaustion on set inclusion); operationalized here on two test int... |
| · | `T_IJC_from_partition_structure` | theorem | `P+IJC` | Phase 20 sharpened derivation theorem.  Under FD1 (substrate as set of configurations) + FD3 (distinctions as binary partitions) + FD2 substrate richness (multiple configs per joint cell) + FD4 + MD (positive cost floor on perturbations), IJC is derived for any pair {d1, d2} whose joint refinemen... |
| · | `T_M` | theorem | `P` | Independence  disjoint anchors. Full proof: () L_loc factorization gives independent budgets at disjoint interfaces. (=>) Shared anchor -> finite budget competition at that interface -> detectable correlation -> not independent. Monogamy (degree-1) follows at saturation C_i = epsilon. |
| · | `T_Tsirelson` | theorem | `P` | Cirelson identity verified: S^2 = 4I - [a1,a2]x[b1,b2]. Commutator norms <= 2 (from a^2=I in M_n(C)). \|\|S\|\| = 2.828427 = 2*sqrt(2). Saturated by maximally entangled state. Quantum bound > classical bound 2. |
| · | `T_adj` | theorem | `P` | Paper 1 Technical Supplement (spine-era T_adj, thm:Tadj_sector): each sector map E_d is the B-orthogonal projection onto its anchor M_d w.r.t. the block-orthogonal bilinear form forced by the sector decomposition (L_omega content, instantiated in-body): E_d^2 = E_d, E_d^dagger = E_d, ker(E_d) = t... |
| · | `T_adj_commutes` | theorem | `P` | T_adj Step 2 defines E_d\|_{M_d}=id, E_d\|_{M_d'}=0, E_d\|_Pi=0. From these definitions: E_d1*E_d2 = 0 = E_d2*E_d1 for all d1!=d2, so [E_d1,E_d2] = 0. The diagonal subalgebra A_diag = span{E_d} is commutative (isomorphic to R^\|D\|). This is the classical regime. The full algebra A strictly contains A... |
| · | `T_alg` | theorem | `P+IJC` | The algebra A = Alg{E_d} generated by admissibility maps has no faithful commutative representation.  Phase 19h AUDIT (2026-04-26): the abstract order-dependence route in the original docstring is a STRUCTURAL SKETCH, not load-bearing; the implication "commutativity => E_d3 E_d1 = E_d3 E_d2" does... |
| · | `T_alg_FPi` | theorem | `P+IJC` | T_alg revised: noncommutativity [E_d1, F_Pi] != 0 proved directly. Key steps: (1) E_d1\|_Pi = 0 (T_adj Step 2). (2) F_Pi\|_Pi != 0 (L_Pi Step 5). (3) For v in Pi: E_d1(F_Pi(v)) != 0 but F_Pi(E_d1(v)) = F_Pi(0) = 0. Therefore [E_d1, F_Pi] != 0. No GNS construction needed. M_2(C) witness (corrected):... |
| · | `T_branch_taxonomy_inclusions` | theorem | `P_regime` | The branch-taxonomy inclusions of Paper 5 v5.1 (Lemmas 4.5, 4.6) hold on the canonical witnesses. SepAdm always implies SepStr (an admissible defender is a fortiori a defender); structural IJC always implies admissible IJC (no commuting defender at all means no admissible commuting defender). The... |
| · | `T_canonical` | theorem | `P` | Paper 13 Ãƒâ€šÃ‚Â§9. The admissibility structure is a sheaf of distinction sets with non-local cost. LOCAL: Adm_Gamma is finite order ideal, bounded depth floor(C/eps), not sublattice, generated by antichain Max(Gamma). INTER-INTERFACE: restriction maps from admissibility footprint; set-level sep... |
| · | `T_entropy` | theorem | `P` | Entropy = irreversibly committed correlation capacity at interfaces. In quantum regimes, S(rho) = -Tr(rho log rho). Verified: S(pure)=0, S(max_mixed)=1.0986=log(3), 0 < S(mid) < log(d), subadditivity S(AB) <= S(A)+S(B), concavity of mixing. |
| · | `T_epsilon` | theorem | `P` | Minimum nonzero realignment cost epsilon > 0 exists. From L_epsilon* (meaningful distinctions have minimum admissibility quantum eps_Gamma > 0) + A1 (admissibility physics bounds total cost). eps = eps_Gamma is the infimum over all independent meaningful distinctions. Previous gap ("finite distin... |
| · | `T_eta` | theorem | `P` | eta/epsilon <= 1. Full proof: T_M gives monogamy (at most 1 independent correlation per distinction). A1 gives budget epsilon + eta <= C_i. T_kappa gives C_i >= 2*epsilon. At saturation (C_i = 2*epsilon): eta <= epsilon. Tight at saturation. |
| · | `T_inseparable_IJC` | theorem | `P+IJC` | Phase 21 strengthened Dichotomy.  The Phase-19 IJC framing (set-theoretic excess of joint threat) is necessary but not sufficient to force noncommutativity: the auditor exhibited a substrate that admits a factorization S = Q × Π under which an independent commuting d_Pi defends the joint threat, ... |
| · | `T_kappa` | theorem | `P` | kappa = 2. Lower bound [P]: L_nc (system interface Gamma_S) + L_irr (environment interface Gamma_E) give two independent epsilon-commitments at separate interfaces -> kappa >= 2. Upper bound [P_structural]: distinction spans at most two interfaces (system + environment); third interface requires ... |
| · | `T_mode_partition_conservation` | theorem | `P+IJC` | Phase 19o follow-up bank check landing Prop 2.3 from the conservation/boats-parable reference doc.  At a branch-(IJC) interface with substrate V = M_d1 (+) M_d2 (+) Pi_12, the mode decomposition V_+ (common) + V_- (differential) + V_Pi (pool) carries the cost-budget structure: F_Pi annihilates V_... |
| · | `T_no_IJC_no_noncommutativity` | theorem | `P_structural` | Spectator countermodel: V = M_d1 (+) M_d2 (+) Pi with Pi inert. A1 + MD + A2 + BW all PASS. Pair {d1, d2} in branch (Sep) of the IJC dichotomy theorem: T(d1, d2) = T(d1) U T(d2). Joint defender W_{12} = M_d1 (+) M_d2 is block-diagonal; Delta = 0; F_Pi = 0; [E_d1, E_{d1,d2}] = [E_d2, E_{d1,d2}] = ... |
| · | `T_quantum_admissibility_condition` | theorem | `P_regime` | Paper 5 v5.1 Theorem 1518 (IJC produces a QAC witness in record-complete coherent interfaces): branch (IJC) plus record-completeness plus coherent-continuation richness produces a Quantum Admissibility Condition witness -- coherent continuations whose Boolean record-locking incurs strictly positi... |
| · | `T_sep` | theorem | `P` | Paper 1 Technical Supplement (spine-era T_sep^op / T_sep): independently enforceable distinctions have disjoint anchors iff joint enforcement cost is exactly additive; a maximal antichain induces the pre-metric direct sum S_Gamma = (+)_d M_d (+) Pi. Forward: FD3 locality + K3 additivity. Converse... |
| · | `T_tensor` | theorem | `P` | Tensor product H_A H_B is the minimal composite space satisfying bilinear composition and closure. Verified: dim(2 x 3) = 6, product states have pure subsystems (purity=1), entangled states have mixed subsystems (S_ent = 0.6931 > 0). Bilinearity confirmed. |
| · | `disjoint_partition` | other | `P` | Substrate disjointness derived from L_cost integrality: eps* is indivisible across interfaces. |
| · | `kappa_zero_Tsep` | other | `P` | Under T_sep disjoint-mechanism condition: delta_Gamma (substrate defense, in S_Gamma\(M_d1 cup M_d2)) and delta_i (mechanism defense, in M_di) occupy physically disjoint regions. Disjoint regions => zero cross-coverage => kappa = 0 (derived from T_sep, not assumed). kappa=0 => Delta = c_Gamma >= ... |
| · | `state_sensitivity` | other | `P+IJC` | Over R: K=3<N^2=4 (states blind to commutators). L_Delta gives Delta>0 detectable. F=R makes Delta undetectable: contradiction. Over H: K=6>N^2. F=C uniquely selected. [P+IJC] post-Phase-19g cascade: depends on T_alg which depends on L_Pi (IJC carrier). |
| · | `worked_example` | other | `P` | C=5, eps(d1)=2, eps(d2)=3, eps(d3)=5/2. Delta(d1,d2)=4>0 (superadditivity). BW: {d1,d3} admissible (residual 1/2), {d2,d3} inadmissible (residual -1/2). T1 witness: order-dependent admissibility outcomes. |

## `apf/gauge.py` — 31 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `B1_prime` | other | `P` | If V is real or pseudoreal, G-equivariant antilinear map J^{otimes n} provides admissibility-preserving identification B <-> B*, collapsing oriented composite distinctions. Complex type forced by L_irr robustness + minimality clause (no added grading). Closes bridge B1 from [Ps] to [P]. Counterex... |
| · | `L_B_operator_exclusion` | lemma | `P` | No B-violating operator exists at any mass dimension within the APF capacity budget. GUT embedding forbidden (budget saturated at 61). No leptoquarks, no X/Y bosons. SM accidental symmetry: no perturbative B violation. Higher-dim operators suppressed by M_Pl: dim-6 τ > 10^49 yr, dim-7 τ > 10^87 y... |
| · | `L_Fisher_gradient` | lemma | `P` | The Lyapunov function V(w) proving sin²θ_W = 3/13 stability is the Bregman/Fisher divergence from w*. Forward (IR) flow β = +P∇V is gradient ascent; UV flow toward w* is gradient descent β_UV = -P∇V. Metric P_ij = w_i A_ij w_j (state-dependent). Fixed point w* = (3/8, 5/4) from Aw* = γ = (1, 17/4... |
| · | `L_MW_scheme_correction` | lemma | `P` | Scheme-consistency lemma for the W mass: with the 3/13 tree M_W^tree = 79.977 GeV, the MS-bar custodial Delta-rho family (top 0.00838, QCD -0.000629, Higgs -0.001504) with exact lever 10/7 gives M_W = 80.3336 GeV (exp 80.3692, 0.044%). The superseded mixed-scheme route (on-shell Delta r = 0.0362 ... |
| · | `L_W_mass` | lemma | `P` | M_W = 80.3336 GeV (exp 80.3692, err 0.044%). Tree: 79.977 GeV (0.49%). Δρ_top=0.00838, lever=10/7. Scheme fix: MS-bar Δρ replaces mixed on-shell Δr=0.0362. sin²θ_W=3/13 [P]. [L_MW_scheme_correction] |
| · | `L_Weinberg_dim` | lemma | `P` | Unique Delta_L=2 operator has dimension 5. EXHAUSTIVE CLASSIFICATION from derived fields (no import): Case A (LL+HH): dim=5, Y=0, SU(2) singlet. UNIQUE at dim<=5. Case B (Le_R+H): Y never neutralizes at dim<=5. Case C (e_Re_R+H): needs 4 Higgs, dim=7. Triplet contraction: no triplet scalar in spe... |
| · | `L_anomaly_free` | lemma | `P` | 7/7 anomaly conditions verified with exact rational arithmetic on framework-derived content. [SU(3)]^3=0, [SU(2)]^3=0 (automatic), [SU(3)]^2 U(1)=0, [SU(2)]^2 U(1)=0, [U(1)]^3=0, [grav]^2 U(1)=0, Witten=0. Particle content derived from capacity (T_field), not from anomaly cancellation. Anomaly-fr... |
| · | `L_anomaly_nonpert` | lemma | `P` | Anomaly cancellation is exact and non-perturbative: (1) Algebraic identities in rational Y_i (exact at all loops). (2) Finite index = 0 (chiral balance with ν_R). (3) No instantons NATIVELY: θ=0 (unique vacuum), B exact post-saturation (T_proton; pre-saturation violable per L_Sakharov, seeding η_... |
| · | `L_baryogenesis_NNLO` | lemma | `P` | η_B(NNLO) = 6.194e-10 (exp 6.12e-10 ± 4e-12). Error: 1.2% (NLO was 0.5%). Pull: 1.8σ. δ₂ = (V_ub/V_cb)²sin²δ = 0.0066. Correction worsens fit slightly but remains < 2σ. |
| · | `L_count` | lemma | `P` | Capacity units = structural admissibility channels, not field modes. Each channel is one independently enforceable binary distinction (kappa=2 from T_kappa, cost=epsilon from L_epsilon*). Gauge: 12 Lie algebra directions (automorphisms, not polarizations). Fermion: 45 chiral species (presences, n... |
| · | `L_dim_angle` | lemma | `P` | Angular advance per generation step: theta_op = pi/d_op. Budget Phi = 2*pi*j = pi. Yukawa: d_Y=4=d (unique at d=4). theta_Y = pi/4 = holonomy (verified). Weinberg: d_W=5=d_Y+1. theta_W = pi/5 (predicted, 0.110% mean PMNS error, 110x isolated). n=4 gives structural wall (resolved). |
| · | `L_gauge_template_uniqueness` | lemma | `P` | Exhaustive Lie algebra classification proves SU(N_c)xSU(2)xU(1) is the UNIQUE gauge template satisfying R1+R2+R3 (Theorem_R [P]). Step 2: 17 compact simple Lie algebras tested against R1 (complex + trilinear). Only SU(N_c>=3) passes. Step 3: Only SU(2) has faithful pseudoreal 2-dim rep (R2). Step... |
| · | `L_proton_decay_channels` | lemma | `P` | All 7 known B-violation mechanisms examined: 3 FORBIDDEN (no GUT, no monopoles, ν_R conserves B), 4 NEGLIGIBLE (sphalerons 10^-323, dim-6 at M_Pl 10^48 yr, gravitational 10^45 yr). Weakest bound exceeds Super-K by 10^10. Defense in depth: even without T_proton's exact argument, no individual chan... |
| · | `L_strong_CP_synthesis` | lemma | `P` | Unified CP violation pattern from A1 cost-benefit: theta_QCD = 0 (topological, no capacity gain, zero cost wins). delta_CKM = pi/4 (geometric, enables 6 history sectors, capacity gain ln(6) = 1.79 exceeds cost). CPT exact -> T violation = CP violation = pi/4 (T_CPT). Key insight: CP-violating par... |
| · | `T4` | theorem | `P` | Confinement + chirality + Witten anomaly freedom + anomaly cancellation select SU(N_c) * SU(2) * U(1) as the unique minimal structure. N_c = 3 is the smallest confining group with chiral matter. v4.3.2: AF derived from L_AF_capacity (det(A)=m>0 => UV attractor). Confinement derived from T_confine... |
| · | `T4E` | theorem | `P` | Three generations emerge with natural mass hierarchy. Capacity ordering: 1st gen cheapest, 3rd gen most expensive. CKM mixing from cross-generation interference eta. Yukawa ratios are regime parameters (parametrization boundary). |
| · | `T4F` | theorem | `P` | 3 generations use E(3) = 6 of C_EW = 8 capacity. Saturation ratio = 75%. Near-saturation explains why no 4th generation exists: E(4) = 10 > 8 = C_EW. |
| · | `T5` | theorem | `P` | Anomaly cancellation with SU(3)*SU(2)*U(1) and template {Q,L,u,d,e} forces unique hypercharge pattern. Analytic proof: z^2 - 2z - 8 = 0 gives z {4, -2}, which are ud related. Pattern is UNIQUE. |
| · | `T7` | theorem | `P` | N_gen = 3. E(N) = N(N+1)/2 in epsilon-units. E(3) = 6 <= 8 < 10 = E(4). C_EW = * channels = 2 * 4 = 8. |
| · | `T9` | theorem | `P` | k = 3 admissibility operations -> 6 inequivalent histories. Each ordering produces a distinct CP map. Record-locking (A4) prevents merging -> orthogonal sectors. |
| · | `T_Higgs` | theorem | `P` | EW vacuum must break (A4: unbroken -> records unstable). Broken vacuum has unique minimum v* (0,1) with positive curvature -> massive Higgs-like scalar exists. Verified: 9/9 non-linear models give d^2E/dv^2>0 at pivot. Linear screening eliminated (negative curvature). Screening exponent: ~_4Er^2(... |
| · | `T_center_order_parameter_triality` | theorem | `P` | At IR saturation an isolated colour charge in R is gluon-screenable to an admissible singlet composite (finite free energy, <P_R> != 0) IFF N-ality t(R) = 0; t(R) != 0 stays confined. Gluons (adjoint) have t=0 so dressing preserves N-ality; the root lattice = the t=0 sublattice (index N) gives su... |
| · | `T_channels` | theorem | `P` | channels_EW = 4. Derived: mixer = dim(su(2)) = 3 (analytic), bookkeeper = 1 (anomaly polynomial z^2-2z-8=0 has unique positive root z=4, giving one U(1) hypercharge). Grid scan is a regression test confirming no solutions below 4. |
| · | `T_confinement` | theorem | `P` | SU(3) AF (m=8>0, L_AF_capacity) => IR coupling growth; AT IR capacity-saturation (the Step-2 CARRIED PREMISE -- not derived here; T4F is flavor/EW-side only, per the HONEST LIMITATION; endpoint typing: check_T_ym_ir_endpoint_trichotomy_branch2_open, yang_mills_md_bridge.py) slack < epsilon => non... |
| · | `T_field` | theorem | `P` | Phase 1: scanned 4680 declared-ansatz templates (7 filters) -> 1 unique minimum = SM (five feasible classes post-CPT; minimality selects 45). Phase 2: 5 closed-form proofs exclude the ENUMERATED enlargement directions (reps 10/15 AF-killed, colored SU(2) triplets AF-killed, colorless triplets kil... |
| · | `T_gauge` | theorem | `P` | Anomaly equation z^2-2z-(N_c^2-1)=0 SOLVED for each N_c. All odd N_c have solutions (N_c=3: z in (4, -2), N_c=5: z in (6, -4), etc). Even N_c fail Witten. Among viable: N_c=3 wins by capacity cost (dim=12). N_c=5 viable but costs dim=28. Selection is by OPTIMIZATION, not by fiat. Objective: routi... |
| · | `T_particle` | theorem | `P` | Admissibility potential V(Phi) derived from L_epsilon* + T_M + A1. SSB forced (Phi=0 unstable), mass gap from d^2V > 0 at well, no classical soliton localizes -> particles require T1+T2 quantum structure. All structural checks pass. |
| · | `T_proton` | theorem | `P` | Baryon number is EXACTLY conserved at full Bekenstein saturation. Three steps: (1) P_exhaust: partition 3+16+42=61 is sharp (MECE) at saturation. (2) L_irr: saturation is irreversible; universe cannot return to pre-saturation regime. (3) No admissible B-changing move exists: partition predicates ... |
| · | `T_theta_QCD` | theorem | `P` | theta_QCD = 0 from A1 + L_epsilon*. theta is topological (no new DOF, C unchanged at 61). L_epsilon*: maintaining theta!=0 costs >= epsilon (enforceable distinction). theta=0: CP symmetry default, zero additional cost. A1 selects minimum cost at fixed capacity: theta=0. CKM phase survives: genera... |
| · | `T_vacuum_stability` | theorem | `P` | EW vacuum is absolutely stable [P]. Admissibility potential has UNIQUE minimum at Phi/C = 0.729 with V = -0.0948. No second minimum (1 minimum total). V(0) = 0.0 > V(well), V(near C) = 49.50 > V(well). Divergence at Phi -> C prevents runaway (A1: admissibility physics). Uniqueness from M_Omega (u... |
| · | `Theorem_R` | other | `P` | Any admissible interaction theory satisfying A1 must support: R1 (faithful complex 3-dim carrier from L_nc + T_M + B1_prime: oriented composites require trilinear invariant on complex carrier), R2 (faithful pseudoreal 2-dim carrier from L_irr + T_M: admissibility independence requires intrinsic g... |

## `apf/generations.py` — 89 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `L_AF_capacity` | lemma | `P` | det(A(m,x)) = m (exact). m>0 (non-Abelian): A invertible, PD, unique UV fixed point w* = A^{-1}gamma with w*>0 for all SU(N>=2). m=0 (Abelian): A singular, no fixed point, Landau pole. Threshold: m > 15/8 = 15/8. All SU(N>=2) satisfy. Zero free parameters. |
| · | `L_CP_channel` | lemma | `P` | CP violation (J!=0) requires non-uniform channel charge difference: q_H - q_B must not be constant across generations. When q_H = q_B: M_d is rank 1, only one massive down quark, J=0 exactly. L_H_curv gives h=(0,1,0) [non-constant] -> rank(M_d)=2 -> J!=0. Verified: J=3.33e-05 (exp 3.08e-05, 8%). ... |
| · | `L_CP_dual_mechanism` | lemma | `P` | CKM and PMNS CP phases arise from different mechanisms. CKM: Q=0.052, C/Q=0.0013, ΔS(full range)=0.007 nats → entropy flat → holonomy selects π/4. PMNS: Q=0.935, C/Q=0.140, ΔS(π/2)=56 nats → entropy steep → Boltzmann forces δ=0. Stiffness ratio g_PMNS/g_CKM = 9551. Root cause: L_kB_sector [P] (k_... |
| · | `L_CP_geometric_bound` | lemma | `P` | Gram matrix positivity det G > 0 requires cos Φ > (Q-1)/C. PMNS: Q=0.935, C=0.1310, Φ_crit=120°. Phases \|Φ\| > 120° are geometrically forbidden. Boltzmann measure peaks at Φ=0: g_ΦΦ=34, σ_δ=10°. ΔS(π/2)=56 nats → P(π/2)/P(0) ≈ 3e-25. NuFIT best fit δ=197° is in the forbidden zone (det G = -0.061 <... |
| · | `L_D2q` | lemma | `P` | D2q := q(1) - 2q(2) + q(3) = -eps for ALL kappa >= 0. Pure algebra: the quadratic term in Q(g) is g(g-1)eps/2, whose second difference is eps. Negation from q = Q(N)-Q(g). Verified for kappa = 0..5. |
| · | `L_DUNE_response` | lemma | `P` | APF predicts δ_PMNS = 0° ± 10° (Boltzmann suppression 4e-25 at 90°). Current T2K+NOvA: δ ≈ -90° ± 40° (2.2σ from APF). DUNE Phase I (σ ≈ 12°): if δ=-90° confirmed, APF excluded at 7.5σ. Mechanism at stake: entropy dominance from Q_PMNS = 0.935 with d_eff = 102. Falsifiable 2028-2035. |
| · | `L_FN_ladder_uniqueness` | lemma | `P` | Among 16 partitions of 11 into 3 parts: 6 have q₃=0 (quadratic budget), 2 survive D2q=-ε filter: (7,4,0) with ε=1, (6,5,0) with ε=4. (7,4,0) selected uniquely by maximum hierarchy (variance): Var=8.22 > 6.89. Mass hierarchy m₁/m₂ ~ x³ = 1/8 matches observation (all sectors < 0.1). (6,5,0) gives m... |
| · | `L_Fisher_curvature` | lemma | `P` | At c=0: g_ab = 102 δ_ab, Γ^k_ij = -(1/2)\|ε_ijk\| (SO(3) structure constants), R = 3/(2 d_eff) = 0.014706 > 0 (S³). K = 1/408, r = 2√d_eff = 20.20. 81/81 Riemann components match constant-curvature form. R(CKM)=0.01442>0, R(PMNS)=0.01014>0: all physical parameters in positive-curvature region. |
| · | `L_Fisher_entropy_budget` | lemma | `P` | ΔS_CKM = 2.66 nats, ΔS_PMNS = 45.70 nats, total = 48.35 nats = 17.1% of S_dS = 282.1 nats. CP cost negligible (0.0031 nats, third order). Resolves 113% puzzle: stiffnesses ≠ entropy deficits. |
| · | `L_Fisher_factorization` | lemma | `P` | Total entropy S = S_gen(c) + S_nu(d) + S_sector(w) factorizes exactly via det(G^{1/2}MG^{1/2}) = det(G)det(M). The 7D Fisher metric is block-diagonal: g = g_gen ⊕ g_nu ⊕ g_sector. Eigenvalues: [1.3, 4.33, 5.83, 102, 102, 102]. Condition number: 78. Generation number and coupling constants indepen... |
| · | `L_Fisher_geodesic` | lemma | `P` | Boundary det(G)=0 at infinite geodesic distance (logarithmic divergence). Metric along axis: g(c) = d_eff(1+c²)/(1-c²)². d(Cabibbo)=2.33, d(PMNS θ₂₃)=11.01. Boltzmann width σ_c = 1/√d_eff = 0.099. |
| · | `L_GJ_from_capacity` | lemma | `P` | GJ modulation (1/N_c, N_c, 1) = (1/3, 3, 1) from capacity color channels. N_c = 3 from T_gauge [P]. Curvature concentration at gen-1 (L_Higgs_curvature_channel [P]). GJ(gen-1) = 2.97 ≈ 3, GJ(gen-0) = 0.33 ≈ 1/3. m_μ/m_τ = 0.06186 (+4.0%). No SU(5) GUT invoked. "Capacity color modulation" not "GJ ... |
| · | `L_Gram` | lemma | `P` | Competition matrix a_ij = Gram matrix of sector demand vectors in canonical object channel space. det(A) = m = dim(su(2)) = 3 by Cauchy-Binet (m nonzero minors, each = 1, x-independent). Verified: det = 3 at 7 x-values; generalizes to SU(N_w) for N_w = 2..6. gamma_2/gamma_1 = Tr(A) = 17/4. Chain:... |
| · | `L_Gram_generation` | lemma | `P` | L_Gram bilinear extends to generation routing in SU(2) adjoint. Generation demand d_g(a) = n_g . e_a. Gram overlap = sum_a d_g(a)d_h(a) = cos(theta_gh) by ONB completeness. Basis-independent (verified). Factorization: det(A) = m is direction-independent => generation and sector optimization decou... |
| · | `L_H_curv` | lemma | `P` | Integer LP on path graph 1-2-3: min sum(h) s.t. edge demands eps=1. Unique solution: h = (0, 1, 0), cost = 1. l2 minimizer (1/3,2/3,1/3) is fractional -> inadmissible under L_eps*. Bridge: L_eps* (discrete quanta) -> l1 (count minimization). |
| · | `L_LL_coherence` | lemma | `P` | Weinberg LLHH has 2 identical L fields. Exchange symmetry (definitional for identical quantum fields) -> identical restriction maps (T_canonical R4) -> coherence (Props 9.5-9.6). D_internal=2 >= 2 with coherence -> cos projection. d_3(nu) = cos(pi/5) = 0.809017, not sin^2(pi/5) = 0.345492. |
| · | `L_NLO_texture` | lemma | `P` | Doubly-asymmetric NLO: up-sector bookkeeper (k_B=3, complex, carries holonomy phase) receives eta = x^d/Q_max = 1/144. Down-sector bookkeeper (k_B=0, real) and both Higgs channels (real VEV) receive NO correction -- no phase coherence cost for real channels. delta_CKM: 85.4 -> 61.8 deg (exp 65.6,... |
| · | `L_NNLO_down_mass` | lemma | `P` | Single rank-1 NNLO: c = x³ = 0.125, ρ = x^d/d = 0.015625. m_d/m_s = 0.0522 (exp 0.05, +4.5%). δ = 66.0° (exp 65.6°, +0.6%). V_us = 0.2271 (exp 0.2243, +1.2%). Closes L_md_zero open problem. Three-effect hierarchy: rescale (0.125) >> cross (0.0020) >> lift (3.05e-05). |
| · | `L_NNLO_three_effects` | lemma | `P` | Rank-1 NNLO δM = c\|v_B + ρe3><v_B + ρe3\| decomposes into: (a) \|v_B><v_B\| rescaling (shifts δ from 61.8° to 66.0°); (b) ρ²\|e3><e3\| rank-lift (m_d/m_s from 0 to 0.063); (c) cross terms (V_us from 0.191 to 0.227). Cross terms ONLY exist in rank-1 form — independent channels cannot fix V_us. |
| · | `L_NNLO_up_mass` | lemma | `P` | NNLO up-sector: η = x⁷/9 = 0.000868. m_u/m_c = 0.0018 (exp 0.0021, err 16.1%). NLO was 0.0080 (281% error). Improvement: 17.5×. Same Δq = 3 Weinberg suppression as down-sector. |
| · | `L_PMNS_NLO_immune` | lemma | `P` | PMNS matrix receives NO NLO capacity-propagator correction. Charged lepton sector: k_B=0 [L_kB_sector P] (W_e=L*e*H, no H~ conjugation) -> flat connection -> eta_e=0 [L_NLO_texture P]. Neutrino sector: real symmetric Gram matrix -> eta_nu=0. Both sides NLO-free -> U_PMNS NLO-free. 0.11% mean PMNS... |
| · | `L_Yukawa_bilinear` | lemma | `P` | Yukawa coupling Y_{gh} = ψ(g)·ψ(h) = x^{q(g)+q(h)} from vertex locality + independent resolution (L_multiplicative_amplitude [P]). Single-channel Y is rank 1 (pure outer product). Hierarchy: m_t/m_c ~ x^{-8} = 256, m_c/m_u ~ x^{-6} = 64. Two channels (T_channels [P]) lift rank to 2 → CKM mixing. |
| · | `L_adjoint_sep` | lemma | `P` | Delta_k = 3 from L_channel_crossing: 2 propagation + 1 conjugation = 3 operations = 3 holonomy steps. dim(adj SU(2)) = 3 is corollary. v4.3.5: upgraded via L_channel_crossing. |
| · | `L_alpha_s` | lemma | `P` | α_s(M_Z) predicted from capacity structure + α_EM. Route A (sin²θ_W=3/13 + α_EM): α_s = 0.1197 (1.6% error, dominated by tree-level sin²θ_W). Route B (exp α₂): α_s = 0.1179 (0.02% error). M_cross = 9.61e+16 GeV. Import: 1-loop RG formula. Coefficients derived [L_beta_capacity]. Experimental input... |
| · | `L_angular_far_edge` | lemma | `P` | alpha_12(nu) = sin^2(pi/5)*cos^2(pi/5) = 0.226127. Off-diagonal squared of rank-1 projector at hub vertex. Rank-1: one angular distinction (L_epsilon*). State fixed by d_3 = cos(theta_W) (L_LL_coherence). Gen 1 couples through \|perp> (lightest mass = max rotation). Off-diagonal UNIQUELY determine... |
| · | `L_beta` | lemma | `P` | I1-I5 invariances grounded in canonical object: I1ÃƒÂ¢Ã¢â‚¬Â Ã‚ÂProp9.1, I2ÃƒÂ¢Ã¢â‚¬Â Ã‚ÂAut(ÃƒÅ½Ã¢â‚¬Å“), I3ÃƒÂ¢Ã¢â‚¬Â Ã‚ÂProps9.9-9.10, I4ÃƒÂ¢Ã¢â‚¬Â Ã‚ÂL_Gram, I5ÃƒÂ¢Ã¢â‚¬Â Ã‚ÂProp9.8. Mechanism: exact refinement (Prop 9.8) produces bilinear interaction term; Gram matrix (L_Gram) gives coe... |
| · | `L_beta_capacity` | lemma | `P` | 6\|b₃\| = C_vacuum = 42 and 6\|b₂\| = C_matter = 19, if and only if N_gen = 3. Two independent linear equations (66-8n = 9n+15 and 43-8n = 6n+1) both give n=3 uniquely. Overdetermined system: consistency is a non-trivial check. Independent generation derivation (cf. T4F). β-coefficients now derived f... |
| · | `L_boundary_projection` | lemma | `P` | ALL sectors [P]. Colored: cos(pi/d_op) [gauge coherence]. Colorless: sin^2(pi/d_op) [incoherent]. Neutrino: cos(pi/5) via LL coherence [L_LL_coherence P]. Down: 3.8%,0.9%. Lep: 2.0%,3.3%. |
| · | `L_c_FN_gap` | lemma | `P` | NNLO coefficient c = x^(q_B[0]-q_B[1]) = x^(7-4) = x³ = 0.125 = 1/8. Derived from FN charge gap between generation-0 (q_B=7) and generation-1 (q_B=4) in the up-sector bookkeeper tower (T_capacity_ladder [P]). Unique: alt gaps x^7 (16x too small) and x^4 (2x too small) give wrong m_d/m_s. Upgrades... |
| · | `L_capacity_depth` | lemma | `P` | ALL sectors [P]. Down x^9, Up x^12, Lep x^8, Nu x^(7/4)=0.297302 [L_capacity_per_dimension P]. |
| · | `L_capacity_per_dimension` | lemma | `P` | d_1(nu) = x^(q_B1/d_Y) = x^(7/4) = 0.297302. A1 uniform distribution: capacity per dim = q/d_op (same argument as angular per dim = pi/d_op in L_dim_angle). Site factors through Yukawa sub-operator (d_Y=4): L_seesaw_type_I [P] derives M_ν = −M_D M_R⁻¹ M_D^T from block diagonalization, confirming ... |
| · | `L_channel_crossing` | lemma | `P` | c_Hu/c_Hd = x^3 = 1/8. Propagation x^2 + Schur conjugation x. |
| · | `L_channel_disjoint` | lemma | `P` | SU(3) and EW admissibility channels are disjoint. 3-sector Gram matrix is block-diagonal: A = A_EW ⊕ A_color. Shared-bookkeeper scenario ruled out: w_U(1) < 0. Disjoint scenario: all fixed-point weights positive. det(A_EW ⊕ A_color) = 24. w_color* = 3/4 > 0. |
| · | `L_color_Gram` | lemma | `P` | cos(pi/2N)=sqrt(N)/2 iff N in {2,3}. Derives x=1/2 independently. |
| · | `L_conjugation` | lemma | `P` | All conjugation factors from [P] chains: L_color_Gram + L_channel_crossing. |
| · | `L_crossing_depletion_capacity_measure` | lemma | `P_structural_seam` | The up-G00 H-tilde crossing depletion factor (1 - c_Hu^2 * w2*) = 251/256 is EXACT, not leading-order. Measure-theoretic: depletion = c_Hu^2 * <Sigma\|Sigma> with <Sigma\|Sigma> = w2* a subspace MEASURE (real-valued, basis-independent), removing the integer-slot reinterpretation that held the resul... |
| · | `L_crossing_entropy` | lemma | `P` | At the α₃=α₂ crossing: 1/α_cross = (\|b₃\|+\|b₂\|)×ln(d_eff) = S_dS/6 = 47.0206. Each of B = C_total/6 = 10.1667 running modes resolves σ = ln(d_eff) = 4.6250 nats (the unique intensive entropy quantum per capacity channel). Fisher equilibrium at the balanced crossing forces per-mode resolution = σ. ... |
| · | `L_crossing_self_energy` | lemma | `P_structural_seam` | The depletion weight xi in the up-G00 H-tilde crossing self-energy is the SU(2)_L-sector equilibrium capacity w2* = 5/4 (T22: sector 2 = SU(2); T21b weak-mixing fixed point). The up-type Yukawa Q_bar_L H-tilde u_R contracts two SU(2) doublets, so the crossing runs through SU(2)_L; by the structur... |
| · | `L_delta_PMNS_confrontation` | lemma | `P` | APF: delta_PMNS = +3 to +11 deg (L_PMNS_CP_corrected [P]; robust \|delta\| < 15 deg). T2K+NOvA Oct 2025 (NO): best-fit -90 deg +- 40 deg; 3-sigma range [-248, +54] deg. APF inside 3-sigma; tension with best-fit: 2.4sigma. Boltzmann suppression at 90 deg: 3.6e-25. DUNE Phase I (~2033): 8.1sigma if d... |
| · | `L_dm2_hierarchy` | lemma | `P` | Δm²₂₁/\|Δm²₃₁\| = 0.0295 (exp 0.0295, err 0.03%). Closes L_nu_mass_gap: 3.4x → 1.0003x. M_R = diag(D) + s×D·D^T with D from L_seesaw_dimension, rank-1 in generation space (no generation label on the vacuum sector -- exchangeable-form re-anchor, check_L_singlet_Gram_exchangeable_form), s=4/15 from L... |
| · | `L_e3_gen0` | lemma | `P` | e3 = v_B × v_H = (1-x)(x⁴, 0, -x¹¹). Gen-1 component is EXACTLY zero (Fraction arithmetic). Gen-0 dominates by x⁻⁷ = 128. e3 ≈ (1,0,0) to accuracy 1 - x¹⁴ ≈ 1 - 6×10⁻⁵. Rank-lift adds mass specifically to lightest generation. |
| · | `L_edge_amplitude` | lemma | `P` | ALL sectors [P]. Near: L_color_Gram. Far: min(capacity, angular). Charged fermions: capacity x^(Q_2+color+conj). Neutrinos: angular sin^2*cos^2 = 0.2261 [L_angular_far_edge P, rank-1 projector]. |
| · | `L_gen_path` | lemma | `P` | Generations form total order under Q(g). Hasse diagram = path 1-2-3. Q = [2, 5, 9], diffs = [3, 4]. Telescoping: Q(3)-Q(1) = 7 = 3+4. Gen 1->3 factors through gen 2. Cech cocycle: coherence on edges implies coherence on path. |
| · | `L_holonomy_phase` | lemma | `P` | BRIDGE CLOSED (v4.3.2): interference = L_Gram overlap. Generation routing vectors n_g in S^2 compete for 3 adjoint channels. Gram overlap = sum_a (n_g.e_a)(n_h.e_a) = cos(theta_gh) (completeness of adjoint ONB, L_Gram_generation [P]). A1 minimizes sum\|cos(theta_gh)\| -> orthogonal (theta=pi/2). No... |
| · | `L_kB_sector` | lemma | `P` | k_B from SM Yukawa structure via L_channel_crossing [P]. T3_VEV = -1/2 (T_q_Higgs [P]). Up: T3=+1/2 mismatch -> H~ required -> conjugation step -> k_B=3. Down/lepton: T3=-1/2 match -> direct H -> no conjugation -> k_B=0. k_B=0 (flat) -> real texture -> no CP phase [L_NLO_texture P]. k_B=3 (curved... |
| · | `L_mass_from_capacity` | lemma | `P` | Two-channel mass matrix derived from A1 through 11-link chain. All links [P]. Capacity-derived matrix matches _build_two_channel output to <10⁻¹⁵. Hierarchy: m_t²/m_u² ~ inf. No Froggatt-Nielsen mechanism invoked. No flavon. No horizontal U(1). The "FN form" M~x^{q(g)+q(h)} is a theorem: additive... |
| · | `L_mass_mixing_indep` | lemma | `P` | Spectral theorem: masses from Gram eigenvalues, mixing from FN eigenvectors. |
| · | `L_mbb_prediction` | lemma | `P` | APF predicts m_ββ = 4.42 meV (0νββ effective mass). All contributions constructive: Majorana phases α₂₁ = α₃₁ = 0 (real seesaw matrices → same-sign eigenvalues). Absolute masses: m₁ = 1.09, m₂ = 8.68, m₃ = 50.12 meV (normal ordering). Σmᵢ = 59.9 meV. m_β = 8.86 meV. Single experimental input: Δm²... |
| · | `L_md_zero` | lemma | `P` | LO: rank-2 texture, m_d=2.79e-10 (zero). NLO: k_B(down)=0 [L_kB_sector P] -> eta_d=0 -> m_d=2.79e-10 (still zero). Rank-lift blocked: NLO non-separability requires k_B>0; k_B=0 gives zero. NNLO (Exit A): \|Q_g-Q_h\|^2 has cross term -2*Q_g*Q_h (non-separable regardless of k_B); NNLO CAN lift m_d. N... |
| · | `L_multiplicative_amplitude` | lemma | `P` | Additive realignment cost (L_cost_C2 [P]) + single-channel Gram overlap x = 1/2 (L_Gram + T27c [P]) → q-channel overlap = x^q (product rule for independent subsystems, T_Born [P]). Generation amplitudes: ψ(g) = x^q(g) = ['1/128', '1/16', '1']. Exponential suppression from INDEPENDENCE, not Boltzm... |
| · | `L_nu_mass_gap` | lemma | `P` | M_nu Gram ev=[0.1775,0.4883,1.4406]. Gram Dm^2_21/Dm^2_31=0.1012. Exp=0.0295. Gap=3.4x. Root cause: ratio anchored by a12, a23 (zero freedom). d_1 variation x^(7/4)->x^6: ratio shifts 0.0080 absolute (gap to exp unchanged). Fix: M_R2/M_R3~1.85. Open problem: derive from A1. |
| · | `L_null_direction` | lemma | `P` | For M₀ = \|v_B><v_B\| + \|v_H><v_H\| with v_B,v_H linearly independent: rank(M₀) = 2, ker(M₀) = span(v_B × v_H). rank(M₀ + c\|w><w\|) = 3 iff w·(v_B × v_H) ≠ 0. Pure linear algebra. Any NNLO rank-lift requires nonzero projection onto e3 = v_B × v_H. |
| · | `L_rank2_texture` | lemma | `P` | FN two-channel mass matrices M = alpha_1*a*b^T + alpha_2*c*c^T are sums of two rank-1 outer products -> rank <= 2. Verified: det(M_d) = 0 exactly (Fraction arithmetic), 2x2 minor nonzero -> rank = 2 exactly. m_u = m_d = 0 at leading FN order. |
| · | `L_rank_lift` | lemma | `P` | LO rank-2 texture gives m_u = 0 (L_rank2_texture [P]). NLO capacity-propagator (eta*\|Q_g-Q_h\|) is non-separable: cannot be written as f(g)+f(h). This breaks rank-2 -> rank-3, lifting m_u from zero. m_u/m_c: LO=0.0e+00 -> NLO=0.0080 (exp 0.0017, ratio 4.7x). Down sector unchanged (eta_d=0): m_d = ... |
| · | `L_rho_spacetime` | lemma | `P` | rho = x^d/d = (1/2)^4/4 = 1/64 = 0.015625. Derived from d=4 spacetime dimensions [T8, P] and FN scale x=1/2: x^d propagation amplitude divided by d independent channels. Dimensional limits: rho→x as d→1 (full amplitude), rho→0 as d→∞ (flat limit). d=4 is proved [T8]. Upgrades L_NNLO_down_mass to ... |
| · | `L_seesaw_dimension` | lemma | `P` | d_seesaw = (d_Y + d_W)/2 = 9/2. M_R hierarchy from A1 capacity averaging of seesaw propagator. M_R1/M_R3 = 2^(14/9) = 2.9395. M_R2/M_R3 = 2^(8/9) = 1.8517. Matches L_nu_mass_gap target ~1.85 to 0.1%. v5.3.5: seesaw de-imported; L_seesaw_type_I [P] derives M_ν = −M_D M_R⁻¹ M_D^T by block diagonali... |
| · | `L_seesaw_ordering` | lemma | `P` | The inverse-rank seesaw pairing m_i = ev_nu[i]/ev_MR[2-i] is uniquely forced by two independent arguments. ARGUMENT A (FN structure): q_B=(7,4,0) creates opposite gen-diagonal orderings in M_nu (gen-1 diagonal 0.297, smallest) and M_R (gen-1 diagonal 5.244, largest). M_nu eigenstate 0 is 69% gen-... |
| · | `L_texture_from_capacity` | lemma | `P` | 10-link chain derives the complete mass texture from A1. LO: rank-2 two-channel (m_lightest = 0). NLO: η = x^d/Q_max lifts m_u. NNLO: c = x^{2d} = 0.0039, θ = π/3, w = nearest-neighbor lifts m_d. Hierarchy: m_b²/m_d² ~ 1.2e+06. Zero Fritzsch imports. "Capacity rank-2 texture" not "Fritzsch texture." |
| · | `L_trace_equality` | lemma | `P` | Dynkin index sums per generation: S₃ = S₂ = 2. Derived from unique T_field content [P], not imposed. SU(3): Q(1) + u^c(1/2) + d^c(1/2) = 2. SU(2): Q(3/2) + L(1/2) = 2. Consequence: fermion contributions cancel in \|b₃\|-\|b₂\|, so the differential running rate is generation-independent. |
| · | `T19` | theorem | `P` | Hypercharge interface has M = 3 independent routing sectors (from fermion representation structure). Forces capacity C_EW >= M_EW and reinforces N_gen = 3. |
| · | `T20` | theorem | `P` | RG running reinterpreted as coarse-graining of the admissibility cost metric. Couplings = weights in the cost functional. Running = redistribution of capacity across scales. |
| · | `T21` | theorem | `P` | beta_i = -gamma_i w_i + lambda w_i sum_j a_ij w_j. Linear term: coarse-graining decay. Quadratic: non-closure competition (L_nc). All parameters resolved: a_ij (T22), gamma2/gamma1 (T27d), gamma1 = 1 (normalization), lambda_ (boundary condition). |
| · | `T21a` | theorem | `P` | p(s) = w(s)/W(s) satisfies non-autonomous share dynamics. Since w(s) ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â‚¬Å¾Ã‚Â¢ w* globally (T21b [P], analytic Lyapunov), p(s) ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â‚¬Å¾Ã‚Â¢ p*... |
| · | `T21b` | theorem | `P` | ANALYTIC PROOF: V(w) = ÃƒÆ’Ã†â€™Ãƒâ€¦Ã‚Â½ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â£(w_i - w_i* - w_i* ln(w_i/w_i*)) is Lyapunov function. dV/ds = (w-w*)ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚ÂµÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ A (w-w*) > 0 since A is symmetric positive definite (det=3, trace=17/4). w* = (3/8, 5/4) is glob... |
| · | `T21c` | theorem | `P` | Basin = entire positive orthant RÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â²ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã‚Â¡ÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â . T21b Lyapunov function V is global with unique minimum at w*. dV/ds > 0 (A sym pos def) excludes limit cycles. Therefore w* is the unique global att... |
| · | `T22` | theorem | `P` | Competition matrix a_ij from routing overlaps. Bare (x=0): a_11=1, a_22=3, a_12=0. Dressed (overlap x): a_11=1, a_22=x^2+3, a_12=x. m=3 from dim(su(2)). Transition: shared interface turns on a_12=x and adds x^2 cross-term to a_22. Matrix determinant = 3 (independent of x). |
| · | `T23` | theorem | `P` | r* = (g1*a22 - g2*a12)/(g2*a11 - g1*a21) = 3/10. sin2_W = r*/(1+r*) = 3/13. Verified with dressed matrix a=[[1,1/2],[1/2,13/4]], gamma=17/4. |
| · | `T24` | theorem | `P` | sin^2theta_W = 3/13 ~= 0.230769 -- THE VALUE CLAIM ONLY, [P]: exact rational arithmetic over T22/T23/T27c/T27d (x = 1/2, gamma2/gamma1 = 17/4, r* = 3/10), anchored on the placement close check_T_ew_load_placement_P (tier 4 [P], v24.3.247) -- named in dependencies and asserted LIVE in-body (the an... |
| · | `T25a` | theorem | `P` | Interface monogamy for m = 3 channels: x [1/3, 2/3]. From cutset argument: each sector contributes >= 1/m overlap. |
| · | `T25b` | theorem | `P` | Near-saturation (T4F: 75%) constrains overlap x toward symmetric value x = 1/2. If x deviates far from 1/2, one sector overflows while another underuses capacity. |
| · | `T26` | theorem | `P` | gamma_2/gamma_1 >= 3 (generator ratio floor). T27d derives exact value 17/4 = 4.25, within bounds (consistency verified). Bounds proved; exact value from T27d. |
| · | `T27c` | theorem | `P` | Overlap x = 1/2 from gauge redundancy argument. The two sectors (SU(2), U(1)) share the hypercharge interface symmetrically: each "sees" half the overlap capacity. |
| · | `T27d` | theorem | `P` | gamma_2/gamma_1 = 17/4, [P]: the value rests on the placement close check_T_ew_load_placement_P (tier 4 [P], v24.3.247) -- gamma_2 = a_22 + n_radial = 13/4 + 1 from the T22 Gram self-competition + the single radial Higgs record billed to SU(2) by FD1 structural completeness + Schur -- named in de... |
| · | `T4G` | theorem | `P` | Yukawa hierarchy = capacity ladder. Q(g)={0,5,9} gives eigenvalue span of 512x. T_mass_ratios [P] provides quantitative values. Supersedes qualitative exp(-E/T). v4.3.5 upgrade. |
| · | `T4G_Q31` | theorem | `P` | Neutrino hierarchy from dim-5 operator + d_1(nu)=x^{7/4} + normal ordering m1<m2<m3. nu_R=(1,1,0) gauge singlet has highest realignment cost. v4.3.5 upgrade. |
| · | `T6` | theorem | `P` | sin^2theta_W(M_U) = 3/8. IMPORT: uses SU(5) embedding (Tr(T_3^2)/Tr(Q^2) ratio). The SU(5) structure is external model input, not derived from A1. Framework contribution: capacity partition motivates unification-scale normalization. |
| · | `T6B` | theorem | `P` | Beta coefficients b_3=-7, b_2=-19/6, b_1=41/10 from T_field [P] + 1-loop formula derived by T6B_beta_one_loop [P] (Casimir arithmetic). v5.3.5: 1-loop beta formula de-imported. Comparison to PDG sin^2theta_W in validation.py. |
| · | `T_CKM` | theorem | `P` | Zero free params -> 6/6 CKM magnitudes within 5%. theta_12=13.50 (exp 13.04, +3.5%). theta_23=2.32 (exp 2.38, -2.6%). theta_13=0.209 (exp 0.201, +3.9%). \|Vus\|=0.2334 \|Vcb\|=0.0404 \|Vub\|=0.00364. J=3.33e-05 (exp 3.08e-5, +8.1%). v4.3.6: upgraded from [Ps] -- all bridge dependencies now [P]. SM: 4 f... |
| · | `T_LV` | theorem | `P` | Five invariances (simplex [A1], absorbing boundaries [L_epsilon*], locality [L_loc], sector-relabeling, minimality [A1]) uniquely determine F(x) = k*x(1-x)(x*-x). Factor form from I1+I2, oddness from I4, linearity from I5. Equivalent to 2-species competitive Lotka-Volterra by change of variables.... |
| · | `T_PMNS` | theorem | `P` | ALL 3 PMNS angles [P], zero free params, 0.11% mean error. theta_12=33.38 (0.08%), theta_23=48.89 (0.22%), theta_13=8.54 (0.04%). v4.3.4: All 6 M_nu entries from [P] axiom chains. Bridges closed: LL coherence, capacity/dim, rank-1 projector. Imports: seesaw (1977-79), Schur (1905). |
| · | `T_PMNS_CP` | theorem | `P` | k_B(lepton)=0 [L_kB_sector P]: W_e=L*e*H (T3 match, no H~ conjugation). Flat connection -> real Me [L_NLO_texture P]. M_nu real symmetric Gram [T_PMNS P]. Both UeL, UnuL real orthogonal. U_PMNS real: max\|Im\|=0.00e+00. J_PMNS=-0.00e+00=0 -> delta_CP=0. Root cause: H vs H~ (L_kB_sector), NOT colorl... |
| · | `T_S0` | theorem | `P` | S0 PROVED: Interface schema {C_ij, x} contains no A/B-distinguishing primitive. Label swap is gauge redundancy (verified computationally: sin^2theta_W = 3/13 invariant under full AB swap). Asymmetry enters through gamma (T27d, sector-level), not through x (interface-level). T27c and T_sin2theta u... |
| · | `T_capacity_ladder` | theorem | `P` | Q(g) = g*kappa + g(g-1)*eps/2 with kappa=2, eps=1. Q = [2, 5, 9]. q_B = Q(3)-Q(g) = [7, 4, 0]. Charges DERIVED from capacity budget (A1). Matrix form (M~x^{{q(g)+q(h)}}) derived from multiplicative cost principle (L_multiplicative_amplitude + L_Yukawa_bilinear [P]). Formerly labeled "FN charges";... |
| · | `T_load_form_selected_by_alpha_s` | theorem | `P_structural_exhaustive` | 3/13 alone does not separate the load-form readings of gamma_2, but the forward alpha_s(M_Z) prediction from the banked horizon counts (1/alpha_cross=47.02, 1/alpha_Y=61) plus the weak angle does: record-in (3/13) -> alpha_s=0.11790 (0.11 sigma); frozen-out (13/35) -> 0.0275 (77% off); two-record... |
| · | `T_mass_ratios` | theorem | `P` | 6 mass ratios, 0 params, ALL [P]. 4/6 <5%. Mean 9.1%. |
| · | `T_nu_ordering` | theorem | `P` | Normal ordering m1<m2<m3 from T_PMNS [P]. Gram eigenvalues: 0.17746, 0.48828, 1.44057. Splitting ratio: 0.246. |
| · | `T_q_Higgs` | theorem | `P` | q_H = q_B + h = (7, 5, 0). Step 1: Q_em = T3 + Y/2 = 0 forces T3(VEV) = -1/2 (down-type). Step 2: additive charges from multiplicative cost principle. Interior bump h=(0,1,0) from L_H_curv [P]. Cabibbo angle source: Dq_H(gen2) = 1. Down-type: direct coupling (c_Hd=1). Up-type: propagate + conjuga... |
| · | `T_sin2theta` | theorem | `P_structural_seam` | sin^2theta_W = 3/13 ~= 0.230769. Mechanism [P_structural] (T23 fixed-point). Parameters derived: x = 1/2 (T27c, gauge redundancy), gamma2/gamma1 = 17/4 (T27d, SU(2) load = self-competition + radial-Higgs record). Ledger share 3/13 is [P] (T_ew_load_placement_P, via FD1 structural completeness); m... |
| · | `T_sin2theta_higgs_record` | theorem | `P_structural_seam` | The electroweak load gamma = (1, 17/4) read as gamma_i = self-competition a_ii + the record sector i locks: gamma_1 = a_11 = 1 (U(1)_em massless, no record; photon theorem); gamma_2 = a_22 + n_radial = 13/4 + 1 = 17/4, the +1 being the one physical (radial) Higgs (n_radial = 4 - 3 = 1, T_Higgs [P... |

## `apf/spacetime.py` — 9 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `Delta_closure` | lemma | `P` | All Delta_geo components closed: Delta_ordering (causal order), Delta_fbc (boundary conditions), Delta_continuum (smooth manifold), Delta_signature (Lorentzian). A9.1-A9.5 all derived. Caveats: R2 event localization, L_nc for d>=5, external imports. |
| · | `Delta_continuum` | lemma | `P` | Kolmogorov extension -> sigma-additive continuum measure. FBC -> C^2 regularity. Chartability bridge: Lipschitz cost -> metric space, compactness + C^2 -> smooth atlas. M1 (manifold structure) DERIVED. Import: Kolmogorov extension theorem (1933). |
| · | `Delta_fbc` | lemma | `P` | Finite boundary conditions from 4-layer proof: Layer 1 (Lipschitz) from L_irr + A1 -> \|DeltaPhi\| <= C_max/N. Source bound from A1 + L_epsilon*. All layers independently proved with numerical verification. |
| · | `Delta_ordering` | lemma | `P` | L_irr (irreversibility) -> strict partial order on events. R1-R4 all fully formalized: R2 via 6-step proof, R3 via 7-step proof (delivers Kolmogorov consistency), R4 via total variation with 7 numerical checks. |
| · | `Delta_particle` | lemma | `P` | Particle structure within Delta_geo framework: V(Phi) forces SSB -> mass gap -> particle spectrum as quantum modes around admissibility well. No classical solitons. Follows from T_particle embedded in geometric framework. |
| · | `Delta_signature` | lemma | `P` | A4 -> causal order -> HKM (1976) -> conformal Lorentzian class -> Omega=1 (volume normalization) -> (-,+,+,+). HKM internalized: L_HKM_causal_geometry [P] (v5.3.5 de-import). Malament internalized: L_Malament_uniqueness [P] (v5.3.5 de-import). |
| · | `L_gr_dof_lovelock_witness` | lemma | `P_math` | check_T8's two external GR imports converted to a machine-verified node (the Maschke .391 pattern). DOF count d(d-3)/2 re-derived by two independent exact routes (little-group symmetric-traceless count; covariant gauge-fixing count) for d = 2..9 (d = 2 rides the formal polynomial identity), givin... |
| · | `T8` | theorem | `P` | d = 4 is the UNIQUE dimension satisfying: (D8.1) propagating DOF exist (d(d-3)/2 = 2), (D8.2) Lovelock uniqueness (only G_munu + Lambda*g_munu), (D8.3) hyperbolic propagation. d <= 3 excluded (0 DOF), d >= 5 excluded (higher Lovelock). IMPORTS: linearized GR DOF formula d(d-3)/2 and Lovelock clas... |
| · | `T_Coleman_Mandula` | theorem | `P` | All 5 Coleman-Mandula hypotheses derived [P]: (1) Lorentz invariance (Delta_signature + T9_grav), (2) Locality (L_loc + T_spin_statistics), (3) Mass gap (d²V = 4.0 > 0, T_particle), (4) Finite types (61 particles, T_field), (5) Nontrivial scattering (12 gauge generators). Theorem: G = Poincare(10... |

## `apf/gravity.py` — 16 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `A9_closure` | closure | `P` | The five geometric prerequisites A9.1..A9.5 are derived from APF axioms, dispersed across core.py, gravity.py, spacetime.py, and internalization_geo.py. This check unifies the closure: A9.1 (locality from A1+FBC), A9.2 (covariance from T7B), A9.3 (conservation from A1+L_loc), A9.4 (second-order f... |
| · | `L_Weinberg_Witten` | lemma | `P` | WW constraints derived from Lorentz rep theory (Delta_signature [P]): spin-1 J^μ → no Lorentz-cov charge for massless \|h\|>1/2; spin-2 T^μν → no local stress for massless \|h\|>1. Per-particle justifications all from [P]: Photon neutral (T_gauge), Maxwell T^μν exists → consistent. Gluon color J^{a,μ... |
| · | `L_global_interface_is_horizon` | lemma | `P` | Makes explicit the cross-module identification of T12 global interface (non-finite-interface stratum) with T_Bek dS horizon (unique area-bounded absorber). Both are the unique non-local absorber in V_{61} -- by T12 exhaustivity (no third option) + T_Bek uniqueness (dS horizon is the only finite-a... |
| · | `L_self_exclusion` | lemma | `P` | Self-correlation excluded from microstate counting. Two independent proofs: (A) eta(i,i) = 0 < eps (L_epsilon* + T_eta): zero-cost state is not a meaningful distinction. (B) T_M (monogamy): correlations need 2 distinct endpoints; self-correlation has 1. d_eff = (61-1) + 42 = 60 + 42 = 102 states ... |
| · | `T10` | theorem | `P` | Lambda*G = 3pi/102^61 = 10^-121.6. The cosmological constant problem resolved: Lambda/M_Pl^4 ~ 10^-122 from 102^61 horizon microstates. 102 = (61-1) + 42 from L_self_exclusion [P]. Absolute G_N requires one dimensional input (M_Pl or v_EW). v4.3.6: upgraded from [Ps] via T_deSitter_entropy. |
| · | `T7B` | theorem | `P` | When E_mix != 0, external feasibility requires a symmetric bilinear cost form. Polarization identity -> metric tensor g_munu. Non-degeneracy from A1 (capacity > 0). This is the minimal geometric representation of external load. |
| · | `T9_grav` | theorem | `P` | A9.1-A9.5 (admissibility conditions) + Lovelock theorem (1971) -> G_munu + Lambdag_munu = kappaT_munu uniquely in d = 4. External import: Lovelock theorem. Internal: all 5 conditions derived from admissibility structure. |
| · | `T_Bek` | theorem | `P` | Entropy bounded by boundary area: S(A) <= kappa * \|A\|. Volume scaling is inadmissible because correlations must pass through the boundary, which has admissibility physics. Verified on 3D lattice: area(600) < volume(1000). Bekenstein-Hawking S = A/4ell_P^2 is a special case with kappa = 1/4 in Pla... |
| · | `T_deSitter_entropy` | theorem | `P` | de Sitter entropy from capacity microstate counting. 61 types x 102 states/type = 102^61 microstates. d_eff = (61-1) + 42 = 102 (off-diagonal correlations + vacuum modes, self excluded). S = 61*ln(102) = 282.123 nats (obs 282.102, error 0.0075%). Predicted H0 = 66.8 km/s/Mpc (1.0 sigma from Planc... |
| · | `T_graviton` | theorem | `P` | Graviton derived from linearized Einstein equations (T9_grav). h_munu: 10 components - 4 gauge - 4 constraints = 2 physical DOF. Cross-check: d(d-3)/2 = 2 (T8). Spin 2 from rank-2 tensor. Helicities: [-2, 2]. Massless: gauge invariance (diffeo) forces m = 0 exactly (exp bound: m < 1.76e-23 eV). B... |
| · | `T_horizon_reciprocity` | theorem | `P` | 102 states = second-epsilon commitments: 60 partner channels (Sector A) + 42 vacuum modes (Sector B). Bulk: Sector A pairings obligatorily symmetric (T_kappa+L_irr); simultaneous configs = M(61,42) ~ 42^61 (ln ~ 228.0 nats). Horizon: reciprocity dissolves at timelike-separated crossings; each cro... |
| · | `T_interface_sector_bridge` | theorem | `P` | STRUCTURAL BRIDGE: T12 interface partition V_{61} = V_local (19) (+) V_global (42) governs second-epsilon sector structure. \|Sector A\| = 61-1 = 60 (bilateral reciprocal targets). \|Sector B\| = dim V_global = 42 (unilateral horizon-absorber targets). The two "42"s in T11 (Omega_Lambda = 42/61) and ... |
| · | `T_v_global_accumulation_from_type_II_resolutions` | theorem | `P_structural_reading` | Each staged Type II resolution deposits its kappa_int payment through the Interface-Sector Bridge into V_global. Cumulative loading over the full sequence of 61 slot resolutions equals dim V_global = Omega_Lambda . C_total = 42, saturating the global-vacuum capacity. Witness: per-slot V_global sh... |
| · | `T_vacuum_content_typing_status` | theorem | `—` | (no summary) |
| · | `T_vglobal_offdiagonal_blocks_scalar_typed` | theorem | `—` | (no summary) |
| · | `T_which_v_no_registered_interior_reader` | theorem | `—` | (no summary) |

## `apf/plec.py` — 10 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `Regime_R` | regime | `P` | On an admissible path class satisfying R1 (smooth), R2 (locally additive), R3 (connected), R4 (unsaturated), the PLEC selector exists: accumulated realignment cost K[q] = int L(q, qdot, t) dt is well-defined, bounded below on the admissible class, and attains a minimum. The Euler-Lagrange equatio... |
| · | `Regime_exit_Type_I` | regime | `P` | Saturation causes the admissible neighborhood to collapse. PLEC selection becomes trivially unique (the saturated configuration) but variational/geometric dynamics becomes empty. Maps to Paper 6 saturation exit and Paper 5 fully-locked measurement limit. Witness: 2-state class with budget C=1 and... |
| · | `Regime_exit_Type_II` | regime | `P` | Branching: the admissible class supports multiple inequivalent minimizers of the cost functional. Admissibility is intact; PLEC is ill-defined as a unique selector. The representation fails to compress realized evolution into a single variational trajectory. Witness: symmetric double-well L(x) = ... |
| · | `Regime_exit_Type_III` | regime | `P` | Regime exit by class transfer: the relevant admissible class itself changes. Canonical case is measurement (coherent class -> record-locked class). Witness: dim(M_sys) = 4, dim(M_sys tensor Z_R) = 8 with k=2 record symbols; the transition is irreversible by L_irr (no M_sys-local operation undoes ... |
| · | `Regime_exit_Type_IV` | regime | `P` | Regime exit by loss of regularity: admissibility is intact but the smoothness / local additivity / tangent-space / chartability assumptions required for variational or geometric representation fail. Canonical cases are singularities, Planck-scale discreteness, topology change. Witness: L(x) = 1/\|... |
| · | `Regime_exit_Type_V` | regime | `P` | Regime exit by descriptive redundancy: the admissible structure and realized minimizer are intact; only the descriptive coding is non-unique. Canonical cases are gauge freedom in Yang-Mills and coordinate ambiguity in GR. Witness: L(x, phi) = (1/2) x^2 with phi -> phi + alpha is cost-invariant al... |
| · | `T_cosmogenic_lattice_ordering` | theorem | `P_structural_reading` | Cosmogenic ordering is partially ordered by Phi_c-monotonic phase staging in the (61, 102) lattice. Any realized cosmic instance instantiates a specific total order on the partial order, fixed by the lattice energy-scale assignments. Theorem_R is a consolidation theorem (R1 ∧ R2 ∧ R3 jointly requ... |
| · | `T_omega_gamma_max_symmetry_group` | theorem | `P_structural_reading` | At the trivial alignment (a, empty), the maximal symmetry group of Omega_Gamma is G_max = S_61 x [SU(3) x SU(2) x U(1)]^(template-carrier-at-each-slot). The S_61 factor is the slot-permutation symmetry on the 61 capacity slots; the gauge template is the forced carrier per L_gauge_template_uniquen... |
| · | `T_trivial_alignment_is_Type_II` | theorem | `P_structural_reading` | The trivial alignment (a, empty) is a Type II configuration of the realignment-cost functional under any nontrivial symmetry group G acting on the admissible distinction-fillings. Admissibility holds (kappa(empty) = 0 <= C); the cost functional is well-defined (Lemma BW); the argmin over admissib... |
| · | `T_type_II_resolution_under_L_irr` | theorem | `P_structural_reading` | L_irr-accumulated record-locking adds an asymmetric correction to a symmetric Type II cost functional, breaking its symmetry group G to a proper subgroup H. Iterated L_irr accumulation collapses H to the trivial group, fully resolving the Type II degeneracy. Witness: symmetric double-well L_sym(x... |

## `apf/cosmology.py` — 21 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `L_DESI_response` | lemma | `P` | APF: (w₀, w_a) = (-1, 0) exactly. DESI DR2: w₀ = -0.75 ± 0.16, w_a = -0.99 ± 0.48. Tension: w₀ at 1.6σ, w_a at 2.1σ, combined Δχ² = 6.7. APF point (-1,0) is within 95% CL. Not excluded. Falsification requires Δχ² > 50 (≥5σ). If confirmed: L_saturation_partition, T11, L_anomaly_free face challenge. |
| · | `L_DH_primordial` | lemma | `P` | APF eta_B = 6.15e-10 -> D/H = 2.530e-05 (SBBN power-law, reference Planck+SBBN). Cooke 2018: (2.527e-05 +- 3.000e-07). Residual: +0.12%, 0.10sigma. Zero free parameters. Only empirical input: SBBN nuclear network. |
| · | `L_GW_matching` | lemma | `P` | First-order matching transition produces SGWB. α = 0.452 (strong), β/H* = 102 (rapid). T* = 6e+17 GeV. f_peak = 2.1e+12 Hz (THz — above all current detectors). Ω_GW h² = 1.5e-10. Genuine prediction but not testable with foreseeable technology. Secondary EW-scale transition (from σ scalar) may pro... |
| · | `L_N_eff_prediction` | lemma | `P` | N_eff = 3.044 from 3 light neutrinos (T4G [P]) + standard QED decoupling correction (+0.044). ν_R too heavy (M_R ≥ 31 GeV) to contribute. No BSM light species in capacity budget (C_total = 61). Planck: 2.99 ± 0.17 (0.3σ). CMB-S4 (σ ≈ 0.03): any N_eff > 3.1 excludes APF. Import: QED decoupling cor... |
| · | `L_bridges_closed` | lemma | `P` | All 5 interpretive bridges identified by the Option 3 Work Plan are now [P] theorems. Bridge A: L_cost (Cauchy uniqueness). Bridge B: L_equip (horizon equipartition). Bridge C: L_self_exclusion + L_equip + T_Bek. Bridge D: T_entropy + T11. Bridge E: T27c + L_Gram. The framework contains ZERO inte... |
| · | `L_common_demand_iff_degenerate` | lemma | `P_structural` | Under the .330 premise pair PLUS the NAMED/OPEN PSD (demand-realizability) premise: the exchangeable vacuum Gram G = (a-b)I + bJ is PSD <=> a+41b >= 0 and a-b >= 0, giving -a/41 <= b <= a -- so b <= a is a theorem under PSD and a = b is the extreme point of the PSD exchangeable cone. The squared-... |
| · | `L_dark_budget` | lemma | `P` | Singlet collective mode saturates s = 4/15 = 0.2667 of vacuum capacity. Collisionless at the rank-1 clause strength ([P_structural] over the exchangeable form + the OPEN a=b identity): σ/m = 0 (rank-1 Gram → no self-scattering channel). N_species = 1. ΔN_eff = 0. s = 4/15 enters M_R = diag(D) + s... |
| · | `L_equation_of_state` | lemma | `P` | The vacuum equation of state is w = -1 at all epochs. Post-matching: L_saturation_partition proves Omega_Lambda = 42/61 is s-independent (topological). T11 proves the vacuum sector is globally locked (non-redistributable). Constant Omega_Lambda with non-dilutable energy => w = -1. Pre-matching: p... |
| · | `L_equip` | lemma | `P` | At causal horizon, max-entropy (A4+T_entropy) distributes capacity surplus uniformly over C_total discrete units (L_ÃƒÆ’Ã†â€™Ãƒâ€¦Ã‚Â½ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âµ*). Uniform distribution preserves count fractions: ÃƒÆ’Ã†â€™Ãƒâ€¦Ã‚Â½ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â©_sector = \|sector\|/C_total exactly, independent of to... |
| · | `L_matching_transition` | lemma | `P` | The matching transition is first-order: anomaly cancellation requires all 61 types simultaneously (L_anomaly_free), so the matching snaps in discontinuously at s_crit = 1/d_eff = 1/102. Order parameter: Omega_Lambda jumps from 1 (pure vacuum) to 42/61 (partitioned). Delta(Omega_Lambda) = 19/61. L... |
| · | `L_nu_mass_confrontation` | lemma | `P` | APF Sigma-m_nu = 58.8 meV (NO, m_1=0; L_sum_mnu_cosmo [P]). DESI LCDM < 64.2 meV: margin = 5.4 meV = 0.30 sigma_future. IO min 108 meV > bound -> IO excluded (Bayes NO/IO=46.5). Euclid+DESI+CMB-S4 (~2030, sigma~18 meV): 3.3sigma detection or m_1>0 falsification. APF w=-1 [P]: LCDM bound self-cons... |
| · | `L_saturation_partition` | lemma | `P` | The capacity partition 3 + 16 + 42 = 61 is determined by discrete type-classification predicates (gauge-addressability, confinement) applied to the anomaly-free field content. These predicates are functions of TYPE LABELS, not of total capacity or saturation level. L_equip proves the density frac... |
| · | `L_singlet_Gram` | lemma | `P_structural` | The 42 vacuum (gauge-singlet) channels: G_singlet is S_42-exchangeable [P_structural]. rank(G) = 1 (single collective mode) holds iff the common-demand identity a = b, OPEN [C] (witness: check_L_singlet_Gram_exchangeable_form). At the banked point a = b = 1/61: eigenvalue = 42/61 = 0.6885, N_spec... |
| · | `L_singlet_Gram_exchangeable_form` | lemma | `P_structural` | Any label-functional vacuum demand Gram is S_42-exchangeable G = (a-b)I + bJ (P_exhaust zero-addressable-labels clause + two named premises, exported as artifacts), with exact spectrum {a+41b x1, a-b x41} and rank(G) = 1 <=> a = b != 0 -- verified by exact Q row-reduction at four witness points (... |
| · | `L_singularity_resolution` | lemma | `P` | No Big Bang singularity: A1 (finite capacity) + T_Bek (area bound) → S_min = ε* = 0.5 > 0 → S=0 state inadmissible. R_min = 0.3989 l_P, ρ_max = 0.7 M_Pl⁴ (finite). Initial state: k=1 de Sitter with Λ·G = 0.0924, R = 5.7 l_P. Strong energy condition violated (w=-1) → Penrose-Hawking inapplicable. ... |
| · | `L_sum_mnu_cosmo` | lemma | `P` | APF: Σmᵢ = 58.8 meV (normal ordering, m₁ ≈ 0). Planck: < 120 meV ✓. DESI DR2+CMB: < 72 meV (marginal). Future (2030): 2.9σ detection with σ = 20 meV. Saturates NO minimum; IO minimum = 107.4 meV (excluded by T_nu_ordering). |
| · | `T11` | theorem | `P` | Lambda from global capacity residual: correlations that are admissible + enforced + irreversible but not localizable. Non-redistributable load ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â‚¬Å¾Ã‚Â¢ uniform curvature (cosmological constant). Lambda > 0 from positi... |
| · | `T12` | theorem | `P` | DM from capacity stratification: gauge-singlet locally committed capacity. Gauge and gravity couple to different scope interfaces (T3 vs T9_grav), so C_local = C_gauge + C_singlet. C_singlet exists (N_matter_refs > dim(G_SM), H=(C²)^⊗61 includes singlet states). Gravitates [P], gauge-dark [P], lo... |
| · | `T12E` | theorem | `P` | f_b = 3/19 = 0.15789 (obs: 0.1571, error 0.51%). Omega_Lambda = 42/61 = 0.6885 (obs: 0.6889, 0.05%). Omega_m = 19/61 = 0.3115 (obs: 0.3111, 0.12%). Full capacity budget: 3 + 16 + 42 = 61. No free parameters. Bridge: L_equip proves ÃƒÆ’Ã†â€™Ãƒâ€¦Ã‚Â½ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â©_sector = \|sector\|/C_total a... |
| · | `T_config_demand_register_split_bank_respected` | theorem | `—` | (no summary) |
| · | `T_cosmogenic_to_recruitment_reduction` | theorem | `—` | (no summary) |

## `apf/validation.py` — 9 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `L_Sakharov` | lemma | `P` | All three Sakharov conditions derived from [P] theorems. (1) B-violation: P_exhaust partition not enforced before saturation -> baryonic routing is violable pre-saturation. (2) CP violation: L_holonomy_phase gives phi = pi/4, sin(2phi) = 1 (maximal). C violated by chiral SU(2)_L. (3) Non-equilibr... |
| · | `L_eta_B_Jarlskog` | lemma | `P` | Correction factor 7/6 = q_max/N_gen! = q_B[0]/3!. LO: 5.274e-10 (-13.8%). Corrected: 6.153e-10 (+0.54%). Obs: 6.120e-10. D/H improves from +23.3% to -3.7%. Both q_max=7 and N_gen!=6 are from [P] theorems. Same q_max controls NNLO c=x^3 (L_c_FN_gap [P]): unified bookkeeper charge structure across ... |
| · | `L_inflation_R2_spectral` | lemma | `P` | Spectral action [P] → R² gravity [math] → Starobinsky inflation [math]. n_s = 1-2/N_* = 0.9609 (0.9σ), r = 12/N_*² = 0.0042 (< 0.036). N_* = 53.4 from Liddle-Leach with A_s = 2.1e-09 (1 input). Discrete staircase smoothed: CMB averages 23 steps. Derivation chain: A1 → spectral triple → spectral a... |
| · | `L_no_BSM` | lemma | `P` | 6 BSM scenarios excluded: SUSY, axion, 4th gen, W'/Z', gravitino, magnetic monopoles. C_total = 61 exactly saturated by SM + 3ν_R. Anomaly cancellation forbids additional types. Strong CP solved without axion (T_theta_QCD). Gauge group derived without GUT (T_gauge). Each exclusion is independentl... |
| · | `L_prediction_catalog` | lemma | `P` | 49 quantitative predictions, 0 free parameters. 40 tested, 33/40 consistent (≤3σ). Mean error: 3.77%, median: 0.51%. 9 await future experiments (m_ββ, Σmᵢ, r, N_e). PLEC + IJC routing (Phase 19): zero free parameters; the four constitutive features (A1, MD, A2, BW) of admissibility space plus reg... |
| · | `T_baryogenesis` | theorem | `P` | UPGRADED [Ps]->[P] v5.0.3. eta_B = sin(2phi)*f_b / (d_eff^N_gen * S_dS) = (3/19) / (102^3 * 282.12) = 5.27e-10 (obs 6.12e-10, error 13.8%). Microcanonical counting: d^N routing configs for N=3 distinguishable generations (T_capacity_ladder [P]) in d=102 states, normalized by S_dS entropy (definit... |
| · | `T_concordance` | theorem | `P` | 12 cosmological observables, 0 free parameters. Mean error: 3.9%. 8/10 within 1%, 8/10 within 5%. Sectors: density fractions [P] (5 observables, all <1%), CC [P] (10^{-122.5} vs 10^{-122.4}), inflation [Ps] (n_s, r consistent), baryogenesis [Ps] (eta_B 13.8%), BBN [Ps] (Y_p, D/H from eta_B), rehe... |
| · | `T_inflation` | theorem | `P` | v5.0.5 HARDENED (N_* consistency + attack surface). Capacity fill drives N_e_max = 141.1 [P]. Lambda decreases by 10^123 from Planck to 10^-122. Liddle-Leach with A_s: N_* = 53.4 (T_rh-insensitive above 10^15). At N_*=53: n_s=0.9625 (0.6sigma). Coincidence: N_*=C-d=57 gives n_s=0.9649 (0.0sigma).... |
| · | `T_reheating` | theorem | `P` | UPGRADED [Ps]->[P] v5.0.3. Admissibility well curvature d2V = 4.00 -> omega = 2.00 (Planck units) [T_particle, P]. Gauge decay via T3 [P] with alpha = 1/40 [T6B, P]. T_rh ~ 5.5e+17 GeV (best estimate, P_structural). STRUCTURAL BOUND [P]: T_rh >> T_BBN with margin 10^21. BBN fails only for alpha <... |

## `apf/supplements.py` — 74 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `L_BH_page_curve_capacity` | lemma | `P` | Page curve derived from RT-capacity formula (L_RT_capacity [P]) applied to BH-radiation bipartition: S_rad(t) = min(C_rad(t), C_BH(t)) × s₁. C_BH + C_rad = C₀ (unitarity, T_CPTP [P]). Page time: τ_Page = 0.646 (Schwarzschild) when C_BH = C_rad. S_rad: 0 → S_max → 0 (rises, peaks, returns to zero)... |
| · | `L_CKM_phase_bracket` | lemma | `P` | Target 6 FULLY CLOSED: both criteria passed by NLO+NNLO. LO: delta=85.4° (13σ). V2 NLO: delta=61.8° (Criterion A met, Vus=-15.3% fails B). V1 NLO: delta=68.6° (between V1 and V2: experiment bracketed). NLO+NNLO: delta=66.0° (+0.6%, Criterion A) Vus=+1.2% (Criterion B). Three-effect mechanism (L_N... |
| · | `L_DPI_finite` | lemma | `P` | DPI: S(Φ(ρ)\|\|Φ(σ)) ≤ S(ρ\|\|σ) for any CPTP Φ. Verified: depolarizing channel reduces S from 0.1927 to 0.0910. Iterated 5× → monotonic decrease. Replaces Data Processing Inequality citation. |
| · | `L_Einstein_from_entanglement` | lemma | `P_structural_seam` | Linearized Einstein equations via the entanglement first law (Jacobson 1995 route). Named inputs T_Bek (area law), L_beta_temp (Unruh T), L_KMS (equilibrium), L_irr (second law) are [P]; the Raychaudhuri identity and the NEC (hardcoded test input) are imported continuum machinery, not A1-derived ... |
| · | `L_Fisher_measure` | lemma | `P` | d_eff = 102 IID capacity channels (T_deSitter_entropy [P]). Per-sample Gaussian entropy: h₁ = (n/2)ln(2πe) + (1/2) ln det G. d_eff IID samples: S = (d_eff/2) ln det G + const. Fisher metric eigenvalue = 102.0 = d_eff (exact). IID exponent 51.0 vs Stiefel exponent 49.0: diff = (n+1)/2 = 2 (3.9%). ... |
| · | `L_Gleason_finite` | lemma | `P` | Frame function axiom (non-negative, sums to 1 on every ONB) implies f(v) = v†ρv in dim ≥ 3. Constructive proof: ρ reconstructed from f on any ONB. Verified on d=4 with 10 random bases (all sums = 1 to 10⁻¹⁰). APF: dim = 2^61 >> 3. Replaces Gleason (1957) citation. |
| · | `L_KMS_trace_state` | lemma | `P` | Saturation state ρ = I/d_eff (L_equip [P]) is the trace state ω. H_mod = -log(ρ) = ln(102)·I (proportional to identity). Modular automorphism σ^ω_t = id (trivial). KMS at any β via trace cyclicity: Tr(AB)=Tr(BA) (algebraic identity). Physical T = ln(102)/ε* = 4.6250 (matches T_zeroth_law [P]). AP... |
| · | `L_MERA_generation` | lemma | `P` | 3-level FN hierarchy (q_B = [7, 4, 0]) maps to 3-level MERA. Scale factors: W₀₁ ~ x^3 = 0.125, W₁₂ ~ x^4 = 0.0625. Isometry condition W†W=1 verified at both levels. Additivity: Δq₀₁ + Δq₁₂ = 3+4 = 7 = q_max. Disentangler U = e^{iφ(g-h)} unitary (φ=π/4, L_holonomy [P]). Bond dim = κ = 2 (T_kappa [... |
| · | `L_NCG_status` | lemma | `P` | 11 NCG items (3 components + 7 axioms + 1 principle) all [P]-derived or verified. 3 mathematical tools (heat kernel, rep theory, KO classification) with same status as Lie algebra classification. 0 physics imports. Spectral action from A1 (invariance + additivity + finiteness). Long-term open: de... |
| · | `L_Noether_finite` | lemma | `P` | Finite-dim Noether: [G,H]=0 ⟺ d⟨G⟩/dt=0. Verified constructively on d=3 witness. 26 APF conservation laws follow from commutation. Replaces Noether (1918) continuum citation. |
| · | `L_P3_interface` | lemma | `P` | Contract: P3 must dag_put("ln_Mcross_over_MZ", value, source="L_epsilon_star_Planck") to close P1. Experimental reference: ln(M_cross/M_Z) = 34.591032 nats. Decomposition: -4.844746 + 39.435778 = 34.591032. P3 status: PARTIAL — combined key present, sub-keys not yet stored. |
| · | `L_QEC_code_space` | lemma | `P` | H_phys = (ℂ^102)^⊗61: log₂(dim) = 407.0 bits. Code state ρ = ⊗_i (I_102/102): unique max-entropy state at Bekenstein saturation (T_deSitter_entropy [P]). S_code = S_dS = 282.1233 nats. Logical algebra = ⊗_i B(ℂ^102): full per-type operator algebra. Block structure: 42 vacuum types (Ω_Λ=42/61) + 1... |
| · | `L_QEC_distance` | lemma | `P` | Two-sector code distance from T11 [P] block structure. Vacuum (globally locked, 42 types): d_vac = C_total = 61. All 60 proper subregions have S < S_dS = 282.12: vacuum inaccessible from any proper boundary subregion. Matter (locally attributable, 19 types): d_mat_full = 19. Information-theoretic... |
| · | `L_QEC_knill_laflamme` | lemma | `P` | Verified all 81 KL conditions for d=3 representative: Tr(ρ E_ab†E_cd) = (1/3)δ_ac·δ_bd (0 violations). C matrix = (1/3)·I_{d²}: non-degenerate code. Same algebra holds exactly for d_eff=102 (same proof, larger d). Interpretation: ρ=I/d_eff is the unique maximally mixed code state such that any no... |
| · | `L_QEC_product_structure` | lemma | `P` | J_ij=0 (L_TN_product_state [P]) → ρ_code = ⊗_i (I_102/102). Verified on 2-type d=3 representative: I(1:2)=0.00e+00=0; marginals exact; [E_1,E_2]=0 (Frobenius=0.0e+00); KL factorizes: Tr(ρ_12 E†E) = Tr(ρ_1 E_1†E_1)·Tr(ρ_2 E_2†E_2). Reduces 61-type problem to 61 independent single-type problems. QE... |
| · | `L_QEC_wedge_duality` | lemma | `P` | Full k-sweep: S(k)+S(61-k)=S_dS for all k∈{0..61} (product additivity). Matter wedge: wedge(A) contains exactly the matter types in A. Vacuum: NOT in wedge(A) for any k<61 (global locking, T11 [P]). Key duality: S(matter block)/S_dS=0.3115=Ω_m=19/61; S(vacuum block)/S_dS=0.6885=Ω_Λ=42/61. Vacuum ... |
| · | `L_QG_UV_finiteness` | lemma | `P` | Quantum gravity is UV-finite to ALL loop orders. Z = (1+e^{βε*})^61 (exact, closed-form). dim(H) = 2^61 (finite Hilbert space). \|\|H\|\| = 61ε* (bounded Hamiltonian). Any n-loop amplitude bounded by κ^2n × 2^61 × 61^L (finite). 2-loop: finite in APF (vs Goroff-Sagnotti divergence in continuum GR). N... |
| · | `L_QG_consistency` | lemma | `P` | 10/10 consistency checks passed across three routes to gravity: (1) Geometric: L_lovelock → G_μν unique in d=4. (2) Thermodynamic: δQ=TdS → same G_μν from entanglement. (3) Quantum: CPTP dynamics + capacity excitations → graviton. Key identifications: DOF=2=κ in all three; G_N=l_P²/(4ln2) unique;... |
| · | `L_RG_lambda` | lemma | `P` | SUPERSEDED by L_Higgs_corrected (123 GeV, 1.6% error). CCM initial condition lambda(M_GUT) = g_2^2/2 = 0.1360. APF d/c^2 = 0.33311 confirms this to 0.07% (L_SA_sector_dominance [P]). 1-loop SM RG (import: T6B beta coefficients): lambda(M_GUT) -> lambda(M_Z) = 0.1832. Prediction: m_H = 149.1 GeV. ... |
| · | `L_RT_capacity` | lemma | `P` | S(A) = k·ln(102) = (k/61)·S_dS for k types in A — the MARGINAL entropy of the maximally-mixed saturation state ρ = I/d_eff^61 (L_equip [P], L_KMS_trace_state [P]). The maximally-mixed state factorizes (I/d^n = ⊗ I/d) → zero mutual info → partial trace gives a k-type trace state → S = k·S_1 [P]. T... |
| · | `L_RT_two_sided_reading_no_go` | lemma | `—` | (no summary) |
| · | `L_SA_Higgs` | lemma | `P` | SUPERSEDED by L_Higgs_corrected (123 GeV, 1.6% error). Physical Yukawa d/c^2 = 0.333106 vs 1/N_c = 0.333333, err = -0.0227%. APF confirms CCM (2007): top-dominated d/c^2 -> 1/3 to 0.07%. CCM spectral action formula: m_H = sqrt(8/3)*m_t = 282.7 GeV (GUT-scale). APF correction factor = 0.999659 -> ... |
| · | `L_SA_moments` | lemma | `P` | Physical Yukawa spectral action coefficients from APF D_F (L_ST_Dirac [P]). Normalization: Y_s = lambda_s * M_s^APF where lambda_s = y_s^heaviest/sv_s[0]. APF structural ratio sv_d/sv_u = 1.8871 (derived: M_d[2,2]/M_u[2,2] = 2/1.125). c = 2.630437, d = 2.304827, N_f = 48. Top dominates c at 99.97... |
| · | `L_SA_sector_dominance` | lemma | `P` | Within each fermion sector, d_s/c_s^2 = 1/N_c to precision eps^2. Up: err=7.77e-08 (eps^2_u=1.17e-07). Down: err=3.95e-08 (eps^2_d=5.90e-08). nu: exact 1/1 (rank-1). lepton: err~1e-5. Result is SCALE-INVARIANT: identical in APF internal units and physical Yukawa units. Analytic: d_s/c_s^2 = (1/N_... |
| · | `L_ST_Dirac` | lemma | `P` | D_F = [[0,M_Y†],[M_Y,0]] with M_Y from [P] theorems. M_u: L_NLO_texture [P]. M_d: L_NNLO_down_mass [P]. M_ν: T_PMNS [P]. M_e = M_d: L_kB_sector [P]. All 7 Connes axioms verified: (i) D†=D, (ii) real spectrum, (iii) compact resolvent (finite-dim), (iv) \|\|[D,π(a)]\|\|<∞, (v) γD+Dγ=0, (vi) J²=-I (KO-d... |
| · | `L_ST_Hilbert` | lemma | `P` | H_F = C^45 ⊕ C^45 = C^90. Particle: 15 Weyl/gen × 3 gen = 45. Antiparticle: 45 (CPT, T_CPT [P]). Block: quarks 72 + leptons 18 = 90. Generation subspace for D_F: 4×2×3 = 24-dim. Vs Connes (96): APF is minimal (no ν_R from T_field). Inner product: L² from GNS (L_T2 [P]). |
| · | `L_ST_algebra` | lemma | `P` | A_F = C ⊕ M_2(C) ⊕ M_3(C) from T_gauge [P] (unique SM gauge group). dim(A_F) = 1+4+9 = 14. C: U(1) algebra on C^1. M_2(C): SU(2) generators + center. M_3(C): 8 Gell-Mann generators. *-algebra: (AB)*=B*A* verified. Z(M_2)=C·I_2 picks out U(1) direction. Note: Connes uses A_F=C⊕H⊕M_3(C) with H⊂M_2(... |
| · | `L_ST_index` | lemma | `P` | Index(D_F) = 0 for all four sectors (u,d,ν,e). Three independent proofs: (a) rank: M_Y square (3×3) → ker(M)=ker(M†) → Index=0. (b) McKean-Singer: Tr_s[exp(-tD²)]=Tr[exp(-tM†M)]-Tr[exp(-tMM†)]=0 at t=0.001,0.01,0.1,1.0 (all < 1e-10). (c) Anomaly: [U(1)]^3=∑Y³=0 (L_anomaly_free [P]). CPT chain: T_... |
| · | `L_TN_Hamiltonian` | lemma | `P` | H = -ε* Σ n_i (uniform, J_ij=0) on C_total=61 binary sites. Ground state E_0 = -61ε* (full matching). Uniformity from L_equip: cost additive per type, no cross-coupling. Physical sector: unique by 7 anomaly conditions (L_anomaly_free). Key insight: APF complexity is in the constraint surface (pol... |
| · | `L_TN_anomaly_protection` | lemma | `P` | Physical TN sector = unique full matching (1/4680 templates). Ground state protected by 7 anomaly conditions. Energy gap: ε* per type, but gap is categorical (all N<61 anomalous). Block structure: vacuum 42 (Ω_Λ=0.6885) + matter 19 (Ω_m=0.3115). Observed: Ω_Λ=0.6889 (err 0.05%), Ω_m=0.3111 (err 0... |
| · | `L_TN_product_state` | lemma | `P` | Z(β) = (1+e^{βε*})^61 (exact factorization from J_ij=0). TN: D_phys=2, D_bond=1 (product state). Config space: 2^61 = 10^18.4. Physical sector: 1 state (full matching, D_bond=1 exact). Zero mutual information: I(i;j)=0 between all type pairs. MERA refinement: 3 levels at scales x^3=0.125, x^4=0.0... |
| · | `L_Tomita_finite` | lemma | `P` | Constructive proof of modular automorphism + KMS condition for finite-dim algebras. Uses only matrix exp/log and cyclic trace. Replaces external citation of Tomita-Takesaki (1967-70). Verified numerically for n=4: KMS condition to 10⁻¹⁰, automorphism homomorphism to 10⁻¹⁰, *-preservation to 10⁻¹⁰... |
| · | `L_Wedderburn_constructive` | lemma | `P` | Constructive Wedderburn decomposition for finite C*-algebras. Center Z(M_n) = C·I verified. Simplicity proved via E_{ij}AE_{kl} extraction. Tensor product M_2^⊗3 ≅ M_8 verified. APF algebra M_2^⊗61 is simple (k=1). Replaces external citation of Wedderburn (1907). No import. |
| · | `L_Z_gauge_lattice` | lemma | `P` | Z_gauge = ∫∏dU exp(-S_Wilson) is the Wilson lattice gauge theory for G = SU(3)×SU(2)×U(1) on a lattice of capacity loci. FINITE by 3 proofs: (1) compact group → vol(G) < ∞, (2) bounded action, (3) character expansion convergence. Lattice coupling: β₃ = 22.5, β₂ = 15.0 at Planck scale (from L_cros... |
| · | `L_algebra_type` | lemma | `P` | Finite: 𝒜_APF = ⊗_{61} M_{102}(ℂ) ≅ M_{102^61}(ℂ), type I. (Wedderburn: every finite-dim C*-algebra = ⊕_i M_{n_i}(ℂ), type I.) Thermodynamic limit (β>0, n→∞): type III_λ Powers factor R_λ, λ = e^{-βε*} = 0.805560. β→0 saturation limit: λ→1 → type III₁. Paper's "type III₁" claim: accurate for the ... |
| · | `L_alpha_em` | lemma | `P` | α_em(M_Z) derived from: sin²θ_W=3/13 [T_sin2theta] + 1/α_cross=S_dS/6 [L_crossing_entropy, P] + \|b₂\|/\|b₃\|=C_mat/C_vac [L_beta_capacity] + one experimental input: α_s(M_Z)=0.1179. Result: 1/α_em(M_Z) = 128.2075 (experiment 127.930, error 0.22%). Key step: M_cross cancels when taking ratio of beta ... |
| · | `L_alpha_s_route_A_zero_input` | lemma | `P` | INPUT SWAP: α_s replaced by α_EM as framework input — ZERO new experimental inputs. α_EM = 1/127.951 already in framework (L_alpha_em). Formula: 1/α_s = (-23/19)×(1/α_cross) + (42/19)×(sin²θ_W/α_EM). 1/α_cross = 47.0206 [L_crossing_entropy, P]. sin²θ_W = 3/13 [T_sin2theta, P]. Result: α_s(M_Z) = ... |
| · | `L_alpha_s_zero_input` | lemma | `P` | MODE: FULL_DERIVATION (zero inputs). Formula: 1/α_s = 1/α_cross − (b₃/2π)×ln(M_cross/M_Z) = 47.0206 − 1.1141×34.5923 = 8.4818. α_s(M_Z) = 0.117900 (exp: 0.1179, err: 0.0001%). Inputs consumed: ['none — zero experimental inputs']. Upgrades to [P] automatically when dag_put("ln_Mcross_over_MZ", ...... |
| · | `L_anomaly_index` | lemma | `P` | 7 anomaly conditions (L_anomaly_free [P]) = vanishing of Atiyah-Singer Dirac index on SM gauge bundle. [U(1)]^3: ∑Y_f^3 = 0 ✓ (index of hypercharge Dirac op). [grav]^2 U(1): ∑Y_f = 0 ✓ (index of gravitational anomaly op). [SU(3)]^3: d^{abc}A(R) = 0 ✓. [SU(2)]^3: d^{abc}=0 automatic (SU(2) no cubi... |
| · | `L_beta_temp` | lemma | `P` | beta(Gamma) = ln(d)/epsilon is well-defined and positive for any interface with d > 1. Derived from T_entropy [P] (S=C*ln(d)) and T_epsilon [P] (DeltaE=epsilon). Finite-difference formulation is exact for discrete capacity. Cosmological: beta_univ = ln(102) = 4.6250, T_univ = 1/ln(102) = 0.2162 (... |
| · | `L_cluster` | lemma | `P` | Distant experiments are independent: correlations decay exponentially with separation. Three ingredients: (1) Locality (L_loc → microcausality), (2) Mass gap (d²V = 4.0 > 0, T_particle [P]), (3) Unique vacuum (M_Omega). Spectral bound DERIVED: G_c(r) = ∫ρ(μ)e^{-μr}dμ; since e^{-μr} ≤ e^{-mr} for ... |
| · | `L_coupling_capacity_id` | lemma | `P` | At the gauge crossing (α₃=α₂), each of B = C_total/6 running modes resolves σ = ln(102) = 4.6250 nats per interaction. Therefore 1/α_cross = B×σ = 47.0206. Proof: (1) 1/α = resolved information [T20]; (2) B modes from capacity ledger [L_beta_capacity]; (3) balanced sectors at crossing [L_Fisher_g... |
| · | `L_crossing_capacity` | lemma | `P` | B×σ = S_dS/6 = 47.0206: exact algebra from L_beta_capacity + L_sigma_intensive. B=C_total/6=61/6, σ=ln(102)=4.6250 nats. Combined with L_coupling_capacity_id [P]: 1/α_cross = B×σ is now fully derived. |
| · | `L_epsilon_star_Planck` | lemma | `P` | PART I — ε* = l_P: unique self-consistent ID from T_Bek + T10 + L_epsilon*. ln(S_Bek) = 61·ln(102) = 282.123 = S_APF. Area per capacity unit = 4.0 l_P² (κ=1/4). PART II (NEW v5.3.6) — ln(M_cross/M_Z) = (2π/b₂)×(1/α_cross − sin²θ_W/α_EM). = 34.592330 nats (exp 34.591032, err 0.0038%). Downstream α... |
| · | `L_equivalence_principle` | lemma | `P` | Equivalence principle is a THEOREM: all 61 types couple to gravity with same κ = √(32πG_N) = 6.0215. From L_equip (uniform cost ε*) + L_lovelock (single metric). Eötvös ratio η = 0 exactly (exp < 10⁻¹⁵). Nordtvedt η_N = 0 (strong EP, exp < 4.4×10⁻⁴). Graviton-matter vertex: V = -(κ/2)T^μν, same κ... |
| · | `L_full_quantum_theory` | lemma | `P` | Z_total = Z_local^N × Z_gauge × Z_matter. Z_local = (1+e^βε*)^61 (exact). Z_gauge = Wilson lattice (compact → finite). Z_matter = lattice fermions + Higgs (finite det + bounded V). N = A/61 (Bekenstein → finite). Gravity: NOT path-integrated. Metric derived from loci. Sum over capacity configs = ... |
| · | `L_graviton_capacity_excitation` | lemma | `P` | Graviton = capacity excitation above saturated ground state. Ground: \|1...1⟩ (de Sitter, E = -61ε*). Excitation: uncommit 1 type → ΔE = +ε*, degeneracy = 61. DOF: 10 - 4(gauge) - 4(constraint) = 2 TT modes (= κ). Massless: ω = \|k\| (gauge invariance, T_graviton). Propagator: G(k) = P₂/k² → V(r) = ... |
| · | `L_graviton_self_interaction` | lemma | `P` | Graviton 3-point vertex uniquely determined by action uniqueness (L_lovelock_internal) + gauge invariance + masslessness. 6 tensor structures in de Donder gauge, 2 independent helicity amplitudes. κ = √(32πG_N) = 6.0215 (dimensionful → non-renorm, but UV finite via C_total = 61 cutoff). 4-gravito... |
| · | `L_mc_mt_twoloop_RG` | lemma | `—` | (no summary) |
| · | `L_metric_from_entanglement_data` | lemma | `P` | Full Lorentzian metric g_μν(x) uniquely reconstructed from: conformal class [g] (from causal order, L_HKM [P]) + conformal factor Ω² (from entanglement, L_RT_capacity [P]). In d=4: Area ∝ Ω² → knowing S(A) for all A determines Ω²(x). Verified: flat space (Ω=1) and de Sitter (Ω=e^{Ht}). Uniqueness... |
| · | `L_mu_mc_unified` | lemma | `—` | (no summary) |
| · | `L_naturalness` | lemma | `P` | The hierarchy m_H/M_Pl ~ 10^{-17} is derived, not fine-tuned. T_Bek: DOF scale with AREA, not volume -> quadratic divergence is an artifact of volume-scaling assumption. Capacity: 102^61 ~ 10^123 total DOF (finite). Radiative correction: only logarithmic survives. delta(m_H^2)/m_H^2 ~ 0.2 (O(1), ... |
| · | `L_primordial_spectrum` | lemma | `P` | P(k) = A_s(k/k*)^{n_s-1}, n_s = 0.9625, r = 0.0042, n_T = -0.00053. 1 input (A_s). n_s tension: 0.6σ. r << 0.036 (BICEP). Consistency: r = -8n_T (exact). Capacity interpretation: fluctuations δn/n from binomial commitment statistics; red tilt from capacity depletion. |
| · | `L_quantum_evolution` | lemma | `P` | Complete quantum dynamics from capacity commitment: H = ⊗₆₁ C² (dim 2^61), evolution by 61 CPTP commitment steps. Path integral = (1/61!) sum over S_61 orderings. ALL orderings give same final state \|1...1⟩ (deterministic endpoint). Intermediate states are MIXED: S(k) = ln C(61,k), maximum S_max ... |
| · | `L_sigma_intensive` | lemma | `P` | σ = S_dS/C_total = ln(102) = 4.624973 nats. From T_deSitter_entropy [P]: S_dS = 61×ln(102). All 61 types share d_eff=102 microstates → uniform σ. |
| · | `L_spacetime_emergence` | lemma | `P` | COMPLETE spacetime emergence from A1 alone: 5 independent chains derive: (1) topology (smooth 4-manifold), (2) dimension (d=4 from DOF), (3) signature (Lorentzian from L_irr), (4) full metric (conformal class + factor), (5) spatial extent (N = A/61 from holographic bound). 5/5 cross-consistency c... |
| · | `L_spacetime_emergence_v2` | lemma | `P` | 4D Lorentzian spacetime from A1 via 4 mechanisms: (1) Capacity overflow → multiple loci (L_loc). (2) Realignment cost → metric + smooth manifold (L_cost → L_chartability). (3) Causal order → full g_μν (L_HKM + L_Malament, 10/10 components). (4) Gauge connection → spatial dynamics + correlations (... |
| · | `L_spatial_factorization` | lemma | `P` | Spatial factorization H = ⊗_x H_x derived (not assumed). MERA layers give coarse-graining; branching factor 2^3=8 in 3D. At Bekenstein saturation: N_sites = 1 (Hubble patch = 1 site). Sub-saturation: N_sites = A/61 (holographic area law). Holographic check: S = N × C × s₁ = A/(4G_N) (exact). dim(... |
| · | `L_spatial_from_cost` | lemma | `P` | Spatial structure DERIVED from realignment cost (not entanglement). (A) Multiple points from capacity overflow (L_loc): one interface holds ≤ 61 distinctions, universe needs more → multiple loci. (B) Distance from cost metric (L_cost): C = dim·ε satisfies metric axioms. (C) Topology from sheaf st... |
| · | `L_spectral_action_coefficients` | lemma | `P` | Spectral action Tr[e^{-tD²}] = N_f - tc + (t²/2)d + O(t³) verified. c = 21.984950, d = 87.201141, d/c² = 0.180414. N_f = 48 fermion d.o.f. SECTOR IDENTITY: d_i/c_i² = 1/N_color(i) to < 10⁻⁵ rel. error for all 4 sectors (up,down,neutrino,lepton). Mechanism: FN hierarchy → σ₁ >> σ₂ → sector dominan... |
| · | `L_upGram_PSD_saturation` | lemma | `—` | (no summary) |
| · | `L_upGram_schur_margin` | lemma | `—` | (no summary) |
| · | `RT_QG_corruption` | red_team | `RED_TEAM` | 6 corruptions tested (C=60, C=100, κ=3, d=5, d=3, C=19). All break ≥ 1 QG check. Far corruptions break ≥ 3. Average 3.7 breaks per corruption. Reference (C=61, κ=2, d=4): 10/10 pass. QG web is LOAD-BEARING and cross-linked, not parallel. Corruptions: {'C=60': 2, 'C=100': 4, 'κ=3': 4, 'd=5': 3, 'd... |
| · | `T_BH_information` | theorem | `P` | No information paradox: (1) T_Bek: info bounded by area (finite, at boundary). (2) T_CPTP: total evolution unitary (info never lost). (3) L_irr: capacity commitment irreversible (transferred to radiation, not destroyed). Page curve verified on 20-qubit model: S_rad rises to max at k=10 (Page time... |
| · | `T_CPT` | theorem | `P` | CPT is exact: derived directly from framework [P]. Step 4a: Jacobian(-1)^4=+1 (d=4). Step 4b: ∫L(x)d⁴x = ∫L(-x)d⁴x (L is Lorentz scalar, T9_grav + T_gauge [P]); verified for m²φ², (∂φ)², F², V. Step 4c: η_J=(-1)^{2J} (L_Pauli_Jordan [P]) → \|η\|²=1 → bilinears invariant. Step 4d: H preserved (\|Jaco... |
| · | `T_Noether` | theorem | `P` | Noether correspondence verified for all framework symmetries. 10 Poincaré (energy, momentum, angular momentum) + 12 gauge (color, weak isospin, hypercharge, Q_em) + 4 accidental (B, L_e, L_mu, L_tau) = 26 conservation laws. All symmetries derived [P] (T9_grav, T_gauge, T_proton, T_field). Noether... |
| · | `T_decoherence` | theorem | `P` | Decoherence from L_irr + T_CPTP + L_loc. When system S interacts with environment E, off-diagonal elements of rho_S decay exponentially: \|<E_0\|E_1>\| -> 0 as E records which-state info. Pointer basis selected by L_loc (interface structure). Born rule (T_Born) gives outcome probabilities. CNOT witn... |
| · | `T_first_law` | theorem | `P` | dE = dQ + dW: dQ = T*dS (heat, irreversible, L_irr [P]), dW = dE - T*dS (work, reversible). Verified: pure heat (dW=0), pure work (dQ=0), mixed. Second-law consistent: heat hot->cold increases total S. Cosmological: all 61 type commitments are pure heat, dW_total=0. First law is an accounting ide... |
| · | `T_interface_modular_period` | theorem | `P` | The off-saturation interface Gibbs state has a type III_lambda modular flow (L_algebra_type, L_Tomita_finite) whose primitive period is a new, finite-exact invariant the bank did not record: T0 = 2pi/\|ln lambda\| = 2pi/(beta eps*) = 29.0596, lambda = e^(-beta eps*) = 0.805560. Verified sigma_(T0)=... |
| · | `T_number_u1_is_interface_modular_flow` | theorem | `P` | On the off-saturation interface the number-phase U(1) alpha_theta = Ad(e^{i theta N}) coincides per-site exactly with the modular flow sigma_{theta/(beta eps*)} (one U(1) turn = one modular period T0 = 29.0596); verified to 1e-9 at N=1,2,3 with KMS-invariance, GNS implementation U_theta Omega=Ome... |
| · | `T_optical` | theorem | `P` | S-matrix is unitary (S†S = I) from T_CPTP. Optical theorem: sigma_total = (1/p)*Im[M_forward]. Verified on 2-channel model with mixing: delta1=0.785, delta2=0.524, theta_mix=0.449. Optical theorem LHS=1.811745 = RHS=1.811745. Probability conservation: sum \|S_{fi}\|^2 = 1 for all i. Physical conten... |
| · | `T_second_law` | theorem | `P` | Three levels, all [P]. (A) Subsystem: CPTP evolution (T_CPTP) never decreases entropy (T_entropy) for unital channels; data processing inequality. Verified on 4 test states x depolarizing channel. (B) Cosmological: S(k) = k*ln(102) strictly increasing (k: 0->61); L_irr makes k non-decreasing in t... |
| · | `T_spin_statistics` | theorem | `P` | Part A: d_space = 3 (T8) -> pi_1(config space) = S_n -> only Bose (kappa=+1) and Fermi (kappa=-1). No anyons (d >= 3), no parastatistics (DR/T3 absorbs into gauge group). Part B: Lorentzian signature (Delta_signature) -> SO(3,1) -> spin J. Microcausality (L_loc + L_irr) forces kappa = e^{2pi*i*J}... |
| · | `T_zeroth_law` | theorem | `P` | Temperature T = epsilon/ln(d) equalizes at equilibrium. Flow direction: capacity flows to higher beta (L_irr [P]). Equalization: flow stops at beta_1 = beta_2. Zeroth law: transitivity of equality (logical). Cosmological: T_univ = epsilon/ln(102) = 0.2162*epsilon; all 61 types thermalized at Beke... |

## `apf/majorana.py` — 10 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `L_Higgs_2loop` | lemma | `P` | CANONICAL APF HIGGS PREDICTION (v5.3.5). m_H = 124.9 GeV at 2-loop SM RG (obs 125.09). Error budget: σ_scale=0.22 GeV (M_GUT range), σ_loop=0.40 GeV (3-loop est., loop ratio 0.220), σ_theory=0.46 GeV → pull=0.324σ (NO tension). 1-loop baseline: 123.1 GeV; 2-loop shift: +1.83 GeV. λ(GUT)=0.000549,... |
| · | `L_Higgs_corrected` | lemma | `P` | Spectral action with APF κ_R: λ(GUT) = 0.000545 (diluted from 0.1360 by κ_R normalization). 1-loop SM RG: λ(M_Z) = 0.1250. m_H = 123.1 GeV (obs 125.09). Error budget: σ_scale=0.17 GeV, σ_loop=5.63 GeV (loop ratio 0.217), σ_theory=5.63 GeV → pull=0.35σ (NO tension). σ₀-independent: y_D²/a_total < ... |
| · | `L_MR3_top_identity` | lemma | `P` | In the spectral action scalar potential, the minimum sets σ₀ = v y_t/(√2 κ₃). Therefore M_R₃ = κ₃ σ₀ = y_t v/√2 = m_t (κ₃ cancels exactly). Dominance limit: M_R₃/m_t = 1.000000000. With sub-leading κ₁,κ₂ corrections (ε = 0.151): M_R₃(exact) = 173.5 GeV, m_t(MSbar) = 163.0 GeV, ratio = 1.0647. M_R... |
| · | `L_mbb_0vbb` | lemma | `P` | APF m_betabeta = 4.42 meV (alpha_21=alpha_31=0; L_mbb_prediction [P]). KZ800: < 36.0-156.0 meV -> safe by 8-35x. LEGEND-1000 (~9-21 meV): ratio 0.21-0.49. nEXO (~5-15 meV): ratio 0.29-0.88. nEXO goal (~4-5.5 meV): ratio 0.80-1.10 (marginal). Prediction written 2026; contact expected ~2030s. |
| · | `L_nuR_collider_bounds` | lemma | `P` | APF M_R = [31, 60, 174] GeV. \|V\|^2 = [2.8e-13,1.4e-13,2.9e-13]. LEP >4e+07x, CMS >7e+07x, ATLAS LLP 4e+04x safe. MATHUSLA projected ratio = 2.8x (marginal). sigma scalar: broad resonance, no di-boson bound applies. |
| · | `L_nuR_enforcement` | lemma | `P` | Dim-5 Weinberg operator LLHH/Λ needs 5ε* at contact vertex, but capacity budget is 4ε* (d_eff=4). Contact interaction FORBIDDEN. Seesaw factorization (L·H→ν_R→L·H) is the unique UV completion with sub-vertices at dim-4 (4ε* ≤ 4ε*). Consequence: ν_R exists as propagating fermion. H_F: ℂ^90 → ℂ^96.... |
| · | `L_seesaw_from_A1` | lemma | `P` | Type-I seesaw derived from A1 through 9-link kinematic chain. M_R from potential minimum: σ₀ = 29.1 GeV → M_R = [31, 61, 177] GeV. y_D = 1.86e-07 from spectral weight. LOW-SCALE seesaw: suppression from y_D² ~ 3e-14, not from large M_R/v (1.4). M_R₃/m_t = 1.023. Zero imports, zero anchors. Closed... |
| · | `L_sigma_VEV` | lemma | `P` | Scalar potential minimization: σ₀²/v² = a_R·b/(a_Y·d_R) = 0.01340. σ₀ = 28.5 GeV. Low-scale seesaw: M_R = [31, 60, 174] GeV. M_R₃/m_t(pole) = 1.0026. m_σ(tree) ~ 713 GeV (above LEP). All consistency checks pass (BBN, EWPT, LHC Higgs couplings). [P]: ½ coefficient derived (L_normalization_coeffici... |
| · | `L_sigma_normalization` | lemma | `P` | Including κ_R in spectral action normalization: a_total = a_Y + a_R = 2.630 + 21.341 = 23.971. Dilution: (a_Y/a_total)² = 0.0120 (factor 83). λ(GUT) = g₂²/2 × b/a² = 0.000545 (was 0.1360). κ₃ dominance: 86.8% of Tr(κ†κ). κ_R eigenvalues [1.078, 2.110, 6.088] from L_dm2_hierarchy [P]. Import: Cham... |
| · | `L_sigma_phenomenology` | lemma | `P` | m_σ = 713 GeV (tree-level). BROAD resonance: Γ_σ/m_σ = 0.8 (κ_R ~ 1-6, strong coupling in σ-ν_R sector). Not a narrow bump-hunt target. sin²θ ≈ 8e-35 (H-σ mixing negligible). Primary signatures from ν_R themselves: M_R = [31, 60, 174] GeV. ν_R₁ long-lived: cτ ~ 1e+03 m (MATHUSLA/SHiP). ν_R₁,₂ acc... |

## `apf/internalization.py` — 3 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `L_normalization_coefficient` | lemma | `P` | The ½ coefficient on Tr(κ†κ) in a₂ = Tr(Y†Y) + ½Tr(κ†κ) is DERIVED from the KO-dimension 6 real structure J (L_ST_Dirac [P]). J² = -1 (quaternionic) identifies ν_R ↔ ν_R^c in H_F = ℂ^96. Physical d.o.f. in Majorana sector: dim(ν_R)/dim(ν_R∪ν_R^c) = 3/6 = ½. Verification: Tr(D²) on 9-dim ν sector ... |
| · | `L_scalar_potential_form` | lemma | `P` | The scalar potential V(H,σ) is DERIVED from: (1) APF spectral triple [all P], (2) spectral action principle (unique spectral invariant from A1), (3) heat kernel expansion (mathematical identity). No Chamseddine-Connes import needed — only the mathematical framework of spectral geometry, applied t... |
| · | `L_spectral_action_internal` | lemma | `P` | The spectral action Tr[f(D/Λ)] is identical to the APF partition function Z(β) = Tr[exp(-βH)] at β = 1/Λ². Heat kernel coefficients (physical Yukawa scale): a₀ = 96, a₂ = 2.630 (= c), a₄ = 2.305 (= d), d/c² = 0.3331 ≈ 1/3 (top-dominated). Uniqueness from spectral + gauge invariance + positivity. ... |

## `apf/internalization_geo.py` — 4 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `L_chartability` | lemma | `P` | Smooth manifold derived internally: L_cost [P] → metric space (ε satisfies metric axioms). A1 → bounded diameter (≤ C_total). Delta_fbc [P] → Lipschitz regularity (\|∂φ\| ≤ K). Elliptic regularity bootstrap: C^{0,1} → C^{2,α} → C^∞. C^∞ + locally ℝ^4 (T8) → smooth atlas by definition. No Nash-Kuipe... |
| · | `L_coleman_mandula_internal` | lemma | `P` | G = Poincaré × Gauge derived internally from: (1) Independent derivation chains (0 shared intermediates), (2) L_loc → [G_S, G_I] = 0 (no spacetime-internal mixing), (3) A1 → conservation law budget saturated (no extra charges), (4) T3 (DR) → no fermionic generators (SUSY excluded). Total: 10 Poin... |
| · | `L_kolmogorov_internal` | lemma | `P` | Continuum limit derived internally: A1 (finite capacity) → finite lattice at each ε. R3 (marginalization, from Delta_ordering [P]) → consistent family. A1 → tightness (automatic for bounded families). Tightness + consistency → unique σ-additive limit (proved by construction: cylinder set definiti... |
| · | `L_lovelock_internal` | lemma | `P` | G_μν + Λg_μν = κT_μν is the UNIQUE field equation in d=4: Direct proof from index counting + Bianchi identity. Ansatz E_μν = αg_μν + βR_μν + γRg_μν. Divergence-free ⟹ γ = -β/2 ⟹ E = βG_μν + αg_μν. Gauss-Bonnet is topological in d=4 → no additional terms. d≤3: 0,0 DOF (excluded). d=4: 2 DOF, uniqu... |

## `apf/extensions.py` — 7 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `L_HKM_causal_geometry` | lemma | `P` | APF internalization of HKM (1976): L_irr partial order determines the conformal class of the Lorentzian metric. Three HKM hypotheses verified: (H1) distinguishing (R4 non-cancellation), (H2) strong causality (L_chartability Lipschitz regularity), (H3) reflection (R3 density). Causal diamond D(p,q... |
| · | `L_Malament_uniqueness` | lemma | `P` | APF internalization of Malament (1977): causal isomorphism → conformal isometry (g₂ = Ω²g₁). Null vector preservation verified for 4 null directions × 4 conformal factors. Volume element transforms as √(-det) → Ω^d √(-det), verified to < 1e-10. Radon-Nikodym recovers Ω from volume: max recovery e... |
| · | `L_McKean_Singer_internal` | lemma | `P` | McKean-Singer supertrace formula INTERNALIZED from pure linear algebra (no external theorem import). Core identity: for square M, eig(M†M) = eig(MM†) (SVD). Max eigenvalue difference: 0.0e+00. Therefore Tr[f(M†M)] = Tr[f(MM†)] for any f. McKean-Singer: Tr_s[exp(-tD²)] = 0, verified at 6 t-values ... |
| · | `L_Pauli_Jordan` | lemma | `P` | Pauli-Jordan (causal propagator) function verified: Δ(-x) = -Δ(x) for scalar (max err 0.0e+00), S(-x) = S(x) - 2mΔ(x)·I for spinor (max err 0.0e+00). Both vanish for spacelike separations (microcausality from L_loc). Spin-statistics connection: (-1)^{2J} determines commutator (bosons, 2J even) vs... |
| · | `L_Tannaka_Krein` | lemma | `P` | Tannaka-Krein reconstruction: symmetric monoidal C*-category with fiber functor → compact group G = Aut(ω). TK1 (monoidal): SU(2) CG verified for all j1,j2 ∈ {0,1/2,1,3/2,2}; character orthogonality < 2% error. TK2 (symmetric ε²=1): d=4 → d_space=3 → π₁=S_n → κ∈{±1} → ε²=1 [T_spin_statistics P]. ... |
| · | `L_seesaw_type_I` | lemma | `P` | Type-I seesaw formula m_ν = -M_D·M_R⁻¹·M_Dᵀ derived by block diagonalization of the APF 6×6 neutral fermion mass matrix [[0,M_D],[M_Dᵀ,M_R]]. Seesaw vs exact diag agreement: 2.02e-16 (< 1%). Heavy eigenvalue agreement: 0.00e+00. Heaviest m_ν = 0.0010 eV (sub-eV as observed). Light eigenvalues sca... |
| · | `T6B_beta_one_loop` | theorem | `P` | One-loop beta coefficients derived from APF particle content (T_field [P]) + gauge group (T_gauge [P]) via Casimir/Dynkin arithmetic. b₁ = -41/10 = -41/10 (U(1), NOT AF → Landau pole). b₂ = 19/6 = 19/6 (SU(2), AF). b₃ = 7 = 7 (SU(3), AF → confinement). GUT-scale running: approximate unification w... |

## `apf/red_team.py` — 17 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `RT_FN_vs_capacity` | red_team | `RED_TEAM` | Capacity-derived mass matrix matches FN parameterization to max element diff = 0.0e+00, eigenvalue diff = 0.0e+00. The capacity geometry route (additive cost → multiplicative amplitude → bilinear vertex) produces IDENTICAL results to the FN route. The FN mechanism is the capacity mechanism. |
| · | `RT_NCG_no_physics_import` | red_team | `RED_TEAM` | NCG contributes zero physics imports to APF. 3 spectral triple components [P]-derived. 7 axioms verified. Spectral action from A1. 3 mathematical tools (= Lie classification status). Long-term open: derive abstract spectral triple formalism from canonical object (math research, not physics gap). |
| · | `RT_R1_stable_composites` | red_team | `RED_TEAM` | R1 chain: 5/6 sound, 1 weak link. Stable composites forced by A1 (confinement + finiteness). Trilinear from oriented composites (B1_prime), not stability. Weak link: Step 4 (oriented-composite requirement). |
| · | `RT_R2_vectorlike_SSB` | red_team | `RED_TEAM` | Vector-like gauge sector is CPT-symmetric: 0 CP phases (vs 1 chiral). No sphalerons. Bare Dirac mass without SSB. R2 SOUND but imprecise: "reversible" -> "no intrinsic irreversibility." Chirality required by T_M admissibility independence. |
| · | `RT_R3_no_U1` | red_team | `RED_TEAM` | SU(3)xSU(2) IS anomaly-free without U(1) ([SU(3)]^3=0, Witten=4 doublets). R3 CANNOT be anomaly-based. Correct argument: admissibility completeness — 4 distinguishable reps for 5 physical states. One U(1) resolves all. R3 derivation REWRITTEN in Theorem_R (v6.7). |
| · | `RT_adversarial_Ngen4` | red_team | `RED_TEAM` | 4-generation exclusion verified via 3 independent routes. (1) Capacity: E(4)=10 > C_EW=8 (margin=2). (2) β=capacity identity: discrepancy=17 at n=4 (vs 0 at n=3). (3) Anomaly cancellation still works for 4 gens — confirming capacity, not anomalies, excludes N_gen=4. (4) With 4 gens: Ω_Λ=0.6711 (2... |
| · | `RT_adversarial_partition` | red_team | `RED_TEAM` | Tested 6 partition schemes. APF standard: max error 0.37%. Best alternative: max error 1.49%. APF partition clearly best. |
| · | `RT_adversarial_sin2_alternatives` | red_team | `RED_TEAM` | Fraction scan: 3 fractions p/q (q≤50) within 0.2% of sin²θ_W = 0.23122. Of these, 1 have q≤20. 3/13 error: 0.1950%. Few simple alternatives — prediction is distinctive. |
| · | `RT_bridge_audit` | red_team | `RED_TEAM` | All 5 interpretive bridges are [P] theorems. 8 capacity→observable connections verified, all with explicit closing theorems. Zero interpretive assumptions remain. |
| · | `RT_dag_chain` | red_team | `RED_TEAM` | DAG chain verification: 50 entries, 0 missing, 0 mismatches, consumption OK. CHAIN INTACT. |
| · | `RT_eigvalsh_audit` | red_team | `RED_TEAM` | _eigvalsh real-projection audit. Test matrix: max imaginary off-diag = 0.9185. True eigenvalues: [1.0, 3.0, 7.0]. Real-projection eigenvalues: [1.604527, 2.395473, 7.0]. Complex Hermitian eigenvalues: [1.0, 3.0, 7.0]. Real-projection error: 0.604527. Complex method error: 4.44e-16. WARNING: real ... |
| · | `RT_regression_SA_norm` | red_team | `RED_TEAM` | Regression guard: v5.2.7 spectral action normalization. Correct d/c² = 0.3333 (1/3). Bug value was 0.18 — now rejected. Correct top fraction ≥ 0.99. Bug value was 0.174 — now rejected. |
| · | `RT_regression_higgs_mass` | red_team | `RED_TEAM` | Higgs mass regression guard. Current APF+CCM+1-loop: 149.1 GeV (gap 19.2% from observed 125.09). Rejected values: 208 GeV (v5.2.6 bug), 124.5 GeV (SW2010 misattribution). CCM standard (no RG): 282.7 GeV. |
| · | `RT_seesaw_necessity` | red_team | `RED_TEAM` | 9-link chain verified. M_R = [31, 61, 177] GeV (kinematic, from potential minimum). y_D = 1.86e-07. Δm²₃₁ error: 100.0%. Low-scale: True. Suppression from y_D²=3.5e-14, not M_R/v=1.4. |
| · | `RT_sensitivity_cosmology` | red_team | `RED_TEAM` | Partition scan: 1 partitions of 61 match Planck (2σ). APF partition (3,16,42) is UNIQUE. Alternative totals with ≥1 match: 7 values in [40,119]. Prediction is non-trivial. |
| · | `RT_sensitivity_sin2theta` | red_team | `RED_TEAM` | Sensitivity analysis for sin²θ_W = 3/13. Max shift under ±10% x perturbation: 10.4%. Max shift under ±10% d perturbation: 21.2%. ∂sin²/∂x = -0.4655, ∂sin²/∂d = -0.118343. Near-hits (integer d, x∈[0.3,0.7], <1% error): 2 found. FRAGILE under perturbation. UNIQUE among integer d values. |
| · | `RT_texture_chain` | red_team | `RED_TEAM` | All NNLO Fritzsch parameters derived from framework constants: c = x^{2d} = 0.00390625 (T27c+T8), θ = π/3 (T7), w nearest-neighbor (L_gen_path), GJ = (1/3, 3, 1) (T_gauge). Zero Fritzsch/GJ imports. |

## `apf/session_v63c.py` — 4 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `L_hierarchy_boson_suppression` | lemma | `C` | EW VEV from capacity suppression: v = 251.1 GeV (obs 246.22, err 2.0%). C_boson = 16 in both coefficient and exponent. d_eff^C_boson = 102^16 = 1.373e+32. Closes P1 §2.1 (absolute hierarchy). σ₀²/v² = 0.01341 → σ₀ = 29.1 GeV. |
| · | `L_hierarchy_cascade` | lemma | `C` | σ₀ = 29.1 GeV from σ₀²/v² = 0.01340 × v = 251.13 GeV. M_R = [31.3, 61.4, 177.0] GeV. M_R REVERTS [P] → [P+anchor]; P1 §2.2 closure WITHDRAWN — σ₀ and M_R inherit v=251.13 from the tuned-c_R vev (re-graded 2026-05-29). |
| · | `L_neutrino_closure` | lemma | `C` | P2 §1.3 CLOSED. Δm²₂₁/Δm²₃₁ = 0.02952 (exp 0.02950, err 0.06%). Gap reduction from Gram alone: 3.4× → 3.3980× (i.e. 0.06% residual). NOTE: the scale-free ratio Δm²₂₁/Δm²₃₁ survives, but the §1.3 *closure* claim depended on M_R [P] via the cascade, which now reverts to [P+anchor] (tuned-c_R vev). ... |
| · | `L_yD_spectral` | lemma | `C` | y_D² = N_gen/(W_seesaw×d_eff^KO) = 3/(77×102⁶) = 3.4596e-14. y_D = 1.8600e-07. W_seesaw = C_f+2C_b = 45+32 = 77 (two Higgs insertions in seesaw M_D·M_R⁻¹·M_D^T). Δm²₃₁ = 2.5139e-03 eV² (exp 2.5150e-03, err 0.04%). Δm²₂₁ = 7.4209e-05 eV² (err 0.01%). Σmᵢ = 59.9 meV. m_ββ = 4.4 meV. ZERO neutrino a... |

## `apf/session_qg.py` — 4 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `L_QG_P1_closure` | lemma | `C` | P1 §3.1 CLOSED (to 0.11%). 8 QG components derived [P], 2 precision items remain. UV finite: Z = (1+e^{βε*})^61 (exact). CC: Λ·G = 10^-121.6. Scale: v = 251.1 GeV (2.0%). Higgs: m_H = 124.9 GeV (0.15%, pull 0.33σ). The 149 GeV CCM problem is SOLVED by κ_R dilution (126× improvement). Residuals: (... |
| · | `L_inflation_smoothing` | lemma | `P` | Inflation staircase attack surface resolved by three mechanisms: (1) Multiplicity averaging: C(61,30) ~ 10^17 microstates suppress step features by factor 10^-17. (2) Fokker-Planck diffusion: δk = 3.9 steps smears staircase over 13% of total (naive ε = 2.0 → averaged ε = 0.26). (3) CMB window: 3.... |
| · | `L_vev_coleman_weinberg` | lemma | `C` | 1-loop Coleman-Weinberg correction: δ_CW = 2.37% (POSITIVE — increases v). v_tree = 251.1 GeV → v_CW = 254.1 GeV (worsens from 2.0% to 3.2% vs obs 246.22). Top quark dominates (90% of \|CW\|). CONCLUSION: the tree-level formula with EW-scale traces implicitly resums loop corrections. The 2% residua... |
| · | `L_vev_threshold_matching` | lemma | `C` | Spectral traces evaluated at ν_R decoupling scale μ_R = (M_R₁·M_R₂·M_R₃)^{1/3} = 68.4 GeV. 1-loop QCD: y_t(μ_R) = 0.9570 (IR-enhanced from 0.9362). v(μ_R) = 246.50 ± 1.39 GeV (obs 246.22, err 0.11%, pull 0.20σ). Improvement: 18× over M_Z evaluation (2.0% → 0.11%). Self-consistent: 1 iteration con... |

## `apf/session_nnlo.py` — 5 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `L_Higgs_curvature_channel` | lemma | `P` | Third FN channel from Higgs VEV curvature on P₃. h = (0,1,0) unique ℓ₁-minimum cover. q_curv = q_B[0]/N_gen = 7/3, v_curv = (0, x^{7/3}, 0). m_s/m_b = 0.0198 (exp 0.019, +4.4%). GJ = 3.00 (exp 3.0, -0.1%). CLOSES m_s/m_b and Georgi-Jarlskog. |
| · | `L_NNLO_Fritzsch` | lemma | `P` | c = x^{2d} = x^8, θ = π/N_gen = π/3, w = (1,-e^{iπ/3},0)/√2. δ_CKM = 65.7° (+0.1%), J = 3.04e-05 (−1.3%), m_d/m_s = 0.044 (−11%), V_us = 0.239 (+6.5%). 8 observables, zero free parameters. |
| · | `L_lepton_GJ` | lemma | `P` | SU(5) GJ: gen-0 × 1/N_c, gen-1 × N_c, gen-2 × 1. m_e/m_μ = 0.00498 (+3%), m_μ/m_τ = 0.06186 (+4%), m_e/m_τ = 0.000308 (+7%). GJ₂ = 2.97 ≈ 3, GJ₁ = 0.33 ≈ 1/3. All from down-quark texture + N_c. Zero new parameters. |
| · | `L_mass_texture_det_real` | lemma | `P` | Every banked mass-texture channel is a unitary-diagonal conjugation of a real symmetric PSD core (down: 3 real rank-1 outers + the Hermitian NNLO Fritzsch \|w><w\|; up: the D(K o bb^T)D^dag bookkeeper with KMS-positive-definite kernel + the real Higgs channel), so M_u and M_d are Hermitian positive... |
| · | `L_sin2_oneloop` | lemma | `P + disp.rel.` | sin²θ̂_W = (3/13)(1+Δκ̂) = 0.23122. Δκ̂ = 0.001953 = 3.4×α/(4π). Tension: 15σ → 0σ. Δρ_t = 0.00938, Δα̂ = 0.05896. Irreducible: Δα_had = 0.02761 [disp.rel.]. 3/13 is MS-bar tree (gap 0.2%), not on-shell (gap 3.3%). |

## `apf/session_delta_pmns.py` — 2 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `L_PMNS_CP_corrected` | lemma | `P` | CORRECTS T_PMNS_CP: k_B(ν)=3 (H̃, not H), but seesaw factorizes dominant holonomy phase (L_seesaw_factorization [P]). Residual from BK/Higgs cross-channel, suppressed by c_Hu=0.125. Conservative: δ=+11.2° with 3.0% angle error (g_13 = 0.0275 ∠-127° on Gram). FN-textured: δ=+2.9° with 0.2% error (... |
| · | `L_seesaw_factorization` | lemma | `P` | Single-channel seesaw M_D·M_R⁻¹·M_D^T with holonomy phase φ(g-h) produces exactly factorizable phases for any real M_R. Proof: M_D = P·f·Q, M_D^T = Q·f^T·P → M_ν = P·[f·Q·M_R⁻¹·Q·f^T]·P^T. Inner bracket has common phase (not differential) → Majorana rephasing removes all phases → δ=0 exactly. Key... |

## `apf/session_cosmo_update.py` — 3 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `L_DESI_DR2_confrontation` | lemma | `P` | APF: (w₀,w_a)=(-1,0). DESI DR2 (15M objects): 2.8-4.2σ (up from ~2.5σ in DR1). BAO alone consistent with ΛCDM. NOT excluded. Supersedes L_DESI_response. |
| · | `L_joint_cosmo_neutrino` | lemma | `P` | Joint: w=-1, Σm_ν=58.8 meV, NO. DESI ΛCDM: < 64.2 meV. Margin: 5.4 meV. IO excluded (min 101 meV). Bayes NO/IO = 46.5. Future: 3σ. |
| · | `L_top_mass_hint` | lemma | `C` | Conjecture: σ = x^(1/d) = 0.8409. m_t = 165.2 GeV (exp 163.0, 1.4%). NOT derived. Down sector unexplained. |

## `apf/_optimize_vendored.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_optimize_vendored_minimize_convex_bounded_P` | theorem | `P_optimize_vendored` | Vendored minimize() converges on the canonical convex bounded QP (f(x) = 0.5 * \|\|x - target\|\|^2 on box [0, 1]) to within 1e-3 of the analytical clip(target, 0, 1) solution. OptimizeResult-compatible return interface (.x / .fun / .success / .nit / .nfev / .message). Used as the scipy.optimize.mini... |

## `apf/a_mu_hvp_capacity_density.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_a_mu_hvp_capacity_counted_distinction_density` | theorem | `P_structural_seam` | The source-codomain reading for muon g-2 (RP-mu, 'upstream'), delivered without manufacturing a resolution. The SM a_mu = QED (dominant, determined) + EW (small, determined) + hadronic (HVP + light-by-light). The leading HVP piece is a_mu^HVP,LO = (1/3)(alpha/pi)^2 int (ds/s) K(s) R(s), with K(s)... |

## `apf/abelian_coupling_capacity_count.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_abelian_coupling_fixed_by_rank1_capacity_count` | theorem | `P_structural_reading` | Supersedes the v24.3.191 no-go: m=0 does not leave the abelian coupling free, it fixes it. The competition matrix A=[[1,x],[x,x^2+m]] (det=m) is rank 2 for the non-abelian sectors (m=8, m=3) and RANK 1 for U(1) (m=0) -- a single undifferentiated mode. By the coupling-information correspondence (T... |

## `apf/aboutness_occupancy_section.py` — 2 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_aboutness_is_occupancy_ssb_section` | theorem | `P_structural_reading` | Record aboutness is the occupancy-selected vacuum of a spontaneously broken symmetry. The law (A2/BW) is symmetry-degenerate on the aboutness manifold (Type II); an irreversible L_irr locking event tilts the cost functional and selects one binding (Type II resolution). The law forces THAT a uniqu... |
| · | `T_held_to_record_typing` | theorem | `P_structural_reading` | Composes the two banked held-to-record faces into the three-way TYPING the Paper 9 Technical Supplement asserts (def:ts-record-transition): the held carrier H, the invariant record quotient R(H), and the outcome-selection instruments {C_i} are PAIRWISE DISTINCT and cannot be identified. All three... |

## `apf/acc_reading_selection.py` — 8 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `L_abelian_no_ledger_channel_structure` | lemma | `P_structural_reading` | The gauge reading dichotomy formerly cited, as a premise, that a gauge coupling's only channel-distinguishing structure is its RG flow (the T20-level exhaustiveness). This lemma discharges that premise for the abelian without the broad claim, by showing the abelian's ACTUAL structures are both ab... |
| · | `L_abelian_support_openness_pins` | lemma | `P_structural_instrument` | The reading-exhaustiveness walk's registered sentinel (2026-07-03, split landing, hostile-audited). Pins the .284 openness in both directions with live flag reads (the .314 pin pattern: a flag flip fails this check until re-adjudicated); recomputes the not-a-state-function corollary -- same horiz... |
| · | `L_reading_profile_blind` | lemma | `P` | The profile-blindness lemma -- the lever that closes the two-form exhaustiveness of a gauge coupling's horizon reading. A reading is 1/alpha = realignment cost per interaction (T20 [P]) = n*epsilon distinctions (L_cost / T_realignment_cost_is_transition_energy [P]); a distinction count is additiv... |
| · | `T_abelian_matter_enters_via_trace` | theorem | `P` | Discharges the Phase-1(R) factorization. The capacity measure on the ledger is the uniform per-slot entropy sigma = ln(d_eff) (L_sigma_intensive [P], from L_self_exclusion: each slot has equal d_eff = 102 = 60+42). Under that [P]-uniform measure the abelian's matter-content projects onto the read... |
| · | `T_acc_reading_selection` | theorem | `P_structural` | One capacity ledger -- C_total = 61 slots at per-slot degeneracy d_eff = 102 -- read four ways. The Reading-Selection Rule: a resolving structure reads the ACC scalar fixed by its RANK and its TYPE, all gauge readings referred to the de Sitter horizon S_dS (L_crossing_entropy [P]). The four insta... |
| · | `T_gauge_reading_dichotomy` | theorem | `P_structural_reading` | The count-selection theorem for gauge structures -- the close of the abelian support-uniqueness residual. A gauge coupling-inverse is the resolved information per interaction, 1/alpha = m*sigma, with sigma = ln d_eff the unique intensive quantum (L_sigma_intensive [P]) and m the count of capacity... |
| · | `T_gauge_value_chain_is_P` | theorem | `P_structural_reading` | The capstone of the gauge-rank close: the quantitative reading rule above the constitutive floor is [P]. Five bank-[P] links compose to the gauge values with no fitted scale: the per-slot degeneracy d_eff = (C_total-1)+C_vacuum = 60+42 = 102 (L_self_exclusion [P]); the unique intensive entropy qu... |
| · | `T_rank_field_selector` | theorem | `P_structural_reading` | The rank clause of the Reading-Selection Rule. The Admissibility-Capacity record carries exactly two scalars -- the bare slot count K = 61 and the degeneracy-smeared count S_dS = K*ln d_eff -- and T_ACC_unification [P] establishes that every regime quantity reads one of the two. Which one a gauge... |

## `apf/acc_unification_all_p.py` — 15 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_ACC_base_record_functor_P` | theorem | `—` | ACC provides the common base record functor (K,d_eff). |
| · | `check_T_ACC_unification_all_P` | theorem | `—` | All legitimate ACC unification layers are P: base, projections, fibered category, canonical lift, strict subspace functors, and original-level pullback. |
| · | `check_T_F_bridge_strict_functor_P` | theorem | `—` | F_bridge is a strict functorial regime fiber over ACC. |
| · | `check_T_F_horizon_strict_functor_P` | theorem | `—` | F_horizon is a strict functorial regime fiber over ACC. |
| · | `check_T_F_operator_strict_functor_P` | theorem | `—` | F_operator is a strict functorial regime fiber over ACC. |
| · | `check_T_F_quantum_strict_functor_P` | theorem | `—` | F_quantum is a strict functorial regime fiber over ACC. |
| · | `check_T_all_four_subspace_witnesses_strict_P` | theorem | `—` | All four subspace witnesses are strict functors over the ACC base. |
| · | `check_T_bare_record_only_boundary_P` | theorem | `—` | Boundary certified: the all-P theorem does not claim bare (K,d_eff) record-only morphisms determine subspace maps. |
| · | `check_T_canonical_resolution_functor_P` | theorem | `—` | Canonical resolution lifts generated ACC morphisms into the fibered category functorially. |
| · | `check_T_fibered_ACC_category_P` | theorem | `—` | The resolved/fibered ACC category satisfies identity and composition laws. |
| · | `check_T_free_vector_space_linearization_P` | theorem | `—` | Free-vector-space linearization preserves identities and composition. |
| · | `check_T_generated_ACC_category_P` | theorem | `—` | The generated APF/ACC bank-facing category is strict. |
| · | `check_T_integer_scalar_projections_strict_P` | theorem | `—` | Integer and scalar readings factor strictly through the ACC base record. |
| · | `check_T_original_generated_level_pullback_P` | theorem | `—` | Strict fiber functoriality pulls back to the original/generated ACC category by canonical resolution. |
| · | `check_T_regime_structures_fibered_over_ACC_P` | theorem | `—` | Regime carrier structures are fibers over the ACC base. |

## `apf/acc_unification_no_imports.py` — 8 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_ACC_unification_all_P_predecessor` | theorem | `—` | Consolidated all-P categorical predecessor passes. |
| · | `check_T_ACC_unification_fully_P_no_external_imports` | theorem | `—` | ACC unification is fully P with explicit no-external-physical-import provenance. |
| · | `check_T_APF_carrier_map_provenance_P` | theorem | `—` | Every carrier map family is generated by an APF witness construction. |
| · | `check_T_APF_morphism_provenance_P` | theorem | `—` | Every unification morphism is APF-generated in the bank presentation. |
| · | `check_T_APF_object_provenance_P` | theorem | `—` | Every unification object is APF ACC-generated. |
| · | `check_T_formal_math_language_not_physical_import_P` | theorem | `—` | Categories, finite sets, and free vector spaces are used only as formal mathematics, not physical imports. |
| · | `check_T_no_bare_record_overclaim_P` | theorem | `—` | The theorem does not overclaim that bare (K,d_eff) records alone determine all subspace maps. |
| · | `check_T_no_external_physical_imports_P` | theorem | `—` | No external physical equations, constants, Lagrangians, Hilbert/C*-primitives, or arbitrary carrier maps enter the unification proof. |

## `apf/admissible_representation_stack.py` — 10 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_admissible_representation_stack_P` | theorem | `—` | APF representations form a finite stack/sheaf-like descent object over the interface base, with obstruction classification. |
| · | `check_T_contextuality_as_failed_descent_schema_P` | theorem | `—` | Contextuality/incompatible-local-description is represented as failed descent via overlap incoherence. |
| · | `check_T_descent_gluing_rule_P` | theorem | `—` | Finite descent/gluing rule accepts ACC-compatible data and rejects obstructed globalizations. |
| · | `check_T_interface_site_finite_P` | theorem | `—` | Finite APF interface site is well-formed. |
| · | `check_T_not_full_infinity_stack_overclaim_P` | theorem | `—` | Scope boundary preserved: this is a finite 1-categorical descent theorem, not a claimed full infinity-stack construction. |
| · | `check_T_obstruction_classification_complete_P` | theorem | `—` | Descent obstruction classes cover the known APF failure modes exercised by this theorem. |
| · | `check_T_quantum_Cstar_as_fiber_local_schema_P` | theorem | `—` | Quantum C*/Hilbert structure is local-admissible in a quantum fiber but fails flat substrate-global descent. |
| · | `check_T_representation_presheaf_defined_P` | theorem | `—` | Representation assignment over the APF interface site is defined and typed. |
| · | `check_T_restriction_maps_defined_P` | theorem | `—` | Restriction maps for local representations are typed and audit-classified. |
| · | `check_T_scheme_dependence_as_fiber_local_schema_P` | theorem | `—` | Scheme dependence is represented as fiber-local evaluator structure that fails substrate-global descent. |

## `apf/aeon_turnover.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_aeon_turnover` | theorem | `—` | Toy-ledger regime: the Type V saturation exit composes with the banked release/export machinery (full-export branch; the declared-codomain branch stays [C]) to the terminal patch configuration (a, empty): distinction family empty, Omega_Gamma intact, kappa(empty) = 0 <= C. Two routes (direct dS-h... |

## `apf/amount_graded_testedness.py` — 4 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `L_amount_graded_testedness_encoding_no_go` | lemma | `P_structural_instrument` | No amount-graded testedness principle is a theorem of the corpus as formalized 2026-07-04. Shape (ii) REFUTED as theorem: three floor-coherent GCC signatures (single-atom / positional / unary) hold the SAME N = 16-valued record at least grades eps*{1, log2 N, N} -- the floor invariant (b1:prop:in... |
| · | `T_agt_par_anatomy` | theorem | `P_structural` | The anatomy of TCP-strong's discharge gap, certified at proved strength ONLY -- no axiom is adopted. (1) Monotone grading is insufficient: the consistency mechanism g(e) = rho forces full re-expression iff g is the identity in the ledger currency (par); logarithmic and quadratic gradings solve wi... |
| · | `T_contention_law_granularity_occupancy_fork` | theorem | `P_structural` | The contention-law walk (2026-07-04, REDUCE 0.85) banked at its proved strength -- the (c1) premise walked, neither derived nor refuted. THE SHARING-PRICE CONSOLIDATION (adverse, <= 0): the banked Delta = eps*(J - R) pricing, extended by TYPED ITERATED JOIN over the walk-typed Sep configuration (... |
| · | `T_fagt2_encoding_argmin_pressure_and_read_channel` | theorem | `P_structural` | The F-AGT2 walk (2026-07-04, REDUCE 0.85) banked at its proved strength -- the (E) distributed-encoding door walked, neither delivered nor shut. THE A2-PRESSURE LEMMA (adverse, new): on both banked cost axes -- GCC formation (grades eps*{1, log2 N, N}; ordering proved trivially for all N >= 3, ex... |

## `apf/anchor_center_correspondence.py` — 2 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_anchor_set_is_electric_center_data` | theorem | `—` | (no summary) |
| · | `check_T_delta_vs_centre_entropy_diagnoses` | theorem | `P` | DELTA VS THE CENTRE-SENSITIVE ENTROPY (Paper 12 round-6 walk C3, reviewer Q7). Comparison object named in-check: the CHR electric-centre entropy S_EC = H({p_c}) + sum p_c log2 d_c on the one-side algebra of check 1 (Donnelly booking; distillable identically 0 on every construction used -- scope n... |

## `apf/anchor_support_algebra.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_anchor_support_formalization` | theorem | `P` | THE ALGEBRAIC ANCHOR (Paper 12 round-6 walk C1, reviewer Q1). On a finite interface presentation (V, {A_v}, C) with ARBITRARY finite-dimensional unital *-algebra factors (full matrix algebras NOT assumed; witnessed on the lattice's own with-centre billing factor C (+) M_2), the support supp(M) = ... |

## `apf/anti_fitting_provenance_audit.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_anti_fitting_provenance_audit_P` | theorem | `—` | Anti-fitting provenance audit detects target/posterior smuggling and fail-closes. |

## `apf/aps.py` — 3 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_APS_construction` | theorem | `P_structural` | Admissible Possibility Space witness satisfies all six structural invariants of Paper 1 Supplement v7.1 Definition 4.1: finite non-empty substrate; non-empty continuation sets; continuation equivalence is a true equivalence relation; physical state space well-defined as quotient; finite positive ... |
| · | `T_continuation_preorder` | theorem | `—` | The continuation preorder [x] preceq [y] iff Cont(y) subseteq Cont(x) is reflexive and transitive on the substrate, and antisymmetric after quotienting to physical classes. This is the formal root of the Paper 3 thermodynamic arrow-of-time: irreversibility = strict continuation contraction. |
| · | `T_state_distinction_ledger_induced` | theorem | `—` | Paper 1 Supplement v7.1 Lemma 4.2: physical states, distinctions, and ledgers are downstream of the APS data, not posited alongside it. State = continuation-equivalence class; distinction = finite-cost separator of classes; ledger = finite capacity accounting over jointly maintained distinctions,... |

## `apf/arch_defect_calculus_internal_identity_real_adapter.py` — 3 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_arch_defect_calculus_internal_identity_adapter_atlas_routes_P` | theorem | `—` | Atlas routes arch defect calculus architecture payload to INTERNAL_IDENTITY_GLOBAL_P. |
| · | `check_T_arch_defect_calculus_internal_identity_adapter_closure_kind_P` | theorem | `—` | arch defect calculus architecture adapter declares closure_kind=internal_identity (engine self-certification). |
| · | `check_T_arch_defect_calculus_internal_identity_adapter_registry_pointer_P` | theorem | `—` | arch defect calculus architecture adapter cites registry pointer. |

## `apf/arch_interface_engine_operational_internal_identity_real_adapter.py` — 3 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_arch_interface_engine_operational_internal_identity_adapter_atlas_routes_P` | theorem | `—` | Atlas routes arch interface engine operational payload to INTERNAL_IDENTITY_GLOBAL_P. |
| · | `check_T_arch_interface_engine_operational_internal_identity_adapter_closure_kind_P` | theorem | `—` | arch interface engine operational adapter declares closure_kind=internal_identity (engine self-certification). |
| · | `check_T_arch_interface_engine_operational_internal_identity_adapter_registry_pointer_P` | theorem | `—` | arch interface engine operational adapter cites registry pointer. |

## `apf/arch_rdfi_kernel_internal_identity_real_adapter.py` — 3 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_arch_rdfi_kernel_internal_identity_adapter_atlas_routes_P` | theorem | `—` | Atlas routes arch RDFI global descent kernel payload to INTERNAL_IDENTITY_GLOBAL_P. |
| · | `check_T_arch_rdfi_kernel_internal_identity_adapter_closure_kind_P` | theorem | `—` | arch RDFI global descent kernel adapter declares closure_kind=internal_identity (engine self-certification). |
| · | `check_T_arch_rdfi_kernel_internal_identity_adapter_registry_pointer_P` | theorem | `—` | arch RDFI global descent kernel adapter cites registry pointer. |

## `apf/artifact_to_route_payload_adapter.py` — 5 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_artifact_adapter_batch_report_P` | theorem | `—` | Artifact adapter emits batch reports with route/confidence counts. |
| · | `check_T_artifact_adapter_detects_EW_P` | theorem | `—` | Artifact adapter infers EW trace payload from verifier text. |
| · | `check_T_artifact_adapter_detects_dark_runtime_P` | theorem | `—` | Artifact adapter infers dark runtime payload from JSON. |
| · | `check_T_artifact_adapter_provenance_boundary_P` | theorem | `—` | Artifact adapter preserves provenance boundary by routing smuggling markers to provenance audit. |
| · | `check_T_artifact_to_route_payload_adapter_P` | theorem | `—` | Artifact-to-Route Payload Adapter is P: integration artifacts compile into conservative route payload candidates. |

## `apf/base_fiber_allocation.py` — 14 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_ACC_unification_not_flat_algebra_P` | theorem | `—` | ACC unification is stratified/fibered, not a flat universal-algebra overclaim. |
| · | `check_T_Cstar_fiber_internal_boundary_P` | theorem | `—` | The *-operation, complex action, and C*-norm are fiber-internal under current substrate primitives. |
| · | `check_T_across_frame_fork_localized` | theorem | `—` | The across-frame fork is cited at exactly three bank surfaces plus one fenced mention, nowhere else; the FOUNDATIONAL_BASE across_region row is provably contained (citation hygiene, closed-world over the current corpus; not semantic horn-blindness). |
| · | `check_T_base_fiber_allocation_criterion_P` | theorem | `—` | Base/fiber allocation criterion is well-defined from current APF substrate primitives. |
| · | `check_T_base_fiber_allocation_theorem_P` | theorem | `—` | APF derives the base/fiber allocation rule: universal substrate structures are separated from interface-local representations. |
| · | `check_T_billed_vs_derived_register_criterion` | theorem | `P_structural` | Billed-vs-derived is REGISTER-RELATIVE: CONSTITUTIVE (declared adoption record, registry-relative) / DERIVED (theorem of the stack-minus-X) / BILLED in a named register (R1 census unit; R3 kind-(a) value-configuration, census-silent; R4 demand row, Delta=1 template class only; R5 named open, unin... |
| · | `check_T_canonical_token_requires_type_or_theorem` | theorem | `—` | Token-registered orientation content is reference-record (T1), relocated type-level structure (T2, landing on the OPEN type-census entry lemma), or the derived-canonicity falsifier slot (T3) -- canonicity cannot hide in token clothing; model-relative, horn-definition-relative, no collision citation. |
| · | `check_T_census_unit_exclusion_conditional` | theorem | `—` | IF a standing type-level commitment constitutes or displaces a horizon census unit THEN excluded amplitude-independently: extension shifts the CC register by ln(102)=4.625 nats (x24-x220 over the honest bands; fractions alone do NOT exclude -- 43/62 at ~0.8 sigma); displacement excluded at unit-c... |
| · | `check_T_cross_interface_algebraic_impossibility_ceiling_P` | theorem | `—` | The cross-interface algebraic impossibility theorem supplies the ceiling: full C*-structure cannot be substrate-global under current primitives. |
| · | `check_T_fiber_local_negative_cases_P` | theorem | `—` | C*-quantum and scheme-evaluator structures fail the substrate-global criterion and are assigned to fibers. |
| · | `check_T_gauge_connection_is_gauge_variant_convention_P` | theorem | `—` | The across-interface gauge connection A_mu is gauge-variant convention and allocates fiber-local (same column as the C*-norm), resting on the banked substrate absence of an across-interface frame-identification (loc_commut). 'No B' for the frame-choice only; the gauge-invariant residue (Wilson va... |
| · | `check_T_gauge_program_kept_separate_P` | theorem | `—` | Gauge-as-fiber-automorphism is kept as a separate theorem program, not smuggled into the C*-impossibility result. |
| · | `check_T_representation_locality_theorem_P` | theorem | `—` | Representation locality is derived: structures requiring absent polarity/reversal/complex/norm/evaluator data are fiber-local. |
| · | `check_T_substrate_global_positive_cases_P` | theorem | `—` | Known APF base structures pass the substrate-global criterion. |

## `apf/bec_codomain_adapter.py` — 4 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_bec_codomain_adapter_atlas_contract_P` | theorem | `P_codomain_adapter_atlas_contract` | Bose-Einstein condensation adapter declares the CODOMAIN atlas contract; live payload reaches COHERENT via the engine. |
| · | `check_T_bec_codomain_adapter_audit_first_P` | theorem | `P_codomain_adapter_audit_first` | Audit-first non-claims preserved; target not consumed; evaluator ledger declared. |
| · | `check_T_bec_codomain_adapter_payload_contract_P` | theorem | `P_codomain_adapter_contract` | Bose-Einstein condensation codomain adapter payload carries the required fields and routes through the engine. |
| · | `check_T_bec_codomain_adapter_verdict_consistent_P` | theorem | `P_codomain_adapter_verdict_consistent` | Installed Bose-Einstein condensation runtime reproduces every fixture verdict through the engine. |

## `apf/born_at_ties.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `L_selection_ledger_completeness` | lemma | `P_structural_reading` | THE FLAT-TIE UNIFORMITY FLOOR, reading-graded and grant-free: under R-sel-LC (admissible outcome laws are functions of counted structure -- the honest, NAMED residue of SUP: A1-motivated via C1's d... |

## `apf/bottom_msbar_export_candidate.py` — 40 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_bottom_msbar_export_all_gates_pass` | theorem | `—` | (no summary) |
| · | `check_T_bottom_msbar_export_alpha_s_future_only` | theorem | `—` | (no summary) |
| · | `check_T_bottom_msbar_export_bank_closure` | theorem | `—` | (no summary) |
| · | `check_T_bottom_msbar_export_boundary_forbids_any_scale` | theorem | `—` | (no summary) |
| · | `check_T_bottom_msbar_export_boundary_forbids_final` | theorem | `—` | (no summary) |
| · | `check_T_bottom_msbar_export_candidate_uncertainty_is_internal_zero` | theorem | `—` | (no summary) |
| · | `check_T_bottom_msbar_export_claim_language_safe` | theorem | `—` | (no summary) |
| · | `check_T_bottom_msbar_export_comparison_sigma_positive` | theorem | `—` | (no summary) |
| · | `check_T_bottom_msbar_export_downstream_gate_qcd` | theorem | `—` | (no summary) |
| · | `check_T_bottom_msbar_export_first_failed_gate_publication` | theorem | `—` | (no summary) |
| · | `check_T_bottom_msbar_export_gates_nonempty` | theorem | `—` | (no summary) |
| · | `check_T_bottom_msbar_export_msbar_residual_small` | theorem | `—` | (no summary) |
| · | `check_T_bottom_msbar_export_no_smuggling_roles` | theorem | `—` | (no summary) |
| · | `check_T_bottom_msbar_export_no_target_consumption_gate` | theorem | `—` | (no summary) |
| · | `check_T_bottom_msbar_export_nonselfscale_open` | theorem | `—` | (no summary) |
| · | `check_T_bottom_msbar_export_pass_status` | theorem | `—` | (no summary) |
| · | `check_T_bottom_msbar_export_pdg_not_consumed` | theorem | `—` | (no summary) |
| · | `check_T_bottom_msbar_export_pole_knockout_strength` | theorem | `—` | (no summary) |
| · | `check_T_bottom_msbar_export_pole_rejected` | theorem | `—` | (no summary) |
| · | `check_T_bottom_msbar_export_pull_quoted_subsigma` | theorem | `—` | (no summary) |
| · | `check_T_bottom_msbar_export_pull_rescaled_less_than_1p5` | theorem | `—` | (no summary) |
| · | `check_T_bottom_msbar_export_ratio_range` | theorem | `—` | (no summary) |
| · | `check_T_bottom_msbar_export_relative_residual_small` | theorem | `—` | (no summary) |
| · | `check_T_bottom_msbar_export_residual_sign` | theorem | `—` | (no summary) |
| · | `check_T_bottom_msbar_export_route_status` | theorem | `—` | (no summary) |
| · | `check_T_bottom_msbar_export_running_not_required_for_mb` | theorem | `—` | (no summary) |
| · | `check_T_bottom_msbar_export_running_required_for_other_scales` | theorem | `—` | (no summary) |
| · | `check_T_bottom_msbar_export_self_scale_branch_closed` | theorem | `—` | (no summary) |
| · | `check_T_bottom_msbar_export_self_scale_identity_gate` | theorem | `—` | (no summary) |
| · | `check_T_bottom_msbar_export_self_scale_required_for_mb` | theorem | `—` | (no summary) |
| · | `check_T_bottom_msbar_export_status` | theorem | `—` | (no summary) |
| · | `check_T_bottom_msbar_export_summary_digest` | theorem | `—` | (no summary) |
| · | `check_T_bottom_msbar_export_summary_tables` | theorem | `—` | (no summary) |
| · | `check_T_bottom_msbar_export_table_has_candidate` | theorem | `—` | (no summary) |
| · | `check_T_bottom_msbar_export_table_has_comparison_only` | theorem | `—` | (no summary) |
| · | `check_T_bottom_msbar_export_table_has_residual` | theorem | `—` | (no summary) |
| · | `check_T_bottom_msbar_export_trace_covariance_boundary` | theorem | `—` | (no summary) |
| · | `check_T_bottom_msbar_export_v23_dependency` | theorem | `—` | (no summary) |
| · | `check_T_bottom_msbar_export_value_preserved` | theorem | `—` | (no summary) |
| · | `check_T_bottom_msbar_export_version` | theorem | `—` | (no summary) |

## `apf/bottom_msbar_rundec_real_adapter.py` — 6 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_bottom_msbar_rundec_adapter_certification_P` | theorem | `—` | EVALUATOR_MAP edge in ew movement graph resolves to MOVES_CLEANLY with bottom_msbar_rundec-filled payload. |
| · | `check_T_bottom_msbar_rundec_adapter_evaluator_consistent_P` | theorem | `—` | v78 threshold-matched RunDec output matches published benchmark case m_b(m_b)=4.163 GeV -> m_b(10 GeV)=3.610 GeV within 1 MeV tolerance. |
| · | `check_T_bottom_msbar_rundec_adapter_external_ledger_declared_P` | theorem | `—` | All 12 required external evaluator ledger fields declared on the bottom_msbar_rundec snapshot. |
| · | `check_T_bottom_msbar_rundec_adapter_no_smuggling_P` | theorem | `—` | No forbidden target-value key in bottom_msbar_rundec payload; target_value_consumed=False. |
| · | `check_T_bottom_msbar_rundec_adapter_payload_contract_P` | theorem | `—` | bottom_msbar_rundec adapter produces ew-shaped route payload with evaluator + codomain filled. |
| · | `check_T_bottom_msbar_rundec_real_adapter_P` | theorem | `—` | bottom_msbar_rundec real adapter wires banked evaluator content into Engine-readable route payload; EVALUATOR_MAP edge fills cleanly; no smuggling; external ledger declared. |

## `apf/bottom_msbar_transport.py` — 42 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_bottom_msbar_alpha_s_context_present` | theorem | `—` | (no summary) |
| · | `check_T_bottom_msbar_bank_closure` | theorem | `—` | (no summary) |
| · | `check_T_bottom_msbar_blocked_export_stage` | theorem | `—` | (no summary) |
| · | `check_T_bottom_msbar_claim_boundary_count` | theorem | `—` | (no summary) |
| · | `check_T_bottom_msbar_closed_stage_count` | theorem | `—` | (no summary) |
| · | `check_T_bottom_msbar_comparison_table_count` | theorem | `—` | (no summary) |
| · | `check_T_bottom_msbar_ew_dependency_closed` | theorem | `—` | (no summary) |
| · | `check_T_bottom_msbar_export_status_open` | theorem | `—` | (no summary) |
| · | `check_T_bottom_msbar_first_failed_gate_exact` | theorem | `—` | (no summary) |
| · | `check_T_bottom_msbar_forbidden_inputs_not_used` | theorem | `—` | (no summary) |
| · | `check_T_bottom_msbar_forbidden_physical_final` | theorem | `—` | (no summary) |
| · | `check_T_bottom_msbar_internal_inputs_allowed` | theorem | `—` | (no summary) |
| · | `check_T_bottom_msbar_metrics_have_both_pulls` | theorem | `—` | (no summary) |
| · | `check_T_bottom_msbar_msbar_scheme_named` | theorem | `—` | (no summary) |
| · | `check_T_bottom_msbar_next_gate_exact` | theorem | `—` | (no summary) |
| · | `check_T_bottom_msbar_no_smuggling_table_count` | theorem | `—` | (no summary) |
| · | `check_T_bottom_msbar_no_target_consumed` | theorem | `—` | (no summary) |
| · | `check_T_bottom_msbar_not_pole_like_certificate` | theorem | `—` | (no summary) |
| · | `check_T_bottom_msbar_open_stage_count` | theorem | `—` | (no summary) |
| · | `check_T_bottom_msbar_pass_status` | theorem | `—` | (no summary) |
| · | `check_T_bottom_msbar_payload_id_version` | theorem | `—` | (no summary) |
| · | `check_T_bottom_msbar_pdg_confidence_tracked` | theorem | `—` | (no summary) |
| · | `check_T_bottom_msbar_pdg_target_declared` | theorem | `—` | (no summary) |
| · | `check_T_bottom_msbar_physical_export_requires_all_prior` | theorem | `—` | (no summary) |
| · | `check_T_bottom_msbar_pole_context_present` | theorem | `—` | (no summary) |
| · | `check_T_bottom_msbar_pole_knockout_large` | theorem | `—` | (no summary) |
| · | `check_T_bottom_msbar_pole_residual_consistency` | theorem | `—` | (no summary) |
| · | `check_T_bottom_msbar_pull_90cl_rescaled` | theorem | `—` | (no summary) |
| · | `check_T_bottom_msbar_pull_quoted_scale` | theorem | `—` | (no summary) |
| · | `check_T_bottom_msbar_ratio_positive` | theorem | `—` | (no summary) |
| · | `check_T_bottom_msbar_relative_residual_small` | theorem | `—` | (no summary) |
| · | `check_T_bottom_msbar_report_digest` | theorem | `—` | (no summary) |
| · | `check_T_bottom_msbar_report_has_open_boundary` | theorem | `—` | (no summary) |
| · | `check_T_bottom_msbar_residual_consistency` | theorem | `—` | (no summary) |
| · | `check_T_bottom_msbar_residual_mev` | theorem | `—` | (no summary) |
| · | `check_T_bottom_msbar_route_requires_covariance` | theorem | `—` | (no summary) |
| · | `check_T_bottom_msbar_route_stage_count` | theorem | `—` | (no summary) |
| · | `check_T_bottom_msbar_safe_claims_only` | theorem | `—` | (no summary) |
| · | `check_T_bottom_msbar_target_is_comparison_only` | theorem | `—` | (no summary) |
| · | `check_T_bottom_msbar_terminal_report_tables` | theorem | `—` | (no summary) |
| · | `check_T_bottom_msbar_trace_anchor_imported` | theorem | `—` | (no summary) |
| · | `check_T_bottom_msbar_validation_not_export` | theorem | `—` | (no summary) |

## `apf/bottom_pole_obstruction_real_adapter.py` — 3 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_bottom_pole_obstruction_adapter_atlas_routes_P` | theorem | `—` | Atlas routes the Bottom-pole Route 6 payload to OBSTRUCTION_NAMED_CLOSURE. |
| · | `check_T_bottom_pole_obstruction_adapter_closure_kind_P` | theorem | `—` | Bottom-pole Route 6 obstruction adapter declares closure_kind=obstruction_named. |
| · | `check_T_bottom_pole_obstruction_adapter_no_smuggling_P` | theorem | `—` | Bottom-pole Route 6 obstruction adapter does not consume target pole-mass values. |

## `apf/capacity_coarse_grain_experiments.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_capacity_coarse_grain_experiments_P` | theorem | `—` | Capacity/coarse-graining experiments certify overspend relief and provenance boundaries. |

## `apf/carrier_trichotomy.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_carrier_trichotomy` | theorem | `—` | (no summary) |

## `apf/center_flux_exit.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `L_center_flux_exit` | lemma | `P_math | electric-basis model convention + per-vertex-singlet admissibility (Gauss reading a named identification) + H-hom as named hypothesis -- for the abstract Z_N law; enumeration legs and the baryon exhibit instance-scoped [P] at stated caps and walked graphs` | In the named oriented electric-basis lattice model (label r at head, conj(r) at tail -- flip-covariance computed; self-loops both-slots-own-vertex and never cut; multi-edges independent; boundary u... |

## `apf/cfts_red_team_audit.py` — 6 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `RT_bottom_anchor_not_opaque_literal` | red_team | `—` | (no summary) |
| · | `RT_codomain_discipline` | red_team | `—` | (no summary) |
| · | `RT_experimental_values_are_benchmarks_only` | red_team | `—` | (no summary) |
| · | `RT_no_inverse_inputs_all` | red_team | `—` | (no summary) |
| · | `RT_up_bridge_hypotheses_present` | red_team | `—` | (no summary) |
| · | `RT_uploaded_function_precedence` | red_team | `—` | (no summary) |

## `apf/charged_lepton_pole_real_adapter.py` — 5 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_charged_lepton_pole_adapter_certification_P` | theorem | `—` | EVALUATOR_MAP edge in ew movement graph resolves to MOVES_CLEANLY with charged_lepton_pole-filled payload. |
| · | `check_T_charged_lepton_pole_adapter_external_ledger_declared_P` | theorem | `—` | All 5 required external evaluator ledger fields declared on the charged_lepton_pole snapshot. |
| · | `check_T_charged_lepton_pole_adapter_no_smuggling_P` | theorem | `—` | No forbidden target-value key in charged_lepton_pole payload; target_value_consumed=False. |
| · | `check_T_charged_lepton_pole_adapter_payload_contract_P` | theorem | `—` | charged_lepton_pole adapter produces ew-shaped route payload with evaluator + codomain filled. |
| · | `check_T_charged_lepton_pole_real_adapter_P` | theorem | `—` | charged_lepton_pole real adapter wires banked evaluator content into Engine-readable route payload; EVALUATOR_MAP edge fills cleanly; no smuggling; external ledger declared. |

## `apf/charged_lepton_qed_real_adapter.py` — 7 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_charged_lepton_qed_adapter_certification_P` | theorem | `—` | EVALUATOR_MAP edge in EW movement graph resolves to MOVES_CLEANLY with v70-filled payload. |
| · | `check_T_charged_lepton_qed_adapter_evaluator_consistent_P` | theorem | `—` | v70 LO self-scale outputs match Phi_l^v43 / (1+alpha/pi) at CODATA 2022 alpha for all three leptons. |
| · | `check_T_charged_lepton_qed_adapter_external_ledger_declared_P` | theorem | `—` | All 9 required QED external evaluator ledger fields declared on the snapshot. |
| · | `check_T_charged_lepton_qed_adapter_no_smuggling_P` | theorem | `—` | No CODATA-pole-as-input or generation-residual-knob in payload; target_value_consumed=False. |
| · | `check_T_charged_lepton_qed_adapter_payload_contract_P` | theorem | `—` | Charged-lepton QED adapter produces EW-shaped route payload with v70-filled evaluator + codomain. |
| · | `check_T_charged_lepton_qed_multiloop_coefficient_ledger_P` | theorem | `—` | QED on-shell<->MSbar multi-loop lepton coefficients (MvR hep-ph/9912391, C_F=1/C_A=0/T_R=1): QCD self-check reproduces Eq.(12) (2-loop exact, 3-loop to rounding); per-lepton mbar_l(M_l) to 3 loops inside the v48 envelope; L>=2 external coefficients imported (full-running ledger closed). |
| · | `check_T_charged_lepton_qed_real_adapter_P` | theorem | `—` | Charged-lepton QED real adapter wires banked v70 LO self-scale evaluator + v48 covariance ledger into Engine-readable route payload; EVALUATOR_MAP edge fills cleanly; no smuggling (CODATA diagnostic-only + r_e/r_mu/r_tau forbidden); 9-field external ledger declared; v70 outputs match Phi_l/(1+alp... |

## `apf/charged_trace_spectrum.py` — 3 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_charged_fermion_apf_trace_spectrum` | theorem | `P_local | upstream-banking-ready` | (no summary) |
| · | `T_no_inverse_inputs_charged_trace` | theorem | `—` | (no summary) |
| · | `T_up_bridge_strengthened` | theorem | `P_local | upstream-banking-ready` | (no summary) |

## `apf/charm_msbar_rundec_real_adapter.py` — 6 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_charm_msbar_rundec_adapter_certification_P` | theorem | `—` | EVALUATOR_MAP edge in ew movement graph resolves to MOVES_CLEANLY with charm_msbar_rundec-filled payload. |
| · | `check_T_charm_msbar_rundec_adapter_evaluator_consistent_P` | theorem | `—` | v78 threshold-matched RunDec output matches published benchmark case m_c(m_c)=1.279 GeV -> m_c(3 GeV)=0.986 GeV within 1 MeV tolerance. |
| · | `check_T_charm_msbar_rundec_adapter_external_ledger_declared_P` | theorem | `—` | All 12 required external evaluator ledger fields declared on the charm_msbar_rundec snapshot. |
| · | `check_T_charm_msbar_rundec_adapter_no_smuggling_P` | theorem | `—` | No forbidden target-value key in charm_msbar_rundec payload; target_value_consumed=False. |
| · | `check_T_charm_msbar_rundec_adapter_payload_contract_P` | theorem | `—` | charm_msbar_rundec adapter produces ew-shaped route payload with evaluator + codomain filled. |
| · | `check_T_charm_msbar_rundec_real_adapter_P` | theorem | `—` | charm_msbar_rundec real adapter wires banked evaluator content into Engine-readable route payload; EVALUATOR_MAP edge fills cleanly; no smuggling; external ledger declared. |

## `apf/charm_pole_obstruction_real_adapter.py` — 3 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_charm_pole_obstruction_adapter_atlas_routes_P` | theorem | `—` | Atlas routes the charm-pole payload to OBSTRUCTION_NAMED_CLOSURE. |
| · | `check_T_charm_pole_obstruction_adapter_closure_kind_P` | theorem | `—` | Charm-pole obstruction adapter declares closure_kind=obstruction_named with named obstruction class. |
| · | `check_T_charm_pole_obstruction_adapter_no_smuggling_P` | theorem | `—` | Charm-pole obstruction adapter does not consume target pole-mass values. |

## `apf/claim_dispatcher_multi_engine.py` — 3 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_claim_dispatcher_codomain_regime_recognizer_P` | theorem | `P_codomain_regime_recognizer` | Codomain regime recognizer identifies all 7 coherent-phase regimes from representative claim text; non-coherent-phase claim returns None (no false positives). |
| · | `check_T_claim_dispatcher_meta_verdict_conjunctive_P` | theorem | `P_meta_verdict_conjunctive` | Meta-status composition is conjunctive per Reference doc Q1 option a: ALL_PASS iff every engine passes; ALL_OPEN iff every engine is open-evidence; PARTIAL_PASS for mixed pass+open/fail; ALL_FAIL iff every engine is fail-closed. |
| · | `check_T_claim_dispatcher_multi_engine_basic_P` | theorem | `P_claim_dispatcher_multi_engine_basic` | Multi-engine claim dispatcher operates end-to-end: SC claim text dispatches to both Route Adjudication and Codomain Selection engines; per-engine sub-verdicts produced; meta-status composed via conjunctive rule per Q1 option a. |

## `apf/claim_to_interface_graph_compiler.py` — 5 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_claim_obligation_packets_P` | theorem | `—` | Claim audits generate appropriate obligation packets or blocker statuses. |
| · | `check_T_claim_required_structures_P` | theorem | `—` | Compiled claims expose route-specific required interface structures. |
| · | `check_T_claim_route_classification_P` | theorem | `—` | Claim compiler classifies canonical prose claims into interface route classes. |
| · | `check_T_claim_text_not_evidence_P` | theorem | `—` | Global-export wording in claim text does not itself promote a route to P. |
| · | `check_T_claim_to_interface_graph_compiler_P` | theorem | `—` | Claim-to-Interface Graph Compiler is P: prose claims compile to conservative interface audits without treating text as evidence. |

## `apf/class_transition.py` — 5 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `L_per_slot_capacity_flow` | lemma | `—` | max RHS diff across grid = 0.00e+00 (Markov-breakdown reduction exact at machine precision) |
| · | `T_class_transition` | theorem | `—` | phi_monotone=True; phi_bounded=True; t_trans=1.1513 (finite=True); round_trip_cost=2.0 (irreversible=True) |
| · | `T_class_transition_completion` | theorem | `—` | t_trans = 1.151293 (formula=1.151293, match=True); boundary_zero=True; boundary_infty=True; independence_of_rel=True |
| · | `T_coherent_free_spend_permanent` | theorem | `P` | [P] composition over A1+occupancy (no [P_structural] in the gate): FREE = ledger_rent_excluded[P] (+ a held/non-resolving alignment does not complete) -> True; SPEND = L_irr[P] (resolution commits ... |
| · | `T_realignment_floor_is_epsilon_star` | theorem | `P_structural` | kappa_min == eps*_Gamma (structural identification): eps*_positive=True, MD_derived=True, transition_one_way=True, kappa_min=1.0 > 0 = True; per-module normalisations differ (identification is stru... |

## `apf/closed_world_completeness.py` — 14 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_adjoint_closure_reversible_lock_cycles` | theorem | `P_regime+P_math` | Reversible record-lock cycles -- sequences of record-locking operations that compose with their inverses to the identity -- induce an adjoint involution on the stable simple-sector family.  Closure of the family under this involution is what licenses the *-algebra structure on the operational quo... |
| · | `T_capacity_only_distinct_from_structural_ijc` | theorem | `P_structural_reading` | v5.97's anti-conflation theorem.  The framework refuses to call capacity-only failure 'quantumness'.  An interface can fail SepAdm (no admissible commuting defender within budget) while being SepStr (commuting defender exists in principle); on such interfaces QAC does NOT apply because QAC is gat... |
| · | `T_closed_ledger_reciprocity` | theorem | `P_regime+accounting` | Finite closed-world ledger conservation forces the prep and measurement cost vectors into a symmetric bilinear pairing B(p, m) = sum p_i m_i.  This pairing is precisely the operational content of the reciprocal-calibration gate: an adjoint of a prep functional is just its swap partner under B.  T... |
| · | `T_closed_read_write_self_duality` | theorem | `P_regime+accounting` | Closed read/write completeness elevates closed-ledger reciprocity to cone-level self-duality: the cone of valid preparation cost vectors equals the cone of valid measurement cost vectors as dual cones under the symmetric pairing.  This is the structural content of the adjoint operation on the rec... |
| · | `T_closed_world_completeness_derives_three_gates` | theorem | `P_structural_reading` | Headline meta-theorem of the v5.43+v5.45 reviewer-response unbundling: the three gates that an external auditor flagged as Barnum-Wilce/Hardy/CDP/Masanes-Mueller-class axioms are NOT independent postulates; they are joint consequences of a single deeper APF primitive -- closed-world ledger conser... |
| · | `T_constructive_commuting_realization` | theorem | `P_math` | v5.65's constructive upgrade replaces v5.55's existential 'a faithful commutative algebra exists' with an explicit construction: the power-set Boolean algebra 2^Q on the query family Q.  This makes the Wedderburn matrix-sector structure instantiable on the witness rather than left to a Hahn-Banac... |
| · | `T_gate_certified_hilbert_born_pipeline` | theorem | `P_structural_reading` | v5.65's gate-certified pipeline is the composite meta-theorem of the framework: the four closed-world-completeness gates -- positivity preservation, closed-ledger reciprocity, operational-radical-equals-Jacobson, split-composite-gates ℂ-selection -- jointly license the Hilbert-Born matrix-sector ... |
| · | `T_no_phantom_record_quotient` | theorem | `P_structural_reading` | Stable simple-record completeness is not a free Hardy-CDP perfect-distinguishability axiom; it is a consequence of the framework's insistence on enforceable distinctions.  Any element of the operational radical does no record-distinguishing work and can be quotiented away without losing the opera... |
| · | `T_operational_radical_equals_jacobson` | theorem | `P_structural_reading` | Under stable-simple completeness (the family Pi_st of stable simple sectors is exhaustive), the operational radical (intersection of stable simple kernels) coincides with the Jacobson radical (intersection of maximal-ideal kernels) of the finite record algebra.  The quotient is then a finite semi... |
| · | `T_positive_cone_quotient_compatible` | theorem | `P_math` | The positivity gate of the v5.97 gate-certified Hilbert-Born pipeline asserts that quotienting by the operational radical does not destroy the order structure on the finite record algebra.  Verified on the 2-dim witness: the cone is preserved under quotient and order-reflecting on canonical lifts... |
| · | `T_preservation_ijc_obstruction` | theorem | `P_regime` | An interface can be SepStr (structurally factorizable, some commuting defender exists in principle) yet IJCPres (no commuting preservation-respecting defender fits the finite capacity-and-distortion budget).  The v5.42 theorem certifies that this happens whenever every commuting candidate sits ab... |
| · | `T_split_closed_world_complex_selection` | theorem | `P_regime+P_math` | Composite meta-theorem of the v5.43 reviewer-response unbundling: 'APF-complete composite closure' is no longer a single black-box axiom.  It is the conjunction of two independently-derivable conditions -- finite tensor closure (rules out H structurally because M_n(H) (x)_R M_m(H) ~= M_{2nm}(R), ... |
| · | `T_split_composite_gates_tensor_closure` | theorem | `P_math` | First leg of the v5.43 split: APF-complete composite closure decomposes into (i) finite tensor closure + (ii) finite tomographic locality.  Leg (i) -- this check -- rules out the quaternions structurally: M_n(H) tensored over R with M_m(H) is real-dimensional 4 n^2 m^2, while a hypothetical quate... |
| · | `T_split_composite_gates_tomographic_locality` | theorem | `P_math` | Second leg of the v5.43 split: finite tomographic locality, the Wootters-Hardy condition that joint state-space dimension factorizes as local marginals + bipartite correlations.  Only C-QM passes this test in the canonical 2x2 setting: dim 15 = 3 + 3 + 9.  R-QM has dim 10 < 15 (local-only effects... |

## `apf/cmb_finite_mode_covariance.py` — 6 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_cmb_fm_finite_multipliers` | theorem | `P_structural_reading` | 29 multipliers finite=True in [0,2]=True |
| · | `T_cmb_fm_high_ell_preservation` | theorem | `P_structural_reading` | max \|m_ell - 1\| for ell>=20: 0.0171 (preserved=True) |
| · | `T_cmb_fm_large_angle_reduction` | theorem | `P_structural_reading` | S_proj/S_std = 0.00138301 (reduced=True) |
| · | `T_cmb_fm_legendre_recurrence` | theorem | `P_structural_reading` | max \|Bonnet residual\| at x=0.3: 4.441e-16 (tol=1e-12) |
| · | `T_cmb_fm_nonneg_reference` | theorem | `P_structural_reading` | a_ell min=27.33 max=833.3 |
| · | `T_cmb_fm_quadrupole_suppression` | theorem | `P_structural_reading` | m_2 = 0.1021 (target < 0.5; suppressed=True) |

## `apf/codef_aggregation.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `L_codef_aggregation_argmin` | lemma | `—` | (no summary) |

## `apf/codomain_selection_engine.py` — 3 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_codomain_selection_engine_audit_first_P` | theorem | `P_engine_audit_first` | Audit-first discipline preserved across all 8 verdict cases: numeric_critical_temperature / material_specific_prediction / highTc_solved / ab_initio_chemistry all = 0 in every export; no obligation packet smuggles target. |
| · | `check_T_codomain_selection_engine_entry_point_P` | theorem | `P_engine_entry_point` | Engine entry point produces correct verdict status across 5 cases: SC positive -> COHERENT_CODOMAIN_SELECTED with positive margin; SC overloaded -> MARGIN_NONPOSITIVE; SF positive -> COHERENT_CODOMAIN_SELECTED via registry-driven dispatch; MAGNETISM with no network -> OPEN_EVIDENCE_REQUIRED with ... |
| · | `check_T_codomain_selection_engine_identity_P` | theorem | `P_engine_identity` | Codomain Selection Engine declares correct Tier 2 role + IE family membership; 7 regimes registered, all 7 runtime-available (SUPERCONDUCTIVITY + SUPERFLUIDITY + MAGNETISM + BOSE_EINSTEIN_CONDENSATION + LASER_COHERENCE + SYNCHRONIZATION + TOPOLOGICAL_ORDER); coherent-phase family complete; 4 pres... |

## `apf/codomain_transport_schema.py` — 8 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_codomain_transport_certificates_well_formed` | theorem | `P_structural_instrument` | Certificate shape uniform across 16 instances. |
| · | `T_codomain_transport_forbidden_inputs_declared` | theorem | `P_structural_instrument` | No-smuggling discipline structurally enforced across all 16 instances. |
| · | `T_codomain_transport_instances_registered` | theorem | `P_structural_instrument` | Every currently-known open frontier instantiated as a transport object. |
| · | `T_codomain_transport_no_smuggling_consistent` | theorem | `P_structural_instrument` | No-smuggling consistency: status / certificate / export-lock triangle uniform. |
| · | `T_codomain_transport_schema_declared` | theorem | `P_structural_instrument` | CodomainTransport + TransportCertificate schema bank-callable. |
| · | `T_codomain_transport_status_classification` | theorem | `P_structural_instrument` | Status classification matches the reference doc exactly. |
| · | `T_codomain_transport_unification` | theorem | `P_structural_instrument` | Master unification theorem: the framework discovers a unified schema for its open frontier. |
| · | `T_codomain_type_declared` | theorem | `P_structural_instrument` | codomain_type declared on all 17 transports: 16 numerical + 1 structural |

## `apf/colour_solder_form_no_go.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_colour_solder_form_no_go` | theorem | `P_structural` | Under P1 (closed-world inventory) + P2 (payload-type/content-blindness reading, DISCLOSED at reading strength, the heavy premise) + P3 (canonicity = equivariance): no canonical map from base-supplied data into the PU(3) identification torsor exists -- the image would be a fixed point of a free no... |

## `apf/commutative_no_unresolved_hold.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `L_commutative_no_unresolved_hold` | lemma | `P_math` | commutative projector algebra: (i) pure states are {0,1} assignments; (ii) A-dephasing D(rho)=sum Q_pi rho Q_pi is invariant on the algebra (hold invisible); (iii) any distinguishing observable is ... |

## `apf/confinement_scale_single_anchor.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_confinement_scale_rides_single_anchor` | theorem | `P_structural_seam` | Closes the single-anchor theorem (v24.3.187) open [C] corollary, using machinery already banked. L_alpha_s ([P+alpha_EM]) fixes alpha_s(M_Z) from capacity structure (Route A fully-native 0.1197 / 1.6%, Route B 0.1179 / 0.02%) and computes the confinement scale by dimensional transmutation Lambda_... |

## `apf/continuation_calculus.py` — 5 checks (3 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_admissibility_greedoid_structure` | theorem | `—` | (no summary) |
| ✓ | `T_finite_minimal_joint_realization_atom_cover` | theorem | `—` | (no summary) |
| ✓ | `T_finite_operational_basis` | theorem | `—` | (no summary) |
| ✓ | `T_finite_operational_basis_scope_contract` | theorem | `P_structural_instrument` | The finite-basis bank node is scoped to a finite atom-cover model: finite content atoms, subset-coded operational classes, union closure/joint carrier, and exact no-excess atom cost. Exact Fraction arithmetic rejects the former +1e-9 boundary enlargement. A finite closed-ledger countermodel with ... |
| · | `T_selection_approximate_A2` | theorem | `—` | (no summary) |

## `apf/continuation_sum_measure.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_continuation_sum_measure_native_from_D4` | theorem | `P_structural_continuation_sum_measure_native_from_D4_modulo_convention` | First genuinely-native bankable result of the EW→distinction-geometry pivot (2026-05-28). The physical content of a loop is the substrate's sum over admissible held continuations; its universal measure factor is derived here from native primitives. (1) Measure theorem: the angular volume of conti... |

## `apf/cosmogenesis_t1_t4_quartet_real_adapter.py` — 3 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_cosmogenesis_t1_t4_quartet_adapter_atlas_routes_P` | theorem | `—` | Atlas routes cosmogenesis T1-T4 quartet payload to INTERNAL_IDENTITY_GLOBAL_P. |
| · | `check_T_cosmogenesis_t1_t4_quartet_adapter_closure_kind_P` | theorem | `—` | cosmogenesis T1-T4 quartet adapter declares closure_kind=internal_identity (framework structural export). |
| · | `check_T_cosmogenesis_t1_t4_quartet_adapter_registry_pointer_P` | theorem | `—` | cosmogenesis T1-T4 quartet adapter cites registry pointer. |

## `apf/cost_energy_identity.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_realignment_cost_is_transition_energy` | theorem | `P` | Removes the cited dictionary premise from the ep* / Yang-Mills bridge at the substrate level. L_cost [P] gives realignment cost C = n*eps; L_beta_temp [P] (beta = DeltaS/DeltaE = ln(d)/eps, Step 3 DeltaE = eps per unit) gives transition energy = n*eps; T_epsilon [P] fixes the per-unit quantum. Th... |

## `apf/critical_slack.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_critical_mean_field` | theorem | `[P_structural]` | Mean-field slack equation Δ*_SSA(1+δ) = C(1+δ)/(2+δ) at saturation. Linear-order Taylor expansion Δ ≈ C/2 + (C/4)·δ + O(δ²) gives β = γ = 1 mean-field exponents.  Single scalar deformation δ moves the system off the critical slack with linear-order asymmetry, confirming codimension-1 character (P... |

## `apf/crystal.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_crystal_v69_consistent` | theorem | `—` | (no summary) |

## `apf/crystal_metrics.py` — 6 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_crystal_cascade_v69` | theorem | `—` | (no summary) |
| · | `T_crystal_centrality_v69` | theorem | `—` | (no summary) |
| · | `T_crystal_convergence_v69` | theorem | `—` | (no summary) |
| · | `T_crystal_min_cut_v69` | theorem | `—` | (no summary) |
| · | `T_crystal_path_attribution_scc_v69` | theorem | `—` | (no summary) |
| · | `T_crystal_path_attribution_v69` | theorem | `—` | (no summary) |

## `apf/dark_apf2_real_adapter.py` — 6 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_dark_apf2_adapter_certification_P` | theorem | `—` | Dark APF2 adapter produces HONEST Engine reading: route at OPEN_EVIDENCE_REQUIRED with critical_fields naming posterior + robustness; EMPIRICAL_POSTERIOR edge MISSING; CODOMAIN_TRANSPORT + ACC_RECORD edges clean. Smoke != posterior preserved structurally. |
| · | `check_T_dark_apf2_adapter_external_ledger_declared_P` | theorem | `—` | All 9 required APF2 smoke external evaluator ledger fields declared on the snapshot. |
| · | `check_T_dark_apf2_adapter_no_smuggling_P` | theorem | `—` | No measured (w_0, w_a) key in payload; APF2 coefficients frozen at -58/61, -16/61; rational coefficients structurally derived at LATEST-62. |
| · | `check_T_dark_apf2_adapter_payload_contract_P` | theorem | `—` | Dark APF2 adapter produces dark-shaped payload with smoke-filled evaluator + no-refit guard. |
| · | `check_T_dark_apf2_adapter_smoke_outputs_finite_P` | theorem | `—` | Smoke logpost = -6565.54 and all 5 per-likelihood loglikes finite at APF2 frozen point. |
| · | `check_T_dark_apf2_real_adapter_P` | theorem | `—` | Dark APF2 real adapter wires banked Campaign A smoke output into Engine-readable dark route payload. Engine produces HONEST typing of the route at OPEN_EVIDENCE_REQUIRED with critical_fields = (posterior_closed, robustness_checks_passed); EMPIRICAL_POSTERIOR edge MISSING; CODOMAIN_TRANSPORT + ACC... |

## `apf/dark_empirical_posterior_admission_contract.py` — 5 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_dark_empirical_posterior_admission_contract_P` | theorem | `APF_DARK_EMPIRICAL_POSTERIOR_ADMISSION_CONTRACT_v1` | (no summary) |
| · | `check_T_posterior_contract_evaluator_admission_separated` | theorem | `APF_DARK_EMPIRICAL_POSTERIOR_ADMISSION_CONTRACT_v1` | (no summary) |
| · | `check_T_posterior_contract_no_smuggling_guard` | theorem | `APF_DARK_EMPIRICAL_POSTERIOR_ADMISSION_CONTRACT_v1` | (no summary) |
| · | `check_T_posterior_contract_preserves_nonclaims` | theorem | `APF_DARK_EMPIRICAL_POSTERIOR_ADMISSION_CONTRACT_v1` | (no summary) |
| · | `check_T_posterior_contract_required_slots_declared` | theorem | `APF_DARK_EMPIRICAL_POSTERIOR_ADMISSION_CONTRACT_v1` | (no summary) |

## `apf/dark_mcmc_posterior_lane_admission.py` — 8 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_mcmc_diagnostics_thresholds_declared` | other | `—` | (no summary) |
| · | `check_mcmc_lane_contract_identity` | other | `—` | (no summary) |
| · | `check_mcmc_lane_grid_complete` | other | `—` | (no summary) |
| · | `check_mcmc_lane_parameter_lockstep` | other | `—` | (no summary) |
| · | `check_mcmc_result_stub_fails_closed_on_partial_chain` | other | `—` | (no summary) |
| · | `check_partial_chain_not_posterior_guard` | other | `—` | (no summary) |
| · | `check_posterior_coordinates_by_model` | other | `—` | (no summary) |
| · | `check_profile_best_not_posterior_MAP_guard` | other | `—` | (no summary) |

## `apf/dark_modified_gravity_obstruction_real_adapter.py` — 3 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_dark_modified_gravity_obstruction_adapter_atlas_routes_P` | theorem | `—` | Atlas routes dark modified gravity payload to OBSTRUCTION_NAMED_CLOSURE. |
| · | `check_T_dark_modified_gravity_obstruction_adapter_closure_kind_P` | theorem | `—` | dark modified gravity obstruction adapter declares closure_kind=obstruction_named. |
| · | `check_T_dark_modified_gravity_obstruction_adapter_registry_pointer_P` | theorem | `—` | dark modified gravity adapter cites registry pointer. |

## `apf/dark_particle_id_obstruction_real_adapter.py` — 3 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_dark_particle_id_obstruction_adapter_atlas_routes_P` | theorem | `—` | Atlas routes dark particle ID payload to OBSTRUCTION_NAMED_CLOSURE. |
| · | `check_T_dark_particle_id_obstruction_adapter_closure_kind_P` | theorem | `—` | dark particle ID obstruction adapter declares closure_kind=obstruction_named. |
| · | `check_T_dark_particle_id_obstruction_adapter_registry_pointer_P` | theorem | `—` | dark particle ID adapter cites registry pointer. |

## `apf/dark_posterior_certifier.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_dark_posterior_certifier_P` | theorem | `—` | Dark-sector posterior certifier separates runtime success from posterior/global P closure. |

## `apf/dark_posterior_real_adapter.py` — 5 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_dark_adapter_certification_P` | theorem | `—` | Dark adapter reports feed the interface-intelligence stack with expected held/P/fail-closed statuses. |
| · | `check_T_dark_adapter_live_probe_safe_P` | theorem | `—` | Live dark-probe mode is safe in partial/standalone environments and defaults to no target consumption. |
| · | `check_T_dark_adapter_no_evidence_no_patch_P` | theorem | `—` | Dark adapter does not patch/rerun without completed evidence obligations. |
| · | `check_T_dark_adapter_payload_contract_P` | theorem | `—` | Dark real adapter emits the standard dark posterior/run route payload contract. |
| · | `check_T_dark_posterior_real_adapter_P` | theorem | `—` | Dark Posterior Real Adapter is P: live/manual dark route state converts into payloads, certifications, obligations, and safe rerun gating. |

## `apf/dark_profile_likelihood_lane_admission.py` — 6 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_profile_best_not_posterior_guard` | other | `—` | (no summary) |
| · | `check_profile_likelihood_lane_contract_identity` | other | `—` | (no summary) |
| · | `check_profile_likelihood_lane_grid_complete` | other | `—` | (no summary) |
| · | `check_profile_likelihood_lane_parameter_lockstep` | other | `—` | (no summary) |
| · | `check_profile_probe_not_full_scan_guard` | other | `—` | (no summary) |
| · | `check_profile_result_stub_fails_closed_on_placeholder` | other | `—` | (no summary) |

## `apf/dark_profile_mcmc_shared_contract.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_dark_profile_mcmc_shared_runtime_contract_P` | theorem | `contract-only-no-empirical-promotion` | INTERFACE_DARK_PROFILE_MCMC_SHARED_CONTRACT_PASS |

## `apf/dark_w2_a_background_real_adapter.py` — 3 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_dark_w2_a_background_adapter_atlas_routes_P` | theorem | `—` | Atlas routes dark w2(a) background payload to INTERNAL_IDENTITY_GLOBAL_P. |
| · | `check_T_dark_w2_a_background_adapter_closure_kind_P` | theorem | `—` | dark w2(a) background adapter declares closure_kind=internal_identity (APF2 structural derivation). |
| · | `check_T_dark_w2_a_background_adapter_structural_only_P` | theorem | `—` | dark w2(a) adapter promotes only structural derivation; separate empirical-promotion gates (DESI full-shape, MCMC convergence, NERSC reproduction) remain HELD_FOR_REPAIR via their own atlas inputs. |

## `apf/defect_calculus_engine.py` — 3 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_defect_calculus_engine_audit_first_P` | theorem | `P_defect_calculus_engine_audit_first` | Audit-first discipline preserved across all verdict cases: target_value_consumed + new_physical_claim + infinity_stack_claim all = 0; no engine smuggling. |
| · | `check_T_defect_calculus_engine_entry_point_P` | theorem | `P_defect_calculus_engine_entry_point` | Entry point produces correct verdicts: no-patches + empty-patches both yield OPEN_EVIDENCE_REQUIRED with patches_missing critical field and target_engine declared correctly. |
| · | `check_T_defect_calculus_engine_identity_P` | theorem | `P_defect_calculus_engine_identity` | Defect Calculus Engine declares Tier 2 role + IE family membership; 6-status verdict taxonomy + 3 preserved non-claims. |

## `apf/delta_alpha_adler_m_z.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_delta_alpha_had_adler_pqcd_first_principles` | theorem | `P_perturbative_QCD_M_Z_first_principles_Adler` | Second APF-banked first-principles slice of Delta alpha_had(M_Z) via Euclidean Adler-function route. Inputs: m_c(m_c)=1.279, m_b(m_b)=4.18, alpha_s(M_Z)=0.1189, Theorem_R charges, N_c=3, M_Z=91.1876, Adler coefficients (1.0, 1.64, 6.37). Q_match = 2 m_c = 2.558 GeV (matched to v24.3.118 Lambda_ma... |

## `apf/delta_alpha_capacity_density.py` — 2 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_dalpha_had_threshold_quantum_number_forced` | theorem | `P_structural_seam` | The hadronic vacuum polarization admits only J^PC=1^{--} intermediate states; single-pi (0^{-+}) is C-forbidden, so the lightest qualifying hadronic distinction is the pi+pi- P-wave and the continuum opens at s=4 m_pi^2 BY SELECTION RULE. m_pi rides Lambda_QCD rides the single Planck anchor, so t... |
| · | `T_delta_alpha_capacity_counted_distinction_density` | theorem | `P_structural_seam` | APF-native reformulation: Delta-alpha = (alpha/3pi) sum_f N_c^f Q_f^2 [ln(M_Z^2/m_f^2) - 5/3], the accumulation of the capacity-counted distinction density R = N_c*sum Q^2 (N_c the colour capacity forced for the EW carrier; sum Q^2 the charge-weighted distinction modes). VALIDATED EXACTLY on the ... |

## `apf/delta_alpha_leptonic.py` — 5 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `L_delta_alpha_hadronic_external_open` | lemma | `C` | Delta alpha_had = 0.02766 (46.9% of the total Delta alpha) is a dispersion integral over e+e- -> hadrons -- data-bound, the same object that limits the muon g-2 prediction. It is NOT first-principles and is NOT internalized; it is the single named open gate of the alpha-running sector. Export fla... |
| · | `L_delta_alpha_leptonic_masses_banked` | lemma | `P` | The three lepton masses feeding Delta alpha_lep are the APF-banked charged-lepton pole masses (charged_lepton_pole_real_adapter .POLE_MASS_MEV: e 0.5110026, mu 105.658244, tau 1776.916832 MeV), value-pinned. No measured/PDG lepton mass is consumed as an independent input; the running is fixed by ... |
| · | `T_delta_alpha_had_principled_external_universal_QCD` | theorem | `C_principled_external_universal_QCD_difficulty` | Naive perturbative quark skeleton (banked MS-bar masses at mixed self-scales, not run to M_Z): Delta alpha_q^pert^naive(M_Z) = 0.03631, overshooting Delta alpha_had_dispersion = 0.02766 by 31.3%. The overshoot IS the non-perturbative hadronic resonance physics below ~1.5 GeV that quarks-as-curren... |
| · | `T_delta_alpha_leptonic_first_principles` | theorem | `P` | Delta alpha_lep(M_Z) = sum_l (alpha_0/3pi)[ln(M_Z^2/m_l^2) - 5/3] = 0.0314209 (one-loop), from the APF-banked charged-lepton pole masses (e 0.017435 + mu 0.009178 + tau 0.004808). Reproduces the known precise (three-loop) leptonic value 0.0314977 to -0.24% at one loop; the gap is higher-order lep... |
| · | `T_delta_alpha_total_decomposition` | theorem | `P_structural_seam` | Delta alpha(M_Z) = 0.059011 = leptonic 0.031421 (53.2%, first-principles) + hadronic 0.02766 (46.9%, data-bound) + top -7e-05. The leptonic share is first-principles from the banked masses; the total is NOT first-principles (it carries the external hadronic dispersion input). |

## `apf/delta_alpha_pqcd_m_z.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_delta_alpha_had_pqcd_above_lambda_match_first_principles` | theorem | `P_perturbative_QCD_M_Z_first_principles` | First APF-banked first-principles slice of Delta alpha_had(M_Z): the perturbative-above-threshold piece via Candidate A dispersion-threshold pQCD. Inputs: m_c(m_c)=1.279, m_b(m_b)=4.18, alpha_s(M_Z)=0.1189, Theorem_R charges, N_c=3, M_Z=91.1876. Lambda_match = 2 m_c = 2.558 GeV (banked self-scale... |

## `apf/delta_calculus.py` — 7 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_cost_count_characterization` | theorem | `P` | CHARACTERIZATION: any kappa satisfying X1 count-dependence (L_cost_C1 [P] + FD1-sc [P] adopted-foundational), X2 additivity over anchor-disjoint families (L_cost_C2 = T_M(<=) + L_loc [P]; executable T_delta_disjoint_additivity), and X3 the MD floor f(1) = eps > 0 (L_epsilon* [P]) equals kappa(S) ... |
| · | `check_T_delta_JR_derived` | theorem | `P` | THE DERIVED COUNTING IDENTITY (Paper 12 round-6 walk C1, reviewer Q2). A presented interface carries a channel ledger (billed channels with nonempty supports -- CH3, a definitional axiom, not a lemma); under CH1 (activation monotonicity -- TYPED as a definitional clause of the join operation unde... |
| · | `check_T_delta_chain_rule_conditional_expectation_dichotomy` | theorem | `P` | THE CHAIN-RULE DICHOTOMY FOR PRESENTED COARSE FAMILIES (Paper 12 round-6 walk C2, reviewer Q9). A conditional expectation E_B onto a subalgebra of the record algebra has no ledger referent by itself; it enters through a PRESENTATION (generating coarse channels billed at their dependency supports ... |
| · | `check_T_delta_coarse_graining_monotonicity` | theorem | `P` | Clause B [P]: kappa is subset-monotone (L3, T_canonical Part I; L_irr structural core (i), occupancy-free), verified exhaustively. Clause D no-go [P]: Delta is NOT monotone under record-subset coarse-graining -- finite counterexamples in BOTH directions on world W1 (0 -> +eps deleting the reducib... |
| · | `check_T_delta_disjoint_additivity` | theorem | `P` | If anc(D1) ^ anc(D2) = empty then kappa(D1 \|_\| D2) = kappa(D1) + kappa(D2), i.e. Delta = 0 -- EQUALITY, not an inequality. Step 1: anchor-disjointness gives independence (T_M steps 1-3, the <= direction of the biconditional), and an irreducibly-joint distinction across the pair is a correlation n... |
| · | `check_T_delta_not_an_information_functional` | theorem | `P` | Under the NAMED readout-pushforward bridge (the pushforward of the uniform measure on Omega(D1 v D2) through the two families' readout maps -- a comparison device defined in-check, the NC1/NC2 epistemic shape; the framework nowhere asserts that records have outcome statistics), Delta is provably ... |
| · | `check_T_register_reading_grounds_ceil_log2_count` | theorem | `P_structural_reading` | THE REGISTER OPERATIONALIZATION (Paper 12 round-5 walk B2). Storage theorem, exact: the minimal FAITHFUL protected register for a d-ary irreducible fusion record is exactly ceil(log2 d) two-valued cells -- FAITHFUL defined as perfectly-distinguishable storage (orthogonal states in the quantum cas... |

## `apf/delta_rho_leading_distinction.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_delta_rho_leading_custodial_from_distinction` | theorem | `P_structural_delta_rho_leading_custodial_from_distinction_modulo_scale_and_convention` | Completes the Δρ-from-distinction rung the continuation-sum keystone (v24.3.166) unlocked. Δρ measures custodial breaking = the substrate holding the t,b doublet members at unequal cost. The leading custodial response composes three native factors: the color distinction-count N_c (apf.gauge); the... |

## `apf/descent_exactness.py` — 9 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_descent_exactness_theorem_P` | theorem | `—` | Descent exactness holds: globally admissible physical structure is exactly ker(Obs)=im(Globalization). |
| · | `check_T_exactness_im_equals_kernel_P` | theorem | `—` | Exactness holds at local representations: im(Globalization)=ker(Obs). |
| · | `check_T_failure_classes_outside_kernel_P` | theorem | `—` | C*, scheme, contextuality, capacity, provenance, and codomain failures lie outside the exact kernel. |
| · | `check_T_globalization_map_defined_P` | theorem | `—` | Globalization/restriction map from global APF structures to local descent classes is defined. |
| · | `check_T_image_globalization_identified_P` | theorem | `—` | Image of the globalization map is identified in the local representation descent classes. |
| · | `check_T_kernel_obstruction_identified_P` | theorem | `—` | Kernel of the obstruction map is the set of zero-obstruction local descent classes. |
| · | `check_T_no_long_exact_sequence_overclaim_P` | theorem | `—` | Scope boundary preserved: exactness is finite im=ker exactness, not a claimed long exact cohomology sequence. |
| · | `check_T_obstruction_map_defined_P` | theorem | `—` | Obstruction map from local descent classes to obstruction objects is defined. |
| · | `check_T_zero_obstruction_exact_part_is_global_physics_P` | theorem | `—` | Global physics is the exact/zero-obstruction part of local representation descent. |

## `apf/descent_obstruction_calculus.py` — 10 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_Cstar_obstruction_schema_P` | theorem | `—` | Flat global C*-unification fails by complex-action, norm, reversal, and codomain obstructions. |
| · | `check_T_capacity_and_provenance_obstruction_schemas_P` | theorem | `—` | Capacity overspend and provenance smuggling are obstruction-calculus failure modes. |
| · | `check_T_contextuality_obstruction_schema_P` | theorem | `—` | Contextuality/incompatible local descriptions are modeled as overlap-incoherence descent obstruction. |
| · | `check_T_descent_obstruction_calculus_P` | theorem | `—` | APF descent obstruction calculus is P: zero obstruction iff descent, with classified failure channels. |
| · | `check_T_descent_obstruction_zero_iff_P` | theorem | `—` | Finite descent succeeds if and only if the obstruction object is zero. |
| · | `check_T_local_obstruction_map_P` | theorem | `—` | Local obstruction map detects capacity, provenance, and codomain failures while accepting clean ACC data. |
| · | `check_T_no_cohomology_overclaim_P` | theorem | `—` | Scope boundary preserved: obstruction object is a finite channel monoid, not a claimed cohomology theory. |
| · | `check_T_obstruction_class_coverage_P` | theorem | `—` | Worked examples exercise the known obstruction channels needed for current APF descent failures. |
| · | `check_T_obstruction_object_monoid_P` | theorem | `—` | Obstruction objects form a finite idempotent commutative monoid under channel union. |
| · | `check_T_scheme_obstruction_schema_P` | theorem | `—` | Scheme/evaluator dependence fails substrate-global descent by evaluator and codomain obstructions. |

## `apf/down_lepton_trace.py` — 4 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `L_bottom_apf_trace` | lemma | `P_local` | m_b^APF_TRACE = 4.1774904559270665 GeV |
| · | `L_residual_down_normalizer_local` | lemma | `P_local` | After color-interface residual quotient, d_R^c is the selected down residual channel and F1(d_R^c)=1. |
| · | `T_down_lepton_apf_trace_vector` | theorem | `P_local` | (no summary) |
| · | `T_no_inverse_inputs_down_lepton_trace` | theorem | `—` | Declared down/lepton APF_TRACE construction uses no observed masses or target-fit physical scheme masses as inputs. |

## `apf/drawn_content_readings.py` — 6 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_drawn_content_readings_functional` | theorem | `—` | (no summary) |
| · | `T_gluonic_content_readings` | theorem | `P_structural_instrument` | PASS |
| · | `T_lr_divisibility_extended_scan` | theorem | `P_structural_instrument` | LR-divisibility extended scan: zero firers to 13x-600x the .334 bounds; mod-12 DP validated against commutant_profile; detector negative-tested; the open stays open |
| · | `T_magic_square_solution_group_rep_forces_4n` | theorem | `P_structural_instrument` | PASS |
| · | `T_reading_coverage_sweep` | theorem | `P_structural_instrument` | PASS |
| · | `T_sm_interface_generation_qutrit_readings` | theorem | `P_structural_instrument` | PASS |

## `apf/ec_inventory_reading.py` — 2 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `L_EC_inventory_reading` | lemma | `P_structural_reading` | THE EC INVENTORY READING, reading-graded: EC (label-injectivity of the kinematic inventory) holds under R-EC-inv (kinematic type-inventory completeness: type-distinctness is exhausted by counted la... |
| · | `L_F6_not_from_EC` | lemma | `P` | EC-LABEL-INJECTIVITY AND F6 ARE LOGICALLY INDEPENDENT, computed exactly over the declared check_T_field Phase-1 scan space (4,680 ordered / 1,680 distinct; full anomaly system solved over the ratio... |

## `apf/evaporation_e1_e4_quartet_real_adapter.py` — 3 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_evaporation_e1_e4_quartet_adapter_atlas_routes_P` | theorem | `—` | Atlas routes evaporation E1-E4 quartet payload to INTERNAL_IDENTITY_GLOBAL_P. |
| · | `check_T_evaporation_e1_e4_quartet_adapter_closure_kind_P` | theorem | `—` | evaporation E1-E4 quartet adapter declares closure_kind=internal_identity (framework structural export). |
| · | `check_T_evaporation_e1_e4_quartet_adapter_registry_pointer_P` | theorem | `—` | evaporation E1-E4 quartet adapter cites registry pointer. |

## `apf/evaporation_microtransport.py` — 20 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_C_evaporation_open_frontier_fence` | other | `—` | Open-frontier fence: six Tier-C evaporation gates remain OPEN and unpromoted (unique scrambling Hamiltonian, explicit physical decoder, physical endpoint phase, universal mode-by-mode micro-S-matrix, derive-islands-from-APF-alone, full amplitude completion). No fake-P promotions. Conjecture-class... |
| · | `check_G_DEC_CRIT_rank_gram_preserving` | other | `—` | Decoder admissibility CRITERION (not a construction): a horizon->radiation decoder is APF-admissible iff it preserves rank, continuation-separation pairing, the four record roles, and has no hidden-remnant dependence. Witness: rank-2 Gram-preserving embedding into C^4, gram_err=0.00e+00. |
| · | `check_G_DIL_ledger_transport_to_unitary_dilation` | other | `—` | Any rank+pairing-preserving ledger transport (isometry V, V^dag V = I) extends to a unitary U on an enlarged finite space agreeing with V on the admissible input sector (Stinespring/basis completion). Witness C^2->C^3, U=I_3. |
| · | `check_G_END_UNIT_endpoint_isometry` | other | `—` | Any endpoint operation Phi_end on the APF physical sector must preserve the continuation-separation pairing: Phi_end^dag Phi_end = I (or a declared isometry into a larger final codomain), else two enforceable distinctions change norm/lose separation. Witness: Phi=I, err=0.00e+00. |
| · | `check_G_FACT_typed_factorization_schema` | other | `—` | A typed amplitude map decomposes into role-labeled operators S = Phi.R.K.B.G.A (thermal/filter/backreaction/scramble/reconstruct/phase) by well-typed composition. BOOKKEEPING theorem only: it does NOT derive the factors' physical values. |
| · | `check_G_GREY_ROLE_beamsplitter` | other | `—` | A greybody transmission factor G in [0,1] embeds in a unitary beam-splitter (transmitted + reflected channels); norm is preserved when both channels are kept. Erasure appears ONLY if the reflected/complement channel is discarded. worst_err=2.22e-16 over G in {0,.25,.5,.75,1}. |
| · | `check_G_ISL_island_instantiation` | other | `—` | Conditional on an imported island/entanglement-wedge reconstruction regime (Penington 2019; replica wormholes), the APF S-map is instantiated on the code subspace via a rank+pairing-preserving decoder. Islands are IMPORTED, NOT derived from APF. |
| · | `check_G_NONPROD_backreaction_nonproduct` | other | `—` | If emission probability depends on a horizon-ledger state that backreacts (M_{n+1}=M_n-omega_n), the joint radiation history does not factor into independent one-emission marginals. Witness: P_cond(1,1)=0.125 != P_fixed_product=0.0625. |
| · | `check_G_SCHW_BR_backreaction_kernel` | other | `—` | Backreaction kernel: +4 pi G omega^2 correction (non-thermal); sequential Delta S telescope to the total (state function); Page-rank turnover at N0/2 by rank equipartition. Conditional on the Schwarzschild ledger regime. |
| · | `check_G_SCHW_THETA_thermal_weight_form` | other | `—` | p(omega\|M) ~ exp(Delta S_H), Delta S_H = -8 pi G M omega + 4 pi G omega^2 from the banked horizon-ledger entropy S=4 pi G M^2; leading order recovers beta_H = 8 pi G M. Conditional on the Schwarzschild ledger regime + area law; not an independent re-derivation of Hawking's QFT calculation. |
| · | `check_G_UNIT_amplitude_unitarity` | other | `—` | On the APF physical/enforceable sector the amplitude matrix satisfies sum_alpha A*_{alpha beta} A_{alpha gamma} = delta_{beta gamma}, i.e. S^dag S = I. Witness: Hadamard, err=2.22e-16. |
| · | `check_G_import_certify_contract_guards` | other | `—` | E3 import-certify discipline: greybody + decoder are typed contracts (derived_from_APF=False) with no-promotion guards all 0; numeric greybody table + decoder map stay [C] until externally imported and integrity-passed; islands NOT derived from APF (Penington 2019 / replica wormholes cited as ext... |
| · | `check_T_apf_physical_quotient` | theorem | `—` | APF physical quotient: H_phys = H_formal/ker(Q); Q Q^dag = I_phys; the full formal-to-radiation map S.Q is NON-unitary on the formal space (by design) while the physical-quotient-sector map is isometric. Unitarity holds BY CONSTRUCTION over enforceable distinctions only. STANCE, not a dynamical H... |
| · | `check_T_apf_species_threshold_registry` | theorem | `—` | Banked APF top-normalized mass ratios wire into the kinematic threshold rule varpi_i = 2 Mhat (m_i/m_top), giving a per-species threshold-availability table + evaluator-status registry. APF ratios internal; absolute scale via external top/Planck anchor (marked external). NO laundering: every ferm... |
| · | `check_T_endpoint_admissibility_exhaustion` | theorem | `—` | Planckian endpoint reframed as continuation-rank exhaustion: under the banked ledger-count law N_H=A/(4 l_P^2), horizon rank transfers monotonically to the exterior radiation ledger (total conserved) and at N_H=0 must be fully exported or explicitly re-coded -- no silent endpoint sink. STRUCTURAL... |
| · | `check_T_endpoint_identity_completion` | theorem | `—` | Endpoint identity-completion stance: IF full ledger export precedes the final horizon-capacity step THEN Phi_end = I_phys (canonical isometry), so no further endpoint destruction of enforceable distinctions. STRUCTURAL corollary of G-END-UNIT + E4 physical quotient -- NOT a derivation of Planckia... |
| · | `check_T_fermion_dirac_greybody_evaluated` | theorem | `—` | Fermion-Dirac greybody EVALUATED for massless spin-1/2 Schwarzschild channels by Chandrasekhar-Page tortoise-coordinate shooting (flux ~1e-8; barrier identity 4 kappa^2/27 at x=3/2 confirms NO integer-spin substitution; cross-checked vs an independent auditor solver to <=0.7% across 45 rows). GR/... |
| · | `check_T_greybody_integer_spin_evaluated` | theorem | `—` | Greybody factor EVALUATED for integer-spin Schwarzschild channels s=0,1,2 by GR Regge-Wheeler shooting (flux-conserved ~1e-7, low-freq anchor G_0 -> 4 varpi^2, no fitted target). GR/QFT-CS physics computed into the APF greybody slot -- NOT APF-derived. Does NOT close the physical evaporation tupl... |
| · | `check_T_md_endpoint_scale_criterion` | theorem | `—` | Endpoint scale derived in CRITERION form N_crit = ceil(eps_*/kappa_int) from the banked MD floor (eps_*) + a rank-capacity normalization (C_res=N*kappa_int): the endpoint is the smallest horizon rank supporting one minimum distinction, replacing the free flag 'N_H=O(1)'. The FORM is derived; the ... |
| · | `check_T_parameter_matching_harness` | theorem | `—` | M1-M6 parameter-matching harness: a toy tuple passing M1-M6 grades [P_toy_parameter_matching_harness]; a physical_imported tuple is held [C_evaluated_physical_Theta_H] until provenance-certified imports are supplied, EVEN IF it passes M1-M6 (no Tier-C laundering). Verified both gradings + guards.... |

## `apf/evaporation_quartet.py` — 4 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_evaporation_inverse_channel_flow` | theorem | `—` | At Type V saturation alignment, the L_irr-compatible substrate-side response is the inverse channel-flow: V_global -> vacuum face -> content face. Direction forced by holographic ceiling: load tracks area monotonically. |
| · | `check_T_evaporation_lattice_ordering` | theorem | `—` | Evaporation course is partially ordered by horizon-area-monotonic phase staging with Page time at half-evaporation as structural turnover. Page time structurally derived from equipartition argument, not free parameter. |
| · | `check_T_saturation_alignment_is_Type_V` | theorem | `—` | Saturation alignment at horizon interface is a Type V realignment-cost configuration: area at A_init (ceiling reached); local V_global at dim-V_global cap; eps_min paid per realignment; zero initial radiation entropy. Distinct from Type II (cosmogenic) and Type III (collapse). |
| · | `check_T_v_global_release_from_evaporation` | theorem | `—` | Cumulative kappa_int release theorem: \|V_global,local\|_deposit = \|V_global,local\|_release + S_radiation over the Page-time course. Release monotonic in horizon area. Structural form of BH unitarity at substrate-side ledger. |

## `apf/ew_bosonic_enforcement_reservoir.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_ew_bosonic_enforcement_reservoir_theorem` | theorem | `P_structural_reading` | Reservoir theorem (the v24.3.178-named revival), banked under the reservoir reading. The EW floor is the ABSOLUTE root-measure of the pre-branch static bosonic enforcement reservoir anchored to M_Pl, not a normalized branch ratio. Capacity by TYPE: bosonic positive-quadratic slots IN (8 gluon + 3... |

## `apf/ew_branch_incidence_density.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_ew_branch_incidence_density_geometry` | theorem | `P_structural_seam` | Branch cone(dq) incidence density 12/7 (denominator 7 = K3 additivity over disjoint supports; numerator 12 = gauge-symmetric incidences). Lift WITNESSED by banked E_rec: uniform-mode stiffness = E_rec per-node diagonal K_ii (A2 per-mode), N=7; cooperative off-diagonal vanishes for the uniform mod... |

## `apf/ew_codomain_reading_contracts.py` — 3 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_ew_codomain_reading_anchors_banked` | theorem | `P_structural_instrument` | Every codomain contract is backed by a live banked check at grade. |
| · | `T_ew_codomain_reading_home_values_from_capacity` | theorem | `P_structural_instrument` | Home codomain values are capacity-derived, not measured. |
| · | `T_ew_codomain_reading_schema_declared` | theorem | `P_structural_instrument` | CodomainReadingContract schema + four EW domains bank-callable and well-formed. |

## `apf/ew_counterterm_uncertainty_protocol.py` — 6 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_ew_counterterm_forbids_fit_and_target_input` | theorem | `P_ew_counterterm_uncertainty_protocol` | (no summary) |
| · | `check_T_ew_counterterm_slots_declared` | theorem | `P_ew_counterterm_uncertainty_protocol` | (no summary) |
| · | `check_T_ew_counterterm_uncertainty_protocol_P` | theorem | `P_ew_counterterm_uncertainty_protocol` | (no summary) |
| · | `check_T_ew_protocol_adapter_flags_safe` | theorem | `P_ew_counterterm_uncertainty_protocol` | (no summary) |
| · | `check_T_ew_uncertainty_comparison_rule_predeclared` | theorem | `P_ew_counterterm_uncertainty_protocol` | (no summary) |
| · | `check_T_ew_uncertainty_protocol_declared` | theorem | `P_ew_counterterm_uncertainty_protocol` | (no summary) |

## `apf/ew_dizet_real_adapter.py` — 6 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_ew_dizet_adapter_certification_P` | theorem | `—` | EVALUATOR_MAP edge in EW movement graph resolves to MOVES_CLEANLY with DIZET-filled payload. |
| · | `check_T_ew_dizet_adapter_external_ledger_declared_P` | theorem | `—` | All 9 required DIZET external evaluator ledger fields declared on the snapshot. |
| · | `check_T_ew_dizet_adapter_no_smuggling_P` | theorem | `—` | No measured-W-mass key in payload; WMASS=0 prediction mode active; target_value_consumed=False. |
| · | `check_T_ew_dizet_adapter_outputs_match_v161_P` | theorem | `—` | Banked DIZET outputs (M_W, SIN2TW, DAL5H, DR_TOTAL) match v16.1 baseline row exactly. |
| · | `check_T_ew_dizet_adapter_payload_contract_P` | theorem | `—` | EW DIZET adapter produces EW-shaped route payload with DIZET-filled evaluator + codomain. |
| · | `check_T_ew_dizet_real_adapter_P` | theorem | `—` | EW DIZET real adapter wires banked DIZET v6.45 W-route output into Engine-readable route payload; EVALUATOR_MAP edge fills cleanly; no smuggling (WMASS=0 prediction mode); 9-field external ledger declared; outputs match v16.1 baseline exactly. |

## `apf/ew_floor_measure_continuation_root.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_ew_floor_measure_is_continuation_sum_root` | theorem | `P_structural_seam` | Audit finding: the missing static-trace-measure theorem is not monolithic. Its 1/pi clause already has a banked home. v_floor = M_Pl sqrt(N_c) sqrt[(4pi)^(-D/2)] d_eff^(-C/2): the measure factor 1/(pi sqrt C_boson) equals sqrt of the BANKED continuation-sum measure (4pi)^(-D/2)=1/(16pi^2) (v24.3.... |

## `apf/ew_osw_numerical_assembly_harness.py` — 5 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `C_ew_osw_numerical_assembly_values_open` | other | `C` | The numerical assembly harness is the wiring layer: given source-certified component VALUES it assembles Delta r_OS / Delta r_rem / M_W, but it computes no self-energy and the included run is synthetic only. All value exports stay 0. The named next gate is COMPONENT VALUE SOURCING -- actually com... |
| · | `T_ew_osw_numerical_assembly_fail_closed` | theorem | `P_structural_instrument` | The assembly fails closed: an uncertified component raises SourceCertificationRequired, a missing slot raises InvalidAssemblyInput, and unphysical kinematics (mW2 >= mZ2) raise InvalidAssemblyInput in both assemble_delta_r_one_loop and compute_delta_r_rem. No value is produced from incomplete or ... |
| · | `T_ew_osw_numerical_assembly_forbidden_input_guard` | theorem | `P_structural_instrument` | The no-smuggling surface holds and is stronger than the families': the recursive guard rejects all 9 forbidden inputs at the top level (the 7 family entries + the two target-interval windows) and also catches a forbidden key buried inside a nested component object. |
| · | `T_ew_osw_numerical_assembly_present` | theorem | `P_structural_instrument` | The fail-closed numerical assembly kernel (apf.ew_osw_numerical_assembly_kernel) exposes assemble_delta_r_one_loop / compute_delta_r_rem / solve_mw_from_delta_r, declares the 8 required Delta r component slots, and carries a 9-entry forbidden-input ledger (the 7 family entries + the two target-in... |
| · | `T_ew_osw_numerical_assembly_slot_algebra` | theorem | `P_structural_instrument` | Under synthetic placeholder inputs the assembly's five slots (gamma-gamma, W-transverse, Z-transverse, gamma-Z, vertex/box) match the corresponding banked family coefficient maps term-by-term (max abs diff 5.4e-20), and the assembled Delta r_OS equals their sum. The assembly introduces no new phy... |

## `apf/ew_osw_reviewed_formula_evaluator_harness.py` — 4 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `C_ew_osw_full_evaluator_open` | other | `C` | The full reviewed-formula evaluator requires a source-certified coefficient import for the 8 pending component families (6 of the original 14 are now source-certified coefficient maps; the named next gate continues with Goldstone/ghost/gauge/tadpole). Until then no Delta r_rem / DeltaRhobarW valu... |
| · | `T_ew_osw_harness_contract_wellformed` | theorem | `P_structural_instrument` | Scheme card complete (on-shell, Denner/Sirlin counterterm + tadpole, finite-part inherited from the banked PV substrate). 16 component families: 2 implemented (banked elsewhere) + 8 pending source-certified; 14 formula-family contracts; 7-entry forbidden-input ledger; 3 Ward/gauge gates. |
| · | `T_ew_osw_harness_fails_closed` | theorem | `P_structural_instrument` | evaluate_delta_r_rem() returns value_evaluated=False with 8 families pending source-certified import; no numeric Delta r_rem / M_W is produced. The publishable closure remains the imported DIZET route. |
| · | `T_ew_osw_harness_no_substrate_duplication` | theorem | `P_structural_instrument` | The harness delegates the finite PV scalar substrate to the banked apf.w_trace_pv_scalar_integral_substrate (a0_fin/b0_fin present) and defines no PV kernels of its own; the two implemented component families reference the banked apf.delta_alpha_leptonic (0.031421) and apf.gauge.check_L_W_mass (0... |

## `apf/ew_osw_source_transcription_families.py` — 5 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `C_ew_osw_source_families_values_open` | other | `C` | The six source-transcription families are coefficient MAPS only: each requires a source-certified self-energy / counterterm value as input and computes none. No Delta r_rem / DeltaRhobarW / M_W is evaluated; all value exports stay 0. The harness now reads 2 implemented + 6 source-certified + 8 pe... |
| · | `T_ew_osw_source_families_coefficient_maps` | theorem | `P_structural_instrument` | Each of the six kernels reproduces its documented Delta r coefficient slot under placeholder unit inputs: W-transverse difference+custodial; gamma-Z 2(cW/sW)Pi/mZ2 and -(cW/sW)RePi/mZ2; Z-transverse -(cW2/sW2)RePi/mZ2 (anti-symmetric with Delta kappa); vertex/box and gamma-gamma identity slots; c... |
| · | `T_ew_osw_source_families_fail_closed` | theorem | `P_structural_instrument` | Each kernel fails closed: gamma-gamma, vertex/box, and the counterterm slice raise (SourceCertificationRequired / SourceValueRequired) without source-certified self-energy inputs; gamma-Z raises without pi_zgamma_0; W-transverse and Z-transverse carry value_is_full_delta_r / value_evaluated = Fal... |
| · | `T_ew_osw_source_families_forbidden_input_guard` | theorem | `P_structural_instrument` | The no-smuggling surface holds: each of the 6 kernels' guard_forbidden_inputs rejects every one of the 7 forbidden target/shortcut inputs (measured M_W, DIZET/ZFITTER aggregate, published total SM M_W, fitted counterterm, post-hoc tolerance, 4/5063 weak-angle shortcut, measured sin2theta_eff) -- ... |
| · | `T_ew_osw_source_families_kernels_present` | theorem | `P_structural_instrument` | All 6 OS-W finite-remainder source-transcription kernels (W-transverse, gamma-Z mixing, Z-transverse, vertex/box, gamma-gamma vacuum polarization, mass/charge/weak-angle counterterms) are installed verbatim under apf.ew_osw_source_families and each carries the 7-entry forbidden-input ledger. Sour... |

## `apf/ew_planck_anchor_gravity_consistency.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_ew_planck_anchor_forced_by_gravity_consistency` | theorem | `P_structural_convention` | First of the two genuinely-absent prefactor clauses (v24.3.181) to close, via the test the independence proof skipped: v24.3.180 proved independence from {A1,A2,K3} but never tested the GRAVITY sector. The banked gravity sector fixes one Planck scale -- Bekenstein S=A/(4 ell_P^2), ell_P^2=G (T_Be... |

## `apf/ew_planck_hierarchy_mechanism.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_ew_planck_hierarchy_capacity_suppression_mechanism` | theorem | `P_structural_convention` | The EW/Planck hierarchy has the FORM of a bosonic root-measure suppression v/M_Pl ~ d_eff^(-C_boson/2) = 102^(-8), the inverse-sqrt of microstate volume Omega_boson = d_eff^C_boson. C_boson=16, d_eff=102 are bank-fixed (no EW tuning); this carries M_Pl to O(100 GeV) -- the hard part of the hierar... |

## `apf/ew_pre_branch_necessity.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_ew_pre_branch_necessity` | theorem | `P_structural_exhaustive` | Closes the exponent by exclusion with the correctly-stated hypothesis (v24.3.182's residual was against 'y_t-free alone', which is too weak). Given the banked floor (y_t-free, C_boson=16) and the separated 12/7 lift: assume post-SSB. CASE A (with fermions) carries m_t=y_t v/sqrt2 -> y_t-dependent... |

## `apf/ew_pre_branch_reservoir_ordering.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_ew_pre_branch_reservoir_ordering` | theorem | `P_structural_reading` | The forcing mechanism v24.3.179 lacked. v_H = M_Pl . Omega_bos^(-1/2) . (12/7), with the root-measure evaluated PRE-branch and the 12/7 lift POST-branch. WHY gluons are in the floor (16) but out of the lift: color cancellation (v24.3.178) is a POST-branch event -- it needs the color-singlet Higgs... |

## `apf/ew_prefactor_axiom_independence.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_ew_prefactor_axiom_independence` | theorem | `P_structural_convention` | Model-theoretic independence (capstone of the prefactor line; stronger than the factor-level no-go v24.3.177). With C, d_eff, the root-measure d_eff^(-C/2), and 1/sqrt(C) fixed, the residual prefactor eta(g,mu,rho)=sqrt(g) rho/(mu sqrt(C)) admits four completions A/B/C/D (g in {N_c,1,N_c^2}, rho ... |

## `apf/ew_prefactor_invariance_no_go.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_ew_prefactor_invariance_no_go` | theorem | `P_structural_convention` | No-go: the O(1) prefactor eta = sqrt(g) rho/(mu sqrt(C_boson)) has three INDEPENDENT carriers under the current stack -- color g=N_c (strip -> x1/sqrt3, = the banked yt no-go fork), measure mu=pi (a SINGLE 1/pi, NOT the C_boson-mode determinant pi^(-8) ~ 1.05e-4; ~3020x apart, so not the Gaussian... |

## `apf/ew_scale_functional_independence.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_ew_scale_functional_independence_no_go` | theorem | `—` | (no summary) |

## `apf/ew_sqrtNc_carrier_color_triplet.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_ew_sqrtNc_carrier_forced_by_color_triplet_trace` | theorem | `P_structural_reading` | The last open prefactor clause, closed under the principal's inversion-only ruling on the y_t no-go. The y_t-free floor's sqrt(N_c) = a_Y/sqrt(b) (y_t cancels; both carry N_c) is the physical color-triplet trace ratio: a2 = Sum N_c*Tr is EXACT over H_F=C^96 (L_normalization_coefficient [P]) with ... |

## `apf/ew_static_well_factorization.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_ew_static_well_factorization_principle` | theorem | `P_structural_reading` | BANKED: the static-well factorization principle. For a local normalized root-measure / Hessian determinant on an order-parameter well, det(H_X (+) H_Xbar) = det(H_X) det(H_Xbar); a lambda-independent complement cancels (toy-verified: full-61 ratio == active-only ratio). So Paper-7 C_total=61 does... |

## `apf/ew_trace_scheme_transport_certifier.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_EW_trace_scheme_transport_certifier_P` | theorem | `—` | EW trace-to-scheme transport certifier gates APF_TRACE local closure vs physical scheme export. |

## `apf/ew_trace_to_scheme_real_adapter.py` — 5 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_EW_adapter_certification_P` | theorem | `—` | EW adapter reports feed the interface-intelligence stack with expected held/P/fail-closed statuses. |
| · | `check_T_EW_adapter_live_probe_safe_P` | theorem | `—` | Live probe mode is safe in partial/standalone environments and defaults to no target consumption. |
| · | `check_T_EW_adapter_no_evidence_no_patch_P` | theorem | `—` | EW adapter does not patch/rerun without completed evidence obligations. |
| · | `check_T_EW_adapter_payload_contract_P` | theorem | `—` | EW real adapter emits the standard EW route payload contract. |
| · | `check_T_EW_trace_to_scheme_real_adapter_P` | theorem | `—` | EW Trace-to-Scheme Real Adapter is P: live/manual EW state converts into payloads, certifications, obligations, and safe rerun gating. |

## `apf/ew_unitarity_eigenscreen.py` — 4 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_ew_coupled_channel_eigenscreen_lqt` | theorem | `P_structural_instrument` | The LQT coupled-channel S-wave core matrix (units -m_h^2/(8*pi*v^2)) on the normalized basis {\|W+_L W-_L>, \|Z_L Z_L>/sqrt2, \|h h>/sqrt2, \|Z_L h>} is verified exactly in Q[sqrt(2)]: the four pack ei... |
| · | `T_ew_custodial_amplitude_basis` | theorem | `P_structural_instrument` | Exact polynomial identities over Q[s, m_h^2]: the tree master amplitude s/v^2 - s^2/(v^2(s-m_h^2)) = -m_h^2 s/(v^2(s-m_h^2)); the radial-Higgs exchange divides as -s^2 = (-s-m)(s-m) - m^2, so the G... |
| · | `T_ew_partial_wave_screens` | theorem | `P_structural_instrument` | The three custodial partial-wave screens are carried at two cleanly separated levels: the finite-m_h log closed forms as verbatim declared strings (transcendental in s; never float-evaluated), and ... |
| · | `T_goldstone_equivalence_boundary_declared` | theorem | `P_structural_instrument` | The Goldstone-equivalence boundary M(V_L) = C_V*M(pi) + O(M_V/E) is carried as a DECLARED calculational contract (validity domain E >> M_V, C_V = 1 exact at the tree-canonical boundary, loop factor... |

## `apf/fencea_hinge_trichotomy.py` — 4 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_correlation_hierarchy_ladder` | theorem | `P_structural` | Rung 0 product (L_loc) / rung 1 classical correlation (the forced L_nc cost) / rung 2 discord-only cq (the bridge theorem's one-sided FLOOR, generic; exception locus Delta = -eps pinned, where the state drops to rung 1) / rung 3 entanglement (two-sided + the .340 gate; diagonal closed form 2 ln(1... |
| · | `T_correlation_ladder_exact_rational_chsh_witness` | theorem | `P_structural` | The native two-cell Gibbs family has populations 102^{-k} (exact rational at the ln102 rungs), so its correlators are exact rationals; rational Pythagorean (3-4-5) measurement settings give an exact-rational CHSH the Boole-polytope engine consumes with no float. Two entangled members at (eps, mu)... |
| · | `T_fencea_hinge_coupling_trichotomy` | theorem | `P_structural` | The FENCE-A cost-to-state hinge is a TRICHOTOMY, not the 06-24 dichotomy: (B) diagonal L_nc cost separable (06-24 reproduced); (b) ONE-sided non-commuting defender exactly cq-separable at every parameter value — the T_inseparable_IJC bridge conclusion ("at least one E_di") is insufficient for cro... |
| · | `T_ladder_ceiling_calibration_from_saturation` | theorem | `P_structural_reading` | The correlation-hierarchy ladder ceiling 2 sqrt2 * d_eff/(d_eff+1) sat at an inserted calibration beta*\|eps\| = ln 102. This check identifies that calibration with the banked per-type saturation cost: sigma = S_dS/C_total = ln(d_eff) [L_sigma_intensive, P], with d_eff = (C_total-1)+C_vacuum = 60+4... |

## `apf/fermion_normalizers.py` — 2 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `L_residual_up_normalizer_local` | lemma | `[P_structural]` | Local up-sector residual normalizer theorem: after the spent quotient (removing L_EW, sqrt(3) spectral lift, weak-carrier bookkeeping, Yukawa-bilinear bookkeeping, and projective trace shape), the residual quadratic interface load uniquely selects u_R^c, and the absolute residual U(1) flux on tha... |
| · | `T_no_inverse_inputs_up_normalizer` | theorem | `[P_structural]` | Non-smuggling guard for L_residual_up_normalizer_local.  Declared inputs are representation multiplicities, hypercharge, the spent quotient, and the two residual functionals; forbidden inputs are m_t, y_t, m_b, m_tau, v_obs, physical_yukawa_normalization.  The intersection is empty by constructio... |

## `apf/fibration_census.py` — 3 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_b_pin_threat_empty` | theorem | `P_structural_exhaustive` | P_Gamma is admissibility-closed by canonical definition (endpoint filter); T_proton [P] excludes the B-altered endpoint at the saturated census; so the B-pin's threat set is empty -- the threat/evaluator divergence question dissolves by vacuity (the fifth shape), and the discriminating instance b... |
| · | `T_record_term_pincer` | theorem | `P_structural_exhaustive` | A gamma record-term requires jointly: (a) a non-empty admissible threat set against a held value (this session's probe/census verdicts) and (b) GW-1's record-level evaluator-constitution (quoted verbatim; modulus/direction split carried as named tension). Walking the complete banked record invent... |
| · | `T_saturation_fibration_census` | theorem | `P_structural_exhaustive` | Every banked census label classified: Q FIBER gauge-rigid (generator-route; operator-inventory premise named, GQL-1a genre); B FIBER saturation-locked -- the only banked class-change (L_Sakharov), making baryogenesis a baryon story; colour EMPTY STRATUM (T_confinement, IR antecedent named, distin... |

## `apf/fluctuation_response_two_faces.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_fluctuation_response_is_two_faces` | theorem | `P` | Temperature is the exchange rate between the ledger's two currencies -- the energy a distinction costs (eps) and the count it carries (sigma=ln d_eff) -- with beta=sigma/eps the rate. On the canonical distribution P(n) ∝ e^{n(sigma-beta eps)} that max-entropy (L_equip) assigns over n in {0..C_tot... |

## `apf/formal_kernel.py` — 3 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `L_maschke_semisimplicity_witness` | lemma | `P_math` | The Maschke semisimplicity import witnessed in exact rational arithmetic: regular trace-form nondegeneracy for Q[Z_4] and Q[S_3]; the S_3 central-idempotent decomposition with block ranks 1 + 1 + 4 = 6; the averaging-projector mechanism on a concrete reducible action; and the F_2[Z_2] nilpotent n... |
| · | `T_FormalKernel_VLambda_uniqueness` | theorem | `[P_structural]` | Executable witness for Theorem 1.1 (Paper 8 Supp §1): V_local irrep-specified ⇒ V_Lambda is unique G_SM-invariant complement. Adversarial random subspace of same dim fails invariance; irrep-content mutation changes V_Lambda. |
| · | `T_vglobal_slot_identification_no_go` | theorem | `P_structural` | The slot-level V_global identification walk, refutation branch: the Higgs isotypic class of V_61 has multiplicity 1 and dim 4, so every G_SM-invariant subspace meets the Higgs sector in dim 0 or 4 — never 3. No G_SM-invariant 42-dim complement has sector signature (12, 3, 27); the complete achiev... |

## `apf/foundation_inputs.py` — 3 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `FD1_structural_completeness` | other | `[P]` | The FD1 structural-completeness clause, adopted as a named foundational commitment (parity with the marginal floor over MD/BW): a physical object is its admissible continuation profile and nothing beyond it; there are no physical facts except those fixed by the continuation structure; any quantit... |
| · | `T_PLEC_derived_from_spine` | theorem | `[P_structural]` | PLEC's four constitutive features A1/MD/A2/BW are derivable consequences of the 4-input declaration under Paper 10 v1.12 §3.5 reductions.  Each derivation is exhibited on the canonical witness: A1 + MD-value are the two halves of the finite-physical-regime hypothesis; the MD tested/gauge cleavage... |
| · | `T_four_input_declaration` | theorem | `[P_structural]` | Canonical 4-input declaration of APF: FD1 (physical identity = finite admissible continuation identity) + FD2 (physical distinction = finite enforceable separator of continuation profiles) + FD3 (physical distinctions carry positive realignment cost) + finite-physical-regime hypothesis (C_Γ < ∞ A... |

## `apf/fractional_reading.py` — 9 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `L_Lambda_absolute_numerical_formula` | lemma | `P` | Numerical identity. Formula rho_vac/M_Planck^4 = (C_vacuum/d_eff) * 1/N_SM = (42/102) * 102^(-61) = 10^(-122.910), with all constants bank-native. Observed value 10^(-122.944) (standard Planck-mass, Planck 2018). Residual 0.0340 decades = factor 1.082 (8%), passing the 0.05-decade (factor 1.12) g... |
| · | `L_N_SM_hierarchy_near_miss` | lemma | `C` | log10(1/N_SM) = -122.525 = -122.525. Observed log10(rho_vac / M_Planck^4) lies in approximately [-122.9, -120.1] depending on Planck-mass convention. Best-case residual 0.42 (standard 0.42, reduced 2.38). Agreement within one decade in log10 is suggestive under FRE + entropy-fraction reading, but... |
| · | `L_Omega_Lambda_is_entropy_fraction` | lemma | `P` | At the SM interface (K = 61, d_eff = 102), the cosmological dark-energy fraction Omega_Lambda = 42/61 = 0.688525 equals the fraction of SM admissibility-capacity S_SM = 282.123 nats supported on the 42-dim V_Lambda subspace of V_61: S(V_Lambda) = 194.249 nats, S(V_Lambda)/S_SM = 0.688525. Three-p... |
| · | `L_Omega_b_is_entropy_fraction` | lemma | `P` | At the SM interface, Omega_b = 3/61 = 0.049180 equals the fraction of S_SM = 282.123 nats supported on V_b (dim 3): S(V_b) = 13.8749 nats, ratio = 0.049180. |
| · | `L_Omega_c_is_entropy_fraction` | lemma | `P` | At the SM interface, Omega_c = 16/61 = 0.262295 equals the fraction of S_SM = 282.123 nats supported on V_c (dim 16): S(V_c) = 73.9996 nats, ratio = 0.262295. |
| · | `T_FRE_SM_to_entropy_dictionary` | theorem | `P` | At the SM interface (K=61, d_eff=102, V_slot = V_61 with residual partition V_b (+) V_c (+) V_Lambda of dims 3+16+42), FRE establishes the dictionary: Omega_b = 3/61 = S(V_b)/S_SM; Omega_c = 16/61 = S(V_c)/S_SM; Omega_Lambda = 42/61 = S(V_Lambda)/S_SM. Entropy-level closure S(V_b)/S_SM + S(V_c)/S... |
| · | `T_Lambda_absolute_structural_derivation` | theorem | `C` | Conjectural structural derivation of the [P] numerical formula rho_vac = (C_vacuum/d_eff) * M_Planck^4 * 1/N_SM: at the SM interface, the dark-energy density equals the vacuum fraction of per-slot admissibility (42/102 from L_self_exclusion) times the Planck density times the reciprocal total-mic... |
| · | `T_fractional_reading_equivalence` | theorem | `P` | FRE verified: at the SM interface (K=61), the slot-counting, admissibility-entropy, and cosmological-residual fractions all collapse to K_X / K for the three-way residual partition (3,16,42). Closure: 3/61 + 16/61 + 42/61 = 1 at the entropy level. The same collapse holds trivially at the canonica... |
| · | `T_residual_entropy_closure` | theorem | `P` | At the SM interface (K=61, d_eff=102), the three entropy fractions S(V_b)/S_SM = 3/61, S(V_c)/S_SM = 16/61, S(V_Lambda)/S_SM = 42/61 sum to 1.000000000000, closing to unity with residual 0.00e+00. This is the entropy-level closure of the cosmological residual partition, parallel to the scalar-lev... |

## `apf/frustrated_choice_family.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `L_frustrated_witness` | lemma | `—` | (no summary) |

## `apf/frustration_center_partition.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_frustration_center_partition` | theorem | `—` | (no summary) |

## `apf/g2_trivial_center_exhibit.py` — 2 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `L_trivial_center_no_nality_obstruction` | lemma | `P_math | lattice-model conventions (the banked oriented electric-basis graph model with per-vertex-singlet admissibility, Gauss reading a named identification) + pinned G2 conventions (Cartan matrix + node order + weight coordinates) -- vacuity billed in-sentence: no kinematic N-ality obstruction, NEVER "everything screens"` | For G2 (compact simple, trivial center), in the named lattice model and pinned conventions: the N-ality receiving group Z(G)-hat = P/Q is TRIVIAL -- det(Cartan) = 1, both fundamental weights intege... |
| · | `T_g2_fusion_screen_exhibit` | theorem | `P | instance-scoped at stated caps and walked graphs: fusion facts on the stated 9-irrep battery grid; graph facts at cap {1,7,14,27} on the walked graphs (TT 1-3, claw 1-3, K4+tail 1-3; the tree control is the sibling check's); nothing beyond -- beyond the battery grid the constructed rules are computed where walked, named where not` | The G2 fusion rules CONSTRUCTED TWICE independently in-module -- route 1 Freudenthal (exact integer recursion, divisibility asserted every step) + Racah-Speiser/Klimyk; route 2 exact Weyl-character... |

## `apf/gamma_c_carrier_program.py` — 4 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `L_notrace_not_from_recruitment_instruments` | lemma | `P_structural_instrument` | The no-trace gate (gamma_C = 1, plane-carrier closure) is NOT a theorem of the licensed recruitment corpus as formalized 2026-07-03: the Paper 10 Supplement B5 + B3.4 instruments, the sec-8 clock-sector response principle (discharged: prices lambda_t only), and the complete Papers 24/25 derived p... |
| · | `L_register_carrier_not_from_account_instruments` | lemma | `P_structural_instrument` | The register-carrier lemma is not derivable from the banked account-structure instruments as of 2026-07-03; its content is exactly the carrier selection. T-RC1 AT SCHEMA STRENGTH (machine): marking a record-combination as line-requiring IS choosing the response -- rule-choice = response-choice. T... |
| · | `T_gammaC_carrier_fork` | theorem | `P_structural` | In the Paper 9 v1.6 calibrated normal form (lambda_t = +1, lambda_s = -gamma_C), the four carrier closures SOLVE to gamma_C in {1, 1/3, 0, -1} (plane / four-cell / per-channel / pooled), pairwise distinct and cross-exclusive (plane closure forces four-cell trace -2; four-cell forces plane trace 2... |
| · | `T_weight_one_reduction` | theorem | `P_structural` | The weight-one walk (2026-07-04, REDUCED) banked at its proved strength. UNCONDITIONAL ARITHMETIC (exact rationals, n = 3..8): L-W0, the banked weight IS the deposit fraction w = D(spread deposit)/D(commitment) -- the denominator n-1 is DISCHARGED as the cell's eta-sum, and D-balance selects gamm... |

## `apf/gapless_serial_floor.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_gapless_serial_floor` | theorem | `—` | (no summary) |

## `apf/gauge_beta_capacity_tiling.py` — 2 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_capacity_coupling_is_leading_log` | theorem | `P_structural_seam` | Establishes that the capacity reading of a gauge coupling is a leading-log object. Leg 1 (banked): the framework's gauge betas are the SM one-loop betas and tile the horizon, 6(\|b_3\|+\|b_2\|+\|b_Y\|)=42+19+41=102=d_eff (parent theorem). Leg 2: the SM two-loop b_ij are continuum rationals with no inte... |
| · | `T_gauge_beta_capacity_tiling_abelian` | theorem | `P_structural_seam` | Closes the gauge sector's beta-to-capacity map. L_beta_capacity matched the two non-abelian betas to the ledger as N_gen=3-forcing conditions (6\|b_3\|=C_vacuum=42, 6\|b_2\|=C_matter=19). This adds the abelian member in the same Standard-Model normalization: 6\|b_Y\| = d_eff - C_total = 41, equivalentl... |

## `apf/gauge_fiber_route_classifier.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_gauge_fiber_route_classifier_P` | theorem | `—` | Gauge fiber route classifier gates codomain/cocycle/descent closure. |

## `apf/gauge_invariant_record.py` — 15 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_canonical_colour_record_iff_multiplicity_free_P` | theorem | `—` | Canonical (frame-free) sharp gauge-invariant colour record EXISTS iff the singlet multiplicity m=1 (trichotomy m=0 no record / m=1 canonical / m>=2 non-canonical). In the verified non-abelian channels (SU(2)/SU(3) meson, SU(2) diquark, SU(3) baryon, all m=1) the unique invariant is entangled (Sch... |
| · | `check_T_chiral_condensate_flavour_density_interface_is_contextual` | theorem | `—` | The chiral condensate's gauge-invariant flavour-density interface is state-independently CONTEXTUAL (IJC_str) at the single-density level (N_f=3). The order parameter Sigma_ij = <qbar_{R,i} q_{L,j}> has scalar-flavour densities (the vector-like qbar q + qbar lambda^A q, U(3)_V) spanning Herm(3) (... |
| · | `check_T_ckm_flavour_coavailability_is_sepstr` | theorem | `—` | The CKM-forced flavour co-availability is SepStr, not the contextual web. The A1-forced CKM (V != 1, fully mixing: \|V_ij\| in (0.0036, 0.9992)) makes exactly two incompatible mass bases (down-mass, up-mass via the charged current) co-available and classically consequential; fed to the Interface En... |
| · | `check_T_colour_contextuality_is_kstring_spectrum_blind` | theorem | `—` | The strong (contextuality) face is k-string-SPECTRUM-BLIND: every invariant that is a function of the confining colour interface's commutant multiplicity structure is N-independent (physical range k<=floor(N/2)) and monotone/asymmetric in k, whereas the k-string tension sigma_k (Casimir k(N-k) or... |
| · | `check_T_exotic_gauge_invariant_algebra_is_nonabelian` | theorem | `—` | The tetraquark gauge-invariant colour algebra is NON-ABELIAN: singlet multiplicity m=2 for SU(2) and SU(3) gives an M_2 block in the commutant, and for SU(2) the two meson-meson pairing projectors P_A, P_B are gauge-invariant and do not commute. This contrasts the meson (m=1, abelian span{pi_s,pi... |
| · | `check_T_gauge_invariant_colour_KS_coloring_obstruction` | theorem | `—` | A gauge-invariant colour interface admits a state-independent Kochen-Specker COLORING obstruction, exactly. The SU(2) pentaquark (fund^5) gauge-invariant algebra contains a full M_4 (spin-3/2, multiplicity 4; exact rational certificate), a two-qubit operator algebra that realizes the Mermin-Peres... |
| · | `check_T_gauge_invariant_colour_interface_is_contextual` | theorem | `—` | A gauge-invariant colour interface is structurally contextual (IJC_str). The SU(2) tetraquark gauge-invariant algebra contains a full M_3 (spin-1 isotypic, exact rank-9 projector, irreducible 3-dim copy, multiplicity 3), so every qutrit observable is realized by a gauge-invariant operator. The ex... |
| · | `check_T_gauge_invariant_colour_interface_state_independent_contextual` | theorem | `—` | A gauge-invariant colour interface is contextual STATE-INDEPENDENTLY. The tetraquark spin-1 M_3 hosts the Yu-Oh 13-ray Kochen-Specker set; on the MAXIMALLY-MIXED qutrit state (every marginal 1/3, lifting to the maximally-mixed gauge-invariant state rho=P1/9) the table is outside the noncontextual... |
| · | `check_T_gauge_invariant_colour_record_general_N` | theorem | `—` | (no summary) |
| · | `check_T_matter_free_colour_record_deep_superselection_no_go` | theorem | `—` | Face (b) of the matter-free branch-2 phenotype (deep superselection) CLOSED: in-sector (m=1) centrality of the colour record is real (fund + adjoint pairs, exact) but ONE adjoint enlargement de-centralizes it (HW multiplicity >= 2, non-scalar record compression, explicit exact gauge-invariant bra... |
| · | `check_T_only_gauge_invariant_sharp_colour_record_is_nonfactorizable_singlet_P` | theorem | `—` | In SU(2)/SU(3) fund (x) antifund the gauge-invariant *-algebra is exactly the 2-dim span{pi_singlet, pi_adjoint}; its unique rank-1 projector is the non-factorizable colour singlet (Schmidt rank N), so every sharp gauge-invariant colour record is entangled and no sharp product-state gauge-invaria... |
| · | `check_T_product_group_sharp_records_factorwise` | theorem | `—` | Sharp product-group records track group structure FACTOR-WISE THROUGH THE SLOT STRUCTURE. On product content the invariant algebra factorizes exactly, (A x B)' = A' (x) B', certified by explicit bases with containment + dimension on ALL THREE instances (U(1) x SU(2): 12 = 6*2; SU(2) x SU(2) bifun... |
| · | `check_T_su3_octet_M4_explicit_construction` | theorem | `—` | The octet M_4 block is CONSTRUCTED, not inferred: 16 explicit 81x81 rational matrix units with [e_pq, G_a] = 0 verified entry-by-entry against all 8 sl(3) generators (128 commutators; extended to sl(3,C) by linearity and to SU(3) by exponentiation), e_pq e_rs = delta_qr e_ps (256 products), sum e... |
| · | `check_T_su3_octet_colour_KS_coloring_obstruction_exact` | theorem | `—` | The physical gauge group SU(3) hosts a state-independent Kochen-Specker COLORING obstruction on a gauge-invariant colour interface, exactly. The real-QCD tetraquark q-qbar-q-qbar octet has multiplicity 4 (exact Weyl-Klimyk + explicit Q[i,sqrt3] Casimir tr C=432, tr C^2=2736), so the colour commut... |
| · | `check_T_unique_gauge_invariant_colour_state_of_N_fundamentals_is_entangled_baryon_P` | theorem | `—` | For SU(2) (2 fundamentals) and SU(3) (3 fundamentals) the invariant subspace of fund^(x)N is exactly 1-dimensional and is spanned by the totally-antisymmetric epsilon baryon, which is non-factorizable (Schmidt rank N across first\|rest). So the unique sharp gauge-invariant colour state of N fundam... |

## `apf/gauge_quotient_ledger.py` — 12 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `L_defended_fact_is_template_invariant` | lemma | `P` | GQL-1 DERIVED by contradiction from canonical threat-defense text, modulo ONE named consumption (GQL-1a: billing-completeness -- billed carriers are template reps, billed interactions template-invariant, and a billed defense's discriminating power is billed-detectable content; the T_gauge/T_field... |
| · | `L_defense_requires_evaluator` | lemma | `P_structural_exhaustive` | GQL-5a-1 DERIVED in BOTH obligation shapes, exhaustively: two-sided (fact-variable) defense against a bidirectionally covering threat forces fiber discrimination (256/256; discrimination necessary, not sufficient); the ONE-SIDED (record) case -- the eighth audit's gap -- closed via 7a non-disturb... |
| · | `L_gauge_orbit_unpinnable` | lemma | `P` | GIVEN the covariance-totality identification GQL-1 (no enforceable separator PINS a gauge-orbit position -- a record fact at a gauged interface is gauge-invariant; carried as a NAMED identification: the banked chain proves species/template uniqueness (T_field, L_gauge_template_uniqueness), not se... |
| · | `L_pinned_demand_is_feasibility_rhs` | lemma | `P` | Identification (iii) of the Schur-billing chain derived from banked [P] content, placement-independently. Funding totality: at the record-free vertex the sector capacities are consumed exactly by the footprints (slack 0, computed), so a class commitment Delta > 0 would be unfunded there -- contra... |
| · | `L_program_bridge_kkt` | lemma | `P` | GQL-4 (the program bridge) advanced, per the 2026-06-10 combined audit's route (b): BINDING is grounded in T21 [P]'s own fixed-point identity A w* = gamma (executed exactly at both points) -- under c = gamma binding is an IDENTITY of banked algebra, replacing the first draft's rejected KKT framin... |
| · | `T_alpha_gamma_coincide_on_template_class` | theorem | `P_structural_exhaustive` | The two surviving usage-measure constructions COINCIDE on the Delta = 1 carrier class -- the alpha-vs-gamma fork is closed; uniqueness-up-to-spec NOT proved (a third S1-S3-passing construction is not excluded; the honest claim is no-live-rival-among-constructed-candidates). Proof, per the ninth a... |
| · | `T_evaluator_canonicity_kills_noncanonical_storage` | theorem | `P` | The (i)-campaign advance, stated per the 2026-06-10 combined audit: the fork is RELOCATED into GQL-5a/5b, with the rivals given an executable death GIVEN the frame. DERIVED sector-neutrally: the fact has exactly ONE evaluator (Schur-canonical pairing, dim 1 exact; U(1)-invariance is VACUOUS on th... |
| · | `T_ew_load_placement_P` | theorem | `P` | The +1 in gamma_2 = a_22 + n_radial (the single radial Higgs record, n_radial = 4-3 = 1, T_Higgs) is billed to SU(2)'s row -- forced, not adopted -- by FD1 structural completeness composed with the Schur asymmetry.  Structural completeness (the adopted foundational clause, check_FD1_structural_co... |
| · | `T_gql1a_reduced_by_co_movement` | theorem | `P` | GQL-1a (billing-completeness) is REDUCED to GQL-1b, not dissolved: an orbit-variant 'fact' cannot be STORED at a gauged interface as a well-defined fact, GIVEN (i') action-totality (the template action is defined on all interface content -- canonically anchored via the V_61/rho_SM realization, fo... |
| · | `T_orientation_ew_route_priced` | theorem | `—` | (no summary) |
| · | `T_record_demand_is_quotient_codim` | theorem | `P` | GIVEN GQL-1/2/3 (named identifications, see L_gauge_orbit_unpinnable + module docstring): a record class pinning k independent quotient facts has pinned demand Delta = k, priced k * epsilon (L_cost uniformity) -- objects of the type the banked access-partition floor governs (routing claim; the to... |
| · | `UB_usage_billing_adopted` | other | `P_structural_reading` | UB ADOPTED-WITH-FALSIFIER (principal ruling 2026-06-10; MD/BW precedent), named SEVERALLY per the tenth adoption audit: (UB-r) routing-as-billing semantics (the Gram FORM is banked [P]; the draws READING is the adopted clause); (UB-b) the diag(A) baseline (supersedes the eighth audit's not-absorb... |

## `apf/globalization_promotion_gate.py` — 8 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_claim_language_emitter_P` | theorem | `—` | Promotion gate emits safe claim language for each status. |
| · | `check_T_export_only_zero_obstruction_P` | theorem | `—` | Global P export is allowed if and only if the obstruction object is zero. |
| · | `check_T_globalization_promotion_gate_P` | theorem | `—` | Globalization promotion gate is P: it exports only zero-obstruction claims and fail-closes/holds all others. |
| · | `check_T_no_promotion_overclaim_P` | theorem | `—` | Scope boundary preserved: repairability is not promotion; only zero obstruction exports global P. |
| · | `check_T_ordinary_repair_hold_not_export_P` | theorem | `—` | Ordinarily repairable claims are held, not exported, until repair is executed and rechecked. |
| · | `check_T_promotion_status_partition_P` | theorem | `—` | Promotion gate partitions claims into export, repair-required, substrate-revision-required, and fail-closed statuses. |
| · | `check_T_provenance_fail_closed_P` | theorem | `—` | Provenance-smuggled claims fail closed and cannot be promoted or repaired mathematically. |
| · | `check_T_substrate_revision_hold_not_current_P` | theorem | `—` | Substrate-revision-repairable claims are not current global P; they open D1/D2/D3 research programs. |

## `apf/graded_threat_robustness.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `L_graded_threat_collapses_to_crisp` | lemma | `P_structural` | Vocabulary-robustness residual of the IJC dichotomy CLOSED. Under graded (fuzzy/probabilistic) threat memberships mu_d : P -> [0,1] with graded-FD5 monotone dominance mu_12 >= max(mu_d1, mu_d2) -- the forced graded reading of joint-meaningfulness -- the graded structure is exactly a threshold-sta... |

## `apf/gravity_bianchi_rigidity_real_adapter.py` — 3 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_gravity_bianchi_rigidity_adapter_atlas_routes_P` | theorem | `—` | Atlas routes gravity Bianchi rigidity payload to INTERNAL_IDENTITY_GLOBAL_P. |
| · | `check_T_gravity_bianchi_rigidity_adapter_closure_kind_P` | theorem | `—` | gravity Bianchi rigidity adapter declares closure_kind=internal_identity (framework structural export). |
| · | `check_T_gravity_bianchi_rigidity_adapter_registry_pointer_P` | theorem | `—` | gravity Bianchi rigidity adapter cites registry pointer. |

## `apf/gravity_gr_limit_full_close_real_adapter.py` — 3 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_gravity_gr_limit_full_close_adapter_atlas_routes_P` | theorem | `—` | Atlas routes gravity GR-limit full close payload to INTERNAL_IDENTITY_GLOBAL_P. |
| · | `check_T_gravity_gr_limit_full_close_adapter_closure_kind_P` | theorem | `—` | gravity GR-limit full close adapter declares closure_kind=internal_identity (framework structural export). |
| · | `check_T_gravity_gr_limit_full_close_adapter_registry_pointer_P` | theorem | `—` | gravity GR-limit full close adapter cites registry pointer. |

## `apf/gravity_ringdown_capacity_schema_real_adapter.py` — 3 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_gravity_ringdown_capacity_schema_adapter_atlas_routes_P` | theorem | `—` | Atlas routes gravity ringdown capacity schema payload to INTERNAL_IDENTITY_GLOBAL_P. |
| · | `check_T_gravity_ringdown_capacity_schema_adapter_closure_kind_P` | theorem | `—` | gravity ringdown capacity schema adapter declares closure_kind=internal_identity (framework structural export). |
| · | `check_T_gravity_ringdown_capacity_schema_adapter_registry_pointer_P` | theorem | `—` | gravity ringdown capacity schema adapter cites registry pointer. |

## `apf/hold_cost_dominance.py` — 2 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `L_mechanism_trichotomy` | lemma | `—` | (no summary) |
| · | `T_hold_cost_dominance_split` | theorem | `—` | (no summary) |

## `apf/horizon_fiber_cost_classifier.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_horizon_fiber_cost_classifier_P` | theorem | `—` | Horizon fiber-cost classifier gates overlap and capacity closure. |

## `apf/horizon_joint_bridge.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_I1_bridge_at_joint_K42` | theorem | `P_bridge` | At the canonical SM-dS joint point K = 42, three independent constructions of a 42-dim subspace in V_61 coincide: (1) F_horizon(acc_horizon(42)) under Convention A (d_eff = e, Bekenstein area quantisation); (2) V_global from T_interface_sector_bridge (SM gauge-cosmological residual partition of V... |

## `apf/horizon_ledger_reindexing.py` — 15 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_C_evaporation_ledger_completion` | other | `—` | OPEN conjecture. Structural scaffolding closes (radiation-codomain sufficiency + thermal-marginals-no-loss + microtransport sufficiency); the two physical-realization gates remain genuinely open: does actual Hawking radiation have the correlation rank, and does actual dynamics supply M1-M4. Consi... |
| · | `check_L_four_commitment_independence` | lemma | `—` | The four commitments (localization, exterior distinguishability, interior exclusion, ledger reversibility) are independent: each fails while the other three remain satisfiable, giving four distinct normal-form obstructions NF_loc/NF_ext/NF_int/NF_rev. Gate 2. |
| · | `check_L_no_bounded_remnant` | lemma | `—` | A bounded-area remnant (N_R <= A_R/4 l_P^2) cannot carry the ledger of an arbitrarily large hole; the deficit grows without bound and the only escape (unbounded hidden degeneracy) violates finite enforceability (A1). Minimal exterior-completion is forced toward radiation correlations. |
| · | `check_T_BH_quarter_coefficient` | theorem | `—` | S_BH = A / (4 l_P^2): the Bekenstein-Hawking quarter coefficient is 1/N_commit = 1/4, with N_commit=4 now representation-invariant (categorical-equivalence fourness) and kappa=1 fixed by the substrate-unit convention. Both former residuals are conditional-P closures, not open gates. Does NOT over... |
| · | `check_T_apf_planck_cell_normalization` | theorem | `—` | Under the APF substrate-unit convention (hbar, c, G = one enforcement, coordination, interface-load unit each), the minimal cell at joint single-unit saturation is A_cell = l_P^2, so kappa = 1. Stronger than dimensional analysis, weaker than a UV microstate calc: it fixes the prefactor by countin... |
| · | `check_T_categorical_fourness` | theorem | `—` | Minimal horizon records form a category HRec with exactly four structure functors (S,E,I,L); necessity + independence + no-fewer + no-more bracket the count. Conditional: universal-mediation property posited, 'no more than four' by case-enumeration. The equivalence-tier upgrade is T_categorical_f... |
| · | `check_T_categorical_fourness_equivalence` | theorem | `—` | Every complete minimal horizon-record formalism C is equivalent to the four-projection category HRec (F_C full+faithful+ess.surjective). The integer 4 is representation-invariant -- not an enumeration artifact. Conditional only on the four-invariant set being a complete capture of the minimal ext... |
| · | `check_T_enforcement_area_quantization` | theorem | `—` | eps_P <-> l_P^2 = hbar G / c^3, the UNIQUE area monomial in the three substrate constants (a=1,b=-3,d=1; substrate matrix nonsingular). Dimensional analysis fixes the monomial up to an O(1) prefactor; the kappa=1 normalization is supplied by check_T_apf_planck_cell_normalization under the substra... |
| · | `check_T_four_commitment_record_cost` | theorem | `—` | One closed exterior horizon record costs eps_hor^min = N_commit * eps_P = 4 * eps_P (additive by independence; sharp; no lower-cost encoding). Hence the coefficient has the structural FORM 1/N_commit. UNCONDITIONAL. |
| · | `check_T_horizon_arealaw_microstate_consistency` | theorem | `—` | De Sitter area-quarter A/4 = 3*pi/(Lambda*G) = Omega = 102^61 ~ 3.3e122 (the microstate COUNT = the horizon area), and the de Sitter ENTROPY is its logarithm S_dS = ln(A/4) = 61*ln(102) = 282.123 nats. Area-law and microstate counting are consistent as count = area, entropy one log below -- not a... |
| · | `check_T_horizon_reindexing` | theorem | `—` | Horizon closure changes the admissibility codomain of bulk-local distinctions: Adm_bulk -> Adm_dH (boundary continuation constraints). The distinction is reindexed, not destroyed; the information paradox is the category error of identifying the two codomains. Geometric form already banked as L_gl... |
| · | `check_T_interior_non_admissibility_criterion` | theorem | `—` | Interior non-admissibility criterion: specializing A1 admissibility (+ Paper 2 failure-of-global-description) to interior labels, an interior refinement is an admissible physical codomain ONLY if reconstructed in an exterior codomain, OR assigned a declared codomain with a closed capacity ledger,... |
| · | `check_T_microtransport_sufficiency` | theorem | `—` | If evaporation supplies maps satisfying M1 (rank preservation), M2 (pairing preservation), M3 (four-role translation), M4 (stepwise composability), then it is information-preserving at the ledger level. Sufficiency theorem (near-tautological); actual realization is the open gate [C_actual_Hawking... |
| · | `check_T_radiation_correlation_space_sufficient` | theorem | `—` | If L_rad^corr has rank >= rank(L_H) and a compatible separation pairing, an isometric embedding V : L_H -> L_rad^corr exists -- the radiation codomain is in principle large enough. Structural sufficiency only; actual richness is the physical gate [C_actual_Hawking_radiation_correlation_richness]. |
| · | `check_T_thermal_marginals_no_ledger_loss` | theorem | `—` | Marginals do not determine the joint: a Bell state and the maximally-mixed product state share identical single-qubit marginals (I/2) but differ globally. So approximately-thermal one-mode marginals are compatible with ledger-bearing high-order correlations; the information need not appear in the... |

## `apf/i4_composition.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_I4_operator_self_identification` | theorem | `P_comp` | Four independent readings of ln Z(beta → 0) = ACC_scalar on the same H_micro: (A) direct partition-function trace (Phase 14d.2); (B) vacuum-projector trace with beta-sweep confirmation; (C) per-microstate uniform probability reading; (D) Paper 7 spectral-action / heat-kernel internalisation (L_sp... |

## `apf/ie_export_core_census.py` — 2 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_ie_export_core_dependency_census` | theorem | `—` | (no summary) |
| · | `T_ie_full_surface_input_inventory` | theorem | `—` | (no summary) |

## `apf/ie_onboarding_registry.py` — 5 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_ie_atlas_verdict_tripwire` | theorem | `—` | (no summary) |
| · | `T_ie_onboarding_registry_coverage` | theorem | `—` | (no summary) |
| · | `T_ie_plumbing_classification` | theorem | `—` | (no summary) |
| · | `T_ie_repair_frontier_census` | theorem | `—` | (no summary) |
| · | `T_ie_reviewer_manifest_current` | theorem | `P_structural_instrument` | The reviewer-facing artifacts (REVIEWER_ATLAS.md + artifacts/ie_atlas_export.json) are certified current against the pinned verdicts at every bank run: a reviewer reading the committed manifest rea... |

## `apf/ie_wall_shadow_census.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_ie_wall_shadow_census` | theorem | `—` | (no summary) |

## `apf/ijc_boolean_defender_bridge.py` — 3 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_boolean_defender_diagonal_npa_feasible` | theorem | `P_math` | From a Boolean defender on the (2,2,2) cover the diagonal projectors E_e = diag(rho(e)(lambda)) and state sigma = diag(p(lambda)) build a finite ALL-DIAGONAL (hence classical, commuting) realizatio... |
| · | `T_chsh_raw_count_confidence_box_local_exclusion` | theorem | `P_math` | A literal 4x4000-trial CHSH count table gives exact correlators (13/20,13/20,13/20,-13/20), balanced 1/2 marginals, S=13/5. For any half-width t with 4t < S-2 = 3/5 the confidence box's minimum of ... |
| · | `T_ijc_boolean_defender_bridge` | theorem | `P_structural_instrument` | On the (2,2,2) Bell-CHSH cover the structural FeasBool predicate is exact Boole-polytope membership: a local behaviour is SepStr with an explicit global section; the PR-box (S=4) is IJCStr with the... |

## `apf/ijc_feasbool_engine.py` — 4 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_feasbool_branch_taxonomy_four_verdicts` | theorem | `P_structural_instrument` | Three-layer cascade (Boole-polytope B1 / declared-preservation B2 / declared-ledger B3) computes exactly one of the four branch-exhaustivity verdicts: PR box -> structural IJC; local table -> SepAd... |
| · | `T_feasbool_general_contextuality` | theorem | `P_structural_instrument` | An exact rational LP decides Boole-polytope membership for an arbitrary finite scenario: SepStr returns the primal global section (hidden-variable model), IJCStr returns a Farkas dual (a generalize... |
| · | `T_ijc_constructive_noncommutator` | theorem | `P_structural_instrument` | Exact rational 2-qubit singlet realization with A0=sigma_z, A1=sigma_x and Bob at +-(3/5,4/5): correlators (-3/5,-3/5,-4/5,4/5) by trace (= -(a.b), cross-checked), CHSH \|S\|=14/5>2 so IJCStr, with [... |
| · | `T_ks_parity_contextuality_scalable` | theorem | `P_structural_instrument` | A Mermin-style parity (all-vs-nothing) scenario is consistent (noncontextual exists) iff its induced GF(2) parity system is consistent; KS = an inconsistent system (0=1), decided by exact Gaussian ... |

## `apf/initial_obstruction_classifier.py` — 7 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_APF_obstruction_object_free_monoid_P` | theorem | `—` | APF obstruction objects form the finite free idempotent commutative monoid generated by primitive descent-failure channels. |
| · | `check_T_compatible_classifier_targets_P` | theorem | `—` | Example target classifiers satisfy finite no-smuggling classifier compatibility. |
| · | `check_T_factorization_through_APF_Obs_P` | theorem | `—` | (no summary) |
| · | `check_T_initial_obstruction_classifier_theorem_P` | theorem | `—` | (no summary) |
| · | `check_T_initiality_minimality_P` | theorem | `—` | The primitive generator set is minimal: deleting any channel loses a distinct APF failure family. |
| · | `check_T_no_smuggling_universal_boundary_P` | theorem | `—` | Universal classifier boundary preserves no-smuggling: provenance failure cannot factor to export or ordinary repair. |
| · | `check_T_primitive_failure_generation_P` | theorem | `—` | Primitive obstruction channels are generated by distinct APF descent-failure axiom families. |

## `apf/interface_atlas.py` — 6 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_interface_atlas_P` | theorem | `—` | (no summary) |
| · | `check_T_interface_atlas_axis_typing_P` | theorem | `P_atlas_axis_typing` | Atlas engine-axis typing operational: mixed-axis input set produces per-axis summary with ROUTE + CODOMAIN axes; SC codomain row classified as COHERENT_CODOMAIN_SELECTED with export_global_P; cross-axis advisory note present (Reference doc Q2 starting position). |
| · | `check_T_interface_atlas_bottlenecks_P` | theorem | `—` | Interface atlas ranks repeated obstructions and failed structure kinds. |
| · | `check_T_interface_atlas_construction_P` | theorem | `—` | Interface atlas constructs route summaries across canonical claims and payloads. |
| · | `check_T_interface_atlas_shared_repairs_P` | theorem | `—` | Interface atlas identifies shared critical repair fields across route frontiers. |
| · | `check_T_interface_atlas_strategy_report_P` | theorem | `—` | Interface atlas emits a JSON strategy report suitable for integration dashboards. |

## `apf/interface_contextuality_adapter.py` — 2 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_interface_contextuality_adapter` | theorem | `P_structural_instrument` | interface_atlas.summarize_input now dispatches AxisKind.CONTEXTUALITY inputs to the FeasBool engine (mirroring the CODOMAIN axis). Routing CHSH-local / PR-box / magic-square / a consistent cycle th... |
| · | `T_interface_contextuality_general_scenario` | theorem | `P_structural_instrument` | interface_atlas.summarize_input now dispatches a full arbitrary-scenario CONTEXTUALITY payload to feasbool() (the exact Boole-polytope LP), not only the (2,2,2) correlator and parity shells. GHZ/Me... |

## `apf/interface_dark_posterior_evidence_intake.py` — 5 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_dark_empirical_posterior_remains_open` | theorem | `APF_INTERFACE_DARK_POSTERIOR_EVIDENCE_INTAKE_v1` | (no summary) |
| · | `check_T_dark_evaluator_map_candidate_present` | theorem | `APF_INTERFACE_DARK_POSTERIOR_EVIDENCE_INTAKE_v1` | (no summary) |
| · | `check_T_dark_intake_no_posterior_overclaim` | theorem | `APF_INTERFACE_DARK_POSTERIOR_EVIDENCE_INTAKE_v1` | (no summary) |
| · | `check_T_dark_posterior_evidence_intake_P` | theorem | `APF_INTERFACE_DARK_POSTERIOR_EVIDENCE_INTAKE_v1` | (no summary) |
| · | `check_T_dark_profile_probe_support_recorded` | theorem | `APF_INTERFACE_DARK_POSTERIOR_EVIDENCE_INTAKE_v1` | (no summary) |

## `apf/interface_engine_close_primitives.py` — 5 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_ie_activation_toggle_primitive` | theorem | `[P_structural]` | Reusable counterfactual verification primitive: the toggle test that certified the 3/13 placement is load-bearing, as the engine activation gate. |
| · | `T_ie_claim_kind_taxonomy` | theorem | `[P_structural]` | Reusable claim-classification ontology distilled from the loads-table retirement: a dependency list must be typed by kind, not tabulated as if uniform adopted assumptions. |
| · | `T_ie_codomain_obstruction_discriminator` | theorem | `[P_structural]` | Reusable engine discriminator distilled from the sin^2theta_W close: a codomain mismatch that makes an empirical difference must be resolved by structure (not assigned by fiat); one that makes none is a coordinative convention and is not an obstruction. |
| · | `T_ie_rerun_gate_audit_template` | theorem | `[P_structural]` | Reusable rerun-gate template: the audit that verified the sin^2theta_W [P] flip (verdict REDUCES) encoded as the engine promotion gate. |
| · | `T_ie_schur_placement_primitive` | theorem | `[P_structural]` | Reusable representation-descent primitive: attach a quantity to the representation whose invariant algebra constitutively contains it -- the factor with the minimal commutant dimension. The sin^2theta_W close used exactly this to place the radial-Higgs record on SU(2). |

## `apf/interface_evidence_rerun_controller.py` — 6 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_already_P_no_rerun_P` | theorem | `—` | Already-P cases do not generate unnecessary patches or reruns. |
| · | `check_T_blocked_cases_refuse_rerun_P` | theorem | `—` | Provenance and substrate-blocked cases refuse evidence patch/rerun. |
| · | `check_T_evidence_complete_triggers_rerun_P` | theorem | `—` | Complete evidence for ordinary minimal bundles triggers payload patching and rerun to global P. |
| · | `check_T_evidence_rerun_controller_boundary_P` | theorem | `—` | Controller distinguishes evidence readiness from rerun certification and reports before/after status. |
| · | `check_T_incomplete_evidence_blocks_rerun_P` | theorem | `—` | Incomplete evidence does not patch payload and does not rerun certification. |
| · | `check_T_interface_evidence_rerun_controller_P` | theorem | `—` | Interface Evidence Rerun Controller is P: complete evidence patches one minimal bundle and reruns certification, while incomplete/blocked cases do not rerun. |

## `apf/interface_ew_counterterm_uncertainty_intake.py` — 4 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_EW_counterterm_evidence_candidate_P` | theorem | `—` | (no summary) |
| · | `check_T_EW_counterterm_uncertainty_intake_P` | theorem | `—` | (no summary) |
| · | `check_T_EW_intake_does_not_promote_route_P` | theorem | `—` | (no summary) |
| · | `check_T_EW_uncertainty_evidence_candidate_P` | theorem | `—` | (no summary) |

## `apf/interface_factor_native.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_interface_algebra_is_factor_native_P` | theorem | `—` | (no summary) |

## `apf/interface_intelligence_CI_orchestrator.py` — 4 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_CI_module_target_coverage_P` | theorem | `—` | CI orchestrator covers the full interface-intelligence stack through atlas and real adapters. |
| · | `check_T_CI_report_generation_P` | theorem | `—` | (no summary) |
| · | `check_T_CI_top_checks_pass_P` | theorem | `—` | (no summary) |
| · | `check_T_interface_intelligence_CI_orchestrator_P` | theorem | `—` | (no summary) |

## `apf/interface_intelligence_E2E_artifact_pipeline.py` — 4 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_e2e_artifact_pipeline_collects_files_P` | theorem | `—` | E2E pipeline collects artifact files deterministically. |
| · | `check_T_e2e_artifact_pipeline_empty_safe_P` | theorem | `—` | E2E pipeline handles empty artifact folders without overclaiming. |
| · | `check_T_e2e_artifact_pipeline_runs_P` | theorem | `—` | (no summary) |
| · | `check_T_interface_intelligence_E2E_artifact_pipeline_P` | theorem | `—` | (no summary) |

## `apf/interface_intelligence_engineering_command_center.py` — 4 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_command_center_dashboard_P` | theorem | `—` | Command center renders an integrator dashboard with boundary language. |
| · | `check_T_command_center_dry_run_P` | theorem | `—` | (no summary) |
| · | `check_T_command_center_structure_P` | theorem | `—` | Engineering command center exposes runner and structured report objects. |
| · | `check_T_interface_intelligence_engineering_command_center_P` | theorem | `—` | (no summary) |

## `apf/interface_intelligence_failure_triage_assistant.py` — 4 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_failure_triage_detects_route_actions_P` | theorem | `—` | Failure triage detects held repair and provenance fail-closed route actions. |
| · | `check_T_failure_triage_detects_smoke_blocker_P` | theorem | `—` | Failure triage detects first missing-script smoke blocker. |
| · | `check_T_failure_triage_markdown_P` | theorem | `—` | Failure triage emits markdown with next action and boundary language. |
| · | `check_T_interface_intelligence_failure_triage_assistant_P` | theorem | `—` | Interface Intelligence Failure Triage Assistant is P: reports become prioritized next actions without overclaiming. |

## `apf/interface_intelligence_live_smoke_harness.py` — 4 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_interface_intelligence_live_smoke_harness_P` | theorem | `—` | (no summary) |
| · | `check_T_live_smoke_harness_dry_run_P` | theorem | `—` | (no summary) |
| · | `check_T_live_smoke_harness_structure_P` | theorem | `—` | Live smoke harness exposes required steps and structured summary objects. |
| · | `check_T_live_smoke_harness_text_summary_P` | theorem | `—` | Live smoke harness emits human-readable summary with boundary language. |

## `apf/interface_intelligence_post_install_acceptance_auditor.py` — 4 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_acceptance_auditor_accepts_complete_P` | theorem | `—` | (no summary) |
| · | `check_T_acceptance_auditor_blocks_failures_P` | theorem | `—` | Acceptance auditor blocks explicit failure evidence. |
| · | `check_T_acceptance_auditor_holds_missing_P` | theorem | `—` | Acceptance auditor holds empty/missing integrations. |
| · | `check_T_interface_intelligence_post_install_acceptance_auditor_P` | theorem | `—` | (no summary) |

## `apf/interface_intelligence_registry_bridge.py` — 6 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_interface_intelligence_registry_bridge_P` | theorem | `—` | Interface Intelligence Registry Bridge is P: all top checks are manifest-defined, importable, registrable, and patch-emittable. |
| · | `check_T_registry_bridge_generated_patches_P` | theorem | `—` | Registry bridge generates bank-registration and verify_all integration snippets. |
| · | `check_T_registry_bridge_imports_ready_P` | theorem | `—` | Registry bridge can import every interface-intelligence top check. |
| · | `check_T_registry_bridge_manifest_complete_P` | theorem | `—` | Registry bridge manifest covers all interface-intelligence top checks. |
| · | `check_T_registry_bridge_registers_dict_P` | theorem | `—` | Registry bridge registers checks into dict/update registries. |
| · | `check_T_registry_bridge_registers_object_P` | theorem | `—` | Registry bridge supports object registries exposing register() or add(). |

## `apf/interface_intelligence_release_manifest.py` — 4 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_interface_intelligence_release_manifest_P` | theorem | `—` | Interface Intelligence Release Manifest is P: install order, markers, top checks, and boundaries are auditable. |
| · | `check_T_release_manifest_boundary_P` | theorem | `—` | Release manifest preserves live-bank and physics-claim boundaries. |
| · | `check_T_release_manifest_layer_count_P` | theorem | `—` | Release manifest covers all engineering layers through command center. |
| · | `check_T_release_manifest_writes_files_P` | theorem | `—` | Release manifest writes JSON/Markdown/CSV/top-check artifacts. |

## `apf/interface_intelligence_reviewer_reporter.py` — 4 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_interface_intelligence_reviewer_reporter_P` | theorem | `—` | Interface Intelligence Reviewer Reporter is P: JSON interface reports become reviewer-safe status language. |
| · | `check_T_reviewer_reporter_classifies_status_P` | theorem | `—` | Reviewer reporter classifies banked/held/provenance/structural statuses. |
| · | `check_T_reviewer_reporter_markdown_P` | theorem | `—` | Reviewer reporter renders markdown status tables with boundary language. |
| · | `check_T_reviewer_reporter_safe_language_P` | theorem | `—` | Reviewer reporter emits conservative claim-boundary language and next evidence fields. |

## `apf/interface_kinematic_holonomy_diagnostics.py` — 5 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_holonomy_field_memory_P` | theorem | `—` | Holonomy detects residual memory/state defect for incomplete return path. |
| · | `check_T_holonomy_flat_canonical_P` | theorem | `—` | Holonomy diagnostic recognizes flat canonical loop. |
| · | `check_T_holonomy_order_curvature_P` | theorem | `—` | Holonomy detects order curvature when return path violates prerequisites. |
| · | `check_T_holonomy_provenance_priority_P` | theorem | `—` | Holonomy preserves provenance fail-closed priority. |
| · | `check_T_interface_kinematic_holonomy_diagnostics_P` | theorem | `—` | Interface Kinematic Holonomy Diagnostics is P: closed interface loops are tested for flat return, residual memory, order curvature, and hard-stop propagation. |

## `apf/interface_kinematic_invariants.py` — 5 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_interface_kinematic_invariants_P` | theorem | `—` | Interface Kinematic Invariants is P: payload transitions are audited for progress, capacity, provenance, blocked-field, and export invariants. |
| · | `check_T_invariant_capacity_worsening_P` | theorem | `—` | Invariant audit catches capacity-class worsening. |
| · | `check_T_invariant_monotone_repair_P` | theorem | `—` | Invariant audit recognizes monotone evidence repair. |
| · | `check_T_invariant_provenance_violation_P` | theorem | `—` | Invariant audit catches provenance contamination as violation. |
| · | `check_T_invariant_signature_EW_P` | theorem | `—` | Invariant signature records EW blocked-field/progress state. |

## `apf/interface_kinematic_phase_space_atlas.py` — 4 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_interface_kinematic_phase_space_atlas_P` | theorem | `—` | Interface Kinematic Phase-Space Atlas is P: route payloads map into state-space coordinates, bottlenecks, repair distances, and markdown summaries. |
| · | `check_T_phase_space_atlas_counts_P` | theorem | `—` | Phase-space atlas aggregates route/region/status/bottleneck counts. |
| · | `check_T_phase_space_markdown_P` | theorem | `—` | Phase-space atlas renders reviewer/integrator markdown. |
| · | `check_T_phase_space_points_P` | theorem | `—` | Phase point maps EW open payload into typed region with codomain bottleneck. |

## `apf/interface_kinematic_solver.py` — 5 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_interface_kinematic_solver_P` | theorem | `—` | Interface Kinematic Solver is P: it computes minimal repair fields, closure depth, and hard-stop classes. |
| · | `check_T_kinematic_solver_EW_repair_path_P` | theorem | `—` | Kinematic solver derives ordered EW repair fields. |
| · | `check_T_kinematic_solver_dark_exportable_P` | theorem | `—` | Kinematic solver recognizes already exportable dark route. |
| · | `check_T_kinematic_solver_fail_closed_P` | theorem | `—` | Kinematic solver refuses evidence patching for provenance fail-closed states. |
| · | `check_T_kinematic_solver_hypothetical_patch_P` | theorem | `—` | Kinematic solver can test hypothetical repair closure without treating patch as evidence. |

## `apf/interface_kinematics_composition.py` — 5 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_composition_capacity_overspend_P` | theorem | `—` | Composition detects shared capacity overspend even when individual routes export. |
| · | `check_T_composition_provenance_propagation_P` | theorem | `—` | Composition propagates provenance fail-closed status. |
| · | `check_T_composition_shared_field_nonclosure_P` | theorem | `—` | Composition detects non-closure from unresolved shared interface fields. |
| · | `check_T_composition_two_exportable_paths_P` | theorem | `—` | Composition succeeds for exportable paths within capacity. |
| · | `check_T_interface_kinematics_composition_P` | theorem | `—` | Interface Kinematics Composition is P: individual path certificates are checked for non-closure, shared field conflicts, capacity overspend, and fail-closed propagation. |

## `apf/interface_kinematics_engine.py` — 5 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_interface_kinematics_engine_P` | theorem | `—` | Interface Kinematics Engine is P: route payloads produce states, transition paths, first blocked moves, and repair-state targets. |
| · | `check_T_kinematics_EW_path_P` | theorem | `—` | EW kinematics halts at the first missing codomain transport move. |
| · | `check_T_kinematics_capacity_overspend_P` | theorem | `—` | Capacity kinematics detects overspend after coarse-graining. |
| · | `check_T_kinematics_dark_export_P` | theorem | `—` | Dark route kinematics reaches GLOBAL_EXPORTABLE when every transition field is satisfied. |
| · | `check_T_kinematics_provenance_fail_closed_P` | theorem | `—` | Kinematics fail-closes provenance before ordinary transition repair. |

## `apf/interface_kinematics_order_defects.py` — 5 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_interface_kinematics_order_defects_P` | theorem | `—` | Interface Kinematics Order Defects is P: transition orders are checked for prerequisite, path-dependence, commutation, and provenance-priority defects. |
| · | `check_T_order_defects_adjacent_table_P` | theorem | `—` | Order-defect engine emits adjacent commutation diagnostics. |
| · | `check_T_order_defects_canonical_P` | theorem | `—` | Canonical route order is admissible when transition fields are satisfied. |
| · | `check_T_order_defects_prerequisite_violation_P` | theorem | `—` | Order defects catch evaluator-before-transport prerequisite violation. |
| · | `check_T_order_defects_provenance_boundary_P` | theorem | `—` | Order-defect engine preserves provenance fail-closed priority. |

## `apf/interface_live_blocker_work_queue.py` — 4 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_interface_live_blocker_work_queue_P` | theorem | `—` | (no summary) |
| · | `check_T_live_blocker_inventory_P` | theorem | `—` | (no summary) |
| · | `check_T_queue_does_not_promote_routes_P` | theorem | `—` | (no summary) |
| · | `check_T_work_items_have_evidence_requirements_P` | theorem | `—` | (no summary) |

## `apf/interface_movement_graph_repair_planner.py` — 5 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_graph_repair_actions_from_witnesses_P` | theorem | `—` | Repair planner converts obstruction witness edges into concrete route-specific actions. |
| · | `check_T_graph_repair_classification_P` | theorem | `—` | Repair planner classifies exact, ordinary repair, substrate revision, and fail-closed provenance cases. |
| · | `check_T_graph_repair_closure_predicates_P` | theorem | `—` | Repair plans produce explicit P-closure conditions. |
| · | `check_T_graph_repair_ordering_P` | theorem | `—` | Repair actions are priority ordered and exact cases do not require rerun. |
| · | `check_T_interface_movement_graph_repair_planner_P` | theorem | `—` | Interface Movement Graph Repair Planner is P: failed movement edges become ordered repair actions with closure predicates. |

## `apf/interface_readout_adapter.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_interface_readout_axis_adapter` | theorem | `—` | (no summary) |

## `apf/interface_repair_closure_simulator.py` — 5 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_exact_case_no_patch_P` | theorem | `—` | Exact/closed cases produce no unnecessary repair patches. |
| · | `check_T_interface_repair_closure_simulator_P` | theorem | `—` | Interface Repair Closure Simulator is P: ordinary repairs can be counterfactually patched and rerun, while provenance/structural blockers refuse auto-patching. |
| · | `check_T_ordinary_repair_simulates_to_P_P` | theorem | `—` | Ordinary repair cases have candidate payload patches that simulate closure to global P. |
| · | `check_T_patch_semantics_are_counterfactual_P` | theorem | `—` | Closure simulation language preserves the no-smuggling boundary: patches are counterfactual checks, not executed physics. |
| · | `check_T_provenance_and_structural_refuse_autopatch_P` | theorem | `—` | Simulator refuses provenance and substrate/structural auto-patching. |

## `apf/interface_repair_frontier_explorer.py` — 5 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_frontier_critical_fields_are_in_every_bundle_P` | theorem | `—` | Critical fields are exactly fields common to every minimal closing bundle. |
| · | `check_T_frontier_exact_cases_no_bundle_P` | theorem | `—` | Already closed cases have no artificial repair frontier. |
| · | `check_T_frontier_finds_minimal_ordinary_bundles_P` | theorem | `—` | Frontier explorer finds minimal closing bundles for ordinary repair cases. |
| · | `check_T_frontier_refuses_blocked_cases_P` | theorem | `—` | Frontier explorer refuses provenance and substrate/structural auto-frontiers. |
| · | `check_T_interface_repair_frontier_explorer_P` | theorem | `—` | Interface Repair Frontier Explorer is P: it finds minimal ordinary repair bundles, critical fields, and refuses blocked/provenance frontiers. |

## `apf/interface_repair_obligation_compiler.py` — 5 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_evidence_template_and_validation_P` | theorem | `—` | Evidence templates validate to ready-to-rerun only after at least one minimal bundle is fully supplied. |
| · | `check_T_interface_repair_obligation_compiler_P` | theorem | `—` | Interface Repair Obligation Compiler is P: minimal repair bundles become auditable evidence obligations and ready-to-rerun packets. |
| · | `check_T_obligation_blocked_cases_P` | theorem | `—` | Obligation compiler refuses evidence packets for provenance and substrate-blocked cases. |
| · | `check_T_obligation_packet_compilation_P` | theorem | `—` | Minimal repair frontiers compile into evidence obligation packets. |
| · | `check_T_ready_to_rerun_is_not_truth_assertion_P` | theorem | `—` | Ready-to-rerun means evidence obligations are filled; it does not assert the original route is already P. |

## `apf/interface_solver_descent_bridge.py` — 7 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_bridge_certificates_status_P` | theorem | `—` | Interface solver bridge emits correct solver/promotion statuses for canonical problems. |
| · | `check_T_bridge_no_overpromotion_P` | theorem | `—` | Interface solver bridge enforces no-overpromotion: global export iff zero obstruction. |
| · | `check_T_bridge_obstruction_certificates_P` | theorem | `—` | Interface solver bridge produces expected obstruction certificates from raw solver outputs. |
| · | `check_T_bridge_repair_and_next_action_P` | theorem | `—` | Interface solver bridge emits repair plans and next actions suitable for solver routing. |
| · | `check_T_interface_solver_descent_bridge_P` | theorem | `—` | Interface Solver Descent Bridge is P: solver outputs are certified by obstruction, repair, and promotion gates. |
| · | `check_T_interface_solver_problem_schema_no_expected_labels_P` | theorem | `—` | Interface solver problem schema uses raw solver outputs only; no expected-label leakage. |
| · | `check_T_problem_to_sector_metadata_translation_P` | theorem | `—` | Interface solver outputs translate correctly into sector metadata. |

## `apf/interface_solver_engineering_extensions.py` — 6 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_batch_certification_P` | theorem | `—` | Batch certification produces JSON/CSV-ready outputs and summaries. |
| · | `check_T_ci_policy_gate_P` | theorem | `—` | CI policy gate distinguishes permissive research, strict global export, and fail-closed provenance. |
| · | `check_T_engineering_contract_validation_P` | theorem | `—` | Strict contract validation works and rejects expected-label leakage. |
| · | `check_T_interface_solver_engineering_extensions_P` | theorem | `—` | Interface solver engineering extensions are P: strict contracts, batch certification, CI gates, reports, and adapters pass. |
| · | `check_T_report_generation_P` | theorem | `—` | Markdown and JSON certification reports render successfully. |
| · | `check_T_route_adapter_templates_P` | theorem | `—` | Route adapter templates produce certifiable InterfaceSolverProblem objects. |

## `apf/interface_structure_discovery_engine.py` — 5 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_discovery_payload_to_ledger_P` | theorem | `—` | Raw route payloads discover typed interface-structure ledgers. |
| · | `check_T_expected_label_leakage_rejected_P` | theorem | `—` | Discovery engine rejects expected-label/certificate leakage in payloads. |
| · | `check_T_interface_structure_discovery_engine_P` | theorem | `—` | Interface Structure Discovery Engine is P: raw route payloads discover typed moving-structure ledgers, certify them, and witness every obstruction. |
| · | `check_T_obstruction_structure_witnesses_P` | theorem | `—` | Every nonzero obstruction has at least one moving-structure witness in the discovered ledger. |
| · | `check_T_zero_obstruction_inventory_clean_P` | theorem | `—` | A zero-obstruction export case has no missing, blocked, or provenance-failed required structures. |

## `apf/interface_structure_movement_graph.py` — 5 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_interface_structure_movement_graph_P` | theorem | `—` | Interface Structure Movement Graph is P: moving structures are explicit source-target edges and every obstruction has a witness path. |
| · | `check_T_movement_graph_construction_P` | theorem | `—` | Canonical route payloads construct explicit source-target movement graphs with typed edges. |
| · | `check_T_movement_graph_kind_coverage_P` | theorem | `—` | Movement graph coverage includes all currently typed interface-moving structure kinds. |
| · | `check_T_obstruction_witness_paths_P` | theorem | `—` | Every nonzero obstruction is witnessed by at least one source->structure->target path. |
| · | `check_T_zero_export_has_clean_graph_P` | theorem | `—` | Every global-export example has a clean movement graph: no failed required edges and zero obstruction. |

## `apf/interface_structure_transport_ledger.py` — 5 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_every_certificate_has_pre_obstruction_inventory_P` | theorem | `—` | Every canonical solver certificate is preceded by a typed inventory of moving structures. |
| · | `check_T_interface_structure_transport_ledger_P` | theorem | `—` | Interface Structure Transport Ledger is P: it inventories moving structures before obstruction/promotion certification and generalizes the trace transport ledger architecture. |
| · | `check_T_ledger_to_solver_certificate_P` | theorem | `—` | Typed structure ledgers translate into v24.3.12 interface-solver certificates with expected statuses. |
| · | `check_T_structure_kind_inventory_P` | theorem | `—` | Interface structure kind inventory covers trace, scheme, capacity, codomain, evaluator, gluing, provenance, fiber, substrate, empirical, constants, counterterms, and uncertainty protocol. |
| · | `check_T_trace_transport_ledger_generalization_P` | theorem | `—` | EW trace transport ledger architecture is represented as an instance of the general interface structure ledger. |

## `apf/itpfi_tail_scalar_native.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `L_itpfi_tail_acts_scalar_on_omega_native` | lemma | `[P]` | Native scalar-on-Omega lemma -- the import-free core of tail-triviality. Steps (i)-(iii) (ampliation lemma (B(K)(x)I)'=I(x)B(H); product-state GNS factorization; cyclicity) prove z Omega = phi(z).Omega for every tail element, with NO Araki-Woods modular structure and NO commutation theorem. SCOPE... |

## `apf/kappa_int_bounds.py` — 6 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_R1_R4_spine_derivable` | theorem | `[P_structural]` | R1-R4 are derivable consequences of the 4-input declaration + the operational structure of physical interrogation, not four regularity hypotheses added on top of the spine.  R1 is automatic via the finite-interrogation theorem; R2 is built into FD2's definition; R3 is structurally automatic from ... |
| · | `T_kappa_int_lower_bound` | theorem | `[P_structural]` | Marginal-floor lemma (Lemma `lem:marginal-floor-on-joint-cost`) + sum-of-floors corollary (Corollary `cor:sum-of-floors-lower-bound`) + structural lower bound (Theorem `thm:kappa-int-singleton-shape`) all witnessed on a finite toy interface. The lower bound is unconditional (any finite physical r... |
| · | `T_kappa_int_two_sided_rigidity` | theorem | `[P_structural]` | Two-sided structural rigidity (Theorem `thm:kappa-int-two-sided-bound`) witnessed on a finite C1-C5 toy interface. The lower bound (n·ε* - Σκ(d), unconditional from MD via BW) and the upper bound (I_int^+ · Σ_{i≠j} \|φ_i\|\|φ_j\|, conditional on C1-C5) jointly determine the structural shape of κ_int ... |
| · | `T_kappa_int_upper_bound_C1C5` | theorem | `[P_structural]` | Continuum-bridge upper bound (Theorem `thm:kappa-int-binary-upper-bound`) + far-separation exponential suppression (Corollary `cor:kappa-int-far-separation`) + singleton-form upper bound (Corollary `cor:kappa-int-singleton-upper-bound`) all witnessed on a finite toy interface satisfying C1-C5. Th... |
| · | `T_kappa_int_upper_bound_topological_gap_regime_restricted_P` | theorem | `[P_structural_topological_regime_restricted]` | Upper bound κ_int(S) ≤ Δ_top · N_defects(S) on the interface-cost residue, regime-restricted to substrates declaring a positive bulk gap Δ_top, finite ground-state degeneracy, no anti-cooperative coupling scale exceeding Δ_top, and Δ_top independent of the per-distinction floor ε*_Γ. The bound is... |
| · | `T_minimum_distinction_floor_via_MD` | theorem | `[P_structural]` | Theorem thm:minimum-distinction-floor (Paper 1 supplement v8.31 §11) witnessed.  By MD, every physical distinction has cost ≥ ε* > 0; for any nonempty admissible family Q ⊂ D_Γ, the floor μ_Γ(Q) := inf κ_Γ(d) is bounded below by ε* by uniform pointwise lower bound.  No compactness, no lower semic... |

## `apf/killed_rivals.py` — 5 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `R_Born_axiomatic_killed` | other | `P_structural_exhaustive` | Rival framework that postulates the Born rule P(a_n) = \|<a_n\|psi>\|^2 as a primitive axiom is strictly dominated by T_Born + T2 (apf.core). T_Born derives the Born rule from A1 + L_irr + admissibility; T2 supplies the Gleason countably-additive frame-function premise. The rival postulates a result... |
| · | `R_Ngen_neq_3_killed` | other | `P_structural_exhaustive` | Rival generation count N_gen =/= 3 is killed by T7. C_EW = kappa * channels = 2 * 4 = 8 is the electroweak capacity ceiling; E(N) = N(N+1)/2 is the triangular per-generation cost. Enumeration over N_gen in {1,2,3,4,5}: N_gen in {1,2} subsaturated (T7 max-selection picks 3); N_gen in {4,5} oversat... |
| · | `R_SU_Nc_neq_3_killed` | other | `P_structural_exhaustive` | Rival gauge group SU(N_c), N_c =/= 3, is dominated by the v6.9 derivation of N_c = 3 via Theorem_R (R1 non-abelian carrier requirement) plus T_gauge (capacity-cost minimum). Enumeration over N_c in [2, 3, 4, 5, 6, 7]: N_c=2 killed by R1; N_c in {4,5,6,7} dominated by E_gauge cost ranking (N_c=3 u... |
| · | `R_extra_axiom_NT_killed` | other | `P_structural_exhaustive` | Rival framework with a non-trivial extra axiom beyond A1 plus the four PLEC components (A1, MD, A2, BW) is killed by enumeration over four candidate extra axioms historically treated as primitive: Lorentz invariance, gauge invariance, Born rule, Lagrangian density existence. Each is either derive... |
| · | `T_killed_rivals_v0` | theorem | `P_structural_exhaustive` | Composed kill: the four rival physical-theory architectures locked in Phase 14b §14b.0 v0 (R_SU_Nc_neq_3, R_Ngen_neq_3, R_extra_axiom_NT, R_Born_axiomatic) are all killed by load-bearing v6.9 bank theorems (Theorem_R + T_gauge for kill 1; T7 for kill 2; A1 + PLEC components for kill 3 via 4-candi... |

## `apf/kinematics_adjudication_engine.py` — 3 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_kinematics_adjudication_engine_audit_first_P` | theorem | `P_kinematics_engine_audit_first` | Audit-first discipline preserved across all verdict cases: target_value_consumed + kinematic_dynamics_imported + phase_space_volume_consumed all = 0; no engine smuggling. |
| · | `check_T_kinematics_adjudication_engine_entry_point_P` | theorem | `P_kinematics_engine_entry_point` | Entry point produces verdicts: no-payload -> OPEN_EVIDENCE_REQUIRED with payload_missing; with-payload -> valid kinematic verdict status with target_engine declared correctly. |
| · | `check_T_kinematics_adjudication_engine_identity_P` | theorem | `P_kinematics_engine_identity` | Kinematics Adjudication Engine declares Tier 2 role + IE family membership; 6-status verdict taxonomy + 3 preserved non-claims. |

## `apf/l_irr_induced_polarity.py` — 5 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_L_irr_polarity_antimultiplicative` | theorem | `—` | *-algebra axiom (ii) antimultiplicativity: (ba)* = a*b* on substrate-side continuations |
| · | `check_T_L_irr_polarity_involution` | theorem | `—` | *-algebra axiom (i) involution: (D*)* = D for every distinction at every alignment |
| · | `check_T_L_irr_polarity_star_axioms_i_ii` | theorem | `—` | L_irr-induced polarity supplies substrate-side *-algebra axioms (i) involution and (ii) antimultiplicativity on the partial fibration's morphism algebra. Dissolves Fact 1 of the cross-interface algebraic impossibility theorem (v0.2). Strong-form Resolution (iii) still blocked by Fact 3 (cost-enri... |
| · | `check_T_L_irr_polarity_substrate_primitive` | theorem | `—` | L_irr-induced polarity construction uses only substrate-side primitives + eternalist commitment; no external imports |
| · | `check_T_L_irr_polarity_well_defined` | theorem | `—` | L_irr-induced polarity is well-defined on the substrate's partial order of class-transition histories |

## `apf/lambda_absolute.py` — 6 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_Lambda_absolute_bulletproof` | theorem | `P` | Composed bulletproof theorem for APF's Lambda-absolute prediction. Four passes, all passing: (1) numerical identity rho_Lambda/M_Pl^4 = 42/102^62 matches observation to 0.034 decades [P]; (2) extended formula matches rho_crit, rho_b, rho_c, rho_Lambda all to within 0.035 decades simultaneously at... |
| · | `T_Lambda_absolute_extended_formula` | theorem | `P` | The Lambda-absolute formula rho_X / M_Planck^4 = C_X / d_eff^(K_SM + 1) = C_X / 102^62 matches all four observed cosmological density components (rho_crit, rho_b, rho_c, rho_Lambda) to within 0.035 decades (8%) simultaneously: rho_crit at C_X=61, rho_b at C_X=3, rho_c at C_X=16, rho_Lambda at C_X... |
| · | `T_Lambda_coefficient_degeneracy_audit` | theorem | `P_structural_convention` | The Lambda coefficient is not one of ~13 numerical near-coincidences: it is forced by FORM. The bare scale factors exactly, d_eff^(-K_SM) = exp(-S_dS) (de Sitter horizon entropy, T11), so rho_Lambda/M_Pl^4 = (C_vacuum/d_eff) * exp(-S_dS) = (vacuum admissibility fraction) x (horizon suppression), ... |
| · | `T_Lambda_operator_model_verification` | theorem | `P_structural_instrument` | Operator-level identity tr(P_vac_at_slot_1) / dim H_micro = C_vac * d_eff^(K-1) / d_eff^K = C_vac / d_eff verified at 6 model interfaces, including the SM interface (K=61, d_eff=102, C_vac=42) where the ratio reduces to 7/17 = 7/17. This rigorously identifies the Lambda-absolute coefficient C_vac... |
| · | `T_Lambda_to_H0_inversion` | theorem | `P_structural_reading` | APF's two bank-forced predictions — Omega_Lambda = 42/61 = 0.6885 and rho_Lambda/M_Pl^4 = 42/102^62 = 10^-122.910 — combined with the standard GR critical-density formula rho_crit = 3 H_0^2 M_Pl^2 / (8 pi), invert algebraically to give H_0_APF = sqrt(8 pi * 61 / 3) / 102^31 * M_Pl = 70.03 km/s/Mp... |
| · | `T_ew_lambda_unified_suppression` | theorem | `P_structural_convention` | Unifies the two hierarchies. v_H^2/M_Pl^2 = pref_EW^2*exp(-S_bos), S_bos=C_boson*sigma=16*ln(102); rho_Lambda/M_Pl^4 = (C_vacuum/d_eff)*exp(-S_dS), S_dS=C_total*sigma=61*ln(102). Same object: a Planck scale times an order-unity capacity prefactor times the single-microstate occupation exp(-S) of ... |

## `apf/lambda_operator_derivation.py` — 4 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_Lambda_Planck_scale_ansatz` | theorem | `C` | Residual Planck-scale ansatz pinpointed in the Phase 14d.2 derivation: eps_Planck = M_Planck identifies the per-slot vacuum-energy scale as Planckian. This is a dimensional input external to APF; M_Planck arises via the Einstein-Hilbert gravitational coupling, not from A1 or the two-tier admissib... |
| · | `T_Lambda_d2_operator_derivation` | theorem | `P` | Composed Phase 14d.2 derivation of the Lambda-absolute formula rho_vac = (C_vac/d_eff) * M_Planck^4 / N_SM at the operator-algebra level. Three-pass structure: (1) Partition-function identities (A)+(B)+(C) at β → 0 verified to machine precision at six test interfaces [P]; (2) β-sweep confirming <... |
| · | `T_Lambda_partition_function_at_beta_zero` | theorem | `P` | At every test interface in [(1, 2, 1), (2, 3, 2), (3, 4, 2), (3, 5, 3), (4, 3, 2), (5, 4, 2)], the β → 0 thermal limit of the explicit H_micro density matrix gives: (A) ln Z = K ln(d_eff) = ACC (partition function limit); (B) <P_vac_slot_i> = C_vac/d_eff (vacuum projector expectation); (C) per-mi... |
| · | `T_Lambda_vacuum_projector_operator_identity` | theorem | `P_structural_instrument` | Operator-level β-sweep at model (K=3, d_eff=4, C_vac=2) confirms: at β = 100 (low T, ground state), <P_vac_slot_0> = 1.000000 → 1 (all slots in vacuum). At β = 1e-4 (high T, near max-mixed), <P_vac_slot_0> = 0.500025 → 0.5 = C_vac/d_eff. The coefficient in the Lambda-absolute formula is the β → 0... |

## `apf/laser_coherence_codomain_adapter.py` — 4 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_laser_coherence_codomain_adapter_atlas_contract_P` | theorem | `P_codomain_adapter_atlas_contract` | Laser coherence adapter declares the CODOMAIN atlas contract; live payload reaches COHERENT via the engine. |
| · | `check_T_laser_coherence_codomain_adapter_audit_first_P` | theorem | `P_codomain_adapter_audit_first` | Audit-first non-claims preserved; target not consumed; evaluator ledger declared. |
| · | `check_T_laser_coherence_codomain_adapter_payload_contract_P` | theorem | `P_codomain_adapter_contract` | Laser coherence codomain adapter payload carries the required fields and routes through the engine. |
| · | `check_T_laser_coherence_codomain_adapter_verdict_consistent_P` | theorem | `P_codomain_adapter_verdict_consistent` | Installed Laser coherence runtime reproduces every fixture verdict through the engine. |

## `apf/light_quark_real_adapter.py` — 6 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_light_quark_adapter_certification_P` | theorem | `—` | EVALUATOR_MAP edge in the movement graph resolves to MOVES_CLEANLY with FLAG-filled payload. |
| · | `check_T_light_quark_adapter_external_ledger_declared_P` | theorem | `—` | All 9 required external evaluator fields declared on the snapshot. |
| · | `check_T_light_quark_adapter_flag_kernel_consistent_P` | theorem | `—` | FLAG K_min diagonal transports APF trace (1.153, 3.871, 87.143) MeV onto FLAG (2.14, 4.70, 93.46) MeV targets. |
| · | `check_T_light_quark_adapter_no_smuggling_P` | theorem | `—` | No FLAG / PDG target value appears as a route payload input. |
| · | `check_T_light_quark_adapter_payload_contract_P` | theorem | `—` | Light-quark adapter produces EW-shaped route payload with FLAG-filled evaluator + codomain. |
| · | `check_T_light_quark_real_adapter_P` | theorem | `—` | Light-quark real adapter wires banked FLAG-derived kernel content into Engine-readable route payload; EVALUATOR_MAP edge fills cleanly; no smuggling; 9-field external ledger declared. |

## `apf/magnetism_codomain_adapter.py` — 4 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_magnetism_codomain_adapter_atlas_contract_P` | theorem | `P_codomain_adapter_atlas_contract` | Magnetism adapter declares the CODOMAIN atlas contract; live payload reaches COHERENT via the engine. |
| · | `check_T_magnetism_codomain_adapter_audit_first_P` | theorem | `P_codomain_adapter_audit_first` | Audit-first non-claims preserved; target not consumed; evaluator ledger declared. |
| · | `check_T_magnetism_codomain_adapter_payload_contract_P` | theorem | `P_codomain_adapter_contract` | Magnetism codomain adapter payload carries the required fields and routes through the engine. |
| · | `check_T_magnetism_codomain_adapter_verdict_consistent_P` | theorem | `P_codomain_adapter_verdict_consistent` | Installed Magnetism runtime reproduces every fixture verdict through the engine. |

## `apf/mcross_planck_ratio_composition.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_mcross_planck_ratio_composition` | theorem | `P_structural_reading` | The single-anchor scale-web named M_cross/M_Pl as the lone un-collapsed ratio -- a surface stale in its GRADE LABELS and its sin^2theta_W-gate identification; the 'open content = v_H/M_Pl' pin is a deliberate fence that STANDS (the .314 no-go proves the form v_H/M_Pl is not base-derivable), so th... |

## `apf/mw_value_from_equilibrium_and_custodial.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_mw_value_equilibrium_plus_custodial_no_loop_construction` | theorem | `P_structural_mw_value_equilibrium_plus_custodial_modulo_absolute_scale_and_alpha_had` | Makes explicit on the bank side what physically sets the W mass in the distinction picture, retiring the loop-expansion framing for the electroweak radiative face. Two native mechanisms, no diagram sum: (1) the weak mixing angle is a distinction-partition equilibrium (sin²θ_W = 3/13, T_sin2theta ... |

## `apf/negative_temperature_ceiling.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_negative_temperature_needs_the_ceiling` | theorem | `P` | A system admits negative temperature iff its energy spectrum is bounded above; FD4's ceiling (n <= C_total) makes the distinction ledger one. The ceiling is load-bearing: the bounded Z(beta) is finite for every real beta, so infinite temperature (beta=0) and negative temperature (beta<0) exist --... |

## `apf/neutrino_mbb_reconciliation.py` — 4 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `L_mbb_canonical_source` | lemma | `P_local` | L_mbb_canonical_source: computed 0nubb effective mass source |
| · | `L_mbb_confrontation_uses_canonical_source` | lemma | `P_local` | L_mbb_confrontation_uses_canonical_source: 0nubb wrapper synchronized |
| · | `T_mbb_transport_certificate` | theorem | `P` | Packages the 0nubb transport certificate from the two banked [P] checks. Source: m_bb = 4.42 meV (L_mbb_prediction [P + Delta m^2_31]). Kernel: Sum \|U_ei\|^2 m_i with U_ei from T_PMNS [P], masses from L_dm2_hierarchy + Delta m^2_31, Majorana phases derived zero (seesaw reality -> constructive sum ... |
| · | `T_neutrino_mbb_reconciled` | theorem | `P_local` | T_neutrino_mbb_reconciled: canonical and confrontation values agree |

## `apf/neutrino_mbb_reconciliation_real_adapter.py` — 3 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_neutrino_mbb_reconciliation_adapter_atlas_routes_P` | theorem | `—` | Atlas routes neutrino m_bb reconciliation payload to INTERNAL_IDENTITY_GLOBAL_P. |
| · | `check_T_neutrino_mbb_reconciliation_adapter_closure_kind_P` | theorem | `—` | neutrino m_bb reconciliation adapter declares closure_kind=internal_identity (framework structural export). |
| · | `check_T_neutrino_mbb_reconciliation_adapter_registry_pointer_P` | theorem | `—` | neutrino m_bb reconciliation adapter cites registry pointer. |

## `apf/obligation_packet_meta_schema.py` — 4 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_obligation_packet_codomain_subtype_P` | theorem | `P_codomain_subtype` | Codomain Selection packets wrap cleanly into meta-schema across multiple verdict cases: positive (COHERENT_CODOMAIN_SELECTED with no_obligation) + no-runtime (OPEN_EVIDENCE_REQUIRED with runtime evaluator missing). Common fields populated (target_engine=codomain_selection; target_unit_id=regime:N... |
| · | `check_T_obligation_packet_meta_schema_identity_P` | theorem | `P_meta_schema_identity` | Meta-schema declares 6 required common fields (obligation_kind + target_engine + target_unit_id + evidence_required + current_status + recommended_next_action) and 5 engine subtypes (ROUTE_ADJUDICATION + CODOMAIN_SELECTION) per Reference doc Q3 starting position. |
| · | `check_T_obligation_packet_route_subtype_P` | theorem | `P_route_subtype` | Route Adjudication packet wraps cleanly into meta-schema: 6 common fields populated correctly (target_engine=route_adjudication; target_unit_id=ew sector; evidence_required from critical_fields); engine_subtype_data preserves bundles + original_certificate + frontier_status etc.; audit-first non-... |
| · | `check_T_obligation_packet_uniform_inspector_P` | theorem | `P_uniform_inspector` | Uniform inspect_packet() reads Route Adjudication + Codomain Selection packets with same return shape (PacketInspectionResult with identical common_fields keys). Engine subtype data preserved per-engine. Audit-first non-claims preserved across both wrappings. |

## `apf/obstruction_dynamics.py` — 10 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_coarse_graining_relief_P` | theorem | `—` | Coarse-graining can relieve logistical pressure but not structural absences or provenance smuggling. |
| · | `check_T_declared_transport_resolution_P` | theorem | `—` | Declared evaluator/codomain transport can move scheme-local data into the exact kernel when no other obstruction remains. |
| · | `check_T_no_physical_time_flow_overclaim_P` | theorem | `—` | Scope boundary preserved: obstruction dynamics is formal transformation calculus, not a physical-time flow equation. |
| · | `check_T_obstruction_dynamics_exact_kernel_motion_P` | theorem | `—` | Obstruction dynamics determines which local data can move into the exact kernel and under what operations. |
| · | `check_T_obstruction_dynamics_operations_defined_P` | theorem | `—` | Finite obstruction dynamics operations are defined on obstruction objects. |
| · | `check_T_obstruction_dynamics_theorem_P` | theorem | `—` | Finite obstruction dynamics is P: transformations of obstruction channels determine motion into/out of the exact kernel. |
| · | `check_T_provenance_absorbing_boundary_P` | theorem | `—` | Provenance smuggling is absorbing under obstruction dynamics; it cannot be repaired by mathematical transport. |
| · | `check_T_refinement_monotonicity_P` | theorem | `—` | Refinement is obstruction-monotone: it can reveal channels but does not erase existing obstructions. |
| · | `check_T_structural_obstruction_invariance_P` | theorem | `—` | Structural C*-obstructions remain invariant under ordinary logistical repairs. |
| · | `check_T_substrate_revision_dissolution_routes_P` | theorem | `—` | D1/D2/D3 substrate-revision routes dissolve exactly their corresponding structural obstructions. |

## `apf/obstruction_repair_normal_form.py` — 9 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_Cstar_repair_requires_D2D3_P` | theorem | `—` | Flat C*-globalization can reach the exact kernel only under D2/D3 substrate revision plus codomain declaration. |
| · | `check_T_kernel_repair_normalization_P` | theorem | `—` | Every repairable obstruction has a canonical normalization path into the exact kernel; provenance failures do not. |
| · | `check_T_minimal_repair_plan_soundness_P` | theorem | `—` | Canonical repair plans are sound: success plans reach zero; provenance failures remain nonzero. |
| · | `check_T_minimality_certificate_P` | theorem | `—` | Canonical repair normal forms are minimal for the finite operation set. |
| · | `check_T_no_optimization_overclaim_P` | theorem | `—` | Scope boundary preserved: repair normal form is finite minimality over declared operations, not a physical optimization principle. |
| · | `check_T_obstruction_repair_normal_form_P` | theorem | `—` | Every finite obstruction object has a canonical repair normal form or a nonrepairability certificate. |
| · | `check_T_ordinary_vs_substrate_revision_boundary_P` | theorem | `—` | Repair normal form separates ordinary logistical repair from substrate-revision repair and nonrepairable provenance failures. |
| · | `check_T_provenance_no_repair_certificate_P` | theorem | `—` | No finite mathematical repair operation set removes provenance smuggling. |
| · | `check_T_repair_operations_cover_channels_P` | theorem | `—` | All non-provenance obstruction channels have a finite repair path; provenance smuggling is correctly nonrepairable. |

## `apf/operational_completeness.py` — 6 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `L_local_removability` | lemma | `P` | A distinction's committed capacity is recoverable by local operations iff no Moebius joint line containing it is billed at >= 2 interfaces. Forward = L_irr [P] (the check-4 simultaneity obstruction, reproduced in the line model on the bank's own tables). Backward = L_operational_completeness: foo... |
| · | `L_operational_completeness` | lemma | `P` | The operation set available to the observer at interface Gamma is exactly the set of admissibility-data REMOVALS billed solely at Gamma, within global admissibility (additions/general modifications not claimed -- row 6's license). UPPER bound: L_loc -- no cross-interface modification, no multi-in... |
| · | `L_recoverability_is_orbit_reachability` | lemma | `—` | (no summary) |
| · | `T_fusion_scope_dissolved` | theorem | `P` | The fusion-scope fork (Paper 3 supp red-team H5; the named non-claim of the v24.3.231/232 translation landing) dissolves: the all-bits and billing-scope arms are ONE per-interface-activation operator semantics handed two different pin-sets. All-bits floor == billing-scope floor of the class pinni... |
| · | `T_ledger_rent_excluded` | theorem | `P` | Every booked cost is a transition-booked level: a formation/realignment commitment standing thereafter as committed capacity (locked iff in a multiply-billed joint line), or a per-activation charge. No third kind: a standing-rent term (cost of merely persisting, accruing at fixed structure) is ex... |
| · | `T_transition_log_residue_readable` | theorem | `P` | The ledger basis grants observable status to the state-borne residue of its own transition log: commitment bookings are transition-toggled and residue-materialized (row 9 [P]); the residue is pin-indexed because the configuration space IS the product of per-interface holding bits (refined product... |

## `apf/paper1_kernel.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_FD1_substrate_distinctions_capacity` | theorem | `[P_structural]` | Executable witness for Paper 1 Supplement v2 §"Definitions" FD1 (enforcement interface = (S_Γ, 𝒟(Γ), C(Γ)) triple) + FD2 (admissible state) + FD4 (perturbation cost function) + K3 (forced additivity on disjoint supports) + SP (substrate faithfulness), instantiated on a finite 4-element substrate ... |

## `apf/payload_batch_certification_runner.py` — 4 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_payload_batch_certification_runner_P` | theorem | `—` | (no summary) |
| · | `check_T_payload_batch_runner_certifies_items_P` | theorem | `—` | Payload batch runner certifies canonical held/P/provenance cases. |
| · | `check_T_payload_batch_runner_loads_candidates_P` | theorem | `—` | Payload batch runner loads artifact adapter candidate reports. |
| · | `check_T_payload_batch_runner_writes_outputs_P` | theorem | `—` | (no summary) |

## `apf/phase_14d3_completions.py` — 3 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_42_over_102_structural_uniqueness` | theorem | `P_structural_reading` | Sharpened structural privilege of the 42/102 coefficient: among APF-native-only ratios (no math constants) within observational precision of the observed rho_Lambda/M_Pl^4, 42/102 is the UNIQUE ratio whose structural derivation terminates at L_self_exclusion's vacuum-fraction reading. The competi... |
| · | `T_Planck_scale_status_clarification` | theorem | `P` | Phase 14d.3 main theorem. An attempted derivation of M_Planck from A1 alone, via 7 candidate routes (see docstring), concludes that M_Planck is NOT derivable from A1 within the current APF framework. The reason is structurally clean: APF predicts dimensionless ratios in Planck units (rho_Lambda/M... |
| · | `T_bridge_observer_independence_open` | theorem | `C` | Formal framing of the open question: T_interface_sector_bridge identifies V_Lambda via three independent routes, two of which are observer-independent in APF (T12's global-interface stratum; Sector B of epsilon-decomposition) and one of which is observer-dependent in GR (de Sitter horizon absorbe... |

## `apf/photon_commitment_profile.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_ledger_reversibility_is_L_irr_lock` | theorem | `P_structural_reading` | The fourth horizon-record commitment C_4 ('ledger reversibility') is identified with the L_irr permanent-ledger-entry: a closed exterior horizon record locks a permanent, locally-irreversible committed entry (C_4 satisfied); a reversible mode passes through and locks none (NF_rev). NF_rev is the ... |

## `apf/photon_masslessness.py` — 8 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_charge_quantization_from_ledger_discreteness` | theorem | `P_structural_reading` | Why electric charge is quantized, in the framework's terms. A free U(1) allows continuous charges; in APF the U(1)_Y is the abelian grading of a discrete capacity ledger (Theorem_R R3 + L_epsilon_star), so the charge is discrete-not-continuous -- the framework's form of U(1) compactness. The comm... |
| · | `T_gauge_force_character_from_record_state` | theorem | `P_structural_reading` | The organizing principle of the gauge sector. The static potential is the propagator's Fourier transform, so the force law's shape is the propagator pole, which is the record state. No record (unbroken abelian) is massless, Coulomb 1/r, infinite range, 2 transverse polarizations -- the photon. A ... |
| · | `T_gravity_on_record_state_axis` | theorem | `P_structural_reading` | Gravity completes the record-state axis. EM and gravity are the two massless long-range forces, both at the no-record seat: massless <=> reversibility <=> no record. The photon's reversibility is the local U(1) gauge redundancy; the graviton's is diffeomorphism invariance (T_graviton [P], Pauli-F... |
| · | `T_particle_mass_is_locked_record` | theorem | `P_structural_reading` | Extends mass-is-a-record from the gauge bosons to all matter. All Standard-Model mass comes from one record -- the electroweak condensate. The W and Z carry it directly (the eaten Goldstone, T_Higgs); a charged fermion carries m_f = y_f * v, the strength with which it is locked to the same conden... |
| · | `T_photon_massless_from_reversibility` | theorem | `P_structural_reading` | The abelian mirror of the confinement closure. cost=count (L_cost) + the gauge-invariant-record theorem split composition by symmetry type (non-abelian Delta>0, abelian Delta=0); L_irr's own countermodel makes Delta=0 fully reversible, locking no record; cost=energy [P] then gives the unbroken ab... |
| · | `T_radiation_arrow_is_absorber_record_lock` | theorem | `P_structural_reading` | Resolves the standard puzzle -- Maxwell is T-symmetric yet radiation has an arrow -- in the framework's own terms. The photon's U(1) is additive/reversible/arrowless (Paper 2 R2); the arrow lives at the endpoints, where absorption commits a locally-unrecoverable record (L_irr [P]) and the gauge s... |
| · | `T_sm_gauge_group_is_record_state_enumeration` | theorem | `P_structural_exhaustive` | The capstone of the record-state axis. The SM gauge group, derived independently (Theorem_R), places each of its three factors in a different record state: SU(3) holds an unscreened colour record and confines; SU(2)_L holds a condensate record (Higgs, 3 Goldstones eaten) and is massive; U(1)_em h... |
| · | `T_visible_mass_is_color_record` | theorem | `P_structural_reading` | The strategic map of where mass comes from, in record terms. There are two mass records: the colour record (the Yang-Mills gap, ~Lambda_QCD) and the condensate record (the electroweak vev v_H, ~10^3 above), both riding the one Planck anchor. The nucleon mass is ~99% QCD binding -- the colour reco... |

## `apf/pi_gammagamma_2l_moment_native.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_pi_gammagamma_2L_moment_native` | theorem | `—` | (no summary) |

## `apf/planck_magnitude_single_anchor.py` — 2 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_fermion_strong_no_new_dimensional_anchor` | theorem | `P_structural_convention` | Completes the single-anchor scale-web over matter. Charged-fermion masses are m_f = y_f * v_H with y_f a dimensionless Yukawa, so m_f/M_Pl is rescaling-invariant exactly as v_H/M_Pl is -- the fermion sector introduces no new dimensionful input. The 'top mass is a new scale' loophole is dissolved ... |
| · | `T_planck_magnitude_single_dimensional_anchor` | theorem | `P_structural_convention` | The gravity sector's missing item, characterized at its honest maximum. The absolute Planck magnitude is the framework's single dimensional anchor. (1) NO-GO: a theory whose axioms fix only dimensionless structure cannot fix an absolute scale -- under the global rescaling M_Pl->lambda*M_Pl with m... |

## `apf/quantum_admissibility.py` — 5 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_Born_trace_rule` | theorem | `—` | Paper 5 v5.1 Corollary 3053 (Born trace rule): on the matrix sector M_n(C), every positive linear functional on effects is given by E \|-> tr(rho E) for some density matrix rho with tr(rho) = 1, and conversely. Verified on a 2x2 witness with two density matrices (pure \|0><0\| and maximally mixed I/... |
| · | `T_capacity_lower_bound_certificate` | theorem | `—` | Paper 5 v5.1 Corollary 1230 (Capacity lower-bound certificate): the universal infeasibility certificate fires exactly when the Boolean-defender minimum exceeds the available capacity. When it fires, the interface lies in IJCPres -- preservation-infeasible -- and is APF-infeasible regardless of an... |
| · | `T_contextual_branch_verdict_threshold_robust` | theorem | `P_structural_instrument` | The distortion threshold in kappa_Bool is stipulated, not derived, but immaterial at a state-independently contextual interface: the minimal classical-defender distortion is a strictly positive contextuality gap (delta* = 1/6 exactly for the magic square), so no Boolean defender is admissible for... |
| · | `T_field_selection_complex` | theorem | `—` | Paper 5 v5.1 Theorem 2907 (Complex selection from APF-complete composite accounting) selects the complex field uniquely among the three associative real division algebras. APF-completeness at composite interfaces forbids hidden record directions (Theorem 2709); under that constraint the parameter... |
| · | `T_kappa_Bool_minimum` | theorem | `—` | Paper 5 v5.1 Lemma 1036 (Finite Boolean-defender minimum): on any finite enumerable candidate-defender lattice with threshold-bounded distortion, the infimum kappa_Bool(Gamma, Q) is attained by an explicit witness D*. The witness here is D* = D_minimal with cost 3.0. Above-threshold candidates (e... |

## `apf/quantum_operator_derivation.py` — 4 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_I3_operator_self_identification` | theorem | `—` | (no summary) |
| · | `T_I3_svn_direct_computation` | theorem | `P` | Explicit numpy construction of rho_max = (1/d) I_d at d in [2, 3, 5, 8, 16, 32, 61, 102].  Each rho is verified Hermitian, trace-1, and PSD; S_vN computed by direct eigenvalue sum S_vN = -sum_i lambda_i log lambda_i matches ln(d) = ACC_scalar(acc_quantum(d)) to machine precision (1e-10) at every ... |
| · | `T_I3_thermal_K1_limit_witness` | theorem | `P` | K=1 specialisation of Phase 14d.2's explicit thermal machinery: for an arbitrary local Hamiltonian H_local on C^d (tested with both flat and linear spectra), rho_beta = exp(-beta H) / Z(beta) converges to rho_max = (1/d) I_d as beta -> 0.  Frobenius residual \|\|rho_beta - rho_max\|\|_F and lnZ resid... |
| · | `T_I3_unitary_invariance_witness` | theorem | `—` | (no summary) |

## `apf/recruitment.py` — 12 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `H1_continuum_from_anchor_profile` | other | `P` | Inside Regime R on a substrate with mode density exceeding the seven-class minimum, the admissibility configuration space is a smooth Banach manifold at scales coarser than ε*. The continuous anchor profile φ_d satisfying Concentration + Resolution-finiteness is forced by PLEC selection on substr... |
| · | `H2_locality_from_recruitment_kernels` | other | `P` | The closure conditions A9.1–A9.5 that drive Lovelock uniqueness are interface-local because the cost-curvature K(x) of the recruitment cost functional inherits locality from the local kernel ε_local(x, d) and the exponentially-decaying cooperative kernel I_int(x, x') by L_loc applied to substrate... |
| · | `T_DCE_Q_dependence_prediction` | theorem | `P_structural_reading` | In the high-Q DCE regime, the recruitment-radius master equation predicts photon production rate dN/dt ∝ (v/c)² ω_d / Q, contrasting with the standard moving-boundary calculation's Q-independent rate. This is the framework's one quantitative discriminating prediction in the radiation domain. Veri... |
| · | `T_cross_branch_matrix_element_form` | theorem | `P_structural_reading` | In the substrate-anchor entangled state, the within-branch mismatch is identically zero (M_mm = 0); the mismatch field's quantum analog lives in cross-branch matrix elements M_mn of the recruitment cost operator. The diagonal vanishing follows from each branch sitting at its branch-conditioned eq... |
| · | `T_master_equation_form` | theorem | `—` | (no summary) |
| · | `T_purcell_DCE_consistency` | theorem | `P_structural_reading` | The Purcell factor F_P = 3 Q λ³ / (4π² V) and the DCE 1/Q scaling both arise from the same cavity-modified-substrate mechanism: finite τ_rec ∝ Q/ω in regime (c) (lossy quantum vacuum). The product F_P × (dN/dt)_DCE is Q-independent — algebraic confirmation that Q enters both observables via the s... |
| · | `T_quantum_anchor_einstein_A` | theorem | `P` | The recruitment-radius quantum master equation reduces, under three structural identifications (squared dipole-vacuum coupling, EM-vacuum density of states, Fermi-rule rate factor in the lossless-vacuum regime), to the standard Einstein A coefficient A_{e→g} = ω_{eg}^3 \|⟨g\|d̂\|e⟩\|^2 / (3π ε_0 ℏ c^... |
| · | `T_sixteen_case_unification_structural` | theorem | `P_structural_reading` | Sixteen previously-disjoint radiation phenomena reduce to the recruitment-radius master equation (or its quantum extension) under appropriate substrate kernels and anchor types. Cases group as: 4 moving-charge (classical anchors) + 4 moving-boundary (classical anchors) + 4 classical-anchor extens... |
| · | `T_substrate_anchor_entangled_state` | theorem | `P_structural_reading` | The substrate-anchor combined state \|Ψ⟩ = Σ c_n \|φ_eq[\|n⟩]⟩ ⊗ \|n⟩ is an Irreducible Joint Constraint structure (Paper 5 vocabulary) when the branch-conditioned equilibria \|φ_eq[\|n⟩]⟩ are distinct. Three structural reasons: linearity of QM forces it; PLEC argmin selects branch-conditioned cost-min... |
| · | `T_three_regimes_tau_rec` | theorem | `P_structural_reading` | The master equation's 1/τ_rec factor has three regime-dependent readings: (a) lossy classical: literal dissipation timescale (plasma collision rate); (b) lossless quantum vacuum: τ_rec → ∞ collapses to Fermi-rule rate factor (2π/ℏ) δ(E_f - E_i); (c) lossy quantum vacuum: cavity Q gives Lorentzian... |
| · | `T_tls_capacity_budget_knee_design_corollary` | theorem | `P_structural_instrument` | The TLS capacity-budget knee T_knee = h f/(r_th kB) pinned against its seven-dataset validation table (all six numeric predictions < 0.5%, both parameter-free scalings exact), and the design corollary corrected: the r_th = 2 TLS-decoupling gap at 20 mK base is 833.5 MHz (margined ~926 MHz), not t... |
| · | `T_tls_transduction_class_discriminator_rule_D` | theorem | `P_structural_instrument` | Rule D (transduction-class discriminator, rescoped per the O6 hostile audit): coverage below T_sat = h f/(2 kB) = T_knee(r_th = 2) is NECESSARY for any transduction-class adjudication (Kumar 2008: T_min 120 mK > T_sat 104.4 mK -> zero coverage, class-UNDECIDABLE, abstention forced under every cla... |

## `apf/representation_descent_application_harness.py` — 8 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_application_harness_export_table_P` | theorem | `—` | Harness export table is complete for canonical active sectors. |
| · | `check_T_harness_no_overpromotion_P` | theorem | `—` | Harness does not overpromote: only zero-obstruction claims export global P; provenance fails closed. |
| · | `check_T_obstruction_derivation_from_metadata_P` | theorem | `—` | Canonical sector obstructions are derived from raw metadata. |
| · | `check_T_promotion_status_outputs_P` | theorem | `—` | Harness emits correct promotion statuses from derived obstructions. |
| · | `check_T_repair_normal_form_outputs_P` | theorem | `—` | Harness emits canonical repair normal forms for sector obstructions. |
| · | `check_T_representation_descent_application_harness_P` | theorem | `—` | Representation Descent Application Harness is P: it derives obstruction, status, repair, and safe claim language from sector metadata. |
| · | `check_T_safe_claim_language_outputs_P` | theorem | `—` | Harness emits safe reviewer-facing claim language for each sector. |
| · | `check_T_sector_metadata_schema_no_expected_labels_P` | theorem | `—` | Sector metadata schema contains raw inputs only and no expected-label leakage. |

## `apf/representation_descent_engine.py` — 3 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_representation_descent_engine_audit_first_P` | theorem | `P_representation_descent_engine_audit_first` | Audit-first discipline preserved: target_value_consumed = 0; blocked-overclaim non-claims from v24.3.11 explicitly tracked (flat_substrate_global_cstar_algebra + infinity_stack_or_cohomology_overclaim both = 0); no engine smuggling. |
| · | `check_T_representation_descent_engine_entry_point_P` | theorem | `P_representation_descent_engine_entry_point` | Entry point produces correct verdicts: no-problem -> OPEN with problem_missing; unknown-canonical-name -> OPEN with unknown_canonical_problem; real canonical problem dispatches to bridge + returns valid status. |
| · | `check_T_representation_descent_engine_identity_P` | theorem | `P_representation_descent_engine_identity` | Representation Descent Engine declares Tier 2 role + IE family membership; 6-status verdict taxonomy + 3 preserved non-claims (flat C*-algebra + infinity-stack overclaim explicitly blocked). |

## `apf/representation_descent_full_integration.py` — 4 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_full_integration_top_layers_P` | theorem | `—` | (no summary) |
| · | `check_T_publication_assets_present_P` | theorem | `—` | Publication/reviewer integration assets are expected in the full integration package. |
| · | `check_T_representation_descent_full_integration_P` | theorem | `—` | (no summary) |
| · | `check_T_solver_bridge_smoke_api_P` | theorem | `—` | Interface solver bridge smoke API returns expected held-for-repair certificate. |

## `apf/representation_descent_kernel.py` — 6 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_APF_representation_descent_kernel_P` | theorem | `—` | APF Representation Descent Kernel is P: global physics is zero-obstruction exact admissible representation descent over the ACC/interface base. |
| · | `check_T_kernel_dependencies_loaded_P` | theorem | `—` | All representation-descent kernel dependency layers load and pass their top P checks. |
| · | `check_T_kernel_ladder_order_P` | theorem | `—` | The representation-descent kernel theorem stack is ordered coherently. |
| · | `check_T_master_unification_sentence_P` | theorem | `—` | Master unification sentence contains all required APF descent-kernel components. |
| · | `check_T_no_flat_master_algebra_or_infinity_overclaim_P` | theorem | `—` | Scope boundary preserved: the kernel is finite/fibered/obstruction-based, not a flat master algebra or infinity-stack claim. |
| · | `check_T_sector_promotion_classification_P` | theorem | `—` | Promotion gate correctly classifies active APF sector examples. |

## `apf/representation_descent_kernel_adversarial_audit.py` — 10 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_exactness_non_tautology_P` | theorem | `—` | Exactness is non-tautological in the audit: descent and obstruction are independently computed and empirically cross-checked. |
| · | `check_T_generated_globalization_image_P` | theorem | `—` | Globalization image is generated from global seeds/covers and independently checked. |
| · | `check_T_independent_descent_predicate_P` | theorem | `—` | Independent descent predicate accepts/rejects examples without using obstruction or promotion functions. |
| · | `check_T_kernel_predecessor_still_passes_P` | theorem | `—` | Representation Descent Kernel predecessor still passes before adversarial audit. |
| · | `check_T_mutation_knockout_each_descent_axiom_P` | theorem | `—` | Each descent axiom has a knockout mutation that independently fails descent and produces nonzero obstruction. |
| · | `check_T_no_expected_label_leakage_P` | theorem | `—` | Sector obstruction derivation contains no expected-label/status leakage. |
| · | `check_T_obstruction_independently_matches_descent_P` | theorem | `—` | Independently derived obstruction zero matches independent descent predicate across hand-built cases. |
| · | `check_T_random_finite_site_stress_P` | theorem | `—` | Deterministic random finite-site stress shows independent descent and obstruction agree across varied cases. |
| · | `check_T_representation_descent_kernel_adversarial_audit_P` | theorem | `—` | Representation Descent Kernel passes adversarial non-tautology, mutation, stress, and metadata-derivation audits. |
| · | `check_T_sector_obstruction_derivation_from_metadata_P` | theorem | `—` | Sector statuses are derived from metadata fields, not expected labels. |

## `apf/route_certification_starter_suite.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_route_certification_starter_suite_P` | theorem | `—` | All route-specific APF certification starters pass. |

## `apf/route_certification_workbench.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_route_workbench_payload_certification_P` | theorem | `—` | Route workbench certifies JSON payloads for all six starter routes and rejects expected-label leakage. |

## `apf/s_higgs_finite_profile_native.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_S_higgs_finite_profile_native` | theorem | `P_S_higgs_finite_profile_native_reproduction` | Closes the last [P+tool] piece of the EW oblique S parameter -- the m_H-DEPENDENT finite Higgs profile G(m_H^2/m_Z^2) -- at native [P]. The profile is D1 (Z,h bubble) + D2 (h,G0 bubble); D3 (ZZhh seagull) is a k^2-independent A0 tadpole that cancels in the subtraction. Couplings are read off \|D_m... |

## `apf/s_parameter_native.py` — 4 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_S_fermion_loop_native_reproduction` | theorem | `P_S_oblique_native_reproduction` | Fermion-loop Peskin–Takeuchi S for a degenerate doublet, reproduced answer-free. S = 16π(Π'_33−Π'_3Q)(0) = 2π N_c(Π'_AA−Π'_VV)(0); the AA−VV transverse numerator is the −8m² g_{μν} blob riding the q-dependent scalar bubble, whose q²-slope is finite (the 1/ε of Γ(2−d/2) cancels the ε from ∂_{q²}Δ^... |
| · | `T_S_higgs_logarithm_native` | theorem | `—` | (no summary) |
| · | `T_S_higgs_mH_dependent_profile_Ptool` | theorem | `P_plus_tool_S_higgs_mH_profile_GLOO_reproduction` | Closes the m_H-DEPENDENT bosonic Higgs profile of Peskin-Takeuchi S at [P+tool]. S_H(m_H) = (1/12pi)[ln(m_H^2/m_ref^2) + G(m_H^2/m_Z^2)] from the imported Grimus-Lavoura-Ogreid-Osland closed form (Ghosh arXiv:2201.01006). The asymptotic slope dS_H/d ln(m_H^2) -> 1/(12pi) cross-checks the native [... |
| · | `T_oblique_curvature_moment_native` | theorem | `P_S_oblique_native_reproduction` | The electroweak oblique sector's perturbative moments are successive q²-moments of the one native current correlator. The 1st moment is S (the 1/6 weight); the 2nd moment — the curvature — is Π''_AA−Π''_VV = −1/(60π²m²), the 1/30 moment of the x(1−x) Feynman weight, native and answer-free, and ma... |

## `apf/s_parameter_pure_gauge_constant_native.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_S_pure_gauge_constant_native` | theorem | `—` | (no summary) |

## `apf/screen_geometry_characterization.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_screen_containment_characterization` | theorem | `—` | (no summary) |

## `apf/sigma_scale_capacity_formula_gate.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_sigma_scale_capacity_formula_held_pending_independent_scale` | theorem | `P_structural_sigma_scale_capacity_formula_held_pending_independent_scale` | Disposition of the electroweak absolute-scale route after the 2026-05-29 top-Yukawa no-go, faithful to the audited-clean sibling pack APF_ABSOLUTE_MASS_SCALE_SIGMA_AUDIT_AND_REPAIR_v1 (12/12 verifier asserts; no forbidden input; no-go respected; fail-closed gate). The Paper-28 / L_vev_threshold_m... |

## `apf/sigma_scale_yukawa_free_geometric_floor.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_sigma_scale_yukawa_free_geometric_component` | theorem | `P_structural_sigma_scale_yukawa_free_geometric_component_modulo_planck_convention` | The y_t-independent consequence that survives the 2026-05-29 top-Yukawa no-go and refines the held v_H-capacity gate. Writing the Paper-28 / L_vev_threshold_matching capacity formula with a_Y = N_c y_t^2, b = N_c y_t^4 gives v = A*(N_c + c_R/y_t^2) with A = M_Pl/[pi sqrt(C_boson N_c) d_eff^(C_bos... |

## `apf/sin2theta_eff_bsy_real_adapter.py` — 6 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_sin2theta_eff_bsy_adapter_certification_P` | theorem | `—` | EVALUATOR_MAP edge in ew movement graph resolves to MOVES_CLEANLY with sin2theta_eff_bsy-filled payload. |
| · | `check_T_sin2theta_eff_bsy_adapter_evaluator_consistent_P` | theorem | `—` | sin^2 theta_eff^APF = 3/13 + 4/5063 matches LATEST-44 derivation; three sin^2 codomains typed-distinct; BSY residual z = -0.003 tight. |
| · | `check_T_sin2theta_eff_bsy_adapter_external_ledger_declared_P` | theorem | `—` | All 9 required external evaluator ledger fields declared on the sin2theta_eff_bsy snapshot. |
| · | `check_T_sin2theta_eff_bsy_adapter_no_smuggling_P` | theorem | `—` | No forbidden target-value key in sin2theta_eff_bsy payload; target_value_consumed=False. |
| · | `check_T_sin2theta_eff_bsy_adapter_payload_contract_P` | theorem | `—` | sin2theta_eff_bsy adapter produces ew-shaped route payload with evaluator + codomain filled. |
| · | `check_T_sin2theta_eff_bsy_real_adapter_P` | theorem | `—` | sin2theta_eff_bsy real adapter wires banked evaluator content into Engine-readable route payload; EVALUATOR_MAP edge fills cleanly; no smuggling; external ledger declared. |

## `apf/sin2theta_eff_kappa_l_decomposition.py` — 6 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `L_sin2theta_eff_kappa_l_drho_matches_gauge` | lemma | `P` | The rho-parameter shift reused in the kappa_l decomposition (top + QCD + Higgs) is value-identical to the banked gauge.check_L_W_mass custodial pieces at banked precision: Drho_top=0.008379, Drho_QCD=-0.000629, Drho_H=-0.001504. No independent re-derivation; same custodial-breaking quantity, two ... |
| · | `L_sin2theta_eff_kappa_l_nonrho_remainder_open` | lemma | `C` | The genuine non-custodial residual = 0.011815 (32.1% of the target) -- bosonic, vertex/box, light-fermion and Delta-alpha-related pieces -- is the residual OPEN gate. Per the framework's Delta r-ladder discipline it is a source-proxy NOT admitted for export; Delta alpha is NOT internalized (the D... |
| · | `L_sin2theta_eff_kappa_l_remainder_named_open` | lemma | `C` | Delta kappa_rem = 0.015087 (41.0% of the target) is the single named, currently-unevaluated slot: the Delta-alpha running plus the non-custodial vertex/box remainder. It is NOT claimed derived. Leading + remainder reconstruct the banked target exactly. The full-form-factor derivation flag and the... |
| · | `T_sin2theta_eff_kappa_l_leading_custodial_internal` | theorem | `P` | Delta kappa_l = Xi_rho * Delta rho + Delta kappa_rem. Xi_rho = c_W^2/s_W^2 = 3.477498 (banked OS codomain sin^2 theta_OS = 0.223339); Delta rho = 0.006246 (banked L_W_mass custodial shift). Leading custodial term = 0.021721 = 59.0% of the banked target Delta kappa_l = 0.036808. Top-only diagnosti... |
| · | `T_sin2theta_eff_kappa_l_no_target_smuggling` | theorem | `P` | The kappa_l decomposition consumes no new external numeric input. The single externally-anchored number is the already-banked kappa_l ratio target (1.036807775, LATEST-51 import-only). No measured sin^2 theta_eff, no fitted kappa_l, no PDG target is read. The leading term is built only from banke... |
| · | `T_sin2theta_eff_kappa_l_remainder_mt_normalization_split` | theorem | `P_structural_partial` | Delta kappa_rem = 0.015087 splits, using the framework's own custodial Delta rho formula at m_t=163 vs the PDG reference m_t=172.61, into: m_t-normalization gap = 0.003272 (21.7% of the remainder, the sigma-normalized-top-mass scheme share) + genuine non-custodial residual = 0.011815 (78.3% of th... |

## `apf/sin2theta_w_OS_capacity_counting.py` — 17 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_GH_OS_codomain_constraint_rank_algebraic_decomposition` | theorem | `P_structural_meta_GH_OS_codomain` | Closed-form algebraic decomposition: r* = (D-2)/(2(D-1)+dim_R H - dim(G/H)). At SM-physical inputs (D=4, dim_R H=4, dim(G/H)=3): r* = 2/(6+1) = 2/7; sin²θ_W^OS = 2/9. Shell capacities (c_W±, c_h, c_A) = (3, 1, 2) emerge as decoupled logistic fixed points. Aggregate (7, 2) is post-equilibrium sum.... |
| · | `T_GH_OS_codomain_foundation_grounded_attractor_structural` | theorem | `P_attractor_structural_GH_OS_codomain` | Paper-18 structural parity for the GH_OS angle, delivered by composition. Chain: A1 → T8 [P] (D=4) → Theorem_R [P] (dim(SU(2)×U(1))=4) → T_Higgs [P] (dim_R H=4, dim(G/H)=3, n_radial=1) → rank-source map (c_W+, c_W-, c_h, c_A) = (3, 3, 1, 2) → KL-Lyapunov replicator flow with closed-form exponenti... |
| · | `T_GH_OS_codomain_full_structural_grade_promotion` | theorem | `P_full_structural_GH_OS_codomain_meta` | GH_OS_codomain grade promoted P_structural → P_full_structural in v24.3.109. Justification: 5-spine convergence (capacity-share, propagation-complement, projector-trace, tangent-normal, resolved-shell complement) standalone-filed at DOCTRINE_CONSEQUENCES_BUNDLE_LATEST_44/ + snapshot-consistency v... |
| · | `T_GH_OS_codomain_rank_derivations_foundational_rigor_equivalence` | theorem | `P_structural_meta_GH_OS_codomain` | Three textbook QFT framings — constraint-projector ranks (v3), BRST/Dirac cohomology (v5), Wigner little-group classification (v6) — all yield identical rank tuple (3, 3, 1, 2) at SM-physical inputs and feed the same algebraic formula r* = (D-2)/(2(D-1)+dim_R H - dim(G/H)) = 2/7. Foundational-rig... |
| · | `T_GH_OS_codomain_rank_variational_universality_gate1_maximal` | theorem | `P_structural_meta_GH_OS_codomain` | Variational uniqueness: F = KL divergence has unique minimum x_i = c_i/C at SM inputs (3,3,1,2)/9. Universality: equilibrium invariant across admissible monotone-homogeneous pressure-flow family P_i = φ(x_i/c_i) — tested with 4 distinct φ (linear, log1p, square, cuberoot), all give equal pressure... |
| · | `T_GH_OS_codomain_scope_restriction_principled` | theorem | `P_structural_meta_GH_OS_codomain` | Gate-2 (κ_b decisive vs scope-mismatch) adjudicated A (scope-restriction) via multi-channel probe + 4 structural distinguishers all supporting A. Naive prediction 8/21 uniform across all charged fermion channels (ℓ/u/c/d/s/b); DFGRU measured values cluster 0.231-0.233; ratio span 0.0061 < 0.01 (u... |
| · | `T_MW2_over_MZ2_capacity_counting_value` | theorem | `P_attractor_structural_GH_OS_codomain` | M_W^2/M_Z^2 = 7/9; M_W/M_Z = sqrt(7)/3 = 0.8819171037 |
| · | `T_M_W_tree_dimensionful_from_M_Z_GH_OS_codomain_composed` | theorem | `P_tree_dimensionful_GH_OS_codomain_composed` | M_W_tree (GH_OS_codomain anchor sin^2 theta_W^OS = 2/9) = M_Z * sqrt(7)/3 = 91.1876 * 0.8819171037 = 80.4199 GeV. Gap to PDG observed (80.377 ± 0.012): +43 MeV (+0.053%, order of one-loop EW corrections). Tree level; not loop-renormalized; M_Z = 91.1876 GeV is the framework's chosen absolute scal... |
| · | `T_OSR_premise_implications_mechanized` | theorem | `P_structural_exhaustive` | OSR rule -> premise-implication mechanized; all 6 verify: True. Audit finding banked: v5's P0-P11 sufficient for OSR1, OSR2, OSR3, OSR5; INSUFFICIENT for OSR4, OSR7 — closed with P12 (Higgs SU(2)-doublet), P13 (charged-W SU(2)-adjoint), P14 (charged-W counted). |
| · | `T_canonical_unique_under_OSR_enumeration` | theorem | `P_structural_exhaustive` | Enumerated 3^8 = 6561 candidate (counted, side) assignments; 1 survives OSR1-OSR7 filter; survivor capacity = (7, 2, 9). |
| · | `T_ew_broken_phase_dof_conservation_12` | theorem | `P_structural` | 12 -> 12 at the SM values, computed (not asserted) from the shared banked inputs through the shell census's own rank formulas (c_W = D-1, c_A = D-2, c_h = dim_R H - dim(G/H)); the check fails under... |
| · | `T_kappa_b_universality_falsified` | theorem | `C` | Naive extension of capacity-counting rule to b-quark channel: total U(1) = 8, total SU(2) = 13, sin^2 theta_eff^b predicted = 8/21 = 0.38095; measured = 0.232 (DFGRU). Ratio = 1.642 (factor 1.65 — rule does NOT extend to fermion-channel form factors). Banked guard against future overextension cla... |
| · | `T_kappa_l_composed_with_paper_18` | theorem | `P_attractor_structural_GH_OS_codomain_composed` | kappa_l = 27/26 = 27/26 is the raw source-angle ratio (3/13)/(2/9); Delta kappa_l = 1/26 = 1/(2*13). Within the DFGRU scheme (M_W-last-input (DFGRU 1906.08815), 2012-2019 vintage, ref M_W=80.385 GeV) it matches the all-orders SM fit to +3.15e-05 (within-scheme; ~4e-5 per 16 MeV M_W sensitivity, U... |
| · | `T_lyapunov_V_unique_global_minimum` | theorem | `P_structural_exhaustive` | V=0 count = 1 (of 6561); unique global minimum: True. Energy histogram: {0: 1, 1: 18, 2: 124, 3: 466, 4: 1104, 5: 1744, 6: 1792, 7: 1056, 8: 256} |
| · | `T_lyapunov_k2_swap_strict_descent` | theorem | `—` | (no summary) |
| · | `T_sin2_theta_W_OS_capacity_counting_value` | theorem | `P_attractor_structural_GH_OS_codomain` | sin^2 theta_W^OS = 2/9, cos^2 = 7/9, g'^2/g^2 = 2/7; sin^2 + cos^2 = 1 verified. |
| · | `T_sin2theta_W_OS_reconciliation_GH_OS_codomain_to_native_one_loop` | theorem | `P_reconciliation_GH_OS_codomain_to_native_one_loop` | Three sin^2 theta_W^OS surfaces banked: (1) structural attractor 2/9 = 0.22222, (2) v24.3.99 native 1-loop @ Denner = 0.22531 (+1.39%), (3) PDG observed = 0.22305 (+0.37%). PDG sits closer to structural (0.37%) than to native 1-loop @ Denner (1.00%) — structurally consistent with UV-attractor rea... |

## `apf/sin2theta_w_mass_ratio_identity_real_adapter.py` — 3 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_sin2theta_w_mass_ratio_identity_adapter_atlas_routes_P` | theorem | `—` | Atlas routes the sin²θ_W on-shell mass-ratio identity Route 14 payload to INTERNAL_IDENTITY_GLOBAL_P. |
| · | `check_T_sin2theta_w_mass_ratio_identity_adapter_closure_kind_P` | theorem | `—` | sin²θ_W on-shell mass-ratio identity Route 14 adapter declares closure_kind=internal_identity. |
| · | `check_T_sin2theta_w_mass_ratio_identity_adapter_no_smuggling_P` | theorem | `—` | sin²θ_W on-shell mass-ratio identity Route 14 adapter does not consume target sin²θ_W values. |

## `apf/sin2theta_w_source_identity_real_adapter.py` — 3 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_sin2theta_w_source_identity_adapter_atlas_routes_P` | theorem | `—` | Atlas routes the sin²θ_W source identity Route 12 payload to INTERNAL_IDENTITY_GLOBAL_P. |
| · | `check_T_sin2theta_w_source_identity_adapter_closure_kind_P` | theorem | `—` | sin²θ_W source identity Route 12 adapter declares closure_kind=internal_identity. |
| · | `check_T_sin2theta_w_source_identity_adapter_no_smuggling_P` | theorem | `—` | sin²θ_W source identity Route 12 adapter does not consume target sin²θ_W values. |

## `apf/strong_cp_completion_no_go.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `L_completion_angle_content_blind_native` | lemma | `P_structural` | The native->realized completion map is CONTENT-BLIND on the strong-CP angle. Completion parameters partition by capacity gain: delta_CKM buys 6 Jarlskog history sectors (record-bearing => content-FIXED); theta-bar buys none (no-record). Witness: two admissible completions R0 (theta-bar=0) and Rpi... |

## `apf/su2_string_cut_testbed.py` — 3 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_no_negative_delta_at_gauge_cut_family` | theorem | `—` | (no summary) |
| · | `check_T_su2_string_cut_comovement` | theorem | `P_structural_reading` | SU(2) Kogut-Susskind strong-coupling string family j in {1/2, 1, 3/2, 2}, orderings only, all arithmetic exact. Verdict PARTIAL with the four-clause split carried in full: (i) the asymptotic N-ality clause CO-MOVES at sign/class strength -- the diagnostic N-ality classes and the Delta_min sign cl... |
| · | `check_T_su2_string_cut_native_algebra` | theorem | `—` | (no summary) |

## `apf/subspace_functors.py` — 4 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_horizon_subspace_functor` | theorem | `P` | Explicit horizon-subspace functor F_horizon : ACC_hor -> Subspace proven well-defined and dimension-preserving across K in [0, 1, 10, 25, 61, 100, 1000, 42], monotone under horizon nesting on 4 test pairs with identical ambient + tagging convention, and coinciding with V_global (dim 42) at the ca... |
| · | `T_operator_subspace_functor` | theorem | `P` | Explicit operator-subspace functor F_operator : ACC_quantum -> Subspace proven well-defined and dimension-preserving across d in [1, 2, 4, 8, 16, 32], monotone under spectrum extension on 4 test pairs in the single canonical ambient 'capacity_space_operator', and carrying the thermal density matr... |
| · | `T_quantum_subspace_functor` | theorem | `P` | Explicit quantum-subspace functor F_quantum : ACC_quantum -> Subspace proven well-defined and dimension-preserving across d in [1, 2, 4, 8, 16, 32, 64], monotone under d-nesting on 5 test pairs in the single canonical ambient 'capacity_space_quantum', and carrying the max-mixed admissible density... |
| · | `T_subspace_functors_unified` | theorem | `P` | Composed top theorem of Phase 14c: the three explicit subspace functors F_horizon (Phase 14c.1, horizon side of I1), F_quantum (Phase 14c.2, quantum side of I3), and F_operator (Phase 14c.3, operator-space side of I4) are jointly well-defined, each satisfies its five structural conditions (i)-(v)... |

## `apf/sun_hhom_battery.py` — 2 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `L_finite_abelian_grading_schema` | lemma | `P_math | computed-instance list as stated (Z_2, Z_3 banked spot-checked; Z_4, Z_5 this battery; Z_2xZ_2, Z_6 SYNTHETIC products of banked data; Z_1 cross_ref) -- the general-A sentence a STATEMENT-SHAPE with instance support, never an exhaustive proof` | on every computed instance, a charge map with the hom property is an A-grading of the fusion ring (additivity == hom; box-conservation mechanism computed at N = 4, 5); reachable charges from a sour... |
| · | `L_su45_hhom_battery` | lemma | `P_math | lattice-model conventions (per-vertex-singlet admissibility a MODEL DEFINITION, Gauss reading a named identification) + battery/cap/depth scoping -- for the fusion, grading, determination, and coset facts; graph-enumeration legs instance-scoped [P] at stated caps on walked graphs` | q = boxes mod N is a fusion homomorphism on every constituent of every stated-battery product at N = 4 (10 irreps, 100 pairs, 306 constituents) and N = 5 (10 irreps, 100 pairs, 347 constituents), t... |

## `apf/superconductivity_codomain_adapter.py` — 4 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_superconductivity_codomain_adapter_atlas_contract_P` | theorem | `P_codomain_adapter_atlas_contract` | SC codomain adapter declares full atlas live-runner contract for the CODOMAIN axis: ATLAS_INPUT_ID + ATLAS_ROUTE + ATLAS_PAYLOAD_NAME + ATLAS_AXIS attributes correct; build_live_atlas_payload returns regime + network_state payload that the atlas's _compile_codomain_input dispatches through adjudi... |
| · | `check_T_superconductivity_codomain_adapter_audit_first_P` | theorem | `P_codomain_adapter_audit_first` | Audit-first discipline preserved: numeric_critical_temperature + material_specific_prediction + highTc_solved + ab_initio_chemistry all = 0 in adapter export; target_value_consumed=False; external evaluator ledger declared with runtime_module + engine_module + reference_doc fields. |
| · | `check_T_superconductivity_codomain_adapter_payload_contract_P` | theorem | `P_codomain_adapter_contract` | SC codomain adapter payload carries the required 9 fields with correct values: adapter identity (name/engine/regime/tier) + source_network + verdict + target_value_consumed=False + preserved_non_claims + external evaluator ledger. |
| · | `check_T_superconductivity_codomain_adapter_verdict_consistent_P` | theorem | `P_codomain_adapter_verdict_consistent` | Adapter verdicts match v5 audit-ladder fixture expectations: positive -> COHERENT_CODOMAIN_SELECTED with positive margin; phase_fragmented -> PHASE_LOCK_FAILED; defect_overloaded -> MARGIN_NONPOSITIVE with nonpositive margin. |

## `apf/superfluidity_codomain_adapter.py` — 5 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_superfluidity_codomain_adapter_atlas_contract_P` | theorem | `P_codomain_adapter_atlas_contract` | SF codomain adapter declares full atlas live-runner contract for the CODOMAIN axis: ATLAS_INPUT_ID + ATLAS_ROUTE + ATLAS_PAYLOAD_NAME + ATLAS_AXIS correct; build_live_atlas_payload returns regime + network_state that the atlas's _compile_codomain_input dispatches through adjudicate_codomain_compe... |
| · | `check_T_superfluidity_codomain_adapter_audit_first_P` | theorem | `P_codomain_adapter_audit_first` | Audit-first discipline preserved: numeric_critical_temperature + material_specific_prediction + highTc_solved + ab_initio_chemistry all = 0 in adapter export; target_value_consumed=False; external evaluator ledger declared with runtime_module + engine_module + reference_doc fields. |
| · | `check_T_superfluidity_codomain_adapter_payload_contract_P` | theorem | `P_codomain_adapter_contract` | SF codomain adapter payload carries the required 9 fields with correct values: adapter identity (name/engine/regime/tier) + source_network + verdict + target_value_consumed=False + preserved_non_claims + external evaluator ledger. Routes through the engine (not its own evaluator). |
| · | `check_T_superfluidity_codomain_adapter_v4_audit_ladder_P` | theorem | `P_codomain_adapter_v4_audit_ladder` | Installed SF runtime reproduces the v4 audit-ladder verdict lattice on all seven APF_SUPERFLUIDITY_IE_AUDIT_LADDER_v4 fixtures through the engine: positive -> SELECT_SUPERFLUID_STRUCTURAL; fragmented -> FRAGMENTED_WINS; thermal -> THERMAL_PRESSURE_OVERLOAD; vortex -> VORTEX_DEFECT_OVERLOAD; bound... |
| · | `check_T_superfluidity_codomain_adapter_verdict_consistent_P` | theorem | `P_codomain_adapter_verdict_consistent` | Adapter verdicts match fixture expectations through the engine: positive -> COHERENT_CODOMAIN_SELECTED with positive margin; fragmented -> MARGIN_NONPOSITIVE; vortex_overloaded -> COHERENCE_INSUFFICIENT (vortex_defect_overload); gauge_contaminated -> OPEN_EVIDENCE_REQUIRED routed back to the SC a... |

## `apf/symmetry_contextuality_independence.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_symmetry_degeneracy_orthogonal_to_contextuality` | theorem | `P_structural_reading` | Exact 2-qubit witnesses populate all four (SYM, IJC_CHSH) cells: (sym,Sep)=I/4 [M=0]; (sym,IJC)=Bell [M=2]; (asym,Sep)=product [M=0.16]; (asym,IJC)=cos(pi/5)\|00>+sin(pi/5)\|11> [M=1.9045]. SYM is a proxy (reduced-state spectral degeneracy) for the cosmogenic Type-II argmin-degeneracy; IJC_CHSH is ... |

## `apf/synchronization_codomain_adapter.py` — 4 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_synchronization_codomain_adapter_atlas_contract_P` | theorem | `P_codomain_adapter_atlas_contract` | Synchronization adapter declares the CODOMAIN atlas contract; live payload reaches COHERENT via the engine. |
| · | `check_T_synchronization_codomain_adapter_audit_first_P` | theorem | `P_codomain_adapter_audit_first` | Audit-first non-claims preserved; target not consumed; evaluator ledger declared. |
| · | `check_T_synchronization_codomain_adapter_payload_contract_P` | theorem | `P_codomain_adapter_contract` | Synchronization codomain adapter payload carries the required fields and routes through the engine. |
| · | `check_T_synchronization_codomain_adapter_verdict_consistent_P` | theorem | `P_codomain_adapter_verdict_consistent` | Installed Synchronization runtime reproduces every fixture verdict through the engine. |

## `apf/t_parameter_native.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_T_parameter_fermionic_native_P` | theorem | `P` | The fermionic (custodial) leg of the Peskin-Takeuchi T parameter is native: alpha*T = Delta rho, with Delta rho read from the APF-owned native PV substrate (Veltman rho function, top-dominated) = 0.008304, giving T_ferm = 1.0623 at the conventional alpha_em(M_Z) = 1/127.93. The answer-free spine ... |

## `apf/tail_center_trivial_native.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `L_tail_center_trivial_native` | lemma | `[P]` | F1 -- the native half of factoriality. Upgrades N4 (tail acts scalar on Omega, a single-vector statement) to: a tail element that is ALSO central is a scalar OPERATOR (Z cap tail = C.1). Centrality, not separating-ness, supplies the upgrade -- it lets the element pass through every x in M onto th... |

## `apf/thermal_absolute.py` — 5 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `L_Sigma_m_nu_suggestive` | lemma | `C` | APF candidate formula Sigma m_nu / M_Planck = 11 / 102^15 predicts Sigma m_nu = 0.0998 eV, within the observational window [0.058, 0.12] eV (normal-ordering minimum to Planck 2018 upper bound). Coefficient 11 and exponent 15 both admit multiple structural APF readings without a privileged unique ... |
| · | `L_eta_does_not_fit_cleanly` | lemma | `C` | Baryon-to-photon ratio eta = 6.12e-10 does NOT fit the C / d_eff^k formula with small-integer C at small k. Best small-k fit: k=5, C=6.78 (3% residual to integer 7, with no clean structural reading of 7). eta is a baryogenesis asymmetry ratio, not a ground-state or thermal-bath density; outside t... |
| · | `T_Phase_14e4_thermal_scope` | theorem | `P` | Phase 14e.4 scope delineation: the APF C / d_eff^k formula structure applies (i) to cosmological ground-state densities at k=62 (rho_crit, rho_b, rho_c, rho_Lambda, all 8% residual), (ii) to thermal-bath energy densities at k=64 (T_CMB, rho_gamma, 0.33% residual — much tighter). The exponent shif... |
| · | `T_T_CMB_absolute_formula` | theorem | `P` | APF thermal absolute formula (T_CMB/M_Pl)^4 = 48/102^64 predicts T_CMB = 2.7166 K, vs FIRAS observed T_CMB = 2.7255 ± 0.0006 K. Residual 0.0089 K = 0.33% on T_CMB itself, or 0.0057 decades on (T_CMB/M_Pl)^4. The exponent 64 = K_SM + 3 = K_SM + 1 + N_pol_photon (photon has 2 polarizations; matter ... |
| · | `T_thermal_exponent_interpretation` | theorem | `C` | Hypothesis (registered [C]): the C/d_eff^k formula's exponent k depends on the polarization count of the species X, via k_X = K_SM + 1 + N_pol_X where K_SM + 1 = 62 is the ground-state exponent. Non-relativistic matter (N_pol = 0) takes k = 62 ✓ confirmed across {rho_crit, rho_b, rho_c, rho_Lambd... |

## `apf/thermo_four_laws_synthesis.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_thermodynamics_four_laws_synthesis` | theorem | `P` | Banks Paper 40's four-laws result as a derivation-axis synthesis. The four laws are carried by ten [P] lemmas composed by exact identity: zeroth = L_beta_temp (beta = sigma/eps, a state function), first = T_realignment_cost_is_transition_energy (energy = accumulated cost = n*eps), second = L_irr ... |

## `apf/thooft_anomaly_matching_chiral.py` — 5 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_pi0_two_photon_anomaly_row` | theorem | `P_structural_instrument` | Exact layer: Q_u = 2/3, Q_d = -1/3 re-derived from Y_Q = 1/6 (the L_anomaly_free pattern); the pi0 -> gamma gamma anomaly coefficient computed on three routes -- direct N_c (Q_u^2 - Q_d^2), the 2 N_c T(3) trace form, and the WZW route at k = 3 = N_c (the .337 cross-identity) -- all exactly 1; the... |
| · | `T_stern_phase_custodial_exclusion_conditional` | theorem | `P_structural_instrument` | Exact certificates for the custodially-protected Stern phase (SChSB with vanishing bilinear) at N_f = 3: ABJ remnant U(1)_A -> Z_6 (coefficient 2 N_f = 6); the bilinear k-table (trivial {0, 3} -- k = 3 is fermion parity -- nontrivial {1, 2, 4, 5}; effective group on bilinears Z_3 = Z_6/Z_2, three... |
| · | `T_thooft_matching_symmetric_vacuum_no_go_conditional` | theorem | `P_structural_instrument` | Exact 't Hooft matching certificates for three-flavour chiral-limit QCD (N_c = 3): UV anomalies [SU(3)_L]^3 = 3, doubled mixed = 1; the minimal qqq spectrum fails the baryon equation by an exact mod-3 certificate (cubic alone satisfiable -- the kill is the baryon equation's); the triality selecti... |
| · | `T_vafa_witten_selects_su3v_pattern_conditional` | theorem | `—` | (no summary) |
| · | `T_vafa_witten_strong_parity_not_spontaneously_broken_conditional` | theorem | `—` | (no summary) |

## `apf/top_msr_R_star_real_adapter.py` — 5 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_top_msr_R_star_adapter_certification_P` | theorem | `—` | EVALUATOR_MAP edge in ew movement graph resolves to MOVES_CLEANLY with top_msr_R_star-filled payload. |
| · | `check_T_top_msr_R_star_adapter_external_ledger_declared_P` | theorem | `—` | All 6 required external evaluator ledger fields declared on the top_msr_R_star snapshot. |
| · | `check_T_top_msr_R_star_adapter_no_smuggling_P` | theorem | `—` | No forbidden target-value key in top_msr_R_star payload; target_value_consumed=False. |
| · | `check_T_top_msr_R_star_adapter_payload_contract_P` | theorem | `—` | top_msr_R_star adapter produces ew-shaped route payload with evaluator + codomain filled. |
| · | `check_T_top_msr_R_star_real_adapter_P` | theorem | `—` | top_msr_R_star real adapter wires banked evaluator content into Engine-readable route payload; EVALUATOR_MAP edge fills cleanly; no smuggling; external ledger declared. |

## `apf/top_msr_r_evolution_real_adapter.py` — 6 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_top_msr_r_evolution_adapter_certification_P` | theorem | `—` | EVALUATOR_MAP edge in ew movement graph resolves to MOVES_CLEANLY with top_msr_r_evolution-filled payload. |
| · | `check_T_top_msr_r_evolution_adapter_evaluator_consistent_P` | theorem | `—` | v67 4-loop R-evolution m_t^MSR(R_EW) = 172.7168 GeV inside combined envelope vs PDG direct (z = 0.500). Loop convergence L1->L4 monotone. |
| · | `check_T_top_msr_r_evolution_adapter_external_ledger_declared_P` | theorem | `—` | All 12 required external evaluator ledger fields declared on the top_msr_r_evolution snapshot. |
| · | `check_T_top_msr_r_evolution_adapter_no_smuggling_P` | theorem | `—` | No forbidden target-value key in top_msr_r_evolution payload; target_value_consumed=False. |
| · | `check_T_top_msr_r_evolution_adapter_payload_contract_P` | theorem | `—` | top_msr_r_evolution adapter produces ew-shaped route payload with evaluator + codomain filled. |
| · | `check_T_top_msr_r_evolution_real_adapter_P` | theorem | `—` | top_msr_r_evolution real adapter wires banked evaluator content into Engine-readable route payload; EVALUATOR_MAP edge fills cleanly; no smuggling; external ledger declared. |

## `apf/top_pole_mc_obstruction_real_adapter.py` — 3 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_top_pole_mc_obstruction_adapter_atlas_routes_P` | theorem | `—` | Atlas routes the Top-pole/MC Route 9 payload to OBSTRUCTION_NAMED_CLOSURE. |
| · | `check_T_top_pole_mc_obstruction_adapter_closure_kind_P` | theorem | `—` | Top-pole/MC Route 9 obstruction adapter declares closure_kind=obstruction_named. |
| · | `check_T_top_pole_mc_obstruction_adapter_no_smuggling_P` | theorem | `—` | Top-pole/MC Route 9 obstruction adapter does not consume target pole-mass values. |

## `apf/topological_order_codomain_adapter.py` — 4 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_topological_order_codomain_adapter_atlas_contract_P` | theorem | `P_codomain_adapter_atlas_contract` | Topological order adapter declares the CODOMAIN atlas contract; live payload reaches COHERENT via the engine. |
| · | `check_T_topological_order_codomain_adapter_audit_first_P` | theorem | `P_codomain_adapter_audit_first` | Audit-first non-claims preserved; target not consumed; evaluator ledger declared. |
| · | `check_T_topological_order_codomain_adapter_payload_contract_P` | theorem | `P_codomain_adapter_contract` | Topological order codomain adapter payload carries the required fields and routes through the engine. |
| · | `check_T_topological_order_codomain_adapter_verdict_consistent_P` | theorem | `P_codomain_adapter_verdict_consistent` | Installed Topological order runtime reproduces every fixture verdict through the engine. |

## `apf/trace_anchors.py` — 4 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `L_bottom_apf_trace_from_ratio` | lemma | `P_local | bank-hardened formula` | (no summary) |
| · | `L_top_apf_trace_anchor` | lemma | `P_local | trace-anchor from prior closed local chain` | (no summary) |
| · | `T_no_inverse_inputs_trace_anchors` | theorem | `—` | (no summary) |
| · | `T_quark_apf_trace_anchors` | theorem | `P_local` | (no summary) |

## `apf/trace_scheme_transport.py` — 10 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_colored_qcd_transport_branch_separated` | theorem | `P_boundary` | QCD transport is declared as a separate map; APF_TRACE values are not pole-like exports. |
| · | `T_external_constants_ledger_required` | theorem | `P_boundary | no-smuggling` | External constants may enter only through a declared transport ledger, not through trace-sector closure. |
| · | `T_identity_map_to_physical_scheme_forbidden` | theorem | `P_boundary | no-smuggling` | Physical agreement/disagreement cannot be scored by silently identifying trace and reporting codomains. |
| · | `T_lepton_ew_qed_transport_branch_separated` | theorem | `P_boundary` | Lepton comparison is cleaner than quark comparison but is still a scheme-transport problem. |
| · | `T_no_physical_mass_inverse_fit` | theorem | `P_boundary | no-smuggling` | No physical mass target is used as an inverse calibration input. |
| · | `T_scheme_target_contract_declared` | theorem | `P_boundary` | A target scheme S and scale/convention must be declared before any physical comparison. |
| · | `T_trace_codomain_immutability` | theorem | `P_boundary | no-smuggling` | The APF_TRACE vector enters transport as an immutable input codomain. |
| · | `T_trace_scheme_boundary_declared` | theorem | `P_boundary` | APF_TRACE/W_TRACE closure is separated from physical scheme transport. |
| · | `T_trace_to_scheme_boundary_bank_closure` | theorem | `P_boundary` | The next push is bank-staged: transport is the open theorem, not an implied consequence of APF_TRACE closure. |
| · | `T_trace_to_scheme_inputs_separated` | theorem | `P_boundary` | The next theorem must add transport data, not retune trace anchors to the target spectrum. |

## `apf/trace_sector_closure.py` — 5 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_W_trace_branch_local` | theorem | `P_local` | W trace branch closes locally; physical W-scheme transport remains separate. |
| · | `T_apf_trace_sector_closure` | theorem | `P_local` | Master trace-sector closure theorem for APF_TRACE/W_TRACE codomain. |
| · | `T_ew_trace_sector_closure` | theorem | `P_local` | Local EW trace-sector closure; physical scheme transport remains separate. |
| · | `T_neutrino_boundary_reconciled` | theorem | `P_local_boundary` | Neutrino boundary reconciled for EW trace-sector closure; absolute scale remains conditional. |
| · | `T_qcd_transport_knockouts` | theorem | `P_local_boundary` | QCD transport knockouts closed; physical scheme transport remains open. |

## `apf/trace_to_scheme_transport_theorem.py` — 9 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_admissible_transport_definition_complete` | theorem | `P_transport_theorem` | Admissible transport is a typed, ledgered, uncertainty-propagating map; it is not a codomain relabeling. |
| · | `check_T_bottom_msbar_route_theorem_obligations` | theorem | `P_transport_theorem` | Bottom remains the best colored target, but its physical MSbar export requires the colored route certificate. |
| · | `check_T_no_inverse_fit_transport_theorem` | theorem | `P_transport_theorem | no-smuggling` | Transport may use external constants and counterterms, but not the quantity being predicted as an inverse calibration input. |
| · | `check_T_residuals_are_transport_observables_not_contradictions` | theorem | `P_transport_theorem` | Validation residuals are now assigned to the transport theorem's open finite-map slots. |
| · | `check_T_route_specific_theorem_clauses_enumerated` | theorem | `P_transport_theorem` | The theorem specializes to W, charged-lepton, colored-MSbar, colored-pole, and light-quark routes. |
| · | `check_T_trace_to_scheme_transport_theorem_bank_closure` | theorem | `—` | (no summary) |
| · | `check_T_transport_export_iff_certificate_complete` | theorem | `P_transport_theorem` | The theorem closes the export predicate while proving that no current route satisfies it. |
| · | `check_T_transport_theorem_upstream_banks_closed` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_on_shell_route_theorem_obligations` | theorem | `P_transport_theorem` | W_TRACE is the cleanest first physical-export route, but current paper status remains validation-only. |

## `apf/trace_transport_completion.py` — 12 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_completion_certificate_schema_complete` | theorem | `P_completion_gate` | The completion certificate distinguishes declared stages from evaluated physical transport. |
| · | `T_counterterm_maps_unfilled_at_terminal_gate` | theorem | `P_completion_gate` | Counterterm slots are named but unevaluated; terminal physical transport is not closed. |
| · | `T_evaluated_maps_required_for_completion` | theorem | `P_completion_gate` | Symbolic route composition is not physical transport; each terminal stage needs an evaluated map. |
| · | `T_external_constants_ledger_unfilled_at_terminal_gate` | theorem | `P_completion_gate` | External slots are ledgered but not numerically filled; terminal export remains blocked. |
| · | `T_forbidden_identity_route_terminal_blocked` | theorem | `P_completion_gate | no-smuggling` | The direct identity route remains forbidden at the terminal gate. |
| · | `T_minimal_closable_route_order_declared` | theorem | `P_completion_gate` | The least-burden next closure attempts are W_TRACE and charged-lepton transport; colored/light-quark routes remain harder. |
| · | `T_physical_export_gate_locked_until_all_certificates_filled` | theorem | `P_completion_gate` | The physical export gate is locked for every current route certificate. |
| · | `T_terminal_gate_forbids_target_observable_consumption` | theorem | `P_completion_gate | no-smuggling` | The terminal gate preserves the no-target-observable/no-inverse-fit discipline. |
| · | `T_terminal_route_set_inherited_from_v88` | theorem | `P_completion_gate` | The terminal gate covers all open v8.8 routes and keeps identity transport forbidden. |
| · | `T_trace_transport_completion_gate_bank_closure` | theorem | `P_completion_gate` | Trace transport is fully staged to the terminal gate; the present codebase cannot honestly export physical scheme masses yet. |
| · | `T_transport_completion_status_declared` | theorem | `P_completion_gate` | v8.9 answers the finish question: current bank state does not yet satisfy the physical-export gate. |
| · | `T_uncertainty_protocol_required_before_physical_export` | theorem | `P_completion_gate` | A numerical map without an uncertainty protocol is still not a physical prediction claim. |

## `apf/trace_transport_composition.py` — 14 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_charged_lepton_composition_ordered` | theorem | `P_composition | lepton-branch` | The charged-lepton route now has an ordered QED/EW symbolic composition plan. |
| · | `T_colored_msbar_composition_ordered` | theorem | `P_composition | colored-branch` | The colored short-distance route now has an ordered symbolic composition plan without evaluating QCD transport. |
| · | `T_colored_pole_composition_extends_msbar` | theorem | `P_composition | colored-branch` | Colored pole/on-shell comparison remains a second-leg route after short-distance transport. |
| · | `T_composition_external_slots_accounted_to_route` | theorem | `P_composition | ledger-compatibility` | Stage composition introduces no hidden external constants or counterterm slots beyond the v8.7 routes. |
| · | `T_composition_graph_acyclic` | theorem | `P_composition | DAG` | Every open route has a strictly ordered symbolic composition chain. |
| · | `T_composition_stage_schema_complete` | theorem | `P_composition | no-smuggling` | Each symbolic stage has explicit codomain, prerequisite-map, ledger-slot, and export flags. |
| · | `T_forbidden_identity_route_has_no_composition_plan` | theorem | `P_composition | no-smuggling` | The forbidden identity route is not merely uncomputed; it has no admissible composition plan. |
| · | `T_light_quark_composition_requires_nonperturbative_leg` | theorem | `P_composition | nonperturbative-boundary` | Light-quark comparison is blocked until a nonperturbative convention leg is declared and evaluated. |
| · | `T_open_routes_have_nonempty_stage_plans` | theorem | `P_composition` | All open routes are composition-ready; the forbidden identity route remains planless. |
| · | `T_stage_inputs_exclude_target_observables` | theorem | `P_composition | no-inverse-fit` | Composition stages cannot read physical target masses as inputs. |
| · | `T_stage_outputs_are_intermediate_not_physical_claims` | theorem | `P_composition | codomain-discipline` | All stage outputs are symbolic/intermediate codomains rather than physical mass predictions. |
| · | `T_trace_transport_composition_bank_closure` | theorem | `P_composition` | The trace-to-scheme transport program now has an executable symbolic composition DAG; physical masses remain open. |
| · | `T_transport_composition_status_declared` | theorem | `P_composition` | v8.8 banks how admissible route stages compose while leaving numerical physical transport open. |
| · | `T_w_trace_composition_ordered` | theorem | `P_composition | W_TRACE-boundary` | The W_TRACE route now has an ordered symbolic EW/on-shell composition plan. |

## `apf/trace_transport_ledger.py` — 13 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_counterterm_slots_declared_not_evaluated` | theorem | `P_ledger | boundary` | The transport theorem has named counterterm slots, but this bank does not evaluate them. |
| · | `T_external_constant_slots_declared_not_filled` | theorem | `P_ledger | no-smuggling` | Transport constants are ledger slots only; no hidden numerical constants are used to close physical masses. |
| · | `T_open_transport_proof_obligations_listed` | theorem | `P_ledger | open-problem-discipline` | The ledger names exactly what remains to be proved before physical scheme masses can be claimed. |
| · | `T_publication_claim_ladder_trace_vs_transport` | theorem | `P_ledger | publication-boundary` | The publication language is constrained before the next physical-mass paper draft is written. |
| · | `T_reference_scale_required_before_comparison` | theorem | `P_ledger | boundary` | No physical comparison can be asserted until S(mu) or an equivalent scheme convention is declared. |
| · | `T_target_observables_not_transport_inputs` | theorem | `P_ledger | no-smuggling` | Target observables are barred as transport inputs; they can enter only after the map is fixed for comparison. |
| · | `T_trace_values_remain_immutable_inputs` | theorem | `P_ledger | no-smuggling` | Transport consumes immutable APF_TRACE/W_TRACE inputs; it cannot retune the local trace sector. |
| · | `T_transport_branch_domains_partitioned` | theorem | `P_ledger` | QCD, QED/EW lepton, and W_TRACE transport branches are separated before formulas are attempted. |
| · | `T_transport_factor_graph_acyclic` | theorem | `P_ledger` | The trace-to-scheme problem is staged as an acyclic ledger, not an implicit identity map. |
| · | `T_transport_ledger_bank_closure` | theorem | `P_ledger` | The trace-to-scheme transport ledger is bank-closed as architecture only; physical transport remains open. |
| · | `T_transport_ledger_status_declared` | theorem | `P_ledger` | v8.6 banks the transport ledger architecture while preserving the open physical-transport boundary. |
| · | `T_transport_scheme_contract_schema_complete` | theorem | `P_ledger | no-smuggling` | Any future physical comparison must first instantiate a full target-scheme contract. |
| · | `T_uncertainty_protocol_required` | theorem | `P_ledger` | Trace-to-scheme transport must carry uncertainties and correlations as part of the theorem, not as after-the-fact prose. |

## `apf/trace_transport_routes.py` — 13 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_charged_lepton_route_prerequisites_declared` | theorem | `P_route | lepton-branch` | Charged-lepton physical comparison is routed through QED/EW conversion and a finite-part convention. |
| · | `T_colored_msbar_route_prerequisites_declared` | theorem | `P_route | colored-branch` | The colored MSbar-like route is admissible only as an open QCD running/matching theorem, not by identity. |
| · | `T_colored_pole_route_requires_short_distance_leg` | theorem | `P_route | colored-branch` | Colored pole/on-shell comparison is staged after a short-distance transport leg and a conversion contract. |
| · | `T_identity_route_forbidden` | theorem | `P_route | no-smuggling` | The identity map from APF_TRACE/W_TRACE to physical reporting values remains explicitly forbidden. |
| · | `T_light_quark_route_nonperturbative_contract_required` | theorem | `P_route | nonperturbative-boundary` | Light-quark values cannot be read as APF_TRACE identities; a low-energy/nonperturbative convention must be declared first. |
| · | `T_required_route_families_enumerated` | theorem | `P_route` | The route space is finite and named before physical comparisons are attempted. |
| · | `T_route_counterterm_slots_subset_of_ledger` | theorem | `P_route | ledger-compatibility` | The route classifier declares counterterm obligations but evaluates none of them. |
| · | `T_route_external_slots_subset_of_ledger` | theorem | `P_route | ledger-compatibility` | The route classifier adds no new hidden constants beyond the banked transport ledger slots. |
| · | `T_route_priority_order_declared` | theorem | `P_route | workplan` | The next push should attack named route maps, not the whole physical spectrum at once. |
| · | `T_transport_route_schema_complete` | theorem | `P_route | no-smuggling` | Each route has explicit branch, target-family, prerequisite-map, external-slot, counterterm, and export flags. |
| · | `T_transport_route_status_declared` | theorem | `P_route` | v8.7 banks the transport route map while preserving the open physical-transport boundary. |
| · | `T_transport_routes_bank_closure` | theorem | `P_route` | The trace-to-scheme transport problem is now route-classified; all physical scheme masses remain open until a named route is derived and evaluated. |
| · | `T_w_trace_route_prerequisites_declared` | theorem | `P_route | W_TRACE-boundary` | W_TRACE comparison must pass through an EW input/on-shell convention rather than direct physical identification. |

## `apf/triality_flux_correspondence.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_nality_additivity_is_hhom` | theorem | `P_math | battery/cap scoping + H-hom named beyond grids — identification leg; composed sentence P_structural | flux-exit 3-item stack + battery/cap scoping — saturation conditional in the antecedent` | AT IR SATURATION (antecedent, carried in-sentence, never discharged): an isolated colour charge's screenability grading -- N-ality -- IS, as a map on irrep labels, the center charge whose fusion-ho... |

## `apf/u1y_landau_pole.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_u1y_landau_pole_trans_planckian` | theorem | `P` | b_Y = 41/6 exact; Landau pole = 1.74e41 GeV (PDG anchor) / 2.20e41 GeV (banked 61-count anchor), 22.15-22.26 decades above M_Pl; anchors agree on 1/alpha_Y(M_Z) to 0.26%; per-generation Delta b_Y =... |

## `apf/u_parameter_native.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_U_parameter_native_P` | theorem | `—` | (no summary) |

## `apf/unification.py` — 9 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `I1_holographic` | other | `P` | At a gravitational horizon, the Bekenstein-Hawking entropy (pi_G), the log of the horizon Hilbert-space dimension (ln o pi_Q), and the admissibility-capacity scalar (pi_T) coincide. Verified on the canonical representative horizon with A = 100 Planck units: S_BH = 100, ln(dim H) = 100, ACC_horizo... |
| · | `I2_gauge_cosmological` | other | `P` | At the Standard-Model interface, K_SM = 61 (= 45 + 4 + 12 fermion + Higgs + gauge slots) equals the denominator of every cosmological fraction produced by pi_C: {'Omega_b': '3/61', 'Omega_c': '16/61', 'Omega_Lambda': '42/61'}. Residual partition closure: Omega_m + Omega_Lambda = True. Partition s... |
| · | `I3_thermo_quantum` | other | `P` | On a maximally mixed admissible state, the von Neumann entropy equals the log of the Hilbert-space dimension equals the admissibility-capacity scalar. Verified on the canonical small quantum interface (d = 8): pi_T = 2.07944, ln(dim H) = 2.07944, S_vN(direct) = 2.0794415416798357. Maximum residua... |
| · | `I4_action_thermo` | other | `P` | The log of the APF partition function approaches the admissibility-capacity scalar in the high-temperature limit. Verified on the canonical small quantum interface (d = 8) across decreasing beta trajectory: ACC_target = 2.07944, final ln Z = 2.07944 at beta_min = 1e-06, residual = -5e-07 < bound ... |
| · | `L_horizon_convention_equivalence` | lemma | `P` | Dual-convention formulation of the horizon interface: the ACC bookkeeping convention d_eff = e (cell size 4 ell_P^2, K_Planck = A/(4 ell_P^2), ACC = S_BH directly in nats) and the microstate-realisation convention d_eff = 2 (cell size 4 ln(2) ell_P^2, K_bit integer, dim H = 2^{K_bit} a literal qu... |
| · | `T_ACC_unification` | theorem | `P` | Cross-module consistency audit of the six regime projections of the admissibility-capacity structure. Verifies four identities (holographic, gauge-cosmological, thermo-quantum, action-thermo) at canonical interfaces. At the Standard-Model interface: K_SM = 61 = 45 + 4 + 12, d_eff = 102, N_SM = d_... |
| · | `T_capacity_redistribution_unification` | theorem | `P_comp` | Every non-trivial Delta_alpha(R, t) in an A1-respecting process falls into one or more of {Flow, Commitment, Saturation}, and within each category the local law is uniquely forced by the interface's ACC signature (K, d_eff) together with the regime projection pi.  Exhaustiveness [P] via case anal... |
| · | `T_capacity_transfer_additive` | theorem | `P` | Capacity is extensive (C_total = 61 = 45 + 4 + 12), which fixes the form of every capacity computation and separates two operations. A source->sink TRANSFER subtracts linearly: retained = 1 - transferred, exact, and selected over the amplitude-renormalised 1/(1+transferred) because only the addit... |
| · | `T_partition_rigidity_coverage_v69` | theorem | `P_structural_exhaustive` | Structural coverage check supporting the T_capacity_redistribution_unification meta-theorem. Case (c) of the exhaustiveness proof rules out continuous Delta P != 0 at fixed (K, k) by citing partition-rigidity theorems at every registered partition.  This check enumerates the canonical PARTITION_R... |

## `apf/unification_projection_essentiality.py` — 7 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_projection_essentiality` | theorem | `P_structural_exhaustive` | The six regime projections of the Admissibility-Capacity Ledger — pi_T (thermodynamic, ACC), pi_G (gravitational, ACC_horizon), pi_Q (quantum, N = dim H), pi_F (gauge/field, K), pi_C (cosmological, residual fractions over K), pi_A (action, Boltzmann Z) — are each individually unique at their cano... |
| · | `pi_A_essentiality` | other | `P_structural_exhaustive` | At an action/spectral-triple interface (canonical quantum d = 8), pi_A(acc, beta, H) = sum_g exp(-beta H(g)) is the unique admissible projection satisfying positivity, flat-cost limit (Z = N = 8 when H ≡ 0), and I4 high-T consistency (ln Z -> ACC = ln d = 2.07944 as beta -> 0). Verified: Z(1e-06)... |
| · | `pi_C_essentiality` | other | `P_structural_exhaustive` | At the SM cosmological-partition interface, pi_C(acc_SM) = {Omega_b: 3/61, Omega_c: 16/61, Omega_Lambda: 42/61} is the unique admissible projection satisfying common-denominator (all fractions have denominator K = 61), closure (numerator sum = 61 = K), and I2 consistency (denominator = pi_F). Ver... |
| · | `pi_F_essentiality` | other | `P_structural_exhaustive` | At the SM gauge-template interface, pi_F(acc_SM) = K = 61 is the unique admissible integer-valued projection satisfying L_count (45 + 4 + 12 = 61 partition sum) + I2 gauge-cosmological consistency (common denominator of pi_C). Verified: partition = {'fermions': 45, 'higgs': 4, 'gauge': 12}, sum =... |
| · | `pi_G_essentiality` | other | `P_structural_exhaustive` | At a horizon interface of area A = 100.0 (4*ell_P^2 units), pi_G(acc) = A / (4 ell_P^2) = K = 100.0 nats is the unique admissible projection satisfying area-scaling + holographic saturation + I1 consistency. Verified: doubling A doubles pi_G (200.0 = 2 * 100.0); pi_G agrees with pi_T at the horiz... |
| · | `pi_Q_essentiality` | other | `P_structural_exhaustive` | At a finite-dim quantum interface of dimension d = 8, pi_Q(acc) = N = d_eff^K = 8 is the unique admissible projection satisfying microstate-counting + tensor multiplicativity + I3 consistency. Verified: multiplicativity on composite (d1 * d2 = 3*4 = 12); exp(ACC) agreement (exp(2.07944) = 8 = d =... |
| · | `pi_T_essentiality` | other | `P_structural_exhaustive` | At a thermodynamic interface, pi_T(acc) = ACC = K * ln(d_eff) is the unique admissible projection satisfying Khinchin additivity + regime normalization + I3 consistency. Verified at the SM interface (pi_T = 282.123 = 61*ln(102)), the canonical quantum interface (pi_T = ln(8) = 2.07944), the compo... |

## `apf/unification_three_levels.py` — 17 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `I1_integer` | other | `P` | At a gravitational horizon, the structural capacity K is the area in 4*ell_P^2 units (integer Bekenstein count). Verified on the canonical representative horizon A = 100.0: K_int = floor(A) = 100 = K_record. |
| · | `I1_scalar` | other | `P` | Scalar-level witness of I1 at the canonical horizon A = 100.0: pi_G (S_BH) = 100, ln(pi_Q) = 100, pi_T (ACC) = 100. Maximum residual 0 < tolerance 1e-10. Aliased to check_I1_holographic. |
| · | `I1_subspace` | other | `P` | Subspace-level witness of I1 at the canonical horizon A = 100.0. Promoted from [C, parked] to [P] in Phase 14c.1 by the explicit horizon-subspace functor F_horizon (apf/subspace_functors.py), which satisfies structural conditions (i)-(v) (existence, dimension preservation, monotonicity under hori... |
| · | `I2_integer` | other | `P` | Integer-level witness of I2 at the Standard-Model interface: K = 61 = denominator(Omega_X) for X ∈ {b, c, Lambda}. Residual partition (3, 16, 42) and capacity partition (45, 4, 12) both sum to K = 61. Pure integer arithmetic; no floating tolerance involved. |
| · | `I2_scalar` | other | `P` | Scalar-level witness of I2 at the SM interface: Omega_m + Omega_Lambda = 19/61 + 42/61 = 1. ACC value = K * ln(d_eff) = 61 * ln(102) = 282.123 nats. Omega_Lambda = 42/61 = 42/61. |
| · | `I2_subspace` | other | `P` | Subspace-level witness of I2 at the Standard-Model interface: V_global = 42-dim subspace of V_61 = capacity space, identified with Sector B target space in the second-epsilon decomposition. Dimension-functor identity: dim V_global = 42 = 61 - 19 = K - dim V_local. Tie to scalar level: Omega_Lambd... |
| · | `I3_integer` | other | `P` | Integer-level witness of I3 at a canonical small quantum interface (d = 8, K = 1, d_eff = d): dim H = N = 8 = d. Pure integer equality. |
| · | `I3_scalar` | other | `P` | Scalar-level witness of I3 at the canonical small quantum interface (d = 8): pi_T = 2.07944, ln(dim H) (formal) = 2.07944, S_vN(direct) = 2.0794415416798357. Maximum residual 0 < tolerance 1e-10. Aliased to check_I3_thermo_quantum. |
| · | `I3_subspace` | other | `P` | Subspace-level witness of I3 at the canonical small quantum interface d = 8. Promoted from [C, parked] to [P] in Phase 14c.2 by the explicit quantum-subspace functor F_quantum (apf/subspace_functors.py), which satisfies structural conditions (i)-(v) (existence, dimension preservation, monotonicit... |
| · | `I4_integer` | other | `P` | Integer-level witness of I4: the Boltzmann sum defining pi_A enumerates exactly N = d_eff^K admissible configurations. At the canonical small quantum interface (d = 8): N = 8, sample spectrum length = 8. Pure integer count. |
| · | `I4_scalar` | other | `P` | Scalar-level witness of I4 at the canonical small quantum interface (d = 8): ACC_target = 2.07944, final ln Z = 2.07944 at beta_min = 1e-06, residual -5e-07 < bound 1.5e-06. Monotone convergence: True. Aliased to check_I4_action_thermo. |
| · | `I4_subspace` | other | `P` | Subspace-level witness of I4 at the canonical small quantum interface d = 8. Promoted from [C, parked] to [P] in Phase 14c.3 by the explicit operator-subspace functor F_operator (apf/subspace_functors.py), which satisfies structural conditions (i)-(v) (existence, dimension preservation, monotonic... |
| · | `T_I1_three_level_consistent` | theorem | `P` | Composed three-level consistency for I1 at the canonical horizon (A = 100.0). f_1 (integer -> scalar): K_int * ln(e) = 100 = ACC_horizon = 100, residual 0. f_2 (scalar -> subspace): ACC_scalar / ln(d_eff) = 100 = dim V = 100, residual 0. f_3 (integer -> subspace): K_int = 100 = dim V = dim F_hori... |
| · | `T_I2_three_level_consistent` | theorem | `P` | Headline composed three-level consistency for I2 at the Standard-Model interface. The integer K = 61, the scalar ACC_value = 282.123 nats = K * ln d_eff, and the subspace dim V_global = 42 all witness the same gauge–cosmological structural identity. f_1 (integer -> scalar): K * ln(d_eff) matches ... |
| · | `T_I3_three_level_consistent` | theorem | `P` | Composed three-level consistency for I3 at the canonical small quantum interface (d = 8). f_1 (integer -> scalar): ln(d) = 2.07944 = ACC = 2.07944, residual 0. f_2 (scalar -> subspace, quantum form): exp(ACC_scalar) = 8 = dim V = 8, log-residual 0. f_3 (integer -> subspace): dim_H = 8 = dim V. Su... |
| · | `T_I4_three_level_consistent` | theorem | `P` | Composed three-level consistency for I4 at the canonical small quantum interface (d = 8, N = 8). f_1 (integer -> scalar): ln(N) = 2.07944 = ACC_target = 2.07944, residual 0. f_2 (scalar -> subspace, action form): exp(ACC_target) = 8 = dim V = 8, log-residual 0. f_3 (integer -> subspace): N = 8 = ... |
| · | `T_three_level_unification` | theorem | `P` | Three-level refinement of T_ACC: each consistency identity I1–I4 admits integer / scalar / subspace witnesses, and the inter-level functor diagram (d_eff coercion, dimension functor, direct identification) commutes for each Ik. As of Phase 14c.3, all four Ik are fully [P] at all three levels via ... |

## `apf/universality_forcing.py` — 7 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_C1_symmetry_class` | theorem | `[P_structural]` | Theorem C1 (Paper 11 v3 §3.5): order parameter ϕ_s = P_A(λ) inherits the substrate-algebra symmetry G_Γ via the canonical equivariance of the algebra projection P_A.  Witnessed on U(1) and Z_2 representative substrates with explicit equivariance checks and Goldstone-mode counts.  Substrate algebr... |
| · | `T_C2_codim_one` | theorem | `[P_structural]` | Theorem C2 (Paper 11 v3 §3.5): single scalar deformation λ moves the system off the critical slack; λ = 0 is a codimension-1 hyperplane in the input space.  L_loc factorization makes λ well-defined on connected components; M_Ω forces uniqueness at full saturation; lifted Lotka-Volterra (separate ... |
| · | `T_C3_dimensional_window` | theorem | `[P_structural]` | Theorem C3 (Paper 11 v3 §3.5): conditional on C1 + C4 + standard RG (Wilson-Fisher 1972; Aharony-Stauffer 1976; Janssen-De Dominicis 1976; Hertz-Millis-Sachdev for QCP), the dimensional window d_l ≤ d ≤ d_u is fixed per sub-family.  Mean-field starting point supplied by T_critical_mean_field (Pap... |
| · | `T_C4_dynamics_class` | theorem | `[P_structural]` | Theorem C4 (Paper 11 v3 §3.5): substrate L_irr regime determines dynamics class via Hohenberg-Halperin classification.  Inactive -> Model A/B (sub-families A, B, A'); Absorbing -> DP/Reggeon (sub-family C); Unitary -> CPTP-Schrödinger (sub-family A'').  Upstream L_irr derivation in core.py (check... |
| · | `T_C5_admissibility_classification` | theorem | `[P_structural]` | Theorem (Paper 11 v3 §3.5 gap (c) closer): C5 admissibility classification predicate.  Inputs: (substrate disjointness, clean-system ν, spatial dimension); outputs: (C5a holds, C5b holds, predicted class).  Witness suite: 13-regime audit table from Paper 11 §1.2 + §6 + Appendix C, covering 5 forc... |
| · | `T_capacity_LV_equilibrium_uniqueness` | theorem | `[P_structural]` | Theorem (Paper 11 v3 §3.5 gap (b) closer): capacity-limited Lotka-Volterra dynamics for general n-interface capacity-utilization vector has unique strictly-positive interior equilibrium with global Lyapunov-function convergence (LaSalle invariance principle).  Lifts check_T_LV in generations.py f... |
| · | `T_universality_forced` | theorem | `[P_structural]` | Master Theorem T_universality_forced (Paper 11 v3 §3.5).  Composition of Theorems C1 (symmetry class from substrate algebra), C2 (codimension-1 from L_loc + M_Ω + lifted Lotka-Volterra + Δα-exhaustiveness), C3 (dimensional window from C1 + C4 + standard RG), and C4 (dynamics class from L_irr regi... |

## `apf/up_family_trace.py` — 4 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `B_gram_to_trace_bridge_scale_covariance` | other | `P_local | upstream-banking-ready` | (no summary) |
| · | `L_up_gram_ratios_executable` | lemma | `P_local` | (no summary) |
| · | `T_no_inverse_inputs_up_trace` | theorem | `—` | (no summary) |
| · | `T_up_family_apf_trace_vector` | theorem | `P_local | B_GramToTrace strengthened` | (no summary) |

## `apf/vacuum_label_code.py` — 5 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_banked_registration_coherent_recovery_no_go` | theorem | `P_structural_instrument` | Measure-and-prepare is entanglement-breaking: output separable with any reference; separable overlap with the maximally entangled state <= 1/d (computed, attained); hence F_e <= 1/d = 1/42 and F_avg <= 2/43 at banked constants -- classical-guess level; identity on any dim >= 2 subspace impossible... |
| · | `T_vacuum_label_code_no_leakage` | theorem | `—` | (no summary) |
| · | `T_vacuum_logical_sector_classical_ceiling` | theorem | `P_structural_instrument` | The privacy requirement of P1 admits NO subspace-coherent (pure-isometric) logical sector of dim >= 2: the uniform superposition of the 42 private label states IS the product state \|0>^x61 (exact Fourier collapse, single-channel leak 1 - 1/42); no 2-dim subspace of the common-mode carrier has sta... |
| · | `T_vacuum_mixed_42dim_secret_scheme_exists` | theorem | `P_structural_instrument` | The clause-(c) fit question closes EXISTS at abstract-encoding strength: 60 applications of the mixed ((2,2)) polynomial-code scheme (base \|s> -> p^{-1/2} sum_a \|a, a+s, a+2s>, third register to the environment; p = 43) yield a perfect ((61,61)) scheme for a coherent 42-dim secret with all 61 sha... |
| · | `T_vacuum_sector_aligned_scheme_share_dim_42` | theorem | `—` | (no summary) |

## `apf/vacuum_o1_fork.py` — 2 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_cc_comparator_registry` | theorem | `P_structural_instrument` | Comparator-hygiene registry. Currency bridge: Lambda*G = 8*pi*(rho/M_Pl^4), so T10's count=area prediction -121.550 matches obs -121.544 to 0.007 decades -- the prior -122.2 in T10 was a currency artifact (phantom ~0.65 dec). The count Omega=102^61 is entropy-pinned to 0.0076% by S_dS (no O(1)); ... |
| · | `T_vacuum_o1_reading_fork` | theorem | `P_structural` | NAMED READING FORK (never a prediction row; the .305 fork-containment precedent). The vacuum O(1) in rho_Lambda/M_Pl^4 = O(1)/102^61 is banked twice: 3/8 (T10, count=area reading) and 42/102 (two-factor reading); exact ratio 56/51 (9.8%). At current obs -122.944 BOTH pass the shared 0.05-decade g... |

## `apf/vacuum_scheme_covariance.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_vacuum_scheme_product_affine_covariance` | theorem | `—` | (no summary) |

## `apf/w_os_route_terminal_closure.py` — 2 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `w_os_delta_r_rem_principled_terminal_boundary` | other | `—` | Physical W export is a principled [P_boundary]: Delta r_rem is gauge-invariant but has no scheme-free standalone measurement, so the four loop-route certificates are retired-not-missing; the native equilibrium+custodial mechanism (M_W=80.3336, 0.044%) carries the physics. Route residual 23.7 MeV ... |
| · | `w_os_route_terminal_closure` | other | `—` | (no summary) |

## `apf/w_trace_BSY_one_loop_kappa_l_native_validator.py` — 2 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_BSY_one_loop_kappa_l_assembly_consistency_at_Denner_validated_inputs` | theorem | `P_one_loop_BSY_3pt_at_Denner_validated_inputs_assembly_consistency` | At Denner-validated inputs (sW²=0.223339, α(M_Z)=1/128.21, m_t=140 GeV, M_H=100 GeV via v24.3.99 hardcoded globals), the BSY (EWWGR Eq 175) composition g_V^ℓ = v_ℓ_tree + 2sc·Q_ℓ·Π̂^γZ_R + F_V^Zℓ, g_A^ℓ = a_ℓ_tree + F_A^Zℓ produces: |
| · | `T_w_trace_kappa_l_ACFW_published_one_loop_benchmark` | theorem | `P_structural_instrument` | The banked _bsy_compose (source-exact eq-rself transcription, .358), run at the ACFW deck (m_t=178.0, m_b=4.85, M_W=80.426, M_Z=91.1876 → sW²=0.222104, α(0) frame), against the published full one-loop O(α) Δκ (Table II): |

## `apf/w_trace_acfw_candidate_preflight.py` — 13 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_w_trace_acfw_candidate_preflight_apf_anchor_forbidden` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_acfw_candidate_preflight_bank_closure` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_acfw_candidate_preflight_can_supply_forward_prediction` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_acfw_candidate_preflight_candidate_id_known` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_acfw_candidate_preflight_candidate_not_admitted` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_acfw_candidate_preflight_comparison_last` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_acfw_candidate_preflight_derive_delta_r_after_forward_output` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_acfw_candidate_preflight_locked_no_export` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_acfw_candidate_preflight_observed_w_forbidden` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_acfw_candidate_preflight_payload_kind_standard` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_acfw_candidate_preflight_record_clean` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_acfw_candidate_preflight_status_declared` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_acfw_candidate_preflight_upstream_registry_present` | theorem | `—` | (no summary) |

## `apf/w_trace_acfw_delta_r_extraction_attempt.py` — 20 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_w_trace_acfw_bank_closure` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_acfw_delta_r_close_neighborhood` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_acfw_delta_r_not_identical_to_apf_target` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_acfw_dimensionless_inputs_nontrivial` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_acfw_extraction_status_declared` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_acfw_forbidden_token_scan_clean` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_acfw_forbidden_token_scan_detects_bad_payload` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_acfw_inverts_to_reasonable_delta_r` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_acfw_no_component_sum_claim` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_acfw_no_covariance_claim` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_acfw_no_physical_w_export` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_acfw_payload_admitted_for_comparison_only` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_acfw_payload_candidate_extracted` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_acfw_predicts_reasonable_mw_window` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_acfw_reference_point_recovers_MW0` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_acfw_report_has_got_there_verdict` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_acfw_source_forbids_apf_anchor_input` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_acfw_source_forbids_observed_w` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_acfw_source_is_standard_parametrization` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_acfw_w_gap_mev_small` | theorem | `—` | (no summary) |

## `apf/w_trace_admitted_row_covariance_bridge.py` — 30 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_w_admitted_row_covariance_bridge_admitted_rows_construct_covariance_record` | theorem | `P_w_admitted_row_covariance_bridge` | (no summary) |
| · | `T_w_admitted_row_covariance_bridge_bank_closure` | theorem | `—` | (no summary) |
| · | `T_w_admitted_row_covariance_bridge_blocks_physical_export_request` | theorem | `P_w_admitted_row_covariance_bridge` | (no summary) |
| · | `T_w_admitted_row_covariance_bridge_component_sum_bridge_integrates` | theorem | `P_w_admitted_row_covariance_bridge` | (no summary) |
| · | `T_w_admitted_row_covariance_bridge_covariance_preserves_order` | theorem | `P_w_admitted_row_covariance_bridge` | (no summary) |
| · | `T_w_admitted_row_covariance_bridge_default_empty_no_covariance` | theorem | `P_w_admitted_row_covariance_bridge` | (no summary) |
| · | `T_w_admitted_row_covariance_bridge_default_export_locked` | theorem | `P_w_admitted_row_covariance_bridge` | (no summary) |
| · | `T_w_admitted_row_covariance_bridge_depends_on_v105_uncertainty_harness` | theorem | `—` | (no summary) |
| · | `T_w_admitted_row_covariance_bridge_depends_on_v109_bundle_gate` | theorem | `—` | (no summary) |
| · | `T_w_admitted_row_covariance_bridge_depends_on_v110_sum_bridge` | theorem | `—` | (no summary) |
| · | `T_w_admitted_row_covariance_bridge_diagonal_from_row_uncertainties` | theorem | `P_w_admitted_row_covariance_bridge` | (no summary) |
| · | `T_w_admitted_row_covariance_bridge_dry_path_certifies_uncertainty_mechanics` | theorem | `P_w_admitted_row_covariance_bridge` | (no summary) |
| · | `T_w_admitted_row_covariance_bridge_dry_path_does_not_unlock_export` | theorem | `P_w_admitted_row_covariance_bridge` | (no summary) |
| · | `T_w_admitted_row_covariance_bridge_empty_bundle_cannot_certify_covariance` | theorem | `P_w_admitted_row_covariance_bridge` | (no summary) |
| · | `T_w_admitted_row_covariance_bridge_export_lock_still_false` | theorem | `P_w_admitted_row_covariance_bridge` | (no summary) |
| · | `T_w_admitted_row_covariance_bridge_forbidden_inputs_named` | theorem | `P_w_admitted_row_covariance_bridge` | (no summary) |
| · | `T_w_admitted_row_covariance_bridge_forbids_apf_anchor_covariance_input` | theorem | `P_w_admitted_row_covariance_bridge` | (no summary) |
| · | `T_w_admitted_row_covariance_bridge_forbids_observed_w_uncertainty_input` | theorem | `P_w_admitted_row_covariance_bridge` | (no summary) |
| · | `T_w_admitted_row_covariance_bridge_forbids_residual_fit_consumption` | theorem | `P_w_admitted_row_covariance_bridge` | (no summary) |
| · | `T_w_admitted_row_covariance_bridge_manifest_remains_open` | theorem | `P_w_admitted_row_covariance_bridge` | (no summary) |
| · | `T_w_admitted_row_covariance_bridge_no_physical_mass_export` | theorem | `P_w_admitted_row_covariance_bridge` | (no summary) |
| · | `T_w_admitted_row_covariance_bridge_policy_blocks_export` | theorem | `P_w_admitted_row_covariance_bridge` | (no summary) |
| · | `T_w_admitted_row_covariance_bridge_rejected_bundle_cannot_certify_covariance` | theorem | `P_w_admitted_row_covariance_bridge` | (no summary) |
| · | `T_w_admitted_row_covariance_bridge_rejects_asymmetric_covariance` | theorem | `P_w_admitted_row_covariance_bridge` | (no summary) |
| · | `T_w_admitted_row_covariance_bridge_rejects_bad_covariance_shape` | theorem | `P_w_admitted_row_covariance_bridge` | (no summary) |
| · | `T_w_admitted_row_covariance_bridge_rejects_negative_variance` | theorem | `P_w_admitted_row_covariance_bridge` | (no summary) |
| · | `T_w_admitted_row_covariance_bridge_required_fields_declared` | theorem | `P_w_admitted_row_covariance_bridge` | (no summary) |
| · | `T_w_admitted_row_covariance_bridge_requires_component_sum_certificate` | theorem | `P_w_admitted_row_covariance_bridge` | (no summary) |
| · | `T_w_admitted_row_covariance_bridge_sigma_delta_r_computable` | theorem | `P_w_admitted_row_covariance_bridge` | (no summary) |
| · | `T_w_admitted_row_covariance_bridge_status_declared` | theorem | `P_w_admitted_row_covariance_bridge` | (no summary) |

## `apf/w_trace_apf_native_one_loop_evaluator.py` — 40 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_w_trace_native_one_loop_admitted_dizet_rows_available` | theorem | `P_w_trace_apf_native_one_loop_evaluator_scaffold` | (no summary) |
| · | `check_T_w_trace_native_one_loop_bank_closure` | theorem | `P_w_trace_apf_native_one_loop_evaluator_scaffold` | (no summary) |
| · | `check_T_w_trace_native_one_loop_c2_over_s2_physical` | theorem | `P_w_trace_apf_native_one_loop_evaluator_scaffold` | (no summary) |
| · | `check_T_w_trace_native_one_loop_delta_alpha_admitted_positive` | theorem | `P_w_trace_apf_native_one_loop_evaluator_scaffold` | (no summary) |
| · | `check_T_w_trace_native_one_loop_delta_alpha_not_apf_owned` | theorem | `P_w_trace_apf_native_one_loop_evaluator_scaffold` | (no summary) |
| · | `check_T_w_trace_native_one_loop_delta_rho_formula_positive` | theorem | `P_w_trace_apf_native_one_loop_evaluator_scaffold` | (no summary) |
| · | `check_T_w_trace_native_one_loop_depends_on_v165` | theorem | `P_w_trace_apf_native_one_loop_evaluator_scaffold` | (no summary) |
| · | `check_T_w_trace_native_one_loop_dizet_total_range` | theorem | `P_w_trace_apf_native_one_loop_evaluator_scaffold` | (no summary) |
| · | `check_T_w_trace_native_one_loop_dmd_delta_r_nonzero` | theorem | `P_w_trace_apf_native_one_loop_evaluator_scaffold` | (no summary) |
| · | `check_T_w_trace_native_one_loop_finite_remainder_nonzero` | theorem | `P_w_trace_apf_native_one_loop_evaluator_scaffold` | (no summary) |
| · | `check_T_w_trace_native_one_loop_first_failed_gate_exact` | theorem | `P_w_trace_apf_native_one_loop_evaluator_scaffold` | (no summary) |
| · | `check_T_w_trace_native_one_loop_forbidden_claims_present` | theorem | `P_w_trace_apf_native_one_loop_evaluator_scaffold` | (no summary) |
| · | `check_T_w_trace_native_one_loop_formal_boundary_correct` | theorem | `P_w_trace_apf_native_one_loop_evaluator_scaffold` | (no summary) |
| · | `check_T_w_trace_native_one_loop_formulae_five` | theorem | `P_w_trace_apf_native_one_loop_evaluator_scaffold` | (no summary) |
| · | `check_T_w_trace_native_one_loop_formulae_include_closed_and_open` | theorem | `P_w_trace_apf_native_one_loop_evaluator_scaffold` | (no summary) |
| · | `check_T_w_trace_native_one_loop_gap_explains_need_for_finite_part` | theorem | `P_w_trace_apf_native_one_loop_evaluator_scaffold` | (no summary) |
| · | `check_T_w_trace_native_one_loop_gap_mw_scale_large` | theorem | `P_w_trace_apf_native_one_loop_evaluator_scaffold` | (no summary) |
| · | `check_T_w_trace_native_one_loop_gap_rows_three` | theorem | `P_w_trace_apf_native_one_loop_evaluator_scaffold` | (no summary) |
| · | `check_T_w_trace_native_one_loop_has_apf_owned_row` | theorem | `P_w_trace_apf_native_one_loop_evaluator_scaffold` | (no summary) |
| · | `check_T_w_trace_native_one_loop_input_sigma_preserved` | theorem | `P_w_trace_apf_native_one_loop_evaluator_scaffold` | (no summary) |
| · | `check_T_w_trace_native_one_loop_inputs_declared` | theorem | `P_w_trace_apf_native_one_loop_evaluator_scaffold` | (no summary) |
| · | `check_T_w_trace_native_one_loop_mw_state_preserved` | theorem | `P_w_trace_apf_native_one_loop_evaluator_scaffold` | (no summary) |
| · | `check_T_w_trace_native_one_loop_native_rows_three` | theorem | `P_w_trace_apf_native_one_loop_evaluator_scaffold` | (no summary) |
| · | `check_T_w_trace_native_one_loop_next_gate_exact` | theorem | `P_w_trace_apf_native_one_loop_evaluator_scaffold` | (no summary) |
| · | `check_T_w_trace_native_one_loop_no_full_loop_claim` | theorem | `P_w_trace_apf_native_one_loop_evaluator_scaffold` | (no summary) |
| · | `check_T_w_trace_native_one_loop_open_finite_row_marked` | theorem | `P_w_trace_apf_native_one_loop_evaluator_scaffold` | (no summary) |
| · | `check_T_w_trace_native_one_loop_payload_digest_present` | theorem | `P_w_trace_apf_native_one_loop_evaluator_scaffold` | (no summary) |
| · | `check_T_w_trace_native_one_loop_pull_state_preserved` | theorem | `P_w_trace_apf_native_one_loop_evaluator_scaffold` | (no summary) |
| · | `check_T_w_trace_native_one_loop_report_contains_gap_rows` | theorem | `P_w_trace_apf_native_one_loop_evaluator_scaffold` | (no summary) |
| · | `check_T_w_trace_native_one_loop_report_contains_rows` | theorem | `P_w_trace_apf_native_one_loop_evaluator_scaffold` | (no summary) |
| · | `check_T_w_trace_native_one_loop_residual_positive` | theorem | `P_w_trace_apf_native_one_loop_evaluator_scaffold` | (no summary) |
| · | `check_T_w_trace_native_one_loop_residual_split_closes` | theorem | `P_w_trace_apf_native_one_loop_evaluator_scaffold` | (no summary) |
| · | `check_T_w_trace_native_one_loop_rho_branch_negative` | theorem | `P_w_trace_apf_native_one_loop_evaluator_scaffold` | (no summary) |
| · | `check_T_w_trace_native_one_loop_rho_resummation_gap_nonzero` | theorem | `P_w_trace_apf_native_one_loop_evaluator_scaffold` | (no summary) |
| · | `check_T_w_trace_native_one_loop_s2_physical` | theorem | `P_w_trace_apf_native_one_loop_evaluator_scaffold` | (no summary) |
| · | `check_T_w_trace_native_one_loop_safe_claims_present` | theorem | `P_w_trace_apf_native_one_loop_evaluator_scaffold` | (no summary) |
| · | `check_T_w_trace_native_one_loop_skeleton_value_range` | theorem | `P_w_trace_apf_native_one_loop_evaluator_scaffold` | (no summary) |
| · | `check_T_w_trace_native_one_loop_status_declared` | theorem | `P_w_trace_apf_native_one_loop_evaluator_scaffold` | (no summary) |
| · | `check_T_w_trace_native_one_loop_transport_status_preserved` | theorem | `P_w_trace_apf_native_one_loop_evaluator_scaffold` | (no summary) |
| · | `check_T_w_trace_native_one_loop_v165_export_candidate_preserved` | theorem | `P_w_trace_apf_native_one_loop_evaluator_scaffold` | (no summary) |

## `apf/w_trace_candidate_payload_attempt.py` — 26 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_w_candidate_payload_attempt_absence_certificate_names_missing_rows` | theorem | `—` | (no summary) |
| · | `T_w_candidate_payload_attempt_bank_closure` | theorem | `—` | (no summary) |
| · | `T_w_candidate_payload_attempt_candidate_gate_accepts_shape_path` | theorem | `—` | (no summary) |
| · | `T_w_candidate_payload_attempt_certificate_schema_declared` | theorem | `—` | (no summary) |
| · | `T_w_candidate_payload_attempt_component_sum_not_certified_even_on_dry_path` | theorem | `—` | (no summary) |
| · | `T_w_candidate_payload_attempt_depends_on_v102_candidate_gate` | theorem | `—` | (no summary) |
| · | `T_w_candidate_payload_attempt_does_not_promote_shape_to_real_payload` | theorem | `—` | (no summary) |
| · | `T_w_candidate_payload_attempt_empty_by_default` | theorem | `—` | (no summary) |
| · | `T_w_candidate_payload_attempt_forbidden_columns_include_apf_anchor` | theorem | `—` | (no summary) |
| · | `T_w_candidate_payload_attempt_forbidden_columns_include_observed_W` | theorem | `—` | (no summary) |
| · | `T_w_candidate_payload_attempt_manifest_remains_no_real_rows` | theorem | `—` | (no summary) |
| · | `T_w_candidate_payload_attempt_parses_json_payload_through_metadata` | theorem | `—` | (no summary) |
| · | `T_w_candidate_payload_attempt_physical_export_remains_locked` | theorem | `—` | (no summary) |
| · | `T_w_candidate_payload_attempt_rejects_apf_anchor_consuming_row` | theorem | `—` | (no summary) |
| · | `T_w_candidate_payload_attempt_rejects_bad_metadata_digest` | theorem | `—` | (no summary) |
| · | `T_w_candidate_payload_attempt_rejects_missing_component` | theorem | `—` | (no summary) |
| · | `T_w_candidate_payload_attempt_rejects_observed_W_consuming_row` | theorem | `—` | (no summary) |
| · | `T_w_candidate_payload_attempt_rejects_physical_export_request` | theorem | `—` | (no summary) |
| · | `T_w_candidate_payload_attempt_rejects_symbol_mismatch` | theorem | `—` | (no summary) |
| · | `T_w_candidate_payload_attempt_rejects_synthetic_metadata` | theorem | `—` | (no summary) |
| · | `T_w_candidate_payload_attempt_rejects_unreviewed_metadata` | theorem | `—` | (no summary) |
| · | `T_w_candidate_payload_attempt_report_schema_declared` | theorem | `—` | (no summary) |
| · | `T_w_candidate_payload_attempt_requires_real_payload_flag_for_admission` | theorem | `—` | (no summary) |
| · | `T_w_candidate_payload_attempt_shape_rows_cover_all_components` | theorem | `—` | (no summary) |
| · | `T_w_candidate_payload_attempt_shape_symbols_match` | theorem | `—` | (no summary) |
| · | `T_w_candidate_payload_attempt_status_declared` | theorem | `P_w_candidate_payload_attempt_gate` | (no summary) |

## `apf/w_trace_cms_global_fit_context.py` — 13 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_w_trace_cms_context_bank_closure` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_cms_context_declares_no_apf_input` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_cms_context_declares_no_cms_measurement_input` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_cms_context_delta_r_inverted` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_cms_context_detects_bad_token` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_cms_context_forbidden_scan_clean` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_cms_context_gap_few_mev` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_cms_context_gap_within_prediction_uncertainty` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_cms_context_kind_is_prediction_not_measurement` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_cms_context_mw_value_reasonable` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_cms_context_no_export` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_cms_context_sigma_value_reasonable` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_cms_context_status_declared` | theorem | `—` | (no summary) |

## `apf/w_trace_component_sum_certificate.py` — 23 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_w_component_sum_certificate_attempt_gate_shape_path_not_real` | theorem | `—` | (no summary) |
| · | `T_w_component_sum_certificate_bank_closure` | theorem | `—` | (no summary) |
| · | `T_w_component_sum_certificate_computes_decimal_sum` | theorem | `—` | (no summary) |
| · | `T_w_component_sum_certificate_depends_on_v103_attempt_gate` | theorem | `—` | (no summary) |
| · | `T_w_component_sum_certificate_dry_path_within_tolerance` | theorem | `—` | (no summary) |
| · | `T_w_component_sum_certificate_empty_by_default` | theorem | `—` | (no summary) |
| · | `T_w_component_sum_certificate_forbidden_inputs_named` | theorem | `—` | (no summary) |
| · | `T_w_component_sum_certificate_manifest_remains_open` | theorem | `—` | (no summary) |
| · | `T_w_component_sum_certificate_no_covariance_no_certification` | theorem | `—` | (no summary) |
| · | `T_w_component_sum_certificate_no_physical_mass_exports` | theorem | `—` | (no summary) |
| · | `T_w_component_sum_certificate_no_uncertainty_no_certification` | theorem | `—` | (no summary) |
| · | `T_w_component_sum_certificate_not_admitted_no_certification` | theorem | `—` | (no summary) |
| · | `T_w_component_sum_certificate_policy_blocks_export` | theorem | `—` | (no summary) |
| · | `T_w_component_sum_certificate_rejects_apf_anchor_consumption` | theorem | `—` | (no summary) |
| · | `T_w_component_sum_certificate_rejects_missing_component` | theorem | `—` | (no summary) |
| · | `T_w_component_sum_certificate_rejects_observed_w_consumption` | theorem | `—` | (no summary) |
| · | `T_w_component_sum_certificate_rejects_physical_export_request` | theorem | `—` | (no summary) |
| · | `T_w_component_sum_certificate_rejects_symbol_mismatch` | theorem | `—` | (no summary) |
| · | `T_w_component_sum_certificate_schema_declared` | theorem | `—` | (no summary) |
| · | `T_w_component_sum_certificate_shape_rows_exact_order` | theorem | `—` | (no summary) |
| · | `T_w_component_sum_certificate_status_declared` | theorem | `P_w_component_sum_certificate_harness` | (no summary) |
| · | `T_w_component_sum_certificate_symbols_match` | theorem | `—` | (no summary) |
| · | `T_w_component_sum_certificate_target_available_from_trace_anchor` | theorem | `—` | (no summary) |

## `apf/w_trace_constants_source_ledger.py` — 15 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_w_GF_pdg_source_value_filled` | theorem | `P_w_constants_source_ledger` | G_F_reference is filled from a muon-lifetime source convention and does not consume W mass. |
| · | `T_w_MZ_pdg_source_value_filled` | theorem | `P_w_constants_source_ledger` | M_Z_on_shell_reference is filled from a Z-pole source convention and does not consume W mass. |
| · | `T_w_alpha_coddata_source_value_filled` | theorem | `P_w_constants_source_ledger` | alpha_em_reference is filled from NIST/CODATA inverse-alpha, not from W data. |
| · | `T_w_constants_completion_gate_remains_locked` | theorem | `P_w_constants_source_ledger` | v8.9 terminal export gate remains locked after constants-source fill. |
| · | `T_w_constants_correlation_policy_declared_not_evaluated` | theorem | `P_w_constants_source_ledger` | constant values are filled, but covariance/correlation propagation remains open. |
| · | `T_w_constants_delta_r_and_counterterms_still_open` | theorem | `P_w_constants_source_ledger` | filling external constants does not solve the finite EW correction map. |
| · | `T_w_constants_forbidden_W_inputs_absent` | theorem | `P_w_constants_source_ledger` | the numerical constants ledger consumes no observed W mass and no W residual. |
| · | `T_w_constants_preserve_W_TRACE_input` | theorem | `P_w_constants_source_ledger` | M_W_TRACE remains the upstream APF_TRACE quantity, not a fitted physical input. |
| · | `T_w_constants_publication_claim_ladder` | theorem | `P_w_constants_source_ledger` | v9.2 is a constants-source ledger bank, not a physical W transport bank. |
| · | `T_w_constants_record_schema_complete` | theorem | `P_w_constants_source_ledger` | constant records carry value, unit, uncertainty, source, convention, and W-exclusion fields. |
| · | `T_w_constants_source_ledger_bank_closure` | theorem | `—` | (no summary) |
| · | `T_w_constants_source_ledger_status_declared` | theorem | `—` | (no summary) |
| · | `T_w_constants_symbols_match_v91_allowed_basis` | theorem | `P_w_constants_source_ledger` | only alpha_em_reference, G_F_reference, and M_Z_on_shell_reference are numerically filled. |
| · | `T_w_constants_uncertainties_positive_and_source_tagged` | theorem | `P_w_constants_source_ledger` | all filled constants have uncertainty strings, relative-uncertainty tags, and source URLs. |
| · | `T_w_constants_units_and_dimensions_declared` | theorem | `P_w_constants_source_ledger` | unit contracts are explicit before any W comparison equation can be evaluated. |

## `apf/w_trace_correlated_uncertainty_model.py` — 13 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_w_trace_corr_uncertainty_bank_closure` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_corr_uncertainty_cms_context_included` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_corr_uncertainty_common_floor_positive` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_corr_uncertainty_conservative_gap_under_1p5sigma` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_corr_uncertainty_conservative_sigma_not_smaller` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_corr_uncertainty_conservative_summary_computed` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_corr_uncertainty_gap_few_mev` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_corr_uncertainty_has_four_points` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_corr_uncertainty_leave_one_out_all_under_1p6sigma` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_corr_uncertainty_no_component_claim` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_corr_uncertainty_no_export` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_corr_uncertainty_status_declared` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_corr_uncertainty_uncorrelated_summary_computed` | theorem | `—` | (no summary) |

## `apf/w_trace_counterterm_convention.py` — 27 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_w_counterterm_convention_bank_closure` | theorem | `—` | (no summary) |
| · | `T_w_counterterm_convention_charge_condition_declared` | theorem | `P_w_counterterm_convention_certificate` | (no summary) |
| · | `T_w_counterterm_convention_component_order_preserved` | theorem | `P_w_counterterm_convention_certificate` | (no summary) |
| · | `T_w_counterterm_convention_default_contract_certifies_schema_only` | theorem | `P_w_counterterm_convention_certificate` | (no summary) |
| · | `T_w_counterterm_convention_depends_on_export_lock` | theorem | `—` | (no summary) |
| · | `T_w_counterterm_convention_dry_release_still_requires_other_flags` | theorem | `P_w_counterterm_convention_certificate` | (no summary) |
| · | `T_w_counterterm_convention_export_request_blocked` | theorem | `P_w_counterterm_convention_certificate` | (no summary) |
| · | `T_w_counterterm_convention_finite_part_normalization_declared` | theorem | `P_w_counterterm_convention_certificate` | (no summary) |
| · | `T_w_counterterm_convention_forbids_apf_anchor_backsolve` | theorem | `P_w_counterterm_convention_certificate` | (no summary) |
| · | `T_w_counterterm_convention_forbids_observed_w_input` | theorem | `P_w_counterterm_convention_certificate` | (no summary) |
| · | `T_w_counterterm_convention_forbids_residual_fit` | theorem | `P_w_counterterm_convention_certificate` | (no summary) |
| · | `T_w_counterterm_convention_forbids_tuned_finite_counterterm` | theorem | `P_w_counterterm_convention_certificate` | (no summary) |
| · | `T_w_counterterm_convention_forbids_world_average_input` | theorem | `P_w_counterterm_convention_certificate` | (no summary) |
| · | `T_w_counterterm_convention_maps_to_delta_r_ct_os_slot` | theorem | `P_w_counterterm_convention_certificate` | (no summary) |
| · | `T_w_counterterm_convention_mixing_angle_definition_declared` | theorem | `P_w_counterterm_convention_certificate` | (no summary) |
| · | `T_w_counterterm_convention_no_physical_w_exports` | theorem | `P_w_counterterm_convention_certificate` | (no summary) |
| · | `T_w_counterterm_convention_numeric_values_still_unadmitted` | theorem | `P_w_counterterm_convention_certificate` | (no summary) |
| · | `T_w_counterterm_convention_on_shell_scheme_family_declared` | theorem | `P_w_counterterm_convention_certificate` | (no summary) |
| · | `T_w_counterterm_convention_pole_mass_condition_declared` | theorem | `P_w_counterterm_convention_certificate` | (no summary) |
| · | `T_w_counterterm_convention_policy_blocks_tuning` | theorem | `P_w_counterterm_convention_certificate` | (no summary) |
| · | `T_w_counterterm_convention_preserves_export_lock_default` | theorem | `P_w_counterterm_convention_certificate` | (no summary) |
| · | `T_w_counterterm_convention_rejects_missing_fields` | theorem | `P_w_counterterm_convention_certificate` | (no summary) |
| · | `T_w_counterterm_convention_rejects_wrong_component_slot` | theorem | `P_w_counterterm_convention_certificate` | (no summary) |
| · | `T_w_counterterm_convention_rejects_wrong_scheme_family` | theorem | `P_w_counterterm_convention_certificate` | (no summary) |
| · | `T_w_counterterm_convention_schema_complete` | theorem | `P_w_counterterm_convention_certificate` | (no summary) |
| · | `T_w_counterterm_convention_status_declared` | theorem | `P_w_counterterm_convention_certificate` | (no summary) |
| · | `T_w_counterterm_convention_tadpole_and_gauge_policies_declared` | theorem | `P_w_counterterm_convention_certificate` | (no summary) |

## `apf/w_trace_delta_r_comparison_harness.py` — 13 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_w_trace_delta_r_comparison_harness_bank_closure` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_delta_r_comparison_harness_comparison_allows_clean_admitted` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_delta_r_comparison_harness_comparison_blocks_apf_input` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_delta_r_comparison_harness_comparison_blocks_export` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_delta_r_comparison_harness_comparison_blocks_observed_w` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_delta_r_comparison_harness_comparison_requires_admitted_source` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_delta_r_comparison_harness_forbidden_token_detected` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_delta_r_comparison_harness_locked_no_export` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_delta_r_comparison_harness_residual_nonexport` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_delta_r_comparison_harness_residual_zero_for_target` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_delta_r_comparison_harness_schema_comparison_only` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_delta_r_comparison_harness_status_declared` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_delta_r_comparison_harness_target_preserved` | theorem | `—` | (no summary) |

## `apf/w_trace_delta_r_component_payload.py` — 24 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_w_delta_r_component_payload_bank_closure` | theorem | `P_w_delta_r_component_payload_worksheet` | (no summary) |
| · | `check_T_w_delta_r_component_payload_blockers_are_sharpened` | theorem | `P_w_delta_r_component_payload_worksheet` | (no summary) |
| · | `check_T_w_delta_r_component_payload_component_sum_not_certified` | theorem | `P_w_delta_r_component_payload_worksheet` | (no summary) |
| · | `check_T_w_delta_r_component_payload_delta_alpha_row_matches_pdg_context` | theorem | `P_w_delta_r_component_payload_worksheet` | (no summary) |
| · | `check_T_w_delta_r_component_payload_delta_r_to_mw_sensitivity_consistent` | theorem | `P_w_delta_r_component_payload_worksheet` | (no summary) |
| · | `check_T_w_delta_r_component_payload_depends_on_v152` | theorem | `P_w_delta_r_component_payload_worksheet` | (no summary) |
| · | `check_T_w_delta_r_component_payload_digest_stable` | theorem | `P_w_delta_r_component_payload_worksheet` | (no summary) |
| · | `check_T_w_delta_r_component_payload_exact_eight_slot_order` | theorem | `P_w_delta_r_component_payload_worksheet` | (no summary) |
| · | `check_T_w_delta_r_component_payload_export_lock_closed` | theorem | `P_w_delta_r_component_payload_worksheet` | (no summary) |
| · | `check_T_w_delta_r_component_payload_mw_roundtrip_still_trace` | theorem | `P_w_delta_r_component_payload_worksheet` | (no summary) |
| · | `check_T_w_delta_r_component_payload_no_apf_anchor_as_component_input` | theorem | `P_w_delta_r_component_payload_worksheet` | (no summary) |
| · | `check_T_w_delta_r_component_payload_no_forbidden_tokens` | theorem | `P_w_delta_r_component_payload_worksheet` | (no summary) |
| · | `check_T_w_delta_r_component_payload_no_observed_w_consumed` | theorem | `P_w_delta_r_component_payload_worksheet` | (no summary) |
| · | `check_T_w_delta_r_component_payload_paper_table_has_nine_rows` | theorem | `P_w_delta_r_component_payload_worksheet` | (no summary) |
| · | `check_T_w_delta_r_component_payload_readiness_remains_open` | theorem | `P_w_delta_r_component_payload_worksheet` | (no summary) |
| · | `check_T_w_delta_r_component_payload_remainder_not_apf_row` | theorem | `P_w_delta_r_component_payload_worksheet` | (no summary) |
| · | `check_T_w_delta_r_component_payload_rho_row_negative_and_computed` | theorem | `P_w_delta_r_component_payload_worksheet` | (no summary) |
| · | `check_T_w_delta_r_component_payload_schema_shape_validates_but_not_real` | theorem | `P_w_delta_r_component_payload_worksheet` | (no summary) |
| · | `check_T_w_delta_r_component_payload_source_remainder_closes_total` | theorem | `P_w_delta_r_component_payload_worksheet` | (no summary) |
| · | `check_T_w_delta_r_component_payload_status_declared` | theorem | `P_w_delta_r_component_payload_worksheet` | (no summary) |
| · | `check_T_w_delta_r_component_payload_terminal_verdict` | theorem | `P_w_delta_r_component_payload_worksheet` | (no summary) |
| · | `check_T_w_delta_r_component_payload_two_numeric_proxies_only` | theorem | `P_w_delta_r_component_payload_worksheet` | (no summary) |
| · | `check_T_w_delta_r_component_payload_uncertainty_scale_context_only` | theorem | `P_w_delta_r_component_payload_worksheet` | (no summary) |
| · | `check_T_w_delta_r_component_payload_unfilled_slots_are_named` | theorem | `P_w_delta_r_component_payload_worksheet` | (no summary) |

## `apf/w_trace_delta_r_finite_map.py` — 15 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_w_delta_r_allowed_inputs_are_non_W_plus_trace_anchor` | theorem | `—` | (no summary) |
| · | `T_w_delta_r_completion_gate_remains_locked` | theorem | `—` | (no summary) |
| · | `T_w_delta_r_correlation_and_uncertainty_still_open` | theorem | `—` | (no summary) |
| · | `T_w_delta_r_counterterm_slots_required_unevaluated` | theorem | `—` | (no summary) |
| · | `T_w_delta_r_depends_on_v92_constants_ledger` | theorem | `—` | (no summary) |
| · | `T_w_delta_r_forbidden_target_observables_absent` | theorem | `—` | (no summary) |
| · | `T_w_delta_r_map_not_numerically_evaluated` | theorem | `—` | (no summary) |
| · | `T_w_delta_r_map_schema_complete` | theorem | `—` | (no summary) |
| · | `T_w_delta_r_no_physical_scheme_mass_export` | theorem | `—` | (no summary) |
| · | `T_w_delta_r_preserves_W_TRACE_anchor_without_identity_export` | theorem | `—` | (no summary) |
| · | `T_w_delta_r_publication_claim_ladder` | theorem | `—` | (no summary) |
| · | `T_w_delta_r_relation_template_on_shell_form` | theorem | `—` | (no summary) |
| · | `T_w_delta_r_slots_decomposed_not_fit_residual` | theorem | `—` | (no summary) |
| · | `T_w_delta_r_symbolic_map_bank_closure` | theorem | `—` | (no summary) |
| · | `T_w_delta_r_symbolic_map_status_declared` | theorem | `P_w_delta_r_symbolic_map` | (no summary) |

## `apf/w_trace_delta_r_pull_diagnostics.py` — 13 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_w_trace_pull_diag_aggregate_green` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_pull_diag_all_green` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_pull_diag_all_rows_have_band` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_pull_diag_all_rows_have_sigma` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_pull_diag_bank_closure` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_pull_diag_delta_r_values_reasonable` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_pull_diag_derivative_nonzero` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_pull_diag_export_lock_preserved` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_pull_diag_has_four_rows` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_pull_diag_max_pull_under_1p5sigma` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_pull_diag_mw_gaps_few_mev` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_pull_diag_no_export` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_pull_diag_status_declared` | theorem | `—` | (no summary) |

## `apf/w_trace_delta_r_remainder_resolution.py` — 28 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_w_delta_r_remainder_resolution_acquisition_requirements_complete` | theorem | `P_w_delta_r_remainder_resolution` | (no summary) |
| · | `check_T_w_delta_r_remainder_resolution_apf_remainder_identity` | theorem | `P_w_delta_r_remainder_resolution` | (no summary) |
| · | `check_T_w_delta_r_remainder_resolution_bank_closure` | theorem | `P_w_delta_r_remainder_resolution` | (no summary) |
| · | `check_T_w_delta_r_remainder_resolution_bucket_components_known` | theorem | `P_w_delta_r_remainder_resolution` | (no summary) |
| · | `check_T_w_delta_r_remainder_resolution_bucket_order_declared` | theorem | `P_w_delta_r_remainder_resolution` | (no summary) |
| · | `check_T_w_delta_r_remainder_resolution_buckets_symbolic_only` | theorem | `P_w_delta_r_remainder_resolution` | (no summary) |
| · | `check_T_w_delta_r_remainder_resolution_component_certificate_still_blocked` | theorem | `P_w_delta_r_remainder_resolution` | (no summary) |
| · | `check_T_w_delta_r_remainder_resolution_depends_on_v153` | theorem | `P_w_delta_r_remainder_resolution` | (no summary) |
| · | `check_T_w_delta_r_remainder_resolution_digest_stable` | theorem | `P_w_delta_r_remainder_resolution` | (no summary) |
| · | `check_T_w_delta_r_remainder_resolution_export_lock_preserved` | theorem | `P_w_delta_r_remainder_resolution` | (no summary) |
| · | `check_T_w_delta_r_remainder_resolution_gap_localized_to_remainder` | theorem | `P_w_delta_r_remainder_resolution` | (no summary) |
| · | `check_T_w_delta_r_remainder_resolution_gap_maps_to_known_mev_shift` | theorem | `P_w_delta_r_remainder_resolution` | (no summary) |
| · | `check_T_w_delta_r_remainder_resolution_no_bucket_consumes_apf_anchor_as_fit_input` | theorem | `P_w_delta_r_remainder_resolution` | (no summary) |
| · | `check_T_w_delta_r_remainder_resolution_no_bucket_consumes_observed_w` | theorem | `P_w_delta_r_remainder_resolution` | (no summary) |
| · | `check_T_w_delta_r_remainder_resolution_no_forbidden_tokens` | theorem | `P_w_delta_r_remainder_resolution` | (no summary) |
| · | `check_T_w_delta_r_remainder_resolution_obstruction_blockers_named` | theorem | `P_w_delta_r_remainder_resolution` | (no summary) |
| · | `check_T_w_delta_r_remainder_resolution_pdg_context_crosswalk_present` | theorem | `P_w_delta_r_remainder_resolution` | (no summary) |
| · | `check_T_w_delta_r_remainder_resolution_pdg_source_context_gap_small` | theorem | `P_w_delta_r_remainder_resolution` | (no summary) |
| · | `check_T_w_delta_r_remainder_resolution_priority_order_declared` | theorem | `P_w_delta_r_remainder_resolution` | (no summary) |
| · | `check_T_w_delta_r_remainder_resolution_proxy_digest_stable` | theorem | `P_w_delta_r_remainder_resolution` | (no summary) |
| · | `check_T_w_delta_r_remainder_resolution_sensitivity_consistent_with_v152` | theorem | `P_w_delta_r_remainder_resolution` | (no summary) |
| · | `check_T_w_delta_r_remainder_resolution_source_remainder_identity` | theorem | `P_w_delta_r_remainder_resolution` | (no summary) |
| · | `check_T_w_delta_r_remainder_resolution_source_remainder_matches_upstream` | theorem | `P_w_delta_r_remainder_resolution` | (no summary) |
| · | `check_T_w_delta_r_remainder_resolution_status_declared` | theorem | `P_w_delta_r_remainder_resolution` | (no summary) |
| · | `check_T_w_delta_r_remainder_resolution_table_contains_proxies_and_buckets` | theorem | `P_w_delta_r_remainder_resolution` | (no summary) |
| · | `check_T_w_delta_r_remainder_resolution_table_has_twelve_rows` | theorem | `P_w_delta_r_remainder_resolution` | (no summary) |
| · | `check_T_w_delta_r_remainder_resolution_terminal_verdict` | theorem | `P_w_delta_r_remainder_resolution` | (no summary) |
| · | `check_T_w_delta_r_remainder_resolution_uncertainty_context_only` | theorem | `P_w_delta_r_remainder_resolution` | (no summary) |

## `apf/w_trace_delta_r_route_input_evaluation.py` — 30 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_w_delta_r_route_input_evaluation_apf_rows_sum_to_apf_target` | theorem | `P_w_delta_r_route_input_evaluation` | (no summary) |
| · | `check_T_w_delta_r_route_input_evaluation_bank_closure` | theorem | `P_w_delta_r_route_input_evaluation` | (no summary) |
| · | `check_T_w_delta_r_route_input_evaluation_component_sum_harness_rejects_model_rows` | theorem | `P_w_delta_r_route_input_evaluation` | (no summary) |
| · | `check_T_w_delta_r_route_input_evaluation_depends_on_v156` | theorem | `P_w_delta_r_route_input_evaluation` | (no summary) |
| · | `check_T_w_delta_r_route_input_evaluation_diagonal_reference_is_subconservative` | theorem | `P_w_delta_r_route_input_evaluation` | (no summary) |
| · | `check_T_w_delta_r_route_input_evaluation_digest_present` | theorem | `P_w_delta_r_route_input_evaluation` | (no summary) |
| · | `check_T_w_delta_r_route_input_evaluation_eight_rows_transferred` | theorem | `P_w_delta_r_route_input_evaluation` | (no summary) |
| · | `check_T_w_delta_r_route_input_evaluation_export_boundary_first_failed_gate` | theorem | `P_w_delta_r_route_input_evaluation` | (no summary) |
| · | `check_T_w_delta_r_route_input_evaluation_export_lock_preserved` | theorem | `P_w_delta_r_route_input_evaluation` | (no summary) |
| · | `check_T_w_delta_r_route_input_evaluation_final_readiness_blocked` | theorem | `P_w_delta_r_route_input_evaluation` | (no summary) |
| · | `check_T_w_delta_r_route_input_evaluation_model_status_on_all_rows` | theorem | `P_w_delta_r_route_input_evaluation` | (no summary) |
| · | `check_T_w_delta_r_route_input_evaluation_mw_from_apf_target_matches_trace` | theorem | `P_w_delta_r_route_input_evaluation` | (no summary) |
| · | `check_T_w_delta_r_route_input_evaluation_no_forbidden_tokens` | theorem | `P_w_delta_r_route_input_evaluation` | (no summary) |
| · | `check_T_w_delta_r_route_input_evaluation_rank_one_covariance_digest_stable` | theorem | `P_w_delta_r_route_input_evaluation` | (no summary) |
| · | `check_T_w_delta_r_route_input_evaluation_rank_one_covariance_shape` | theorem | `P_w_delta_r_route_input_evaluation` | (no summary) |
| · | `check_T_w_delta_r_route_input_evaluation_rank_one_covariance_symmetric` | theorem | `P_w_delta_r_route_input_evaluation` | (no summary) |
| · | `check_T_w_delta_r_route_input_evaluation_rank_one_sigma_matches_source_scale` | theorem | `P_w_delta_r_route_input_evaluation` | (no summary) |
| · | `check_T_w_delta_r_route_input_evaluation_reviewed_same_input_not_claimed` | theorem | `P_w_delta_r_route_input_evaluation` | (no summary) |
| · | `check_T_w_delta_r_route_input_evaluation_route_point_declared` | theorem | `P_w_delta_r_route_input_evaluation` | (no summary) |
| · | `check_T_w_delta_r_route_input_evaluation_same_input_closed_but_reviewed_open` | theorem | `P_w_delta_r_route_input_evaluation` | (no summary) |
| · | `check_T_w_delta_r_route_input_evaluation_source_apf_pull_under_two_sigma` | theorem | `P_w_delta_r_route_input_evaluation` | (no summary) |
| · | `check_T_w_delta_r_route_input_evaluation_source_local_sum_preserved` | theorem | `P_w_delta_r_route_input_evaluation` | (no summary) |
| · | `check_T_w_delta_r_route_input_evaluation_source_rows_sum_to_source_total` | theorem | `P_w_delta_r_route_input_evaluation` | (no summary) |
| · | `check_T_w_delta_r_route_input_evaluation_source_total_mw_preserved` | theorem | `P_w_delta_r_route_input_evaluation` | (no summary) |
| · | `check_T_w_delta_r_route_input_evaluation_status_declared` | theorem | `P_w_delta_r_route_input_evaluation` | (no summary) |
| · | `check_T_w_delta_r_route_input_evaluation_terminal_verdict` | theorem | `P_w_delta_r_route_input_evaluation` | (no summary) |
| · | `check_T_w_delta_r_route_input_evaluation_transfer_factors_positive` | theorem | `P_w_delta_r_route_input_evaluation` | (no summary) |
| · | `check_T_w_delta_r_route_input_evaluation_uncertainty_harness_rejects_perturbative_order` | theorem | `P_w_delta_r_route_input_evaluation` | (no summary) |
| · | `check_T_w_delta_r_route_input_evaluation_uncertainty_pushforward_numeric` | theorem | `P_w_delta_r_route_input_evaluation` | (no summary) |
| · | `check_T_w_delta_r_route_input_evaluation_weight_sum_unity` | theorem | `P_w_delta_r_route_input_evaluation` | (no summary) |

## `apf/w_trace_delta_r_row_extraction_closeout.py` — 28 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_w_delta_r_row_extraction_closeout_acfw_candidate_present_upstream` | theorem | `P_w_delta_r_row_extraction_closeout` | (no summary) |
| · | `check_T_w_delta_r_row_extraction_closeout_bank_closure` | theorem | `P_w_delta_r_row_extraction_closeout` | (no summary) |
| · | `check_T_w_delta_r_row_extraction_closeout_bucket_mapping_complete_except_covariance` | theorem | `P_w_delta_r_row_extraction_closeout` | (no summary) |
| · | `check_T_w_delta_r_row_extraction_closeout_component_sum_not_promoted_to_apf_total` | theorem | `P_w_delta_r_row_extraction_closeout` | (no summary) |
| · | `check_T_w_delta_r_row_extraction_closeout_contains_fermionic_and_bosonic_rows` | theorem | `P_w_delta_r_row_extraction_closeout` | (no summary) |
| · | `check_T_w_delta_r_row_extraction_closeout_coverage_extends_v155` | theorem | `P_w_delta_r_row_extraction_closeout` | (no summary) |
| · | `check_T_w_delta_r_row_extraction_closeout_depends_on_v155` | theorem | `P_w_delta_r_row_extraction_closeout` | (no summary) |
| · | `check_T_w_delta_r_row_extraction_closeout_digest_stable` | theorem | `P_w_delta_r_row_extraction_closeout` | (no summary) |
| · | `check_T_w_delta_r_row_extraction_closeout_dimensionless_conversion` | theorem | `P_w_delta_r_row_extraction_closeout` | (no summary) |
| · | `check_T_w_delta_r_row_extraction_closeout_dominant_proxy_not_confused_with_source_one_loop` | theorem | `P_w_delta_r_row_extraction_closeout` | (no summary) |
| · | `check_T_w_delta_r_row_extraction_closeout_export_lock_preserved` | theorem | `P_w_delta_r_row_extraction_closeout` | (no summary) |
| · | `check_T_w_delta_r_row_extraction_closeout_extracts_eight_rows` | theorem | `P_w_delta_r_row_extraction_closeout` | (no summary) |
| · | `check_T_w_delta_r_row_extraction_closeout_first_failed_gate_is_same_input` | theorem | `P_w_delta_r_row_extraction_closeout` | (no summary) |
| · | `check_T_w_delta_r_row_extraction_closeout_mw_shift_preserved` | theorem | `P_w_delta_r_row_extraction_closeout` | (no summary) |
| · | `check_T_w_delta_r_row_extraction_closeout_no_covariance_row_admitted` | theorem | `P_w_delta_r_row_extraction_closeout` | (no summary) |
| · | `check_T_w_delta_r_row_extraction_closeout_no_forbidden_tokens` | theorem | `P_w_delta_r_row_extraction_closeout` | (no summary) |
| · | `check_T_w_delta_r_row_extraction_closeout_numeric_context_preserved` | theorem | `P_w_delta_r_row_extraction_closeout` | (no summary) |
| · | `check_T_w_delta_r_row_extraction_closeout_physical_export_disabled_in_report` | theorem | `P_w_delta_r_row_extraction_closeout` | (no summary) |
| · | `check_T_w_delta_r_row_extraction_closeout_promotion_moved_past_source_located` | theorem | `P_w_delta_r_row_extraction_closeout` | (no summary) |
| · | `check_T_w_delta_r_row_extraction_closeout_raw_values_match_acfw_table1` | theorem | `P_w_delta_r_row_extraction_closeout` | (no summary) |
| · | `check_T_w_delta_r_row_extraction_closeout_row_sum_scope_labeled_source_local` | theorem | `P_w_delta_r_row_extraction_closeout` | (no summary) |
| · | `check_T_w_delta_r_row_extraction_closeout_rows_not_admitted_as_apf_rows` | theorem | `P_w_delta_r_row_extraction_closeout` | (no summary) |
| · | `check_T_w_delta_r_row_extraction_closeout_source_acquisition_no_longer_first_blocker` | theorem | `P_w_delta_r_row_extraction_closeout` | (no summary) |
| · | `check_T_w_delta_r_row_extraction_closeout_source_local_sum_certified` | theorem | `P_w_delta_r_row_extraction_closeout` | (no summary) |
| · | `check_T_w_delta_r_row_extraction_closeout_source_table_input_point_declared` | theorem | `P_w_delta_r_row_extraction_closeout` | (no summary) |
| · | `check_T_w_delta_r_row_extraction_closeout_status_declared` | theorem | `P_w_delta_r_row_extraction_closeout` | (no summary) |
| · | `check_T_w_delta_r_row_extraction_closeout_terminal_verdict` | theorem | `P_w_delta_r_row_extraction_closeout` | (no summary) |
| · | `check_T_w_delta_r_row_extraction_closeout_uncertainty_still_blocked` | theorem | `P_w_delta_r_row_extraction_closeout` | (no summary) |

## `apf/w_trace_delta_r_source_acquisition_matrix.py` — 31 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_w_delta_r_source_acquisition_matrix_acfw_quarantined_as_total` | theorem | `P_w_delta_r_source_acquisition_matrix` | (no summary) |
| · | `check_T_w_delta_r_source_acquisition_matrix_bank_closure` | theorem | `P_w_delta_r_source_acquisition_matrix` | (no summary) |
| · | `check_T_w_delta_r_source_acquisition_matrix_bosonic_bucket_has_bosonic_source` | theorem | `P_w_delta_r_source_acquisition_matrix` | (no summary) |
| · | `check_T_w_delta_r_source_acquisition_matrix_bucket_coverage_complete` | theorem | `P_w_delta_r_source_acquisition_matrix` | (no summary) |
| · | `check_T_w_delta_r_source_acquisition_matrix_bucket_rows_shape` | theorem | `P_w_delta_r_source_acquisition_matrix` | (no summary) |
| · | `check_T_w_delta_r_source_acquisition_matrix_bucket_rows_source_located_not_extracted` | theorem | `P_w_delta_r_source_acquisition_matrix` | (no summary) |
| · | `check_T_w_delta_r_source_acquisition_matrix_candidate_ids_unique` | theorem | `P_w_delta_r_source_acquisition_matrix` | (no summary) |
| · | `check_T_w_delta_r_source_acquisition_matrix_candidate_roles_not_export` | theorem | `P_w_delta_r_source_acquisition_matrix` | (no summary) |
| · | `check_T_w_delta_r_source_acquisition_matrix_candidates_have_citations` | theorem | `P_w_delta_r_source_acquisition_matrix` | (no summary) |
| · | `check_T_w_delta_r_source_acquisition_matrix_claim_boundary_not_export` | theorem | `P_w_delta_r_source_acquisition_matrix` | (no summary) |
| · | `check_T_w_delta_r_source_acquisition_matrix_component_sum_still_blocked` | theorem | `P_w_delta_r_source_acquisition_matrix` | (no summary) |
| · | `check_T_w_delta_r_source_acquisition_matrix_counterterm_bucket_has_convention_source` | theorem | `P_w_delta_r_source_acquisition_matrix` | (no summary) |
| · | `check_T_w_delta_r_source_acquisition_matrix_depends_on_v154` | theorem | `P_w_delta_r_source_acquisition_matrix` | (no summary) |
| · | `check_T_w_delta_r_source_acquisition_matrix_digest_stable` | theorem | `P_w_delta_r_source_acquisition_matrix` | (no summary) |
| · | `check_T_w_delta_r_source_acquisition_matrix_each_bucket_has_multiple_source_paths_where_possible` | theorem | `P_w_delta_r_source_acquisition_matrix` | (no summary) |
| · | `check_T_w_delta_r_source_acquisition_matrix_export_lock_preserved` | theorem | `P_w_delta_r_source_acquisition_matrix` | (no summary) |
| · | `check_T_w_delta_r_source_acquisition_matrix_extraction_protocol_ordered` | theorem | `P_w_delta_r_source_acquisition_matrix` | (no summary) |
| · | `check_T_w_delta_r_source_acquisition_matrix_fermionic_bucket_has_complete_fermionic_source` | theorem | `P_w_delta_r_source_acquisition_matrix` | (no summary) |
| · | `check_T_w_delta_r_source_acquisition_matrix_gap_remains_localized` | theorem | `P_w_delta_r_source_acquisition_matrix` | (no summary) |
| · | `check_T_w_delta_r_source_acquisition_matrix_mw_shift_unchanged` | theorem | `P_w_delta_r_source_acquisition_matrix` | (no summary) |
| · | `check_T_w_delta_r_source_acquisition_matrix_no_candidate_claims_numerical_bucket_rows` | theorem | `P_w_delta_r_source_acquisition_matrix` | (no summary) |
| · | `check_T_w_delta_r_source_acquisition_matrix_no_candidate_supplies_covariance_rows` | theorem | `P_w_delta_r_source_acquisition_matrix` | (no summary) |
| · | `check_T_w_delta_r_source_acquisition_matrix_no_forbidden_tokens` | theorem | `P_w_delta_r_source_acquisition_matrix` | (no summary) |
| · | `check_T_w_delta_r_source_acquisition_matrix_numeric_context_matches_v154` | theorem | `P_w_delta_r_source_acquisition_matrix` | (no summary) |
| · | `check_T_w_delta_r_source_acquisition_matrix_obstruction_is_sharper_than_v154` | theorem | `P_w_delta_r_source_acquisition_matrix` | (no summary) |
| · | `check_T_w_delta_r_source_acquisition_matrix_promotion_matrix_all_blocked_at_extraction` | theorem | `P_w_delta_r_source_acquisition_matrix` | (no summary) |
| · | `check_T_w_delta_r_source_acquisition_matrix_row_state_ladder_declared` | theorem | `P_w_delta_r_source_acquisition_matrix` | (no summary) |
| · | `check_T_w_delta_r_source_acquisition_matrix_status_declared` | theorem | `P_w_delta_r_source_acquisition_matrix` | (no summary) |
| · | `check_T_w_delta_r_source_acquisition_matrix_terminal_verdict` | theorem | `P_w_delta_r_source_acquisition_matrix` | (no summary) |
| · | `check_T_w_delta_r_source_acquisition_matrix_uncertainty_protocol_total_only` | theorem | `P_w_delta_r_source_acquisition_matrix` | (no summary) |
| · | `check_T_w_delta_r_source_acquisition_matrix_uncertainty_still_blocked` | theorem | `P_w_delta_r_source_acquisition_matrix` | (no summary) |

## `apf/w_trace_delta_r_source_candidate_registry.py` — 24 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_w_trace_source_candidate_registry_apf_anchor_comparison_only` | theorem | `—` | (no summary) |
| · | `T_w_trace_source_candidate_registry_bank_closure` | theorem | `—` | (no summary) |
| · | `T_w_trace_source_candidate_registry_candidate_count` | theorem | `—` | (no summary) |
| · | `T_w_trace_source_candidate_registry_candidate_ids_stable` | theorem | `—` | (no summary) |
| · | `T_w_trace_source_candidate_registry_constants_only_not_delta_r_payload` | theorem | `—` | (no summary) |
| · | `T_w_trace_source_candidate_registry_constants_sources_present` | theorem | `—` | (no summary) |
| · | `T_w_trace_source_candidate_registry_counterterm_source_present` | theorem | `—` | (no summary) |
| · | `T_w_trace_source_candidate_registry_extraction_required` | theorem | `—` | (no summary) |
| · | `T_w_trace_source_candidate_registry_forbidden_token_rejected` | theorem | `—` | (no summary) |
| · | `T_w_trace_source_candidate_registry_lineage_source_present` | theorem | `—` | (no summary) |
| · | `T_w_trace_source_candidate_registry_no_candidate_admitted` | theorem | `—` | (no summary) |
| · | `T_w_trace_source_candidate_registry_observed_w_audit_required` | theorem | `—` | (no summary) |
| · | `T_w_trace_source_candidate_registry_physical_export_locked` | theorem | `—` | (no summary) |
| · | `T_w_trace_source_candidate_registry_precision_source_present` | theorem | `—` | (no summary) |
| · | `T_w_trace_source_candidate_registry_priority_order_declared` | theorem | `—` | (no summary) |
| · | `T_w_trace_source_candidate_registry_required_fields_complete` | theorem | `—` | (no summary) |
| · | `T_w_trace_source_candidate_registry_roles_declared` | theorem | `—` | (no summary) |
| · | `T_w_trace_source_candidate_registry_serializable` | theorem | `—` | (no summary) |
| · | `T_w_trace_source_candidate_registry_source_plan_no_export` | theorem | `—` | (no summary) |
| · | `T_w_trace_source_candidate_registry_standard_payload_kind_limited` | theorem | `—` | (no summary) |
| · | `T_w_trace_source_candidate_registry_status_declared` | theorem | `—` | (no summary) |
| · | `T_w_trace_source_candidate_registry_tiers_declared` | theorem | `—` | (no summary) |
| · | `T_w_trace_source_candidate_registry_unknown_candidate_rejected` | theorem | `—` | (no summary) |
| · | `T_w_trace_source_candidate_registry_upstream_mapping_imports` | theorem | `—` | (no summary) |

## `apf/w_trace_delta_r_source_extraction_protocol.py` — 25 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_w_trace_delta_r_source_extraction_protocol_acfw_gets_parametrization_kind` | theorem | `—` | (no summary) |
| · | `T_w_trace_delta_r_source_extraction_protocol_apf_anchor_comparison_only` | theorem | `—` | (no summary) |
| · | `T_w_trace_delta_r_source_extraction_protocol_attestations_required` | theorem | `—` | (no summary) |
| · | `T_w_trace_delta_r_source_extraction_protocol_bad_digest_rejected` | theorem | `—` | (no summary) |
| · | `T_w_trace_delta_r_source_extraction_protocol_bank_closure` | theorem | `—` | (no summary) |
| · | `T_w_trace_delta_r_source_extraction_protocol_candidate_role_mismatch_rejected` | theorem | `—` | (no summary) |
| · | `T_w_trace_delta_r_source_extraction_protocol_completed_synthetic_accepted_pre_admission` | theorem | `—` | (no summary) |
| · | `T_w_trace_delta_r_source_extraction_protocol_constants_get_reference_kind` | theorem | `—` | (no summary) |
| · | `T_w_trace_delta_r_source_extraction_protocol_denner_gets_decomposition_kind` | theorem | `—` | (no summary) |
| · | `T_w_trace_delta_r_source_extraction_protocol_extraction_plan_steps_ordered` | theorem | `—` | (no summary) |
| · | `T_w_trace_delta_r_source_extraction_protocol_forbidden_token_rejected` | theorem | `—` | (no summary) |
| · | `T_w_trace_delta_r_source_extraction_protocol_input_scheme_keys_required` | theorem | `—` | (no summary) |
| · | `T_w_trace_delta_r_source_extraction_protocol_locked_state_no_export` | theorem | `—` | (no summary) |
| · | `T_w_trace_delta_r_source_extraction_protocol_notation_keys_required` | theorem | `—` | (no summary) |
| · | `T_w_trace_delta_r_source_extraction_protocol_payload_kinds_extend_standard` | theorem | `—` | (no summary) |
| · | `T_w_trace_delta_r_source_extraction_protocol_physical_export_request_rejected` | theorem | `—` | (no summary) |
| · | `T_w_trace_delta_r_source_extraction_protocol_priority_order_preserved` | theorem | `—` | (no summary) |
| · | `T_w_trace_delta_r_source_extraction_protocol_required_fields_declared` | theorem | `—` | (no summary) |
| · | `T_w_trace_delta_r_source_extraction_protocol_serializable` | theorem | `—` | (no summary) |
| · | `T_w_trace_delta_r_source_extraction_protocol_status_declared` | theorem | `—` | (no summary) |
| · | `T_w_trace_delta_r_source_extraction_protocol_template_built_for_all_candidates` | theorem | `—` | (no summary) |
| · | `T_w_trace_delta_r_source_extraction_protocol_template_rejected` | theorem | `—` | (no summary) |
| · | `T_w_trace_delta_r_source_extraction_protocol_unknown_candidate_rejected` | theorem | `—` | (no summary) |
| · | `T_w_trace_delta_r_source_extraction_protocol_unknown_plan_rejected` | theorem | `—` | (no summary) |
| · | `T_w_trace_delta_r_source_extraction_protocol_upstream_imports` | theorem | `—` | (no summary) |

## `apf/w_trace_delta_r_source_mapping.py` — 19 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_w_trace_delta_r_source_mapping_apf_anchor_comparison_only` | theorem | `—` | (no summary) |
| · | `T_w_trace_delta_r_source_mapping_apf_anchor_input_forbidden` | theorem | `—` | (no summary) |
| · | `T_w_trace_delta_r_source_mapping_bad_ratio_rejected` | theorem | `—` | (no summary) |
| · | `T_w_trace_delta_r_source_mapping_bank_closure` | theorem | `—` | (no summary) |
| · | `T_w_trace_delta_r_source_mapping_candidate_source_classes_declared` | theorem | `—` | (no summary) |
| · | `T_w_trace_delta_r_source_mapping_comparison_no_export` | theorem | `—` | (no summary) |
| · | `T_w_trace_delta_r_source_mapping_decomposition_payload_allowed` | theorem | `—` | (no summary) |
| · | `T_w_trace_delta_r_source_mapping_forbidden_token_scan` | theorem | `—` | (no summary) |
| · | `T_w_trace_delta_r_source_mapping_input_scheme_preserved` | theorem | `—` | (no summary) |
| · | `T_w_trace_delta_r_source_mapping_legacy_eight_slot_not_required_first` | theorem | `—` | (no summary) |
| · | `T_w_trace_delta_r_source_mapping_missing_component_rejected` | theorem | `—` | (no summary) |
| · | `T_w_trace_delta_r_source_mapping_observed_w_forbidden` | theorem | `—` | (no summary) |
| · | `T_w_trace_delta_r_source_mapping_parametrization_payload_allowed` | theorem | `—` | (no summary) |
| · | `T_w_trace_delta_r_source_mapping_physical_export_locked` | theorem | `—` | (no summary) |
| · | `T_w_trace_delta_r_source_mapping_serializable` | theorem | `—` | (no summary) |
| · | `T_w_trace_delta_r_source_mapping_standard_decomposition_declared` | theorem | `—` | (no summary) |
| · | `T_w_trace_delta_r_source_mapping_status_declared` | theorem | `—` | (no summary) |
| · | `T_w_trace_delta_r_source_mapping_strategy_shift_declared` | theorem | `—` | (no summary) |
| · | `T_w_trace_delta_r_source_mapping_total_payload_allowed` | theorem | `—` | (no summary) |

## `apf/w_trace_delta_r_transport_buildout.py` — 20 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_w_delta_r_transport_buildout_bank_closure` | theorem | `P_w_delta_r_transport_buildout` | (no summary) |
| · | `check_T_w_delta_r_transport_buildout_blockers_are_terminal_and_named` | theorem | `P_w_delta_r_transport_buildout` | (no summary) |
| · | `check_T_w_delta_r_transport_buildout_component_contract_exact_order` | theorem | `P_w_delta_r_transport_buildout` | (no summary) |
| · | `check_T_w_delta_r_transport_buildout_component_sum_absence_locked` | theorem | `P_w_delta_r_transport_buildout` | (no summary) |
| · | `check_T_w_delta_r_transport_buildout_covariance_dryrun_mechanics_available` | theorem | `P_w_delta_r_transport_buildout` | (no summary) |
| · | `check_T_w_delta_r_transport_buildout_depends_on_v151_worksheet` | theorem | `P_w_delta_r_transport_buildout` | (no summary) |
| · | `check_T_w_delta_r_transport_buildout_digest_stable` | theorem | `P_w_delta_r_transport_buildout` | (no summary) |
| · | `check_T_w_delta_r_transport_buildout_does_not_promote_total_to_rows` | theorem | `P_w_delta_r_transport_buildout` | (no summary) |
| · | `check_T_w_delta_r_transport_buildout_export_lock_remains_closed` | theorem | `P_w_delta_r_transport_buildout` | (no summary) |
| · | `check_T_w_delta_r_transport_buildout_forbidden_tokens_absent_from_source_material` | theorem | `P_w_delta_r_transport_buildout` | (no summary) |
| · | `check_T_w_delta_r_transport_buildout_jacobian_negative` | theorem | `P_w_delta_r_transport_buildout` | (no summary) |
| · | `check_T_w_delta_r_transport_buildout_no_physical_export_claim` | theorem | `P_w_delta_r_transport_buildout` | (no summary) |
| · | `check_T_w_delta_r_transport_buildout_on_shell_roundtrip_source` | theorem | `P_w_delta_r_transport_buildout` | (no summary) |
| · | `check_T_w_delta_r_transport_buildout_readiness_remains_open` | theorem | `P_w_delta_r_transport_buildout` | (no summary) |
| · | `check_T_w_delta_r_transport_buildout_real_covariance_absent` | theorem | `P_w_delta_r_transport_buildout` | (no summary) |
| · | `check_T_w_delta_r_transport_buildout_source_residual_matches_linear_sensitivity` | theorem | `P_w_delta_r_transport_buildout` | (no summary) |
| · | `check_T_w_delta_r_transport_buildout_status_declared` | theorem | `P_w_delta_r_transport_buildout` | (no summary) |
| · | `check_T_w_delta_r_transport_buildout_table_has_seven_rows` | theorem | `P_w_delta_r_transport_buildout` | (no summary) |
| · | `check_T_w_delta_r_transport_buildout_trace_anchor_roundtrip` | theorem | `P_w_delta_r_transport_buildout` | (no summary) |
| · | `check_T_w_delta_r_transport_buildout_uncertainty_equivalent_positive` | theorem | `P_w_delta_r_transport_buildout` | (no summary) |

## `apf/w_trace_denner_diagram_coefficient_table_closeout.py` — 51 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_w_trace_denner_coeff_all_rows_have_fields` | theorem | `P_w_trace_denner_diagram_coefficient_table_closeout` | (no summary) |
| · | `check_T_w_trace_denner_coeff_all_rows_have_slots` | theorem | `P_w_trace_denner_diagram_coefficient_table_closeout` | (no summary) |
| · | `check_T_w_trace_denner_coeff_alpha_partial` | theorem | `P_w_trace_denner_diagram_coefficient_table_closeout` | (no summary) |
| · | `check_T_w_trace_denner_coeff_bank_closure` | theorem | `P_w_trace_denner_diagram_coefficient_table_closeout` | (no summary) |
| · | `check_T_w_trace_denner_coeff_basis_not_empty` | theorem | `P_w_trace_denner_diagram_coefficient_table_closeout` | (no summary) |
| · | `check_T_w_trace_denner_coeff_box_row_open` | theorem | `P_w_trace_denner_diagram_coefficient_table_closeout` | (no summary) |
| · | `check_T_w_trace_denner_coeff_closed_ontology_gate` | theorem | `P_w_trace_denner_diagram_coefficient_table_closeout` | (no summary) |
| · | `check_T_w_trace_denner_coeff_closed_schema_gate` | theorem | `P_w_trace_denner_diagram_coefficient_table_closeout` | (no summary) |
| · | `check_T_w_trace_denner_coeff_closed_slot_coverage_gate` | theorem | `P_w_trace_denner_diagram_coefficient_table_closeout` | (no summary) |
| · | `check_T_w_trace_denner_coeff_counterterm_target_range` | theorem | `P_w_trace_denner_diagram_coefficient_table_closeout` | (no summary) |
| · | `check_T_w_trace_denner_coeff_dependency_pass` | theorem | `P_w_trace_denner_diagram_coefficient_table_closeout` | (no summary) |
| · | `check_T_w_trace_denner_coeff_dizet_total_range` | theorem | `P_w_trace_denner_diagram_coefficient_table_closeout` | (no summary) |
| · | `check_T_w_trace_denner_coeff_family_count` | theorem | `P_w_trace_denner_diagram_coefficient_table_closeout` | (no summary) |
| · | `check_T_w_trace_denner_coeff_first_failed_gate_exact` | theorem | `P_w_trace_denner_diagram_coefficient_table_closeout` | (no summary) |
| · | `check_T_w_trace_denner_coeff_forbidden_claims_present` | theorem | `P_w_trace_denner_diagram_coefficient_table_closeout` | (no summary) |
| · | `check_T_w_trace_denner_coeff_forbids_native_closure_claim` | theorem | `P_w_trace_denner_diagram_coefficient_table_closeout` | (no summary) |
| · | `check_T_w_trace_denner_coeff_forbids_projection_as_proof` | theorem | `P_w_trace_denner_diagram_coefficient_table_closeout` | (no summary) |
| · | `check_T_w_trace_denner_coeff_gate_count` | theorem | `P_w_trace_denner_diagram_coefficient_table_closeout` | (no summary) |
| · | `check_T_w_trace_denner_coeff_import_row_count` | theorem | `P_w_trace_denner_diagram_coefficient_table_closeout` | (no summary) |
| · | `check_T_w_trace_denner_coeff_mass_rows_open` | theorem | `P_w_trace_denner_diagram_coefficient_table_closeout` | (no summary) |
| · | `check_T_w_trace_denner_coeff_mw_residual_preserved` | theorem | `P_w_trace_denner_diagram_coefficient_table_closeout` | (no summary) |
| · | `check_T_w_trace_denner_coeff_native_closure_gate_open` | theorem | `P_w_trace_denner_diagram_coefficient_table_closeout` | (no summary) |
| · | `check_T_w_trace_denner_coeff_native_status_open` | theorem | `P_w_trace_denner_diagram_coefficient_table_closeout` | (no summary) |
| · | `check_T_w_trace_denner_coeff_next_gate_exact` | theorem | `P_w_trace_denner_diagram_coefficient_table_closeout` | (no summary) |
| · | `check_T_w_trace_denner_coeff_no_source_formula_imported` | theorem | `P_w_trace_denner_diagram_coefficient_table_closeout` | (no summary) |
| · | `check_T_w_trace_denner_coeff_open_gates_block_native` | theorem | `P_w_trace_denner_diagram_coefficient_table_closeout` | (no summary) |
| · | `check_T_w_trace_denner_coeff_open_rows_block_native` | theorem | `P_w_trace_denner_diagram_coefficient_table_closeout` | (no summary) |
| · | `check_T_w_trace_denner_coeff_payload_digest_present` | theorem | `P_w_trace_denner_diagram_coefficient_table_closeout` | (no summary) |
| · | `check_T_w_trace_denner_coeff_projection_guard_closed` | theorem | `P_w_trace_denner_diagram_coefficient_table_closeout` | (no summary) |
| · | `check_T_w_trace_denner_coeff_projection_has_nonzero_coeffs` | theorem | `P_w_trace_denner_diagram_coefficient_table_closeout` | (no summary) |
| · | `check_T_w_trace_denner_coeff_projection_rows_count` | theorem | `P_w_trace_denner_diagram_coefficient_table_closeout` | (no summary) |
| · | `check_T_w_trace_denner_coeff_projection_rows_fit_only` | theorem | `P_w_trace_denner_diagram_coefficient_table_closeout` | (no summary) |
| · | `check_T_w_trace_denner_coeff_projection_sum_exact` | theorem | `P_w_trace_denner_diagram_coefficient_table_closeout` | (no summary) |
| · | `check_T_w_trace_denner_coeff_qcd_quarantined` | theorem | `P_w_trace_denner_diagram_coefficient_table_closeout` | (no summary) |
| · | `check_T_w_trace_denner_coeff_report_has_families` | theorem | `P_w_trace_denner_diagram_coefficient_table_closeout` | (no summary) |
| · | `check_T_w_trace_denner_coeff_report_has_import_rows` | theorem | `P_w_trace_denner_diagram_coefficient_table_closeout` | (no summary) |
| · | `check_T_w_trace_denner_coeff_report_has_projection` | theorem | `P_w_trace_denner_diagram_coefficient_table_closeout` | (no summary) |
| · | `check_T_w_trace_denner_coeff_required_fields_count` | theorem | `P_w_trace_denner_diagram_coefficient_table_closeout` | (no summary) |
| · | `check_T_w_trace_denner_coeff_required_fields_unique` | theorem | `P_w_trace_denner_diagram_coefficient_table_closeout` | (no summary) |
| · | `check_T_w_trace_denner_coeff_rho_partial` | theorem | `P_w_trace_denner_diagram_coefficient_table_closeout` | (no summary) |
| · | `check_T_w_trace_denner_coeff_route_export_candidate_preserved` | theorem | `P_w_trace_denner_diagram_coefficient_table_closeout` | (no summary) |
| · | `check_T_w_trace_denner_coeff_safe_claims_present` | theorem | `P_w_trace_denner_diagram_coefficient_table_closeout` | (no summary) |
| · | `check_T_w_trace_denner_coeff_sigma_preserved` | theorem | `P_w_trace_denner_diagram_coefficient_table_closeout` | (no summary) |
| · | `check_T_w_trace_denner_coeff_sign_gauge_gate_open` | theorem | `P_w_trace_denner_diagram_coefficient_table_closeout` | (no summary) |
| · | `check_T_w_trace_denner_coeff_source_formula_gate_open` | theorem | `P_w_trace_denner_diagram_coefficient_table_closeout` | (no summary) |
| · | `check_T_w_trace_denner_coeff_status_declared` | theorem | `P_w_trace_denner_diagram_coefficient_table_closeout` | (no summary) |
| · | `check_T_w_trace_denner_coeff_target_closure_zero` | theorem | `P_w_trace_denner_diagram_coefficient_table_closeout` | (no summary) |
| · | `check_T_w_trace_denner_coeff_terminal_report_status` | theorem | `P_w_trace_denner_diagram_coefficient_table_closeout` | (no summary) |
| · | `check_T_w_trace_denner_coeff_v17_slots_covered` | theorem | `P_w_trace_denner_diagram_coefficient_table_closeout` | (no summary) |
| · | `check_T_w_trace_denner_coeff_vertex_box_gate_open` | theorem | `P_w_trace_denner_diagram_coefficient_table_closeout` | (no summary) |
| · | `check_T_w_trace_denner_coeff_vertex_row_open` | theorem | `P_w_trace_denner_diagram_coefficient_table_closeout` | (no summary) |

## `apf/w_trace_denner_formula_import_native_assembly.py` — 62 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_w_trace_formula_import_assembly_row_count` | theorem | `P_w_trace_denner_formula_import_native_assembly` | (no summary) |
| · | `check_T_w_trace_formula_import_bank_closure` | theorem | `P_w_trace_denner_formula_import_native_assembly` | (no summary) |
| · | `check_T_w_trace_formula_import_counterterm_target_preserved` | theorem | `P_w_trace_denner_formula_import_native_assembly` | (no summary) |
| · | `check_T_w_trace_formula_import_coverage_evaluated_fraction` | theorem | `P_w_trace_denner_formula_import_native_assembly` | (no summary) |
| · | `check_T_w_trace_formula_import_coverage_total` | theorem | `P_w_trace_denner_formula_import_native_assembly` | (no summary) |
| · | `check_T_w_trace_formula_import_delta_alpha_evaluated` | theorem | `P_w_trace_denner_formula_import_native_assembly` | (no summary) |
| · | `check_T_w_trace_formula_import_delta_alpha_gate_closed` | theorem | `P_w_trace_denner_formula_import_native_assembly` | (no summary) |
| · | `check_T_w_trace_formula_import_dependency_pass` | theorem | `P_w_trace_denner_formula_import_native_assembly` | (no summary) |
| · | `check_T_w_trace_formula_import_dizet_total_preserved` | theorem | `P_w_trace_denner_formula_import_native_assembly` | (no summary) |
| · | `check_T_w_trace_formula_import_evaluated_rows_count` | theorem | `P_w_trace_denner_formula_import_native_assembly` | (no summary) |
| · | `check_T_w_trace_formula_import_evaluated_rows_numeric` | theorem | `P_w_trace_denner_formula_import_native_assembly` | (no summary) |
| · | `check_T_w_trace_formula_import_first_failed_gate_exact` | theorem | `P_w_trace_denner_formula_import_native_assembly` | (no summary) |
| · | `check_T_w_trace_formula_import_forbidden_claims_present` | theorem | `P_w_trace_denner_formula_import_native_assembly` | (no summary) |
| · | `check_T_w_trace_formula_import_forbids_full_closure` | theorem | `P_w_trace_denner_formula_import_native_assembly` | (no summary) |
| · | `check_T_w_trace_formula_import_forbids_target_as_formula` | theorem | `P_w_trace_denner_formula_import_native_assembly` | (no summary) |
| · | `check_T_w_trace_formula_import_formula_matrix_gate_closed` | theorem | `P_w_trace_denner_formula_import_native_assembly` | (no summary) |
| · | `check_T_w_trace_formula_import_full_native_gate_open` | theorem | `P_w_trace_denner_formula_import_native_assembly` | (no summary) |
| · | `check_T_w_trace_formula_import_gate_count` | theorem | `P_w_trace_denner_formula_import_native_assembly` | (no summary) |
| · | `check_T_w_trace_formula_import_gauge_gate_open` | theorem | `P_w_trace_denner_formula_import_native_assembly` | (no summary) |
| · | `check_T_w_trace_formula_import_missing_families_block` | theorem | `P_w_trace_denner_formula_import_native_assembly` | (no summary) |
| · | `check_T_w_trace_formula_import_missing_families_cover_box` | theorem | `P_w_trace_denner_formula_import_native_assembly` | (no summary) |
| · | `check_T_w_trace_formula_import_missing_families_cover_self_energy` | theorem | `P_w_trace_denner_formula_import_native_assembly` | (no summary) |
| · | `check_T_w_trace_formula_import_missing_families_cover_vertex` | theorem | `P_w_trace_denner_formula_import_native_assembly` | (no summary) |
| · | `check_T_w_trace_formula_import_missing_family_count` | theorem | `P_w_trace_denner_formula_import_native_assembly` | (no summary) |
| · | `check_T_w_trace_formula_import_mw_residual_preserved` | theorem | `P_w_trace_denner_formula_import_native_assembly` | (no summary) |
| · | `check_T_w_trace_formula_import_native_status_partial` | theorem | `P_w_trace_denner_formula_import_native_assembly` | (no summary) |
| · | `check_T_w_trace_formula_import_native_to_full_gap_positive` | theorem | `P_w_trace_denner_formula_import_native_assembly` | (no summary) |
| · | `check_T_w_trace_formula_import_next_gate_exact` | theorem | `P_w_trace_denner_formula_import_native_assembly` | (no summary) |
| · | `check_T_w_trace_formula_import_no_fit_guard_closed` | theorem | `P_w_trace_denner_formula_import_native_assembly` | (no summary) |
| · | `check_T_w_trace_formula_import_no_fitted_coefficients` | theorem | `P_w_trace_denner_formula_import_native_assembly` | (no summary) |
| · | `check_T_w_trace_formula_import_open_gates_block_full` | theorem | `P_w_trace_denner_formula_import_native_assembly` | (no summary) |
| · | `check_T_w_trace_formula_import_open_rows_block_full` | theorem | `P_w_trace_denner_formula_import_native_assembly` | (no summary) |
| · | `check_T_w_trace_formula_import_open_rows_not_numeric` | theorem | `P_w_trace_denner_formula_import_native_assembly` | (no summary) |
| · | `check_T_w_trace_formula_import_open_rows_present` | theorem | `P_w_trace_denner_formula_import_native_assembly` | (no summary) |
| · | `check_T_w_trace_formula_import_partial_assembly_gate_closed` | theorem | `P_w_trace_denner_formula_import_native_assembly` | (no summary) |
| · | `check_T_w_trace_formula_import_partial_native_range` | theorem | `P_w_trace_denner_formula_import_native_assembly` | (no summary) |
| · | `check_T_w_trace_formula_import_partial_native_value` | theorem | `P_w_trace_denner_formula_import_native_assembly` | (no summary) |
| · | `check_T_w_trace_formula_import_payload_digest_present` | theorem | `P_w_trace_denner_formula_import_native_assembly` | (no summary) |
| · | `check_T_w_trace_formula_import_report_has_assembly` | theorem | `P_w_trace_denner_formula_import_native_assembly` | (no summary) |
| · | `check_T_w_trace_formula_import_report_has_missing` | theorem | `P_w_trace_denner_formula_import_native_assembly` | (no summary) |
| · | `check_T_w_trace_formula_import_report_has_rows` | theorem | `P_w_trace_denner_formula_import_native_assembly` | (no summary) |
| · | `check_T_w_trace_formula_import_required_fields_preserved` | theorem | `P_w_trace_denner_formula_import_native_assembly` | (no summary) |
| · | `check_T_w_trace_formula_import_rho_gate_closed` | theorem | `P_w_trace_denner_formula_import_native_assembly` | (no summary) |
| · | `check_T_w_trace_formula_import_rho_lead_evaluated` | theorem | `P_w_trace_denner_formula_import_native_assembly` | (no summary) |
| · | `check_T_w_trace_formula_import_route_export_candidate` | theorem | `P_w_trace_denner_formula_import_native_assembly` | (no summary) |
| · | `check_T_w_trace_formula_import_safe_claims_present` | theorem | `P_w_trace_denner_formula_import_native_assembly` | (no summary) |
| · | `check_T_w_trace_formula_import_self_energy_gate_open` | theorem | `P_w_trace_denner_formula_import_native_assembly` | (no summary) |
| · | `check_T_w_trace_formula_import_sigma_preserved` | theorem | `P_w_trace_denner_formula_import_native_assembly` | (no summary) |
| · | `check_T_w_trace_formula_import_source_row_count` | theorem | `P_w_trace_denner_formula_import_native_assembly` | (no summary) |
| · | `check_T_w_trace_formula_import_status_declared` | theorem | `P_w_trace_denner_formula_import_native_assembly` | (no summary) |
| · | `check_T_w_trace_formula_import_target_closure_gate_closed` | theorem | `P_w_trace_denner_formula_import_native_assembly` | (no summary) |
| · | `check_T_w_trace_formula_import_target_closure_zero` | theorem | `P_w_trace_denner_formula_import_native_assembly` | (no summary) |
| · | `check_T_w_trace_formula_import_target_only_count` | theorem | `P_w_trace_denner_formula_import_native_assembly` | (no summary) |
| · | `check_T_w_trace_formula_import_target_only_value` | theorem | `P_w_trace_denner_formula_import_native_assembly` | (no summary) |
| · | `check_T_w_trace_formula_import_target_row_not_admitted` | theorem | `P_w_trace_denner_formula_import_native_assembly` | (no summary) |
| · | `check_T_w_trace_formula_import_terminal_report_status` | theorem | `P_w_trace_denner_formula_import_native_assembly` | (no summary) |
| · | `check_T_w_trace_formula_import_unique_gates` | theorem | `P_w_trace_denner_formula_import_native_assembly` | (no summary) |
| · | `check_T_w_trace_formula_import_unique_source_rows` | theorem | `P_w_trace_denner_formula_import_native_assembly` | (no summary) |
| · | `check_T_w_trace_formula_import_v18_families_available` | theorem | `P_w_trace_denner_formula_import_native_assembly` | (no summary) |
| · | `check_T_w_trace_formula_import_v18_gates_available` | theorem | `P_w_trace_denner_formula_import_native_assembly` | (no summary) |
| · | `check_T_w_trace_formula_import_v18_import_contract_available` | theorem | `P_w_trace_denner_formula_import_native_assembly` | (no summary) |
| · | `check_T_w_trace_formula_import_vertex_box_gate_open` | theorem | `P_w_trace_denner_formula_import_native_assembly` | (no summary) |

## `apf/w_trace_denner_sirlin_counterterm_functional.py` — 42 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_w_trace_denner_sirlin_bank_closure` | theorem | `P_w_trace_denner_sirlin_counterterm_functional` | (no summary) |
| · | `check_T_w_trace_denner_sirlin_counterterm_evaluator_gate_open` | theorem | `P_w_trace_denner_sirlin_counterterm_functional` | (no summary) |
| · | `check_T_w_trace_denner_sirlin_counterterm_target_mw_scale` | theorem | `P_w_trace_denner_sirlin_counterterm_functional` | (no summary) |
| · | `check_T_w_trace_denner_sirlin_counterterm_target_positive` | theorem | `P_w_trace_denner_sirlin_counterterm_functional` | (no summary) |
| · | `check_T_w_trace_denner_sirlin_covariance_inherited` | theorem | `P_w_trace_denner_sirlin_counterterm_functional` | (no summary) |
| · | `check_T_w_trace_denner_sirlin_dependencies_pass` | theorem | `P_w_trace_denner_sirlin_counterterm_functional` | (no summary) |
| · | `check_T_w_trace_denner_sirlin_dimensional_values_reasonable` | theorem | `P_w_trace_denner_sirlin_counterterm_functional` | (no summary) |
| · | `check_T_w_trace_denner_sirlin_drrem_assembly_closes` | theorem | `P_w_trace_denner_sirlin_counterterm_functional` | (no summary) |
| · | `check_T_w_trace_denner_sirlin_drrem_newdr_positive` | theorem | `P_w_trace_denner_sirlin_counterterm_functional` | (no summary) |
| · | `check_T_w_trace_denner_sirlin_export_candidate_preserved` | theorem | `P_w_trace_denner_sirlin_counterterm_functional` | (no summary) |
| · | `check_T_w_trace_denner_sirlin_finite_remainder_positive` | theorem | `P_w_trace_denner_sirlin_counterterm_functional` | (no summary) |
| · | `check_T_w_trace_denner_sirlin_first_failed_gate_exact` | theorem | `P_w_trace_denner_sirlin_counterterm_functional` | (no summary) |
| · | `check_T_w_trace_denner_sirlin_forbidden_claims_present` | theorem | `P_w_trace_denner_sirlin_counterterm_functional` | (no summary) |
| · | `check_T_w_trace_denner_sirlin_functional_terms_count` | theorem | `P_w_trace_denner_sirlin_counterterm_functional` | (no summary) |
| · | `check_T_w_trace_denner_sirlin_gate_count` | theorem | `P_w_trace_denner_sirlin_counterterm_functional` | (no summary) |
| · | `check_T_w_trace_denner_sirlin_has_finite_remainder` | theorem | `P_w_trace_denner_sirlin_counterterm_functional` | (no summary) |
| · | `check_T_w_trace_denner_sirlin_has_leading_rho` | theorem | `P_w_trace_denner_sirlin_counterterm_functional` | (no summary) |
| · | `check_T_w_trace_denner_sirlin_has_rho_cross_target` | theorem | `P_w_trace_denner_sirlin_counterterm_functional` | (no summary) |
| · | `check_T_w_trace_denner_sirlin_has_running_alpha` | theorem | `P_w_trace_denner_sirlin_counterterm_functional` | (no summary) |
| · | `check_T_w_trace_denner_sirlin_has_total` | theorem | `P_w_trace_denner_sirlin_counterterm_functional` | (no summary) |
| · | `check_T_w_trace_denner_sirlin_imported_v163_equation_closes` | theorem | `P_w_trace_denner_sirlin_counterterm_functional` | (no summary) |
| · | `check_T_w_trace_denner_sirlin_master_identity_closes` | theorem | `P_w_trace_denner_sirlin_counterterm_functional` | (no summary) |
| · | `check_T_w_trace_denner_sirlin_mw_residual_preserved` | theorem | `P_w_trace_denner_sirlin_counterterm_functional` | (no summary) |
| · | `check_T_w_trace_denner_sirlin_next_gate_exact` | theorem | `P_w_trace_denner_sirlin_counterterm_functional` | (no summary) |
| · | `check_T_w_trace_denner_sirlin_no_full_native_claim` | theorem | `P_w_trace_denner_sirlin_counterterm_functional` | (no summary) |
| · | `check_T_w_trace_denner_sirlin_open_gates_block_full_native_loop` | theorem | `P_w_trace_denner_sirlin_counterterm_functional` | (no summary) |
| · | `check_T_w_trace_denner_sirlin_payload_digest_present` | theorem | `P_w_trace_denner_sirlin_counterterm_functional` | (no summary) |
| · | `check_T_w_trace_denner_sirlin_pull_preserved` | theorem | `P_w_trace_denner_sirlin_counterterm_functional` | (no summary) |
| · | `check_T_w_trace_denner_sirlin_qcd_terms_physical_signs` | theorem | `P_w_trace_denner_sirlin_counterterm_functional` | (no summary) |
| · | `check_T_w_trace_denner_sirlin_report_has_drrem_assembly` | theorem | `P_w_trace_denner_sirlin_counterterm_functional` | (no summary) |
| · | `check_T_w_trace_denner_sirlin_report_has_gates` | theorem | `P_w_trace_denner_sirlin_counterterm_functional` | (no summary) |
| · | `check_T_w_trace_denner_sirlin_report_has_master_identity` | theorem | `P_w_trace_denner_sirlin_counterterm_functional` | (no summary) |
| · | `check_T_w_trace_denner_sirlin_report_has_terms` | theorem | `P_w_trace_denner_sirlin_counterterm_functional` | (no summary) |
| · | `check_T_w_trace_denner_sirlin_rho_gap_negative` | theorem | `P_w_trace_denner_sirlin_counterterm_functional` | (no summary) |
| · | `check_T_w_trace_denner_sirlin_safe_claims_present` | theorem | `P_w_trace_denner_sirlin_counterterm_functional` | (no summary) |
| · | `check_T_w_trace_denner_sirlin_scalar_integral_gate_open` | theorem | `P_w_trace_denner_sirlin_counterterm_functional` | (no summary) |
| · | `check_T_w_trace_denner_sirlin_skeleton_plus_target_equals_total` | theorem | `P_w_trace_denner_sirlin_counterterm_functional` | (no summary) |
| · | `check_T_w_trace_denner_sirlin_status_declared` | theorem | `P_w_trace_denner_sirlin_counterterm_functional` | (no summary) |
| · | `check_T_w_trace_denner_sirlin_symbolic_basis_closed` | theorem | `P_w_trace_denner_sirlin_counterterm_functional` | (no summary) |
| · | `check_T_w_trace_denner_sirlin_target_not_shapeless` | theorem | `P_w_trace_denner_sirlin_counterterm_functional` | (no summary) |
| · | `check_T_w_trace_denner_sirlin_target_split_closes` | theorem | `P_w_trace_denner_sirlin_counterterm_functional` | (no summary) |
| · | `check_T_w_trace_denner_sirlin_total_mw_sigma_positive` | theorem | `P_w_trace_denner_sirlin_counterterm_functional` | (no summary) |

## `apf/w_trace_denner_sirlin_notation_map.py` — 13 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_w_trace_denner_sirlin_notation_map_bank_closure` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_denner_sirlin_notation_map_combined_clean` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_denner_sirlin_notation_map_ct_maps_standard` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_denner_sirlin_notation_map_delta_r_maps_standard` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_denner_sirlin_notation_map_denner_supports_counterterm` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_denner_sirlin_notation_map_denner_supports_decomposition` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_denner_sirlin_notation_map_locked_no_export` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_denner_sirlin_notation_map_no_physical_export` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_denner_sirlin_notation_map_sirlin_delta_r_present` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_denner_sirlin_notation_map_sirlin_supports_lineage` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_denner_sirlin_notation_map_standard_symbols_complete` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_denner_sirlin_notation_map_status_declared` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_denner_sirlin_notation_map_upstream_candidate_registry_loaded` | theorem | `—` | (no summary) |

## `apf/w_trace_denner_ward_identity_counterterm_import.py` — 73 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_w_trace_ward_import_all_open_block` | theorem | `P_w_trace_denner_ward_identity_counterterm_import` | (no summary) |
| · | `check_T_w_trace_ward_import_bank_closure` | theorem | `P_w_trace_denner_ward_identity_counterterm_import` | (no summary) |
| · | `check_T_w_trace_ward_import_basis_contains_A0` | theorem | `P_w_trace_denner_ward_identity_counterterm_import` | (no summary) |
| · | `check_T_w_trace_ward_import_basis_contains_B0` | theorem | `P_w_trace_denner_ward_identity_counterterm_import` | (no summary) |
| · | `check_T_w_trace_ward_import_basis_has_native_terms` | theorem | `P_w_trace_denner_ward_identity_counterterm_import` | (no summary) |
| · | `check_T_w_trace_ward_import_box_imported` | theorem | `P_w_trace_denner_ward_identity_counterterm_import` | (no summary) |
| · | `check_T_w_trace_ward_import_charge_ct_imported` | theorem | `P_w_trace_denner_ward_identity_counterterm_import` | (no summary) |
| · | `check_T_w_trace_ward_import_coverage_families` | theorem | `P_w_trace_denner_ward_identity_counterterm_import` | (no summary) |
| · | `check_T_w_trace_ward_import_coverage_fraction` | theorem | `P_w_trace_denner_ward_identity_counterterm_import` | (no summary) |
| · | `check_T_w_trace_ward_import_coverage_relations` | theorem | `P_w_trace_denner_ward_identity_counterterm_import` | (no summary) |
| · | `check_T_w_trace_ward_import_delta_alpha_value` | theorem | `P_w_trace_denner_ward_identity_counterterm_import` | (no summary) |
| · | `check_T_w_trace_ward_import_dependencies_pass` | theorem | `P_w_trace_denner_ward_identity_counterterm_import` | (no summary) |
| · | `check_T_w_trace_ward_import_dizet_total_preserved` | theorem | `P_w_trace_denner_ward_identity_counterterm_import` | (no summary) |
| · | `check_T_w_trace_ward_import_evaluated_family_count` | theorem | `P_w_trace_denner_ward_identity_counterterm_import` | (no summary) |
| · | `check_T_w_trace_ward_import_evaluated_relation_count` | theorem | `P_w_trace_denner_ward_identity_counterterm_import` | (no summary) |
| · | `check_T_w_trace_ward_import_family_count` | theorem | `P_w_trace_denner_ward_identity_counterterm_import` | (no summary) |
| · | `check_T_w_trace_ward_import_field_aa_imported` | theorem | `P_w_trace_denner_ward_identity_counterterm_import` | (no summary) |
| · | `check_T_w_trace_ward_import_field_za_imported` | theorem | `P_w_trace_denner_ward_identity_counterterm_import` | (no summary) |
| · | `check_T_w_trace_ward_import_first_failed_gate_exact` | theorem | `P_w_trace_denner_ward_identity_counterterm_import` | (no summary) |
| · | `check_T_w_trace_ward_import_forbidden_claims_present` | theorem | `P_w_trace_denner_ward_identity_counterterm_import` | (no summary) |
| · | `check_T_w_trace_ward_import_forbids_full_closure` | theorem | `P_w_trace_denner_ward_identity_counterterm_import` | (no summary) |
| · | `check_T_w_trace_ward_import_forbids_target_derivation` | theorem | `P_w_trace_denner_ward_identity_counterterm_import` | (no summary) |
| · | `check_T_w_trace_ward_import_frontier_count` | theorem | `P_w_trace_denner_ward_identity_counterterm_import` | (no summary) |
| · | `check_T_w_trace_ward_import_frontier_next_steps_nonempty` | theorem | `P_w_trace_denner_ward_identity_counterterm_import` | (no summary) |
| · | `check_T_w_trace_ward_import_frontier_relations_closed` | theorem | `P_w_trace_denner_ward_identity_counterterm_import` | (no summary) |
| · | `check_T_w_trace_ward_import_frontier_rows_closed` | theorem | `P_w_trace_denner_ward_identity_counterterm_import` | (no summary) |
| · | `check_T_w_trace_ward_import_gate_count` | theorem | `P_w_trace_denner_ward_identity_counterterm_import` | (no summary) |
| · | `check_T_w_trace_ward_import_gate_no_fit_guard` | theorem | `P_w_trace_denner_ward_identity_counterterm_import` | (no summary) |
| · | `check_T_w_trace_ward_import_gate_relation_dag_closed` | theorem | `P_w_trace_denner_ward_identity_counterterm_import` | (no summary) |
| · | `check_T_w_trace_ward_import_gate_relation_import_closed` | theorem | `P_w_trace_denner_ward_identity_counterterm_import` | (no summary) |
| · | `check_T_w_trace_ward_import_gate_target_localized` | theorem | `P_w_trace_denner_ward_identity_counterterm_import` | (no summary) |
| · | `check_T_w_trace_ward_import_gauge_imported` | theorem | `P_w_trace_denner_ward_identity_counterterm_import` | (no summary) |
| · | `check_T_w_trace_ward_import_mass_ct_w_imported` | theorem | `P_w_trace_denner_ward_identity_counterterm_import` | (no summary) |
| · | `check_T_w_trace_ward_import_mass_ct_z_imported` | theorem | `P_w_trace_denner_ward_identity_counterterm_import` | (no summary) |
| · | `check_T_w_trace_ward_import_mw_preserved` | theorem | `P_w_trace_denner_ward_identity_counterterm_import` | (no summary) |
| · | `check_T_w_trace_ward_import_native_gap_equals_target` | theorem | `P_w_trace_denner_ward_identity_counterterm_import` | (no summary) |
| · | `check_T_w_trace_ward_import_native_partial_matches_v19` | theorem | `P_w_trace_denner_ward_identity_counterterm_import` | (no summary) |
| · | `check_T_w_trace_ward_import_native_partial_range` | theorem | `P_w_trace_denner_ward_identity_counterterm_import` | (no summary) |
| · | `check_T_w_trace_ward_import_native_status_partial` | theorem | `P_w_trace_denner_ward_identity_counterterm_import` | (no summary) |
| · | `check_T_w_trace_ward_import_next_gate_exact` | theorem | `P_w_trace_denner_ward_identity_counterterm_import` | (no summary) |
| · | `check_T_w_trace_ward_import_no_fit_admitted` | theorem | `P_w_trace_denner_ward_identity_counterterm_import` | (no summary) |
| · | `check_T_w_trace_ward_import_no_orphan_relations` | theorem | `P_w_trace_denner_ward_identity_counterterm_import` | (no summary) |
| · | `check_T_w_trace_ward_import_open_gates_block` | theorem | `P_w_trace_denner_ward_identity_counterterm_import` | (no summary) |
| · | `check_T_w_trace_ward_import_open_numeric_family_count` | theorem | `P_w_trace_denner_ward_identity_counterterm_import` | (no summary) |
| · | `check_T_w_trace_ward_import_payload_digest_present` | theorem | `P_w_trace_denner_ward_identity_counterterm_import` | (no summary) |
| · | `check_T_w_trace_ward_import_pull_preserved` | theorem | `P_w_trace_denner_ward_identity_counterterm_import` | (no summary) |
| · | `check_T_w_trace_ward_import_relation_count` | theorem | `P_w_trace_denner_ward_identity_counterterm_import` | (no summary) |
| · | `check_T_w_trace_ward_import_relation_dag_references_exist` | theorem | `P_w_trace_denner_ward_identity_counterterm_import` | (no summary) |
| · | `check_T_w_trace_ward_import_relation_dependencies_nonempty` | theorem | `P_w_trace_denner_ward_identity_counterterm_import` | (no summary) |
| · | `check_T_w_trace_ward_import_relation_inputs_nonempty` | theorem | `P_w_trace_denner_ward_identity_counterterm_import` | (no summary) |
| · | `check_T_w_trace_ward_import_relation_outputs_nonempty` | theorem | `P_w_trace_denner_ward_identity_counterterm_import` | (no summary) |
| · | `check_T_w_trace_ward_import_rho_value` | theorem | `P_w_trace_denner_ward_identity_counterterm_import` | (no summary) |
| · | `check_T_w_trace_ward_import_route_status_export_candidate` | theorem | `P_w_trace_denner_ward_identity_counterterm_import` | (no summary) |
| · | `check_T_w_trace_ward_import_safe_claims_present` | theorem | `P_w_trace_denner_ward_identity_counterterm_import` | (no summary) |
| · | `check_T_w_trace_ward_import_status_declared` | theorem | `P_w_trace_denner_ward_identity_counterterm_import` | (no summary) |
| · | `check_T_w_trace_ward_import_summary_has_families` | theorem | `P_w_trace_denner_ward_identity_counterterm_import` | (no summary) |
| · | `check_T_w_trace_ward_import_summary_has_frontier` | theorem | `P_w_trace_denner_ward_identity_counterterm_import` | (no summary) |
| · | `check_T_w_trace_ward_import_summary_has_graph` | theorem | `P_w_trace_denner_ward_identity_counterterm_import` | (no summary) |
| · | `check_T_w_trace_ward_import_summary_has_relations` | theorem | `P_w_trace_denner_ward_identity_counterterm_import` | (no summary) |
| · | `check_T_w_trace_ward_import_target_blocks_full` | theorem | `P_w_trace_denner_ward_identity_counterterm_import` | (no summary) |
| · | `check_T_w_trace_ward_import_target_closure_zero` | theorem | `P_w_trace_denner_ward_identity_counterterm_import` | (no summary) |
| · | `check_T_w_trace_ward_import_target_family_count` | theorem | `P_w_trace_denner_ward_identity_counterterm_import` | (no summary) |
| · | `check_T_w_trace_ward_import_target_not_admitted_formula` | theorem | `P_w_trace_denner_ward_identity_counterterm_import` | (no summary) |
| · | `check_T_w_trace_ward_import_target_range` | theorem | `P_w_trace_denner_ward_identity_counterterm_import` | (no summary) |
| · | `check_T_w_trace_ward_import_terminal_report_status` | theorem | `P_w_trace_denner_ward_identity_counterterm_import` | (no summary) |
| · | `check_T_w_trace_ward_import_unique_families` | theorem | `P_w_trace_denner_ward_identity_counterterm_import` | (no summary) |
| · | `check_T_w_trace_ward_import_unique_gates` | theorem | `P_w_trace_denner_ward_identity_counterterm_import` | (no summary) |
| · | `check_T_w_trace_ward_import_unique_relations` | theorem | `P_w_trace_denner_ward_identity_counterterm_import` | (no summary) |
| · | `check_T_w_trace_ward_import_v19_gates_available` | theorem | `P_w_trace_denner_ward_identity_counterterm_import` | (no summary) |
| · | `check_T_w_trace_ward_import_v19_missing_available` | theorem | `P_w_trace_denner_ward_identity_counterterm_import` | (no summary) |
| · | `check_T_w_trace_ward_import_v19_rows_available` | theorem | `P_w_trace_denner_ward_identity_counterterm_import` | (no summary) |
| · | `check_T_w_trace_ward_import_vertex_imported` | theorem | `P_w_trace_denner_ward_identity_counterterm_import` | (no summary) |
| · | `check_T_w_trace_ward_import_weak_angle_imported` | theorem | `P_w_trace_denner_ward_identity_counterterm_import` | (no summary) |

## `apf/w_trace_diagram_family_numeric_evaluator_import.py` — 79 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_w_trace_family_numeric_admitted_count` | theorem | `P_w_trace_diagram_family_numeric_evaluator_import` | (no summary) |
| · | `check_T_w_trace_family_numeric_anchor_count` | theorem | `P_w_trace_diagram_family_numeric_evaluator_import` | (no summary) |
| · | `check_T_w_trace_family_numeric_anchor_ids_unique` | theorem | `P_w_trace_diagram_family_numeric_evaluator_import` | (no summary) |
| · | `check_T_w_trace_family_numeric_anchors_map_to_known_families` | theorem | `P_w_trace_diagram_family_numeric_evaluator_import` | (no summary) |
| · | `check_T_w_trace_family_numeric_bank_closure` | theorem | `P_w_trace_diagram_family_numeric_evaluator_import` | (no summary) |
| · | `check_T_w_trace_family_numeric_box_present` | theorem | `P_w_trace_diagram_family_numeric_evaluator_import` | (no summary) |
| · | `check_T_w_trace_family_numeric_charge_present` | theorem | `P_w_trace_diagram_family_numeric_evaluator_import` | (no summary) |
| · | `check_T_w_trace_family_numeric_coverage_anchors_total` | theorem | `P_w_trace_diagram_family_numeric_evaluator_import` | (no summary) |
| · | `check_T_w_trace_family_numeric_coverage_family_total` | theorem | `P_w_trace_diagram_family_numeric_evaluator_import` | (no summary) |
| · | `check_T_w_trace_family_numeric_coverage_tasks_total` | theorem | `P_w_trace_diagram_family_numeric_evaluator_import` | (no summary) |
| · | `check_T_w_trace_family_numeric_delta_alpha_family_present` | theorem | `P_w_trace_diagram_family_numeric_evaluator_import` | (no summary) |
| · | `check_T_w_trace_family_numeric_delta_alpha_value` | theorem | `P_w_trace_diagram_family_numeric_evaluator_import` | (no summary) |
| · | `check_T_w_trace_family_numeric_dependency_pv_pass` | theorem | `P_w_trace_diagram_family_numeric_evaluator_import` | (no summary) |
| · | `check_T_w_trace_family_numeric_dependency_tensor_pass` | theorem | `P_w_trace_diagram_family_numeric_evaluator_import` | (no summary) |
| · | `check_T_w_trace_family_numeric_dependency_v20_pass` | theorem | `P_w_trace_diagram_family_numeric_evaluator_import` | (no summary) |
| · | `check_T_w_trace_family_numeric_diagnostic_count` | theorem | `P_w_trace_diagram_family_numeric_evaluator_import` | (no summary) |
| · | `check_T_w_trace_family_numeric_diagnostic_not_native` | theorem | `P_w_trace_diagram_family_numeric_evaluator_import` | (no summary) |
| · | `check_T_w_trace_family_numeric_dizet_delta_alpha_anchor` | theorem | `P_w_trace_diagram_family_numeric_evaluator_import` | (no summary) |
| · | `check_T_w_trace_family_numeric_dizet_internal_total_close` | theorem | `P_w_trace_diagram_family_numeric_evaluator_import` | (no summary) |
| · | `check_T_w_trace_family_numeric_dr1bos_reasonable` | theorem | `P_w_trace_diagram_family_numeric_evaluator_import` | (no summary) |
| · | `check_T_w_trace_family_numeric_dr1ferm_reasonable` | theorem | `P_w_trace_diagram_family_numeric_evaluator_import` | (no summary) |
| · | `check_T_w_trace_family_numeric_drrem_positive` | theorem | `P_w_trace_diagram_family_numeric_evaluator_import` | (no summary) |
| · | `check_T_w_trace_family_numeric_export_mw_preserved` | theorem | `P_w_trace_diagram_family_numeric_evaluator_import` | (no summary) |
| · | `check_T_w_trace_family_numeric_export_residual_preserved` | theorem | `P_w_trace_diagram_family_numeric_evaluator_import` | (no summary) |
| · | `check_T_w_trace_family_numeric_family_count` | theorem | `P_w_trace_diagram_family_numeric_evaluator_import` | (no summary) |
| · | `check_T_w_trace_family_numeric_family_ids_unique` | theorem | `P_w_trace_diagram_family_numeric_evaluator_import` | (no summary) |
| · | `check_T_w_trace_family_numeric_finite_remainder_present` | theorem | `P_w_trace_diagram_family_numeric_evaluator_import` | (no summary) |
| · | `check_T_w_trace_family_numeric_finite_target_range` | theorem | `P_w_trace_diagram_family_numeric_evaluator_import` | (no summary) |
| · | `check_T_w_trace_family_numeric_first_failed_gate_exact` | theorem | `P_w_trace_diagram_family_numeric_evaluator_import` | (no summary) |
| · | `check_T_w_trace_family_numeric_forbidden_claims_count` | theorem | `P_w_trace_diagram_family_numeric_evaluator_import` | (no summary) |
| · | `check_T_w_trace_family_numeric_forbidden_drrem` | theorem | `P_w_trace_diagram_family_numeric_evaluator_import` | (no summary) |
| · | `check_T_w_trace_family_numeric_forbidden_full` | theorem | `P_w_trace_diagram_family_numeric_evaluator_import` | (no summary) |
| · | `check_T_w_trace_family_numeric_full_closure` | theorem | `P_w_trace_diagram_family_numeric_evaluator_import` | (no summary) |
| · | `check_T_w_trace_family_numeric_gate_closed_count` | theorem | `P_w_trace_diagram_family_numeric_evaluator_import` | (no summary) |
| · | `check_T_w_trace_family_numeric_gate_count` | theorem | `P_w_trace_diagram_family_numeric_evaluator_import` | (no summary) |
| · | `check_T_w_trace_family_numeric_gate_ids_unique` | theorem | `P_w_trace_diagram_family_numeric_evaluator_import` | (no summary) |
| · | `check_T_w_trace_family_numeric_gate_no_fit_closed` | theorem | `P_w_trace_diagram_family_numeric_evaluator_import` | (no summary) |
| · | `check_T_w_trace_family_numeric_gate_open_count` | theorem | `P_w_trace_diagram_family_numeric_evaluator_import` | (no summary) |
| · | `check_T_w_trace_family_numeric_gauge_present` | theorem | `P_w_trace_diagram_family_numeric_evaluator_import` | (no summary) |
| · | `check_T_w_trace_family_numeric_native_partial` | theorem | `P_w_trace_diagram_family_numeric_evaluator_import` | (no summary) |
| · | `check_T_w_trace_family_numeric_native_partial_matches_v20` | theorem | `P_w_trace_diagram_family_numeric_evaluator_import` | (no summary) |
| · | `check_T_w_trace_family_numeric_native_status_partial` | theorem | `P_w_trace_diagram_family_numeric_evaluator_import` | (no summary) |
| · | `check_T_w_trace_family_numeric_newdr_nonzero` | theorem | `P_w_trace_diagram_family_numeric_evaluator_import` | (no summary) |
| · | `check_T_w_trace_family_numeric_next_gate_exact` | theorem | `P_w_trace_diagram_family_numeric_evaluator_import` | (no summary) |
| · | `check_T_w_trace_family_numeric_no_fit_not_admitted` | theorem | `P_w_trace_diagram_family_numeric_evaluator_import` | (no summary) |
| · | `check_T_w_trace_family_numeric_open_count` | theorem | `P_w_trace_diagram_family_numeric_evaluator_import` | (no summary) |
| · | `check_T_w_trace_family_numeric_open_families_block` | theorem | `P_w_trace_diagram_family_numeric_evaluator_import` | (no summary) |
| · | `check_T_w_trace_family_numeric_open_gates_block` | theorem | `P_w_trace_diagram_family_numeric_evaluator_import` | (no summary) |
| · | `check_T_w_trace_family_numeric_pass_status` | theorem | `P_w_trace_diagram_family_numeric_evaluator_import` | (no summary) |
| · | `check_T_w_trace_family_numeric_payload_id` | theorem | `P_w_trace_diagram_family_numeric_evaluator_import` | (no summary) |
| · | `check_T_w_trace_family_numeric_pull_preserved` | theorem | `P_w_trace_diagram_family_numeric_evaluator_import` | (no summary) |
| · | `check_T_w_trace_family_numeric_qcd_aux_nonzero` | theorem | `P_w_trace_diagram_family_numeric_evaluator_import` | (no summary) |
| · | `check_T_w_trace_family_numeric_quarantined_block` | theorem | `P_w_trace_diagram_family_numeric_evaluator_import` | (no summary) |
| · | `check_T_w_trace_family_numeric_quarantined_count` | theorem | `P_w_trace_diagram_family_numeric_evaluator_import` | (no summary) |
| · | `check_T_w_trace_family_numeric_report_has_anchors` | theorem | `P_w_trace_diagram_family_numeric_evaluator_import` | (no summary) |
| · | `check_T_w_trace_family_numeric_report_has_digest` | theorem | `P_w_trace_diagram_family_numeric_evaluator_import` | (no summary) |
| · | `check_T_w_trace_family_numeric_report_has_families` | theorem | `P_w_trace_diagram_family_numeric_evaluator_import` | (no summary) |
| · | `check_T_w_trace_family_numeric_report_has_gates` | theorem | `P_w_trace_diagram_family_numeric_evaluator_import` | (no summary) |
| · | `check_T_w_trace_family_numeric_report_has_tasks` | theorem | `P_w_trace_diagram_family_numeric_evaluator_import` | (no summary) |
| · | `check_T_w_trace_family_numeric_rho_cross_target_range` | theorem | `P_w_trace_diagram_family_numeric_evaluator_import` | (no summary) |
| · | `check_T_w_trace_family_numeric_rho_family_present` | theorem | `P_w_trace_diagram_family_numeric_evaluator_import` | (no summary) |
| · | `check_T_w_trace_family_numeric_rho_resummation_family_present` | theorem | `P_w_trace_diagram_family_numeric_evaluator_import` | (no summary) |
| · | `check_T_w_trace_family_numeric_rho_resummation_negative` | theorem | `P_w_trace_diagram_family_numeric_evaluator_import` | (no summary) |
| · | `check_T_w_trace_family_numeric_rho_value` | theorem | `P_w_trace_diagram_family_numeric_evaluator_import` | (no summary) |
| · | `check_T_w_trace_family_numeric_route_status_export_candidate` | theorem | `P_w_trace_diagram_family_numeric_evaluator_import` | (no summary) |
| · | `check_T_w_trace_family_numeric_safe_claims_count` | theorem | `P_w_trace_diagram_family_numeric_evaluator_import` | (no summary) |
| · | `check_T_w_trace_family_numeric_self_energy_present` | theorem | `P_w_trace_diagram_family_numeric_evaluator_import` | (no summary) |
| · | `check_T_w_trace_family_numeric_sigma_preserved` | theorem | `P_w_trace_diagram_family_numeric_evaluator_import` | (no summary) |
| · | `check_T_w_trace_family_numeric_status_strings` | theorem | `P_w_trace_diagram_family_numeric_evaluator_import` | (no summary) |
| · | `check_T_w_trace_family_numeric_target_decomposition` | theorem | `P_w_trace_diagram_family_numeric_evaluator_import` | (no summary) |
| · | `check_T_w_trace_family_numeric_target_not_formula` | theorem | `P_w_trace_diagram_family_numeric_evaluator_import` | (no summary) |
| · | `check_T_w_trace_family_numeric_task_count` | theorem | `P_w_trace_diagram_family_numeric_evaluator_import` | (no summary) |
| · | `check_T_w_trace_family_numeric_task_ids_unique` | theorem | `P_w_trace_diagram_family_numeric_evaluator_import` | (no summary) |
| · | `check_T_w_trace_family_numeric_tasks_have_formulae` | theorem | `P_w_trace_diagram_family_numeric_evaluator_import` | (no summary) |
| · | `check_T_w_trace_family_numeric_tasks_have_integrals` | theorem | `P_w_trace_diagram_family_numeric_evaluator_import` | (no summary) |
| · | `check_T_w_trace_family_numeric_tasks_have_next_action` | theorem | `P_w_trace_diagram_family_numeric_evaluator_import` | (no summary) |
| · | `check_T_w_trace_family_numeric_tasks_map_to_known_families` | theorem | `P_w_trace_diagram_family_numeric_evaluator_import` | (no summary) |
| · | `check_T_w_trace_family_numeric_version` | theorem | `P_w_trace_diagram_family_numeric_evaluator_import` | (no summary) |
| · | `check_T_w_trace_family_numeric_vertex_present` | theorem | `P_w_trace_diagram_family_numeric_evaluator_import` | (no summary) |

## `apf/w_trace_dizet_acquisition_instrumentation.py` — 36 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_w_trace_dizet_acquisition_acquisition_first_failed_gate_named` | theorem | `P_w_trace_dizet_acquisition_instrumentation` | (no summary) |
| · | `check_T_w_trace_dizet_acquisition_apf_input_deck_has_required_fields` | theorem | `P_w_trace_dizet_acquisition_instrumentation` | (no summary) |
| · | `check_T_w_trace_dizet_acquisition_apf_trace_not_input` | theorem | `P_w_trace_dizet_acquisition_instrumentation` | (no summary) |
| · | `check_T_w_trace_dizet_acquisition_bank_closure` | theorem | `P_w_trace_dizet_acquisition_instrumentation` | (no summary) |
| · | `check_T_w_trace_dizet_acquisition_capabilities_nonempty` | theorem | `P_w_trace_dizet_acquisition_instrumentation` | (no summary) |
| · | `check_T_w_trace_dizet_acquisition_channels_unique` | theorem | `P_w_trace_dizet_acquisition_instrumentation` | (no summary) |
| · | `check_T_w_trace_dizet_acquisition_claim_boundary_allowed` | theorem | `P_w_trace_dizet_acquisition_instrumentation` | (no summary) |
| · | `check_T_w_trace_dizet_acquisition_code_ocean_channel_recorded` | theorem | `P_w_trace_dizet_acquisition_instrumentation` | (no summary) |
| · | `check_T_w_trace_dizet_acquisition_cpc_channel_is_primary` | theorem | `P_w_trace_dizet_acquisition_instrumentation` | (no summary) |
| · | `check_T_w_trace_dizet_acquisition_default_flags_captured` | theorem | `P_w_trace_dizet_acquisition_instrumentation` | (no summary) |
| · | `check_T_w_trace_dizet_acquisition_depends_on_v158` | theorem | `P_w_trace_dizet_acquisition_instrumentation` | (no summary) |
| · | `check_T_w_trace_dizet_acquisition_flag_mapping_uses_dizet_names` | theorem | `P_w_trace_dizet_acquisition_instrumentation` | (no summary) |
| · | `check_T_w_trace_dizet_acquisition_instrumentation_produces_export_conditions` | theorem | `P_w_trace_dizet_acquisition_instrumentation` | (no summary) |
| · | `check_T_w_trace_dizet_acquisition_instrumentation_steps_complete` | theorem | `P_w_trace_dizet_acquisition_instrumentation` | (no summary) |
| · | `check_T_w_trace_dizet_acquisition_license_terms_not_ignored` | theorem | `P_w_trace_dizet_acquisition_instrumentation` | (no summary) |
| · | `check_T_w_trace_dizet_acquisition_mw_roundtrip_preserved` | theorem | `P_w_trace_dizet_acquisition_instrumentation` | (no summary) |
| · | `check_T_w_trace_dizet_acquisition_no_dizet_run_claim` | theorem | `P_w_trace_dizet_acquisition_instrumentation` | (no summary) |
| · | `check_T_w_trace_dizet_acquisition_no_local_vendor_claim` | theorem | `P_w_trace_dizet_acquisition_instrumentation` | (no summary) |
| · | `check_T_w_trace_dizet_acquisition_numerics_preserved` | theorem | `P_w_trace_dizet_acquisition_instrumentation` | (no summary) |
| · | `check_T_w_trace_dizet_acquisition_old_gate_split` | theorem | `P_w_trace_dizet_acquisition_instrumentation` | (no summary) |
| · | `check_T_w_trace_dizet_acquisition_payload_digest_present` | theorem | `P_w_trace_dizet_acquisition_instrumentation` | (no summary) |
| · | `check_T_w_trace_dizet_acquisition_physical_export_locked` | theorem | `P_w_trace_dizet_acquisition_instrumentation` | {'physical_W_export_enabled': False, 'exports_physical_M_W': False, 'first_failed_gate_after_v15_9': 'DIZET_CODE_NOT_YET_ACQUIRED_COMPILED_AND_RUN'} |
| · | `check_T_w_trace_dizet_acquisition_report_contains_all_tables` | theorem | `P_w_trace_dizet_acquisition_instrumentation` | (no summary) |
| · | `check_T_w_trace_dizet_acquisition_route_status_named` | theorem | `P_w_trace_dizet_acquisition_instrumentation` | (no summary) |
| · | `check_T_w_trace_dizet_acquisition_row_covariance_still_open` | theorem | `P_w_trace_dizet_acquisition_instrumentation` | (no summary) |
| · | `check_T_w_trace_dizet_acquisition_same_input_total_gate_located` | theorem | `P_w_trace_dizet_acquisition_instrumentation` | {'reviewed_total_evaluator_source_path_located': True, 'compiled_dizet_available_in_repo': False} |
| · | `check_T_w_trace_dizet_acquisition_sanc_tarball_channel_recorded` | theorem | `P_w_trace_dizet_acquisition_instrumentation` | (no summary) |
| · | `check_T_w_trace_dizet_acquisition_sensitivity_negative` | theorem | `P_w_trace_dizet_acquisition_instrumentation` | (no summary) |
| · | `check_T_w_trace_dizet_acquisition_source_channels_located` | theorem | `P_w_trace_dizet_acquisition_instrumentation` | (no summary) |
| · | `check_T_w_trace_dizet_acquisition_split_gate_status_exact` | theorem | `P_w_trace_dizet_acquisition_instrumentation` | (no summary) |
| · | `check_T_w_trace_dizet_acquisition_status_declared` | theorem | `P_w_trace_dizet_acquisition_instrumentation` | (no summary) |
| · | `check_T_w_trace_dizet_acquisition_steps_ordered` | theorem | `P_w_trace_dizet_acquisition_instrumentation` | (no summary) |
| · | `check_T_w_trace_dizet_acquisition_terminal_verdict_exact` | theorem | `P_w_trace_dizet_acquisition_instrumentation` | (no summary) |
| · | `check_T_w_trace_dizet_acquisition_toggle_plan_has_core_buckets` | theorem | `P_w_trace_dizet_acquisition_instrumentation` | (no summary) |
| · | `check_T_w_trace_dizet_acquisition_toggle_rows_not_export_admitted` | theorem | `P_w_trace_dizet_acquisition_instrumentation` | (no summary) |
| · | `check_T_w_trace_dizet_acquisition_wmass_zero_prediction_mode` | theorem | `P_w_trace_dizet_acquisition_instrumentation` | (no summary) |

## `apf/w_trace_dizet_executable_run.py` — 34 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_w_trace_dizet_executable_apf_inputs_non_w_only` | theorem | `P_w_trace_dizet_executable_run` | (no summary) |
| · | `check_T_w_trace_dizet_executable_apf_trace_not_consumed` | theorem | `P_w_trace_dizet_executable_run` | (no summary) |
| · | `check_T_w_trace_dizet_executable_archive_hash_recorded` | theorem | `P_w_trace_dizet_executable_run` | (no summary) |
| · | `check_T_w_trace_dizet_executable_bank_closure` | theorem | `P_w_trace_dizet_executable_run` | (no summary) |
| · | `check_T_w_trace_dizet_executable_baseline_delta_r_inverted_recorded` | theorem | `P_w_trace_dizet_executable_run` | (no summary) |
| · | `check_T_w_trace_dizet_executable_baseline_mw_recorded` | theorem | `P_w_trace_dizet_executable_run` | (no summary) |
| · | `check_T_w_trace_dizet_executable_benchmarks_declared` | theorem | `P_w_trace_dizet_executable_run` | (no summary) |
| · | `check_T_w_trace_dizet_executable_comparison_to_apf_recorded` | theorem | `P_w_trace_dizet_executable_run` | (no summary) |
| · | `check_T_w_trace_dizet_executable_convention_toggles_present` | theorem | `P_w_trace_dizet_executable_run` | (no summary) |
| · | `check_T_w_trace_dizet_executable_delta_alpha_output_recorded` | theorem | `P_w_trace_dizet_executable_run` | (no summary) |
| · | `check_T_w_trace_dizet_executable_depends_on_v159` | theorem | `P_w_trace_dizet_executable_run` | (no summary) |
| · | `check_T_w_trace_dizet_executable_dizet_dr_distinguished_from_inverted_dr` | theorem | `P_w_trace_dizet_executable_run` | (no summary) |
| · | `check_T_w_trace_dizet_executable_dmw_ddr_negative` | theorem | `P_w_trace_dizet_executable_run` | (no summary) |
| · | `check_T_w_trace_dizet_executable_first_failed_gate_named` | theorem | `P_w_trace_dizet_executable_run` | (no summary) |
| · | `check_T_w_trace_dizet_executable_iamt5_distinct_mw` | theorem | `P_w_trace_dizet_executable_run` | (no summary) |
| · | `check_T_w_trace_dizet_executable_iamt6_same_mw_as_iamt8` | theorem | `P_w_trace_dizet_executable_run` | (no summary) |
| · | `check_T_w_trace_dizet_executable_iamt_toggles_present` | theorem | `P_w_trace_dizet_executable_run` | (no summary) |
| · | `check_T_w_trace_dizet_executable_idmww_affects_mw_not_zpard_dr` | theorem | `P_w_trace_dizet_executable_run` | (no summary) |
| · | `check_T_w_trace_dizet_executable_ihvp_toggles_present` | theorem | `P_w_trace_dizet_executable_run` | (no summary) |
| · | `check_T_w_trace_dizet_executable_iqcd_affects_zpard_not_mw_here` | theorem | `P_w_trace_dizet_executable_run` | (no summary) |
| · | `check_T_w_trace_dizet_executable_payload_digest_present` | theorem | `P_w_trace_dizet_executable_run` | (no summary) |
| · | `check_T_w_trace_dizet_executable_physical_export_locked` | theorem | `P_w_trace_dizet_executable_run` | (no summary) |
| · | `check_T_w_trace_dizet_executable_preferred_flags_used` | theorem | `P_w_trace_dizet_executable_run` | (no summary) |
| · | `check_T_w_trace_dizet_executable_pull_computed` | theorem | `P_w_trace_dizet_executable_run` | (no summary) |
| · | `check_T_w_trace_dizet_executable_qcd_toggles_present` | theorem | `P_w_trace_dizet_executable_run` | (no summary) |
| · | `check_T_w_trace_dizet_executable_report_contains_rows` | theorem | `P_w_trace_dizet_executable_run` | (no summary) |
| · | `check_T_w_trace_dizet_executable_row_covariance_gate_open` | theorem | `P_w_trace_dizet_executable_run` | (no summary) |
| · | `check_T_w_trace_dizet_executable_same_input_total_gate_closed` | theorem | `P_w_trace_dizet_executable_run` | (no summary) |
| · | `check_T_w_trace_dizet_executable_status_declared` | theorem | `P_w_trace_dizet_executable_run` | (no summary) |
| · | `check_T_w_trace_dizet_executable_sw2_matches_mass_ratio` | theorem | `P_w_trace_dizet_executable_run` | (no summary) |
| · | `check_T_w_trace_dizet_executable_terminal_verdict_exact` | theorem | `P_w_trace_dizet_executable_run` | (no summary) |
| · | `check_T_w_trace_dizet_executable_theory_toggle_plus_minus` | theorem | `P_w_trace_dizet_executable_run` | (no summary) |
| · | `check_T_w_trace_dizet_executable_toggle_rows_not_admitted` | theorem | `P_w_trace_dizet_executable_run` | (no summary) |
| · | `check_T_w_trace_dizet_executable_toolchain_declared` | theorem | `P_w_trace_dizet_executable_run` | (no summary) |

## `apf/w_trace_dizet_flag_sensitivity_covariance.py` — 32 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_w_trace_dizet_flag_sensitivity_all_responses_unadmitted` | theorem | `P_w_trace_dizet_flag_sensitivity_covariance` | (no summary) |
| · | `check_T_w_trace_dizet_flag_sensitivity_alpha_s_small_input_uncertainty` | theorem | `P_w_trace_dizet_flag_sensitivity_covariance` | (no summary) |
| · | `check_T_w_trace_dizet_flag_sensitivity_apf_dizet_residual_preserved` | theorem | `P_w_trace_dizet_flag_sensitivity_covariance` | (no summary) |
| · | `check_T_w_trace_dizet_flag_sensitivity_apf_not_input` | theorem | `P_w_trace_dizet_flag_sensitivity_covariance` | (no summary) |
| · | `check_T_w_trace_dizet_flag_sensitivity_bank_closure` | theorem | `P_w_trace_dizet_flag_sensitivity_covariance` | (no summary) |
| · | `check_T_w_trace_dizet_flag_sensitivity_baseline_consistent` | theorem | `P_w_trace_dizet_flag_sensitivity_covariance` | (no summary) |
| · | `check_T_w_trace_dizet_flag_sensitivity_blocker_sharpened` | theorem | `P_w_trace_dizet_flag_sensitivity_covariance` | (no summary) |
| · | `check_T_w_trace_dizet_flag_sensitivity_conventions_do_not_move_mw` | theorem | `P_w_trace_dizet_flag_sensitivity_covariance` | (no summary) |
| · | `check_T_w_trace_dizet_flag_sensitivity_covariance_positive` | theorem | `P_w_trace_dizet_flag_sensitivity_covariance` | (no summary) |
| · | `check_T_w_trace_dizet_flag_sensitivity_delta_alpha_derivative_large` | theorem | `P_w_trace_dizet_flag_sensitivity_covariance` | (no summary) |
| · | `check_T_w_trace_dizet_flag_sensitivity_depends_on_v161` | theorem | `P_w_trace_dizet_flag_sensitivity_covariance` | (no summary) |
| · | `check_T_w_trace_dizet_flag_sensitivity_derivatives_present` | theorem | `P_w_trace_dizet_flag_sensitivity_covariance` | (no summary) |
| · | `check_T_w_trace_dizet_flag_sensitivity_forbidden_claim_named` | theorem | `P_w_trace_dizet_flag_sensitivity_covariance` | (no summary) |
| · | `check_T_w_trace_dizet_flag_sensitivity_gate_split_preserved` | theorem | `P_w_trace_dizet_flag_sensitivity_covariance` | (no summary) |
| · | `check_T_w_trace_dizet_flag_sensitivity_higgs_small_input_uncertainty` | theorem | `P_w_trace_dizet_flag_sensitivity_covariance` | (no summary) |
| · | `check_T_w_trace_dizet_flag_sensitivity_iamt0_knockout_large` | theorem | `P_w_trace_dizet_flag_sensitivity_covariance` | (no summary) |
| · | `check_T_w_trace_dizet_flag_sensitivity_iamt5_small_but_nonzero` | theorem | `P_w_trace_dizet_flag_sensitivity_covariance` | (no summary) |
| · | `check_T_w_trace_dizet_flag_sensitivity_iamt6_equivalent_for_mw` | theorem | `P_w_trace_dizet_flag_sensitivity_covariance` | (no summary) |
| · | `check_T_w_trace_dizet_flag_sensitivity_ihvp2016_submev` | theorem | `P_w_trace_dizet_flag_sensitivity_covariance` | (no summary) |
| · | `check_T_w_trace_dizet_flag_sensitivity_iqcd0_dr_only` | theorem | `P_w_trace_dizet_flag_sensitivity_covariance` | (no summary) |
| · | `check_T_w_trace_dizet_flag_sensitivity_mt_input_uncertainty_nontrivial` | theorem | `P_w_trace_dizet_flag_sensitivity_covariance` | (no summary) |
| · | `check_T_w_trace_dizet_flag_sensitivity_mz_dominates_inputs` | theorem | `P_w_trace_dizet_flag_sensitivity_covariance` | (no summary) |
| · | `check_T_w_trace_dizet_flag_sensitivity_payload_digest_present` | theorem | `P_w_trace_dizet_flag_sensitivity_covariance` | (no summary) |
| · | `check_T_w_trace_dizet_flag_sensitivity_physical_export_locked` | theorem | `P_w_trace_dizet_flag_sensitivity_covariance` | (no summary) |
| · | `check_T_w_trace_dizet_flag_sensitivity_pull_reduced_by_covariance` | theorem | `P_w_trace_dizet_flag_sensitivity_covariance` | (no summary) |
| · | `check_T_w_trace_dizet_flag_sensitivity_report_contains_scan` | theorem | `P_w_trace_dizet_flag_sensitivity_covariance` | (no summary) |
| · | `check_T_w_trace_dizet_flag_sensitivity_scan_counts_recorded` | theorem | `P_w_trace_dizet_flag_sensitivity_covariance` | (no summary) |
| · | `check_T_w_trace_dizet_flag_sensitivity_status_declared` | theorem | `P_w_trace_dizet_flag_sensitivity_covariance` | (no summary) |
| · | `check_T_w_trace_dizet_flag_sensitivity_terminal_verdict_exact` | theorem | `P_w_trace_dizet_flag_sensitivity_covariance` | (no summary) |
| · | `check_T_w_trace_dizet_flag_sensitivity_theory_toggles_symmetric` | theorem | `P_w_trace_dizet_flag_sensitivity_covariance` | (no summary) |
| · | `check_T_w_trace_dizet_flag_sensitivity_timeout_quarantined` | theorem | `P_w_trace_dizet_flag_sensitivity_covariance` | (no summary) |
| · | `check_T_w_trace_dizet_flag_sensitivity_total_sigma_value` | theorem | `P_w_trace_dizet_flag_sensitivity_covariance` | (no summary) |

## `apf/w_trace_dizet_internal_dr_decomposition.py` — 30 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_w_trace_dizet_internal_dr_apf_deck_not_using_w_trace` | theorem | `P_w_trace_dizet_internal_dr_decomposition` | (no summary) |
| · | `check_T_w_trace_dizet_internal_dr_bank_closure` | theorem | `P_w_trace_dizet_internal_dr_decomposition` | (no summary) |
| · | `check_T_w_trace_dizet_internal_dr_bosonic_kernel_positive` | theorem | `P_w_trace_dizet_internal_dr_decomposition` | (no summary) |
| · | `check_T_w_trace_dizet_internal_dr_claim_boundary_names_forbidden` | theorem | `P_w_trace_dizet_internal_dr_decomposition` | (no summary) |
| · | `check_T_w_trace_dizet_internal_dr_covariance_inherited` | theorem | `P_w_trace_dizet_internal_dr_decomposition` | (no summary) |
| · | `check_T_w_trace_dizet_internal_dr_delta_alpha_near_expected` | theorem | `P_w_trace_dizet_internal_dr_decomposition` | (no summary) |
| · | `check_T_w_trace_dizet_internal_dr_depends_on_v162` | theorem | `P_w_trace_dizet_internal_dr_decomposition` | (no summary) |
| · | `check_T_w_trace_dizet_internal_dr_dr_matches_export` | theorem | `P_w_trace_dizet_internal_dr_decomposition` | (no summary) |
| · | `check_T_w_trace_dizet_internal_dr_drrem_assembly_closes` | theorem | `P_w_trace_dizet_internal_dr_decomposition` | (no summary) |
| · | `check_T_w_trace_dizet_internal_dr_drrem_matches_export` | theorem | `P_w_trace_dizet_internal_dr_decomposition` | (no summary) |
| · | `check_T_w_trace_dizet_internal_dr_equations_all_pass` | theorem | `P_w_trace_dizet_internal_dr_decomposition` | (no summary) |
| · | `check_T_w_trace_dizet_internal_dr_fermionic_proxy_positive` | theorem | `P_w_trace_dizet_internal_dr_decomposition` | (no summary) |
| · | `check_T_w_trace_dizet_internal_dr_first_failed_gate_sharp` | theorem | `P_w_trace_dizet_internal_dr_decomposition` | (no summary) |
| · | `check_T_w_trace_dizet_internal_dr_gate_upgrade` | theorem | `P_w_trace_dizet_internal_dr_decomposition` | (no summary) |
| · | `check_T_w_trace_dizet_internal_dr_has_useful_internal_components` | theorem | `P_w_trace_dizet_internal_dr_decomposition` | (no summary) |
| · | `check_T_w_trace_dizet_internal_dr_newdr_exposed` | theorem | `P_w_trace_dizet_internal_dr_decomposition` | (no summary) |
| · | `check_T_w_trace_dizet_internal_dr_no_internal_rows_admitted` | theorem | `P_w_trace_dizet_internal_dr_decomposition` | (no summary) |
| · | `check_T_w_trace_dizet_internal_dr_payload_digest_present` | theorem | `P_w_trace_dizet_internal_dr_decomposition` | (no summary) |
| · | `check_T_w_trace_dizet_internal_dr_physical_export_locked` | theorem | `P_w_trace_dizet_internal_dr_decomposition` | (no summary) |
| · | `check_T_w_trace_dizet_internal_dr_qcd_nonzero` | theorem | `P_w_trace_dizet_internal_dr_decomposition` | (no summary) |
| · | `check_T_w_trace_dizet_internal_dr_qcd_terms_exposed` | theorem | `P_w_trace_dizet_internal_dr_decomposition` | (no summary) |
| · | `check_T_w_trace_dizet_internal_dr_report_contains_equations` | theorem | `P_w_trace_dizet_internal_dr_decomposition` | (no summary) |
| · | `check_T_w_trace_dizet_internal_dr_residual_preserved` | theorem | `P_w_trace_dizet_internal_dr_decomposition` | (no summary) |
| · | `check_T_w_trace_dizet_internal_dr_rho_terms_exposed` | theorem | `P_w_trace_dizet_internal_dr_decomposition` | (no summary) |
| · | `check_T_w_trace_dizet_internal_dr_search_core_exposed` | theorem | `P_w_trace_dizet_internal_dr_decomposition` | (no summary) |
| · | `check_T_w_trace_dizet_internal_dr_status_declared` | theorem | `P_w_trace_dizet_internal_dr_decomposition` | (no summary) |
| · | `check_T_w_trace_dizet_internal_dr_terminal_verdict_exact` | theorem | `P_w_trace_dizet_internal_dr_decomposition` | (no summary) |
| · | `check_T_w_trace_dizet_internal_dr_total_result_preserved` | theorem | `P_w_trace_dizet_internal_dr_decomposition` | (no summary) |
| · | `check_T_w_trace_dizet_internal_dr_uninitialized_quarantine_named` | theorem | `P_w_trace_dizet_internal_dr_decomposition` | (no summary) |
| · | `check_T_w_trace_dizet_internal_dr_variables_exposed` | theorem | `P_w_trace_dizet_internal_dr_decomposition` | (no summary) |

## `apf/w_trace_dizet_row_admission_covariance.py` — 40 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_w_trace_dizet_row_admission_alpha_s_sensitivity_in_qcd_subrow` | theorem | `P_w_trace_dizet_row_admission_covariance` | (no summary) |
| · | `check_T_w_trace_dizet_row_admission_apf_deck_preserved` | theorem | `P_w_trace_dizet_row_admission_covariance` | (no summary) |
| · | `check_T_w_trace_dizet_row_admission_assembly_closes` | theorem | `P_w_trace_dizet_row_admission_covariance` | (no summary) |
| · | `check_T_w_trace_dizet_row_admission_auxiliary_rows_quarantined` | theorem | `P_w_trace_dizet_row_admission_covariance` | (no summary) |
| · | `check_T_w_trace_dizet_row_admission_bank_closure` | theorem | `P_w_trace_dizet_row_admission_covariance` | (no summary) |
| · | `check_T_w_trace_dizet_row_admission_covariance_positive_variance` | theorem | `P_w_trace_dizet_row_admission_covariance` | (no summary) |
| · | `check_T_w_trace_dizet_row_admission_covariance_psd` | theorem | `P_w_trace_dizet_row_admission_covariance` | (no summary) |
| · | `check_T_w_trace_dizet_row_admission_covariance_shape` | theorem | `P_w_trace_dizet_row_admission_covariance` | (no summary) |
| · | `check_T_w_trace_dizet_row_admission_covariance_symmetric` | theorem | `P_w_trace_dizet_row_admission_covariance` | (no summary) |
| · | `check_T_w_trace_dizet_row_admission_depends_on_v163` | theorem | `P_w_trace_dizet_row_admission_covariance` | (no summary) |
| · | `check_T_w_trace_dizet_row_admission_derivatives_finite` | theorem | `P_w_trace_dizet_row_admission_covariance` | (no summary) |
| · | `check_T_w_trace_dizet_row_admission_dizet_residual_preserved` | theorem | `P_w_trace_dizet_row_admission_covariance` | (no summary) |
| · | `check_T_w_trace_dizet_row_admission_drdmw_sign_correct` | theorem | `P_w_trace_dizet_row_admission_covariance` | (no summary) |
| · | `check_T_w_trace_dizet_row_admission_export_candidate_not_final` | theorem | `P_w_trace_dizet_row_admission_covariance` | (no summary) |
| · | `check_T_w_trace_dizet_row_admission_finite_remainder_admitted` | theorem | `P_w_trace_dizet_row_admission_covariance` | (no summary) |
| · | `check_T_w_trace_dizet_row_admission_first_failed_gate_publication_review` | theorem | `P_w_trace_dizet_row_admission_covariance` | (no summary) |
| · | `check_T_w_trace_dizet_row_admission_forbidden_language_present` | theorem | `P_w_trace_dizet_row_admission_covariance` | (no summary) |
| · | `check_T_w_trace_dizet_row_admission_gate_covariance_closed` | theorem | `P_w_trace_dizet_row_admission_covariance` | (no summary) |
| · | `check_T_w_trace_dizet_row_admission_gate_row_ledger_closed` | theorem | `P_w_trace_dizet_row_admission_covariance` | (no summary) |
| · | `check_T_w_trace_dizet_row_admission_grid_cases_recorded` | theorem | `P_w_trace_dizet_row_admission_covariance` | (no summary) |
| · | `check_T_w_trace_dizet_row_admission_has_three_admitted_rows` | theorem | `P_w_trace_dizet_row_admission_covariance` | (no summary) |
| · | `check_T_w_trace_dizet_row_admission_input_sigma_positive` | theorem | `P_w_trace_dizet_row_admission_covariance` | (no summary) |
| · | `check_T_w_trace_dizet_row_admission_jacobian_covers_admitted_rows` | theorem | `P_w_trace_dizet_row_admission_covariance` | (no summary) |
| · | `check_T_w_trace_dizet_row_admission_jacobian_covers_inputs` | theorem | `P_w_trace_dizet_row_admission_covariance` | (no summary) |
| · | `check_T_w_trace_dizet_row_admission_jacobian_nonempty` | theorem | `P_w_trace_dizet_row_admission_covariance` | (no summary) |
| · | `check_T_w_trace_dizet_row_admission_mtop_sensitivity_dominates_rho` | theorem | `P_w_trace_dizet_row_admission_covariance` | (no summary) |
| · | `check_T_w_trace_dizet_row_admission_no_double_count_auxiliaries` | theorem | `P_w_trace_dizet_row_admission_covariance` | (no summary) |
| · | `check_T_w_trace_dizet_row_admission_payload_digest_present` | theorem | `P_w_trace_dizet_row_admission_covariance` | (no summary) |
| · | `check_T_w_trace_dizet_row_admission_physical_export_not_final` | theorem | `P_w_trace_dizet_row_admission_covariance` | (no summary) |
| · | `check_T_w_trace_dizet_row_admission_pull_reasonable` | theorem | `P_w_trace_dizet_row_admission_covariance` | (no summary) |
| · | `check_T_w_trace_dizet_row_admission_report_contains_rows` | theorem | `P_w_trace_dizet_row_admission_covariance` | (no summary) |
| · | `check_T_w_trace_dizet_row_admission_report_contains_uncertainty` | theorem | `P_w_trace_dizet_row_admission_covariance` | (no summary) |
| · | `check_T_w_trace_dizet_row_admission_rho_cross_admitted` | theorem | `P_w_trace_dizet_row_admission_covariance` | (no summary) |
| · | `check_T_w_trace_dizet_row_admission_route_status_upgraded` | theorem | `P_w_trace_dizet_row_admission_covariance` | (no summary) |
| · | `check_T_w_trace_dizet_row_admission_running_alpha_admitted` | theorem | `P_w_trace_dizet_row_admission_covariance` | (no summary) |
| · | `check_T_w_trace_dizet_row_admission_status_declared` | theorem | `P_w_trace_dizet_row_admission_covariance` | (no summary) |
| · | `check_T_w_trace_dizet_row_admission_terminal_verdict_exact` | theorem | `P_w_trace_dizet_row_admission_covariance` | (no summary) |
| · | `check_T_w_trace_dizet_row_admission_theory_sigma_positive` | theorem | `P_w_trace_dizet_row_admission_covariance` | (no summary) |
| · | `check_T_w_trace_dizet_row_admission_total_evaluator_preserved` | theorem | `P_w_trace_dizet_row_admission_covariance` | (no summary) |
| · | `check_T_w_trace_dizet_row_admission_total_sigma_positive` | theorem | `P_w_trace_dizet_row_admission_covariance` | (no summary) |

## `apf/w_trace_e2e_import_pipeline_manifest.py` — 34 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_w_e2e_pipeline_manifest_bank_closure` | theorem | `P_w_e2e_import_pipeline_manifest` | (no summary) |
| · | `T_w_e2e_pipeline_manifest_component_sum_requires_bridge` | theorem | `P_w_e2e_import_pipeline_manifest` | (no summary) |
| · | `T_w_e2e_pipeline_manifest_covariance_bridge_requires_admitted_rows` | theorem | `P_w_e2e_import_pipeline_manifest` | (no summary) |
| · | `T_w_e2e_pipeline_manifest_covariance_requires_bridge` | theorem | `P_w_e2e_import_pipeline_manifest` | (no summary) |
| · | `T_w_e2e_pipeline_manifest_default_locked_state` | theorem | `P_w_e2e_import_pipeline_manifest` | (no summary) |
| · | `T_w_e2e_pipeline_manifest_depends_on_export_stack` | theorem | `P_w_e2e_import_pipeline_manifest` | (no summary) |
| · | `T_w_e2e_pipeline_manifest_depends_on_v117_to_v120` | theorem | `P_w_e2e_import_pipeline_manifest` | (no summary) |
| · | `T_w_e2e_pipeline_manifest_doc_exists` | theorem | `P_w_e2e_import_pipeline_manifest` | (no summary) |
| · | `T_w_e2e_pipeline_manifest_doc_warns_locked` | theorem | `P_w_e2e_import_pipeline_manifest` | (no summary) |
| · | `T_w_e2e_pipeline_manifest_edges_are_adjacent_and_acyclic` | theorem | `P_w_e2e_import_pipeline_manifest` | (no summary) |
| · | `T_w_e2e_pipeline_manifest_example_template_exists` | theorem | `P_w_e2e_import_pipeline_manifest` | (no summary) |
| · | `T_w_e2e_pipeline_manifest_export_requires_all_release_predicates` | theorem | `P_w_e2e_import_pipeline_manifest` | (no summary) |
| · | `T_w_e2e_pipeline_manifest_failure_reasons_deduplicated` | theorem | `P_w_e2e_import_pipeline_manifest` | (no summary) |
| · | `T_w_e2e_pipeline_manifest_forbidden_tokens_declared` | theorem | `P_w_e2e_import_pipeline_manifest` | (no summary) |
| · | `T_w_e2e_pipeline_manifest_handoff_before_import_log` | theorem | `P_w_e2e_import_pipeline_manifest` | (no summary) |
| · | `T_w_e2e_pipeline_manifest_import_before_rows_admitted` | theorem | `P_w_e2e_import_pipeline_manifest` | (no summary) |
| · | `T_w_e2e_pipeline_manifest_import_log_before_replay` | theorem | `P_w_e2e_import_pipeline_manifest` | (no summary) |
| · | `T_w_e2e_pipeline_manifest_json_serializable` | theorem | `P_w_e2e_import_pipeline_manifest` | (no summary) |
| · | `T_w_e2e_pipeline_manifest_no_duplicate_stages` | theorem | `P_w_e2e_import_pipeline_manifest` | (no summary) |
| · | `T_w_e2e_pipeline_manifest_physical_mw_requires_export_enable` | theorem | `P_w_e2e_import_pipeline_manifest` | (no summary) |
| · | `T_w_e2e_pipeline_manifest_rejects_forbidden_tokens` | theorem | `P_w_e2e_import_pipeline_manifest` | (no summary) |
| · | `T_w_e2e_pipeline_manifest_replay_before_rows_imported` | theorem | `P_w_e2e_import_pipeline_manifest` | (no summary) |
| · | `T_w_e2e_pipeline_manifest_required_fields_declared` | theorem | `P_w_e2e_import_pipeline_manifest` | (no summary) |
| · | `T_w_e2e_pipeline_manifest_review_before_handoff` | theorem | `P_w_e2e_import_pipeline_manifest` | (no summary) |
| · | `T_w_e2e_pipeline_manifest_reviewed_no_rows_is_not_export_ready` | theorem | `P_w_e2e_import_pipeline_manifest` | (no summary) |
| · | `T_w_e2e_pipeline_manifest_stage_order_declared` | theorem | `P_w_e2e_import_pipeline_manifest` | (no summary) |
| · | `T_w_e2e_pipeline_manifest_status_declared` | theorem | `P_w_e2e_import_pipeline_manifest` | (no summary) |
| · | `T_w_e2e_pipeline_manifest_status_versions_complete` | theorem | `P_w_e2e_import_pipeline_manifest` | (no summary) |
| · | `T_w_e2e_pipeline_manifest_sum_bridge_requires_admitted_rows` | theorem | `P_w_e2e_import_pipeline_manifest` | (no summary) |
| · | `T_w_e2e_pipeline_manifest_template_not_real` | theorem | `P_w_e2e_import_pipeline_manifest` | (no summary) |
| · | `T_w_e2e_pipeline_manifest_template_path_declared` | theorem | `P_w_e2e_import_pipeline_manifest` | (no summary) |
| · | `T_w_e2e_pipeline_manifest_terminal_states_declared` | theorem | `P_w_e2e_import_pipeline_manifest` | (no summary) |
| · | `T_w_e2e_pipeline_manifest_uncertainty_requires_sum_and_covariance` | theorem | `P_w_e2e_import_pipeline_manifest` | (no summary) |
| · | `T_w_e2e_pipeline_manifest_write_template` | theorem | `P_w_e2e_import_pipeline_manifest` | (no summary) |

## `apf/w_trace_external_ingestion_dryrun.py` — 25 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_w_external_ingestion_all_synthetic_formats_admit_shape_rows` | theorem | `—` | (no summary) |
| · | `T_w_external_ingestion_completion_gate_remains_locked` | theorem | `—` | (no summary) |
| · | `T_w_external_ingestion_component_order_preserved_all_formats` | theorem | `—` | (no summary) |
| · | `T_w_external_ingestion_csv_parser_roundtrip` | theorem | `—` | (no summary) |
| · | `T_w_external_ingestion_dryrun_bank_closure` | theorem | `—` | (no summary) |
| · | `T_w_external_ingestion_dryrun_depends_on_v100_adapter` | theorem | `—` | (no summary) |
| · | `T_w_external_ingestion_dryrun_formats_match_adapter` | theorem | `—` | (no summary) |
| · | `T_w_external_ingestion_dryrun_record_schema_preserved` | theorem | `—` | (no summary) |
| · | `T_w_external_ingestion_dryrun_report_shape` | theorem | `—` | (no summary) |
| · | `T_w_external_ingestion_dryrun_status_declared` | theorem | `P_w_external_ingestion_dryrun` | (no summary) |
| · | `T_w_external_ingestion_forbidden_inputs_reused_from_adapter` | theorem | `—` | (no summary) |
| · | `T_w_external_ingestion_json_parser_roundtrip` | theorem | `—` | (no summary) |
| · | `T_w_external_ingestion_mapping_parser_roundtrip` | theorem | `—` | (no summary) |
| · | `T_w_external_ingestion_no_component_sum_certified` | theorem | `—` | (no summary) |
| · | `T_w_external_ingestion_parser_outputs_external_records` | theorem | `—` | (no summary) |
| · | `T_w_external_ingestion_rejects_apf_anchor_column_after_parse` | theorem | `—` | (no summary) |
| · | `T_w_external_ingestion_rejects_bad_csv_header` | theorem | `—` | (no summary) |
| · | `T_w_external_ingestion_rejects_bad_json_version` | theorem | `—` | (no summary) |
| · | `T_w_external_ingestion_rejects_duplicate_component_after_parse` | theorem | `—` | (no summary) |
| · | `T_w_external_ingestion_rejects_fit_residual_column_after_parse` | theorem | `—` | (no summary) |
| · | `T_w_external_ingestion_rejects_missing_component_after_parse` | theorem | `—` | (no summary) |
| · | `T_w_external_ingestion_rejects_observed_W_column_after_parse` | theorem | `—` | (no summary) |
| · | `T_w_external_ingestion_rejects_unknown_format` | theorem | `—` | (no summary) |
| · | `T_w_external_ingestion_symbols_preserved_all_formats` | theorem | `—` | (no summary) |
| · | `T_w_external_ingestion_synthetic_only_flag_blocks_real_rows` | theorem | `—` | (no summary) |

## `apf/w_trace_external_source_adapter.py` — 23 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_w_external_source_adapter_bank_closure` | theorem | `—` | (no summary) |
| · | `T_w_external_source_adapter_completion_gate_remains_locked` | theorem | `—` | (no summary) |
| · | `T_w_external_source_adapter_covers_all_components` | theorem | `—` | (no summary) |
| · | `T_w_external_source_adapter_depends_on_v99_source_pack` | theorem | `—` | (no summary) |
| · | `T_w_external_source_adapter_empty_by_default` | theorem | `—` | (no summary) |
| · | `T_w_external_source_adapter_forbidden_inputs_superset_source_pack` | theorem | `—` | (no summary) |
| · | `T_w_external_source_adapter_formats_declared` | theorem | `—` | (no summary) |
| · | `T_w_external_source_adapter_manifest_export_shape` | theorem | `—` | (no summary) |
| · | `T_w_external_source_adapter_no_component_sum_certification_yet` | theorem | `—` | (no summary) |
| · | `T_w_external_source_adapter_rejects_apf_anchor_column` | theorem | `—` | (no summary) |
| · | `T_w_external_source_adapter_rejects_duplicate_components` | theorem | `—` | (no summary) |
| · | `T_w_external_source_adapter_rejects_missing_components` | theorem | `—` | (no summary) |
| · | `T_w_external_source_adapter_rejects_observed_W_column` | theorem | `—` | (no summary) |
| · | `T_w_external_source_adapter_rejects_residual_fit_column` | theorem | `—` | (no summary) |
| · | `T_w_external_source_adapter_rejects_unknown_components` | theorem | `—` | (no summary) |
| · | `T_w_external_source_adapter_requires_external_uri` | theorem | `—` | (no summary) |
| · | `T_w_external_source_adapter_requires_extraction_log_digest` | theorem | `—` | (no summary) |
| · | `T_w_external_source_adapter_requires_sha256_pack_digest` | theorem | `—` | (no summary) |
| · | `T_w_external_source_adapter_requires_supported_format` | theorem | `—` | (no summary) |
| · | `T_w_external_source_adapter_schema_extends_source_pack` | theorem | `—` | (no summary) |
| · | `T_w_external_source_adapter_shape_pack_admissible` | theorem | `—` | (no summary) |
| · | `T_w_external_source_adapter_status_declared` | theorem | `P_w_external_source_adapter` | (no summary) |
| · | `T_w_external_source_adapter_symbols_match_skeleton` | theorem | `—` | (no summary) |

## `apf/w_trace_final_export_readiness.py` — 32 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_w_final_export_readiness_all_true_predicate_only_symbolic_ready` | theorem | `P_w_final_export_readiness_aggregator` | (no summary) |
| · | `T_w_final_export_readiness_bank_closure` | theorem | `P_w_final_export_readiness_aggregator` | (no summary) |
| · | `T_w_final_export_readiness_blocks_physical_export_request_when_locked` | theorem | `P_w_final_export_readiness_aggregator` | (no summary) |
| · | `T_w_final_export_readiness_component_sum_required` | theorem | `P_w_final_export_readiness_aggregator` | (no summary) |
| · | `T_w_final_export_readiness_counterterm_convention_contributes_true` | theorem | `P_w_final_export_readiness_aggregator` | (no summary) |
| · | `T_w_final_export_readiness_counterterm_required` | theorem | `P_w_final_export_readiness_aggregator` | (no summary) |
| · | `T_w_final_export_readiness_covariance_bridge_empty_remains_uncertified` | theorem | `P_w_final_export_readiness_aggregator` | (no summary) |
| · | `T_w_final_export_readiness_covariance_required` | theorem | `P_w_final_export_readiness_aggregator` | (no summary) |
| · | `T_w_final_export_readiness_current_state_matches_locked_flags` | theorem | `P_w_final_export_readiness_aggregator` | (no summary) |
| · | `T_w_final_export_readiness_default_locked` | theorem | `P_w_final_export_readiness_aggregator` | (no summary) |
| · | `T_w_final_export_readiness_depends_on_v105_uncertainty_harness` | theorem | `—` | (no summary) |
| · | `T_w_final_export_readiness_depends_on_v106_export_lock` | theorem | `—` | (no summary) |
| · | `T_w_final_export_readiness_depends_on_v107_counterterm_convention` | theorem | `—` | (no summary) |
| · | `T_w_final_export_readiness_depends_on_v109_bundle_admission` | theorem | `—` | (no summary) |
| · | `T_w_final_export_readiness_depends_on_v110_sum_bridge` | theorem | `—` | (no summary) |
| · | `T_w_final_export_readiness_depends_on_v111_covariance_bridge` | theorem | `P_w_final_export_readiness_aggregator` | (no summary) |
| · | `T_w_final_export_readiness_dry_rows_do_not_set_current_flags` | theorem | `P_w_final_export_readiness_aggregator` | (no summary) |
| · | `T_w_final_export_readiness_forbidden_inputs_named` | theorem | `P_w_final_export_readiness_aggregator` | (no summary) |
| · | `T_w_final_export_readiness_forbids_apf_anchor_as_input` | theorem | `P_w_final_export_readiness_aggregator` | (no summary) |
| · | `T_w_final_export_readiness_forbids_observed_w_input` | theorem | `P_w_final_export_readiness_aggregator` | (no summary) |
| · | `T_w_final_export_readiness_forbids_residual_fit_input` | theorem | `P_w_final_export_readiness_aggregator` | (no summary) |
| · | `T_w_final_export_readiness_manifest_has_anchor_and_trace_mass` | theorem | `P_w_final_export_readiness_aggregator` | (no summary) |
| · | `T_w_final_export_readiness_manual_override_forbidden` | theorem | `P_w_final_export_readiness_aggregator` | (no summary) |
| · | `T_w_final_export_readiness_no_target_observable_consumption_required` | theorem | `P_w_final_export_readiness_aggregator` | (no summary) |
| · | `T_w_final_export_readiness_physical_mass_exports_false` | theorem | `P_w_final_export_readiness_aggregator` | (no summary) |
| · | `T_w_final_export_readiness_policy_blocks_manual_override` | theorem | `P_w_final_export_readiness_aggregator` | (no summary) |
| · | `T_w_final_export_readiness_real_rows_required` | theorem | `P_w_final_export_readiness_aggregator` | (no summary) |
| · | `T_w_final_export_readiness_report_schema_declared` | theorem | `P_w_final_export_readiness_aggregator` | (no summary) |
| · | `T_w_final_export_readiness_status_declared` | theorem | `P_w_final_export_readiness_aggregator` | (no summary) |
| · | `T_w_final_export_readiness_sum_bridge_empty_remains_uncertified` | theorem | `P_w_final_export_readiness_aggregator` | (no summary) |
| · | `T_w_final_export_readiness_target_scheme_required` | theorem | `P_w_final_export_readiness_aggregator` | (no summary) |
| · | `T_w_final_export_readiness_uncertainty_required` | theorem | `P_w_final_export_readiness_aggregator` | (no summary) |

## `apf/w_trace_finite_part_evaluator_gate.py` — 18 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_w_finite_part_component_sum_not_certified_without_values` | theorem | `—` | (no summary) |
| · | `T_w_finite_part_component_sum_predicate_declared` | theorem | `—` | (no summary) |
| · | `T_w_finite_part_counterterm_evaluator_slot_required_open` | theorem | `—` | (no summary) |
| · | `T_w_finite_part_covariance_uncertainty_still_block_export` | theorem | `—` | (no summary) |
| · | `T_w_finite_part_evaluator_completion_gate_remains_locked` | theorem | `—` | (no summary) |
| · | `T_w_finite_part_evaluator_depends_on_v94_ledger` | theorem | `—` | (no summary) |
| · | `T_w_finite_part_evaluator_gate_bank_closure` | theorem | `—` | (no summary) |
| · | `T_w_finite_part_evaluator_gate_status_declared` | theorem | `P_w_finite_part_evaluator_gate` | (no summary) |
| · | `T_w_finite_part_evaluator_next_requirements_explicit` | theorem | `—` | (no summary) |
| · | `T_w_finite_part_evaluator_no_fit_or_backsolve_allowed` | theorem | `—` | (no summary) |
| · | `T_w_finite_part_evaluator_no_physical_export` | theorem | `—` | (no summary) |
| · | `T_w_finite_part_evaluator_observed_W_forbidden` | theorem | `—` | (no summary) |
| · | `T_w_finite_part_evaluator_publication_ladder` | theorem | `—` | (no summary) |
| · | `T_w_finite_part_evaluator_slot_schema_complete` | theorem | `—` | (no summary) |
| · | `T_w_finite_part_evaluator_slots_cover_v94_components` | theorem | `—` | (no summary) |
| · | `T_w_finite_part_evaluator_source_requirements_declared` | theorem | `—` | (no summary) |
| · | `T_w_finite_part_evaluator_target_not_component_input` | theorem | `—` | (no summary) |
| · | `T_w_finite_part_evaluator_values_not_supplied_yet` | theorem | `—` | (no summary) |

## `apf/w_trace_finite_part_ledger.py` — 17 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_w_finite_part_allowed_inputs_are_v92_plus_trace_anchor` | theorem | `—` | (no summary) |
| · | `T_w_finite_part_anchor_delta_r_target_computed_from_trace_not_observed` | theorem | `—` | (no summary) |
| · | `T_w_finite_part_completion_gate_remains_locked` | theorem | `—` | (no summary) |
| · | `T_w_finite_part_component_schema_complete` | theorem | `—` | (no summary) |
| · | `T_w_finite_part_component_sum_not_certified_yet` | theorem | `—` | (no summary) |
| · | `T_w_finite_part_components_declared_unevaluated` | theorem | `—` | (no summary) |
| · | `T_w_finite_part_constants_ledger_still_source_tagged` | theorem | `—` | (no summary) |
| · | `T_w_finite_part_counterterm_component_required_not_filled` | theorem | `—` | (no summary) |
| · | `T_w_finite_part_covariance_and_uncertainty_gate_open` | theorem | `—` | (no summary) |
| · | `T_w_finite_part_depends_on_v93_symbolic_map` | theorem | `—` | (no summary) |
| · | `T_w_finite_part_ledger_bank_closure` | theorem | `—` | (no summary) |
| · | `T_w_finite_part_ledger_status_declared` | theorem | `P_w_finite_part_ledger` | (no summary) |
| · | `T_w_finite_part_next_completion_requirements_explicit` | theorem | `—` | (no summary) |
| · | `T_w_finite_part_no_observed_W_or_residual_inputs` | theorem | `—` | (no summary) |
| · | `T_w_finite_part_no_physical_W_export` | theorem | `—` | (no summary) |
| · | `T_w_finite_part_publication_claim_ladder` | theorem | `—` | (no summary) |
| · | `T_w_finite_part_required_components_enumerated` | theorem | `—` | (no summary) |

## `apf/w_trace_finite_part_skeleton.py` — 18 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_w_finite_part_skeleton_allowed_numeric_leaves_source_filled` | theorem | `—` | (no summary) |
| · | `T_w_finite_part_skeleton_bank_closure` | theorem | `—` | (no summary) |
| · | `T_w_finite_part_skeleton_codomain_not_physical_export` | theorem | `—` | (no summary) |
| · | `T_w_finite_part_skeleton_completion_gate_remains_locked` | theorem | `—` | (no summary) |
| · | `T_w_finite_part_skeleton_component_schema_complete` | theorem | `—` | (no summary) |
| · | `T_w_finite_part_skeleton_component_sum_still_uncertified` | theorem | `—` | (no summary) |
| · | `T_w_finite_part_skeleton_covers_all_slots` | theorem | `—` | (no summary) |
| · | `T_w_finite_part_skeleton_dependency_graph_acyclic` | theorem | `—` | (no summary) |
| · | `T_w_finite_part_skeleton_depends_on_v95_gate` | theorem | `—` | (no summary) |
| · | `T_w_finite_part_skeleton_forbids_observed_W_inputs` | theorem | `—` | (no summary) |
| · | `T_w_finite_part_skeleton_forbids_target_as_leaf` | theorem | `—` | (no summary) |
| · | `T_w_finite_part_skeleton_next_requirements_explicit` | theorem | `—` | (no summary) |
| · | `T_w_finite_part_skeleton_no_counterterm_tuning` | theorem | `—` | (no summary) |
| · | `T_w_finite_part_skeleton_publication_ladder` | theorem | `—` | (no summary) |
| · | `T_w_finite_part_skeleton_remains_symbolic_not_numeric` | theorem | `—` | (no summary) |
| · | `T_w_finite_part_skeleton_status_declared` | theorem | `P_w_finite_part_skeleton` | (no summary) |
| · | `T_w_finite_part_skeleton_sum_expression_declared` | theorem | `—` | (no summary) |
| · | `T_w_finite_part_skeleton_symbols_unique` | theorem | `—` | (no summary) |

## `apf/w_trace_full_loop_derivation_closeout.py` — 39 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_w_trace_full_loop_action_gate_named` | theorem | `P_w_trace_full_loop_derivation_closeout` | (no summary) |
| · | `check_T_w_trace_full_loop_allows_export_candidate_claim` | theorem | `P_w_trace_full_loop_derivation_closeout` | (no summary) |
| · | `check_T_w_trace_full_loop_bank_closure` | theorem | `P_w_trace_full_loop_derivation_closeout` | (no summary) |
| · | `check_T_w_trace_full_loop_closed_layers_exist` | theorem | `P_w_trace_full_loop_derivation_closeout` | (no summary) |
| · | `check_T_w_trace_full_loop_closed_layers_include_dizet_total` | theorem | `P_w_trace_full_loop_derivation_closeout` | (no summary) |
| · | `check_T_w_trace_full_loop_covariance_psd_preserved` | theorem | `P_w_trace_full_loop_derivation_closeout` | (no summary) |
| · | `check_T_w_trace_full_loop_decision_claims_candidate_not_native_full_loop` | theorem | `P_w_trace_full_loop_derivation_closeout` | (no summary) |
| · | `check_T_w_trace_full_loop_depends_on_v164` | theorem | `P_w_trace_full_loop_derivation_closeout` | (no summary) |
| · | `check_T_w_trace_full_loop_dizet_rows_still_admitted` | theorem | `P_w_trace_full_loop_derivation_closeout` | (no summary) |
| · | `check_T_w_trace_full_loop_export_candidate_closed` | theorem | `P_w_trace_full_loop_derivation_closeout` | (no summary) |
| · | `check_T_w_trace_full_loop_first_failed_gate_exact` | theorem | `P_w_trace_full_loop_derivation_closeout` | (no summary) |
| · | `check_T_w_trace_full_loop_forbids_full_loop_claim` | theorem | `P_w_trace_full_loop_derivation_closeout` | (no summary) |
| · | `check_T_w_trace_full_loop_layers_nonempty` | theorem | `P_w_trace_full_loop_derivation_closeout` | (no summary) |
| · | `check_T_w_trace_full_loop_mixed_higher_gate_named` | theorem | `P_w_trace_full_loop_derivation_closeout` | (no summary) |
| · | `check_T_w_trace_full_loop_native_cov_gate_named` | theorem | `P_w_trace_full_loop_derivation_closeout` | (no summary) |
| · | `check_T_w_trace_full_loop_native_full_loop_not_claimed` | theorem | `P_w_trace_full_loop_derivation_closeout` | (no summary) |
| · | `check_T_w_trace_full_loop_next_push_is_one_loop` | theorem | `P_w_trace_full_loop_derivation_closeout` | (no summary) |
| · | `check_T_w_trace_full_loop_no_raw_physical_final_claim` | theorem | `P_w_trace_full_loop_derivation_closeout` | (no summary) |
| · | `check_T_w_trace_full_loop_numerical_state_preserved` | theorem | `P_w_trace_full_loop_derivation_closeout` | (no summary) |
| · | `check_T_w_trace_full_loop_one_loop_gate_named` | theorem | `P_w_trace_full_loop_derivation_closeout` | (no summary) |
| · | `check_T_w_trace_full_loop_open_layers_exist` | theorem | `P_w_trace_full_loop_derivation_closeout` | (no summary) |
| · | `check_T_w_trace_full_loop_open_layers_include_counterterm` | theorem | `P_w_trace_full_loop_derivation_closeout` | (no summary) |
| · | `check_T_w_trace_full_loop_open_layers_include_two_loop` | theorem | `P_w_trace_full_loop_derivation_closeout` | (no summary) |
| · | `check_T_w_trace_full_loop_payload_digest_present` | theorem | `P_w_trace_full_loop_derivation_closeout` | (no summary) |
| · | `check_T_w_trace_full_loop_pull_preserved` | theorem | `P_w_trace_full_loop_derivation_closeout` | (no summary) |
| · | `check_T_w_trace_full_loop_reduction_gates_all_open` | theorem | `P_w_trace_full_loop_derivation_closeout` | (no summary) |
| · | `check_T_w_trace_full_loop_reduction_gates_five` | theorem | `P_w_trace_full_loop_derivation_closeout` | (no summary) |
| · | `check_T_w_trace_full_loop_reduction_is_minimal_ordered` | theorem | `P_w_trace_full_loop_derivation_closeout` | (no summary) |
| · | `check_T_w_trace_full_loop_report_contains_layers` | theorem | `P_w_trace_full_loop_derivation_closeout` | (no summary) |
| · | `check_T_w_trace_full_loop_report_contains_safe_claims` | theorem | `P_w_trace_full_loop_derivation_closeout` | (no summary) |
| · | `check_T_w_trace_full_loop_safe_claims_include_allowed_and_forbidden` | theorem | `P_w_trace_full_loop_derivation_closeout` | (no summary) |
| · | `check_T_w_trace_full_loop_status_declared` | theorem | `P_w_trace_full_loop_derivation_closeout` | (no summary) |
| · | `check_T_w_trace_full_loop_taxonomy_carries_v164_rows` | theorem | `P_w_trace_full_loop_derivation_closeout` | (no summary) |
| · | `check_T_w_trace_full_loop_taxonomy_has_mixed_higher` | theorem | `P_w_trace_full_loop_derivation_closeout` | (no summary) |
| · | `check_T_w_trace_full_loop_taxonomy_has_one_loop` | theorem | `P_w_trace_full_loop_derivation_closeout` | (no summary) |
| · | `check_T_w_trace_full_loop_taxonomy_has_two_loop` | theorem | `P_w_trace_full_loop_derivation_closeout` | (no summary) |
| · | `check_T_w_trace_full_loop_two_loop_gate_named` | theorem | `P_w_trace_full_loop_derivation_closeout` | (no summary) |
| · | `check_T_w_trace_full_loop_upgrade_gate_exact` | theorem | `P_w_trace_full_loop_derivation_closeout` | (no summary) |
| · | `check_T_w_trace_full_loop_v164_route_has_export_candidate` | theorem | `P_w_trace_full_loop_derivation_closeout` | (no summary) |

## `apf/w_trace_import_session_log.py` — 30 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_w_import_session_log_bank_closure` | theorem | `P_w_import_session_log` | (no summary) |
| · | `T_w_import_session_log_blocks_physical_export_request` | theorem | `P_w_import_session_log` | (no summary) |
| · | `T_w_import_session_log_default_no_session` | theorem | `P_w_import_session_log` | (no summary) |
| · | `T_w_import_session_log_depends_on_v118_handoff` | theorem | `P_w_import_session_log` | (no summary) |
| · | `T_w_import_session_log_digest_algorithm_fixed_sha256` | theorem | `P_w_import_session_log` | (no summary) |
| · | `T_w_import_session_log_doc_exists` | theorem | `P_w_import_session_log` | (no summary) |
| · | `T_w_import_session_log_doc_warns_locked` | theorem | `P_w_import_session_log` | (no summary) |
| · | `T_w_import_session_log_does_not_promote_dryrun_to_real` | theorem | `P_w_import_session_log` | (no summary) |
| · | `T_w_import_session_log_example_dir_exists` | theorem | `P_w_import_session_log` | (no summary) |
| · | `T_w_import_session_log_failure_reasons_deduplicated` | theorem | `P_w_import_session_log` | (no summary) |
| · | `T_w_import_session_log_forbidden_tokens_declared` | theorem | `P_w_import_session_log` | (no summary) |
| · | `T_w_import_session_log_handoff_version_recorded` | theorem | `P_w_import_session_log` | (no summary) |
| · | `T_w_import_session_log_json_serializable` | theorem | `P_w_import_session_log` | (no summary) |
| · | `T_w_import_session_log_loader_invoked_only_after_valid_handoff` | theorem | `P_w_import_session_log` | (no summary) |
| · | `T_w_import_session_log_loader_status_recorded` | theorem | `P_w_import_session_log` | (no summary) |
| · | `T_w_import_session_log_missing_payload_fails_closed` | theorem | `P_w_import_session_log` | (no summary) |
| · | `T_w_import_session_log_no_rows_or_certificates_by_default` | theorem | `P_w_import_session_log` | (no summary) |
| · | `T_w_import_session_log_payload_digest_changes_with_file` | theorem | `P_w_import_session_log` | (no summary) |
| · | `T_w_import_session_log_preserves_export_lock` | theorem | `P_w_import_session_log` | (no summary) |
| · | `T_w_import_session_log_promoted_awaits_payload` | theorem | `P_w_import_session_log` | (no summary) |
| · | `T_w_import_session_log_real_flag_does_not_admit_rows` | theorem | `P_w_import_session_log` | (no summary) |
| · | `T_w_import_session_log_record_schema_declared` | theorem | `P_w_import_session_log` | (no summary) |
| · | `T_w_import_session_log_records_json_dryrun_digest` | theorem | `P_w_import_session_log` | (no summary) |
| · | `T_w_import_session_log_rejects_forbidden_review_digest_token` | theorem | `P_w_import_session_log` | (no summary) |
| · | `T_w_import_session_log_states_declared` | theorem | `P_w_import_session_log` | (no summary) |
| · | `T_w_import_session_log_status_declared` | theorem | `P_w_import_session_log` | (no summary) |
| · | `T_w_import_session_log_template_file_exists` | theorem | `P_w_import_session_log` | (no summary) |
| · | `T_w_import_session_log_template_not_real` | theorem | `P_w_import_session_log` | (no summary) |
| · | `T_w_import_session_log_template_path_declared` | theorem | `P_w_import_session_log` | (no summary) |
| · | `T_w_import_session_log_write_template` | theorem | `P_w_import_session_log` | (no summary) |

## `apf/w_trace_import_session_replay.py` — 31 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_w_import_session_replay_bank_closure` | theorem | `—` | (no summary) |
| · | `T_w_import_session_replay_blocks_physical_export_request` | theorem | `P_w_import_session_replay_validator` | (no summary) |
| · | `T_w_import_session_replay_default_no_session` | theorem | `P_w_import_session_replay_validator` | (no summary) |
| · | `T_w_import_session_replay_depends_on_v119_log` | theorem | `P_w_import_session_replay_validator` | (no summary) |
| · | `T_w_import_session_replay_digest_algorithm_fixed_sha256` | theorem | `P_w_import_session_replay_validator` | (no summary) |
| · | `T_w_import_session_replay_digest_match_yields_dryrun_replayable` | theorem | `P_w_import_session_replay_validator` | (no summary) |
| · | `T_w_import_session_replay_digest_mismatch_fails_closed` | theorem | `P_w_import_session_replay_validator` | (no summary) |
| · | `T_w_import_session_replay_digest_recomputed_sha256` | theorem | `P_w_import_session_replay_validator` | (no summary) |
| · | `T_w_import_session_replay_doc_exists` | theorem | `P_w_import_session_replay_validator` | (no summary) |
| · | `T_w_import_session_replay_doc_warns_locked` | theorem | `P_w_import_session_replay_validator` | (no summary) |
| · | `T_w_import_session_replay_does_not_promote_dryrun_to_real` | theorem | `P_w_import_session_replay_validator` | (no summary) |
| · | `T_w_import_session_replay_example_dir_exists` | theorem | `P_w_import_session_replay_validator` | (no summary) |
| · | `T_w_import_session_replay_failure_reasons_deduplicated` | theorem | `P_w_import_session_replay_validator` | (no summary) |
| · | `T_w_import_session_replay_forbidden_tokens_declared` | theorem | `P_w_import_session_replay_validator` | (no summary) |
| · | `T_w_import_session_replay_json_serializable` | theorem | `P_w_import_session_replay_validator` | (no summary) |
| · | `T_w_import_session_replay_loader_preserved_only_on_digest_match` | theorem | `P_w_import_session_replay_validator` | (no summary) |
| · | `T_w_import_session_replay_missing_file_fails_closed` | theorem | `P_w_import_session_replay_validator` | (no summary) |
| · | `T_w_import_session_replay_no_rows_or_certificates_by_default` | theorem | `P_w_import_session_replay_validator` | (no summary) |
| · | `T_w_import_session_replay_preserves_export_lock` | theorem | `P_w_import_session_replay_validator` | (no summary) |
| · | `T_w_import_session_replay_promoted_without_payload_missing` | theorem | `P_w_import_session_replay_validator` | (no summary) |
| · | `T_w_import_session_replay_real_flag_does_not_admit_rows` | theorem | `P_w_import_session_replay_validator` | (no summary) |
| · | `T_w_import_session_replay_recompute_required` | theorem | `P_w_import_session_replay_validator` | (no summary) |
| · | `T_w_import_session_replay_record_schema_declared` | theorem | `P_w_import_session_replay_validator` | (no summary) |
| · | `T_w_import_session_replay_rejects_forbidden_expected_digest_token` | theorem | `P_w_import_session_replay_validator` | (no summary) |
| · | `T_w_import_session_replay_source_session_version_recorded` | theorem | `P_w_import_session_replay_validator` | (no summary) |
| · | `T_w_import_session_replay_states_declared` | theorem | `P_w_import_session_replay_validator` | (no summary) |
| · | `T_w_import_session_replay_status_declared` | theorem | `P_w_import_session_replay_validator` | (no summary) |
| · | `T_w_import_session_replay_template_file_exists` | theorem | `P_w_import_session_replay_validator` | (no summary) |
| · | `T_w_import_session_replay_template_not_real` | theorem | `P_w_import_session_replay_validator` | (no summary) |
| · | `T_w_import_session_replay_template_path_declared` | theorem | `P_w_import_session_replay_validator` | (no summary) |
| · | `T_w_import_session_replay_write_template` | theorem | `P_w_import_session_replay_validator` | (no summary) |

## `apf/w_trace_independent_delta_r_crosscheck.py` — 15 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_w_trace_independent_crosscheck_bank_closure` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_independent_crosscheck_delta_r_in_window` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_independent_crosscheck_detects_bad_token` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_independent_crosscheck_dgg_cross_scheme_labeled` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_independent_crosscheck_forbidden_scan_clean` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_independent_crosscheck_gaps_under_6_mev` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_independent_crosscheck_gaps_within_1sigma` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_independent_crosscheck_has_dgg` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_independent_crosscheck_has_gfitter` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_independent_crosscheck_no_component_claim` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_independent_crosscheck_no_covariance_claim` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_independent_crosscheck_no_export` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_independent_crosscheck_sources_forbid_apf_inputs` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_independent_crosscheck_sources_forbid_observed_w` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_independent_crosscheck_status_declared` | theorem | `—` | (no summary) |

## `apf/w_trace_input_basis_ledger.py` — 14 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_w_delta_r_slot_declared_unevaluated` | theorem | `P_w_input_basis_ledger` | Delta_r is an explicit finite-part slot and cannot be tuned to a W residual in v9.1. |
| · | `T_w_input_basis_completion_gate_remains_locked` | theorem | `P_w_input_basis_ledger` | The W terminal export gate is still locked after the input-basis ledger is selected. |
| · | `T_w_input_basis_ledger_bank_closure` | theorem | `P_w_input_basis_ledger` | W_TRACE input-basis ledger is banked; W physical transport remains open and gated. |
| · | `T_w_input_basis_ledger_schema_complete` | theorem | `P_w_input_basis_ledger` | The W input-basis ledger separates symbols, provenance, forbidden inputs, and terminal export status. |
| · | `T_w_input_basis_ledger_status_declared` | theorem | `P_w_input_basis_ledger` | v9.1 fills the W input-basis ledger contract while the physical export gate remains locked. |
| · | `T_w_input_basis_no_inverse_fit_channel` | theorem | `P_w_input_basis_ledger` | The W input-basis ledger exposes no inverse-fit channel for minimizing the W mass discrepancy. |
| · | `T_w_input_basis_publication_claim_ladder` | theorem | `P_w_input_basis_ledger` | The claim ladder permits only a W input-basis ledger claim, not a physical W prediction claim. |
| · | `T_w_input_basis_selected_from_v90_options` | theorem | `P_w_input_basis_ledger` | The W route now has a selected input-basis family without adding a new hidden option. |
| · | `T_w_input_correlation_requirements_declared` | theorem | `P_w_input_basis_ledger` | The W input-basis ledger requires covariance/correlation policy before any comparison error can be quoted. |
| · | `T_w_input_provenance_requirements_complete` | theorem | `P_w_input_basis_ledger` | Each allowed W input symbol must be source-tagged and uncertainty-tagged before numerical fill. |
| · | `T_w_input_relation_template_declared_not_solved` | theorem | `P_w_input_basis_ledger` | The W on-shell relation is banked as a symbolic terminal template, not a solved mass prediction. |
| · | `T_w_input_symbols_enumerated_without_values` | theorem | `P_w_input_basis_ledger` | The W route knows which EW symbols are allowed, but no numerical constants are imported. |
| · | `T_w_observed_MW_excluded_from_input_basis` | theorem | `P_w_input_basis_ledger` | The W input-basis ledger explicitly excludes observed M_W, W residuals, and residual-tuned Delta_r. |
| · | `T_w_trace_value_remains_upstream_not_input_constant` | theorem | `P_w_input_basis_ledger` | M_W^TRACE is the upstream APF object; neither M_W^TRACE nor physical M_W is an external input constant. |

## `apf/w_trace_input_convention_stress_test.py` — 13 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_w_trace_input_convention_acfw_is_carried_forward` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_input_convention_bank_closure` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_input_convention_cross_scheme_is_labeled` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_input_convention_delta_r_all_reasonable` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_input_convention_detects_bad_token` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_input_convention_forbidden_scan_clean` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_input_convention_gaps_few_mev` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_input_convention_gaps_within_declared_uncertainties` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_input_convention_global_fit_is_labeled` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_input_convention_has_three_sources` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_input_convention_no_export` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_input_convention_sensitivity_nonzero` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_input_convention_status_declared` | theorem | `—` | (no summary) |

## `apf/w_trace_measurement_quarantine_context.py` — 13 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_w_trace_measurement_quarantine_all_rows_context_only` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_measurement_quarantine_all_rows_not_admissible_as_source` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_measurement_quarantine_bank_closure` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_measurement_quarantine_cdf_is_outlier_context` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_measurement_quarantine_cdf_not_used_to_tune_apf` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_measurement_quarantine_cms_near_trace_context` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_measurement_quarantine_cms_not_used_to_tune_apf` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_measurement_quarantine_context_summary_present` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_measurement_quarantine_has_cdf_outlier_context` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_measurement_quarantine_has_cms_context` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_measurement_quarantine_no_delta_r_extraction_from_measurements` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_measurement_quarantine_no_export` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_measurement_quarantine_status_declared` | theorem | `—` | (no summary) |

## `apf/w_trace_multisource_delta_r_comparison.py` — 15 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_w_trace_multisource_all_points_few_mev` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_multisource_all_points_within_1p2sigma` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_multisource_apf_above_source_cluster` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_multisource_bank_closure` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_multisource_delta_r_weighted_reasonable` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_multisource_has_three_points` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_multisource_no_component_claim` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_multisource_no_covariance_claim` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_multisource_no_export` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_multisource_source_spread_small` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_multisource_status_declared` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_multisource_verdict_is_not_export` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_multisource_weighted_gap_near_one_sigma` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_multisource_weighted_gap_small` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_multisource_weighted_mean_computed` | theorem | `—` | (no summary) |

## `apf/w_trace_mw_from_effective_angle.py` — 3 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `C_w_trace_mw_from_3_13_chain` | other | `C` | Running the effective-mixing chain FORWARD from APF's candidate sin^2 theta_eff = 3/13 = 0.230769: s^2_OS = (3/13)/kappa_l = 0.222577 (kappa_l = 1.036808), M_W/M_Z = 0.881716, and with the M_Z scale anchor M_W = 80.4016 GeV -- 32 MeV from the measured 80.3692 GeV. This is the first chain in which... |
| · | `C_w_trace_mw_from_3_13_open_gates` | other | `C` | Three named gates stand between this chain and a [P] M_W/M_Z: (1) kappa_l is ~63% native -- two rungs of one ladder: custodial-only Xi_rho*Delta rho = 59% [P], + native gamma-Z oblique = 63% [P_structural] (v24.3.102); remainder Delta kappa_rem = 0.0136 (proper Zll vertex + light-fermion + Delta ... |
| · | `T_w_trace_mw_from_3_13_dimensionless` | theorem | `P_structural_partial` | The only quantity 3/13 can ever fix at [P] is the DIMENSIONLESS ratio M_W/M_Z = sqrt(1 - s^2_OS) = 0.881716. Converting to a GeV value requires M_Z as an external scale anchor -- absolute mass scales are the open sigma-derivation problem, so a zero-parameter M_W in GeV is architecturally out of r... |

## `apf/w_trace_native_bfm_photon_vp.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_w_trace_native_bfm_photon_vp_gauge_invariant` | theorem | `—` | (no summary) |

## `apf/w_trace_native_bosonic_gauge_self_energy.py` — 4 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_w_trace_native_bosonic_drho_pole` | theorem | `—` | (no summary) |
| · | `T_w_trace_native_bosonic_photon_pole` | theorem | `P` | The native bosonic photon self-energy Sigma^AA_bos = -(a/4pi){[3k^2+4MW^2]B0(k^2,MW,MW) - 4MW^2 B0(0,MW,MW)} has UV pole 3 k^2 (read off the mu-running to 4.9e-10), i.e. photon vacuum-polarization coefficient -3 -- reproducing the banked bosonic photon pole (v24.3.88: Goldstone +1/3, W+ghost -10/... |
| · | `T_w_trace_native_bosonic_regularity` | theorem | `—` | (no summary) |
| · | `T_w_trace_native_bosonic_scope_partial` | theorem | `P_structural_partial` | Denner's reviewed bosonic Sigma^AA_T / Sigma^ZZ_T / Sigma^W_T (App.B) are now native functions on the PV toolkit, validated by the banked poles (photon -3, bosonic Delta rho +4, M_H-independent) and k^2->0 regularity -- the v24.3.87-held W-sector bosonic piece done from the checked vertex algebra... |

## `apf/w_trace_native_bosonic_photon_vp.py` — 5 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_w_trace_native_bosonic_photon_vp_fermionic_norm_anchor` | theorem | `P` | The fermionic brace of the SAME Denner Sigma^{AA}_T -- bracket pole -k^2 per species -- assembled over the SM fermion content gives the photon-VP pole -(e^2/12pi^2) sum N_c Q^2 with sum N_c Q^2 = 8, value-identical to the banked apf.w_trace_native_uv_pole.photon_vp_pole_coeff (rel 1e-16). This is... |
| · | `T_w_trace_native_bosonic_photon_vp_finite_pole_consistency` | theorem | `P` | At deeply spacelike k^2 the native finite bosonic running d Pi_bos/d ln(-k^2) = -2.9999 PREF reproduces minus the pole coefficient (-3 PREF) to rel 4.9e-05, confirming the finite part (native re_b0_timelike quadrature of (3k^2+4M_W^2)B0) is consistent with the exact UV pole. Finite and divergent ... |
| · | `T_w_trace_native_bosonic_photon_vp_pole_minus3` | theorem | `P` | The bosonic Pi-pole = +3 PREF (M_W-independent to 0.0e+00), i.e. -3 in the screening-positive beta convention (Dirac +4/3, scalar +1/3); ratio to one Dirac fermion = -2.2500 = -9/4. Subtracting the v24.3.87 banked Goldstone piece (-1/3 in beta units) leaves the W gauge+seagull+ghost piece = -10/3... |
| · | `T_w_trace_native_bosonic_photon_vp_scope_partial` | theorem | `P_structural_partial` | The complete bosonic transverse photon self-energy Sigma^{AA}_T (W gauge + seagull + Goldstone + FP ghost, 't Hooft-Feynman gauge) is now native, evaluated from Denner's reviewed closed form with the banked PV toolkit and validated by transversality, the -3 pole (with the banked Goldstone piece c... |
| · | `T_w_trace_native_bosonic_photon_vp_transversality` | theorem | `P` | Denner's bosonic brace (3k^2+4M_W^2)B0(k^2,M_W,M_W) - 4M_W^2 B0(0,M_W,M_W) vanishes at k^2=0 to rel 1.4e-05 for two distinct M_W values -- the M_W^2 pieces cancel, leaving Sigma^{AA}_T,bos(0)=0, the U(1)_em Ward identity. This is the gauge gate the v24.3.87 memory-vertex attempt failed; the revie... |

## `apf/w_trace_native_bosonic_scalar_vp.py` — 4 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_w_trace_native_bosonic_scalar_vp_scope_partial` | theorem | `P_structural_partial` | The first bosonic piece of the photon self-energy -- the charged Goldstone (scalar-QED) loop -- is built and validated three ways (transversality, the 1/4-of-a-fermion pole, the 8/3 finite constant), reusing the v24.3.86 UV-pole layer. Still OPEN toward the bosonic Pi_gamma_gamma and the APF-inte... |
| · | `T_w_trace_native_scalar_vp_finite_closed_form` | theorem | `P` | The on-shell-subtracted charged-scalar running Pi_phi(M_Z^2) - Pi_phi(0) reproduces the scalar-QED closed form (e^2 Q^2/16 pi^2)(1/3)[ln(q^2/m^2) - 8/3] to max rel 2.2e-04 -- the leading coefficient 1/3 (one quarter of the fermion's 4/3) and the scalar constant 8/3 (vs the fermion's 5/3). Confirm... |
| · | `T_w_trace_native_scalar_vp_pole_one_quarter` | theorem | `P` | Via the v24.3.86 UV-pole layer, the scalar numerator pole 4 B00_pole - 2 A0_pole = -p^2/3, so the scalar form-factor pole is -(e^2 Q^2/48 pi^2) = (1/3) Q^2 in beta-function units -- exactly 1/4 of a Dirac fermion's (4/3) Q^2 (ratio 0.250000). This is the correct scalar-QED contribution to the pho... |
| · | `T_w_trace_native_scalar_vp_transversality` | theorem | `P` | The charged-scalar photon self-energy (gamma-phi-phi bubble + gamma-gamma-phi-phi seagull) has g^{mu nu} numerator 4 B00 - 2 A0, which vanishes at p^2 = 0 to rel 2.8e-07 (because 2 B00(0,m^2,m^2) = A0(m^2)), so Sigma^{mu nu}(0) = 0 and the self-energy is purely transverse -- the U(1)_em Ward iden... |

## `apf/w_trace_native_charge_running.py` — 5 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_w_trace_native_charge_running_bosonic_minus7` | theorem | `P` | The bosonic one-loop running of the electric charge, b = 2 delta Z_e with delta Z_e = (1/2) dSigma^{AA}_T/dk^2\|_0 - (s_W/c_W)Sigma^{AZ}_T(0)/M_Z^2, assembled natively from Denner's reviewed Sigma^{AA}_T (banked v24.3.88, contributing -3) and Sigma^{AZ}_T (contributing -4), equals -7 exactly. This... |
| · | `T_w_trace_native_charge_running_fermionic_anchor` | theorem | `P` | The fermionic gamma-Z brace vanishes at k^2=0 (to 0e+00, coupling-independently), so the fermionic charge running is the photon-SE piece only and equals +(4/3) sum N_c Q^2 = 10.6667 with sum N_c Q^2 = 8, value-identical to the banked \|photon_vp_pole_coeff\|/PREF. This is the no-smuggling calibrati... |
| · | `T_w_trace_native_charge_running_gammaZ_mixing` | theorem | `P` | Denner's bosonic gamma-Z mixing Sigma^{AZ}_T,bos(0), evaluated natively, matches its closed form +(alpha/4pi)(2/(s_W c_W))M_W^2 B0(0,M_W,M_W) to rel 5.0e-16 across M_W and sin^2 theta values. Its (s_W/c_W)Sigma^{AZ}(0)/M_Z^2 pole coefficient is +2 (s_W/c_W cancelling against the 2c_W/s_W from the... |
| · | `T_w_trace_native_charge_running_gauge_invariance` | theorem | `P` | The bosonic charge-running coefficient stays -7 across sin^2 theta_W in [0.20, 0.30] (spread 9e-16) and across M_W -- the s_W/c_W in the gamma-Z term cancels against the 2 c_W/s_W from M_Z^2 = M_W^2/c_W^2, and the photon-SE -3 is intrinsically scale-free. A gauge-invariance / Ward gate: the physi... |
| · | `T_w_trace_native_charge_running_scope_partial` | theorem | `P_structural_partial` | The gauge-invariant one-loop running of the electric charge is now native: the bosonic -7 (= -3 photon SE + -4 gamma-Z mixing) and the fermionic +(4/3) sum N_c Q^2, assembled from Denner's reviewed Sigma^{AA}_T + Sigma^{AZ}_T with the convention calibrated on the banked QED fermion value. Still O... |

## `apf/w_trace_native_delta_r_mw_assembly.py` — 4 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_w_trace_native_delta_r_ir_finite` | theorem | `P` | As the photon IR regulator lambda^2 sweeps 1e-4 -> 1e-8 the assembled Delta r changes by only 1.6e-06: the ln(lambda) from the W-photon loop in Sigma^W(M_W^2) cancels in the Delta r combination, as required for the muon-decay correction (the QED/Fermi-model IR is subtracted, leaving the finite de... |
| · | `T_w_trace_native_delta_r_mu_independent` | theorem | `P` | With all native self-energies evaluated at a common scale mu, the assembled Delta r is mu-independent under mu^2 -> {0.25, 1, 4} M_Z^2 (spread 1.5e-09) -- the per-term mu-running (in Pi^AA(0), Sigma^ZZ, Sigma^W, Sigma^AZ) cancels exactly in the physical combination, a strong consistency check on ... |
| · | `T_w_trace_native_delta_r_mw_scope_partial` | theorem | `P_structural_partial` | The native one-loop OS-W evaluator is complete: Denner's full Delta r is assembled from native PV-evaluated self-energies and reproduces the published one-loop M_W to ~30 MeV, mu-independent and IR-finite. This closes the long-tracked 'native OS-W Delta r_rem / M_W' item -- APF no longer needs to... |
| · | `T_w_trace_native_mw_reproduces_denner` | theorem | `P` | Denner's complete one-loop Delta r, assembled from the native PV-evaluated self-energies (Sigma^AA/AZ/ZZ/W, fermionic + bosonic) and solved in the on-shell scheme, gives native M_W = 80.2605 GeV, reproducing Denner's published one-loop M_W = 80.23 GeV to 30 MeV (Denner inputs: alpha=1/137.036, M_... |

## `apf/w_trace_native_delta_r_uv_assembly.py` — 4 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_w_trace_native_delta_VB_closed_form` | theorem | `P` | The Sirlin vertex+box correction delta_VB = (alpha/4pi s^2)(6 + (7-4s^2)/(2s^2) ln c^2), Denner's reviewed closed form (the assembled muon-decay vertex+box that the native 3-/4-point C/D tensors of v24.3.74-.79 build), evaluated at the APF s^2 = 3/13 gives delta_VB = 0.006406 -- finite and gauge-... |
| · | `T_w_trace_native_delta_r_assembly_scope_partial` | theorem | `P_structural_partial` | Denner's native Delta r is now assembled at the structural + divergence level: the full UV cancellation closes (all native self-energy poles), delta_VB is native (closed form), and Pi^{AA}(0) / Sigma^{AZ}(0) are native (v24.3.88-.92). The ONE remaining input is the finite REAL part of the timelik... |
| · | `T_w_trace_native_delta_r_uv_cancellation` | theorem | `P` | Substituting every native gauge-boson self-energy pole -- Sigma^{AA} (P_AA_bos + P_AA_ferm, stage-4), Sigma^{ZZ}/Sigma^{WW} (banked bosonic P_*_bos + fermionic p2coeff_* + the m^2 pieces), Sigma^{AZ}(0) -- into Denner's Delta r master formula yields a UV pole of 2.3e-14 (rel 3.0e-15), i.e. ZERO: ... |
| · | `T_w_trace_native_delta_r_uv_gauge_invariance` | theorem | `P` | The full Delta r UV pole vanishes (max \|pole\| 2.3e-14) across sin^2 theta_W in [0.20, 0.30] -- the cancellation is gauge/weak-angle independent, as a physical (finite) Delta r must be. A strong consistency gate on the entire native self-energy pole structure simultaneously. |

## `apf/w_trace_native_drho_top.py` — 4 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_w_trace_native_drho_top_mb_limit` | theorem | `P` | The native Veltman F(m_t^2, m_b^2) rises monotonically toward m_t^2 = 26569.0 as m_b -> 0 (F(m_b=0.03) within 1e-3 of m_t^2), confirming the banked m_b = 0 form Drho_top ~ m_t^2 is the correct limit of the native loop function and the finite-m_b Veltman correction is reproduced. |
| · | `T_w_trace_native_drho_top_reproduces_banked` | theorem | `P` | Fed the APF-internal inputs (m_t=163 [L_sigma_normalization], sin^2 theta_W=3/13 [T_sin2theta], alpha=1/128.21 [L_alpha_em]), the native Delta rho_top = (3 alpha)/(16 pi M_W^2 s_W^2) * F_native(m_t^2, m_b^2) reproduces the banked gauge.L_W_mass Drho_top = 0.008379 in the m_b -> 0 limit (native 0.... |
| · | `T_w_trace_native_drho_top_scope_partial` | theorem | `P_structural_partial` | This rung establishes that the native PV substrate reproduces the leading custodial Delta rho_top (the p^2=0 fermionic piece) from genuine loop integrals -- the Stage-2 fermionic gate of the native OS-W one-loop evaluator work plan. The full APF-internal Delta r_rem remains OPEN: the timelike Re ... |
| · | `T_w_trace_native_veltman_F_identity` | theorem | `P` | The Veltman rho-function has the exact, mu-independent native PV representation F(m1^2,m2^2) = (m1^2+m2^2)(1+B0(0;m1^2,m2^2)) - A0(m1^2) - A0(m2^2) (confirmed symbolically: F_identity - F_closed = 0). Evaluated with the native a0_fin/b0_fin it matches the closed-form Veltman function to max relat... |

## `apf/w_trace_native_ew_self_energy.py` — 4 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_w_trace_native_drho_routes_consistent` | theorem | `P` | The two independent native routes to Delta rho_top agree: the slot-by-slot transverse self-energies (0.008376) and the v24.3.82 Veltman-F-via-A0/B0 result (0.008378) match to rel 2.6e-04 -- a cross-check between the per-coupling self-energy construction and the custodial-combination identity. |
| · | `T_w_trace_native_drho_slot_by_slot` | theorem | `P` | The fermionic transverse self-energies built SLOT-BY-SLOT from the SM electroweak couplings and colour -- W from the purely left-handed (t,b) current (g/sqrt2), Z from per-fermion g_L=(g/c)(T3-Q s^2), g_R=(g/c)(-Q s^2), N_c=3 -- give Delta rho = A_W(0)/M_W^2 - A_Z(0)/M_Z^2 = 0.008376, reproducing... |
| · | `T_w_trace_native_photon_transversality` | theorem | `P` | The native fermion-loop photon self-energy (g_L=g_R=eQ, equal mass) is purely transverse: A_gamma(0) vanishes relative to A_gamma(-100 GeV^2) to 3.5e-13, while A_gamma(p^2) ~ p^2 is non-trivial (A/p^2 stable to 13%). In the native convention this holds because 2 B00(0,m^2,m^2) = A0(m^2). This ind... |
| · | `T_w_trace_native_self_energy_scope_partial` | theorem | `P_structural_partial` | Stage 2 of the native OS-W evaluator now has the full fermionic transverse self-energies at p^2=0, built slot-by-slot from SM couplings and colour, validated by photon transversality and the banked Delta rho_top. Still OPEN toward the APF-internal Delta r_rem: the timelike Re Pi_WW(M_W^2) / Re Pi... |

## `apf/w_trace_native_fermion_sum_self_energy.py` — 4 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_w_trace_native_fermion_sum_charge_anchor` | theorem | `P` | The SM-fermion registry gives sum N_c Q^2 = 8.0 (leptons 3 + up-type 4 + down-type 1), and the assembled fermionic photon vacuum-polarization slope dP_gammagamma/dp^2\|_0 = -(e^2/12 pi^2) sum N_c Q^2 reproduces the one-loop QED beta coefficient to rel 1.3e-16. The fermion content's charge structur... |
| · | `T_w_trace_native_fermion_sum_drho_top` | theorem | `P` | Within the full fermion-sum assembly the top (t,b) doublet contribution to Sigma_WW(0)/M_W^2 - Sigma_ZZ(0)/M_Z^2 = 0.008379 reproduces the banked gauge.L_W_mass Delta rho_top = 0.008379 to rel 1.2e-05 -- confirming the colour-parametrized fermion-sum machinery agrees with the banked custodial res... |
| · | `T_w_trace_native_fermion_sum_mu_independence` | theorem | `—` | (no summary) |
| · | `T_w_trace_native_fermion_sum_scope_partial` | theorem | `P_structural_partial` | The full SM fermionic transverse self-energies are now assembled natively and OS-renormalized, with the total proven mu-independent and anchored to sum N_c Q^2 = 8 and the banked Delta rho_top. The fermionic sector was already banked piecewise (Delta alpha_lep v24.3.69, Delta rho v24.3.82/83); th... |

## `apf/w_trace_native_fermionic_gauge_self_energy.py` — 4 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_w_trace_native_fermionic_gauge_W_su2_structure` | theorem | `P` | The fermionic W self-energy p^2-pole coefficient is -(2/3)(1/2 s_W^2) N_doublet = -4/s_W^2 with N_doublet = 12 (3 lepton + 9 colour-counted quark left doublets). It scales as 1/s_W^2 (ratio 1.0833 = s2b/s2a) -- the g^2 = e^2/s_W^2 coupling structure -- and carries the correct SM doublet count, th... |
| · | `T_w_trace_native_fermionic_gauge_ZAZ_weinberg` | theorem | `P` | The fermionic Z and gamma-Z self-energy couplings, assembled from Denner's chiral g^+ = -s^2 Q/(s c), g^- = (I_3 - s^2 Q)/(s c), reproduce the electroweak charge sum rules: sum N_c Q I_3 = 6, sum N_c I_3^2 = 6, the gamma-Z sum = -(sum Q I_3 - 2 s^2 sum Q^2)/(s c) = -5.4772, and the ZZ sum = (2 s^... |
| · | `T_w_trace_native_fermionic_gauge_photon_anchor` | theorem | `P` | The fermionic photon self-energy p^2-pole coefficient assembled from the SM charges is -(4/3) sum N_c Q^2 with sum N_c Q^2 = 8, value-identical to the banked apf.w_trace_native_uv_pole QED beta-function (whose finite part is Delta alpha_lep). The electroweak charge consistency Q^2 = I_3^2 + 2 I_3... |
| · | `T_w_trace_native_fermionic_gauge_scope_partial` | theorem | `P_structural_partial` | The fermionic gauge-boson self-energy p^2-pole coefficients (AA/AZ/ZZ/WW) are now native, assembled from the SM gauge charges + Denner's chiral couplings and anchored on the banked photon (sum N_c Q^2 = 8), the SU(2) g^2/s^2 + 12-doublet structure, and the electroweak charge sum rules. Combined w... |

## `apf/w_trace_native_finite_remainder_evaluator.py` — 35 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_w_trace_native_finite_admitted_rows_available` | theorem | `P_w_trace_native_finite_remainder_evaluator_target` | (no summary) |
| · | `check_T_w_trace_native_finite_bank_closure` | theorem | `P_w_trace_native_finite_remainder_evaluator_target` | (no summary) |
| · | `check_T_w_trace_native_finite_closed_target_gate_present` | theorem | `P_w_trace_native_finite_remainder_evaluator_target` | (no summary) |
| · | `check_T_w_trace_native_finite_denner_gate_blocks_native_loop` | theorem | `P_w_trace_native_finite_remainder_evaluator_target` | (no summary) |
| · | `check_T_w_trace_native_finite_dependencies_pass` | theorem | `P_w_trace_native_finite_remainder_evaluator_target` | (no summary) |
| · | `check_T_w_trace_native_finite_drrem_positive` | theorem | `P_w_trace_native_finite_remainder_evaluator_target` | (no summary) |
| · | `check_T_w_trace_native_finite_export_candidate_preserved` | theorem | `P_w_trace_native_finite_remainder_evaluator_target` | (no summary) |
| · | `check_T_w_trace_native_finite_first_failed_gate_exact` | theorem | `P_w_trace_native_finite_remainder_evaluator_target` | (no summary) |
| · | `check_T_w_trace_native_finite_forbidden_claims_present` | theorem | `P_w_trace_native_finite_remainder_evaluator_target` | (no summary) |
| · | `check_T_w_trace_native_finite_fraction_reasonable` | theorem | `P_w_trace_native_finite_remainder_evaluator_target` | (no summary) |
| · | `check_T_w_trace_native_finite_gates_count` | theorem | `P_w_trace_native_finite_remainder_evaluator_target` | (no summary) |
| · | `check_T_w_trace_native_finite_has_drrem_piece` | theorem | `P_w_trace_native_finite_remainder_evaluator_target` | (no summary) |
| · | `check_T_w_trace_native_finite_has_rho_gap_piece` | theorem | `P_w_trace_native_finite_remainder_evaluator_target` | (no summary) |
| · | `check_T_w_trace_native_finite_has_total_target_piece` | theorem | `P_w_trace_native_finite_remainder_evaluator_target` | (no summary) |
| · | `check_T_w_trace_native_finite_input_physical` | theorem | `P_w_trace_native_finite_remainder_evaluator_target` | (no summary) |
| · | `check_T_w_trace_native_finite_mw_conversion_sign` | theorem | `P_w_trace_native_finite_remainder_evaluator_target` | (no summary) |
| · | `check_T_w_trace_native_finite_mw_pull_preserved` | theorem | `P_w_trace_native_finite_remainder_evaluator_target` | (no summary) |
| · | `check_T_w_trace_native_finite_mw_scale_large` | theorem | `P_w_trace_native_finite_remainder_evaluator_target` | (no summary) |
| · | `check_T_w_trace_native_finite_no_double_count_identity` | theorem | `P_w_trace_native_finite_remainder_evaluator_target` | (no summary) |
| · | `check_T_w_trace_native_finite_no_physical_final_claim` | theorem | `P_w_trace_native_finite_remainder_evaluator_target` | (no summary) |
| · | `check_T_w_trace_native_finite_open_closure_requires_counterterms` | theorem | `P_w_trace_native_finite_remainder_evaluator_target` | (no summary) |
| · | `check_T_w_trace_native_finite_open_gate_present` | theorem | `P_w_trace_native_finite_remainder_evaluator_target` | (no summary) |
| · | `check_T_w_trace_native_finite_payload_digest_present` | theorem | `P_w_trace_native_finite_remainder_evaluator_target` | (no summary) |
| · | `check_T_w_trace_native_finite_piece_count` | theorem | `P_w_trace_native_finite_remainder_evaluator_target` | (no summary) |
| · | `check_T_w_trace_native_finite_report_contains_gates` | theorem | `P_w_trace_native_finite_remainder_evaluator_target` | (no summary) |
| · | `check_T_w_trace_native_finite_report_contains_pieces` | theorem | `P_w_trace_native_finite_remainder_evaluator_target` | (no summary) |
| · | `check_T_w_trace_native_finite_rho_gap_negative` | theorem | `P_w_trace_native_finite_remainder_evaluator_target` | (no summary) |
| · | `check_T_w_trace_native_finite_row_covariance_available` | theorem | `P_w_trace_native_finite_remainder_evaluator_target` | (no summary) |
| · | `check_T_w_trace_native_finite_safe_claims_present` | theorem | `P_w_trace_native_finite_remainder_evaluator_target` | (no summary) |
| · | `check_T_w_trace_native_finite_skeleton_below_total` | theorem | `P_w_trace_native_finite_remainder_evaluator_target` | (no summary) |
| · | `check_T_w_trace_native_finite_skeleton_fraction_reasonable` | theorem | `P_w_trace_native_finite_remainder_evaluator_target` | (no summary) |
| · | `check_T_w_trace_native_finite_status_declared` | theorem | `P_w_trace_native_finite_remainder_evaluator_target` | (no summary) |
| · | `check_T_w_trace_native_finite_target_pieces_sum_to_total_target` | theorem | `P_w_trace_native_finite_remainder_evaluator_target` | (no summary) |
| · | `check_T_w_trace_native_finite_target_positive` | theorem | `P_w_trace_native_finite_remainder_evaluator_target` | (no summary) |
| · | `check_T_w_trace_native_finite_target_recomposes` | theorem | `P_w_trace_native_finite_remainder_evaluator_target` | (no summary) |

## `apf/w_trace_native_gauge_boson_drho_uv.py` — 4 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_w_trace_native_drho_bosonic_pole_universal` | theorem | `P` | The bosonic custodial Delta rho carries a universal bare UV pole +4 (in alpha/4pi units), independent of sin^2 theta_W, M_W, and M_H (spread 6e-15). Unlike the fermionic Delta rho, the bosonic part is NOT separately UV-finite: this +4 is exactly the pole the Stage-4 M_W^2/M_Z^2 counterterms must ... |
| · | `T_w_trace_native_drho_fermionic_uv_finite` | theorem | `P` | The fermionic custodial Delta rho = Sigma^{WW}_T,ferm(0)/M_W^2 - Sigma^{ZZ}_T,ferm(0)/M_Z^2 has a vanishing UV pole (max rel 2.7e-16) for the (t,b) doublet, the full SM fermion content, and across sin^2 theta_W and M_W -- the famous UV-finiteness of the custodial parameter. Because both Denner se... |
| · | `T_w_trace_native_drho_per_doublet_custodial` | theorem | `P` | For every SM doublet (U,D) individually, Sigma^{WW}_T,ferm(0)/M_W^2 pole = Sigma^{ZZ}_T,ferm(0)/M_Z^2 pole (both = (N_c/(2 s_W^2))(m_U^2+m_D^2)/M_W^2 once M_Z^2 = M_W^2/c_W^2), max rel 2.7e-16. The divergence is custodial-symmetric per doublet, so it cancels in Delta rho independent of the mass s... |
| · | `T_w_trace_native_drho_uv_scope_partial` | theorem | `P_structural_partial` | The k^2=0 UV-pole structure of Denner's Sigma^{WW}_T / Sigma^{ZZ}_T is now native, with the fermionic custodial Delta rho proven UV-finite (validating the transcription) and the bosonic Delta rho's universal +4 divergence characterized as the Stage-4 counterterm target. Still OPEN toward Delta r_... |

## `apf/w_trace_native_os_renormalized_self_energy.py` — 4 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_w_trace_native_os_renorm_mu_independence` | theorem | `—` | (no summary) |
| · | `T_w_trace_native_os_renorm_os_conditions` | theorem | `P` | The twice-subtracted Sigma_hat(p^2)=A(p^2)-A(M^2)-(p^2-M^2)A'(M^2) satisfies the OS conditions Sigma_hat(M^2)=0 (max 0.0e+00) and Sigma_hat'(M^2)=0 (max 0.0e+00) for the W(t,b), W(c,s) and Z(t,t) fermion loops -- the renormalized self-energy entering the OS Delta r, by construction free of the ba... |
| · | `T_w_trace_native_os_renorm_running_matches_pole` | theorem | `—` | (no summary) |
| · | `T_w_trace_native_os_renorm_scope_partial` | theorem | `P_structural_partial` | The OS-renormalized transverse self-energy Sigma_hat(p^2) is native and proven mu-independent (per fermion loop), OS conditions Sigma_hat(M^2)=Sigma_hat'(M^2)=0 built in -- closing the bare term-by-term scale-dependence that spoiled the precision attempt. OPEN toward Delta r_rem: the full SM ferm... |

## `apf/w_trace_native_pv_massless_safe.py` — 5 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_w_trace_native_pv_massless_safe_closed_forms` | theorem | `P` | The analytic massless/degenerate Re B0 branches -- B0(p^2,0,0), B0(p^2,0,m^2) (incl. the p^2=m^2 pseudo-threshold), B0(0,m^2,m^2), B0(0,m0^2,m1^2), B0(0,0,m^2) -- reproduce the banked midpoint quadrature with tiny mass/momentum regulators (eps=1e-6) to max abs err 1.9e-05. Native, no external input. |
| · | `T_w_trace_native_pv_massless_safe_imaginary` | theorem | `P` | The closed-form absorptive parts -- Im B0(p^2,0,0)=pi theta(p^2) and Im B0(p^2,0,m^2)=pi(1-m^2/p^2) theta(p^2-m^2) -- reproduce the regulated banked Im quadrature to max abs err 1.0e-05, and vanish spacelike / below threshold. Native, no external input. |
| · | `T_w_trace_native_pv_massless_safe_no_crash` | theorem | `P` | re_b0_safe returns the scaleless finite part 0 for B0(0,0,0) (where the banked quadrature throws log(0)), stays finite at the one-massless pseudo-threshold B0(m^2,0,m^2) via the removable-singularity guard, and is finite for exactly-massless lines -- the cases the SM self-energies need (neutrino ... |
| · | `T_w_trace_native_pv_massless_safe_overlap` | theorem | `P` | For all-massive, p^2 != 0 kinematics the dispatcher re_b0_safe / im_b0_safe routes straight to the banked re_b0_timelike / im_b0_timelike and is value-identical (max err 0.0e+00) -- the massless branch is a continuation of the banked substrate, not a separate object. |
| · | `T_w_trace_native_pv_massless_safe_subgate_partial` | theorem | `P_structural_partial` | The native two-point B0 now has clean analytic massless / degenerate branches (exactly-massless lines, zero momentum, the scaleless point, the one-massless pseudo-threshold), reducing to the banked quadrature for massive lines. Still OPEN toward the APF-internal Delta r_rem: the tensor coefficien... |

## `apf/w_trace_native_timelike_gauge_width.py` — 4 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_w_trace_native_timelike_W_optical_theorem` | theorem | `P` | The native absorptive part of Denner's fermionic Sigma^{WW}_T at p^2=M_W^2 satisfies Im Sigma^{WW}(M_W^2)/M_W = Gamma_W to ratio 1.0000000000 (massless open channels), with Gamma_W = (alpha M_W/12 s^2) N_open and N_open = 9 (3 lepton doublets + N_c x 2 open up-type quark channels; the top doublet... |
| · | `T_w_trace_native_timelike_Z_optical_theorem` | theorem | `P` | The native absorptive part of Denner's fermionic Sigma^{ZZ}_T at p^2=M_Z^2, built from the banked timelike Im B0 and the chiral Z couplings, satisfies the optical theorem Im Sigma^{ZZ}(M_Z^2)/M_Z = Gamma_Z to ratio 1.0000000000 (massless open channels), where Gamma_Z = sum_f N_c (alpha M_Z/6)(g+^... |
| · | `T_w_trace_native_timelike_gauge_width_scope_partial` | theorem | `P_structural_partial` | The absorptive (Im) parts of the timelike gauge-boson self-energies Sigma^{WW}_T(M_W^2)/Sigma^{ZZ}_T(M_Z^2) are now native, evaluated via the banked timelike Im B0 and validated by the optical theorem against the tree decay widths (unitarity, no measured input) with correct threshold gating. Stil... |
| · | `T_w_trace_native_timelike_threshold_structure` | theorem | `P` | The banked timelike Im B0 gates the absorptive part to OPEN channels only: Im B0(M_Z^2, m_t, m_t) = 0 (2 m_t > M_Z) and Im B0(M_W^2, m_t, m_b) = 0 (m_t + m_b > M_W), so the top contributes nothing to Im Sigma^{ZZ}/Sigma^{WW}, while every lighter fermion has Im B0 > 0. The native absorptive self-e... |

## `apf/w_trace_native_timelike_self_energy.py` — 4 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_w_trace_native_delta_alpha_lep_timelike` | theorem | `P` | The native fermion-loop photon self-energy, evaluated at the TIMELIKE on-shell point p^2 = M_Z^2 via the v24.3.84 timelike two-point branch, gives the leptonic running Delta alpha_lep = sum_l [Re Pihat_l(M_Z^2) - Pihat_l(0)] = 0.0314190, reproducing the banked one-loop delta_alpha_leptonic value ... |
| · | `T_w_trace_native_timelike_self_energy_scope_partial` | theorem | `P_structural_partial` | Stage 2's timelike validation anchor is closed: the native fermionic photon VP, evaluated at p^2 = M_Z^2 through the timelike two-point branch, reproduces the banked Delta alpha_lep, validated pointwise against the closed form and shown mu-independent. Both Stage-2 internal anchors (Delta rho_top... |
| · | `T_w_trace_native_vp_mu_independence` | theorem | `P` | Delta alpha_lep computed from the native subtracted VP is invariant under the renormalization scale mu^2 -> {1, 100, 1000} * MU2 (spread 4.8e-12). The bare transverse self-energy carries a 1/epsilon + ln mu^2 divergence proportional to p^2, so its form factor A_gamma/p^2 carries a p^2-independent... |
| · | `T_w_trace_native_vp_per_lepton_closed_form` | theorem | `P` | Each lepton's native subtracted running Re Pihat_l(M_Z^2) - Pihat_l(0) reproduces the analytic one-loop closed form (alpha_0/3pi)[ln(M_Z^2/m_l^2) - 5/3] to max rel err 3.7e-04 (e 5.0e-07, mu 1.5e-06, tau 3.7e-04). Because the analytic form carries no renormalization scale, the pointwise match sim... |

## `apf/w_trace_native_two_loop_phase2_bosonic_vertex_master_anchors.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_two_loop_phase2_bosonic_vertex_master_anchors_I4_I10` | theorem | `P_two_loop_phase2_bosonic_vertex_master_anchors_I4_I10` | Sibling-AI delivery via APF_TWO_LOOP_PHASE2_PUSH_BUNDLE_v5 / APF_TWO_LOOP_PHASE2_BOSONIC_VERTEX_MASTER_ANCHORS_v2. I4-I10 banked as named MasterAnchor records with pole_order (I4/I7 simple, I5/I8 double, I6/I9/I10 finite), leading_pole_coefficient and finite_part_symbolic strings, and numeric eva... |

## `apf/w_trace_native_two_loop_phase2_coefficient_output_slices.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_two_loop_phase2_coefficient_output_slices_current_depth` | theorem | `P_two_loop_phase2_coefficient_output_slices_current_depth` | Sibling-AI delivery via APF_TWO_LOOP_PHASE2_PUSH_BUNDLE_v10 (5 packs: TP5 native rational coefficient output, SUN3 DE coefficient output, ZFF_LIGHT LF1 coefficient output, BOSONIC ultrasoft coefficient output, status/next-gate; self-verifier 7/7 PASS). This module re-derives the TP5 numerator-exp... |

## `apf/w_trace_native_two_loop_phase2_coefficient_surface_no_smuggling.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_two_loop_phase2_coefficient_surface_no_smuggling_current_depth` | theorem | `—` | (no summary) |

## `apf/w_trace_native_two_loop_phase2_counterterm_residue_formula_ledger.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_two_loop_phase2_counterterm_residue_formula_ledger_current_depth` | theorem | `P_two_loop_phase2_counterterm_residue_formula_ledger_current_depth` | Sibling-AI delivery via APF_TWO_LOOP_PHASE2_PUSH_BUNDLE_v7 (5 packs: counterterm formula ledger + Z-pole NNLO residue evaluator + Δr/M_W validation grid + DIZET instrumentation harness + six-channel seed ledger; self-verifier 5/5 PASS). This module certifies the structural contract: all six requi... |

## `apf/w_trace_native_two_loop_phase2_current_source_coefficient_no_go.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_two_loop_phase2_current_source_coefficient_no_go` | theorem | `P_two_loop_phase2_current_source_coefficient_no_go` | Sibling-AI delivery via APF_TWO_LOOP_PHASE2_PUSH_BUNDLE_v5 / APF_TWO_LOOP_PHASE2_CURRENT_SOURCE_COEFFICIENT_NO_GO_v1. Strongest audit-first content in the Phase-2 arc: a decision matrix catalogues the 5 row families the currently uploaded sources actually deliver and explicitly DOES NOT promote a... |

## `apf/w_trace_native_two_loop_phase2_delta_r_source_import.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_two_loop_phase2_delta_r_source_import_v1` | theorem | `P_two_loop_phase2_delta_r_source_import_v1` | Sibling-AI delivery via APF_TWO_LOOP_PHASE2_PUSH_BUNDLE_v6 / APF_TWO_LOOP_PHASE2_DELTA_R_SOURCE_IMPORT_v1. Direct execution of v24.3.155 derivation plan Stage A/B: 4 named SourceClaim records (FHW 2000 fermionic Δr stack, FHW 2002 complex-pole/IR convention, AC 2002 bosonic matching+numeric ancho... |

## `apf/w_trace_native_two_loop_phase2_ew_coefficient_ledger_audit.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_two_loop_phase2_ew_coefficient_ledger_audit_scaffold` | theorem | `P_two_loop_phase2_ew_coefficient_ledger_audit_scaffold` | Sibling-AI delivery via APF_TWO_LOOP_PHASE2_PUSH_BUNDLE_v3 / APF_TWO_LOOP_PHASE2_EW_COEFFICIENT_LEDGER_AUDIT_v2. CoefficientRow schema fields: row_id, channel ∈ {Σ_W,Σ_Z,Π_γγ,Π_γZ}, diagram_class, topology ∈ {tadpole, sunset, two_point_5line, counterterm, vertex_box, ward_normalization, mixing_re... |

## `apf/w_trace_native_two_loop_phase2_ew_diagram_coefficient_derivation_engine_scaffold.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_two_loop_phase2_ew_diagram_coefficient_derivation_engine_scaffold_v1` | theorem | `P_two_loop_phase2_ew_diagram_coefficient_derivation_engine_scaffold_v1` | Sibling-AI delivery via APF_TWO_LOOP_PHASE2_PUSH_BUNDLE_v6 / APF_TWO_LOOP_PHASE2_EW_DIAGRAM_COEFFICIENT_DERIVATION_ENGINE_SCAFFOLD_v1. Executes v24.3.155 Stages C-G as a typed contract. REQUIRED_FAMILIES (8): the 4 EW self-energy channels Σ_W/Σ_Z/Π_γγ/Π_γZ + 2 vertex/box families (muon-decay, Z→ℓ... |

## `apf/w_trace_native_two_loop_phase2_ew_self_energy_assembly_gate.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_two_loop_phase2_ew_self_energy_assembly_gate_toy_ledger` | theorem | `P_two_loop_phase2_ew_self_energy_assembly_gate_toy_ledger` | Sibling-AI delivery via APF_TWO_LOOP_PHASE2_PUSH_BUNDLE_v1 / APF_TWO_LOOP_PHASE2_EW_SELF_ENERGY_ASSEMBLY_GATE_v1. Five components: (a) PoleSeries Laurent record with addition, scaling, finite-part extraction; (b) RenormalizationContract schema declaring scheme, μ², finite-part convention, subtrac... |

## `apf/w_trace_native_two_loop_phase2_ew_source_table_extraction.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_two_loop_phase2_ew_source_table_extraction_aggregate_and_convention` | theorem | `P_two_loop_phase2_ew_source_table_extraction_aggregate_and_convention` | Sibling-AI delivery via APF_TWO_LOOP_PHASE2_PUSH_BUNDLE_v4 / APF_TWO_LOOP_PHASE2_EW_SOURCE_TABLE_EXTRACTION_v1. Implements: (a) ACFW 2004 M_W parametrization with c1..c11 in two variants (full range and M_H ≥ 100 GeV); shift table reproduction M_H 100→200 = -41.4 MeV, mt+5.1 = +31 MeV, M_Z+2.1 = ... |

## `apf/w_trace_native_two_loop_phase2_ew_source_table_extraction_queue.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_two_loop_phase2_ew_source_table_extraction_queue` | theorem | `P_two_loop_phase2_ew_source_table_extraction_queue` | Sibling-AI delivery via APF_TWO_LOOP_PHASE2_PUSH_BUNDLE_v3 / APF_TWO_LOOP_PHASE2_EW_SOURCE_TABLE_EXTRACTION_QUEUE_v1. SourceTarget record carries key, source_title, authors, arxiv_id, primary_role, extraction_task, aggregate_only_guard, promoted_as_coefficient_source flags. Default queue holds ex... |

## `apf/w_trace_native_two_loop_phase2_ew_tex_source_exact_extraction.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_two_loop_phase2_ew_tex_source_exact_extraction_v2` | theorem | `P_two_loop_phase2_ew_tex_source_exact_extraction_v2` | Sibling-AI delivery via APF_TWO_LOOP_PHASE2_PUSH_BUNDLE_v5 / APF_TWO_LOOP_PHASE2_EW_TEX_SOURCE_EXACT_EXTRACTION_v2. 23 byte-level source windows with line ranges + SHA256 + the verbatim textual snippet preserved at the bundle. Promotion class is fixed exact_source_window_not_coefficient_row on ev... |

## `apf/w_trace_native_two_loop_phase2_fermionic_vertex_reduction_ledger.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_two_loop_phase2_fermionic_vertex_reduction_ledger` | theorem | `P_two_loop_phase2_fermionic_vertex_reduction_ledger` | Sibling-AI delivery via APF_TWO_LOOP_PHASE2_PUSH_BUNDLE_v5 / APF_TWO_LOOP_PHASE2_FERMIONIC_VERTEX_REDUCTION_LEDGER_v1. Five named FermionicReductionRow records: (1) top_large_mass — top-quark closed fermion loops via x = M_Z²/m_t² expansion to order x⁵, method_anchor; (2) light_LF1_DE — light-fer... |

## `apf/w_trace_native_two_loop_phase2_ibp_reduction_engine_tier0.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_two_loop_phase2_ibp_reduction_engine_tier0_current_depth` | theorem | `P_two_loop_phase2_ibp_reduction_engine_tier0_current_depth` | Sibling-AI delivery via APF_TWO_LOOP_PHASE2_PUSH_BUNDLE_v9 (5 packs: IBP reduction engine, Tier-0 reduced-row ledger, Laporta batch job specs, real-row cancellation/aggregate bridge, row-production status; self-verifier 5/5 PASS). This module re-derives the exact scalar-product → inverse-propagat... |

## `apf/w_trace_native_two_loop_phase2_master_interface_router.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_two_loop_phase2_master_interface_router_current_depth` | theorem | `P_two_loop_phase2_master_interface_router_current_depth` | Sibling-AI delivery via APF_TWO_LOOP_PHASE2_PUSH_BUNDLE_v1 / APF_TWO_LOOP_PHASE2_MASTER_INTERFACE_AND_REGION_ROUTER_v1. Routing kernel exports per-topology RouteDecision records with (topology, region, evaluator, status, promoted, reason, required_next_gate). Three families: (a) tadpole: q=0 scal... |

## `apf/w_trace_native_two_loop_phase2_missing_terms_source_and_derivation_plan.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_two_loop_phase2_missing_terms_source_and_derivation_plan` | theorem | `P_two_loop_phase2_missing_terms_source_map_and_derivation_plan` | Sibling-AI delivery via APF_TWO_LOOP_PHASE2_MISSING_TERMS_SOURCE_AND_DERIVATION_PLAN_v1. Direct follow-on to the v24.3.154 current-source no-go: names the 14 acquisition targets (5 Δr / muon-lifetime + 6 sin²θ_eff + 1 b̄b optional + 1 Denner convention-only + 1 ZFITTER forbidden-component); 7 gap... |

## `apf/w_trace_native_two_loop_phase2_osw_deltar_connector_refusal.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_two_loop_phase2_osw_deltar_connector_refusal_toy` | theorem | `P_two_loop_phase2_osw_deltar_connector_refusal_toy` | Sibling-AI delivery via APF_TWO_LOOP_PHASE2_PUSH_BUNDLE_v3 / APF_TWO_LOOP_PHASE2_OSW_DELTAR_CONNECTOR_AND_REFUSAL_v2. Three components: (a) FiniteComponent record carrying value, covariance, source_reference, convention_key, source_certified boolean, plus target/fitted refusal flags — validate() ... |

## `apf/w_trace_native_two_loop_phase2_p_plus_ibp_tool_admission_policy.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_two_loop_phase2_p_plus_ibp_tool_admission_policy` | theorem | `P_p_plus_ibp_tool_admission_policy` | Principal decision banked 2026-05-28 from the sibling-AI encoding in APF_TWO_LOOP_PHASE2_PUSH_BUNDLE_v26 / APF_TWO_LOOP_PHASE2_EVALUATOR_REDIRECT_AND_PIBP_LEDGER_v1. Establishes [P+IBP-tool] as a framework epistemic grade: an IBP reduction coefficient is determined algebra (a rational function fi... |

## `apf/w_trace_native_two_loop_phase2_projectors_preibp_router.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_two_loop_phase2_projectors_preibp_router_current_depth` | theorem | `P_two_loop_phase2_projectors_preibp_router_current_depth` | Sibling-AI delivery via APF_TWO_LOOP_PHASE2_PUSH_BUNDLE_v8 (5 packs: EW diagram generator + projectors, pre-IBP scalar row ledger, IBP master router + reduction contract, UV/IR/Ward cancellation testbench, row-production status; self-verifier 5/5 PASS). This module re-derives the exact-rational L... |

## `apf/w_trace_native_two_loop_phase2_zfitter_comparator_guard.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_two_loop_phase2_zfitter_comparator_guard_v1` | theorem | `P_two_loop_phase2_zfitter_comparator_guard_v1` | Sibling-AI delivery via APF_TWO_LOOP_PHASE2_PUSH_BUNDLE_v6 / APF_TWO_LOOP_PHASE2_ZFITTER_COMPARATOR_GUARD_v1. Closed-set role allowlist with 4 entries permitting ZFITTER/DIZET as black-box comparator, same-input total-evaluator audit reference, implementation_context for two-loop conventions, or ... |

## `apf/w_trace_native_two_loop_phase2_zpole_bosonic_deltakappa_import.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_two_loop_phase2_zpole_bosonic_deltakappa_import_v1` | theorem | `P_two_loop_phase2_zpole_bosonic_deltakappa_import_v1` | Sibling-AI delivery via APF_TWO_LOOP_PHASE2_PUSH_BUNDLE_v6 / APF_TWO_LOOP_PHASE2_ZPOLE_BOSONIC_DELTAKAPPA_IMPORT_v1. Imports the ACF 2006 hep-ph/0605339 bosonic Δκ + sin²θ_eff^bos aggregate shift tables across 4 M_H values plus the Hollik comparison sub-leading cross-check, all in 10⁻⁴ units. The... |

## `apf/w_trace_native_two_loop_phase2_zpole_form_factor_connector_dag.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_two_loop_phase2_zpole_form_factor_connector_dag` | theorem | `P_two_loop_phase2_zpole_form_factor_connector_dag` | Sibling-AI delivery via APF_TWO_LOOP_PHASE2_PUSH_BUNDLE_v5 / APF_TWO_LOOP_PHASE2_ZPOLE_FORM_FACTOR_CONNECTOR_DAG_v1. 12 typed nodes: pole anchor M̄_Z, one-loop self-energy derivatives Σ'_ZZ^(1), Σ''_ZZ^(1), Σ_γZ^(1), Σ'_γZ^(1); two-loop derivative Σ'_ZZ^(2); one- and two-loop form factors ẑ_f^(1)... |

## `apf/w_trace_native_two_loop_sunrise_2d_finite.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_two_loop_sunrise_2d_finite_core_and_boundary` | theorem | `P_two_loop_sunrise_2d_finite_core_and_boundary` | Sibling-AI delivery via APF_TWO_LOOP_PHASE1_CLOSURE_PUSH_BUNDLE_v2 / APF_NATIVE_TWO_LOOP_SUNSET_FINITE_CORE_AND_BOUNDARY_v2. Three-piece kernel: (a) ABW 2D Feynman-parameter quadrature S(p_E²; m_i²) = μ² ∫_σ ω/F_E with F_E = p_E² x1 x2 x3 + (Σ x_i m_i²) U via Gauss-Legendre on the unit square wit... |

## `apf/w_trace_native_two_loop_sunrise_de.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_two_loop_sunrise_DE_matrix_source_certified` | theorem | `P_source_certified_two_loop_sunrise_DE_matrix` | Sibling-AI delivery via APF_TWO_LOOP_PHASE1_PUSH_HARD_BUNDLE_v1 / APF_NATIVE_TWO_LOOP_SUNSET_DE_MATRIX_AND_ROUTER_v1. Three layers: (a) polynomial coefficients R²(a,b,c) and D(a,b,c,s) implementing CCLR Eq.(12)-(20) — both expanded and factored-over-threshold forms verified to agree at (1,1,1,s=5... |

## `apf/w_trace_native_two_loop_sunset.py` — 4 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_two_loop_sunset_DE_solver_with_threshold_branch` | theorem | `P_DE_solver_threshold_gate_two_loop_sunset` | Sibling delivery APF_NATIVE_TWO_LOOP_SUNSET_DE_SOLVER_WITH_THRESHOLD_BRANCH_v1 (verifier 37/37 PASS). Types the DE-solver scaffold; threshold-branch regions named (Smirnov 1991 hard-hard / Beneke-Smirnov 1998 potential-potential); F0/F1/F2/F3 system declared; p²=0 boundary tied to tadpole closure... |
| · | `T_two_loop_sunset_current_depth_certification` | theorem | `P_current_depth_two_loop_sunset_substrate` | Sibling cert pack APF_NATIVE_TWO_LOOP_SUNSET_CURRENT_DEPTH_CERTIFICATION_v1 (verifier 19/19 PASS). Records that v24.3.130 represents current sunset ladder depth; next gate is DE solver. |
| · | `T_two_loop_sunset_numeric_DE_master_attempt` | theorem | `C_two_loop_sunset_DE_numeric_master_attempt` | Sibling APF_NATIVE_TWO_LOOP_SUNSET_NUMERIC_DE_MASTER_P_ATTEMPT_v1 (verifier 7/7 PASS). Sibling RAN the DE-solver numeric attempt; scaffold validated (4-region regime classifier with branch-point detection, F0/F1/F2/F3 master basis schema, p²=0 boundary tied to tadpole closure via v24.3.124+.125);... |
| · | `T_two_loop_sunset_source_DE_and_threshold_gate` | theorem | `P_source_gate_two_loop_sunset_DE_threshold` | Sibling-AI Phase-1 Tier-1 SUNSET-LADDER first gate APF_NATIVE_TWO_LOOP_SUNSET_SOURCE_DE_AND_THRESHOLD_GATE_v1 (staged at DOCTRINE_CONSEQUENCES_BUNDLE_LATEST_44/). Verifier 31/31 PASS standalone. **First sunset pack** of the two-loop arc Phase-1 Tier-1 — mirrors v24.3.126 (bubble source+DC gate) a... |

## `apf/w_trace_native_two_loop_tadpole.py` — 3 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_two_loop_tadpole_chetyrkin_Eq1_full_form` | theorem | `P_chetyrkin_Eq1_full_form_two_loop_tadpole_scalar` | Sibling-AI delivery via APF_TWO_LOOP_PHASE1_PUSH_HARD_BUNDLE_v1 / APF_NATIVE_TWO_LOOP_TADPOLE_SCALAR_BANK_PUSH_v1. Provides the FULL Chetyrkin Eq.(1) normalization (mass-power factor + Γ-ratios + M(α,β,γ)) — extends v24.3.124's M-factor-only Chetyrkin implementation. Eq.(1) full form: (m²)^(D-α-β... |
| · | `T_two_loop_tadpole_connected_scalar_master_current_scope` | theorem | `P_two_loop_tadpole_scalar_connected_master_current_scope` | Sibling-AI Phase-1 Tier-1 closure-pack delivery APF_NATIVE_TWO_LOOP_TADPOLE_CONNECTED_MASTER_ASSEMBLY_v1 (staged at Codebase/DOCTRINE_CONSEQUENCES_BUNDLE_LATEST_44/). Verifier 16/16 PASS standalone. Connected scalar tadpole master assembled from three source-gated branches: all-massive unit-power... |
| · | `T_two_loop_tadpole_tier1_scalar_master_certification` | theorem | `P_two_loop_master_integral_tadpole_scalar_Tier1` | Sibling-AI Phase-1 Tier-1 grade-promotion delivery APF_NATIVE_TWO_LOOP_TADPOLE_TIER1_SCALAR_MASTER_CERTIFICATION_v1 (staged at DOCTRINE_CONSEQUENCES_BUNDLE_LATEST_44/). Verifier 11/11 PASS. Promotion event: the connected scalar tadpole master assembled by v24.3.124 (Export_two_loop_tadpole_connec... |

## `apf/w_trace_native_two_loop_tier1_status.py` — 2 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_two_loop_tier1_single_swing_capstone` | theorem | `P_tier1_single_swing_status` | Sibling-AI cross-cutting capstone APF_NATIVE_TWO_LOOP_TIER1_SINGLE_SWING_CAPSTONE_v1 (verifier 22/22 PASS, staged at DOCTRINE_CONSEQUENCES_BUNDLE_LATEST_44/). Records the Phase-1 Tier-1 sweep state across all three master integrals: 11 bank-side checks across 3 masters. Tadpole closed at Tier-1 m... |
| · | `T_two_loop_tier1_true_closure_attempt_capstone` | theorem | `P_tadpole_scalar_Tier1_available_with_C_two_point_sunset_attempted` | Sibling APF_NATIVE_TWO_LOOP_TIER1_TRUE_CLOSURE_ATTEMPT_CAPSTONE_v1 (verifier 4/4 PASS). Final true-closure attempt capstone for the Phase-1 Tier-1 sweep. After running all three master-integral attempts: ONLY the tadpole achieves scoped Tier-1 P (v24.3.125 grade promotion stands); the bubble + su... |

## `apf/w_trace_native_two_loop_two_point.py` — 7 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_two_loop_two_point_anchor_gate` | theorem | `P_two_loop_two_point_anchor_gate` | Sibling-AI Phase-1 Tier-1 bubble-ladder second gate APF_NATIVE_TWO_LOOP_TWO_POINT_MASSLESS_HIGH_ENERGY_AND_THRESHOLD_ANCHOR_v1 (staged at DOCTRINE_CONSEQUENCES_BUNDLE_LATEST_44/). Verifier 18/18 PASS standalone. Extends v24.3.126's source-formula + DOUBLE_COUNT_LEDGER gate with: (a) proper-branch... |
| · | `T_two_loop_two_point_branch_assembly_and_epsilon_pole_audit_gate` | theorem | `P_branch_assembly_gate_two_loop_two_point` | Sibling-AI Phase-1 Tier-1 bubble-ladder FOURTH gate APF_NATIVE_TWO_LOOP_TWO_POINT_MASTER_BRANCH_ASSEMBLY_AND_EPSILON_POLE_AUDIT_v1 (staged at DOCTRINE_CONSEQUENCES_BUNDLE_LATEST_44/). Verifier 27/27 PASS standalone (metadata + SHA256SUMS validation). This gate UNIFIES the three earlier bubble gat... |
| · | `T_two_loop_two_point_bubble_source_and_double_count_gate` | theorem | `P_source_formula_and_double_count_gate_two_loop_two_point_bubble` | Sibling-AI Phase-1 Tier-1 second-track delivery APF_NATIVE_TWO_LOOP_TWO_POINT_BUBBLE_SOURCE_AND_DOUBLE_COUNT_GATE_v1 (staged at DOCTRINE_CONSEQUENCES_BUNDLE_LATEST_44/). Verifier 18/18 PASS standalone. This is the FIRST step of the bubble ladder — source-formula binding + DOUBLE_COUNT discipline ... |
| · | `T_two_loop_two_point_coefficient_family_and_threshold_numeric_row` | theorem | `P_coefficient_family_threshold_anchor_two_loop_two_point` | Sibling delivery APF_NATIVE_TWO_LOOP_TWO_POINT_COEFFICIENT_FAMILY_AND_THRESHOLD_NUMERIC_ROW_v1 (verifier 34/34 PASS). Closes coefficient-family gate + threshold numeric-anchor row; retains v24.3.128 Padé bridge + v24.3.127 anchor; irreducible/reducible DOUBLE_COUNT guard active. Full numeric mast... |
| · | `T_two_loop_two_point_current_depth_certification` | theorem | `P_current_depth_two_loop_two_point_substrate` | Sibling cert pack APF_NATIVE_TWO_LOOP_TWO_POINT_CURRENT_DEPTH_CERTIFICATION_v1 (verifier 18/18 PASS). Records that the v24.3.126→.129 four-gate ladder represents the current achievable depth for the bubble; next gate is the master-coefficient implementation. |
| · | `T_two_loop_two_point_low_energy_pade_bridge_gate` | theorem | `P_two_loop_two_point_low_energy_pade_bridge_gate` | Sibling-AI Phase-1 Tier-1 bubble-ladder THIRD gate APF_NATIVE_TWO_LOOP_TWO_POINT_LOW_ENERGY_SERIES_AND_PADE_BRIDGE_v1 (staged at DOCTRINE_CONSEQUENCES_BUNDLE_LATEST_44/). Verifier 20/20 PASS standalone. Brackets v24.3.127's high-energy anchor (BFT 1993 leading-log at p² ≫ m²) with the small-q² Ta... |
| · | `T_two_loop_two_point_numeric_implementation_attempt` | theorem | `C_two_loop_two_point_current_depth_numeric_implementation_attempt` | Sibling APF_NATIVE_TWO_LOOP_TWO_POINT_TIER1_SCALAR_MASTER_NUMERIC_IMPLEMENTATION_v1 (verifier 8/8 PASS). Sibling RAN the numeric implementation attempt at master closure; scaffold validated (high-energy leading-log anchor + 3-region threshold classifier + reducible-topology rejection guard); but ... |

## `apf/w_trace_native_two_loop_two_point_bft_dst.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_two_loop_two_point_BFT_DST_coefficient_family_current_depth` | theorem | `P_two_point_BFT_DST_coefficient_family_current_depth` | Sibling-AI delivery via APF_TWO_LOOP_PHASE1_PUSH_HARD_BUNDLE_v1 / APF_NATIVE_TWO_LOOP_TWO_POINT_COEFFICIENT_FAMILY_IMPLEMENTATION_v1. Three integrated layers: (a) BFT 1993 one-mass normalized hypergeometric branches — N_I1 with mixed (1-eps)/(1-3eps) gamma structure, N_I2/N_I4/N_Ie3 with paper-ex... |

## `apf/w_trace_native_two_loop_two_point_euclidean_master.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_two_loop_two_point_5line_euclidean_master_arbitrary_mass` | theorem | `P_two_loop_two_point_5line_euclidean_master_arbitrary_mass` | Sibling-AI delivery via APF_TWO_LOOP_PHASE1_CLOSURE_PUSH_BUNDLE_v2 / APF_NATIVE_TWO_LOOP_TWO_POINT_EUCLIDEAN_MASTER_EVALUATOR_v2. Three-piece kernel: (a) explicit graph polynomials U_5 + K_5_external + F_5_euclidean for the 5-denominator (p,q,p-q,p-k,q-k) topology; (b) stick-breaking 4-cube → 4-s... |

## `apf/w_trace_native_uv_cancellation_stage4.py` — 4 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_w_trace_native_uv_cancel_drho_plus4_absorbed` | theorem | `P` | The v24.3.90 bare bosonic Delta rho pole (+4, reproduced here as 4.0000) is a bare-quantity artifact: once W and Z are OS-renormalized, Sigma_hat_WW and Sigma_hat_ZZ are UV-finite, so the bosonic Delta rho built from the RENORMALIZED self-energies is finite -- the +4 is exactly what delta M_W^2 /... |
| · | `T_w_trace_native_uv_cancel_os_renormalized_finite` | theorem | `P` | With the on-shell counterterms delta M_V^2 = Re Sigma_VV(M_V^2) and delta Z_V = -Re Sigma'_VV(M_V^2), the renormalized self-energy Sigma_hat_VV(p^2) = Sigma_VV(p^2) - delta M_V^2 + (p^2-M_V^2) delta Z_V has zero UV pole at all p^2 (max rel 5.4e-16) for the photon (full ferm+bos, massless so delta... |
| · | `T_w_trace_native_uv_cancel_poles_linear` | theorem | `P` | The UV-pole content P_VV(p^2) of Denner's Sigma^{AA}_T/Sigma^{WW}_T/Sigma^{ZZ}_T (bosonic, and full photon) is strictly linear in p^2 (relative second difference 5.9e-16): no p^4 and no 1/p^2 pole survives. In particular the (M^4/p^2)(B0(p^2)-B0(0)) terms in Sigma^{WW}_T are pole-free (the pole c... |
| · | `T_w_trace_native_uv_cancel_scope_partial` | theorem | `P_structural_partial` | The bosonic-sector (and full-photon) Stage-4 UV cancellation is native: the self-energy poles are linear in p^2 (renormalizable) and the OS mass + field counterterms render the renormalized self-energies UV-finite, removing the v24.3.90 bosonic Delta rho +4 divergence. Still OPEN toward Delta r_r... |

## `apf/w_trace_native_uv_pole.py` — 4 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_w_trace_native_photon_vp_pole_beta_function` | theorem | `P` | The bare fermion-loop photon-VP bracket pole is purely transverse (bracket_pole/p^2 = (4/3)e^2, constant and mass-independent to 4e-13) -- the Ward identity at the divergent level. The assembled form-factor pole sum_f -(N_c/16pi^2) bracket_pole/p^2 = -(e^2/12pi^2) sum_f N_c Q^2 with sum_f N_c Q^2... |
| · | `T_w_trace_native_uv_pole_coeffs_match_mu_running` | theorem | `P` | The exact UV-pole coefficients A0->m^2, B0->1, B1->-1/2, B11->1/3, B00->(m0^2+m1^2)/4 - p^2/12 each equal the renormalization-scale slope d X_fin/d ln(mu^2) of the corresponding banked finite function (a0_fin + native re_b*_timelike), to max rel 1.1e-08 by finite difference. This ties the new pol... |
| · | `T_w_trace_native_uv_pole_scope_partial` | theorem | `P_structural_partial` | Prerequisite B of the native OS-W evaluator is in place: the PV toolkit now carries exact UV-pole coefficients (A0/B0/B1/B11/B00), validated against the mu-running of the banked finite functions, against the pole-level trace relation, and against the one-loop QED beta-function via the fermionic p... |
| · | `T_w_trace_native_uv_pole_trace_relation` | theorem | `P` | At the pole level the finite constant in the rank-2 trace relation drops and it reads 4 B00_pole + p^2 B11_pole = A0_pole(m1^2) + m0^2 B0_pole, which holds identically (max \|LHS-RHS\| 5.7e-14) over spacelike and timelike test points -- the pole coefficients of B00/B11 are mutually consistent with ... |

## `apf/w_trace_native_zll_R2_counterterm_pieces.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_w_trace_native_zll_R2_counterterm_pieces` | theorem | `P_structural_partial` | Wrapper module over the banked v24.3.99 Denner OS scheme. Exposes four self-energy-derived counterterms (delta_Z2_Z = 3.259927e-03, delta_Z2_gamma = -6.681335e-02, delta_Z_AZ = -1.093592e-03, delta_Z_e = -3.369946e-02) plus the composed Z-vertex counterterm (delta_Z1_Z = 2.238768e-03) at standard... |

## `apf/w_trace_native_zll_kappa_l_oblique.py` — 5 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `L_w_trace_native_kappa_l_proper_vertex_open` | lemma | `C` | THE SURVIVING NAMED-OPEN (re-cut v24.3.361): of the canonical slot budget +0.017590 (= all-orders import 0.036808 - custodial 0.021721 - effva gamma-Z -0.002503), the vertex component +0.003453 is CLOSED (the .361 fill, ACFW-gated -- see T_w_trace_native_kappa_l_vertex_component_closed); the resi... |
| · | `T_w_trace_native_kappa_l_custodial_consistent` | theorem | `P` | The oblique assembly reuses the banked custodial leading term Xi_rho*Delta rho = 0.021721 [P, v24.3.67] and the banked target Delta kappa_l = 0.036808, so the oblique kappa_l is built on the validated decomposition, not a new fit. |
| · | `T_w_trace_native_kappa_l_gammaZ_mixing` | theorem | `P_structural_partial` | The DFGRU-recipe gamma-Z-mixing evaluation, Dkappa_gammaZ = (c/s) Re[Sigma^gZ(M_Z^2)/M_Z^2] = 0.001483, computed natively from the banked total (fermionic+bosonic) gamma-Z self-energy (w_trace_native_delta_r_mw_assembly.Sig_AZ at the Z pole), sign sourced from arXiv:1906.08815 eq 1.1/1.2, not rec... |
| · | `T_w_trace_native_kappa_l_oblique_assembly` | theorem | `P_structural_partial` | Oblique Delta kappa_l in BOTH bookings of the same banked Sig_AZ object (booking adjudicated 2026-07-03: effva CANONICAL). CANONICAL: custodial (banked 0.021721) + effva gamma-Z (-0.002503) = 0.019218 = 52.2% of the banked target 0.036808; canonical remainder 0.017590 (Delta-alpha/light-fermion l... |
| · | `T_w_trace_native_kappa_l_vertex_component_closed` | theorem | `P_structural_vertex_component_effva_canonical_ruling_ACFW_benchmark_gated` | THE FILL (v24.3.361): Dk_vertex = +0.003452700 at the banked-OS deck (sW2 = 0.223339, alpha(M_Z) = 1/128.21); ACFW-deck cross-value +0.003247798 (the .360 headline '+0.0032'); both pinned -- the ~6% deck spread is alpha/sW2 frame, part of the claim. Extraction: the F_V/F_A-only shift of g_V/g_A a... |

## `apf/w_trace_native_zll_vertex_form_factors.py` — 5 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_w_trace_native_vertex_ff_Va_matches_denner_closed_form` | theorem | `P` | The native haba3 generic vertex form factor V_a(0,k^2,0,M,0,0) reproduces Denner's own hab6 special-case closed form (-2k^2 C0(1+M^2/k^2)^2 - B0(k^2,0,0)(3+2M^2/k^2) + 2 B0(0,M,0)(2+M^2/k^2) - 2) to max rel err 1.70e-03, mesh-converging (coarse 5.46e-04 -> fine 3.28e-04). Source-internal, target-... |
| · | `T_w_trace_native_vertex_ff_Vb_matches_denner_closed_form` | theorem | `P` | The native haba3 generic vertex form factor V_b^-(0,k^2,0,0,M1,M2) reproduces Denner's own hab6 special-case closed form (2(M1^2+M2^2+M1^2 M2^2/k^2)C0 - (1+(M1^2+M2^2)/k^2)B0(k^2,M1,M2) + (2+M1^2/k^2)B0(0,0,M1) + (2+M2^2/k^2)B0(0,0,M2)) to max rel err 3.40e-04. A second independent source-interna... |
| · | `T_w_trace_native_vertex_ff_convention_map` | theorem | `P` | The Denner-convention three-point wrapper (C0_D..C22_D over the banked native general-momentum toolkit) is validated two ways: C0_D at zero external momentum reproduces the native zero-momentum C0 exactly, and the rank-2 wrapper satisfies Denner's own haba3 explicit C00 reduction to max rel err 1... |
| · | `T_w_trace_native_vertex_ff_qed_schwinger_anchor` | theorem | `P` | The on-shell QED photon-fermion magnetic (Pauli) form factor F_2(0), evaluated on the same Feynman-simplex quadrature engine that carries the native vertex form factors, reproduces Schwinger's anomalous magnetic moment a_e = alpha/(2 pi) = 0.001161410 (F_2(0)/(a/2pi) = 1.000000). The gold-standar... |
| · | `T_w_trace_native_vertex_ff_subgate_partial` | theorem | `P_structural_partial` | The native generic vertex form-factor layer (Denner App. C / haba3: V_a, V_b^+-, on the Denner-convention three-point wrapper) is in place and anchored on Denner's own hab6 closed forms + the QED Schwinger term. The physical Zll vertex assembly (Lambda_V/Lambda_S), the native kappa_l evaluation, ... |

## `apf/w_trace_next_payload_requirements.py` — 13 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_w_trace_next_payload_requirements_apf_target_rejected` | theorem | `—` | (no summary) |
| · | `T_w_trace_next_payload_requirements_bank_closure` | theorem | `—` | (no summary) |
| · | `T_w_trace_next_payload_requirements_eight_components_required` | theorem | `—` | (no summary) |
| · | `T_w_trace_next_payload_requirements_export_locked` | theorem | `—` | (no summary) |
| · | `T_w_trace_next_payload_requirements_forbidden_sources_declared` | theorem | `—` | (no summary) |
| · | `T_w_trace_next_payload_requirements_mapping_guide_declared` | theorem | `—` | (no summary) |
| · | `T_w_trace_next_payload_requirements_observed_w_rejected` | theorem | `—` | (no summary) |
| · | `T_w_trace_next_payload_requirements_payload_requirements_declared` | theorem | `—` | (no summary) |
| · | `T_w_trace_next_payload_requirements_payload_requirements_serializable` | theorem | `—` | (no summary) |
| · | `T_w_trace_next_payload_requirements_physics_phase_actions_declared` | theorem | `—` | (no summary) |
| · | `T_w_trace_next_payload_requirements_real_rows_required_before_more_scaffolding` | theorem | `—` | (no summary) |
| · | `T_w_trace_next_payload_requirements_source_classes_declared` | theorem | `—` | (no summary) |
| · | `T_w_trace_next_payload_requirements_status_declared` | theorem | `—` | (no summary) |

## `apf/w_trace_numeric_source_adapter.py` — 19 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_w_numeric_source_adapter_allowed_source_classes_declared` | theorem | `—` | (no summary) |
| · | `T_w_numeric_source_adapter_bank_closure` | theorem | `—` | (no summary) |
| · | `T_w_numeric_source_adapter_codomain_not_physical_export` | theorem | `—` | (no summary) |
| · | `T_w_numeric_source_adapter_completion_gate_remains_locked` | theorem | `—` | (no summary) |
| · | `T_w_numeric_source_adapter_contract_export_shape` | theorem | `—` | (no summary) |
| · | `T_w_numeric_source_adapter_covers_all_components` | theorem | `—` | (no summary) |
| · | `T_w_numeric_source_adapter_depends_on_v96_skeleton` | theorem | `—` | (no summary) |
| · | `T_w_numeric_source_adapter_forbids_apf_target_as_input` | theorem | `—` | (no summary) |
| · | `T_w_numeric_source_adapter_forbids_observed_W_inputs` | theorem | `—` | (no summary) |
| · | `T_w_numeric_source_adapter_next_requirements_explicit` | theorem | `—` | (no summary) |
| · | `T_w_numeric_source_adapter_no_component_sum_certification_yet` | theorem | `—` | (no summary) |
| · | `T_w_numeric_source_adapter_payload_predicate_accepts_independent_shape` | theorem | `—` | (no summary) |
| · | `T_w_numeric_source_adapter_payload_predicate_rejects_apf_target_consumption` | theorem | `—` | (no summary) |
| · | `T_w_numeric_source_adapter_payload_predicate_rejects_target_backsolve` | theorem | `—` | (no summary) |
| · | `T_w_numeric_source_adapter_publication_ladder` | theorem | `—` | (no summary) |
| · | `T_w_numeric_source_adapter_schema_complete` | theorem | `—` | (no summary) |
| · | `T_w_numeric_source_adapter_slots_unfilled_by_default` | theorem | `—` | (no summary) |
| · | `T_w_numeric_source_adapter_status_declared` | theorem | `P_w_numeric_source_adapter` | (no summary) |
| · | `T_w_numeric_source_adapter_symbols_match_skeleton` | theorem | `—` | (no summary) |

## `apf/w_trace_onshell_transport.py` — 13 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_w_trace_completion_gate_remains_locked` | theorem | `P_w_trace_contract` | The v8.9 export gate remains locked for W_TRACE after v9.0 contract closure. |
| · | `T_w_trace_contract_schema_complete` | theorem | `P_w_trace_contract` | The W contract schema separates target declaration, evaluated maps, and physical export. |
| · | `T_w_trace_contract_status_declared` | theorem | `P_w_trace_contract` | The next concrete route is W_TRACE -> on-shell contract closure; the export gate remains locked. |
| · | `T_w_trace_counterterm_slots_subset_of_transport_ledger` | theorem | `P_w_trace_contract` | W route finite-part/counterterm slots reuse the banked transport ledger. |
| · | `T_w_trace_external_slots_subset_of_transport_ledger` | theorem | `P_w_trace_contract` | W route external constants are a subset of the existing transport ledger, not new hidden inputs. |
| · | `T_w_trace_input_basis_slots_declared_unfilled` | theorem | `P_w_trace_contract` | The W route can now name its input-basis choices without importing numerical EW constants or target M_W. |
| · | `T_w_trace_local_input_preserved` | theorem | `P_w_trace_contract` | v9.0 preserves M_W^TRACE as an upstream local trace value, not a physical on-shell mass. |
| · | `T_w_trace_no_target_MW_observable_consumed` | theorem | `P_w_trace_contract` | Observed M_W and W residuals are explicitly forbidden as transport inputs. |
| · | `T_w_trace_on_shell_contract_bank_closure` | theorem | `P_w_trace_contract` | W_TRACE on-shell route contract is banked; terminal physical W transport remains open and gated. |
| · | `T_w_trace_on_shell_target_contract_declared` | theorem | `P_w_trace_contract` | The W on-shell target is declared as a contract, not as an evaluated physical prediction. |
| · | `T_w_trace_radiative_conversion_slots_declared_unevaluated` | theorem | `P_w_trace_contract` | The W finite-conversion route is explicit but remains unevaluated. |
| · | `T_w_trace_route_selected_from_completion_order` | theorem | `P_w_trace_contract` | The W_TRACE route is selected because it is the least-burden terminal transport path. |
| · | `T_w_trace_uncertainty_protocol_declared_not_evaluated` | theorem | `P_w_trace_contract` | The W route now has a required uncertainty protocol slot, but no comparison claim is made. |

## `apf/w_trace_payload_fixture.py` — 20 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_w_payload_fixture_bank_closure` | theorem | `—` | (no summary) |
| · | `T_w_payload_fixture_checksum_locator_required` | theorem | `—` | (no summary) |
| · | `T_w_payload_fixture_codomain_not_physical_export` | theorem | `—` | (no summary) |
| · | `T_w_payload_fixture_completion_gate_remains_locked` | theorem | `—` | (no summary) |
| · | `T_w_payload_fixture_covers_all_components` | theorem | `—` | (no summary) |
| · | `T_w_payload_fixture_depends_on_v97_adapter` | theorem | `—` | (no summary) |
| · | `T_w_payload_fixture_empty_table_rejected_by_admission` | theorem | `—` | (no summary) |
| · | `T_w_payload_fixture_manifest_schema_complete` | theorem | `—` | (no summary) |
| · | `T_w_payload_fixture_no_component_sum_certification_yet` | theorem | `—` | (no summary) |
| · | `T_w_payload_fixture_numeric_parse_policy_declared` | theorem | `—` | (no summary) |
| · | `T_w_payload_fixture_positive_shape_table_admissible` | theorem | `—` | (no summary) |
| · | `T_w_payload_fixture_rejects_apf_anchor_consumption_rows` | theorem | `—` | (no summary) |
| · | `T_w_payload_fixture_rejects_duplicate_components` | theorem | `—` | (no summary) |
| · | `T_w_payload_fixture_rejects_observed_W_consumption_rows` | theorem | `—` | (no summary) |
| · | `T_w_payload_fixture_rejects_target_backsolve_rows` | theorem | `—` | (no summary) |
| · | `T_w_payload_fixture_rejects_unknown_components` | theorem | `—` | (no summary) |
| · | `T_w_payload_fixture_requires_full_component_coverage` | theorem | `—` | (no summary) |
| · | `T_w_payload_fixture_rows_unfilled_by_default` | theorem | `—` | (no summary) |
| · | `T_w_payload_fixture_status_declared` | theorem | `P_w_payload_fixture` | (no summary) |
| · | `T_w_payload_fixture_symbols_match_skeleton` | theorem | `—` | (no summary) |

## `apf/w_trace_payload_import_cli.py` — 28 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_w_payload_import_cli_apf_anchor_consumption_rejected` | theorem | `P_w_payload_import_cli_loader` | (no summary) |
| · | `T_w_payload_import_cli_attested_shape_still_no_physical_export` | theorem | `P_w_payload_import_cli_loader` | (no summary) |
| · | `T_w_payload_import_cli_bank_closure` | theorem | `—` | (no summary) |
| · | `T_w_payload_import_cli_bundle_report_stays_unadmitted_for_fixture` | theorem | `P_w_payload_import_cli_loader` | (no summary) |
| · | `T_w_payload_import_cli_csv_fixture_loads_rows` | theorem | `P_w_payload_import_cli_loader` | (no summary) |
| · | `T_w_payload_import_cli_csv_fixture_not_promoted_to_real` | theorem | `P_w_payload_import_cli_loader` | (no summary) |
| · | `T_w_payload_import_cli_current_flags_false` | theorem | `P_w_payload_import_cli_loader` | (no summary) |
| · | `T_w_payload_import_cli_default_absence_certificate_locked` | theorem | `P_w_payload_import_cli_loader` | (no summary) |
| · | `T_w_payload_import_cli_depends_on_v103_attempt_gate` | theorem | `—` | (no summary) |
| · | `T_w_payload_import_cli_depends_on_v109_bundle_gate` | theorem | `—` | (no summary) |
| · | `T_w_payload_import_cli_depends_on_v112_readiness` | theorem | `P_w_payload_import_cli_loader` | (no summary) |
| · | `T_w_payload_import_cli_explicit_format_enforced` | theorem | `P_w_payload_import_cli_loader` | (no summary) |
| · | `T_w_payload_import_cli_forbidden_consumption_rejected` | theorem | `P_w_payload_import_cli_loader` | (no summary) |
| · | `T_w_payload_import_cli_forbidden_fields_named` | theorem | `P_w_payload_import_cli_loader` | (no summary) |
| · | `T_w_payload_import_cli_forbids_physical_export_request` | theorem | `P_w_payload_import_cli_loader` | (no summary) |
| · | `T_w_payload_import_cli_infers_csv_format` | theorem | `P_w_payload_import_cli_loader` | (no summary) |
| · | `T_w_payload_import_cli_infers_json_format` | theorem | `P_w_payload_import_cli_loader` | (no summary) |
| · | `T_w_payload_import_cli_json_fixture_loads_rows` | theorem | `P_w_payload_import_cli_loader` | (no summary) |
| · | `T_w_payload_import_cli_json_fixture_not_promoted_to_real` | theorem | `P_w_payload_import_cli_loader` | (no summary) |
| · | `T_w_payload_import_cli_manifest_contains_absence_certificate` | theorem | `P_w_payload_import_cli_loader` | (no summary) |
| · | `T_w_payload_import_cli_missing_file_fails_closed` | theorem | `P_w_payload_import_cli_loader` | (no summary) |
| · | `T_w_payload_import_cli_parse_error_fails_closed` | theorem | `P_w_payload_import_cli_loader` | (no summary) |
| · | `T_w_payload_import_cli_readiness_remains_locked_after_load` | theorem | `P_w_payload_import_cli_loader` | (no summary) |
| · | `T_w_payload_import_cli_rejects_unknown_extension` | theorem | `P_w_payload_import_cli_loader` | (no summary) |
| · | `T_w_payload_import_cli_report_schema_declared` | theorem | `P_w_payload_import_cli_loader` | (no summary) |
| · | `T_w_payload_import_cli_review_required_for_real_claim` | theorem | `P_w_payload_import_cli_loader` | (no summary) |
| · | `T_w_payload_import_cli_status_declared` | theorem | `P_w_payload_import_cli_loader` | (no summary) |
| · | `T_w_payload_import_cli_supported_formats_match_parser_path` | theorem | `P_w_payload_import_cli_loader` | (no summary) |

## `apf/w_trace_payload_source_pack.py` — 23 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_w_payload_source_pack_bank_closure` | theorem | `—` | (no summary) |
| · | `T_w_payload_source_pack_codomain_not_physical_export` | theorem | `—` | (no summary) |
| · | `T_w_payload_source_pack_completion_gate_remains_locked` | theorem | `—` | (no summary) |
| · | `T_w_payload_source_pack_covers_all_components` | theorem | `—` | (no summary) |
| · | `T_w_payload_source_pack_depends_on_v98_fixture` | theorem | `—` | (no summary) |
| · | `T_w_payload_source_pack_empty_by_default` | theorem | `—` | (no summary) |
| · | `T_w_payload_source_pack_empty_rows_rejected` | theorem | `—` | (no summary) |
| · | `T_w_payload_source_pack_forbidden_inputs_superset_adapter` | theorem | `—` | (no summary) |
| · | `T_w_payload_source_pack_manifest_export_shape` | theorem | `—` | (no summary) |
| · | `T_w_payload_source_pack_no_component_sum_certification_yet` | theorem | `—` | (no summary) |
| · | `T_w_payload_source_pack_rejects_apf_anchor_consumption` | theorem | `—` | (no summary) |
| · | `T_w_payload_source_pack_rejects_delta_r_residual_fit` | theorem | `—` | (no summary) |
| · | `T_w_payload_source_pack_rejects_duplicate_components` | theorem | `—` | (no summary) |
| · | `T_w_payload_source_pack_rejects_missing_components` | theorem | `—` | (no summary) |
| · | `T_w_payload_source_pack_rejects_observed_W_consumption` | theorem | `—` | (no summary) |
| · | `T_w_payload_source_pack_rejects_unknown_components` | theorem | `—` | (no summary) |
| · | `T_w_payload_source_pack_rejects_unreviewed_numeric_rows` | theorem | `—` | (no summary) |
| · | `T_w_payload_source_pack_requires_license_or_access_note` | theorem | `—` | (no summary) |
| · | `T_w_payload_source_pack_requires_provenance_chain` | theorem | `—` | (no summary) |
| · | `T_w_payload_source_pack_reviewed_shape_rows_admissible` | theorem | `—` | (no summary) |
| · | `T_w_payload_source_pack_schema_extends_fixture_and_adapter` | theorem | `—` | (no summary) |
| · | `T_w_payload_source_pack_status_declared` | theorem | `P_w_payload_source_pack` | (no summary) |
| · | `T_w_payload_source_pack_symbols_match_skeleton` | theorem | `—` | (no summary) |

## `apf/w_trace_payload_template_pack.py` — 26 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_w_payload_template_pack_bank_closure` | theorem | `—` | (no summary) |
| · | `T_w_payload_template_pack_component_order_preserved_csv` | theorem | `P_w_payload_template_pack` | (no summary) |
| · | `T_w_payload_template_pack_component_order_preserved_json` | theorem | `P_w_payload_template_pack` | (no summary) |
| · | `T_w_payload_template_pack_csv_loader_path_works` | theorem | `P_w_payload_template_pack` | (no summary) |
| · | `T_w_payload_template_pack_csv_shape_not_real_payload` | theorem | `P_w_payload_template_pack` | (no summary) |
| · | `T_w_payload_template_pack_csv_template_parses` | theorem | `P_w_payload_template_pack` | (no summary) |
| · | `T_w_payload_template_pack_depends_on_v101_parser` | theorem | `—` | (no summary) |
| · | `T_w_payload_template_pack_depends_on_v113_loader` | theorem | `—` | (no summary) |
| · | `T_w_payload_template_pack_digests_declared` | theorem | `P_w_payload_template_pack` | (no summary) |
| · | `T_w_payload_template_pack_directory_exists` | theorem | `P_w_payload_template_pack` | (no summary) |
| · | `T_w_payload_template_pack_format_inference_for_templates` | theorem | `P_w_payload_template_pack` | (no summary) |
| · | `T_w_payload_template_pack_json_csv_digests_distinct` | theorem | `P_w_payload_template_pack` | (no summary) |
| · | `T_w_payload_template_pack_json_loader_path_works` | theorem | `P_w_payload_template_pack` | (no summary) |
| · | `T_w_payload_template_pack_json_shape_not_real_payload` | theorem | `P_w_payload_template_pack` | (no summary) |
| · | `T_w_payload_template_pack_json_template_parses` | theorem | `P_w_payload_template_pack` | (no summary) |
| · | `T_w_payload_template_pack_manifest_has_absence_logic` | theorem | `P_w_payload_template_pack` | (no summary) |
| · | `T_w_payload_template_pack_no_forbidden_consumption_csv` | theorem | `P_w_payload_template_pack` | (no summary) |
| · | `T_w_payload_template_pack_no_forbidden_consumption_json` | theorem | `P_w_payload_template_pack` | (no summary) |
| · | `T_w_payload_template_pack_physical_export_request_still_blocked` | theorem | `P_w_payload_template_pack` | (no summary) |
| · | `T_w_payload_template_pack_readiness_remains_locked` | theorem | `P_w_payload_template_pack` | (no summary) |
| · | `T_w_payload_template_pack_readme_warns_shape_only` | theorem | `P_w_payload_template_pack` | (no summary) |
| · | `T_w_payload_template_pack_required_files_exist` | theorem | `P_w_payload_template_pack` | (no summary) |
| · | `T_w_payload_template_pack_review_attestation_still_no_export` | theorem | `P_w_payload_template_pack` | (no summary) |
| · | `T_w_payload_template_pack_status_declared` | theorem | `P_w_payload_template_pack` | (no summary) |
| · | `T_w_payload_template_pack_templates_do_not_certify_sum` | theorem | `P_w_payload_template_pack` | (no summary) |
| · | `T_w_payload_template_pack_templates_do_not_export_physical_mw` | theorem | `P_w_payload_template_pack` | (no summary) |

## `apf/w_trace_physical_export_lock.py` — 25 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_w_physical_export_lock_bank_closure` | theorem | `—` | (no summary) |
| · | `T_w_physical_export_lock_completion_gate_still_locked` | theorem | `—` | (no summary) |
| · | `T_w_physical_export_lock_default_locked` | theorem | `—` | (no summary) |
| · | `T_w_physical_export_lock_depends_on_uncertainty_harness` | theorem | `—` | (no summary) |
| · | `T_w_physical_export_lock_dry_positive_predicate_true_but_no_export` | theorem | `—` | (no summary) |
| · | `T_w_physical_export_lock_no_physical_mass_exports` | theorem | `—` | (no summary) |
| · | `T_w_physical_export_lock_policy_blocks_smuggling` | theorem | `—` | (no summary) |
| · | `T_w_physical_export_lock_preserves_W_TRACE_as_anchor_not_export` | theorem | `—` | (no summary) |
| · | `T_w_physical_export_lock_preserves_apf_delta_r_as_comparison_only` | theorem | `—` | (no summary) |
| · | `T_w_physical_export_lock_rejects_apf_anchor_as_input` | theorem | `—` | (no summary) |
| · | `T_w_physical_export_lock_rejects_export_request_when_locked` | theorem | `—` | (no summary) |
| · | `T_w_physical_export_lock_rejects_identity_transport` | theorem | `—` | (no summary) |
| · | `T_w_physical_export_lock_rejects_observed_w_input` | theorem | `—` | (no summary) |
| · | `T_w_physical_export_lock_rejects_residual_fit_input` | theorem | `—` | (no summary) |
| · | `T_w_physical_export_lock_rejects_world_average_input` | theorem | `—` | (no summary) |
| · | `T_w_physical_export_lock_requires_component_sum` | theorem | `—` | (no summary) |
| · | `T_w_physical_export_lock_requires_counterterm_convention` | theorem | `—` | (no summary) |
| · | `T_w_physical_export_lock_requires_covariance` | theorem | `—` | (no summary) |
| · | `T_w_physical_export_lock_requires_no_target_observable_consumption` | theorem | `—` | (no summary) |
| · | `T_w_physical_export_lock_requires_real_rows` | theorem | `—` | (no summary) |
| · | `T_w_physical_export_lock_requires_target_scheme_contract` | theorem | `—` | (no summary) |
| · | `T_w_physical_export_lock_requires_uncertainty` | theorem | `—` | (no summary) |
| · | `T_w_physical_export_lock_schema_declared` | theorem | `—` | (no summary) |
| · | `T_w_physical_export_lock_status_declared` | theorem | `—` | (no summary) |
| · | `T_w_physical_export_lock_uncertainty_absence_blocks_release` | theorem | `—` | (no summary) |

## `apf/w_trace_physics_source_stop_condition.py` — 13 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_w_trace_physics_source_stop_condition_allowed_order_refines_last` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_physics_source_stop_condition_allows_payload_ingestion` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_physics_source_stop_condition_allows_source_acquisition` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_physics_source_stop_condition_bank_closure` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_physics_source_stop_condition_forbids_export` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_physics_source_stop_condition_forbids_more_scaffold` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_physics_source_stop_condition_forbids_observed_w` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_physics_source_stop_condition_forbids_target_fit` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_physics_source_stop_condition_locked_no_export` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_physics_source_stop_condition_report_clean` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_physics_source_stop_condition_requires_real_payload` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_physics_source_stop_condition_status_declared` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_physics_source_stop_condition_stop_active` | theorem | `—` | (no summary) |

## `apf/w_trace_prediction_cluster_robustness.py` — 13 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_w_trace_cluster_robust_apf_above_cluster` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_cluster_robust_band_green` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_cluster_robust_bank_closure` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_cluster_robust_export_lock_preserved` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_cluster_robust_floor_8_computed` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_cluster_robust_floor_scan_has_five` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_cluster_robust_floor_zero_computed` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_cluster_robust_four_points` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_cluster_robust_max_gap_under_6MeV` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_cluster_robust_max_pull_under_1p6` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_cluster_robust_no_export` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_cluster_robust_status_declared` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_cluster_robust_subset_scan_nonempty` | theorem | `—` | (no summary) |

## `apf/w_trace_publication_claim_language.py` — 13 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_w_trace_claim_language_all_allowed_safe` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_claim_language_allowed_nonempty` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_claim_language_bank_closure` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_claim_language_export_lock_preserved` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_claim_language_forbidden_nonempty` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_claim_language_forbids_observed_input` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_claim_language_forbids_physical_prediction` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_claim_language_mentions_validation_not_export` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_claim_language_no_component_certification_claim` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_claim_language_no_export` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_claim_language_preferred_mentions_green_or_few_mev` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_claim_language_preferred_sentence_safe` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_claim_language_status_declared` | theorem | `—` | (no summary) |

## `apf/w_trace_pv_c0_general_momentum.py` — 4 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_w_trace_pv_c0_general_mesh_consistency` | theorem | `P` | The C0 simplex quadrature is mesh-converged: n=150 vs n=300 agree to max relative err 4.91e-06, confirming the numerical evaluation is stable in the spacelike domain. |
| · | `T_w_trace_pv_c0_general_permutation_symmetry` | theorem | `P` | The native general-momentum C0 is invariant under cyclic and reflection permutations of the (mass, invariant) labels to max relative err 1.18e-05 -- a target-free validation of the F momentum<->mass pairing structure. |
| · | `T_w_trace_pv_c0_general_subgate_partial` | theorem | `P_structural_partial` | The native scalar substrate is extended from zero-momentum-only C0 to general-momentum spacelike C0 (with a domain quarantine for above-threshold/complex kinematics) -- the prerequisite for 3-point (vertex) tensor reduction. The 3-point tensor coefficients Cij, the 4-point Dij, the above-threshol... |
| · | `T_w_trace_pv_c0_general_zero_momentum_limit` | theorem | `P` | The native general-momentum C0 reduces, at vanishing external invariants, to the banked c0_fin_zero_momenta to max relative err 7.06e-07 -- ties the new evaluator to the banked substrate. |

## `apf/w_trace_pv_cij_three_point.py` — 6 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_w_trace_pv_c1_c2_mesh_consistency` | theorem | `P` | Direct C1,C2 quadrature mesh-converged: n=150 vs n=300 to 1.73e-05. |
| · | `T_w_trace_pv_c1_c2_reduction_matches_direct` | theorem | `P` | Rank-1 C1,C2 from the PV Gram reduction (contraction identities, banked B0 sub-bubbles + native C0) agree with the direct Feynman integral to max relative err 7.28e-06. |
| · | `T_w_trace_pv_c_tensor_subgate_partial` | theorem | `P_structural_partial` | The native three-point tensor basis is complete through rank 2 (C1,C2,C00,C11,C12,C22), built on the general-momentum C0 + banked B0/B1. The 4-point Dij, the above-threshold branch, the Denner coefficient map, and the self-energy/counterterm assembly remain OPEN; no Delta r_rem / M_W is produced;... |
| · | `T_w_trace_pv_cij_rank2_contraction_identity` | theorem | `P` | The native rank-2 Cij satisfy the p1.p1 scalar contraction identity (p1_mu p1_nu C^{mu nu} expressed through the banked B1/B0 sub-bubbles and C0/C1/C2) to max relative err 1.50e-05 -- a target-free validation of the full rank-2 tensor structure against banked quantities. |
| · | `T_w_trace_pv_cij_rank2_mesh_consistency` | theorem | `P` | Rank-2 Cij quadrature mesh-converged: n=130 vs n=260 to 6.72e-05. |
| · | `T_w_trace_pv_cij_rank2_trace_relation` | theorem | `P` | The native rank-2 three-point coefficients satisfy the finite d=4-2eps metric-trace relation against the banked B0 + native C0 to max relative err 7.25e-06 -- validates C00 (incl. the -1/2 trace finite correction) and the C11/C22/C12 combination, target-free. |

## `apf/w_trace_pv_d0_general_momentum.py` — 4 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_w_trace_pv_d0_general_cyclic_symmetry` | theorem | `P` | The native box D0 is invariant under cyclic permutation of the leg (mass, invariant) labels with the diagonal s<->t swap to max relative err 3.00e-04 -- a target-free validation of the (s,t) diagonal pairing structure of F. |
| · | `T_w_trace_pv_d0_general_mesh_consistency` | theorem | `P` | Box D0 simplex quadrature mesh-converged: n=40 vs n=80 to 5.32e-04. |
| · | `T_w_trace_pv_d0_general_subgate_partial` | theorem | `P_structural_partial` | The native scalar substrate is now complete at general (spacelike) momenta for all four Passarino-Veltman scalars A0/B0/C0/D0 (with a domain quarantine for above-threshold/complex kinematics). The 4-point tensor coefficients Dij, the above-threshold branch, the Denner coefficient map, and the cou... |
| · | `T_w_trace_pv_d0_general_zero_momentum_limit` | theorem | `P` | The native general-momentum box D0 reduces, at vanishing external invariants, to the banked d0_fin_zero_momenta to max relative err 7.09e-05 -- ties the new evaluator to the banked substrate. |

## `apf/w_trace_pv_derivative_two_point.py` — 4 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_w_trace_pv_b0_prime_closed_forms` | theorem | `P` | The native B0' reproduces its analytic closed forms -- equal-mass zero-momentum 1/(6 m^2) and massless 1/\|p^2\| (spacelike) -- to max relative err 5.21e-11. |
| · | `T_w_trace_pv_b0_prime_matches_finite_difference` | theorem | `P` | The native B0' = int x(1-x)/F dx agrees with the central finite difference of the banked b0_fin to max diff 7.14e-13 across 4 spacelike points -- an independent confirmation. |
| · | `T_w_trace_pv_b1_prime_matches_finite_difference` | theorem | `P` | The native B1' = -int x^2(1-x)/F dx agrees with the central finite difference of the native B1 to max diff 1.48e-14 across 4 spacelike points. |
| · | `T_w_trace_pv_derivative_two_point_subgate_partial` | theorem | `P_structural_partial` | The native OS-W toolkit gains the two-point momentum derivatives B0', B1' needed for on-shell wave-function/mass renormalization, on top of the two-point value tensors (B1,B00,B11). The self-energy assembly, the 3-/4-point Cij/Dij, the Denner coefficient map, and the counterterm assembly remain O... |

## `apf/w_trace_pv_dij_four_point.py` — 7 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_w_trace_pv_d00_dij_rank2_mesh_consistency` | theorem | `P` | Box rank-2 D00/Dij quadrature mesh-converged: n=28 vs n=46 to 1.27e-03. |
| · | `T_w_trace_pv_d00_dij_rank2_trace_relation` | theorem | `—` | (no summary) |
| · | `T_w_trace_pv_d00k_dijk_rank3_mesh_consistency` | theorem | `P` | Box rank-3 D00k/Dijk quadrature mesh-converged: n=28 vs n=46 to 2.15e-03. |
| · | `T_w_trace_pv_d00k_dijk_rank3_trace_relation` | theorem | `P` | The native rank-3 box coefficients D00k (metric x momentum) and D_ijk satisfy the p_i-projected metric-trace relation 6 sum_m (p_i.p_m) D00m + sum_{abc} (p_a.p_b)(p_i.p_c) D_abc = (p_i . C(2,3,4)) + m1^2 sum_m (p_i.p_m) D_m for i=1,2,3 -- the box rank-3 reduced against the native triangle (2,3,4)... |
| · | `T_w_trace_pv_d1_d2_d3_contraction_identities` | theorem | `P` | The native rank-1 box coefficients D1,D2,D3 satisfy the three contraction identities p_i.D^mu = 1/2 [C0(sub) - C0(sub) - f_i D0], reducing the box to the four native triangle sub-functions C0 (with box-induced invariants) and the box D0, to max relative err 4.29e-04 -- a target-free validation ag... |
| · | `T_w_trace_pv_d1_d2_d3_mesh_consistency` | theorem | `P` | Box rank-1 D quadrature mesh-converged: n=36 vs n=72 to 4.15e-04. |
| · | `T_w_trace_pv_d_rank123_subgate_partial` | theorem | `P_structural_partial` | The native four-point (box) tensor reduction is complete through rank 3 (D1/D2/D3; D00/Dij; D00k/Dijk), built on the general-momentum box D0 + the native triangle C0, every rung self-validated by contraction / metric-trace relations against native lower-point functions with zero external input. T... |

## `apf/w_trace_pv_ewwgr_bare_proper_vertex.py` — 5 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_w_trace_pv_ewwgr_bare_F_L_ell_target` | theorem | `P` | At the Z pole with the APF-native sin^2 theta_W = 3/13, the channel-specific F_L^ell = (1/4 sW^2) Lambda_2(M_W^2) - (3 cW^2/2 sW^2) Lambda_3(M_W^2) evaluates to 2.7137 + 2.2825i, \|F_L^ell\| = 3.5459, on the v24.3.360 SIGN-CORRECTED Lambda_3. The pre-.360 working-doc target '~18' is RETIRED, not re... |
| · | `T_w_trace_pv_ewwgr_bare_neutrino_consistency` | theorem | `P` | The neutrino bare proper-vertex form factors satisfy F_V^Zν = F_A^Zν (the standard left-handed-only coupling structure of the SM neutrino sector reflected at one loop) to 0.0e+00 -- a structural consistency check on the wrapper layer. |
| · | `T_w_trace_pv_ewwgr_bare_reference_values` | theorem | `P` | Eleven bare proper-vertex form factors (F_L^f and G_L^f for f in {ell, u, d}, the neutrino F^Zν, the leptonic Z-channel F_V^Zell + F_A^Zell, and the leptonic photon-channel F_V^γell + F_A^γell) match an INDEPENDENT mpmath dps=40 computation (Lambda from polylog(2,.), Feynman iepsilon) at s = M_Z^... |
| · | `T_w_trace_pv_ewwgr_bare_spacelike_real` | theorem | `P` | For spacelike external invariant s < 0, all bare proper-vertex form factors (F_V^Zf, F_A^Zf, F_Zν, F_V^γf, F_A^γf for f in {ell, u, d}) are real to max \|Im\| 1.7e-21 -- inherits the spacelike reality of Lambda_2, Lambda_3 (R1, v24.3.106) through linear combination with tree EW couplings. |
| · | `T_w_trace_pv_ewwgr_bare_subgate_partial` | theorem | `P_structural_partial` | The EWWGR section 6 Zff and γff proper-vertex 3-pt form factors -- F_V^Zf, F_A^Zf, F_Zν, F_V^γf, F_A^γf, plus the channel-specific F_L^f and G_L^f for f in {ell, u, d} -- are now native, built as a thin layer on the R1 BHM Lambda_2, Lambda_3 (v24.3.106) and wrapped with the tree EW couplings v_f,... |

## `apf/w_trace_pv_lambda_bhm_vertex.py` — 6 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_w_trace_pv_lambda3_sign_corrigendum_denner_anchor` | theorem | `P` | The v24.3.360 sign corrigendum certified in-check: (1) s->0 -- corrected Lambda_3(-1.29e-04*M_Z^2) = 3.07e-05 (vanishes, like the validated Lambda_2), while the printed form tracks its unphysical divergence -8w/3 - 10/9 = 16084.3 (negative control); (2) the Denner anchor -- Lambda_3_corr(s) = (1/... |
| · | `T_w_trace_pv_lambda_bhm_Li2_abel_identity` | theorem | `P` | The pure-Python Li_2 satisfies the Abel identity Li_2(z) + Li_2(1 - z) + log(z) log(1 - z) = pi^2 / 6 on six complex test points (real + complex, \|z\| < 1 + \|z\| > 1) to max abs err 3.6e-15 -- a target-free validation across the full branch structure of the implementation. |
| · | `T_w_trace_pv_lambda_bhm_Li2_reference_values` | theorem | `P` | The pure-Python principal-branch dilogarithm Li_2 reproduces four classical reference values (Li_2(1) = pi^2/6, Li_2(-1) = -pi^2/12, Li_2(1/2) = pi^2/12 - (ln 2)^2/2, Li_2(0) = 0) to max abs err 1.1e-16 -- validates the series + reflection implementation. |
| · | `T_w_trace_pv_lambda_bhm_physical_values` | theorem | `P` | At physical kinematics (s = M_Z^2 with M = M_W and M = M_Z; s = -M_Z^2 spacelike) the pure-Python implementation matches an independent high-precision mpmath computation (Li_2 = polylog(2, .), dps = 40, w = M^2 / (s + i eps)) to max rel err 2.0e-15 -- a tight machine-level reference anchor on fiv... |
| · | `T_w_trace_pv_lambda_bhm_spacelike_real` | theorem | `P` | For spacelike external invariant s < 0 (where the s-channel branch cut is closed) the absorptive parts of Lambda_2, Lambda_3 vanish to max \|Im\| 4.6e-18 across four kinematic test points -- confirms the correct analytic structure of the Feynman iepsilon prescription w = M^2 / (s + i eps). |
| · | `T_w_trace_pv_lambda_bhm_subgate_partial` | theorem | `P_structural_partial` | The BHM Z-vertex scalar functions Lambda_2(s, M^2) and Lambda_3(s, M^2) (EWWGR L6062 / hep-ph/9709229) are now native via the closed-form route: pure-Python implementation with a self-contained Li_2 + reflection structure, Feynman iepsilon prescription w = M^2 / (s + i eps), and a tight mpmath-an... |

## `apf/w_trace_pv_scalar_integral_substrate.py` — 45 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_w_trace_pv_a0_equal_mu_identity` | theorem | `P_w_trace_pv_scalar_integral_substrate` | (no summary) |
| · | `check_T_w_trace_pv_a0_gate_closed` | theorem | `P_w_trace_pv_scalar_integral_substrate` | (no summary) |
| · | `check_T_w_trace_pv_a0_scale_values_finite` | theorem | `P_w_trace_pv_scalar_integral_substrate` | (no summary) |
| · | `check_T_w_trace_pv_b0_gate_closed` | theorem | `P_w_trace_pv_scalar_integral_substrate` | (no summary) |
| · | `check_T_w_trace_pv_b0_route_domain_quarantined_or_finite` | theorem | `P_w_trace_pv_scalar_integral_substrate` | (no summary) |
| · | `check_T_w_trace_pv_b0_route_value_reasonable` | theorem | `P_w_trace_pv_scalar_integral_substrate` | (no summary) |
| · | `check_T_w_trace_pv_b0_symmetry` | theorem | `P_w_trace_pv_scalar_integral_substrate` | (no summary) |
| · | `check_T_w_trace_pv_b0_zero_equal_mw_matches_analytic` | theorem | `P_w_trace_pv_scalar_integral_substrate` | (no summary) |
| · | `check_T_w_trace_pv_b0_zero_equal_mz_matches_analytic` | theorem | `P_w_trace_pv_scalar_integral_substrate` | (no summary) |
| · | `check_T_w_trace_pv_bank_closure` | theorem | `P_w_trace_pv_scalar_integral_substrate` | (no summary) |
| · | `check_T_w_trace_pv_c0_equal_matches_analytic` | theorem | `P_w_trace_pv_scalar_integral_substrate` | (no summary) |
| · | `check_T_w_trace_pv_c0_gate_closed` | theorem | `P_w_trace_pv_scalar_integral_substrate` | (no summary) |
| · | `check_T_w_trace_pv_c0_mixed_finite` | theorem | `P_w_trace_pv_scalar_integral_substrate` | (no summary) |
| · | `check_T_w_trace_pv_coefficient_map_gate_open` | theorem | `P_w_trace_pv_scalar_integral_substrate` | (no summary) |
| · | `check_T_w_trace_pv_counterterm_target_inherited` | theorem | `P_w_trace_pv_scalar_integral_substrate` | (no summary) |
| · | `check_T_w_trace_pv_d0_equal_matches_analytic` | theorem | `P_w_trace_pv_scalar_integral_substrate` | (no summary) |
| · | `check_T_w_trace_pv_d0_gate_closed` | theorem | `P_w_trace_pv_scalar_integral_substrate` | (no summary) |
| · | `check_T_w_trace_pv_d0_mixed_finite` | theorem | `P_w_trace_pv_scalar_integral_substrate` | (no summary) |
| · | `check_T_w_trace_pv_dependency_pass` | theorem | `P_w_trace_pv_scalar_integral_substrate` | (no summary) |
| · | `check_T_w_trace_pv_first_failed_gate_exact` | theorem | `P_w_trace_pv_scalar_integral_substrate` | (no summary) |
| · | `check_T_w_trace_pv_forbidden_claims_present` | theorem | `P_w_trace_pv_scalar_integral_substrate` | (no summary) |
| · | `check_T_w_trace_pv_gate_count` | theorem | `P_w_trace_pv_scalar_integral_substrate` | (no summary) |
| · | `check_T_w_trace_pv_has_a0_evaluator` | theorem | `P_w_trace_pv_scalar_integral_substrate` | (no summary) |
| · | `check_T_w_trace_pv_has_b0_evaluator` | theorem | `P_w_trace_pv_scalar_integral_substrate` | (no summary) |
| · | `check_T_w_trace_pv_has_c0_evaluator` | theorem | `P_w_trace_pv_scalar_integral_substrate` | (no summary) |
| · | `check_T_w_trace_pv_has_d0_evaluator` | theorem | `P_w_trace_pv_scalar_integral_substrate` | (no summary) |
| · | `check_T_w_trace_pv_master_identity_inherited` | theorem | `P_w_trace_pv_scalar_integral_substrate` | (no summary) |
| · | `check_T_w_trace_pv_mu_reference_is_mz` | theorem | `P_w_trace_pv_scalar_integral_substrate` | (no summary) |
| · | `check_T_w_trace_pv_mw_residual_preserved` | theorem | `P_w_trace_pv_scalar_integral_substrate` | (no summary) |
| · | `check_T_w_trace_pv_next_gate_exact` | theorem | `P_w_trace_pv_scalar_integral_substrate` | (no summary) |
| · | `check_T_w_trace_pv_no_full_native_claim` | theorem | `P_w_trace_pv_scalar_integral_substrate` | (no summary) |
| · | `check_T_w_trace_pv_open_gates_block_full_native` | theorem | `P_w_trace_pv_scalar_integral_substrate` | (no summary) |
| · | `check_T_w_trace_pv_payload_digest_present` | theorem | `P_w_trace_pv_scalar_integral_substrate` | (no summary) |
| · | `check_T_w_trace_pv_report_has_benchmarks` | theorem | `P_w_trace_pv_scalar_integral_substrate` | (no summary) |
| · | `check_T_w_trace_pv_report_has_gates` | theorem | `P_w_trace_pv_scalar_integral_substrate` | (no summary) |
| · | `check_T_w_trace_pv_report_has_scalar_results` | theorem | `P_w_trace_pv_scalar_integral_substrate` | (no summary) |
| · | `check_T_w_trace_pv_results_all_finite` | theorem | `P_w_trace_pv_scalar_integral_substrate` | (no summary) |
| · | `check_T_w_trace_pv_results_count` | theorem | `P_w_trace_pv_scalar_integral_substrate` | (no summary) |
| · | `check_T_w_trace_pv_safe_claims_present` | theorem | `P_w_trace_pv_scalar_integral_substrate` | (no summary) |
| · | `check_T_w_trace_pv_status_declared` | theorem | `P_w_trace_pv_scalar_integral_substrate` | (no summary) |
| · | `check_T_w_trace_pv_status_export_candidate_preserved` | theorem | `P_w_trace_pv_scalar_integral_substrate` | (no summary) |
| · | `check_T_w_trace_pv_tensor_reduction_gate_open` | theorem | `P_w_trace_pv_scalar_integral_substrate` | (no summary) |
| · | `check_T_w_trace_pv_threshold_gate_closed` | theorem | `P_w_trace_pv_scalar_integral_substrate` | (no summary) |
| · | `check_T_w_trace_pv_total_sigma_preserved` | theorem | `P_w_trace_pv_scalar_integral_substrate` | (no summary) |
| · | `check_T_w_trace_pv_units_declared` | theorem | `P_w_trace_pv_scalar_integral_substrate` | (no summary) |

## `apf/w_trace_pv_tensor_reduction.py` — 7 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_w_trace_pv_b00_b11_trace_relation` | theorem | `P` | The native rank-2 coefficients B00, B11 satisfy the finite d=4-2eps metric-trace relation against the banked A0/B0 substrate to max relative err 2.87e-08 across 5 spacelike points. This ties B00 (incl. its trace finite correction) and B11 to an independent banked quantity -- a target-free validat... |
| · | `T_w_trace_pv_b00_massless_closed_form` | theorem | `P` | The massless B00 reproduces its analytic closed form \|p^2\|(2/9 - ln(\|p^2\|/mu^2)/12) to max relative err 2.35e-09 -- an independent confirmation of the d=4-2eps trace finite correction. |
| · | `T_w_trace_pv_b11_massless_closed_form` | theorem | `P` | The massless B11 reproduces its analytic closed form -1/3 ln(\|p^2\|/mu^2) + 13/18 to max err 8.66e-06 (quadrature residual). |
| · | `T_w_trace_pv_b1_argument_swap_identity` | theorem | `P` | The exact PV identity B1(m0,m1)+B1(m1,m0) = -B0 holds to max err 1.78e-15 across 5 points -- a target-free internal-consistency proof of the B1 reduction. |
| · | `T_w_trace_pv_b1_massless_closed_form` | theorem | `P` | The massless B1 reproduces its analytic closed form to max err 8.66e-05; the residual is the banked B0 midpoint-quadrature error. |
| · | `T_w_trace_pv_b1_reduction_matches_direct` | theorem | `P` | The PV reduction B1 = [A0(m0)-A0(m1)-(p^2+m0^2-m1^2)B0]/(2p^2) on the banked A0/B0 substrate agrees with the independent direct integral int x ln(F/mu^2) dx across 5 spacelike points; max \|diff\| = 1.45e-08. |
| · | `T_w_trace_pv_twopoint_tensor_subgate_partial` | theorem | `P_structural_partial` | The OPEN G2F_TENSOR_REDUCTION gate now has its complete TWO-POINT tensor basis (B1, B00, B11) APF-owned and self-validated. The 3-point Cij, 4-point Dij, the Denner coefficient map, and the counterterm assembly remain OPEN. No Delta r_rem / DeltaRhobarW / M_W value is produced; DIZET stays the pu... |

## `apf/w_trace_pv_timelike_three_point.py` — 5 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_w_trace_pv_timelike_c0_absorptive_closed_form` | theorem | `P` | For the two-massless-external equal-internal-mass triangle the absorptive part reproduces the analytic closed form -(pi/s) ln((1+beta)/(1-beta)), beta=sqrt(1-4M^2/s), to max rel err 6.5e-11 -- a target-free analytic anchor on the cut, derived from the linear-inner reduction. |
| · | `T_w_trace_pv_timelike_c0_absorptive_two_ways` | theorem | `P` | The absorptive part of the timelike C0 obtained from the analytic inner integral (cmath branch of ln(F - i eps)) agrees with an explicit delta(F) root count -pi int dx sum 1/\|dF/dy\| over the cut to max rel err 4.5e-14 -- two independent derivations of the imaginary part. |
| · | `T_w_trace_pv_timelike_c0_permutation_threshold` | theorem | `P` | The timelike-branch C0 is invariant under cyclic and reflection permutations of the (mass, invariant) labels to max rel err 9.6e-11 -- a target-free validation that re-evaluates the same triangle from different label assignments -- and its absorptive part vanishes below threshold, confirming the ... |
| · | `T_w_trace_pv_timelike_c0_spacelike_overlap` | theorem | `P` | Wherever the Feynman denominator stays positive (spacelike external invariants) the timelike-branch scalar C0 reduces exactly to the banked general-momentum c0_general (max rel err 3.7e-06) with a vanishing absorptive part (max \|Im\| 3.2e-16) -- the branch is a consistent continuation of the banke... |
| · | `T_w_trace_pv_timelike_c0_subgate_partial` | theorem | `P_structural_partial` | The native scalar three-point C0 now extends to the timelike / above-threshold branch (principal-value Re + absorptive Im via the 1D-reduced Feynman integral with tanh-sinh on each smooth piece), the R0 prerequisite for the complex BHM Zll vertex functions Lambda_2(s,M_Z) / Lambda_3(s,M_W) at s=M... |

## `apf/w_trace_pv_timelike_three_point_tensor.py` — 4 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_w_trace_pv_timelike_c1_c2_absorptive_closed_form` | theorem | `P` | The absorptive parts Im(C1), Im(C2) reproduce two independently derived closed forms: class A C(0,M,M;0,0,s>M) and class B C(M,M,M;0,0,s>4M). Max rel err 6.9e-11 -- target-free analytic anchors on the cut. |
| · | `T_w_trace_pv_timelike_c1_c2_absorptive_two_ways` | theorem | `P` | Im(C1), Im(C2) from the analytic inner (cmath branches of ln(F - i eps)) agree with the explicit delta(F) root count to max rel err 5.9e-13. The absorptive parts vanish below threshold, confirming the correct analytic structure of the cut. |
| · | `T_w_trace_pv_timelike_c1_c2_spacelike_overlap` | theorem | `P` | Wherever F>0 throughout the simplex (spacelike external invariants) the timelike-branch rank-1 (C1,C2) reduce to the banked direct spacelike c1_c2_direct (max rel err 5.8e-06) with vanishing absorptive parts (max \|Im\| 2.1e-16) -- a consistent continuation of the banked spacelike substrate. |
| · | `T_w_trace_pv_timelike_c1_c2_subgate_partial` | theorem | `P_structural_partial` | The native three-point rank-1 tensor coefficients (C1, C2) extend to the timelike branch (1D-reduced Feynman integral with the closed-form inner J, single-log stable I, tanh-sinh + kink-subdivision on each smooth piece), the R0b prerequisite for the complex BHM Zll vertex functions Lambda_2(s,M_Z... |

## `apf/w_trace_pv_timelike_three_point_tensor_rank2.py` — 4 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_w_trace_pv_timelike_cij_rank2_spacelike_overlap` | theorem | `P` | Wherever F>0 throughout the simplex the timelike-branch rank-2 (C00, C11, C12, C22) reduce to the banked spacelike cij_rank2_direct (max rel err 4.6e-07) with vanishing absorptive parts (max \|Im\| 1.4e-12) -- a consistent continuation. |
| · | `T_w_trace_pv_timelike_cij_rank2_subgate_partial` | theorem | `P_structural_partial` | The native three-point rank-2 tensor coefficients (C00, C11, C12, C22) now extend to the timelike branch via the closed-form inner K and single-log L (integration by parts), with the same tanh-sinh + kink-subdivision outer quadrature. Together with the timelike scalar C0 (v24.3.103) and rank-1 (C... |
| · | `T_w_trace_pv_timelike_cij_rank2_threshold` | theorem | `P` | The absorptive parts of the native rank-2 coefficients vanish below threshold (max sum \|Im\| 1.4e-07) and in the spacelike domain (max sum \|Im\| 1.2e-12), confirming the correct analytic structure of the cut. |
| · | `T_w_trace_pv_timelike_cij_rank2_trace_relation` | theorem | `P` | The native rank-2 coefficients satisfy the finite d=4-2 eps metric-trace relation (Ward identity) against the banked complex timelike B0 + native timelike C0 to max rel err 7.9e-04 across spacelike + timelike test points -- a target-free validation that ties the new rank-2 Cij to the banked B0 + ... |

## `apf/w_trace_pv_timelike_two_point.py` — 5 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_w_trace_pv_timelike_b0_massless_closed` | theorem | `P` | On the timelike branch the principal-value Re B0(p^2,0,0) reproduces 2 - ln(\|p^2\|/mu^2) to 5.8e-06 and the absorptive Im B0(p^2,0,0) = pi exactly. Native, no external input. |
| · | `T_w_trace_pv_timelike_b0_threshold_closed` | theorem | `P` | Above threshold the principal-value Re B0 reproduces both the equal-mass form 2 - ln(m^2/mu^2) + beta ln((1-beta)/(1+beta)) and the unequal-mass two-log closed form to 1.1e-05, with the absorptive part Im B0 = pi sqrt(lambda)/s matching to <3e-3. Three independent closed-form validations; native,... |
| · | `T_w_trace_pv_timelike_spacelike_overlap` | theorem | `P` | Wherever F>0 (spacelike, or timelike below threshold) the timelike Re B0/B1/B11/B00 reduce exactly to the banked spacelike b0_fin/b1_direct/b11_direct/b00_direct (max err 1.4e-06) -- the branch is a consistent continuation of the banked substrate, not a separate object. |
| · | `T_w_trace_pv_timelike_subgate_partial` | theorem | `P_structural_partial` | The native two-point PV functions now extend to the timelike / above-threshold branch (Re B0/B1/B11/B00 via principal value + the absorptive Im B0), reducing to the banked spacelike functions where F>0 -- the prerequisite for Re Pi_WW(M_W^2) / Re Pi_ZZ(M_Z^2). Still OPEN toward the APF-internal D... |
| · | `T_w_trace_pv_timelike_trace_relation` | theorem | `P` | Above threshold the real parts satisfy the rank-2 trace relation 4 Re B00 + p^2 Re B11 - (m0^2/2+m1^2/2-p^2/6) = A0(m1^2) + m0^2 Re B0 to max rel err 2.4e-05, jointly validating the timelike Re B00/B11/B0 against the banked A0. |

## `apf/w_trace_real_row_bundle_admission.py` — 24 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_w_real_row_bundle_admission_states_exhaustive` | theorem | `P_w_real_row_bundle_admission` | (no summary) |
| · | `T_w_real_row_bundle_bank_closure` | theorem | `—` | (no summary) |
| · | `T_w_real_row_bundle_default_empty_certificate` | theorem | `P_w_real_row_bundle_admission` | (no summary) |
| · | `T_w_real_row_bundle_default_exports_locked` | theorem | `P_w_real_row_bundle_admission` | (no summary) |
| · | `T_w_real_row_bundle_depends_on_v108_schema` | theorem | `—` | (no summary) |
| · | `T_w_real_row_bundle_does_not_certify_component_sum` | theorem | `P_w_real_row_bundle_admission` | (no summary) |
| · | `T_w_real_row_bundle_does_not_certify_covariance` | theorem | `P_w_real_row_bundle_admission` | (no summary) |
| · | `T_w_real_row_bundle_dry_rows_can_admit_when_not_shipped_default` | theorem | `P_w_real_row_bundle_admission` | (no summary) |
| · | `T_w_real_row_bundle_forbids_apf_anchor_metadata` | theorem | `P_w_real_row_bundle_admission` | (no summary) |
| · | `T_w_real_row_bundle_forbids_observed_w_metadata` | theorem | `P_w_real_row_bundle_admission` | (no summary) |
| · | `T_w_real_row_bundle_forbids_residual_fit_metadata` | theorem | `P_w_real_row_bundle_admission` | (no summary) |
| · | `T_w_real_row_bundle_metadata_fields_complete` | theorem | `P_w_real_row_bundle_admission` | (no summary) |
| · | `T_w_real_row_bundle_physical_export_request_blocked` | theorem | `P_w_real_row_bundle_admission` | (no summary) |
| · | `T_w_real_row_bundle_policy_blocks_export` | theorem | `P_w_real_row_bundle_admission` | (no summary) |
| · | `T_w_real_row_bundle_preserves_release_lock` | theorem | `P_w_real_row_bundle_admission` | (no summary) |
| · | `T_w_real_row_bundle_rejects_bad_review_status` | theorem | `P_w_real_row_bundle_admission` | (no summary) |
| · | `T_w_real_row_bundle_rejects_duplicate_component` | theorem | `P_w_real_row_bundle_admission` | (no summary) |
| · | `T_w_real_row_bundle_rejects_missing_component` | theorem | `P_w_real_row_bundle_admission` | (no summary) |
| · | `T_w_real_row_bundle_rejects_missing_metadata` | theorem | `P_w_real_row_bundle_admission` | (no summary) |
| · | `T_w_real_row_bundle_rejects_schema_version_mismatch` | theorem | `P_w_real_row_bundle_admission` | (no summary) |
| · | `T_w_real_row_bundle_rejects_unknown_component` | theorem | `P_w_real_row_bundle_admission` | (no summary) |
| · | `T_w_real_row_bundle_rejects_wrong_order` | theorem | `P_w_real_row_bundle_admission` | (no summary) |
| · | `T_w_real_row_bundle_shape_fixture_rejected_as_real` | theorem | `P_w_real_row_bundle_admission` | (no summary) |
| · | `T_w_real_row_bundle_status_declared` | theorem | `P_w_real_row_bundle_admission` | (no summary) |

## `apf/w_trace_real_source_candidate.py` — 25 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_w_real_source_candidate_absence_certificate_names_missing_rows` | theorem | `—` | (no summary) |
| · | `T_w_real_source_candidate_bank_closure` | theorem | `—` | (no summary) |
| · | `T_w_real_source_candidate_complete_metadata_predicate_positive` | theorem | `—` | (no summary) |
| · | `T_w_real_source_candidate_depends_on_v101_ingestion` | theorem | `—` | (no summary) |
| · | `T_w_real_source_candidate_does_not_certify_component_sum` | theorem | `—` | (no summary) |
| · | `T_w_real_source_candidate_does_not_supply_covariance_or_uncertainty` | theorem | `—` | (no summary) |
| · | `T_w_real_source_candidate_empty_by_default` | theorem | `—` | (no summary) |
| · | `T_w_real_source_candidate_forbidden_inputs_include_apf_target` | theorem | `—` | (no summary) |
| · | `T_w_real_source_candidate_forbidden_inputs_include_observed_W` | theorem | `—` | (no summary) |
| · | `T_w_real_source_candidate_forbidden_inputs_include_residual_fit` | theorem | `—` | (no summary) |
| · | `T_w_real_source_candidate_manifest_shape` | theorem | `—` | (no summary) |
| · | `T_w_real_source_candidate_metadata_schema_declared` | theorem | `—` | (no summary) |
| · | `T_w_real_source_candidate_parser_uses_metadata_format` | theorem | `—` | (no summary) |
| · | `T_w_real_source_candidate_physical_export_remains_locked` | theorem | `—` | (no summary) |
| · | `T_w_real_source_candidate_rejects_apf_anchor_consuming_rows` | theorem | `—` | (no summary) |
| · | `T_w_real_source_candidate_rejects_bad_metadata_format` | theorem | `—` | (no summary) |
| · | `T_w_real_source_candidate_rejects_incomplete_table_shape` | theorem | `—` | (no summary) |
| · | `T_w_real_source_candidate_rejects_observed_W_consuming_rows` | theorem | `—` | (no summary) |
| · | `T_w_real_source_candidate_rejects_symbol_mismatch` | theorem | `—` | (no summary) |
| · | `T_w_real_source_candidate_rejects_synthetic_fixture_metadata` | theorem | `—` | (no summary) |
| · | `T_w_real_source_candidate_requires_extraction_log_digest` | theorem | `—` | (no summary) |
| · | `T_w_real_source_candidate_requires_metadata_digest` | theorem | `—` | (no summary) |
| · | `T_w_real_source_candidate_requires_review_attestation` | theorem | `—` | (no summary) |
| · | `T_w_real_source_candidate_status_declared` | theorem | `P_w_real_source_candidate_gate` | (no summary) |
| · | `T_w_real_source_candidate_supported_formats_inherited` | theorem | `—` | (no summary) |

## `apf/w_trace_release_attestation.py` — 38 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_w_release_attestation_bad_hash_rejected` | theorem | `—` | (no summary) |
| · | `T_w_release_attestation_bad_manifest_digest_rejected` | theorem | `—` | (no summary) |
| · | `T_w_release_attestation_bad_signature_scheme_rejected` | theorem | `—` | (no summary) |
| · | `T_w_release_attestation_bad_validator_version_rejected` | theorem | `—` | (no summary) |
| · | `T_w_release_attestation_bank_closure` | theorem | `—` | (no summary) |
| · | `T_w_release_attestation_completed_shape_valid_but_export_locked` | theorem | `—` | (no summary) |
| · | `T_w_release_attestation_depends_on_release_packet_validator` | theorem | `—` | (no summary) |
| · | `T_w_release_attestation_doc_exists` | theorem | `—` | (no summary) |
| · | `T_w_release_attestation_doc_warns_locked` | theorem | `—` | (no summary) |
| · | `T_w_release_attestation_export_lock_ack_required` | theorem | `—` | (no summary) |
| · | `T_w_release_attestation_export_request_rejected` | theorem | `—` | (no summary) |
| · | `T_w_release_attestation_forbidden_manual_unlock_rejected` | theorem | `—` | (no summary) |
| · | `T_w_release_attestation_forbidden_observed_w_token_rejected` | theorem | `—` | (no summary) |
| · | `T_w_release_attestation_hash_algorithm_locked_sha256` | theorem | `—` | (no summary) |
| · | `T_w_release_attestation_immutable_manifest_binds_all_terminal_artifacts` | theorem | `—` | (no summary) |
| · | `T_w_release_attestation_json_serializable` | theorem | `—` | (no summary) |
| · | `T_w_release_attestation_manifest_digest_recomputed` | theorem | `—` | (no summary) |
| · | `T_w_release_attestation_manifest_fields_declared` | theorem | `—` | (no summary) |
| · | `T_w_release_attestation_manifest_fields_unique` | theorem | `—` | (no summary) |
| · | `T_w_release_attestation_manifest_mismatch_rejected` | theorem | `—` | (no summary) |
| · | `T_w_release_attestation_missing_manifest_field_rejected` | theorem | `—` | (no summary) |
| · | `T_w_release_attestation_no_physical_export_flags` | theorem | `—` | (no summary) |
| · | `T_w_release_attestation_real_state_false` | theorem | `—` | (no summary) |
| · | `T_w_release_attestation_release_packet_digest_required` | theorem | `—` | (no summary) |
| · | `T_w_release_attestation_release_packet_validator_still_locked` | theorem | `—` | (no summary) |
| · | `T_w_release_attestation_required_fields_declared` | theorem | `—` | (no summary) |
| · | `T_w_release_attestation_required_fields_unique` | theorem | `—` | (no summary) |
| · | `T_w_release_attestation_signature_not_verified_without_artifact` | theorem | `—` | (no summary) |
| · | `T_w_release_attestation_signature_schemes_declared` | theorem | `—` | (no summary) |
| · | `T_w_release_attestation_status_declared` | theorem | `—` | (no summary) |
| · | `T_w_release_attestation_template_not_real` | theorem | `—` | (no summary) |
| · | `T_w_release_attestation_template_path_declared` | theorem | `—` | (no summary) |
| · | `T_w_release_attestation_template_rejected` | theorem | `—` | (no summary) |
| · | `T_w_release_attestation_template_signature_rejected` | theorem | `—` | (no summary) |
| · | `T_w_release_attestation_template_signer_rejected` | theorem | `—` | (no summary) |
| · | `T_w_release_attestation_terminal_state_blocked_default` | theorem | `—` | (no summary) |
| · | `T_w_release_attestation_validator_version_pinned` | theorem | `—` | (no summary) |
| · | `T_w_release_attestation_write_template` | theorem | `—` | (no summary) |

## `apf/w_trace_release_evidence_bundle.py` — 13 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_w_trace_release_evidence_bundle_all_terminal_artifacts_present` | theorem | `—` | (no summary) |
| · | `T_w_trace_release_evidence_bundle_bank_closure` | theorem | `—` | (no summary) |
| · | `T_w_trace_release_evidence_bundle_evidence_bundle_template_not_real` | theorem | `—` | (no summary) |
| · | `T_w_trace_release_evidence_bundle_export_locked` | theorem | `—` | (no summary) |
| · | `T_w_trace_release_evidence_bundle_forbidden_observed_w_rejected` | theorem | `—` | (no summary) |
| · | `T_w_trace_release_evidence_bundle_forbidden_override_rejected` | theorem | `—` | (no summary) |
| · | `T_w_trace_release_evidence_bundle_missing_covariance_blocks_release` | theorem | `—` | (no summary) |
| · | `T_w_trace_release_evidence_bundle_missing_rows_blocks_release` | theorem | `—` | (no summary) |
| · | `T_w_trace_release_evidence_bundle_missing_signature_blocks_release` | theorem | `—` | (no summary) |
| · | `T_w_trace_release_evidence_bundle_missing_sum_blocks_release` | theorem | `—` | (no summary) |
| · | `T_w_trace_release_evidence_bundle_missing_uncertainty_blocks_release` | theorem | `—` | (no summary) |
| · | `T_w_trace_release_evidence_bundle_required_evidence_declared` | theorem | `—` | (no summary) |
| · | `T_w_trace_release_evidence_bundle_status_declared` | theorem | `—` | (no summary) |

## `apf/w_trace_release_packet_validator.py` — 35 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_w_release_packet_validator_actions_required` | theorem | `P_w_release_packet_validator` | (no summary) |
| · | `T_w_release_packet_validator_bad_digest_rejected` | theorem | `P_w_release_packet_validator` | (no summary) |
| · | `T_w_release_packet_validator_bank_closure` | theorem | `P_w_release_packet_validator` | (no summary) |
| · | `T_w_release_packet_validator_completed_shape_still_export_locked` | theorem | `P_w_release_packet_validator` | (no summary) |
| · | `T_w_release_packet_validator_default_rejected` | theorem | `P_w_release_packet_validator` | (no summary) |
| · | `T_w_release_packet_validator_depends_on_runbook` | theorem | `P_w_release_packet_validator` | (no summary) |
| · | `T_w_release_packet_validator_doc_exists` | theorem | `P_w_release_packet_validator` | (no summary) |
| · | `T_w_release_packet_validator_doc_warns_locked` | theorem | `P_w_release_packet_validator` | (no summary) |
| · | `T_w_release_packet_validator_export_lock_ack_required` | theorem | `P_w_release_packet_validator` | (no summary) |
| · | `T_w_release_packet_validator_forbidden_audit_required` | theorem | `P_w_release_packet_validator` | (no summary) |
| · | `T_w_release_packet_validator_json_serializable` | theorem | `P_w_release_packet_validator` | (no summary) |
| · | `T_w_release_packet_validator_manual_unlock_rejected` | theorem | `P_w_release_packet_validator` | (no summary) |
| · | `T_w_release_packet_validator_no_physical_export_flags` | theorem | `P_w_release_packet_validator` | (no summary) |
| · | `T_w_release_packet_validator_observed_w_token_rejected` | theorem | `P_w_release_packet_validator` | (no summary) |
| · | `T_w_release_packet_validator_operator_actions_match_runbook` | theorem | `P_w_release_packet_validator` | (no summary) |
| · | `T_w_release_packet_validator_predicates_required` | theorem | `P_w_release_packet_validator` | (no summary) |
| · | `T_w_release_packet_validator_real_state_false` | theorem | `P_w_release_packet_validator` | (no summary) |
| · | `T_w_release_packet_validator_rejects_bad_decision` | theorem | `P_w_release_packet_validator` | (no summary) |
| · | `T_w_release_packet_validator_rejects_template_token` | theorem | `P_w_release_packet_validator` | (no summary) |
| · | `T_w_release_packet_validator_release_predicates_match_runbook` | theorem | `P_w_release_packet_validator` | (no summary) |
| · | `T_w_release_packet_validator_reports_missing_artifacts` | theorem | `P_w_release_packet_validator` | (no summary) |
| · | `T_w_release_packet_validator_reports_missing_digests` | theorem | `P_w_release_packet_validator` | (no summary) |
| · | `T_w_release_packet_validator_required_fields_declared` | theorem | `P_w_release_packet_validator` | (no summary) |
| · | `T_w_release_packet_validator_required_fields_unique` | theorem | `P_w_release_packet_validator` | (no summary) |
| · | `T_w_release_packet_validator_requires_two_reviewers` | theorem | `P_w_release_packet_validator` | (no summary) |
| · | `T_w_release_packet_validator_runbook_dependency_invoked` | theorem | `P_w_release_packet_validator` | (no summary) |
| · | `T_w_release_packet_validator_runbook_version_required` | theorem | `P_w_release_packet_validator` | (no summary) |
| · | `T_w_release_packet_validator_sha256_digest_accepted_shape` | theorem | `P_w_release_packet_validator` | (no summary) |
| · | `T_w_release_packet_validator_status_declared` | theorem | `P_w_release_packet_validator` | (no summary) |
| · | `T_w_release_packet_validator_template_not_real` | theorem | `P_w_release_packet_validator` | (no summary) |
| · | `T_w_release_packet_validator_template_path_declared` | theorem | `P_w_release_packet_validator` | (no summary) |
| · | `T_w_release_packet_validator_terminal_state_blocked_default` | theorem | `P_w_release_packet_validator` | (no summary) |
| · | `T_w_release_packet_validator_terminal_state_valid_shape_locked` | theorem | `P_w_release_packet_validator` | (no summary) |
| · | `T_w_release_packet_validator_valid_decisions_declared` | theorem | `P_w_release_packet_validator` | (no summary) |
| · | `T_w_release_packet_validator_write_template` | theorem | `P_w_release_packet_validator` | (no summary) |

## `apf/w_trace_release_runbook.py` — 32 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_w_release_runbook_bank_closure` | theorem | `P_w_release_runbook` | (no summary) |
| · | `T_w_release_runbook_checklist_template_not_real` | theorem | `P_w_release_runbook` | (no summary) |
| · | `T_w_release_runbook_complete_packet_not_export_ready_without_pipeline` | theorem | `P_w_release_runbook` | (no summary) |
| · | `T_w_release_runbook_component_sum_requires_admission_report` | theorem | `P_w_release_runbook` | (no summary) |
| · | `T_w_release_runbook_covariance_requires_admission_report` | theorem | `P_w_release_runbook` | (no summary) |
| · | `T_w_release_runbook_default_locked_state` | theorem | `P_w_release_runbook` | (no summary) |
| · | `T_w_release_runbook_depends_on_e2e_manifest` | theorem | `P_w_release_runbook` | (no summary) |
| · | `T_w_release_runbook_doc_exists` | theorem | `P_w_release_runbook` | (no summary) |
| · | `T_w_release_runbook_doc_warns_locked` | theorem | `P_w_release_runbook` | (no summary) |
| · | `T_w_release_runbook_forbidden_tokens_declared` | theorem | `P_w_release_runbook` | (no summary) |
| · | `T_w_release_runbook_import_log_requires_replay` | theorem | `P_w_release_runbook` | (no summary) |
| · | `T_w_release_runbook_json_serializable` | theorem | `P_w_release_runbook` | (no summary) |
| · | `T_w_release_runbook_json_template_not_real` | theorem | `P_w_release_runbook` | (no summary) |
| · | `T_w_release_runbook_missing_artifacts_reported` | theorem | `P_w_release_runbook` | (no summary) |
| · | `T_w_release_runbook_no_duplicate_phases` | theorem | `P_w_release_runbook` | (no summary) |
| · | `T_w_release_runbook_no_physical_export_flags` | theorem | `P_w_release_runbook` | (no summary) |
| · | `T_w_release_runbook_operator_actions_declared` | theorem | `P_w_release_runbook` | (no summary) |
| · | `T_w_release_runbook_payload_digest_required` | theorem | `P_w_release_runbook` | (no summary) |
| · | `T_w_release_runbook_phase_order_declared` | theorem | `P_w_release_runbook` | (no summary) |
| · | `T_w_release_runbook_pipeline_stage_order_referenced` | theorem | `P_w_release_runbook` | (no summary) |
| · | `T_w_release_runbook_rejects_manual_override_token` | theorem | `P_w_release_runbook` | (no summary) |
| · | `T_w_release_runbook_rejects_observed_w_token` | theorem | `P_w_release_runbook` | (no summary) |
| · | `T_w_release_runbook_release_predicates_declared` | theorem | `P_w_release_runbook` | (no summary) |
| · | `T_w_release_runbook_required_artifacts_declared` | theorem | `P_w_release_runbook` | (no summary) |
| · | `T_w_release_runbook_required_artifacts_unique` | theorem | `P_w_release_runbook` | (no summary) |
| · | `T_w_release_runbook_required_manifest_fields_referenced` | theorem | `P_w_release_runbook` | (no summary) |
| · | `T_w_release_runbook_status_declared` | theorem | `P_w_release_runbook` | (no summary) |
| · | `T_w_release_runbook_template_path_declared` | theorem | `P_w_release_runbook` | (no summary) |
| · | `T_w_release_runbook_terminal_state_locked` | theorem | `P_w_release_runbook` | (no summary) |
| · | `T_w_release_runbook_uncertainty_requires_sum_and_covariance` | theorem | `P_w_release_runbook` | (no summary) |
| · | `T_w_release_runbook_write_checklist_template` | theorem | `P_w_release_runbook` | (no summary) |
| · | `T_w_release_runbook_write_json_template` | theorem | `P_w_release_runbook` | (no summary) |

## `apf/w_trace_residual_interpretation.py` — 13 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_w_trace_residual_apf_above_cluster_positive` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_residual_band_green` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_residual_bank_closure` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_residual_delta_r_gap_small` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_residual_derivative_positive` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_residual_export_lock_preserved` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_residual_gap_under_6MeV` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_residual_no_export` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_residual_overclaim_guard_active` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_residual_pull_under_1sigma_or_near` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_residual_sentence_mentions_mev` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_residual_sentence_mentions_not_export` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_residual_status_declared` | theorem | `—` | (no summary) |

## `apf/w_trace_review_packet_validator.py` — 32 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_w_review_packet_validator_bank_closure` | theorem | `—` | (no summary) |
| · | `T_w_review_packet_validator_default_packet_rejected` | theorem | `P_w_review_packet_validator` | (no summary) |
| · | `T_w_review_packet_validator_depends_on_v116_review_packet` | theorem | `—` | (no summary) |
| · | `T_w_review_packet_validator_doc_exists` | theorem | `P_w_review_packet_validator` | (no summary) |
| · | `T_w_review_packet_validator_doc_warns_locked` | theorem | `P_w_review_packet_validator` | (no summary) |
| · | `T_w_review_packet_validator_json_template_exists` | theorem | `P_w_review_packet_validator` | (no summary) |
| · | `T_w_review_packet_validator_json_template_not_importable` | theorem | `P_w_review_packet_validator` | (no summary) |
| · | `T_w_review_packet_validator_no_rows_or_certificates` | theorem | `P_w_review_packet_validator` | (no summary) |
| · | `T_w_review_packet_validator_preflight_decisions_declared` | theorem | `P_w_review_packet_validator` | (no summary) |
| · | `T_w_review_packet_validator_promoted_packet_validates` | theorem | `P_w_review_packet_validator` | (no summary) |
| · | `T_w_review_packet_validator_promoted_ready_without_import_or_export` | theorem | `P_w_review_packet_validator` | (no summary) |
| · | `T_w_review_packet_validator_readiness_lock_unchanged` | theorem | `P_w_review_packet_validator` | (no summary) |
| · | `T_w_review_packet_validator_rejects_APF_anchor_token` | theorem | `P_w_review_packet_validator` | (no summary) |
| · | `T_w_review_packet_validator_rejects_bad_packet_digest` | theorem | `P_w_review_packet_validator` | (no summary) |
| · | `T_w_review_packet_validator_rejects_candidate_forbidden_input` | theorem | `P_w_review_packet_validator` | (no summary) |
| · | `T_w_review_packet_validator_rejects_candidate_template_only` | theorem | `P_w_review_packet_validator` | (no summary) |
| · | `T_w_review_packet_validator_rejects_incomplete_candidate` | theorem | `P_w_review_packet_validator` | (no summary) |
| · | `T_w_review_packet_validator_rejects_missing_evidence_digest` | theorem | `P_w_review_packet_validator` | (no summary) |
| · | `T_w_review_packet_validator_rejects_missing_preimport_step` | theorem | `P_w_review_packet_validator` | (no summary) |
| · | `T_w_review_packet_validator_rejects_missing_review_digest` | theorem | `P_w_review_packet_validator` | (no summary) |
| · | `T_w_review_packet_validator_rejects_missing_reviewer` | theorem | `P_w_review_packet_validator` | (no summary) |
| · | `T_w_review_packet_validator_rejects_missing_section` | theorem | `P_w_review_packet_validator` | (no summary) |
| · | `T_w_review_packet_validator_rejects_observed_W_token` | theorem | `P_w_review_packet_validator` | (no summary) |
| · | `T_w_review_packet_validator_rejects_physical_export_request` | theorem | `P_w_review_packet_validator` | (no summary) |
| · | `T_w_review_packet_validator_rejects_template_packet` | theorem | `P_w_review_packet_validator` | (no summary) |
| · | `T_w_review_packet_validator_rejects_wrong_decision` | theorem | `P_w_review_packet_validator` | (no summary) |
| · | `T_w_review_packet_validator_rejects_wrong_section_order` | theorem | `P_w_review_packet_validator` | (no summary) |
| · | `T_w_review_packet_validator_report_locks_default_state` | theorem | `P_w_review_packet_validator` | (no summary) |
| · | `T_w_review_packet_validator_required_fields_extend_packet` | theorem | `P_w_review_packet_validator` | (no summary) |
| · | `T_w_review_packet_validator_schema_serializes_json` | theorem | `P_w_review_packet_validator` | (no summary) |
| · | `T_w_review_packet_validator_status_declared` | theorem | `P_w_review_packet_validator` | (no summary) |
| · | `T_w_review_packet_validator_template_dir_exists` | theorem | `P_w_review_packet_validator` | (no summary) |

## `apf/w_trace_reviewed_source_import_handoff.py` — 32 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_w_reviewed_source_import_handoff_bank_closure` | theorem | `P_w_reviewed_source_import_handoff` | (no summary) |
| · | `T_w_reviewed_source_import_handoff_default_loader_not_invoked` | theorem | `P_w_reviewed_source_import_handoff` | (no summary) |
| · | `T_w_reviewed_source_import_handoff_default_no_packet_blocked` | theorem | `P_w_reviewed_source_import_handoff` | (no summary) |
| · | `T_w_reviewed_source_import_handoff_depends_on_v113_loader` | theorem | `—` | (no summary) |
| · | `T_w_reviewed_source_import_handoff_depends_on_v117_validator` | theorem | `—` | (no summary) |
| · | `T_w_reviewed_source_import_handoff_doc_exists` | theorem | `P_w_reviewed_source_import_handoff` | (no summary) |
| · | `T_w_reviewed_source_import_handoff_doc_warns_locked` | theorem | `P_w_reviewed_source_import_handoff` | (no summary) |
| · | `T_w_reviewed_source_import_handoff_example_dir_exists` | theorem | `P_w_reviewed_source_import_handoff` | (no summary) |
| · | `T_w_reviewed_source_import_handoff_invalid_packet_blocks_existing_file` | theorem | `P_w_reviewed_source_import_handoff` | (no summary) |
| · | `T_w_reviewed_source_import_handoff_loader_failures_propagate` | theorem | `P_w_reviewed_source_import_handoff` | (no summary) |
| · | `T_w_reviewed_source_import_handoff_missing_file_fails_closed` | theorem | `P_w_reviewed_source_import_handoff` | (no summary) |
| · | `T_w_reviewed_source_import_handoff_no_physical_W_export` | theorem | `P_w_reviewed_source_import_handoff` | (no summary) |
| · | `T_w_reviewed_source_import_handoff_no_rows_or_certificates` | theorem | `P_w_reviewed_source_import_handoff` | (no summary) |
| · | `T_w_reviewed_source_import_handoff_promoted_packet_validates` | theorem | `P_w_reviewed_source_import_handoff` | (no summary) |
| · | `T_w_reviewed_source_import_handoff_promoted_without_payload_no_import` | theorem | `P_w_reviewed_source_import_handoff` | (no summary) |
| · | `T_w_reviewed_source_import_handoff_readiness_lock_preserved` | theorem | `P_w_reviewed_source_import_handoff` | (no summary) |
| · | `T_w_reviewed_source_import_handoff_real_flag_still_no_admission_without_bundle` | theorem | `P_w_reviewed_source_import_handoff` | (no summary) |
| · | `T_w_reviewed_source_import_handoff_rejects_physical_export_request` | theorem | `P_w_reviewed_source_import_handoff` | (no summary) |
| · | `T_w_reviewed_source_import_handoff_rejects_template_preflight` | theorem | `P_w_reviewed_source_import_handoff` | (no summary) |
| · | `T_w_reviewed_source_import_handoff_report_schema_declared` | theorem | `P_w_reviewed_source_import_handoff` | (no summary) |
| · | `T_w_reviewed_source_import_handoff_review_attestation_only_after_validation` | theorem | `P_w_reviewed_source_import_handoff` | (no summary) |
| · | `T_w_reviewed_source_import_handoff_serializes_report_json` | theorem | `P_w_reviewed_source_import_handoff` | (no summary) |
| · | `T_w_reviewed_source_import_handoff_shape_fixture_not_real_payload` | theorem | `P_w_reviewed_source_import_handoff` | (no summary) |
| · | `T_w_reviewed_source_import_handoff_states_declared` | theorem | `P_w_reviewed_source_import_handoff` | (no summary) |
| · | `T_w_reviewed_source_import_handoff_status_declared` | theorem | `P_w_reviewed_source_import_handoff` | (no summary) |
| · | `T_w_reviewed_source_import_handoff_supported_formats_inherited` | theorem | `P_w_reviewed_source_import_handoff` | (no summary) |
| · | `T_w_reviewed_source_import_handoff_template_file_exists` | theorem | `P_w_reviewed_source_import_handoff` | (no summary) |
| · | `T_w_reviewed_source_import_handoff_template_not_real` | theorem | `P_w_reviewed_source_import_handoff` | (no summary) |
| · | `T_w_reviewed_source_import_handoff_template_path_declared` | theorem | `P_w_reviewed_source_import_handoff` | (no summary) |
| · | `T_w_reviewed_source_import_handoff_validated_csv_fixture_invokes_loader` | theorem | `P_w_reviewed_source_import_handoff` | (no summary) |
| · | `T_w_reviewed_source_import_handoff_validated_json_fixture_invokes_loader` | theorem | `P_w_reviewed_source_import_handoff` | (no summary) |
| · | `T_w_reviewed_source_import_handoff_write_template` | theorem | `P_w_reviewed_source_import_handoff` | (no summary) |

## `apf/w_trace_row_bundle_to_component_sum.py` — 27 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_w_row_bundle_sum_bridge_admitted_bundle_constructs_summands` | theorem | `P_w_row_bundle_to_component_sum_bridge` | (no summary) |
| · | `T_w_row_bundle_sum_bridge_bank_closure` | theorem | `—` | (no summary) |
| · | `T_w_row_bundle_sum_bridge_blocks_physical_export_request` | theorem | `P_w_row_bundle_to_component_sum_bridge` | (no summary) |
| · | `T_w_row_bundle_sum_bridge_default_empty_no_invocation` | theorem | `P_w_row_bundle_to_component_sum_bridge` | (no summary) |
| · | `T_w_row_bundle_sum_bridge_default_export_locked` | theorem | `P_w_row_bundle_to_component_sum_bridge` | (no summary) |
| · | `T_w_row_bundle_sum_bridge_depends_on_v104_sum_harness` | theorem | `—` | (no summary) |
| · | `T_w_row_bundle_sum_bridge_depends_on_v109_bundle_gate` | theorem | `—` | (no summary) |
| · | `T_w_row_bundle_sum_bridge_dry_target_rows_can_certify_mechanics` | theorem | `P_w_row_bundle_to_component_sum_bridge` | (no summary) |
| · | `T_w_row_bundle_sum_bridge_dry_target_rows_do_not_unlock_export` | theorem | `P_w_row_bundle_to_component_sum_bridge` | (no summary) |
| · | `T_w_row_bundle_sum_bridge_empty_bundle_cannot_certify` | theorem | `P_w_row_bundle_to_component_sum_bridge` | (no summary) |
| · | `T_w_row_bundle_sum_bridge_export_lock_still_false` | theorem | `P_w_row_bundle_to_component_sum_bridge` | (no summary) |
| · | `T_w_row_bundle_sum_bridge_forbidden_inputs_named` | theorem | `P_w_row_bundle_to_component_sum_bridge` | (no summary) |
| · | `T_w_row_bundle_sum_bridge_forbids_apf_anchor_consumption` | theorem | `P_w_row_bundle_to_component_sum_bridge` | (no summary) |
| · | `T_w_row_bundle_sum_bridge_forbids_observed_w_consumption` | theorem | `P_w_row_bundle_to_component_sum_bridge` | (no summary) |
| · | `T_w_row_bundle_sum_bridge_forbids_residual_fit_consumption` | theorem | `P_w_row_bundle_to_component_sum_bridge` | (no summary) |
| · | `T_w_row_bundle_sum_bridge_manifest_remains_open` | theorem | `P_w_row_bundle_to_component_sum_bridge` | (no summary) |
| · | `T_w_row_bundle_sum_bridge_no_physical_mass_export` | theorem | `P_w_row_bundle_to_component_sum_bridge` | (no summary) |
| · | `T_w_row_bundle_sum_bridge_policy_blocks_export` | theorem | `P_w_row_bundle_to_component_sum_bridge` | (no summary) |
| · | `T_w_row_bundle_sum_bridge_rejected_bundle_cannot_certify` | theorem | `P_w_row_bundle_to_component_sum_bridge` | (no summary) |
| · | `T_w_row_bundle_sum_bridge_rejects_order_mismatch` | theorem | `P_w_row_bundle_to_component_sum_bridge` | (no summary) |
| · | `T_w_row_bundle_sum_bridge_required_fields_declared` | theorem | `P_w_row_bundle_to_component_sum_bridge` | (no summary) |
| · | `T_w_row_bundle_sum_bridge_requires_covariance_for_certification` | theorem | `P_w_row_bundle_to_component_sum_bridge` | (no summary) |
| · | `T_w_row_bundle_sum_bridge_requires_uncertainty_for_certification` | theorem | `P_w_row_bundle_to_component_sum_bridge` | (no summary) |
| · | `T_w_row_bundle_sum_bridge_status_declared` | theorem | `P_w_row_bundle_to_component_sum_bridge` | (no summary) |
| · | `T_w_row_bundle_sum_bridge_summand_translation_preserves_order` | theorem | `P_w_row_bundle_to_component_sum_bridge` | (no summary) |
| · | `T_w_row_bundle_sum_bridge_summand_translation_preserves_symbols` | theorem | `P_w_row_bundle_to_component_sum_bridge` | (no summary) |
| · | `T_w_row_bundle_sum_bridge_zero_rows_do_not_certify_sum` | theorem | `P_w_row_bundle_to_component_sum_bridge` | (no summary) |

## `apf/w_trace_row_schema_adapter.py` — 29 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_w_row_schema_bank_closure` | theorem | `—` | (no summary) |
| · | `T_w_row_schema_component_order_matches_skeleton` | theorem | `P_w_row_schema_adapter` | (no summary) |
| · | `T_w_row_schema_component_symbols_match` | theorem | `P_w_row_schema_adapter` | (no summary) |
| · | `T_w_row_schema_counterterm_row_present_but_unadmitted` | theorem | `P_w_row_schema_adapter` | (no summary) |
| · | `T_w_row_schema_default_empty_state_no_rows_admitted` | theorem | `P_w_row_schema_adapter` | (no summary) |
| · | `T_w_row_schema_depends_on_counterterm_convention` | theorem | `—` | (no summary) |
| · | `T_w_row_schema_dimensionless_units_required` | theorem | `P_w_row_schema_adapter` | (no summary) |
| · | `T_w_row_schema_forbids_apf_anchor_consumption` | theorem | `P_w_row_schema_adapter` | (no summary) |
| · | `T_w_row_schema_forbids_observed_w_consumption` | theorem | `P_w_row_schema_adapter` | (no summary) |
| · | `T_w_row_schema_forbids_residual_fit_consumption` | theorem | `P_w_row_schema_adapter` | (no summary) |
| · | `T_w_row_schema_no_component_sum_or_export` | theorem | `P_w_row_schema_adapter` | (no summary) |
| · | `T_w_row_schema_physical_export_request_blocked` | theorem | `P_w_row_schema_adapter` | (no summary) |
| · | `T_w_row_schema_preserves_export_lock` | theorem | `P_w_row_schema_adapter` | (no summary) |
| · | `T_w_row_schema_rejects_duplicate_component` | theorem | `P_w_row_schema_adapter` | (no summary) |
| · | `T_w_row_schema_rejects_missing_component` | theorem | `P_w_row_schema_adapter` | (no summary) |
| · | `T_w_row_schema_rejects_missing_field` | theorem | `P_w_row_schema_adapter` | (no summary) |
| · | `T_w_row_schema_rejects_unknown_component` | theorem | `P_w_row_schema_adapter` | (no summary) |
| · | `T_w_row_schema_rejects_wrong_convention_id` | theorem | `P_w_row_schema_adapter` | (no summary) |
| · | `T_w_row_schema_rejects_wrong_counterterm_component` | theorem | `P_w_row_schema_adapter` | (no summary) |
| · | `T_w_row_schema_rejects_wrong_scheme_family` | theorem | `P_w_row_schema_adapter` | (no summary) |
| · | `T_w_row_schema_rejects_wrong_source_class` | theorem | `P_w_row_schema_adapter` | (no summary) |
| · | `T_w_row_schema_rejects_wrong_symbol` | theorem | `P_w_row_schema_adapter` | (no summary) |
| · | `T_w_row_schema_report_fields_complete` | theorem | `P_w_row_schema_adapter` | (no summary) |
| · | `T_w_row_schema_required_fields_complete` | theorem | `P_w_row_schema_adapter` | (no summary) |
| · | `T_w_row_schema_shape_rows_cannot_be_real_payload` | theorem | `P_w_row_schema_adapter` | (no summary) |
| · | `T_w_row_schema_shape_rows_validate_schema_only` | theorem | `P_w_row_schema_adapter` | (no summary) |
| · | `T_w_row_schema_status_declared` | theorem | `P_w_row_schema_adapter` | (no summary) |
| · | `T_w_row_schema_uncertainty_nonnegative` | theorem | `P_w_row_schema_adapter` | (no summary) |
| · | `T_w_row_schema_values_finite_numeric` | theorem | `P_w_row_schema_adapter` | (no summary) |

## `apf/w_trace_same_input_evaluator_closeout.py` — 33 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_w_same_input_evaluator_closeout_acfw_role_split` | theorem | `P_w_same_input_evaluator_terminal_closeout` | (no summary) |
| · | `check_T_w_same_input_evaluator_closeout_apf_rows_still_sum_to_target` | theorem | `P_w_same_input_evaluator_terminal_closeout` | (no summary) |
| · | `check_T_w_same_input_evaluator_closeout_bank_closure` | theorem | `P_w_same_input_evaluator_terminal_closeout` | (no summary) |
| · | `check_T_w_same_input_evaluator_closeout_candidate_audit_nonempty` | theorem | `P_w_same_input_evaluator_terminal_closeout` | (no summary) |
| · | `check_T_w_same_input_evaluator_closeout_candidate_ids_unique` | theorem | `P_w_same_input_evaluator_terminal_closeout` | (no summary) |
| · | `check_T_w_same_input_evaluator_closeout_candidate_verdicts_reject_export` | theorem | `P_w_same_input_evaluator_terminal_closeout` | (no summary) |
| · | `check_T_w_same_input_evaluator_closeout_covariance_sigma_preserved` | theorem | `P_w_same_input_evaluator_terminal_closeout` | (no summary) |
| · | `check_T_w_same_input_evaluator_closeout_depends_on_v157` | theorem | `P_w_same_input_evaluator_terminal_closeout` | (no summary) |
| · | `check_T_w_same_input_evaluator_closeout_eight_transferred_rows_retained` | theorem | `P_w_same_input_evaluator_terminal_closeout` | (no summary) |
| · | `check_T_w_same_input_evaluator_closeout_export_lock_preserved` | theorem | `P_w_same_input_evaluator_terminal_closeout` | (no summary) |
| · | `check_T_w_same_input_evaluator_closeout_final_readiness_blocked` | theorem | `P_w_same_input_evaluator_terminal_closeout` | (no summary) |
| · | `check_T_w_same_input_evaluator_closeout_first_failed_gate_locked` | theorem | `P_w_same_input_evaluator_terminal_closeout` | (no summary) |
| · | `check_T_w_same_input_evaluator_closeout_forbidden_claim_present_only_as_forbidden` | theorem | `P_w_same_input_evaluator_terminal_closeout` | (no summary) |
| · | `check_T_w_same_input_evaluator_closeout_gate_ladder_has_terminal_blockers` | theorem | `P_w_same_input_evaluator_terminal_closeout` | (no summary) |
| · | `check_T_w_same_input_evaluator_closeout_ladder_has_open_physical_row` | theorem | `P_w_same_input_evaluator_terminal_closeout` | (no summary) |
| · | `check_T_w_same_input_evaluator_closeout_ladder_prior_layers_closed` | theorem | `P_w_same_input_evaluator_terminal_closeout` | (no summary) |
| · | `check_T_w_same_input_evaluator_closeout_model_limited_status_named` | theorem | `P_w_same_input_evaluator_terminal_closeout` | (no summary) |
| · | `check_T_w_same_input_evaluator_closeout_mw_roundtrip_preserved` | theorem | `P_w_same_input_evaluator_terminal_closeout` | (no summary) |
| · | `check_T_w_same_input_evaluator_closeout_no_exact_evaluator_found` | theorem | `P_w_same_input_evaluator_terminal_closeout` | (no summary) |
| · | `check_T_w_same_input_evaluator_closeout_no_forbidden_tokens` | theorem | `P_w_same_input_evaluator_terminal_closeout` | (no summary) |
| · | `check_T_w_same_input_evaluator_closeout_no_row_admitted_for_export` | theorem | `P_w_same_input_evaluator_terminal_closeout` | (no summary) |
| · | `check_T_w_same_input_evaluator_closeout_payload_digest_present` | theorem | `P_w_same_input_evaluator_terminal_closeout` | (no summary) |
| · | `check_T_w_same_input_evaluator_closeout_publication_claim_allowed` | theorem | `P_w_same_input_evaluator_terminal_closeout` | (no summary) |
| · | `check_T_w_same_input_evaluator_closeout_pull_under_one_sigma` | theorem | `P_w_same_input_evaluator_terminal_closeout` | (no summary) |
| · | `check_T_w_same_input_evaluator_closeout_remaining_action_specific` | theorem | `P_w_same_input_evaluator_terminal_closeout` | (no summary) |
| · | `check_T_w_same_input_evaluator_closeout_required_capabilities_named` | theorem | `P_w_same_input_evaluator_terminal_closeout` | (no summary) |
| · | `check_T_w_same_input_evaluator_closeout_route_input_preserved` | theorem | `P_w_same_input_evaluator_terminal_closeout` | (no summary) |
| · | `check_T_w_same_input_evaluator_closeout_route_numerics_stable` | theorem | `P_w_same_input_evaluator_terminal_closeout` | (no summary) |
| · | `check_T_w_same_input_evaluator_closeout_source_local_rows_do_not_unlock` | theorem | `P_w_same_input_evaluator_terminal_closeout` | (no summary) |
| · | `check_T_w_same_input_evaluator_closeout_status_declared` | theorem | `P_w_same_input_evaluator_terminal_closeout` | (no summary) |
| · | `check_T_w_same_input_evaluator_closeout_terminal_status_exact` | theorem | `P_w_same_input_evaluator_terminal_closeout` | (no summary) |
| · | `check_T_w_same_input_evaluator_closeout_total_contexts_admitted_only_as_context` | theorem | `P_w_same_input_evaluator_terminal_closeout` | (no summary) |
| · | `check_T_w_same_input_evaluator_closeout_v157_boundary_consistent` | theorem | `P_w_same_input_evaluator_terminal_closeout` | (no summary) |

## `apf/w_trace_signature_verification_adapter.py` — 13 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_w_trace_signature_verification_adapter_apf_anchor_token_rejected` | theorem | `—` | (no summary) |
| · | `T_w_trace_signature_verification_adapter_bank_closure` | theorem | `—` | (no summary) |
| · | `T_w_trace_signature_verification_adapter_digest_mismatch_rejected` | theorem | `—` | (no summary) |
| · | `T_w_trace_signature_verification_adapter_export_locked` | theorem | `—` | (no summary) |
| · | `T_w_trace_signature_verification_adapter_manual_unlock_token_rejected` | theorem | `—` | (no summary) |
| · | `T_w_trace_signature_verification_adapter_missing_signature_rejected` | theorem | `—` | (no summary) |
| · | `T_w_trace_signature_verification_adapter_observed_w_token_rejected` | theorem | `—` | (no summary) |
| · | `T_w_trace_signature_verification_adapter_required_artifacts_declared` | theorem | `—` | (no summary) |
| · | `T_w_trace_signature_verification_adapter_status_declared` | theorem | `—` | (no summary) |
| · | `T_w_trace_signature_verification_adapter_supported_schemes_declared` | theorem | `—` | (no summary) |
| · | `T_w_trace_signature_verification_adapter_template_signature_rejected` | theorem | `—` | (no summary) |
| · | `T_w_trace_signature_verification_adapter_unsupported_scheme_rejected` | theorem | `—` | (no summary) |
| · | `T_w_trace_signature_verification_adapter_valid_shape_does_not_verify_without_crypto_artifact` | theorem | `—` | (no summary) |

## `apf/w_trace_signed_release_replay.py` — 13 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_w_trace_signed_release_replay_bad_order_rejected` | theorem | `—` | (no summary) |
| · | `T_w_trace_signed_release_replay_bank_closure` | theorem | `—` | (no summary) |
| · | `T_w_trace_signed_release_replay_depends_on_attestation` | theorem | `—` | (no summary) |
| · | `T_w_trace_signed_release_replay_depends_on_session_replay` | theorem | `—` | (no summary) |
| · | `T_w_trace_signed_release_replay_digest_chain_required` | theorem | `—` | (no summary) |
| · | `T_w_trace_signed_release_replay_export_locked` | theorem | `—` | (no summary) |
| · | `T_w_trace_signed_release_replay_missing_attestation_rejected` | theorem | `—` | (no summary) |
| · | `T_w_trace_signed_release_replay_no_target_observable_consumption` | theorem | `—` | (no summary) |
| · | `T_w_trace_signed_release_replay_ordered_replay_stages_declared` | theorem | `—` | (no summary) |
| · | `T_w_trace_signed_release_replay_replay_artifacts_declared` | theorem | `—` | (no summary) |
| · | `T_w_trace_signed_release_replay_status_declared` | theorem | `—` | (no summary) |
| · | `T_w_trace_signed_release_replay_template_replay_rejected` | theorem | `—` | (no summary) |
| · | `T_w_trace_signed_release_replay_unsigned_replay_rejected` | theorem | `—` | (no summary) |

## `apf/w_trace_source_acquisition_review_packet.py` — 30 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_w_source_acquisition_review_packet_bank_closure` | theorem | `—` | (no summary) |
| · | `T_w_source_acquisition_review_packet_carries_allowed_source_classes` | theorem | `P_w_source_acquisition_review_packet` | (no summary) |
| · | `T_w_source_acquisition_review_packet_carries_forbidden_inputs` | theorem | `P_w_source_acquisition_review_packet` | (no summary) |
| · | `T_w_source_acquisition_review_packet_carries_preimport_order` | theorem | `P_w_source_acquisition_review_packet` | (no summary) |
| · | `T_w_source_acquisition_review_packet_carries_registry_evidence_fields` | theorem | `P_w_source_acquisition_review_packet` | (no summary) |
| · | `T_w_source_acquisition_review_packet_decisions_declared` | theorem | `P_w_source_acquisition_review_packet` | (no summary) |
| · | `T_w_source_acquisition_review_packet_default_template_not_complete` | theorem | `P_w_source_acquisition_review_packet` | (no summary) |
| · | `T_w_source_acquisition_review_packet_depends_on_v115_registry` | theorem | `—` | (no summary) |
| · | `T_w_source_acquisition_review_packet_doc_exists` | theorem | `P_w_source_acquisition_review_packet` | (no summary) |
| · | `T_w_source_acquisition_review_packet_doc_warns_no_real_source` | theorem | `P_w_source_acquisition_review_packet` | (no summary) |
| · | `T_w_source_acquisition_review_packet_json_template_exists` | theorem | `P_w_source_acquisition_review_packet` | (no summary) |
| · | `T_w_source_acquisition_review_packet_json_template_not_real_payload` | theorem | `P_w_source_acquisition_review_packet` | (no summary) |
| · | `T_w_source_acquisition_review_packet_markdown_template_exists` | theorem | `P_w_source_acquisition_review_packet` | (no summary) |
| · | `T_w_source_acquisition_review_packet_markdown_template_has_placeholders` | theorem | `P_w_source_acquisition_review_packet` | (no summary) |
| · | `T_w_source_acquisition_review_packet_no_component_sum_or_covariance` | theorem | `P_w_source_acquisition_review_packet` | (no summary) |
| · | `T_w_source_acquisition_review_packet_promoted_packet_complete` | theorem | `P_w_source_acquisition_review_packet` | (no summary) |
| · | `T_w_source_acquisition_review_packet_readiness_locked` | theorem | `P_w_source_acquisition_review_packet` | (no summary) |
| · | `T_w_source_acquisition_review_packet_rejects_APF_anchor_input` | theorem | `P_w_source_acquisition_review_packet` | (no summary) |
| · | `T_w_source_acquisition_review_packet_rejects_incomplete_preimport_steps` | theorem | `P_w_source_acquisition_review_packet` | (no summary) |
| · | `T_w_source_acquisition_review_packet_rejects_incomplete_sections` | theorem | `P_w_source_acquisition_review_packet` | (no summary) |
| · | `T_w_source_acquisition_review_packet_rejects_missing_evidence_digest` | theorem | `P_w_source_acquisition_review_packet` | (no summary) |
| · | `T_w_source_acquisition_review_packet_rejects_missing_review_digest` | theorem | `P_w_source_acquisition_review_packet` | (no summary) |
| · | `T_w_source_acquisition_review_packet_rejects_observed_W_input` | theorem | `P_w_source_acquisition_review_packet` | (no summary) |
| · | `T_w_source_acquisition_review_packet_rejects_physical_export_request` | theorem | `P_w_source_acquisition_review_packet` | (no summary) |
| · | `T_w_source_acquisition_review_packet_rejects_template_flag` | theorem | `P_w_source_acquisition_review_packet` | (no summary) |
| · | `T_w_source_acquisition_review_packet_rejects_wrong_decision` | theorem | `P_w_source_acquisition_review_packet` | (no summary) |
| · | `T_w_source_acquisition_review_packet_report_locks_default_state` | theorem | `P_w_source_acquisition_review_packet` | (no summary) |
| · | `T_w_source_acquisition_review_packet_required_fields_complete` | theorem | `P_w_source_acquisition_review_packet` | (no summary) |
| · | `T_w_source_acquisition_review_packet_sections_declared` | theorem | `P_w_source_acquisition_review_packet` | (no summary) |
| · | `T_w_source_acquisition_review_packet_status_declared` | theorem | `P_w_source_acquisition_review_packet` | (no summary) |

## `apf/w_trace_source_authority_grading.py` — 13 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_w_trace_source_authority_acfw_grade_A` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_source_authority_all_comparison_have_payload_kind` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_source_authority_bank_closure` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_source_authority_cdf_measurement_quarantined` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_source_authority_cms_global_fit_admissible` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_source_authority_cms_measurement_quarantined` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_source_authority_dgg_cross_scheme` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_source_authority_gfitter_context_not_measurement` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_source_authority_has_prediction_sources` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_source_authority_matches_corr_points` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_source_authority_no_export` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_source_authority_no_measurements_as_sources` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_source_authority_status_declared` | theorem | `—` | (no summary) |

## `apf/w_trace_source_candidate_registry.py` — 28 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_w_source_candidate_registry_allowed_classes_declared` | theorem | `P_w_source_candidate_registry` | (no summary) |
| · | `T_w_source_candidate_registry_bank_closure` | theorem | `—` | (no summary) |
| · | `T_w_source_candidate_registry_candidate_classes_allowed` | theorem | `P_w_source_candidate_registry` | (no summary) |
| · | `T_w_source_candidate_registry_candidate_completion_predicate_accepts_promoted_independent_source` | theorem | `P_w_source_candidate_registry` | (no summary) |
| · | `T_w_source_candidate_registry_candidate_ids_unique` | theorem | `P_w_source_candidate_registry` | (no summary) |
| · | `T_w_source_candidate_registry_candidates_cover_all_components` | theorem | `P_w_source_candidate_registry` | (no summary) |
| · | `T_w_source_candidate_registry_candidates_not_acquired_by_default` | theorem | `P_w_source_candidate_registry` | (no summary) |
| · | `T_w_source_candidate_registry_completion_rejects_forbidden_input` | theorem | `P_w_source_candidate_registry` | (no summary) |
| · | `T_w_source_candidate_registry_completion_rejects_missing_digest` | theorem | `P_w_source_candidate_registry` | (no summary) |
| · | `T_w_source_candidate_registry_completion_rejects_partial_coverage` | theorem | `P_w_source_candidate_registry` | (no summary) |
| · | `T_w_source_candidate_registry_completion_rejects_template_shape_source` | theorem | `P_w_source_candidate_registry` | (no summary) |
| · | `T_w_source_candidate_registry_completion_rejects_unacquired_default` | theorem | `P_w_source_candidate_registry` | (no summary) |
| · | `T_w_source_candidate_registry_completion_rejects_wrong_review_status` | theorem | `P_w_source_candidate_registry` | (no summary) |
| · | `T_w_source_candidate_registry_depends_on_v114_template_pack` | theorem | `—` | (no summary) |
| · | `T_w_source_candidate_registry_doc_exists` | theorem | `P_w_source_candidate_registry` | (no summary) |
| · | `T_w_source_candidate_registry_doc_warns_no_real_rows` | theorem | `P_w_source_candidate_registry` | (no summary) |
| · | `T_w_source_candidate_registry_forbidden_inputs_declared` | theorem | `P_w_source_candidate_registry` | (no summary) |
| · | `T_w_source_candidate_registry_has_candidates` | theorem | `P_w_source_candidate_registry` | (no summary) |
| · | `T_w_source_candidate_registry_no_component_sum_certified` | theorem | `P_w_source_candidate_registry` | (no summary) |
| · | `T_w_source_candidate_registry_no_default_complete_imports` | theorem | `P_w_source_candidate_registry` | (no summary) |
| · | `T_w_source_candidate_registry_no_physical_export` | theorem | `P_w_source_candidate_registry` | (no summary) |
| · | `T_w_source_candidate_registry_preimport_steps_ordered` | theorem | `P_w_source_candidate_registry` | (no summary) |
| · | `T_w_source_candidate_registry_readiness_locked` | theorem | `P_w_source_candidate_registry` | (no summary) |
| · | `T_w_source_candidate_registry_report_exposes_adapter_fields` | theorem | `P_w_source_candidate_registry` | (no summary) |
| · | `T_w_source_candidate_registry_required_evidence_complete` | theorem | `P_w_source_candidate_registry` | (no summary) |
| · | `T_w_source_candidate_registry_source_classes_unique` | theorem | `P_w_source_candidate_registry` | (no summary) |
| · | `T_w_source_candidate_registry_status_declared` | theorem | `P_w_source_candidate_registry` | (no summary) |
| · | `T_w_source_candidate_registry_template_pack_locked` | theorem | `P_w_source_candidate_registry` | (no summary) |

## `apf/w_trace_standard_delta_r_extraction_worksheet.py` — 16 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_w_standard_delta_r_worksheet_bank_closure` | theorem | `P_w_standard_delta_r_extraction_worksheet` | (no summary) |
| · | `check_T_w_standard_delta_r_worksheet_bundle_admission_remains_empty` | theorem | `P_w_standard_delta_r_extraction_worksheet` | (no summary) |
| · | `check_T_w_standard_delta_r_worksheet_close_to_trace_neighborhood` | theorem | `P_w_standard_delta_r_extraction_worksheet` | (no summary) |
| · | `check_T_w_standard_delta_r_worksheet_component_sum_remains_uncertified` | theorem | `P_w_standard_delta_r_extraction_worksheet` | (no summary) |
| · | `check_T_w_standard_delta_r_worksheet_depends_on_acfw_extraction` | theorem | `P_w_standard_delta_r_extraction_worksheet` | (no summary) |
| · | `check_T_w_standard_delta_r_worksheet_depends_on_payload_schema` | theorem | `P_w_standard_delta_r_extraction_worksheet` | (no summary) |
| · | `check_T_w_standard_delta_r_worksheet_formula_declared` | theorem | `P_w_standard_delta_r_extraction_worksheet` | (no summary) |
| · | `check_T_w_standard_delta_r_worksheet_independent_inputs_only` | theorem | `P_w_standard_delta_r_extraction_worksheet` | (no summary) |
| · | `check_T_w_standard_delta_r_worksheet_no_physical_export_claim` | theorem | `P_w_standard_delta_r_extraction_worksheet` | (no summary) |
| · | `check_T_w_standard_delta_r_worksheet_not_component_decomposition` | theorem | `P_w_standard_delta_r_extraction_worksheet` | (no summary) |
| · | `check_T_w_standard_delta_r_worksheet_payload_minimal_schema_valid` | theorem | `P_w_standard_delta_r_extraction_worksheet` | (no summary) |
| · | `check_T_w_standard_delta_r_worksheet_promotion_obstruction_declared` | theorem | `P_w_standard_delta_r_extraction_worksheet` | (no summary) |
| · | `check_T_w_standard_delta_r_worksheet_readiness_remains_locked` | theorem | `P_w_standard_delta_r_extraction_worksheet` | (no summary) |
| · | `check_T_w_standard_delta_r_worksheet_source_digest_stable` | theorem | `P_w_standard_delta_r_extraction_worksheet` | (no summary) |
| · | `check_T_w_standard_delta_r_worksheet_status_declared` | theorem | `P_w_standard_delta_r_extraction_worksheet` | (no summary) |
| · | `check_T_w_standard_delta_r_worksheet_values_match_acfw_payload` | theorem | `P_w_standard_delta_r_extraction_worksheet` | (no summary) |

## `apf/w_trace_standard_delta_r_payload_schema.py` — 13 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_w_trace_standard_delta_r_payload_schema_bank_closure` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_standard_delta_r_payload_schema_common_fields_include_attestations` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_standard_delta_r_payload_schema_decomposition_requires_three_terms` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_standard_delta_r_payload_schema_decomposition_schema_valid` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_standard_delta_r_payload_schema_export_request_rejected` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_standard_delta_r_payload_schema_forbidden_rejected` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_standard_delta_r_payload_schema_locked_no_export` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_standard_delta_r_payload_schema_parametrization_requires_forward_policy` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_standard_delta_r_payload_schema_parametrization_schema_valid` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_standard_delta_r_payload_schema_payload_kinds_match_source_mapping` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_standard_delta_r_payload_schema_status_declared` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_standard_delta_r_payload_schema_total_schema_valid` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_standard_delta_r_payload_schema_unknown_schema_invalid` | theorem | `—` | (no summary) |

## `apf/w_trace_tensor_coefficient_map_scaffold.py` — 45 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_w_trace_tensor_coeff_b00_gate_closed` | theorem | `P_w_trace_tensor_coefficient_map_scaffold` | (no summary) |
| · | `check_T_w_trace_tensor_coeff_b00_mixed_finite` | theorem | `P_w_trace_tensor_coefficient_map_scaffold` | (no summary) |
| · | `check_T_w_trace_tensor_coeff_b00_route_finite` | theorem | `P_w_trace_tensor_coefficient_map_scaffold` | (no summary) |
| · | `check_T_w_trace_tensor_coeff_b1_gate_closed` | theorem | `P_w_trace_tensor_coefficient_map_scaffold` | (no summary) |
| · | `check_T_w_trace_tensor_coeff_b1_mixed_finite` | theorem | `P_w_trace_tensor_coefficient_map_scaffold` | (no summary) |
| · | `check_T_w_trace_tensor_coeff_b1_route_finite` | theorem | `P_w_trace_tensor_coefficient_map_scaffold` | (no summary) |
| · | `check_T_w_trace_tensor_coeff_b1_sensitive_to_mass_order` | theorem | `P_w_trace_tensor_coefficient_map_scaffold` | (no summary) |
| · | `check_T_w_trace_tensor_coeff_bank_closure` | theorem | `P_w_trace_tensor_coefficient_map_scaffold` | (no summary) |
| · | `check_T_w_trace_tensor_coeff_basis_all_finite` | theorem | `P_w_trace_tensor_coefficient_map_scaffold` | (no summary) |
| · | `check_T_w_trace_tensor_coeff_basis_contains_c0_d0` | theorem | `P_w_trace_tensor_coefficient_map_scaffold` | (no summary) |
| · | `check_T_w_trace_tensor_coeff_basis_count` | theorem | `P_w_trace_tensor_coefficient_map_scaffold` | (no summary) |
| · | `check_T_w_trace_tensor_coeff_counterterm_target_range` | theorem | `P_w_trace_tensor_coefficient_map_scaffold` | (no summary) |
| · | `check_T_w_trace_tensor_coeff_dependency_pass` | theorem | `P_w_trace_tensor_coefficient_map_scaffold` | (no summary) |
| · | `check_T_w_trace_tensor_coeff_dizet_total_range` | theorem | `P_w_trace_tensor_coefficient_map_scaffold` | (no summary) |
| · | `check_T_w_trace_tensor_coeff_first_failed_gate_exact` | theorem | `P_w_trace_tensor_coefficient_map_scaffold` | (no summary) |
| · | `check_T_w_trace_tensor_coeff_forbidden_claims_present` | theorem | `P_w_trace_tensor_coefficient_map_scaffold` | (no summary) |
| · | `check_T_w_trace_tensor_coeff_forbids_full_native_claim` | theorem | `P_w_trace_tensor_coefficient_map_scaffold` | (no summary) |
| · | `check_T_w_trace_tensor_coeff_gate_count` | theorem | `P_w_trace_tensor_coefficient_map_scaffold` | (no summary) |
| · | `check_T_w_trace_tensor_coeff_mass_counterterm_open` | theorem | `P_w_trace_tensor_coefficient_map_scaffold` | (no summary) |
| · | `check_T_w_trace_tensor_coeff_mw_residual_preserved` | theorem | `P_w_trace_tensor_coefficient_map_scaffold` | (no summary) |
| · | `check_T_w_trace_tensor_coeff_native_status_open` | theorem | `P_w_trace_tensor_coefficient_map_scaffold` | (no summary) |
| · | `check_T_w_trace_tensor_coeff_next_gate_exact` | theorem | `P_w_trace_tensor_coefficient_map_scaffold` | (no summary) |
| · | `check_T_w_trace_tensor_coeff_no_fit_guard_closed` | theorem | `P_w_trace_tensor_coefficient_map_scaffold` | (no summary) |
| · | `check_T_w_trace_tensor_coeff_no_fitted_coefficient_claim` | theorem | `P_w_trace_tensor_coefficient_map_scaffold` | (no summary) |
| · | `check_T_w_trace_tensor_coeff_open_gates_block_native` | theorem | `P_w_trace_tensor_coefficient_map_scaffold` | (no summary) |
| · | `check_T_w_trace_tensor_coeff_open_slots_present` | theorem | `P_w_trace_tensor_coefficient_map_scaffold` | (no summary) |
| · | `check_T_w_trace_tensor_coeff_partial_slots_present` | theorem | `P_w_trace_tensor_coefficient_map_scaffold` | (no summary) |
| · | `check_T_w_trace_tensor_coeff_payload_digest_present` | theorem | `P_w_trace_tensor_coefficient_map_scaffold` | (no summary) |
| · | `check_T_w_trace_tensor_coeff_report_has_basis` | theorem | `P_w_trace_tensor_coefficient_map_scaffold` | (no summary) |
| · | `check_T_w_trace_tensor_coeff_report_has_gates` | theorem | `P_w_trace_tensor_coefficient_map_scaffold` | (no summary) |
| · | `check_T_w_trace_tensor_coeff_report_has_slots` | theorem | `P_w_trace_tensor_coefficient_map_scaffold` | (no summary) |
| · | `check_T_w_trace_tensor_coeff_reviewed_table_open` | theorem | `P_w_trace_tensor_coefficient_map_scaffold` | (no summary) |
| · | `check_T_w_trace_tensor_coeff_route_export_candidate_preserved` | theorem | `P_w_trace_tensor_coefficient_map_scaffold` | (no summary) |
| · | `check_T_w_trace_tensor_coeff_safe_claims_present` | theorem | `P_w_trace_tensor_coefficient_map_scaffold` | (no summary) |
| · | `check_T_w_trace_tensor_coeff_schema_gate_closed` | theorem | `P_w_trace_tensor_coefficient_map_scaffold` | (no summary) |
| · | `check_T_w_trace_tensor_coeff_sigma_preserved` | theorem | `P_w_trace_tensor_coefficient_map_scaffold` | (no summary) |
| · | `check_T_w_trace_tensor_coeff_slot_blockers_present` | theorem | `P_w_trace_tensor_coefficient_map_scaffold` | (no summary) |
| · | `check_T_w_trace_tensor_coeff_slot_count` | theorem | `P_w_trace_tensor_coefficient_map_scaffold` | (no summary) |
| · | `check_T_w_trace_tensor_coeff_status_declared` | theorem | `P_w_trace_tensor_coefficient_map_scaffold` | (no summary) |
| · | `check_T_w_trace_tensor_coeff_target_closure_zero` | theorem | `P_w_trace_tensor_coefficient_map_scaffold` | (no summary) |
| · | `check_T_w_trace_tensor_coeff_tensor_primitive_count` | theorem | `P_w_trace_tensor_coefficient_map_scaffold` | (no summary) |
| · | `check_T_w_trace_tensor_coeff_tensor_primitives_admitted` | theorem | `P_w_trace_tensor_coefficient_map_scaffold` | (no summary) |
| · | `check_T_w_trace_tensor_coeff_tensor_values_not_all_zero` | theorem | `P_w_trace_tensor_coefficient_map_scaffold` | (no summary) |
| · | `check_T_w_trace_tensor_coeff_terminal_report_status` | theorem | `P_w_trace_tensor_coefficient_map_scaffold` | (no summary) |
| · | `check_T_w_trace_tensor_coeff_vertex_box_open` | theorem | `P_w_trace_tensor_coefficient_map_scaffold` | (no summary) |

## `apf/w_trace_terminal_state_report.py` — 13 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_w_trace_terminal_state_report_bank_closure` | theorem | `—` | (no summary) |
| · | `T_w_trace_terminal_state_report_closed_layers_listed` | theorem | `—` | (no summary) |
| · | `T_w_trace_terminal_state_report_delta_r_target_preserved` | theorem | `—` | (no summary) |
| · | `T_w_trace_terminal_state_report_export_locked` | theorem | `—` | (no summary) |
| · | `T_w_trace_terminal_state_report_micro_gate_diminishing_returns_flagged` | theorem | `—` | (no summary) |
| · | `T_w_trace_terminal_state_report_no_more_scaffolding_stop_condition_declared` | theorem | `—` | (no summary) |
| · | `T_w_trace_terminal_state_report_no_target_observable_consumption` | theorem | `—` | (no summary) |
| · | `T_w_trace_terminal_state_report_open_physics_items_listed` | theorem | `—` | (no summary) |
| · | `T_w_trace_terminal_state_report_physical_export_open_not_closed` | theorem | `—` | (no summary) |
| · | `T_w_trace_terminal_state_report_source_data_next_phase_declared` | theorem | `—` | (no summary) |
| · | `T_w_trace_terminal_state_report_status_declared` | theorem | `—` | (no summary) |
| · | `T_w_trace_terminal_state_report_terminal_report_serializable` | theorem | `—` | (no summary) |
| · | `T_w_trace_terminal_state_report_w_trace_value_preserved` | theorem | `—` | (no summary) |

## `apf/w_trace_uncertainty_propagation.py` — 24 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_w_uncertainty_propagation_apf_anchor_comparison_only` | theorem | `—` | (no summary) |
| · | `T_w_uncertainty_propagation_bank_closure` | theorem | `—` | (no summary) |
| · | `T_w_uncertainty_propagation_component_order_matches_skeleton` | theorem | `—` | (no summary) |
| · | `T_w_uncertainty_propagation_computes_sigma_delta_r` | theorem | `—` | (no summary) |
| · | `T_w_uncertainty_propagation_covariance_shape_ok` | theorem | `—` | (no summary) |
| · | `T_w_uncertainty_propagation_depends_on_component_sum_harness` | theorem | `—` | (no summary) |
| · | `T_w_uncertainty_propagation_diagonal_nonnegative_required` | theorem | `—` | (no summary) |
| · | `T_w_uncertainty_propagation_dry_path_certifies_mechanics_only` | theorem | `—` | (no summary) |
| · | `T_w_uncertainty_propagation_empty_by_default` | theorem | `—` | (no summary) |
| · | `T_w_uncertainty_propagation_jacobian_required_for_W_pushforward` | theorem | `—` | (no summary) |
| · | `T_w_uncertainty_propagation_manifest_remains_open` | theorem | `—` | (no summary) |
| · | `T_w_uncertainty_propagation_no_physical_mass_exports` | theorem | `—` | (no summary) |
| · | `T_w_uncertainty_propagation_policy_blocks_export` | theorem | `—` | (no summary) |
| · | `T_w_uncertainty_propagation_rejects_apf_anchor_covariance_input` | theorem | `—` | (no summary) |
| · | `T_w_uncertainty_propagation_rejects_asymmetric_covariance` | theorem | `—` | (no summary) |
| · | `T_w_uncertainty_propagation_rejects_bad_shape` | theorem | `—` | (no summary) |
| · | `T_w_uncertainty_propagation_rejects_negative_variance` | theorem | `—` | (no summary) |
| · | `T_w_uncertainty_propagation_rejects_observed_w_uncertainty_input` | theorem | `—` | (no summary) |
| · | `T_w_uncertainty_propagation_rejects_physical_export_request` | theorem | `—` | (no summary) |
| · | `T_w_uncertainty_propagation_requires_component_sum_certified` | theorem | `—` | (no summary) |
| · | `T_w_uncertainty_propagation_requires_rows_admitted` | theorem | `—` | (no summary) |
| · | `T_w_uncertainty_propagation_schema_declared` | theorem | `—` | (no summary) |
| · | `T_w_uncertainty_propagation_status_declared` | theorem | `—` | (no summary) |
| · | `T_w_uncertainty_propagation_symmetric_required` | theorem | `—` | (no summary) |

## `apf/w_trace_v142_physics_validation_sprint_report.py` — 13 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_w_trace_v142_all_real_export_locked` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_v142_bank_closure` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_v142_crosscheck_module_passes` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_v142_has_three_sprint_modules` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_v142_multisource_module_passes` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_v142_no_component_sum_claim` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_v142_no_covariance_claim` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_v142_second_source_family_present` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_v142_status_declared` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_v142_stress_module_passes` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_v142_verdict_got_there` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_v142_weighted_gap_less_than_1p2sigma` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_v142_weighted_gap_small` | theorem | `—` | (no summary) |

## `apf/w_trace_v143_physics_deep_validation_report.py` — 13 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_w_trace_v143_report_bank_closure` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_v143_report_cdf_not_source` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_v143_report_cms_context_present` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_v143_report_cms_measurement_not_source` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_v143_report_correlated_model_present` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_v143_report_four_source_context` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_v143_report_gap_few_mev` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_v143_report_gap_under_1p5sigma` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_v143_report_measurements_quarantined` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_v143_report_next_is_physics_or_paper` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_v143_report_no_export` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_v143_report_pull_diagnostics_green` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_v143_report_status_declared` | theorem | `—` | (no summary) |

## `apf/w_trace_v144_publication_validation_report.py` — 13 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_w_trace_v144_report_authority_present` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_v144_report_bank_closure` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_v144_report_claim_language_safe` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_v144_report_gap_few_mev` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_v144_report_measurements_quarantined` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_v144_report_next_is_paper_or_payload` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_v144_report_no_component_certification` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_v144_report_no_covariance_certification` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_v144_report_no_export` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_v144_report_preferred_sentence_no_export` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_v144_report_residual_green` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_v144_report_robustness_green` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_v144_report_status_declared` | theorem | `—` | (no summary) |

## `apf/w_trace_v14_physics_sprint_terminal_report.py` — 13 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `check_T_w_trace_v14_physics_sprint_terminal_report_bank_closure` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_v14_physics_sprint_terminal_report_five_modules_listed` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_v14_physics_sprint_terminal_report_includes_acfw` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_v14_physics_sprint_terminal_report_includes_comparison` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_v14_physics_sprint_terminal_report_includes_denner_sirlin` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_v14_physics_sprint_terminal_report_includes_payload_schema` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_v14_physics_sprint_terminal_report_includes_stop_condition` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_v14_physics_sprint_terminal_report_locked_no_export` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_v14_physics_sprint_terminal_report_next_artifact_real_payload` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_v14_physics_sprint_terminal_report_no_export` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_v14_physics_sprint_terminal_report_no_payload_admitted` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_v14_physics_sprint_terminal_report_status_declared` | theorem | `—` | (no summary) |
| · | `check_T_w_trace_v14_physics_sprint_terminal_report_terminal_status_no_more_scaffold` | theorem | `—` | (no summary) |

## `apf/wg2_dictionary_typing_no_go.py` — 3 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `L_wg2_dictionary_index_content_blind_native` | lemma | `P_structural` | Under the .354/.359 record-partition (called live: check_L_completion_angle_content_blind_native, [P_structural]), the w propto g^n dictionary index is NO-RECORD (zero native capacity gain; C_total = 61 for every probed n) and CONTENT-BLIND: completions at n=2 and n=4 share every native-preserved... |
| · | `T_mcross_gate_dictionary_conditional` | theorem | `P_structural` | The banked forward solve (_alpha_s_forward, abelian_coupling_capacity_count.py) supplies t = ln(M_cross/M_Z) = 34.59 from the counts alone -- so the fence clause "which the counts do not supply" was half-stale -- BUT the supplied t is dictionary-index-conditional in its very formulation: the rati... |
| · | `T_wg2_dictionary_index_no_native_consumer_census` | theorem | `—` | (no summary) |

## `apf/yang_mills_gap.py` — 6 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_OS_structure_SU2` | theorem | `[P_structural]` | Composed-master witness for the OS axiomatic structure of SU(2) Wilson Yang-Mills lattice gauge theory in d = 3 and d = 4 at all coupling beta > 0.  Verifies the entire dependency chain: Paper 29 PRD (SU(2) + SU(3) cascade + adjoint Step 3) -> Paper 30 mass gap (kappa_3 negativity, d=3 Turan, d=4... |
| · | `T_PRD_SU2_Bessel` | theorem | `[P_structural]` | Plaquette Representation Dominance for SU(2): the fundamental (spin-1/2) Wilson character coefficient strictly exceeds all higher-spin coefficients for all beta > 0.  Reduction: PRD <=> I_n(beta) > I_{n+1}(beta) for n >= 0, which follows from the Turan inequality.  Bank witness verifies both legs... |
| · | `T_PRD_SU3_Casimir_cascade` | theorem | `[P_structural]` | Full PRD for SU(3) reduces (via Casimir cascade + weak-coupling ordering) to PRD for the adjoint, which Paper 29 Theorem thm:osc_su3 proves via exact elliptic-integral reduction.  Bank witness verifies the Casimir cascade combinatorics: C_{(p,q)} >= C_adj = 3 for every (p,q) other than fund and a... |
| · | `T_PRD_SU3_adjoint_step3` | theorem | `[P_structural]` | Polynomial sign inequality at the heart of Paper 29 Theorem thm:osc_su3 Step 3: the cubic q(v) = 3v^3 - 11v^2 + 18 changes sign at v_c approx 1.786 and at v = 3, with q < 0 on the intervening interval.  This algebraic content licenses the elliptic-reduction step that proves OSC for the SU(3) adjo... |
| · | `T_mass_gap_SU2_d3` | theorem | `[P_structural]` | All-beta mass gap for SU(2) Wilson lattice in d = 3, structurally witnessed.  lambda_1 < 4/27 uniformly in beta, hence Delta(beta) >= log(27/4) > 0.  The Turan-based tail bound that closes the argument depends on kappa_3(beta) < 0 for all beta > 0, which is witnessed by the companion check_T_kapp... |
| · | `T_mass_gap_SU2_d4` | theorem | `[P_structural]` | All-beta mass gap for SU(2) Wilson lattice in d = 4, structurally witnessed.  Paper 30 Theorem thm:comparison establishes the comparison inequality chi_4 <= 1.11 * chi_3 via Schur test on plaquette independence + conditional variance + recoupling deficit.  Combined with the d=3 bound and the one-... |

## `apf/yang_mills_kappa3.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_kappa3_negative_all_beta` | theorem | `[P_structural]` | Witness for kappa_3(beta) < 0 for all beta > 0, where kappa_3 = d^3/dbeta^3 log(I_1(beta)/beta).  Three sampling phases (small / mid / large beta) plus algebraic consistency of the Riccati formula r'(beta) = 1 - r^2 + r/beta against numerical d/dbeta of kappa_3.  Full certified-interval-block ver... |

## `apf/yang_mills_md_bridge.py` — 8 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_contextuality_implies_superadditive_cost` | theorem | `—` | (no summary) |
| · | `T_su2_single_plaquette_curvature_exact` | theorem | `P` | Exact curvature-dimension tensor of the SU(2) single-plaquette/heat-bath measure: A = (2 + h cos phi) g, isotropic, from Ric(S^3)=2 and Obata's Hess(cos phi)=-cos phi.g. Threshold h=2. A diagonal single-site fact; the mass-gap off-diagonal assembly is open and the Otto-Reznikoff tensorization to ... |
| · | `T_su2_single_site_uniform_gap_drift` | theorem | `—` | (no summary) |
| · | `T_ym_conformal_phase_excluded_by_record_locking` | theorem | `P_structural_reading` | The symmetry/geometry/record-locking closure of the confining-vs-conformal question. Non-abelian composition is superadditive (L_cost + record theorem, Delta>0: the non-abelian colour record is the non-factorizable entangled singlet); the abelian case is additive (Delta=0), which is why U(1) is C... |
| · | `T_ym_gap_positivity_from_MD` | theorem | `P_structural_reading` | The ep* bridge, banked at the honest conditional level. L_epsilon_star [P] proves the Minimum-Distinction realignment floor eps_min(Gamma) > 0 ('zero isolated from the spectrum'). Via the OS2 reflection-positive transfer matrix T = exp(-aH) (self-adjoint H >= 0, vacuum at 0) the lightest excitati... |
| · | `T_ym_ir_endpoint_trichotomy_branch2_open` | theorem | `P_structural_reading` | Under named readings R1(i)-(iii) (RG step = continuation; commitment inheritance; budget constancy -- none banked), the matter-free IR ledger terminates in exactly one of: saturation (exact under L_cost quantization: slack < eps* <=> slack = 0; <= C strict increments), the INERT RECORD-LOCKED PLA... |
| · | `T_ym_lattice_substrate_admissible` | theorem | `P` | Places the Wilson lattice inside the APF substrate framework at [P]. The Wilson action is reflection-positive (Osterwalder-Seiler, exact on the lattice), so OS reconstruction gives a genuine Hilbert space and a bounded positive transfer matrix -- the lattice is a real finite causal region. A1 the... |
| · | `T_ym_meaningful_spectrum_is_singlet_gapped` | theorem | `P_structural_reading` | Ties the ep* bridge to the already-banked confinement theorem and closes the Route-3 soft-mode loophole. T_confinement [P] (AF + finite capacity + MD) excludes non-singlet states at IR saturation, so the meaningful (gauge-invariant, robust) IR spectrum is the singlet spectrum. Massless gluons, be... |

## `apf/ym_quotient_ledger.py` — 8 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `L_ym_orbit_unpinnable` | lemma | `P_structural_instrument` | On the Q8 single-loop gauge model, an exhaustive scan of all 256 separators shows the covariant ones are exactly the 32 class functions and every orbit-mate separator is non-covariant; the ungauged control admits orbit-mate separators. The YM-quotient instance of the promoted GQL-1 chain: gauge-o... |
| · | `T_demand_not_routing_readable` | theorem | `P` | Three exact algebraic facts on the banked competition form: the solution moves at fixed Gram (V1, d w_1*/d Delta = -x/m); a unit demand draws distinct inverse-Gram columns by row at one identical routing structure (so no routing column carries a demand's funding); and the extra-loads readback ret... |
| · | `T_det_gram_is_pair_count` | theorem | `P` | Cauchy-Binet on A = D^T diag(1/C) D: det A is the sum of squared 2x2 routing minors over edge pairs, each term per-edge-gauge invariant -- an exact identity in every realization (verified on the census and on both CX countermodels). T22's banked det A = m is thereby read: in the audited census ex... |
| · | `T_routing_parallel_interface_conditional` | theorem | `P_structural_instrument` | Conditional on T22's internal-block premise (m = 3 internal sector-2 edges at unit contribution), the dressed Gram (1, 1/2, 13/4) FORCES the routing-parallel interface: S_11 = 1 (no private U(1) support), shared profiles parallel (Cauchy-Schwarz equality case), one shared capacity direction. The ... |
| · | `T_sector_granularity_below_billing_type` | theorem | `P_structural_instrument` | The canonical billing vocabulary types every billing locus at interface granularity (row 7b; the Paper 3 TS coincidence sentence); transformation-typing cannot supply sector granularity because template-invariant content carries the trivial rho_Gamma-label (executed exactly on the finite model, w... |
| · | `T_ub_consistency_three_record_states` | theorem | `P_structural_instrument` | The banked sector loads against the maintenance-demand column (0, 1, 0): U(1) carries no record term (r_1 = 0, photon no-record); SU(2) carries exactly the condensate's Delta = 1 (r_2 = gamma_2 - a_22 = 1); the colour record has value-pin count 0 and its gamma_3 = 6 is trace-grounded outside the ... |
| · | `T_ym_demand_count_resolution_independent` | theorem | `P_structural_instrument` | Subdividing the Q8 loop into two links: the coarse map is surjective (uniform fibers, exhibited), the pulled-back presence fact is invariant under both fine gauge parameters, and the pinned count is preserved 1 -> 1. The demand count is a resolution-independent quotient quantity, not an artifact ... |
| · | `T_ym_record_demand_is_pinned_count` | theorem | `P_structural_instrument` | On the Q8 model the presence fact pins exactly 1 distinction against the full admissible space (2-cell invariant partition); the tautology control (restricted space: 0 pins) and the dependent-pin control (minimal generating count: {f1, f2, f1 OR f2} has k_pin = 2) both execute exactly. Demand = k... |

## `apf/yt_absolute_scale_normalization_no_go.py` — 1 checks (0 bundled)

| Bundled | Name | Kind | Tag | Summary |
|---|---|---|---|---|
| · | `T_yt_absolute_scale_not_fixable_by_normalization_no_go` | theorem | `P_structural_yt_absolute_scale_normalization_no_go` | Negative result fencing off route (a). The inter-generation Yukawa ratios (y_g/y_t = x^{q(g)}) and the mixing angle (normalized Gram correlation → 3/13) are native and basis-invariant; the open piece is the absolute top Yukawa y_t. Route (a) asked whether a unitarity / normalized-overlap principl... |

---

## How to use this catalog

- **Grep for a check:** `grep -i 'keyword' THEOREMS.md` or use `theorems.json` with `jq`.
- **Load as data:** `python -c "import json; data = json.load(open('ai_context/theorems.json')); print([e for e in data['entries'] if 'keyword' in e['summary'].lower()])"`.
- **Find all [P] theorems in a module:** `jq '.entries[] | select(.module == "core" and .epistemic == "P") | .name' ai_context/theorems.json`.
- **List all bundled checks:** `jq '.entries[] | select(.bundled_in_this_repo) | .name' ai_context/theorems.json`.

*Generated by `create-repo` from the canonical codebase. Counts are authoritative at release time; the live codebase in `__APF Library/Codebase/APF_Codebase_v<version>/` is the source of truth for the current state.*
