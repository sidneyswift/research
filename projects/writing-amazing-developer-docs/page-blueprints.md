---
domain: projects
type: authoring-guide
status: proposed
last-reviewed: 2026-11-05
---

# Developer documentation page blueprints

These are proposed authoring aids derived from [[concepts/developer-documentation-design]], which owns the findings and qualifications. Choose the sections a real reader needs; do not publish empty templates. Adapt fields to the implemented contract. None of the illustrative wording below describes an existing Flex API.

## Write a brief before the page

- **Reader:** role, technical experience and domain familiarity.
- **Situation:** problem that brought them here and existing system state.
- **Result:** what they will accomplish or understand, with observable evidence where applicable.
- **Applicability:** product, environment, contract version and SDK/runtime requirements.
- **Prerequisites:** identity/role, account configuration, dependencies and fixture data.
- **Owner:** person/team accountable for technical accuracy and release updates.
- **Evidence:** implementation/specification, tested example and last verified scope.

Audience/task fields apply [[sources/google--developer-documentation#audience]] and [[sources/gitlab--documentation-engineering#tasks]]. Ownership/release fields apply [[sources/gitlab--documentation-engineering#workflow]] and [[patterns/quality-bar/revision-bound-review]].

## Quickstart / learning tutorial

```markdown
# [Achieve one concrete result]

Build [small capability] in [environment]. At the end, verify [result].

## Before you start
[Account, role, versions, tools, test data, credentials setup, cost/effect.]

## Create the example
[One supported path. Commands, file names, execution context.]

## Run it
[Complete program or a link to its versioned runnable project.]

## Check the result
[Expected output. Which values vary. Evidence in the system of record.]

## If the result differs
[Likely symptom, diagnostic check, next action.]

## Clean up
[Resources created and how to remove them, if applicable.]

## Continue
[One useful next task and the production constraints it introduces.]
```

Keep teaching through small observable actions; link deeper explanation and alternatives. Prerequisites, runnable code and output come from Google/Diátaxis; cleanup and business-result verification are our proposed additions. [[sources/diataxis--documentation-framework#tutorials]] [[sources/google--developer-documentation#sample-code]]

## How-to guide

```markdown
# [Verb + real task]

Use this procedure when [situation]. It results in [state].

## Prerequisites
[Required existing state, role, environment and tools.]

## Choose the applicable path
[Only decisions that actually change the procedure.]

## Complete the task
[Ordered actions. Put consequences before consequential steps.]

## Verify
[Evidence proving the intended result.]

## Recover or reverse
[Relevant supported recovery, reversal limits, escalation.]

## Related contracts
[Exact API/resource/error references.]
```

Assume appropriate competence and let real-world conditions branch. Avoid teaching unrelated foundations. Recovery/reversal sections apply when the operation supports or requires them. [[sources/diataxis--documentation-framework#how-to]] [[sources/gitlab--documentation-engineering#tasks]]

## API capability reference

```markdown
# [Capability / resource / operation]

[Purpose and applicability.]

## Contract
[Method/path or symbol, version, actor/permissions, scope.]

## Inputs
[Required/optional, defaults, units, constraints, null versus omitted.]

## Results and effects
[Return schema, authoritative state changes, freshness/consistency.]

## Lifecycle
[Acceptance versus completion, states, observation, partial results.]

## Failure behavior
[Errors, concurrency/preconditions, supported retries/idempotency.]

## Examples
[Minimal call and output, with environment/SDK version.]

## Limits and compatibility
[Known limits, availability, deprecation/migration links.]

## Related tasks
[Practical task guide and relevant explanation.]
```

This coverage is our business-platform application; describe actual guarantees, including unsupported capabilities. Generated shapes supplement these semantics. [[concepts/business-platform-api-design]] [[sources/diataxis--documentation-framework#reference]]

## Troubleshooting entry

```markdown
# [Recognizable error or symptom]

## What it means
[Failed boundary; what may already have succeeded.]

## Check the cause
[Observable checks, most likely/safest first.]

## Resolve
[Cause-specific action. Identify a temporary workaround explicitly.]

## Retry and verify
[Whether/how retry is supported. Evidence recovery succeeded.]

## Escalate
[Useful non-secret context and correlation IDs, if available.]
```

Exact messages support search. A retry may be inappropriate when the failure reflects permission, business state or an uncertain external effect. [[sources/gitlab--documentation-engineering#troubleshooting]] [[sources/developer-docs--product-examples#github-troubleshooting]] [[sources/developer-docs--product-examples#twilio-error-21610]]

## Explanation / architecture page

Start with a bounded question, then explain the model, system relationships, design constraints, alternatives and consequences. Add a diagram when it clarifies a boundary or sequence, with equivalent text. Link the implemented contract and concrete tasks. Keep proposal/decision history separate from current operating behavior. [[sources/diataxis--documentation-framework#explanation]] [[sources/google--developer-documentation#accessibility]] [[sources/google--developer-documentation#maintenance]]

## Precise wording exercises

| Vague draft | More useful illustrative wording | What the author must verify |
| --- | --- | --- |
| “Configure authentication.” | “Create a test-tenant token with the vendor-read permission and make it available to the example.” | Actual credential mechanism, permission and secret handling |
| “Run the command.” | “Start the local server from the example directory. Open its printed URL and check the response.” | Real directory, command, URL and expected result |
| “The job ran successfully.” | “For an asynchronous job, wait for its documented success state, then verify the business result. Follow recovery guidance for failure or cancellation.” | Actual acceptance and completion semantics |
| “Retry on failure.” | “Use the documented retry policy for this error; reconcile an unknown result before submitting a new intent.” | Operation-specific deduplication and reconciliation behavior |
| “See here for details.” | “See the webhook signature verification guide.” | Correct target and section |
| “Simply update your configuration.” | “Set [field] to [value], restart [component] if required, then verify [observable result].” | Actual field, reload semantics and evidence |

These rewrites apply descriptive link, step-order and sample guidance. Bracketed fields are author placeholders, never copy-ready commands. [[sources/google--developer-documentation#links]] [[sources/google--developer-documentation#procedures]] [[sources/google--developer-documentation#sample-code]]

## Review checklist

Use this to review a concrete reader task, not as a requirement that every page contain every item.

- Can the intended reader recognize the right page from its title and opening?
- Are prerequisites and version/environment applicability visible before commands?
- Can they run the supplied path from the stated starting condition?
- Are copied examples complete or clearly marked as fragments?
- Are expected outputs and business-state verification explicit?
- Are asynchronous acceptance, completion and failure distinguished?
- Do permission, retries and side-effect descriptions match the owning contract?
- Can a reader diagnose the likely failure and take a safe next step?
- Are warnings close to consequential actions and preserved in Markdown exports?
- Are reference, task, explanation and troubleshooting links precise?
- Can keyboard/screen-reader users reach instructions and copy actual text?
- Is there one accountable source for repeated facts and one owner for updates?
- Have relevant mechanical checks, technical review and reader checks been distinguished?
- Does the release process keep supported versions and docs aligned?
- Are observed results and untested assumptions reported separately?

This checklist operationalizes [[concepts/developer-documentation-design]]; its full evidence map and counterarguments remain on that page. A completed checklist is author review, not proof of runtime or usability success.

## Patterns demonstrated

Applications of [[patterns/quality-bar/revision-bound-review]] and [[patterns/composition/single-source-multi-surface-distribution]]; no new confirmed pattern is introduced.

## What we'd steal

Use the brief, choose one appropriate blueprint, then review a real task. Preserve technical qualifications when making prose shorter. Keep the templates subordinate to observed reader needs.

## Wider-pass blueprints

These additions apply the later sections of [[concepts/developer-documentation-design]]. They are proposed fields for a concrete task, not a mandate to fill every section on every page.

### Decision record

- Choice in the title and a stable identifier.
- Context/constraints and options considered.
- Decision, positive/negative consequences and accountable owner/reviewers.
- Status under the team's explicit amendment policy.
- Link to implementation work and current architecture; superseding decision when applicable.

Choose local lifecycle rules: AWS and GDS do not prescribe identical amendment behavior. Agreement and implementation are separate. [[sources/docs-research--architecture-20261105#nygard-adr]] [[sources/docs-research--architecture-20261105#aws-adr]] [[sources/docs-research--architecture-20261105#gds-adr]]

### Operational runbook

- Trigger, symptoms, environment and when this procedure does not apply.
- Required authority, access, current incident link and role responsibilities.
- Checks: expected/actual evidence, interpretation and uncertainty.
- Actions: consequence, predicted result, checkpoint and next branch.
- Stop/escalate conditions, supported reversal or reconciliation, and handoff.
- Verification, changes that remain active and follow-up owner.

Keep live observations in the incident record and later causal analysis in the retrospective. Make instructions/contact paths available even if the affected system is down. Do not treat possessing a runbook as permission to execute it. [[sources/docs-research--operations-20261105#google-managing-incidents]] [[sources/docs-research--operations-20261105#google-troubleshooting]]

### Migration guide

- Affected consumers, starting state, target/version and dependencies.
- Old/new behavior, changed defaults and newly required data.
- Intermediate states, which path processes effects and duplicate/concurrency concerns.
- Detection methods and preflight tests.
- Checkpoints for advancing, monitoring and explicit reversal limits.
- Conditions for retiring the old path and evidence of the intended business result.

A rename/conversion does not establish equivalent behavior. Rollback may depend on stored representation, replay and accumulated state. Use the actual provider contract; Stripe's retry/status policy is not universal. [[sources/docs-research--operations-20261105#kubernetes-migration]] [[sources/docs-research--operations-20261105#stripe-upgrade]]

### Example verification record

Record example source/version, displayed fragment, complete runnable project/setup, execution context, test mode, dependencies and outcome check. Report compiled, executed, skipped and asserted examples separately. State which setup was supplied by the runner but not the reader-facing page. Preserve the distinction between mocked/fixture tests and live integrations. [[sources/docs-research--executable-reference-20261105#rust-tests]] [[sources/docs-research--executable-reference-20261105#python-context]] [[sources/docs-research--executable-reference-20261105#sphinx-fixtures]]

A reproducible narrowly scoped example of why this matters is the [[projects/writing-amazing-developer-docs/experiments/README|local synthetic probe]]. It is not an audit of the cited vendors' examples.
