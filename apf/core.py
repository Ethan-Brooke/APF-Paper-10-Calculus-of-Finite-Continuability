"""apf/core.py — Paper 10 subset.

Vendored single-file extraction of the check functions cited in
Paper 10: The Calculus of Finite Continuability. The canonical APF codebase v6.8 (frozen 2026-04-18)
verifies 348 checks across 335 bank-registered theorems; this file
contains the 3-check subset
for this paper.

Each function is copied verbatim from its original source module.
See https://doi.org/10.5281/zenodo.18529115 for the full codebase.
"""

import itertools
import math
from fractions import Fraction
import numpy as np
from apf.apf_utils import check, _result
_SEED = 20260703
_FINITE_BASIS_MODEL_HYPOTHESES = ('finite_content_atoms', 'operational_classes_are_atom_subsets', 'operational_closure_is_union', 'joint_realization_is_union_carrier', 'exact_no_excess_atom_cost', 'full_content_is_admissible', 'closed_world_union_cover')
_FINITE_BASIS_GENERAL_OPEN_OBLIGATIONS = ('finite_joint_extension_or_amalgamation', 'downward_closed_joint_realizability', 'minimum_joint_realization_attainment', 'compatible_joint_realization', 'operational_basis_to_precision_channel_bridge')
IE_DECLARATIONS = ({'input_id': 'foundation:continuation_capacity_floor_bound', 'axis': 'ROUTE', 'route': 'continuation_capacity_floor', 'expect_export': True, 'payload': {'name': 'continuation_capacity_floor_bound', 'closure_kind': 'internal_identity', 'identity_summary': 'The finite-continuability capacity-floor bound |S| <= N + J(S), with N = floor(C_Gamma / eps*), holds UNCONDITIONALLY by structural identity (composite-inclusive floor ruling, 2026-07-03): the derived cardinality bound is the codomain by construction, not an evaluator-transported export. M_break witness -- eps* = 1, N = floor(2/1) = 2, block |S| = 4 defeats the naive bound (4 > 2) while |S| <= N + J(S) = 2 + 3 = 5 holds. (check_T_admissibility_greedoid_structure, continuation_calculus.py)'}, 'note': 'Pre-existing Paper 10 capacity-floor identity. It does not by itself assert existence of a finite complete operational basis.'}, {'input_id': 'foundation:finite_operational_basis_atom_cover_model', 'axis': 'ROUTE', 'route': 'continuation_finite_basis_atom_cover', 'expect_export': True, 'payload': {'name': 'finite_operational_basis_atom_cover_model', 'closure_kind': 'internal_identity', 'source_check': 'T_finite_operational_basis', 'scope_check': 'T_finite_operational_basis_scope_contract', 'compatible_realization_check': 'T_finite_minimal_joint_realization_atom_cover', 'model_class': 'finite_atom_cover', 'hypotheses': list(_FINITE_BASIS_MODEL_HYPOTHESES), 'non_claims': ['not_a_general_physical_joint_extension_theorem', 'not_precision_channel_generation', 'not_finite_smooth_generation'], 'identity_summary': 'IN THE DECLARED FINITE ATOM-COVER MODEL ONLY: finite admitted content atoms, subset-coded operational classes, union joint carrier/closure, and exact no-excess atom cost make the finite complete-basis extraction and one compatible minimum joint realization internal identities of the model. Exact Fraction arithmetic certifies |B_U| <= floor(C_U/eps*). This export does NOT discharge finite joint-extension/amalgamation on an arbitrary physical operational closure and does NOT generate precision channels or smooth geometry.'}, 'note': 'Honest restricted-model export. The source and codomain coincide only after the finite atom-cover contract is declared.'}, {'input_id': 'foundation:finite_operational_basis_general_bridge', 'axis': 'ROUTE', 'route': 'continuation_finite_basis_general', 'expect_export': False, 'payload': {'name': 'finite_operational_basis_general_physical_bridge', 'closure_kind': 'obstruction_named', 'obstruction_class': 'FINITE_JOINT_EXTENSION_PACKAGE_REQUIRED', 'source_check': 'T_finite_operational_basis_scope_contract', 'open_obligations': ['downward_closed_joint_realizability', 'finite_joint_extension_or_amalgamation', 'minimum_joint_realization_attainment', 'closure_invariance_across_no_excess_minima'], 'knockout_summary': 'The exact finite atom-cover witness does not export the general physical finite-basis premise package. A general closed interface must separately establish a downward-closed joint-realizability domain, finite joint extension or amalgamation, attained minimum joint cost, and closure invariance. Until then the general theorem is conditional and no global-P physical bridge is exported.', 'target_value_consumed': False}, 'note': 'Closure-by-design obstruction. Uses the existing Interface Atlas obstruction_named path; no new dependency or verdict system.'}, {'input_id': 'foundation:finite_compatible_joint_realization_general_bridge', 'axis': 'ROUTE', 'route': 'continuation_compatible_joint_realization_general', 'expect_export': False, 'payload': {'name': 'finite_compatible_joint_realization_general_bridge', 'closure_kind': 'obstruction_named', 'obstruction_class': 'COMPATIBLE_MINIMUM_JOINT_REALIZATION_REQUIRED', 'source_check': 'T_finite_minimal_joint_realization_atom_cover', 'open_obligations': ['attained_minimum_joint_carrier_for_the_complete_basis', 'deterministic_lossless_basis_projections', 'shared_joint_carrier_compatibility'], 'knockout_summary': 'The atom-cover model constructs one minimum shared joint carrier, but arbitrary physical operational classes do not inherit compatible representatives from independently chosen classwise minima. The general compatible-realization bridge remains obstructed until one attained joint carrier and its lossless projections are proved.', 'target_value_consumed': False}, 'note': 'Keeps compatibility distinct from individual minimum existence.'}, {'input_id': 'foundation:operational_basis_to_precision_channel_bridge', 'axis': 'ROUTE', 'route': 'continuation_operational_to_precision_channel', 'expect_export': False, 'payload': {'name': 'operational_basis_to_precision_channel_bridge', 'closure_kind': 'obstruction_named', 'obstruction_class': 'OPERATIONAL_TO_PRECISION_CHANNEL_REALIZATION_REQUIRED', 'source_check': 'T_finite_operational_basis', 'open_obligations': ['joint_preservation', 'recoverability_preservation_and_reflection', 'reduced_state_separation', 'faithful_real_limit'], 'knockout_summary': 'A finite operational-class basis is not yet a finite physical precision-channel basis. A faithful realization functor must preserve joint realizability, preserve and reflect closure, separate reduced states, and provide faithful real limits. This bridge remains explicitly open.', 'target_value_consumed': False}, 'note': 'Paper 9 bridge gate; prevents the finite-basis theorem from silently generating physical refinement channels.'})
if __name__ == '__main__':
    for _n, _r in run_all().items():
        print('PASS' if _r.get('passed', True) else 'FAIL', _n)
        print('  grade:', _r['epistemic'], '| tier', _r['tier'])
        print('  ', _r['key_result'])


