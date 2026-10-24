---
domain: patterns
type: pattern
name: defect-derived-validation
category: quality-bar
status: proposed
last-reviewed: 2026-07-22
example-count: 1
---

# defect-derived-validation

> Build your validation/lint rule set by mining what real maintainers actually fixed across a large historical corpus — commit messages, PR titles, merged diffs — instead of authoring rules from generic best-practice intuition. Then validate the rule set itself by running it back over the same corpus and reporting hit rates, so its coverage is measured, not assumed.

*Done when it passes the [page checklist](_definition-of-done.md).*

## Longer definition

Most linters and validation checklists are written top-down: someone who knows the domain imagines what could go wrong and encodes each worry as a rule. This pattern inverts the direction — it's bottom-up. You start from a large population of real, historical corrections (a corpus of merged commits, PR titles like "fix YAML frontmatter" or "update outdated model names," accepted code review comments) and extract the *recurring* defect classes directly from that evidence. The rule set is a transcription of what the population actually fixes, not a guess at what it might fix. The pattern's second half closes the loop: once the rule set exists, run it back over the same (or an equivalently large) corpus and report what fraction of instances trigger each rule — turning "this rule set is comprehensive" from an assertion into a measured claim.

## Mechanism

1. **Assemble a corpus of real corrections** — commit-by-commit history, merged PRs, code review threads — large enough that recurring patterns are statistically visible, not just anecdotal.
2. **Mine the recurring defect classes from the corpus's own language.** Read commit subjects / PR titles for the phrasing maintainers actually use to describe fixes (in `skill-diffs`'s case: "fix YAML frontmatter," "update outdated model names," "add language tags to code blocks"), and let those phrases *become* the rule categories rather than inventing categories independently.
3. **Encode each defect class as a deterministic, checkable rule** — a regex, a structural parse, a threshold — with a severity and a fix hint, so the rule can run without an LLM and produce the same verdict every time on the same input.
4. **Validate the rule set against the corpus, not just against a handful of hand-picked examples.** Run every rule over the full historical population and report per-rule trigger rates. A rule that never fires on real historical data is either wrong or address a defect class too rare to matter; a rule that fires on the overwhelming majority of instances may be miscalibrated (too strict) rather than genuinely diagnostic.
5. **Treat the rule set as a living artifact tied to the corpus's growth** — as more history accumulates (or the population being validated changes conventions), re-derive or re-check the rule set rather than freezing it at its first draft.

## When to use

- You have (or can assemble) a **large historical corpus of real corrections** to the exact kind of artifact you want to validate — not a hypothetical population, an actual one.
- The artifact is common enough, and edited by enough independent people/agents, that recurring defect classes are a real statistical signal rather than one author's pet peeves.
- You want validation rules that are **defensible with evidence** ("this check fires on 34% of real instances, derived from what maintainers actually fix") rather than validation rules that are merely plausible.
- You plan to **re-validate the rule set periodically** as the corpus grows — this pattern is cheapest to sustain when mining and checking are both automatable.

## When NOT to use

