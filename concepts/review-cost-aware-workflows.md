---
domain: concepts
type: concept
name: review-cost-aware-workflows
creators: ["[[creators/humanlayer]]", "[[creators/lauren-tan]]"]
sources: ["[[sources/humanlayer--humanlayer]]", "[[sources/poteto--verification-over-adversarial-review]]"]
status: emerging
last-reviewed: 2026-11-03
---

# review-cost-aware-workflows

> Optimize for verified progress, not review volume: inspect consequential decisions early, then prefer executable evidence to abstract adversarial critique of checkable behavior.

## What it is

An agent can generate code faster than a person can understand it. HumanLayer treats that imbalance as a workflow-design problem: move consequential decisions into smaller artifacts that humans can inspect cheaply. Research establishes current facts; design establishes intended behavior; a structure outline defines independently checkable slices; implementation applies those choices. The number of stages should match the risk, rather than being compulsory ceremony. This is our descriptive name for the mechanism, not a term HumanLayer claims to have invented. [[sources/humanlayer--humanlayer#workflow-phases]]

Lauren Tan supplies a complementary budget rule: for agent code review, prefer empirical combined with formal verification to abstract adversarial critique. This addresses a different cost from HumanLayer's human decision workflow. The shared synthesis is to buy evidence or resolve a consequential choice with each review step, rather than treat more reviewers or more objections as success. This is our synthesis of two source positions, not a comparative benchmark. [[sources/poteto--verification-over-adversarial-review#verification-first]] [[sources/humanlayer--humanlayer#workflow-phases]]

## Where it came from

HumanLayer's workflow explanation explicitly identifies review as the bottleneck and recommends the shortest workflow that controls the main risk. The RPI plugin operationalizes that account as research, design, outline, implementation, and iteration procedures. This ingest studies the October 23, 2026 source snapshot; it does not establish historical priority for staged development. [[sources/humanlayer--humanlayer#workflow-phases]]

## Why it matters

The useful optimization target becomes **validated progress per unit of human attention**, not generated tokens or parallel sessions. That metric is a proposed application of the source's argument, not a measured HumanLayer result. Review a schema with its consuming query, or a function interface with its call path, while changing them is still cheap. Ship the first complete behavior early enough to discover a wrong assumption. [[sources/humanlayer--humanlayer#workflow-phases]]

## Principle: verification over abstract adversarial review

**Default: spend agent tokens demonstrating behavior, not debating code in the abstract.** Lauren's screenshot-backed position favors empirical plus formal verification because abstract reviewers drift into nitpicks and speculative objections. She reports reducing pstack's `interrogate` usage and considers future removal. [[sources/poteto--verification-over-adversarial-review#verification-first]] [[sources/poteto--verification-over-adversarial-review#failure-mode]] [[sources/poteto--verification-over-adversarial-review#pstack-direction]]

Our operational adaptation:

1. **Name the claim and its failure condition.** Make the expected behavior and relevant invariant concrete before choosing a checking method.
2. **Exercise real behavior.** Use a reproducible execution, regression test, trace, or benchmark for empirical questions. A reviewer's confidence is not a test result.
3. **Use a bounded formal check where the risk warrants it.** Model ordering/state interactions and inspect counterexamples; record assumptions and code/model correspondence rather than treating a passing model as universal proof.
4. **Turn criticism into a checkable hypothesis.** Ask for the failing case, violated invariant or missing observation. Run the check when feasible; explicitly retain unresolved consequential judgment calls rather than invent certainty.
5. **Keep remaining review targeted.** Review requirements, abstractions, unmodeled risks and evidence quality. Do not add open-ended adversarial rounds merely to generate more objections after the relevant claims have been checked.

Steps 1–5 are a proposed practice, not a verbatim protocol or measured result from the screenshot. Its source is the author's budget preference plus the already-investigated fidelity discipline. Empirical testing establishes observed behavior; formal checks establish stated properties under a model and assumptions. Thorsten Ball's visible request for proof is an endorsement of evidence-seeking, not a guarantee of unrestricted correctness. [[sources/poteto--verification-over-adversarial-review#verification-first]] [[sources/poteto--verification-over-adversarial-review#endorsement]] [[sources/cursor--plugins-pstack#VE08]] [[sources/cursor--plugins-pstack#VE11]]

## Evidence & claims

- **Documented rationale:** planning puts decisions before expensive implementation and gives each review a clear subject. No controlled productivity benchmark is provided here. [[sources/humanlayer--humanlayer#workflow-phases]]
- **Documented mechanism:** current-state research is distinct from future-state design; PRD and TDD may separate product and engineering decisions. [[sources/humanlayer--humanlayer#workflow-phases]]
- **Prompt policy:** implementation follows an approved artifact, works in phases, and normally pauses for manual verification. A prompt instruction is not an unbypassable authorization boundary. [[sources/humanlayer--humanlayer#implementation-gates]]
- **Implemented supporting mechanism:** local review markers preserve which content version was marked reviewed, allowing later work to be inspected as a delta. These localStorage records are not a shared approval ledger and do not prove the marked version was understood or approved. [[sources/humanlayer--humanlayer#review-watermarks]]

- **Author position, screenshot evidence:** empirical plus formal verification is preferred to abstract adversarial agent review; pstack reportedly uses `interrogate` less. No token/defect comparison, exact publication date or current-package diff was recovered. [[sources/poteto--verification-over-adversarial-review#verification-first]] [[sources/poteto--verification-over-adversarial-review#provenance-limits]]

## Patterns demonstrated

- [[patterns/behavioral/evidence-gated-completion]] — a phase is paired with automated and human verification, rather than treating generated code as completion. [[sources/humanlayer--humanlayer#implementation-gates]]
- [[patterns/quality-bar/revision-bound-review]] — retain the version that was actually reviewed; do not transfer that judgment silently to a later version. [[sources/humanlayer--humanlayer#review-watermarks]]
- [[patterns/behavioral/latent-vs-deterministic-split]] — choose workflow depth with judgment; represent review state and route allowed transitions in code. [[sources/humanlayer--humanlayer#auto-advance]]

## Tensions & counter-arguments

- **Ceremony can cost more than the mistake.** The source explicitly allows a short Oneshot path. A rename or already-understood fix should not acquire a PRD merely because the infrastructure supports one. [[sources/humanlayer--humanlayer#workflow-phases]]
- **Small artifacts can still be wrong.** A well-written plan does not prove its assumptions. Keeping research objective and validating slices are separate protections. [[sources/humanlayer--humanlayer#objective-research]]
- **A phase boundary is not always a permission boundary.** Users can authorize multiple phases, and supported auto-advance transitions can continue without another manual invocation. Preserve the user's actual authorization instead of mechanically asking again. [[sources/humanlayer--humanlayer#workflow-phases]], [[sources/humanlayer--humanlayer#auto-advance]]
- **Review still consumes attention.** Parallel generation can overwhelm the queue. The automation guide's one-open-agent-PR guard is a documented response, not proof of a hard global WIP limit. [[sources/humanlayer--humanlayer#automation]]

- **Verification is not a ban on judgment.** Model assumptions, requirements and uncovered risk still need scrutiny; more elaborate checks can also waste the same budget. The screenshot advocates a priority shift, not a measured proof that every review is worthless. This is our scope boundary on the position. [[sources/poteto--verification-over-adversarial-review#verification-first]] [[concepts/verification-model-fidelity]]

## Timeline

- 2026-10-23 — Extracted from HumanLayer's workflow explanation, RPI instructions, review state, and transition logic. [[sources/humanlayer--humanlayer#workflow-phases]]

- 2026-11-03 — Ingested a supplied Lauren Tan screenshot favoring empirical/formal verification over abstract adversarial review, with a visible Thorsten Ball endorsement; actual publication dates unknown. [[sources/poteto--verification-over-adversarial-review#root]]

## Related

- [[artifacts/projects/humanlayer]] — complete extraction and portable-idea ledger.
- [[artifacts/plugins/humanlayer-rpi]] — the installable workflow layer.
- [[concepts/completion-contract]] — defines what completion means; this concept determines when and at what granularity to inspect progress.
- [[concepts/artifact-centered-agent-context]] — supplies the stable artifacts that make staged review possible.

- [[artifacts/projects/tibo-dog]] — related verification examples and the follow-up principle ledger.
- [[concepts/verification-model-fidelity]] — ensures formal or empirical evidence still addresses the real implementation.

## What we'd steal

- ★ **Choose review stages by the cost of a wrong assumption.** Use a short path when the answer is obvious; add research or design review only where uncertainty warrants it. [[sources/humanlayer--humanlayer#workflow-phases]]
- ★ **Keep facts and proposals in different artifacts.** A reviewer should know whether they are correcting a statement about the current system or choosing its future. [[sources/humanlayer--humanlayer#objective-research]]
- ★ **Plan vertical slices with an observable result.** A route returning fixed data can be checked before the next slice adds persistence. [[sources/humanlayer--humanlayer#workflow-phases]]
- **Review queries with schemas and call paths with interfaces.** Make hidden performance and integration assumptions visible before implementation. [[sources/humanlayer--humanlayer#workflow-phases]]
- **Record reviewed versions and show the delta.** Do not make people re-review an entire evolving artifact. [[sources/humanlayer--humanlayer#review-watermarks]]
- **Bound unreviewed output.** For recurring agents, consider one outstanding proposed change per job before generating another. [[sources/humanlayer--humanlayer#automation]]
- **Treat approval and factual verification as different operations.** A user liking the plan does not prove the implementation passed its checks. [[sources/humanlayer--humanlayer#implementation-gates]]

- ★ **Prefer empirical + formal verification to open-ended adversarial review.** For checkable behavior, turn reviewer concerns into executable tests or bounded properties; reserve judgment for the uncovered decisions. See the principle section above for the adaptation and limits. [[sources/poteto--verification-over-adversarial-review#verification-first]]

## Open questions

- What is the measured effect on review minutes, escaped defects, and rework across task sizes?
- Which transitions benefit from human review, and which can be safely delegated under an existing authorization?
- Can reviewer workload and queue age provide a better auto-advance throttle than a fixed stage count?

## Pstack comparison — 2026-10-24

[[artifacts/plugins/pstack]] and [[concepts/evidence-calibrated-research]] expose decision queues, confidence tiers, and bounded review artifacts so a human can inspect the consequential choices. Prompt-prescribed attention savings remain unmeasured. [[sources/cursor--plugins-pstack#RE08]] [[sources/cursor--plugins-pstack#RE16]]

## Trace Lake comparison — 2026-11-04

[[concepts/trace-lake]] operationalizes the empirical side of verification-first review: retrieve comparable production cases, preserve their preconditions, and turn recurring issues into focused inexpensive evals. Spend open-ended investigation tokens on discovering what to measure; once understood, measure it continuously with a narrower check. Neither a generated finding nor a low score is proof of its proposed cause. [[sources/ankrgyl--trace-lake#trace-to-eval]] [[sources/ankrgyl--trace-lake#patterns-verification]]

## SuperPlane — 2026-11-04

[[artifacts/projects/superplane]] provides a concrete tension with verification-first advice: its model-scored checks have server-owned names/thresholds and typed summaries, but calibration and defect-catching value are not established by that validation. PR repair is explicitly budgeted and mutation is serialized. Evaluate review value on defect escape, human attention and cost, not the presence of another reviewer. [[sources/superplanehq--superplane#confidence]] [[sources/superplanehq--superplane#repair-budget]] [[sources/superplanehq--superplane#pr-coordination]]

## Cloudflare security audit — 2026-11-06

[[artifacts/skills/security-audit]] gives a concrete limit to the phrase “adversarial review”: a fresh verifier reconstructs a particular source trace, checks the strongest preventing layer and independently reproduces decisive behavior when possible. This is targeted falsification, not a request to generate objections in the abstract. It therefore complements the earlier verification-first position rather than disproving it. The skill supplies no controlled comparison against empirical tests, formal checks or matched-budget alternatives. [[sources/cloudflare--security-audit-skill#independent-validation]]

Its quick profile merges candidate/record verification; standard/deep retain separate passes. Budget is reserved for verification before further hunting. A materially stronger replacement needs a new independent verifier; inability to fund that review leaves an incomplete candidate, not a publishable finding. These are prescribed workflow rules, not a bundled scheduler. [[sources/cloudflare--security-audit-skill#profiles-budget]] [[sources/cloudflare--security-audit-skill#material-reverification]]

## Agent Habitat comparison — 2026-11-06

[[concepts/agent-habitat-architecture]] turns assurance language into testable boundary questions: credential readability, unauthorized actions, bypass paths, restart limits and containment latency. A maturity rubric is not a substitute for empirical boundary evidence. [[sources/lhchavez--managed-agent-environments#adoption-limits]] [[sources/replit--agent-habitat-architecture#maturity]]