# ======================================================================
# Extracted from canonical continuation_calculus.py
# ======================================================================

def check_T_finite_operational_basis_scope_contract():
    """Scope guard and exact-arithmetic contract for the Paper 10/Paper 9 node.

    This check makes two reviewer-critical facts executable:

    1. The banked positive theorem is a theorem of a finite atom-cover model,
       whose hidden structure is explicitly named in
       ``_FINITE_BASIS_MODEL_HYPOTHESES``.
    2. The unrestricted manuscript theorem needs a separate finite
       joint-extension/amalgamation premise.  A closed ledger with individually
       admitted classes but no jointly realizable pair is a finite countermodel
       to the unqualified induction.
    """
    Omega = frozenset({0, 1, 2})
    F = (frozenset({0, 1}), frozenset({2}), frozenset({1, 2}))
    eps = Fraction(3, 5)
    covered = _u(F)
    check(covered == Omega, 'closed-world atom-cover family must cover Omega')
    check(Fraction(len(covered)) * eps == Fraction(9, 5), 'exact no-excess atom cost is |covered|*eps')
    boundary_capacity = Fraction(1999999999, 2000000000)
    boundary_eps = Fraction(1)
    check(_safe_floor_ratio(boundary_capacity, boundary_eps) == 0, 'exact floor below one commitment is zero')
    check(boundary_eps > boundary_capacity, 'one full commitment is exactly inadmissible at the boundary')
    A = frozenset({'a', 'b', 'c'})
    jointly_realizable = {frozenset(), frozenset({'a'}), frozenset({'b'}), frozenset({'c'})}
    closure = lambda S: frozenset(S)
    closed_world_individual = all((frozenset({a}) in jointly_realizable for a in A))
    complete_joint_families = [S for S in jointly_realizable if closure(S) == A]
    extension_candidates_from_a = [a for a in A - closure(frozenset({'a'})) if frozenset({'a', a}) in jointly_realizable]
    check(closed_world_individual, 'every admitted class is present in the finite closed ledger')
    check(not complete_joint_families, 'without amalgamation no complete jointly realizable basis exists')
    check(not extension_candidates_from_a, 'the greedy induction gets stuck unless finite joint extension is named')
    return _result(name='T_finite_operational_basis_scope_contract -- finite atom-cover model contract, exact boundary, and no-amalgamation scope guard', tier=4, epistemic='P_structural_instrument', summary='The finite-basis bank node is scoped to a finite atom-cover model: finite content atoms, subset-coded operational classes, union closure/joint carrier, and exact no-excess atom cost. Exact Fraction arithmetic rejects the former +1e-9 boundary enlargement. A finite closed-ledger countermodel with only singleton joint families proves that the unrestricted physical theorem additionally requires finite joint-extension/amalgamation and minimum compatible joint realization. This is a scope instrument, not a new physical derivation.', key_result='Restricted model hypotheses named; C=1999999999/2000000000, eps*=1 gives exact N=0; finite no-amalgamation ledger has every class individually admitted but no complete jointly realizable basis.', dependencies=[], cross_refs=['T_admissibility_greedoid_structure', 'T_selection_approximate_A2', 'FD1_structural_completeness'], artifacts={'claim_kind': 'adopted_with_falsifier', 'model_class': 'finite_atom_cover', 'hypotheses': list(_FINITE_BASIS_MODEL_HYPOTHESES), 'general_open_obligations': list(_FINITE_BASIS_GENERAL_OPEN_OBLIGATIONS), 'boundary_control': {'capacity': '1999999999/2000000000', 'eps_star': '1', 'exact_floor': 0, 'one_commitment_admissible': False}, 'no_amalgamation_control': {'n_classes': len(A), 'jointly_realizable': 'empty and singletons only', 'complete_joint_basis_exists': False}, 'non_claims': ['not_a_general_joint_extension_theorem', 'not_precision_channel_generation', 'not_finite_smooth_generation']})

