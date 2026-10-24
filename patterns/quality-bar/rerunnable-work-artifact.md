---
domain: patterns
type: pattern
name: rerunnable-work-artifact
category: quality-bar
status: proposed
last-reviewed: 2026-10-24
example-count: 1
---

# rerunnable-work-artifact

> Before repeating a transformation broadly, produce one checked result, turn the method into an idempotent runnable tool, and give workers the same tool and acceptance check.

## Longer definition

The artifact of repeated work should include a way to repeat it correctly. Pstack's build-the-lever principle asks for a representative manual unit, a reusable script/codemod/recipe, and a comparison proving that automation reproduces the intended result. Deterministic transformations run before parallel judgment work. Shared instructions live outside delegates' write scopes so workers do not silently rewrite their own contract. The reusable artifact must exist before the agent claims to have applied the principle. The source applies the same discipline even to nontrivial one-off work when the tool makes it reviewable; repetition is not its only trigger. This pattern names the repeated-work specialization. This is prompt-prescribed process, not a universal runtime enforcer. [[sources/cursor--plugins-pstack#PP03]]

## Mechanism

1. Select a representative unit and establish its accepted output.
2. Extract repeated mechanics into a parameterized tool.
3. Compare its output with the accepted unit, including meaningful failure cases.
4. Make retries converge rather than duplicate effects.
5. Run deterministic work once, then delegate independent judgments with a shared recipe and bounded writes.
6. Deliver the tool, usage, and verification result alongside transformed outputs. [[sources/cursor--plugins-pstack#PP03]] [[sources/cursor--plugins-pstack#PP12]]

## When to use

- Repository-wide migrations, documentation inventories, repeated evidence/citation checks, or batch transformations with a stable mechanical core.
- Several agents would otherwise independently invent the same recipe.
- Future re-ingests or corrections will need the same operation.

## When NOT to use

- A one-off, low-cost judgment task whose automation costs more than repetition.
- A poorly understood example that would encode the wrong rule broadly.
- External side effects without an explicit retry/deduplication contract.

## Why it works

It moves invariant mechanics out of repeated model reasoning and makes the result reproducible. Comparing against an accepted unit supplies an oracle; negative fixtures test what the tool should reject. Idempotence makes interruption and reruns less costly. These are engineering reasons to expect benefit, not a measured pstack effect size. [[sources/cursor--plugins-pstack#PP03]] [[sources/cursor--plugins-pstack#PP12]]

## Detection recipe

- **Look for:** a checked manual specimen, runnable transformation, reusable invocation, and retry-safe behavior.
- **Confirm with:** the tool reproduces the specimen and preserves the invariant on rerun; delegates share its contract.
- **Rule out:** a reusable prompt alone, a one-time generated script never checked against output, or a batch job that duplicates side effects.

## Examples in this wiki

- [[artifacts/plugins/pstack]] — build-the-lever explicitly prescribes manual oracle → runnable artifact → verified bulk application. [[sources/cursor--plugins-pstack#PP03]]

Only one independently studied source family currently establishes the full mechanism. This wiki's own citation-checker application is a derivative use, not a second independent artifact confirming the pattern.

## Counter-examples or anti-pattern

- Fan out identical mechanical work to many agents before extracting the common operation; this scales divergence and integration work.
- Pstack's own packaging checks illustrate a limit: a rerunnable tool can consistently miss an untested class. Our injected missing skill link passed the generator and docs checker, so reproducibility is not comprehensiveness. [[sources/cursor--plugins-pstack#packaging-negative-probe]]

## Related patterns

- [[patterns/behavioral/latent-vs-deterministic-split]] — separates judgment from mechanics; this pattern adds the accepted specimen and delivered reusable artifact.
- [[patterns/quality-bar/complexity-ratchet]] — the tool makes future repetitions cheaper and more reliable.
- [[patterns/behavioral/evidence-gated-completion]] — checks the transformation's promised result rather than the mere existence of a script.

## Open questions

- Which second independent artifact shows the full specimen/tool/rerun/delegation mechanism?
- How many representative examples are needed before a transformation is safe to generalize?