- **No real corpus exists yet, or it's too small to show recurring patterns.** For a brand-new artifact type with a handful of instances, hand-authored rules from domain expertise are the only option — don't fabricate a corpus or over-fit rules to 5 examples.
- **The defect you care about is rare-but-catastrophic, not recurring-but-common.** Mining a corpus for *frequency* will systematically under-weight a defect class that's dangerous exactly because it's rare (a security hole that's only ever happened once). Pair defect-derived rules with a separate, deliberately-designed check for known catastrophic failure modes.
- **The corpus itself is biased or low-quality**, e.g. mined from repos with poor review discipline where "what got merged" reflects lax gatekeeping rather than genuine correctness. Mining defect classes from a corpus you haven't also quality-filtered risks encoding the corpus's own bad habits as "rules."
- **You need semantic, not structural, correctness.** This pattern produces rules that are cheap, deterministic, and fast — but by construction they catch what's mechanically checkable (missing fields, deprecated string literals, malformed structure), not whether the content is *substantively* right. Don't oversell a defect-derived linter as a correctness oracle.

## Why it works

It routes a scarce resource — domain judgment about what "good" looks like — to where it's actually needed, and replaces the rest with statistics. A domain expert designing rules from intuition alone is guessing at a distribution they haven't measured; mining the corpus replaces the guess with an empirical answer to "what does this population actually get wrong, and how often." It also produces rules whose *coverage claim* is falsifiable: "13 rules, derived from observed defects" is a testable claim once you've run the rules back over the corpus and reported trigger rates, in a way that "13 rules, based on best practices" never is. The self-validation step (rule set checked against the same corpus it was mined from) is the same discipline this wiki applies to its own claims — evidence over assertion — turned into a mechanical pipeline.

## Detection recipe

- **Look for**: a linter/checklist/validation rule set whose documentation explicitly cites a corpus of real historical corrections as its origin (not "best practices" or an unstated author's intuition), plus a reported coverage/trigger-rate statistic from running the rules back over that corpus.
- **Confirm with**: the rule categories map recognizably onto phrases that appear in the actual corpus (commit subjects, PR titles, review comments) — not onto a generic domain checklist that could have been written without ever looking at real history.
- **Rule out**: a rule set that's merely *described* as evidence-based without a reported validation run (assertion, not measurement) — and the inverse case, a purely statistical anomaly-detector with no interpretable rule categories at all (that's outlier detection, not this pattern; this pattern's rules are legible and named, e.g. "E002-missing-name," not opaque scores).

## Examples in this wiki

- [[artifacts/projects/skill-diffs]] — `skill_linter.py`'s rule set is explicitly "derived from the most common defect patterns observed across the skill-diffs corpus (PR titles like 'fix YAML frontmatter'... reveal what skill maintainers actually fix in merged commits)," and the tool's `--report` mode validates the rule set by running it over the full ~665k-skill corpus, finding 61% of skills trigger at least one rule. — citation: [[sources/SHL0MS--skill-diffs#skill_linter]], [[sources/SHL0MS--skill-diffs#skill_linter-rules]]

*(1 example — held `proposed` per the wiki's own rule that a pattern needs ≥2 artifacts to confirm. A strong candidate 2nd example would be any linter/reviewer in this wiki's other packs whose rules are documented as derived from real historical fixes rather than authored from scratch — none of the currently-ingested packs' lint/review tooling documents that provenance explicitly; check on next ingest of a linter-shipping artifact.)*

## Counter-examples or anti-pattern

- No confirmed counter-example is logged yet in this wiki. The nearest cautionary note is internal to the founding example itself: `skill_linter.py`'s own docstring claims "13 rules," but the current snapshot defines 7 rule functions producing 17 distinct rule codes depending how you count — a reminder that even a defect-derived rule set needs its *own* count kept honest as it evolves (see [[artifacts/projects/skill-diffs]]'s "verified-against-the-tree" note).

## Related patterns

- [[patterns/behavioral/latent-vs-deterministic-split]] — **composes-with.** A defect-derived rule set is, by construction, encoded as deterministic checks; the *mining* step (reading commit messages for recurring phrasing) is itself a latent, judgment-driven pass over the corpus. The pattern is a pipeline that starts latent (mine) and ends deterministic (check).
- [[patterns/quality-bar/complexity-ratchet]] — **relative.** Both patterns treat a growing historical record as an asset rather than noise; the ratchet is forward-only *within one codebase's session history*, while this pattern mines forward-only lessons *across a whole population's* history.
- [[concepts/imitation-vs-correctness-eval]] — **enables.** The gold-independent correctness metric (`linter_delta`) in that concept is only possible because a defect-derived rule set already exists to check against.

## Open questions

- Does the mining step generalize to smaller corpora, or does it need the ~665k-skill scale this founding example has? Untested at smaller n.
- How do you catch defect classes that are *rare but severe* when the mining process is inherently frequency-weighted? The pattern as observed has no answer to this yet — likely needs a deliberate second, hand-authored rule tier for known catastrophic failure modes.
- What's the right cadence for re-validating a defect-derived rule set as the underlying population's conventions shift (e.g., a new agent platform's `SKILL.md`-equivalent format)? Not addressed in the founding example.

## Pstack comparison — 2026-10-24

[[artifacts/plugins/pstack]] is a **related local-scale prescription**, not confirmation of this full corpus-scale pattern: `correct` mines recurring failures and adds negative tests and enforcement, but no measured historical-corpus validation is established. Status and example-count remain unchanged. [[sources/cursor--plugins-pstack#PK18]]
