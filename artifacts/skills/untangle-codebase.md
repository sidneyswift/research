---
domain: artifacts
type: skill
name: untangle-codebase
creator: "[[creators/caldoai]]"
source: "[[sources/caldoai--skills]]"
ecosystem: cross-platform
discovered-via: other
status: active
last-reviewed: 2026-11-09
popularity-signals:
  - signal: github-stars
    value: 966
    as-of: 2026-11-09
    source: "[[sources/caldoai--skills#popularity]]"
---

# untangle-codebase

> Organize a codebase around what changes together: expose hidden dependencies, remove unnecessary coupling, and connect multiple symptoms to one structural fix.

## Attributes

- **What it does:** prescribes a whole-codebase refactor: inventory, redesign, implement, then repeat independent inspection. It targets agent navigation and maintenance, not a separate bug hunt. Claimed benefits are fewer search tokens, silent breaks and debugging delays; no benchmark accompanies them. [[sources/caldoai--skills#claims]] [[sources/caldoai--skills#completion]]
- **Trigger description (verbatim):** “Untangle a whole codebase in one pass, so agents working in it read less per change, break less without noticing, and debug faster.” Declares `disable-model-invocation: true` and an optional area/concern argument. These are source metadata, not proof every host honors the same invocation semantics. [[sources/caldoai--skills#invocation]]
- **Routing neighborhood:** overlaps architecture improvement and refactoring in [[artifacts/plugins/mattpocock-skills]], but this skill asks for a broad end-to-end transformation, not only a report/pick-one opportunity scan. It explicitly avoids a separate bug hunt. Comment/test pruning is an optional scope extension, not an automatic consequence of invoking the main refactor. Routing retention, discovery and actual task success are untested. [[sources/caldoai--skills#scope]] [[sources/caldoai--skills#redesign]] [[sources/mattpocock--skills#README-why]]
- **Bundled resources:** a single 142-line, 8,881-byte `SKILL.md` (about 2.2k tokens by bytes/4; not tokenizer-measured). No scripts, reference files, subagent definitions or tests. The whole repository is four files including README, marketplace and license. One body-loading level; its example is internal. [[sources/caldoai--skills#inventory-receipt]]
- **Execution dependencies:** a host with code inspection/editing/testing capability; suggests subagents, Git history and ad-hoc skeleton/dependency graph scripts. No particular graph tool, language, test runner or MCP is specified. [[sources/caldoai--skills#context-tools]]
- **Distribution:** README describes skills CLI, Claude Code marketplace and manual copy routes. Marketplace names one plugin with `source: "./"`, `strict: false` and the explicit skill path. Cross-agent installation is advertised, not tested here. [[sources/caldoai--skills#root]] [[sources/caldoai--skills#marketplace]]
- **License:** MIT; copyright 2026 Maze. [[sources/caldoai--skills#license]]

## Relationships

- Creator: [[creators/caldoai]]; full pinned source: [[sources/caldoai--skills#root]].
- Comparison: [[artifacts/plugins/mattpocock-skills]] for deep-module vocabulary and architecture improvement; no fork or influence claimed.
- Context/records: [[concepts/artifact-centered-agent-context]] and [[patterns/behavioral/diarization]] for skeletons, summaries and a compaction-resistant decision log.
- Completion/review: [[concepts/completion-contract]], [[concepts/agentic-loop]], [[concepts/review-cost-aware-workflows]] and [[artifacts/skills/loop-library]] provide contrasting evidence and bounded-loop contracts.
- Test-evidence comparison: [[artifacts/skills/security-audit]] separates actual validators from agent instructions. This skill has the latter only.
- Distribution/invocation: [[concepts/skill-invocation-axis]], [[concepts/workspace-skill-distribution]] and [[concepts/lifelong-skill-routing]]. No other skill is explicitly invoked by this source.

## What problem it solves

A seemingly small change can require reading and editing scattered files because the code hides real dependencies, exposes internals or carries unnecessary indirection. The skill offers one unifying diagnostic question—whether pieces should change together—and asks the agent to repair the structure behind several symptoms rather than repeatedly patching each one. Its efficiency claim is a plausible design objective, not measured evidence in this repository. [[sources/caldoai--skills#inventory]] [[sources/caldoai--skills#redesign]] [[sources/caldoai--skills#claims]]

## How it works (mechanism)

### 1. Scope the optional destructive cleanup

The main job is refactoring. Before starting, the source asks which additional comment/test cleanup to perform and limits those additions to the choices. This is a workflow instruction, not a host permission mechanism. In this ingestion we only study it: no target code, comments or tests are being changed. [[sources/caldoai--skills#scope]]

### 2. Inventory relationships before changing code

| Category | Source's diagnostic examples | Intended correction |
| --- | --- | --- |
| Hidden links | Duplicated values/logic, global/file coupling, features scattered by layer, implicit call order | Make real dependency/change boundaries visible |
| Needless links | Consumers of internals, stable modules depending on volatile ones, caller-specific general parameters, shallow modules | Decouple different reasons to change |
| Surplus | Pass-through wrappers, unused extension/config points, dead code | Remove structures without a present responsibility |

These are heuristics for source inspection, not proof that every wrapper or cross-folder feature is bad. The skill separately lists special cases—specific values/callers, swallowed errors, sleeps/retries and disabled tests—as requirements to investigate. Its later instruction explicitly retains exceptions the redesigned system still needs. [[sources/caldoai--skills#inventory]] [[sources/caldoai--skills#special-cases]] [[sources/caldoai--skills#redesign]]

### 3. Map many symptoms to fewer design decisions

The example turns ten listed problems into three proposed changes: restore dialog focus generically instead of sleeping and setting a global exception flag; hide two actual payment providers behind one interface; give commands a shared definition consumed by menus, toolbar, shortcuts, palette and undo. Each fix owns its supporting symptom list. These are illustrative paths/snippets, not a committed application refactor or before/after experiment. [[sources/caldoai--skills#decision-log]]

The generalization test is present needs, not hypothetical extensibility. Two providers give a concrete reason for an abstraction; one universal command registry may work for shared command semantics but should not conflate distinct authorization or lifecycle rules. That last qualification is our inference, not demonstrated by the example. [[sources/caldoai--skills#provider-example]] [[sources/caldoai--skills#command-example]] [[patterns/behavioral/context-is-not-authority]]

### 4. Preserve useful context and regression evidence

Optional comment cleanup distinguishes information tied to the implementation from external facts the code cannot express. Workaround explanations disappear only when their underlying problem is removed. Optional test cleanup happens last: rewrite implementation-coupled tests around behavior and remove checks that cannot catch a real regression. The skill prescribes these judgments; it supplies no mutation-test proof, coverage check or automatic deletion validator. [[sources/caldoai--skills#comments]] [[sources/caldoai--skills#tests]]

### 5. Reinspect, using evidence rather than reviewer confidence alone

Subagents are instructed to search the same categories until no worthwhile issues remain. Completion also requires fewer special cases, local typical changes, sensible/stability-directed imports and unchanged intended behavior except incidental bug fixes. Only the final behavior test is explicitly requested; no pre-change baseline, named commands, time/iteration budget or formal acceptance artifact is specified. Those are implementation choices an adopting team must supply, not features this repository implements. [[sources/caldoai--skills#completion]]

Skeletons and summaries compress navigation context, while dependency graphs and Git co-change history offer structural/historical signals. Scripts are suggested, not bundled. Our reading: generate skeletons as derived views rather than deleting target function bodies; treat Git correlation and import frequency as evidence to interpret, not proof of a business boundary. A shallow history may miss the relevant changes. [[sources/caldoai--skills#context-tools]]

## Patterns demonstrated

- [[patterns/behavioral/diarization]] — a decision log retains why one fix resolves several symptoms across compaction. [[sources/caldoai--skills#decision-log]] [[sources/caldoai--skills#context-tools]]
- [[patterns/behavioral/latent-vs-deterministic-split]] — model judgment interprets coupling; suggested scripts expose imports and skeletons. There is no bundled deterministic enforcement layer. [[sources/caldoai--skills#context-tools]]
- [[patterns/structural/thin-harness-fat-skills]] — methodology lives entirely in prose; supporting evidence for the skill layer, not an inspected runtime architecture. [[sources/caldoai--skills#inventory-receipt]]
- [[patterns/composition/single-source-multi-surface-distribution]] — one skill body is offered through CLI, marketplace and manual installation; host conformance untested. [[sources/caldoai--skills#root]] [[sources/caldoai--skills#marketplace]]
- [[patterns/quality-bar/complexity-ratchet]] — preserve the test safety net through refactoring and investigate vacuous tests; weaker than an enforced quality floor. [[sources/caldoai--skills#tests]]
- [[patterns/behavioral/evidence-gated-completion]] — final behavior preservation is required, but qualitative reviewer satisfaction and a low special-case count do not establish it. Supporting prescription/limit, not a new enforced example. [[sources/caldoai--skills#completion]]

## Source citations

- Procedure, diagnostic taxonomy and optional scope: [[sources/caldoai--skills#scope]] [[sources/caldoai--skills#inventory]] [[sources/caldoai--skills#redesign]].
- Comments/tests and completion limits: [[sources/caldoai--skills#comments]] [[sources/caldoai--skills#tests]] [[sources/caldoai--skills#completion]].
- Context techniques and worked ledger: [[sources/caldoai--skills#context-tools]] [[sources/caldoai--skills#decision-log]].
- Packaging, license, complete inventory and dated popularity: [[sources/caldoai--skills#marketplace]] [[sources/caldoai--skills#license]] [[sources/caldoai--skills#inventory-receipt]] [[sources/caldoai--skills#popularity]].

## What makes it great

Its strongest design move is a shared explanatory test for duplication, coupling, module depth and unnecessary abstractions: reasons to change. That makes the inventory useful for redesign rather than merely collecting style complaints. The many-to-one decision log makes each proposed abstraction answerable to concrete problems, while the comment rule preserves facts about the outside world. These are strengths of the procedure's design, not measured evidence that running it produces better software. [[sources/caldoai--skills#inventory]] [[sources/caldoai--skills#decision-log]] [[sources/caldoai--skills#comments]]

## What we'd steal

Exhaustive portable ledger; application qualifications are our synthesis, not silently added upstream rules.

1. ★ Evaluate architecture through concrete change scenarios: which pieces must move together and which should not? [[sources/caldoai--skills#inventory]]
2. Name the desired operational benefit—less search/context, fewer unnoticed breaks, faster debugging—and measure it separately from aesthetic cleanup. [[sources/caldoai--skills#claims]]
3. Keep optional comment/test pruning separately scoped from the core structural change. [[sources/caldoai--skills#scope]]
4. Inventory problems before editing, so the first symptom does not dictate the whole design. [[sources/caldoai--skills#inventory]]
5. Expose duplicated rules/values that require coordinated edits. [[sources/caldoai--skills#inventory]]
6. Make global/file state dependencies and lifecycle ordering explicit. [[sources/caldoai--skills#inventory]]
7. Colocate features when real changes cut across artificial layer folders; do not equate physical proximity with good design by itself. [[sources/caldoai--skills#inventory]]
8. Protect stable callers from volatile internals with a boundary justified by actual requirements. [[sources/caldoai--skills#inventory]]
9. Move caller-specific vocabulary out of supposedly general interfaces unless it represents a shared responsibility. [[sources/caldoai--skills#inventory]]
10. Prefer interfaces that hide implementation changes rather than exposing every internal decision. [[sources/caldoai--skills#inventory]]
11. Question wrappers, configuration and extension points that add no present responsibility; confirm their role before removal. [[sources/caldoai--skills#inventory]]
12. Treat apparent dead code as a removal candidate, with dynamic/external consumers considered before declaring it unused. This qualification is ours. [[sources/caldoai--skills#inventory]]
13. Use special cases as requirement clues; a retry or disabled test is a reason to investigate, not automatic evidence of bad design. [[sources/caldoai--skills#special-cases]] [[sources/caldoai--skills#redesign]]
14. ★ Search for the one structural fix behind several symptoms, including fixes that look unlike the original complaints. [[sources/caldoai--skills#redesign]]
15. Record each proposed fix above the exact problems it resolves; retain paths and evidence. [[sources/caldoai--skills#decision-log]]
16. Retain necessary exceptions and avoid an unrelated bug-hunting expansion; record any incidental behavior corrections explicitly. [[sources/caldoai--skills#redesign]] [[sources/caldoai--skills#completion]]
17. Preserve comments about external constraints; prune implementation restatements only within authorized scope. [[sources/caldoai--skills#comments]]
18. Remove workaround commentary with the underlying workaround, not merely because it looks dated. [[sources/caldoai--skills#comments]]
19. ★ Keep tests as a safety net until the structural work is complete; optional test cleanup comes last. [[sources/caldoai--skills#tests]]
20. Rewrite tests around stable behavior when internal changes cause false failures. [[sources/caldoai--skills#tests]]
21. Challenge implementation-mirroring and vacuous tests by the regression they could detect; this skill supplies the criterion, not an automated proof. [[sources/caldoai--skills#tests]]
22. Give fresh reviewers the diagnostic categories rather than only an unstructured request to criticize. [[sources/caldoai--skills#completion]]
23. Check typical change locality and dependency direction alongside behavior; do not optimize special-case count as the only score. [[sources/caldoai--skills#completion]]
24. Carry the decision log across context compaction so a new pass understands the design intent. [[sources/caldoai--skills#context-tools]]
25. Build a derived skeleton view for navigation, then return to bodies when behavior matters. Non-destructive generation is our implementation qualification. [[sources/caldoai--skills#context-tools]]
26. Summarize bounded areas while retaining links to source evidence and uncertainty. [[sources/caldoai--skills#context-tools]]
27. Regenerate dependency graphs as the architecture changes; stale diagrams should not judge new code. [[sources/caldoai--skills#context-tools]]
28. Use Git co-change/volatility history as a clue, accounting for missing history and batch commits rather than treating correlation as necessity. [[sources/caldoai--skills#context-tools]]
29. Enter high-leverage boundaries first, where one fix can remove multiple sources of coordinated work. [[sources/caldoai--skills#redesign]] [[sources/caldoai--skills#context-tools]]
30. Restore generic dialog lifecycle behavior instead of accumulating timing delays and global exception flags when that lifecycle really owns the problem. [[sources/caldoai--skills#dialog-example]]
31. Introduce a shared provider boundary when multiple actual integrations create repeated branching; avoid an abstraction justified only by imagined future providers. [[sources/caldoai--skills#provider-example]] [[sources/caldoai--skills#inventory]]
32. Use a canonical command definition for shared action surfaces, with consistent availability/undo semantics and per-consumer behavior tests. [[sources/caldoai--skills#command-example]]

## Tensions and adoption boundaries

- **Broad goal, subjective finish.** “Nothing worth fixing” can expand without a budget. The repo has no formal exhausted/blocked/stagnated states; pair adoption with a scoped change contract and explicit residual findings. [[sources/caldoai--skills#completion]] [[concepts/agentic-loop]]
- **Special cases can be legitimate.** Retries can encode unreliable transports; wrappers can enforce policy; comments can capture non-obvious invariants. Preserve the requirement and proof, not just a reduced count. The source itself says to keep necessary exceptions. [[sources/caldoai--skills#redesign]] [[sources/caldoai--skills#comments]]
- **Test reduction can weaken the safety net.** A test that resembles implementation can still catch a realistic regression. Test deletions need evidence for the lost assertion, and final green alone cannot establish behavioral equivalence. [[sources/caldoai--skills#tests]] [[sources/caldoai--skills#completion]]
- **Compression hides details.** Skeletons, summaries and import graphs omit dynamic loading, side effects and external contracts; revisit the source before concluding a link is absent. [[sources/caldoai--skills#context-tools]]
- **Intended behavior versus bug fixes.** The exception for incidental bug fixes makes an explicit behavior-delta ledger useful; otherwise a regression can be relabeled as cleanup. This is our adoption recommendation. [[sources/caldoai--skills#completion]]

## Evidence lifecycle and enforcement boundary

The prescribed lifecycle is observed problem → proposed grouped fix → implementation → repeated review → final behavior check. There is no machine-readable finding schema, enforced state transition, validator, reviewer-identity check or test baseline. All gates depend on the executing agent/host; marketplace packaging does not supply a refactor safety mechanism. [[sources/caldoai--skills#inventory]] [[sources/caldoai--skills#decision-log]] [[sources/caldoai--skills#completion]] [[sources/caldoai--skills#inventory-receipt]]

## Open questions / what's unclear

- Which representative changes demonstrate reduced reading, edit spread, defects or debug time after the refactor?
- How are high-risk boundaries, budgets and stop conditions chosen for a large repository?
- What baseline establishes intended behavior, and what evidence justifies deleting each test?
- How does the chosen host enforce invocation metadata and optional-scope decisions?
- Which skeleton/graph tools preserve the language's dynamic dependency semantics?

**Study result:** source-inspected and preserved, not installed or run. No application refactor, model benchmark or behavioral-equivalence test performed. The repository ships no executable test suite to run. [[sources/caldoai--skills#inventory-receipt]]