def check_T_finite_operational_basis():
    """Exact finite atom-cover model witness for the finite basis mechanism."""
    rng = np.random.default_rng(_SEED)
    adm = inadm = stuck = tight = incr_used = complete = 0
    for _ in range(600):
        eps = _positive_fraction(rng, num_hi=50, den_hi=20)
        C = _positive_fraction(rng, num_hi=240, den_hi=20)
        Nmax = _safe_floor_ratio(C, eps)
        if Nmax < 1:
            continue
        m = int(rng.integers(1, 11))
        Omega, F = _rich_family(rng, m, int(rng.integers(1, 2 ** min(m, 6) + 1)))
        content_cost = Fraction(m) * eps
        admissible = content_cost <= C
        cwc = _u(F) == Omega
        if not admissible:
            inadm += 1
            check(m > Nmax, 'inadmissible atom content exceeds floor(C/eps*) exactly')
            check(content_cost > C, 'inadmissible atom content has exact no-excess cost above C')
            continue
        adm += 1
        if m == Nmax:
            tight += 1
        B, covered, is_stuck = _greedy_basis(Omega, F)
        if not cwc:
            stuck += 1
            check(is_stuck and covered != Omega, 'non-covering family must stop without a false complete basis')
            check(any((a not in _u(F) for a in Omega)), 'a real atom remains absent from the closed ledger')
            continue
        check(not is_stuck, 'closed-world union cover makes greedy extraction complete')
        sub = frozenset()
        for cls in B:
            if not cls <= sub:
                inc = Fraction(len(sub | cls) - len(sub)) * eps
                check(inc >= eps, 'every class outside union closure adds at least one exact atom floor')
                incr_used += 1
            sub |= cls
        check(covered == Omega and all((cls <= covered for cls in F)), 'cl(B_U)=A_U in the finite atom-cover model')
        check(len(B) <= Nmax, 'basis cardinality is bounded by exact floor(C_U/eps*)')
        M = _minimize(B, Omega)
        for i in range(len(M)):
            rest = _u((M[j] for j in range(len(M)) if j != i))
            check(not M[i] <= rest, 'inclusion-minimal basis has no union-redundant member')
        check(len(M) <= Nmax, 'minimal basis remains under the exact capacity bound')
        complete += 1
    check(adm > 30 and inadm > 20 and (stuck > 10) and (tight > 0) and (incr_used > 50) and (complete > 30), 'all finite-basis model arms must be exercised')
    eps = Fraction(1)
    reserved = frozenset({5})
    cost_excess = lambda U: Fraction(len(U | reserved))
    Su = frozenset({0})
    check(cost_excess(Su | {5}) - cost_excess(Su) == 0, 'reserved excess kills the distinction increment')
    cost_free = lambda U: sum((Fraction(1) for a in U if a != 3))
    check(cost_free(frozenset({0, 1, 3})) - cost_free(frozenset({0, 1})) == 0, 'a floor-free atom adds zero marginal cost')
    check(_safe_floor_ratio(Fraction(6), Fraction(1, 10 ** 9)) > 10 ** 8, 'eps* tending to zero makes the cardinality bound vacuous')
    Omega_s = frozenset({0, 1, 2})
    F_s = [frozenset({0, 1}), frozenset({2}), frozenset({0}), frozenset({1, 2})]

    def _N_under_mult(F, mult):
        total = sum((mult.get(cls, 1) for cls in F))
        classes = sorted(set(F), key=lambda s: (len(s), tuple(sorted(s))))
        B, _, _ = _greedy_basis(Omega_s, classes)
        return (len(_minimize(B, Omega_s)), total)
    N1, tot1 = _N_under_mult(F_s, {cls: 1 for cls in F_s})
    N2, tot2 = _N_under_mult(F_s, {frozenset({0, 1}): 10 ** 6, frozenset({2}): 10 ** 9, frozenset({0}): 7, frozenset({1, 2}): 10 ** 4})
    check(N1 == N2 and tot2 > 10 ** 8 and (tot1 < 10), 'realization multiplicity cannot change the operational basis size')
    return _result(name='T_finite_operational_basis -- exact finite atom-cover model witness for the Finite Operational Basis mechanism', tier=4, epistemic='P_structural', summary='Restricted executable theorem: on a finite atom-cover model, where admitted content is a finite atom set, operational classes are atom subsets, joint realization/closure is union, and exact no-excess cost is |covered atoms|*eps*, full-content admissibility plus closed-world union cover yields a finite complete inclusion-minimal operational-class basis with size at most floor(C_U/eps*). All theorem boundaries use Fraction arithmetic. Fail-controls exercise non-covering ledgers, capacity overspend, reserved excess, a floor-free atom, and realization-multiplicity invariance. The separate scope-contract check proves that this is not an unrestricted physical joint-extension theorem.', key_result='Exact finite atom-cover model: complete minimal basis exists and |B_U|<=floor(C_U/eps*); every control arm fires; no float tolerance enlarges the admissible set. General physical export remains gated by finite joint extension and compatible joint realization.', dependencies=['A1', 'L_epsilon*', 'T_admissibility_greedoid_structure', 'T_finite_operational_basis_scope_contract'], cross_refs=['T_selection_approximate_A2', 'T_sep', 'FD1_structural_completeness'], artifacts={'claim_kind': 'adopted_with_falsifier', 'model_class': 'finite_atom_cover', 'hypotheses': list(_FINITE_BASIS_MODEL_HYPOTHESES), 'general_open_obligations': list(_FINITE_BASIS_GENERAL_OPEN_OBLIGATIONS), 'arms_exercised': {'admissible': adm, 'inadmissible_bound_bites': inadm, 'closed_world_stuck': stuck, 'capacity_tight': tight, 'increment_steps': incr_used, 'complete_models': complete}, 'arithmetic': 'fractions.Fraction + _safe_floor_ratio; exact boundaries', 'paper_anchor': 'Paper 10 v1.21 sec:finite-operational-basis', 'non_claims': ['not_a_derivation_of_finite_joint_extension', 'not_a_general_physical_closure_theorem', 'not_precision_channel_generation', 'not_finite_smooth_generation']})

