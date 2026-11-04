---
domain: artifacts
subdomain: projects
type: project
name: tibo-dog
creator: "[[creators/lauren-tan]]"
source: "[[sources/poteto--tibo-engineering]]"
ecosystem: browser-game / agent-assisted-engineering
status: author-report-investigated
last-reviewed: 2026-11-03
---

# tibo.dog — make engineering intent executable

> The portable lesson is not to maximize agent-written PRs. It is to turn discovered failure modes and product requirements into durable checks, while keeping humans responsible for what those checks mean.

## Attributes

- **Unit of study:** Lauren Tan's engineering account of tibo.dog, a browser game built with coding agents; not an audit of a game repository. The parent announcement credits Grok bot and Cursor. [[sources/poteto--tibo-engineering#parent]]
- **Evidence:** complete long-form X post published November 1, 2026; parent post; four downloaded and visually inspected images; game homepage and About page captured November 3. No game revision, source tree, formal model, benchmark trace, or production replay implementation was supplied or executed. [[sources/poteto--tibo-engineering#root]] [[sources/poteto--tibo-engineering#current-site]]
- **Reported throughput:** approximately 1,150 PRs in four days. The screenshot gives an initial-commit date, not an independently checked merge count, quality measure, or comparison against human-only work. [[sources/poteto--tibo-engineering#throughput]]
- **Availability / licensing:** public playable URL `https://tibo.dog/`; no code license established by this source. A public game is not evidence of an open-source implementation. [[sources/poteto--tibo-engineering#current-site]]
- **Dated attention:** 3,712 likes and 5,945 bookmarks at retrieval; exact metrics and timestamp remain in the citation page. [[sources/poteto--tibo-engineering#traction]]

## Relationships

- **Creator:** [[creators/lauren-tan]].
- **Source:** [[sources/poteto--tibo-engineering]].
- **Related toolkit:** [[artifacts/plugins/pstack]], [[artifacts/skills/poteto-mode]], and [[artifacts/skills/statechart]] share the creator and related design concerns. The post does not identify the game's exact skills, installed package versions, or renderer; this is a comparison, not proven dependency provenance. [[sources/poteto--tibo-engineering#formal-verification]] [[sources/cursor--plugins-pstack#PK01]]
- **Related concepts:** [[concepts/verification-model-fidelity]] explains the model/implementation boundary; [[concepts/durable-agent-execution]] distinguishes simulation replay from recovery of external effects.

- **Follow-up principle source:** [[sources/poteto--verification-over-adversarial-review]] — separate screenshot-backed position, added as principle 17; not part of the original 14-bullet game post.

## Mechanism and themes

The author's workflow has two compounding loops. The **correction loop** turns a discovered defect into a lint rule that future changes must satisfy. The **product loop** expresses behavior and operating requirements as models, input replay, build limits and simulated outcomes. Fast code production operates inside those constraints; the post does not measure how much of the reported speed each constraint caused. [[sources/poteto--tibo-engineering#defect-lints]] [[sources/poteto--tibo-engineering#formal-verification]] [[sources/poteto--tibo-engineering#download-budget]] [[sources/poteto--tibo-engineering#headless-tuning]]

The interesting naming choice is `.hot.ts`: a path tells a human or agent that the file runs every frame/tick **and** selects an allocation rule. The enforcement comes from the linter, not the filename by itself. Similarly, a download target becomes a build failure, and a claimed score becomes input for server recomputation instead of being accepted on client authority. These are distinct checks with distinct coverage. [[sources/poteto--tibo-engineering#hot-paths]] [[sources/poteto--tibo-engineering#download-budget]] [[sources/poteto--tibo-engineering#deterministic-replay]]

### Formal methods at interaction boundaries

The attached close-up reports three auto-pick bugs: a timer interrupts a tutorial, auto-pick runs while the player is away, and reroll leaves auto-pick targeting the old hand. The wider diagrams separate concurrent story, fires, dialogue/lines, pause and offer state. The portable concern is **interleaving**: each feature can appear sensible alone while its transitions conflict with another region. This is why a subsystem model can be more informative than adding another happy-path test. This last sentence is our interpretation of the displayed failures, not a controlled comparison. [[sources/poteto--tibo-engineering#auto-pick-counterexamples]] [[sources/poteto--tibo-engineering#statechart-images]]

The post reports one formal-verification skill per major system. Reuse that scope boundary, but import the separate fidelity discipline: name properties, retain code/model mappings, record bounds and revision, and establish that counterexamples correspond to actual code. The screenshots do not establish these steps were followed in the game. [[sources/poteto--tibo-engineering#formal-verification]] [[sources/cursor--plugins-pstack#VE08]] [[sources/cursor--plugins-pstack#VE11]]

### Authority and guarantee boundaries

| Input / intent | Reported enforcement | What remains unverified |
| --- | --- | --- |
| Discovered defect | New lint rule | Coverage, false positives, negative fixtures, actual mandatory invocation |
| `.hot.ts` file classification | Allocation constructs forbidden in that file class | Correct classification and allocations through callees, libraries or runtime internals |
| Temporal state properties | TLA+ checks / subsystem skills | Model fidelity, explored bounds, properties, raw counterexamples and fixed-code replay |
| Client high-score submission | Server replays submitted inputs | Version/seed pinning, allowed-input validation, botting, tamper resistance and replay cost |
| Initial-download requirement | Build fails over its budget | Exact threshold, compressed entry-point accounting and actual deployed payload |
| Difficulty target | Headless bots measured against survival rates | Seeds, sample size, statistical uncertainty and correspondence to real players |

The rows describe the author's reported boundaries, not verified implementation guarantees. The unverified column identifies the evidence needed before adopting stronger claims. [[sources/poteto--tibo-engineering#defect-lints]] [[sources/poteto--tibo-engineering#hot-paths]] [[sources/poteto--tibo-engineering#formal-verification]] [[sources/poteto--tibo-engineering#deterministic-replay]] [[sources/poteto--tibo-engineering#download-budget]] [[sources/poteto--tibo-engineering#headless-tuning]]

## Patterns demonstrated

- [[patterns/behavioral/latent-vs-deterministic-split]] — supporting author-reported example: agents help create code/checks; lint, builds and replay evaluate mechanical conditions. Deciding the right invariant or player experience remains judgment. [[sources/poteto--tibo-engineering#defect-lints]] [[sources/poteto--tibo-engineering#deterministic-replay]]
- [[patterns/behavioral/evidence-gated-completion]] — narrower product-level analogy: build acceptance is gated by download size and a submitted score by replay. This is not evidence that an agent's entire completion/stop workflow is enforced. [[sources/poteto--tibo-engineering#download-budget]] [[sources/poteto--tibo-engineering#deterministic-replay]]
- [[patterns/quality-bar/defect-derived-validation]] — related online, local-scale variant only. The post describes issue → rule, not corpus mining plus measured historical coverage. Keep that existing pattern proposed; do not inflate its example count. [[sources/poteto--tibo-engineering#defect-lints]]
- **Candidate mechanism, retained here rather than duplicated into a new page:** semantic filenames select executable policy (`.hot.ts` → allocation ban). A broader pattern needs another independently grounded implementation. [[sources/poteto--tibo-engineering#hot-paths]]

## What we'd steal

Each entry separates an observed report from our proposed adaptation and its limit. ★ marks priorities, not omissions from the ledger.

1. **★ Turn a discovered bug into prevention.** The author asks for a lint rule after each issue. Adaptation: choose the cheapest meaningful guard for the actual failure—lint for syntax/structure, a regression test for behavior, a model for ordering—and preserve a failing example. Trigger: an observed defect with a stable, checkable invariant. Limit: do not manufacture a lint rule for subjective taste or claim that every defect is statically decidable. [[sources/poteto--tibo-engineering#defect-lints]]
2. **★ Put operational context where both agents and tools can see it.** `.hot.ts` identifies frame/tick code and selects an allocation ban. Adaptation: a small naming convention can route local policy without loading a long document. Trigger: a real code class with stricter constraints. Limit: verify that all relevant code is classified; a local syntax ban does not prove a transitive call graph is allocation-free. [[sources/poteto--tibo-engineering#hot-paths]]
3. **★ Model interactions, not only feature happy paths.** The author uses TLA+ across game systems. Adaptation: apply a bounded model when timer, pause, retry, cancellation or competing state transitions create hard-to-enumerate failures. Trigger: overlapping transitions and a consequential invariant. Limit: a passing abstraction is not proof of its implementation; keep source mappings and replay real counterexamples. [[sources/poteto--tibo-engineering#formal-verification]] [[sources/poteto--tibo-engineering#auto-pick-counterexamples]] [[sources/cursor--plugins-pstack#VE11]]
4. **★ Make verification subsystem-specific and reusable.** One verification skill per major system is reported. Adaptation: keep the promise, covered state, reproducible command and revision beside the system, so the next agent can rerun the right check. Trigger: a subsystem whose correctness needs repeated verification. Limit: the post does not expose the actual skill files or maintenance process. [[sources/poteto--tibo-engineering#formal-verification]]
5. **★ Make results reproducible from inputs.** The simulation reportedly replays a run exactly. Adaptation: preserve sufficient inputs, initial state, randomness and implementation version to reproduce a bug or evaluation. Trigger: expensive failures that are difficult to reproduce from screenshots. Limit: those preservation details are adaptation requirements, not inspected game implementation. [[sources/poteto--tibo-engineering#deterministic-replay]]
6. **★ Recompute consequential claims at the authority boundary.** The server reportedly replays high scores. Adaptation: prefer independently derived outcomes over trusting a client-supplied summary when replay is affordable. Limit: valid simulation inputs can still be machine-generated or manipulated; replay is not proof of human play or a complete anti-cheat system. Do not transfer pure simulation replay directly to billing or other external side effects. [[sources/poteto--tibo-engineering#deterministic-replay]]
7. **★ Fail the build on a real resource budget.** First-download size is a build gate. Adaptation: define the user path, compression/accounting method and acceptable threshold, then check that exact artifact. Trigger: a measured size/latency/cost constraint that matters to use. Limit: the reported 124 KB is an achieved size, not the disclosed threshold; do not turn it into a universal budget. [[sources/poteto--tibo-engineering#download-budget]]
8. **★ Tune against outcomes with a headless harness.** Bots tune difficulty to target survival rates. Adaptation: choose an observable success/failure distribution, fixed scenarios, held-out cases and uncertainty reporting. Trigger: a repeatable tuning problem with measurable outcomes. Limit: optimizing for bots can miss human understanding, enjoyment and accessibility. [[sources/poteto--tibo-engineering#headless-tuning]]
9. **Keep a deliberate library/custom-code boundary.** The author delegates 3D rendering to three.js while owning simulation, audio and post-processing. Adaptation: use existing components for commodity work and own the behavior needed for product constraints. Limit: this is one project's boundary, not evidence that writing a custom engine is generally cheaper. [[sources/poteto--tibo-engineering#engine-boundary]]
10. **Use text/code as an editable asset representation when it fits the medium.** Music and sound are synthesized live; songs and sprites live as code. Adaptation: make small procedural assets diffable, reproducible and agent-editable. Limit: runtime synthesis trades transfer bytes for runtime work and has artistic/accessibility constraints; it is not a universal replacement for authored media. [[sources/poteto--tibo-engineering#procedural-audio]] [[sources/poteto--tibo-engineering#procedural-art]]
11. **Separate editable source assets from optimized delivery.** Individual sprites share one palette and are packed into an atlas at build time. Adaptation: preserve small reviewable sources and automate the runtime representation; centralized style constraints reduce drift. Limit: the pipeline, atlas settings and measured rendering benefits were not inspected. [[sources/poteto--tibo-engineering#procedural-art]]
12. **Preserve continuity through state changes.** Biome music changes without abandoning the preceding melody. Adaptation: specify transition behavior, not just endpoint assets; a feature's handoff can matter as much as each state. Limit: seamlessness is the author's qualitative report, not our listening test. [[sources/poteto--tibo-engineering#music-continuity]]
13. **Design for the real distribution surface.** The target ranges from a small embedded X card to fullscreen, with a stated mid-range-phone workload. Adaptation: use the smallest entry surface and representative device/workload as acceptance cases. Limit: 60 fps with 500 enemies is the stated bar, not a reproduced result. [[sources/poteto--tibo-engineering#runtime-target]]
14. **Make completed work generate its own shareable artifact.** Each run gets a localized OG image from final statistics. Adaptation: attach an automatically generated, accurate result summary to a completed workflow. Limit: counts and localization support change; preserve the historical ten-language report separately from the current site's 27-language description. [[sources/poteto--tibo-engineering#share-and-localize]] [[sources/poteto--tibo-engineering#current-site]]
15. **Prefer names and executable examples for explanations they can carry.** The author goes further and bans comments with lint. Adaptation: improve names/types/tests when prose merely repeats mechanics. Limit: retain legal notices, external constraints, design rationale and explanations a test cannot express; do not copy a universal comment ban. This is deliberately narrower than the source's rule. [[sources/poteto--tibo-engineering#comments]] [[sources/cursor--plugins-pstack#OR42]]
16. **Treat delivery volume as context, not the objective.** The four-day / 1,150-PR report makes the scale noteworthy. Adaptation: measure user-visible results, failure recurrence and review burden alongside throughput. Limit: the source provides no controlled productivity comparison, maintenance cost or verified PR audit. [[sources/poteto--tibo-engineering#throughput]]

17. **★ Prefer empirical + formal verification over abstract adversarial review.** In a separate screenshot supplied after the game-post ingest, Lauren argues that abstract agent review spends tokens on nitpicks and YAGNI-related objections, and reports reducing pstack's `interrogate` usage. Adaptation: spend the verification budget on real execution, reproducible tests and scoped formal checks; use reviewer concerns to generate falsifiable cases rather than more ungrounded debate. Trigger: a correctness claim that can be exercised or modeled. Limit: this is an attributed engineering preference, not a measured universal result; preserve targeted judgment for requirements, model assumptions and risks the checks do not cover. The post discusses possible future removal, not completed deletion. Canonical synthesis: [[concepts/review-cost-aware-workflows#principle-verification-over-abstract-adversarial-review]]. [[sources/poteto--verification-over-adversarial-review#verification-first]] [[sources/poteto--verification-over-adversarial-review#pstack-direction]] [[sources/poteto--verification-over-adversarial-review#failure-mode]]

## Tensions and anti-patterns

- **Do not launder a report into a benchmark.** Assertions about GC stutter, deterministic replay, build size and speed remain attributed; diagrams strengthen specificity but do not independently verify execution. [[sources/poteto--tibo-engineering#hot-paths]] [[sources/poteto--tibo-engineering#statechart-images]]
- **Do not equate a familiar design with proven tool usage.** The existing pstack study offers relevant techniques, but the post does not name its package version or prove these diagrams were rendered by the cataloged statechart skill. [[sources/poteto--tibo-engineering#formal-verification]]
- **Do not erase time.** The November 1 post says ten languages; the November 3 site says 27. These are separately dated author/publisher descriptions, plausibly reflecting change, but no release history was inspected to settle why. [[sources/poteto--tibo-engineering#share-and-localize]] [[sources/poteto--tibo-engineering#current-site]]
- **Do not overgeneralize local constraints.** Allocation bans, synthesized assets, custom subsystems and comment prohibitions serve a particular game. Transfer the requirement → check mechanism, not every policy verbatim. [[sources/poteto--tibo-engineering#hot-paths]] [[sources/poteto--tibo-engineering#engine-boundary]] [[sources/poteto--tibo-engineering#comments]]

## Open questions and verification record

- **Unverified implementation:** which public or authorized repository/revision would let us inspect lint coverage, build accounting, models and server validation? The post does not supply one.
- **Unverified performance:** what device/browser, warm-up, runtime distribution, memory trace and download artifact substantiate the goals? Need reproducible runs, not inferred metrics.
- **Unverified model fidelity:** what properties/bounds were checked, and can the reported counterexamples be replayed against the before/after implementation?
- **Unverified tuning:** which bot policies, seeds, target rates and human playtests constrain the difficulty search?
- **Completed research scope:** full post recovered from `note_tweet`, parent read, all four images preserved and visually reviewed, linked game pages captured, source anchors mapped, principles deduplicated against existing pages. No game/agent workflows installed or run. [[sources/poteto--tibo-engineering#capture]] [[sources/poteto--tibo-engineering#root]]

Wiki validation results and the unchanged pre-existing lint backlog are recorded in [[log]].
