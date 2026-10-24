---
domain: concepts
type: concept
name: verification-model-fidelity
creators: ["[[creators/lauren-tan]]"]
sources: ["[[sources/cursor--plugins-pstack]]"]
status: emerging
last-reviewed: 2026-10-24
---

# verification-model-fidelity

> Before trusting a passing check, establish that its model still describes the current implementation and still detects the failure it claims to guard.

## What it is

Verification-model fidelity is the maintained relationship between an implementation, the representation used to verify it, and the promise being checked. A verifier can execute correctly while proving something about an obsolete or inaccurate model. A property can also become vacuous or lose its connection to a real defect after a refactor. The practical response is to record coverage and a last-confirmed revision, reconcile relevant code changes, preserve implementation atomicity, challenge the updated check with a deliberate broken variant, and replay counterexamples against real behavior. This is our synthesis label for pstack's source-backed discipline, not a term or novel formal method claimed by its creator. [[sources/cursor--plugins-pstack#VE08]] [[sources/cursor--plugins-pstack#VE09]] [[sources/cursor--plugins-pstack#VE10]] [[sources/cursor--plugins-pstack#VE11]]

The concept differs from [[concepts/completion-contract]]. A completion contract asks what evidence allows work to end. Fidelity asks whether the evidence-producing apparatus is still about the right system. It also differs from ordinary test maintenance: changing a test to match new output is insufficient unless the changed behavior is intentional and the check still detects the relevant failure. [[sources/cursor--plugins-pstack#VE11]] [[sources/cursor--plugins-pstack#VE36]]

## Where it came from

This page distills Lauren Tan's pstack `create-formal-verification-skill`, `maintain-formal-verification-skill`, real-app verification companions, and statechart implementation at commit `9580c23696ac8d7abed0c166f2f9918800afb819`, inspected 2026-10-24. The source explicitly identifies the dangerous case: an unchanged check can keep passing after the code it describes has disappeared. It operationalizes the response as a maintenance workflow and a reviewable result format. This page does not claim pstack originated model validation, mutation testing, refinement, or the distinction between testing and proof. [[sources/cursor--plugins-pstack#VE07]] [[sources/cursor--plugins-pstack#VE10]] [[sources/cursor--plugins-pstack#VE49]]

## Why it matters

Agents can generate specifications and test harnesses quickly, then optimize toward green output. If the model merges two separate code operations into one atomic action, omits a writer of guarded state, or adopts a condition the code never checks, a valid model-checking result can support an invalid application claim. Maintenance must therefore be driven by source changes and intended promises, not by what makes the verifier pass. The source's deliberate-defect requirement provides a practical sensitivity test, while real-entry-point replay reconnects counterexamples to the system people use. Neither eliminates the need for judgment. [[sources/cursor--plugins-pstack#VE08]] [[sources/cursor--plugins-pstack#VE11]] [[sources/cursor--plugins-pstack#VE14]] [[sources/cursor--plugins-pstack#VE29]]

The same principle applies outside formal modeling. A UI driver's health check may be green while it is controlling the wrong build, a feature map may silently omit a second entry point, or a benchmark may time rejected work. A useful verification result needs both an executing check and a truthful relationship between that check and its claim. [[sources/cursor--plugins-pstack#VE02]] [[sources/cursor--plugins-pstack#VE03]] [[sources/cursor--plugins-pstack#VE35]]

## Mechanism and authority

1. **Name the promise and scope.** Identify the harm, covered code, bounds, assumptions and exclusions. Choose the method for the question: model checking for ordering, code verification when suitable, generated inputs against real code when needed, or proof for claims requiring it. [[sources/cursor--plugins-pstack#VE07]] [[sources/cursor--plugins-pstack#VE08]]
2. **Maintain the representation-to-source map.** Cite variables/actions/guards to the code, preserve its atomic steps, and track both moved functions and new paths that write guarded state. A citation is a review aid; syntactic presence does not establish entailment. [[sources/cursor--plugins-pstack#VE08]] [[sources/cursor--plugins-pstack#VE11]] [[sources/cursor--plugins-pstack#VE29]]
3. **Classify change before rerunning.** Distinguish irrelevant edits, stale representation, intentional promise change and possible regression. Update the model from code before looking for a passing result. Change a property only with evidence that the intended promise changed; disclose weaker bounds. [[sources/cursor--plugins-pstack#VE11]]
4. **Test both positive and negative behavior.** Run the reconciled check, then deliberately break the real behavior it guards and confirm detection. When it fails, replay the counterexample: an impossible step is a model error; a reachable harmful sequence is a code finding. Keep partial execution and source-reading evidence separate. [[sources/cursor--plugins-pstack#VE09]] [[sources/cursor--plugins-pstack#VE11]] [[sources/cursor--plugins-pstack#VE14]]
5. **Bind the result to its revision and explain it.** Advance the sync commit only after reconciliation, leave blocked checks at their prior commit, and separate verification updates from product fixes. Explain findings in the code's or reader's terms, with the exact command and omissions. [[sources/cursor--plugins-pstack#VE11]] [[sources/cursor--plugins-pstack#VE12]] [[sources/cursor--plugins-pstack#VE15]]

Current code owns the factual question of what happens. The agreed property/spec owns the intended promise. The model is a checkable representation, and its configuration determines the scope. The chart is a projection for review. None automatically inherits all the authority of the others. A later model that passes is not evidence that the promise changed; a chart that looks correct is not a proof that the implementation refines it. [[sources/cursor--plugins-pstack#VE11]] [[sources/cursor--plugins-pstack#VE18]] [[sources/cursor--plugins-pstack#VE22]] [[sources/cursor--plugins-pstack#VE45]]

## Evidence & claims

- **Prompt policy:** generated formal checks must be grounded in source, show sensitivity to a deliberate real-code break, expose bounds/assumptions and remain cheap to rerun. No generated app-specific skill was trialed during this ingest. [[sources/cursor--plugins-pstack#VE08]] [[sources/cursor--plugins-pstack#VE09]] [[sources/cursor--plugins-pstack#verification-local-checks]]
- **Prompt policy:** maintenance explicitly preserves stale-baseline results, reads covered-code changes, separates drift from bugs, permits “updated and bug,” and refuses to advance blocked sync commits. These are instructions to an agent, not an automatically enforced semantic gate. [[sources/cursor--plugins-pstack#VE10]] [[sources/cursor--plugins-pstack#VE11]] [[sources/cursor--plugins-pstack#VE12]]
- **Implemented, narrower guarantee:** statechart checks each invariant independently, reports omitted comparison rules, guards cross-model schema access, and distinguishes mixed reader labels. These mechanisms reduce misleading presentation; they do not establish that a handwritten model matches production. [[sources/cursor--plugins-pstack#VE16]] [[sources/cursor--plugins-pstack#VE21]] [[sources/cursor--plugins-pstack#VE23]] [[sources/cursor--plugins-pstack#VE45]]
- **Implemented, qualified revision binding:** specifications/configs are copied for TLC, and recognized inputs are content-checked before publication. The mapping is still loaded from its original path, so this is not a fully immutable rendering snapshot. Persistent changes are rejected; a stronger claim about every transient change is unsupported. [[sources/cursor--plugins-pstack#VE31]] [[sources/cursor--plugins-pstack#VE50]]
- **Observed local checks:** 21 modules passed syntax checks; an isolated 44-test offline subset passed 43 and failed the piped-help completeness test on Node v23.6.1. TLC/PNG integration checks were not run. This demonstrates why the verification tool itself needs evidence, without establishing model-checker effectiveness. [[sources/cursor--plugins-pstack#verification-local-checks]] [[sources/cursor--plugins-pstack#VE38]]

## Patterns demonstrated

- [[patterns/behavioral/evidence-gated-completion]] — supporting policy: execution and deliberate-defect evidence are conditions for handing over a generated verification skill. Fidelity examines the validity of that evidence surface. [[sources/cursor--plugins-pstack#VE03]] [[sources/cursor--plugins-pstack#VE09]]
- [[patterns/behavioral/latent-vs-deterministic-split]] — choose the promise and model with judgment, then execute precise checks and compare results. The division does not make the chosen premises true. [[sources/cursor--plugins-pstack#VE07]] [[sources/cursor--plugins-pstack#VE16]]
- [[patterns/quality-bar/revision-bound-review]] — supporting analogy: retain the revision actually reconciled or checked, rather than a timeless “verified” label. These records are distinct from human authorization. [[sources/cursor--plugins-pstack#VE11]] [[sources/cursor--plugins-pstack#VE31]]

## Tensions & counter-arguments

- **A mutation probe is not complete validation.** Detecting one removed guard demonstrates sensitivity to that defect, not all bugs or all incorrect abstractions. The workflow requires judgment about representative breaks and useful bounds. [[sources/cursor--plugins-pstack#VE08]] [[sources/cursor--plugins-pstack#VE11]]
- **The model and its reviewer can share the same blind spot.** Source links and replay help, but no inspected mechanism automatically proves semantic correspondence. Even citation warnings only recognize selected syntactic conditions and citation-shaped text. [[sources/cursor--plugins-pstack#VE14]] [[sources/cursor--plugins-pstack#VE29]]
- **Maintaining a verifier can cost more than the target warrants.** pstack chooses harmful, poorly tested promises and demands cheap reruns; its TDD skill explicitly declines impractical or brittle tests. Reuse fidelity proportionately, rather than requiring formal modeling for every small change. [[sources/cursor--plugins-pstack#VE07]] [[sources/cursor--plugins-pstack#VE08]] [[sources/cursor--plugins-pstack#VE36]]
- **Readable abstractions can hide causal distinctions.** Statechart reports mixed states and hidden steps, but mappings still determine which differences people can see. Its region consistency check is relative to the projected graph; it does not recover information already removed by labels. [[sources/cursor--plugins-pstack#VE20]] [[sources/cursor--plugins-pstack#VE21]] [[sources/cursor--plugins-pstack#VE26]]
- **“Expected failure” can be mistaken for success.** Exit 0 can preserve a known-bug baseline, including a valid narrower counterexample when exploration later fails. A consumer must inspect expected rules and warnings instead of treating zero as “no defects.” [[sources/cursor--plugins-pstack#VE17]] [[sources/cursor--plugins-pstack#VE44]]

These are source-grounded limitations and our counterarguments, not a documented public debate about this newly synthesized label.

## Timeline

- 2026-10-24 — Distilled verification-model fidelity from pstack's creation/maintenance contracts and statechart implementation at the pinned revision. Conducted isolated syntax and offline tests; no TLC, PNG or real-app verification run. [[sources/cursor--plugins-pstack#VE08]] [[sources/cursor--plugins-pstack#VE11]] [[sources/cursor--plugins-pstack#verification-local-checks]]

## Related

- [[artifacts/plugins/pstack]] — parent workflow system.
- [[artifacts/skills/statechart]] — executable adapter and complete specialized-family ledger.
- [[concepts/completion-contract]] — specifies when evidence permits completion; fidelity asks whether that evidence still describes the intended system.
- [[concepts/artifact-centered-agent-context]] — a generated skill/coverage record makes context portable, while fidelity requires the next agent to reopen source instead of treating the artifact as timeless truth. [[sources/cursor--plugins-pstack#VE09]] [[sources/cursor--plugins-pstack#VE11]]

## What we'd steal

- ★ **Store a verification contract beside the check:** promise, harm, code coverage, command/version, bounds, assumptions, omissions and sync revision. [[sources/cursor--plugins-pstack#VE08]] [[sources/cursor--plugins-pstack#VE09]]
- ★ **Require sensitivity evidence:** deliberately break the real guarded behavior, run the published instructions, restore the change and confirm the baseline. [[sources/cursor--plugins-pstack#VE09]]
- ★ **Reconcile source before optimizing for green:** write the model update from code, then rerun; cite intentional promise changes and disclose weaker bounds. [[sources/cursor--plugins-pstack#VE11]]
- ★ **Track semantic coverage through refactors:** find moved/split functions and new writers of the protected state. [[sources/cursor--plugins-pstack#VE11]]
- ★ **Replay failures through real boundaries:** distinguish impossible model steps, actual bugs and partially executed evidence; do not hide a finding by weakening the rule. [[sources/cursor--plugins-pstack#VE11]] [[sources/cursor--plugins-pstack#VE14]]
- **Separate representation status from behavior status:** a check can be reconciled and still expose a bug. [[sources/cursor--plugins-pstack#VE10]]
- **Retain stale-pass evidence:** explain when an earlier success belonged to an obsolete description. [[sources/cursor--plugins-pstack#VE11]] [[sources/cursor--plugins-pstack#VE12]]
- **Treat source citations as review obligations:** verify the cited code's semantics and atomicity, not merely citation syntax. [[sources/cursor--plugins-pstack#VE08]] [[sources/cursor--plugins-pstack#VE29]]
- **Keep configuration and projection limits visible:** name which rules were checked and which chart distinctions were collapsed or omitted. [[sources/cursor--plugins-pstack#VE21]] [[sources/cursor--plugins-pstack#VE25]] [[sources/cursor--plugins-pstack#VE45]]
- **Keep blocked revisions honest:** do not move the sync commit until reconciliation finishes; separate verifier changes from product fixes. [[sources/cursor--plugins-pstack#VE11]] [[sources/cursor--plugins-pstack#VE12]]
- **Validate the verifier's own outputs:** syntax checks, malformed-input tests, incomplete-output handling and publication tests are part of trustworthy evidence generation. [[sources/cursor--plugins-pstack#VE37]] [[sources/cursor--plugins-pstack#VE38]] [[sources/cursor--plugins-pstack#VE40]]

## Open questions

- How should mutation probes be selected so they challenge the abstraction rather than only a convenient guard?
- Can coverage records discover new writers of guarded state across services without becoming a second incomplete model?
- Which guarantees require a formal refinement relation, and when is source-linked counterexample replay the right practical standard?
- How much does this workflow improve real defect detection per maintenance hour? The inspected source supplies contracts and mechanisms, not a measured answer.
