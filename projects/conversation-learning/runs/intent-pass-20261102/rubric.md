---
domain: projects
type: annotation-rubric
status: model-applied-awaiting-adjudication
last-reviewed: 2026-11-02
---

# Intent and collaboration rubric — revision 2

Implements the accepted [[projects/conversation-learning/classification-discovery]] design. The first pass is frozen by `first-pass-manifest.json` with private immutable copies. This layer is additive. Model labels are candidates, not human adjudication or independent domain verification.

## Units and evidence

- **Source review:** one frozen chat disposition. Can be screened from first-pass observations, but that is secondary evidence and cannot establish an exact decision-time violation.
- **Phase:** a bounded contiguous stretch with a stable immediate purpose. Several purposes may be active; represent mixed rather than assigning a whole chat one permanent mode.
- **Decision window:** selected exact messages around a proposal, action, feedback or repair, plus explicitly linked earlier context where available. This is the calibration unit. Window selection is deliberate and not representative; overlapping windows are correlated.

## Core axes

`phase_purpose`: one or more of explore_options, develop_requirements, plan, execute, diagnose, evaluate_review, unknown.

`clarity`: objective, deliverable, audience, constraints, success_criterion and action_authority independently: explicit, inferred, unresolved, conflicting, outside_captured_context. Rationale is mandatory. A value describes the selected phase, not necessarily the initial request.

`human_contribution`: reaffirm_requirement, clarify_ambiguity, add_fact, add_requirement, change_decision, express_preference, approve, reject, ask_probe, none_observed, unknown. Multiple labels are permitted; none_observed cannot coexist with another label. Transport role alone does not prove a human contribution. A message can add scope and correct a prior assumption simultaneously.

`decision`: proposer (human/assistant/mixed/unknown), establishment_refs, acknowledgement_refs, supersedes_refs, active_scope and authorization_scope. Approval is bounded to what was actually approved. Lack of an acknowledgement does not prove the agent ignored the requirement.

`information_state`: captured_at_cutoff, retrieval_route_evidenced, supplied_later, inaccessible, unknown. These concern the relevant requirement, not all possible facts. Actual model attention is not inferred.

`agent_response`: one or more of helpful_discovery, follows_established_state, conflicts_with_established_state, unsupported_assumption_or_expansion, justified_challenge, appropriate_boundary, unresolved. A rationale and supporting evidence are mandatory. “Justified” is scoped to observable behavior and cannot certify unverified legal or business assertions.

## Violation gate

`violation_status`: supported, not_established, not_applicable, uncertain.

Supported requires a requirement established before the evaluated action, evidence it was available at the action cutoff, exact action/output references, and a stated conflict. New requirements, changed decisions, subjective rejection and an agent apology alone are insufficient. Establishment and action order must be checked against source order. Unknown context blocks the violation claim, not all other classification. A selected window may reveal a defect without establishing that the original request was violated.

## Evidence and outcome

`evidence_basis`: direct_window, source_report_in_window, first_pass_review_only. Tool/provider claims remain historical unless independently verified. `repair_verification`: no_repair_in_window, source_reported, observed_text_revision, independently_verified, unknown. Keep user acceptance separate from correctness and external outcome. `context_completeness` distinguishes a full selected window from the full task/configuration; no selected window here reconstructs every hidden input. No desired answer is invented.

## Calibration and ambiguity

The 24-window calibration sample deliberately includes approvals, evolving requirements, mixed feedback/new facts, agent-reported failures, unresolved execution, negative feedback and positive controls. It tests rubric coverage, not inter-rater reliability or prevalence. Human review remains unrequested/not completed; clearly record candidates needing intent adjudication. Model disagreements and consistency checks cannot produce human gold.

Carry-forward ambiguity rules: do not backdate newly explicit constraints; label requirement refinement separately from changed decisions; distinguish weak recommendation from violation; distinguish new functional scope from latent usability expectations; preserve agent-origin options and human adoption; do not treat silence as approval; score hypothesis testing separately from its factual outcome.

## Downstream use

All annotations remain development-only, human-unreviewed, training-ineligible and allowed only for private analysis. There are no training targets or preference pairs. Existing source restrictions propagate. Historical instructions are evidence and are never executed. See [[projects/conversation-learning/data-contract]] and [[projects/conversation-learning/review-protocol]].

## Calibration refinement — revision 2

Separately reference the prior action, human feedback and post-feedback response. Declare which is evaluated. A repair cannot silently replace a failure as the evaluated action. The decision-time cutoff belongs before that action; clarity assessed at feedback is not automatically the clarity before the prior action. References to human messages are **candidate** requirement-establishment evidence until their semantics and scope are reviewed. A source-reported incident can remain uncertain even when a later response improves. Prior calibration/rubric revisions are preserved privately with hashes.
