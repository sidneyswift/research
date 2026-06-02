---
domain: patterns
type: pattern
name: skill-pack-bundle
category: quality-bar
status: confirmed
last-reviewed: 2026-06-02
example-count: 3
---

# skill-pack-bundle

> A skill is not just its `SKILL.md` — it ships as a **tested bundle**: the markdown instruction layer, the minimal deterministic code, and a *test suite that covers all of it* (unit test for the code, LLM eval for the skill, integration test across both, plus the skill's resolver and an eval for the resolver). The tests are what let the skill change without breaking — "what separates it from vibe coding."

## Longer definition

Garry Tan names this primitive directly: *"That bundle is a skill pack. A unit of reusable capability that compounds. The tests are the magic… A skill pack has tests"* ([[sources/garrytan--foxconn-factories#skill-pack]]). The shape he gives it has seven parts produced by a one-word "skillify" loop ([[sources/garrytan--foxconn-factories#skillify-loop]]):

1. the markdown skill (the instruction/intent layer)
2. the minimal code it needs (the thin deterministic I/O layer)
3. a unit test for the code
4. an LLM eval for the skill
5. an integration test across both
6. a resolver so the agent invokes the skill automatically when it's relevant
7. an eval for the resolver

The pattern operates on *a single capability* and produces *a maintainable, composable unit*. A creator reaches for it because markdown behavior is editable prose — which means it drifts silently unless something pins it. The bundle makes "did this edit break the skill?" a runnable question (LLM eval + E2E) rather than a hope. Crucially it tests the **resolver** too — the part that decides *whether the skill fires* — which is where description-triggered skills usually rot.

**Essay #5 (the Skillify Manifesto) expands the bundle to a 10-step checklist** ([[sources/garrytan--skillify-manifesto#skillify-checklist]]) — the same seven parts plus the *system-hygiene* layer that keeps a growing pack coherent:

1. `SKILL.md` — the contract (name, triggers, rules)
2. deterministic code — `scripts/*.mjs` (no LLM for what code can do)
3. unit tests (vitest)
4. integration tests (live endpoints)
5. LLM evals (quality + correctness)
6. resolver trigger (an entry in the routing table)
7. resolver eval (verify the trigger actually routes)
8. **check-resolvable + DRY audit** (is the skill reachable? does it duplicate another's lane?)
9. E2E smoke test
10. **brain filing rules** (a knowledge-writing skill must file by primary subject)

The two steps beyond the essay-#8 list — **8 (reachability + dedup)** and **10 (filing)** — fold the [[patterns/composition/resolver-routing-table]] governance layer into the bundle. Garry's rule: *"A feature that doesn't pass all ten is not a skill. It's just code that happens to work today"* ([[sources/garrytan--skillify-manifesto#skillify-checklist]]). And the loop is one word: prototype in conversation → say **"skillify it"** → the agent emits the whole bundle ([[sources/garrytan--skillify-manifesto#skillify-as-verb]]).

## Mechanism

The essay describes the bundle; **gstack is where you can see all seven parts as real files** ([[sources/garrytan--gstack#CLAUDE.md]], [[sources/garrytan--gstack#test]]). The mapping is near 1:1:

| Skill-pack component | gstack artifact realization |
|---|---|
| markdown skill | `<skill>/SKILL.md`, generated from a `.tmpl` via `bun run gen:skill-docs` |
| minimal code | `browse/`, `design/` (compiled Bun binaries), `bin/` CLI helpers |
| unit test for the code | `test/skill-validation.test.ts`, `gen-skill-docs.test.ts`, `browse/test/` (free, <1s — Tier 1) |
| LLM eval for the skill | `test/skill-llm-eval.test.ts` — LLM-as-judge, ~$0.15/run (Tier 3) |
| integration test across both | `test/skill-e2e-*.test.ts` — end-to-end via `claude -p`, ~$3.85/run (Tier 2) |
| resolver | `scripts/resolvers/*.ts` (preamble, design, review, gbrain, learnings, composition, confidence…) |
| eval for the resolver | `test/resolver-ask-user-format.test.ts`, `test/writing-style-resolver.test.ts`, `test/resolvers-gbrain-put-rewrite.test.ts` |

Two production details make the bundle affordable to run: **diff-based test selection** (each test declares file dependencies in `test/helpers/touchfiles.ts`; only tests whose inputs changed run) and a **two-tier split** (`gate` tests block merge in CI; `periodic` quality/Opus/non-deterministic evals run on a weekly cron) ([[sources/garrytan--gstack#CLAUDE.md]]). That is the answer to the obvious objection — "you can't run a $4 E2E on every commit" — you don't; you run the cheap deterministic tier on every PR and the paid LLM evals selectively.

The "skillify" loop is the *authoring* half: you build a capability interactively until it works, then say **"skillify it"** and the agent emits the whole bundle at once ([[sources/garrytan--foxconn-factories#skillify-loop]]). gstack ships a *narrower, literal* `/skillify` command that codifies a successful `/scrape` flow into `script.ts + script.test.ts + fixture` ([[sources/garrytan--gstack#skillify]]) — i.e. components 2+3 of the bundle for the browser-scrape special case. The general 7-part loop in the essay is the superset.

**gbrain enforces the bundle as a build gate, which is what makes it a full second example.** The Skillify Manifesto states plainly that "the skillify checklist… is what `gbrain doctor` actually checks" ([[sources/garrytan--skillify-manifesto#gbrain-skillpack]]), and the real repo carries the machinery: a `skills/skillify/` skill + `src/core/skillify/generator.ts` (the scaffolder), `src/commands/check-resolvable.ts` + `test/check-resolvable.test.ts` (step 8 reachability), `src/commands/doctor.ts` + `src/core/dry-fix.ts` (`gbrain doctor --fix`, the DRY half of step 8, git-working-tree-guarded), and `skills/_brain-filing-rules.md` (step 10) ([[sources/garrytan--gbrain#skill-skillify]], [[sources/garrytan--gbrain#skills-brain-filing-rules]]). So where gstack demonstrates the bundle *per skill as files*, gbrain demonstrates it *as an enforced checklist a CLI runs* — the same discipline, two surfaces. (Provenance caveat from [[sources/garrytan--skillify-manifesto]]: the per-skill *counts* — "179 unit tests," "35 daily evals" — are author self-claims about his **private** brain; the *machinery* above is verified in the public repo.)

## When to use

- **The skill is production-maintained** — you (or an agent) will keep editing the markdown, and you need each edit to be safe. This is the core case: coverage is what lets prose behavior change without silent regressions.
- **The skill's *triggering* matters**, not just its body — i.e. it auto-fires on description/resolver match and a false fire (or a silent no-fire) is costly. The resolver eval is the distinctive, high-value part.
- **You ship many skills that compound** — at 350+ packs ([[sources/garrytan--foxconn-factories#skillify-loop]]) or 23 interdependent skills (gstack), untested prose becomes unmaintainable; the bundle is what makes a *library* of skills tractable.
- **An agent is doing the authoring** — the "skillify it" loop is designed for the model to emit skill + code + tests + resolver + evals in one shot, so the marginal cost of the full bundle is low.

## When NOT to use

- **Demonstration / reference skills.** A skill whose job is to *show the format* (cf. [[artifacts/plugins/anthropic-skills-marketplace]]) gains little from a shipped LLM-eval + resolver-eval suite; the reader is a human studying it, not a CI pipeline guarding it. Carrying the bundle there is overhead, not safety.
- **One-shot / throwaway capability.** If you'll run it once and discard it, the bundle is pure cost — this is literally the "skillify" *graduation* step, applied only after a capability proves worth keeping.
- **No willingness to pay for evals.** The LLM eval and E2E tiers cost real tokens (~$0.15 and ~$3.85/run in gstack). Without the "tokenmaxxing" posture ([[sources/garrytan--foxconn-factories#tokenmaxxing]]) — or at least diff-based selection + a gate/periodic split — the eval halves get skipped and you're back to validating prose by vibes.
- **The "minimal code" isn't minimal.** The pattern assumes a *thin* deterministic layer under the markdown. If you find yourself writing hundreds of lines of code to "police" the model, you've rebuilt the Foxconn factory the same author warns against ([[sources/garrytan--foxconn-factories#factory-audit]]) — fix the altitude before bundling tests around it.

## Why it works

Markdown behavior is editable natural language, which is the pattern's whole advantage ("the behavior lives in instructions you can edit in plain language instead of logic frozen in code" — [[sources/garrytan--foxconn-factories#jit-software]]) **and** its hazard: prose has no compiler, so a one-word edit can change behavior with zero signal. The bundle converts that hazard into a runnable check. It works because it tests at the right *layers*: deterministic code gets cheap unit tests; the non-deterministic skill gets an LLM-as-judge eval; their interaction gets an E2E; and the **resolver** — the meta-decision of whether to fire at all — gets its own eval, which is exactly the failure mode that description-triggered skills (and Anthropic's auto-trigger heuristic) leave unguarded. gstack's `gate`/`periodic` tiering and diff-based selection ([[sources/garrytan--gstack#CLAUDE.md]]) are what keep the expensive non-deterministic evals economically runnable, which is the practical reason the pattern survives contact with a real CI budget.

## Examples in this wiki

- [[artifacts/plugins/gstack]] — **the one fully-worked example.** All seven components exist as real files: generated `SKILL.md` + `browse/`/`design`/`bin` code + `skill-validation`/`gen-skill-docs` unit tests + `skill-llm-eval` (LLM-as-judge) + `skill-e2e-*` integration + `scripts/resolvers/*` + resolver tests (`resolver-ask-user-format`, `writing-style-resolver`, `resolvers-gbrain-put-rewrite`), run under a diff-selected `gate`/`periodic` two-tier harness. — citation: [[sources/garrytan--gstack#CLAUDE.md]], [[sources/garrytan--gstack#test]]
- [[artifacts/plugins/gbrain]] — **the second full example: the bundle as an enforced build gate.** `gbrain doctor` *is* the 10-step checklist ([[sources/garrytan--skillify-manifesto#gbrain-skillpack]]); the repo ships `skills/skillify/` + `src/core/skillify/generator.ts` (scaffold), `src/commands/check-resolvable.ts` + test (step 8), `src/commands/doctor.ts` + `src/core/dry-fix.ts` (step 8 DRY), `skills/_brain-filing-rules.md` (step 10), plus quantitative evals shipped *with* the pack (BrainBench; self-reported P@5 49.1% / R@5 97.9%). Where gstack shows the bundle *as per-skill files*, gbrain shows it *as a checklist a CLI enforces*. — citation: [[sources/garrytan--gbrain#skill-skillify]], [[sources/garrytan--gbrain#skills-brain-filing-rules]], [[sources/garrytan--gbrain#README]], [[sources/garrytan--skillify-manifesto#skillify-checklist]]
- [[artifacts/plugins/compound-engineering]] — **the non-Garry third example that retires the same-creator caveat.** A tested skill pack from Every (Kieran Klaassen): **~1,094 test cases across 52 files**, including **behavioral contract tests** that assert a skill conforms to its contract (`review-skill-contract.test.ts`, `pipeline-review-contract.test.ts`), **convention-as-test** (`skill-agent-ce-prefix.test.ts`; `frontmatter.test.ts` enforces the *description* constraints that make the built-in resolver fire — ≤1024 chars, quoted colons, no angle-bracket tokens), and **safety tests** (`skill-shell-safety`, `path-sanitization`, `manifest-path-safety`) — all gating merge via branch protection. *Honest nuance on completeness:* CE has markdown + thin code + unit/integration/contract/safety tests, but it leans on the **harness's built-in description-resolver** rather than shipping a dedicated resolver + *resolver eval* the way gstack/gbrain do — it tests the resolver *surface* (the description) without a separate routing eval. **Test-complete, resolver-light.** — citation: [[sources/every--compound-engineering-plugin#tests]], [[sources/every--compound-engineering-plugin#cross-platform-authoring]]
- *Articulation (not an artifact):* [[sources/garrytan--foxconn-factories#skill-pack]] (the 7-part definition) and [[sources/garrytan--skillify-manifesto#skillify-checklist]] (the 10-step expansion) — the author's own definition of the bundle and the "skillify" loop.

> **Confirmed; same-creator caveat retired 2026-06-02.** Three in-wiki artifacts now demonstrate the tested-bundle discipline across **two ecosystems**: gstack (the 7 components as real files) and gbrain (`gbrain doctor` enforcing all 10 steps) — both Garry Tan — plus [[artifacts/plugins/compound-engineering]] (Every / Kieran Klaassen; ~1,094 cases incl. behavioral contract tests, branch-protection-gated). "A skill pack has tests" is therefore a **cross-ecosystem convention**, not one creator's house style. **One refinement survives the retirement:** the *resolver eval* — testing whether a skill *fires*, not just what it outputs — remains best demonstrated by Garry (gstack/gbrain ship explicit resolver evals); CE and [[artifacts/plugins/anthropic-financial-services-marketplace]] test skill *output*/*contracts* but lean on the harness's built-in description-resolver. So "resolver eval" is still the rarest, most-stealable part of the bundle.

## Counter-examples or anti-pattern

- [[artifacts/plugins/anthropic-skills-marketplace]] — Anthropic's demonstration skills ship as minimal-frontmatter `SKILL.md` reference implementations *without* per-skill LLM evals or resolver evals. That's the **correct** choice for reference material (the consumer is a human learning the format), and it sharpens the pattern's scope: the bundle is a *production-maintenance* discipline, not a universal one. A skill meant to be read ≠ a skill meant to be defended in CI.
- **The Foxconn-factory anti-pattern (the inverse failure).** The same essay's self-audit — ~276K lines of tests "bolted on to police" the app, 127 jobs, a 1,778-line fact-checker fanning every claim out to five sources ([[sources/garrytan--foxconn-factories#factory-audit]]) — is what skill-pack testing must *not* become. The distinction is altitude: skill-pack tests pin a *thin* markdown+code unit so it can change safely; the Foxconn factory is mountains of code written to distrust a capable model. Same word ("tests"), opposite spirit. If your "skill pack" is mostly defensive code, you've crossed back over the line.

## Related patterns

- [[patterns/quality-bar/complexity-ratchet]] — closest sibling: the skill-pack bundle is the **unit** (one tested skill); the complexity ratchet is the **system property** that unit produces at scale (every session adds tests/docs/evals that reload into context, so the quality floor only rises). Read together.
- [[patterns/composition/resolver-routing-table]] — supplies two of the bundle's parts (the resolver trigger + the resolver eval) and step 8 (check-resolvable). The bundle is where those tested-routing pieces live per skill.
- [[patterns/structural/thin-harness-fat-skills]] — the bundle is *what a single fat skill ships as*; [[patterns/behavioral/latent-vs-deterministic-split]] — the bundle's "minimal code" (with unit tests) is the deterministic half, the skill (with LLM evals) the latent half.
- [[patterns/composition/single-source-multi-surface-distribution]] — composes-with: single-sourcing keeps one definition across surfaces; the bundle is what makes that one definition *safe to edit*. gbrain does both.
- *(proposed, tracked on [[artifacts/plugins/anthropic-financial-services-marketplace]]):* "quantitative evals shipped with the artifact" — FSI and gbrain both ship evals as proof-of-quality; that's the *eval-shipping* sub-mechanism of this one.

## Open questions

- **Does a non-Garry artifact ship the full bundle?** That's the promotion gate. Candidates to check: do any [[artifacts/plugins/anthropic-financial-services-marketplace]] skills carry resolver-level evals, or only output/quality evals?
- **Is the resolver eval actually the rare part?** Hypothesis: lots of people test skill *output*; almost nobody tests skill *triggering*. If true, "resolver eval" is the single most stealable idea here.
- **What's the real cost curve?** gstack's diff-based `gate`/`periodic` split implies the full bundle is too expensive to run naively. Quantify: what fraction of commits trigger a paid eval in practice? (Needs a CHANGELOG/CI skim.)
- **Granularity mismatch.** The essay frames the bundle as *per-skill*; gstack's strongest evidence is *repo-level* test architecture (one `skill-llm-eval.test.ts` covering many skills, not one per skill). Is the true unit the individual skill, or the pack? This affects how the pattern is described and reused.
