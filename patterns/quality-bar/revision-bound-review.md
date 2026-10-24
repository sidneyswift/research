---
domain: patterns
type: pattern
name: revision-bound-review
category: quality-bar
status: proposed
last-reviewed: 2026-10-23
example-count: 1
---

# revision-bound-review

> Attach review state and feedback to the content version actually seen. Show what changed afterward, and preserve precise feedback targets rather than silently broadening them.

## Longer definition

In agent work, content can change faster than the reviewer can inspect it. A bare “reviewed” flag or a free-floating comment obscures which version the human judged. HumanLayer stores local review markers tied to content versions, computes changes since review, and separately carries contextual comment targets into agent feedback. The review markers use localStorage keyed by task/file; they are not an authenticated per-user audit log or a shared approval record. A viewed/reviewed marker is not automatically approval to merge or execute. [[sources/humanlayer--humanlayer#review-watermarks]], [[sources/humanlayer--humanlayer#feedback-targets]]

## Mechanism

1. Identify the artifact, diff base, file, and content version being reviewed.
2. Save the review marker with the content version, and make its local or shared scope explicit.
3. Compute later changes against that stored version rather than the latest arbitrary base.
4. Preserve structured selections such as line ranges, image targets, or document anchors when submitting feedback.
5. When a narrow target no longer resolves, report that state; do not silently turn “change this selection” into “rewrite the file.”
6. In an optional send-and-resolve action, resolve captured comments after delivery is accepted and confirmed; distinguish successful delivery from failed resolution bookkeeping. Neither outcome proves that the issue was fixed.

These are related mechanisms in one artifact, not a single all-or-nothing transaction. [[sources/humanlayer--humanlayer#review-watermarks]], [[sources/humanlayer--humanlayer#feedback-targets]], [[sources/humanlayer--humanlayer#feedback-delivery]]

## When to use

- Agents revise documents or code while teammates review them asynchronously.
- Reviewers need to see only new changes after an earlier pass.
- A comment's location materially constrains the requested edit.

## When NOT to use

- Immutable, one-shot outputs with no continuing revision cycle.
- As proof that the reviewer understood, approved, or authorized every effect of the content.
- When reconstructing a precise anchor is impossible: mark the uncertainty instead of manufacturing precision.

## Why it works

It binds a human judgment to the evidence it concerned and makes the remaining delta visible. That supports [[concepts/review-cost-aware-workflows]] without pretending that a timestamp alone establishes correctness. The source tests and implementation support the state mechanism, not a measured improvement in review quality. [[sources/humanlayer--humanlayer#review-watermarks]]

## Detection recipe

- **Look for:** version-bound review markers with explicit local or shared scope, “since last review” views, typed feedback targets, explicit missing-anchor states.
- **Confirm with:** the diff really derives from the reviewed content, the selection survives delivery, and failed delivery does not silently resolve comments.
- **Rule out:** a global boolean called `reviewed`, a timestamp unrelated to content identity, or a UI selection that is dropped when constructing the agent prompt.

## Examples in this wiki

- [[artifacts/projects/humanlayer]] — local content-version review markers, structured comment targeting, and delivery-aware resolution. [[sources/humanlayer--humanlayer#review-watermarks]], [[sources/humanlayer--humanlayer#feedback-targets]], [[sources/humanlayer--humanlayer#feedback-delivery]]

One verified artifact; the code-review and artifact-comment implementations are not counted as two independent examples.

## Counter-examples or anti-pattern

- **Hypothetical inverse:** retaining “approved” after the plan has materially changed, without recording which revision was accepted.
- **Hypothetical inverse:** marking every comment resolved before the agent accepted the feedback, so a failed send looks like completed work.
- A watermark by itself remains only a record of review state. HumanLayer's distinct feedback dispatch/result handling is necessary evidence for the stronger delivery claim. [[sources/humanlayer--humanlayer#feedback-delivery]]

## Related patterns

- [[patterns/behavioral/evidence-gated-completion]] — review state is evidence about a version, not a blanket completion certificate.
- [[patterns/structural/authoritative-recheck-after-notification]] — both distinguish old observations from current authority.
- [[concepts/artifact-centered-agent-context]] — structured feedback becomes part of the next agent's task context.

## Open questions

- How should approvals be invalidated when edits are semantically material but mechanically small?
- Which independent system provides a second source-backed example?
- How should review state behave under rebases, conflicting edits, and regenerated files beyond the cases covered by the inspected tests?

## Pstack comparison — 2026-10-24

[[artifacts/skills/poteto-mode]] independently implements the narrower core of review freshness: verification records are keyed by PR plus exact SHA, and a new revision does not inherit that key. The verifier field is optional text and same-key writes replace prior values; reviewer authority is not enforced. Shipping playbooks prescribe independent verdicts and equivalent-build carryover, but that is policy. This does not establish the complete feedback-anchor/delta-view mechanism above, so status remains **proposed** and the full-pattern example count stays one. [[sources/cursor--plugins-pstack#OR11]] [[sources/cursor--plugins-pstack#OR18]]