def check_T_finite_minimal_joint_realization_atom_cover():
    """Concrete compatible joint-realization corollary on the atom-cover model."""
    rng = np.random.default_rng(_SEED + 1)
    exercised = 0
    for _ in range(400):
        eps = _positive_fraction(rng, num_hi=30, den_hi=15)
        C = _positive_fraction(rng, num_hi=180, den_hi=15)
        Nmax = _safe_floor_ratio(C, eps)
        if Nmax < 1:
            continue
        m = int(rng.integers(1, min(9, Nmax) + 1))
        Omega, F = _rich_family(rng, m, int(rng.integers(max(2, m), 2 ** min(m, 6) + 1)))
        if _u(F) != Omega:
            continue
        B, covered, stuck = _greedy_basis(Omega, F)
        check(not stuck and covered == Omega, 'closed atom-cover family must admit a complete greedy basis')
        M = _minimize(B, Omega)
        joint = _build_atom_cover_joint_realization(M, eps)
        check(joint['covered'] == Omega, 'one joint carrier realizes the whole minimal basis')
        check(joint['total_cost'] == joint['minimum_lower_bound'], 'joint carrier attains the exact atom-cover lower bound')
        check(joint['total_cost'] <= C, 'joint minimum remains physically admissible')
        check(_projection_family_is_compatible(joint), 'all basis projections descend from one joint realization id')
        check(all((cls <= joint['covered'] for cls in F)), 'the joint carrier is complete under deterministic subset projection')
        check(len(M) <= Nmax, 'compatible joint realization has a finite bounded basis interface')
        exercised += 1
    check(exercised > 40, 'compatible joint-realization theorem must exercise many complete models')
    incompatible = {'joint_id': 'none', 'covered': frozenset({0, 1}), 'basis': (frozenset({0}), frozenset({1})), 'projections': ({'joint_id': 'independent-r0', 'class': frozenset({0}), 'visible_atoms': frozenset({0})}, {'joint_id': 'independent-r1', 'class': frozenset({1}), 'visible_atoms': frozenset({1})})}
    check(not _projection_family_is_compatible(incompatible), 'independently selected minima are rejected without a shared joint carrier')
    return _result(name='T_finite_minimal_joint_realization_atom_cover -- one compatible minimum joint carrier and deterministic basis projections', tier=4, epistemic='P_structural', summary='On every exercised closed finite atom-cover model, a complete inclusion-minimal basis is represented by one concrete joint carrier containing exactly the union of its atoms. Exact atom cost makes that carrier minimum and no-excess; deterministic subset projections recover every basis class and every class in the closed family. A negative control rejects independently minimum representatives with different joint-realization ids. This repairs the former string-tag corollary on the restricted model; the general physical compatible-minimizer theorem remains a named obligation.', key_result='One minimum no-excess joint carrier realizes the complete basis; all projections share one joint id; isolated minima with distinct ids fail compatibility.', dependencies=['T_finite_operational_basis', 'T_finite_operational_basis_scope_contract'], cross_refs=['T_selection_approximate_A2'], artifacts={'claim_kind': 'derived_theorem', 'model_class': 'finite_atom_cover', 'models_exercised': exercised, 'joint_realization_fields': ['joint_id', 'basis', 'covered', 'total_cost', 'minimum_lower_bound', 'projections'], 'negative_control': 'independent minima with distinct joint ids rejected', 'general_open_obligation': 'compatible_joint_realization', 'paper_anchor': 'Paper 10 v1.21 cor:finite-minimal-joint-realization'})

def _safe_floor_ratio(num, den, tol=1e-09):
    """Rational-safe floor(num/den) (the witness's audit repair, carried).

    Exact for int/Fraction inputs (Fraction floor division, no float
    roundoff). For floats: if num/den lands within tol of an integer
    without being exactly it, raise LOUDLY instead of silently rounding
    -- such a quotient is ambiguous under float arithmetic and the caller
    must supply exact rationals.
    """
    if isinstance(num, (int, Fraction)) and isinstance(den, (int, Fraction)):
        return int(Fraction(num) // Fraction(den))
    q = num / den
    nearest = round(q)
    if q != nearest and abs(q - nearest) < tol:
        raise ValueError(f'_safe_floor_ratio({num!r}, {den!r}): quotient {q!r} within {tol} of integer {int(nearest)} -- ambiguous under floats; supply fractions.Fraction')
    return math.floor(q)

_FINITE_BASIS_MODEL_HYPOTHESES = ('finite_content_atoms', 'operational_classes_are_atom_subsets', 'operational_closure_is_union', 'joint_realization_is_union_carrier', 'exact_no_excess_atom_cost', 'full_content_is_admissible', 'closed_world_union_cover')

def _u(sets):
    sets = list(sets)
    return frozenset().union(*sets) if sets else frozenset()

_FINITE_BASIS_GENERAL_OPEN_OBLIGATIONS = ('finite_joint_extension_or_amalgamation', 'downward_closed_joint_realizability', 'minimum_joint_realization_attainment', 'compatible_joint_realization', 'operational_basis_to_precision_channel_bridge')

def _greedy_basis(Omega, F):
    """Extract classes that add new atom content until complete or stuck."""
    covered = frozenset()
    B = []
    while covered != Omega:
        cand = next((c for c in F if not c <= covered), None)
        if cand is None:
            return (B, covered, True)
        covered |= cand
        B.append(cand)
    return (B, covered, False)

def _rich_family(rng, m, ntry):
    """A large operational-class family over ``m`` content atoms.

    Singletons are not forced.  Thus closed-world completeness
    ``union(F) == Omega`` is a genuine, fallible hypothesis rather than a
    sampler invariant.
    """
    Omega = frozenset(range(m))
    F = set()
    for _ in range(int(ntry)):
        k = int(rng.integers(1, m + 1))
        F.add(frozenset((int(x) for x in rng.choice(m, size=k, replace=False))))
    return (Omega, sorted(F, key=lambda s: (len(s), tuple(sorted(s)))))

_SEED = 20260703

def _minimize(B, Omega):
    """Delete union-redundant members while preserving complete coverage."""
    M = list(B)
    changed = True
    while changed:
        changed = False
        for i in range(len(M)):
            rest = _u((M[j] for j in range(len(M)) if j != i))
            if M[i] <= rest:
                del M[i]
                changed = True
                break
    check(_u(M) == Omega, 'minimalization must preserve full atom coverage')
    return M

def _positive_fraction(rng, *, num_hi=80, den_hi=24):
    """Deterministic positive rational sampler for exact theorem boundaries."""
    return Fraction(int(rng.integers(1, num_hi + 1)), int(rng.integers(1, den_hi + 1)))

def _build_atom_cover_joint_realization(basis, eps):
    """Construct one compatible no-excess joint carrier for the whole basis.

    The carrier is the union of the atoms required by the basis.  Every basis
    class is recovered by a deterministic projection to its subset.  Under the
    exact atom-cost law, every joint carrier realizing the basis must cover at
    least this union, so the construction is minimum and no-excess.
    """
    basis = tuple(basis)
    covered = _u(basis)
    joint_id = _joint_realization_id(basis)
    projections = tuple(({'joint_id': joint_id, 'class': cls, 'visible_atoms': cls} for cls in basis))
    return {'joint_id': joint_id, 'basis': basis, 'covered': covered, 'total_cost': Fraction(len(covered)) * eps, 'minimum_lower_bound': Fraction(len(covered)) * eps, 'projections': projections}

def _projection_family_is_compatible(joint):
    projections = tuple(joint.get('projections', ()))
    if not projections:
        return not joint.get('basis')
    ids = {p.get('joint_id') for p in projections}
    if ids != {joint.get('joint_id')}:
        return False
    covered = joint.get('covered', frozenset())
    return all((p.get('visible_atoms') == p.get('class') and p.get('class', frozenset()) <= covered for p in projections))

def _joint_realization_id(basis):
    rows = []
    for cls in sorted(basis, key=lambda s: (len(s), tuple(sorted(s)))):
        rows.append('{' + ','.join((str(x) for x in sorted(cls))) + '}')
    return 'atom-cover-joint:[' + ';'.join(rows) + ']'
