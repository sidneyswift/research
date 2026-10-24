---
domain: meta
type: ledger
last-reviewed: 2026-06-02
---

# Self-Improvements Ledger

The output of the **REFLECT** operation (see [CLAUDE.md](../CLAUDE.md)). This wiki studies how to build great agents/skills — and it *is* one (the `CLAUDE.md` harness + `_schemas/` skills + operations routing + `index.md`/`log.md` memory). So every confirmed pattern is a candidate upgrade to our own machinery. This ledger keeps that loop honest: each entry traces a concrete wiki change back to a pattern **observed in this wiki** (never generic advice), so we can see *why* we work the way we do — and avoid re-proposing the same thing.

**Anti-rule:** no entry without a `[[patterns/...]]` or `[[concepts/...]]` citation. If you can't cite the learning, it's not a reflection — it's an opinion.

## Status legend

- `proposed` — recorded but not yet applied. Rare and transient: REFLECT normally applies grounded changes immediately (no human gate), so this status mostly appears mid-session.
- `applied` — change is live; links to where + the `log.md` entry.
- `embodied` — the pattern is already satisfied by existing structure; no change needed (still recorded so we don't re-propose it).
- `rejected` — considered and declined; keep the reasoning so we don't relitigate.

## Ledger

### [2026-06-01] Seed pass — reflecting the AI-Explainer patterns onto the wiki

A retroactive REFLECT over the patterns extracted from Garry Tan's essay series. They were catalogued but never applied to the wiki itself; this pass closes that gap. **All 6 applied 2026-06-02** (REFLECT ships grounded changes without asking — see `CLAUDE.md`).

| # | Learning (cited) | Wiki change | Status |
| --- | --- | --- | --- |
| 1 | [[patterns/composition/resolver-routing-table]] — a tested table mapping *intent → which skill/doc to load* | Added an explicit **Routing** table to `CLAUDE.md` Operations: *request → operation* and *source type → citation `type:` + raw-material location + page schema*. | **applied** 2026-06-02 (`CLAUDE.md` §Routing) |
| 2 | [[patterns/quality-bar/complexity-ratchet]] — every session adds tests/docs that reload into context, so quality only rises (forward-only) | Ingests now **ratchet**: INGEST closes with a `ratchet: links +N · orphans +0 · patterns +N` tally; LINT check #12 flags any ingest that added a page but no links, or stranded an orphan. | **applied** 2026-06-02 (`CLAUDE.md` INGEST + LINT #12) |
| 3 | [[patterns/behavioral/diarization]] — read everything about a subject, write *one* page of distilled judgment | Added a "this page is a **judgment distillation**, not a transcription" reminder to every artifact + concept schema header. | **applied** 2026-06-02 (`_schemas/{skill,plugin,mcp-server,concept}.md`) |
| 4 | [[patterns/behavioral/latent-vs-deterministic-split]] — every step is model-judgment (latent) or same-in/same-out (deterministic) | Tagged each INGEST step **(det)** or **(latent)** with a legend; det steps (clone, index row, log) are flagged as future-tooling candidates. | **applied** 2026-06-02 (`CLAUDE.md` INGEST) |
| 5 | [[patterns/structural/thin-harness-fat-skills]] — push intelligence up into markdown, execution down into code, keep the harness thin | Added LINT check #13 (**harness bloat**): flag detailed how-to that crept into `CLAUDE.md` and belongs in a `_schemas/` template. | **applied** 2026-06-02 (`CLAUDE.md` LINT #13) |
| 6 | [[patterns/quality-bar/skill-pack-bundle]] — a skill isn't done until it ships with tests/evals | Added a `## Detection recipe` section to `_schemas/pattern.md` (look-for / confirm-with / rule-out); the ≥2 examples are the positive fixtures, the counter-example the negative test. | **applied** 2026-06-02 (`_schemas/pattern.md`) |

### [2026-06-02] Pass 2 — the remaining confirmed/with-page patterns

REFLECT over the patterns not covered by the seed pass. Applied immediately (grounded → ships).

| # | Learning (cited) | Wiki change | Status |
| --- | --- | --- | --- |
| 7 | [[patterns/behavioral/skill-as-method-call]] — a skill file is a parameterized procedure; same file + different args → different capability | Documented each operation as a **parameterized call** in `CLAUDE.md` Routing (`INGEST(<source>)`, `QUERY(<question>)`, `LINT(<scope?>)`, `REFLECT(<since?>)`); noted that a `_schemas/` template is likewise a parameterized page. | **applied** 2026-06-02 (`CLAUDE.md` §Routing) |
| 8 | [[patterns/composition/single-source-multi-surface-distribution]] — one definition, many runtime surfaces | Added an anti-rule: wiki pages are the single source; `DASHBOARD.html`, query deliverables, and any future `llms.txt` are *surfaces* rendered from them, never parallel copies that drift. | **applied** 2026-06-02 (`CLAUDE.md` anti-rules) |
| 9 | [[patterns/structural/marketplace-as-multi-plugin]] — one manifest registers N à-la-carte units | No change: already embodied. `index.md` (+ per-domain `_index.md`) is exactly this registry — it lists every page as an independently-linkable unit. Recorded so we don't re-propose it. | **embodied** 2026-06-02 (`index.md`) |

### [2026-06-02] Pass 3 — deep review of the Garry Tan corpus

Mined the gstack/gbrain pages + all 8 essays (esp. #5 *Skillify Manifesto* and #6 *Meta-Meta-Prompting*, which credits Karpathy's LLM Wiki as gbrain's own origin). gbrain is our pattern realized with extras, so it's the richest mine. Small/safe items applied immediately; larger tooling items recorded as `proposed`.

**Applied this pass:**

| # | Learning (cited) | Wiki change | Status |
| --- | --- | --- | --- |
| 10 | [[patterns/composition/resolver-routing-table]] — "test the routing, not just the output" (gbrain ships `routing-eval.jsonl`) | Added a **Routing evals** table to `CLAUDE.md` (sample request → expected operation) so the resolver is spot-checkable, not just declared. | **applied** 2026-06-02 (`CLAUDE.md` §Routing) |
| 11 | [[patterns/behavioral/diarization]] — gbrain's "entity propagation": after ingest, walk every entity mentioned and update its page | INGEST step 5 now **propagates to every entity the source touches**, not just the creator — the real source of cross-link density. | **applied** 2026-06-02 (`CLAUDE.md` INGEST 5) |
| 12 | [[patterns/composition/resolver-routing-table]] — `check-resolvable` finds "dark" (unreachable) skills | LINT check #15: every routing request resolves to an operation, every schema is reachable from an operation, every page reachable from `index.md`. | **applied** 2026-06-02 (`CLAUDE.md` LINT #15) |
| 13 | [[patterns/composition/resolver-routing-table]] — gbrain's DRY audit catches duplicate/overlapping skills | LINT check #16: flag near-duplicate pages competing for the same role (distinct from contradictions). | **applied** 2026-06-02 (`CLAUDE.md` LINT #16) |
| 14 | [[patterns/quality-bar/complexity-ratchet]] — Garry's "search your history for where you said wtf" = the tests you're missing | LINT check #17: aggregate every `## Open questions` + `TODO` into one "what to chase next" backlog. | **applied** 2026-06-02 (`CLAUDE.md` LINT #17) |

**Proposed (bigger — genuine "could add" items):**

| # | Learning (cited) | Proposed change | Status |
| --- | --- | --- | --- |
| 15 | [[patterns/behavioral/diarization]] + [[artifacts/plugins/gbrain]] — brain-page schema: *compiled truth on top, append-only timeline below, raw sidecars* | Added a "compiled truth on top + append-only `## Timeline`" shape to `creator.md` and `concept.md` schemas; retrofitted [[creators/garry-tan]] with the star/essay time-series. | **applied** 2026-06-02 (`_schemas/{creator,concept}.md`, `creators/garry-tan.md`) |
| 16 | [[patterns/quality-bar/complexity-ratchet]] + [[artifacts/plugins/gbrain]] — "every page has a score"; 90% coverage as the AI-affordable bar | `scripts/wiki-doctor.py` computes a 0–100 **health score** (penalties for broken links, orphans, missing sections, staleness, gitlinks; target 90 per gbrain). | **applied** 2026-06-02 (`scripts/wiki-doctor.py`) |
| 17 | [[patterns/quality-bar/skill-pack-bundle]] — the 10-step skillify checklist; "a feature that doesn't pass all ten is not a skill" | Added `_schemas/_definition-of-done.md` (an underscore-prefixed shared-rules file, à la gbrain's `_brain-filing-rules.md`) with per-page-type checklists; every schema header now links to it. DRY — one gate, not copied six times. | **applied** 2026-06-02 (`_schemas/_definition-of-done.md` + all schemas) |
| 18 | [[artifacts/plugins/gbrain]] — vector+graph retrieval (97.6% recall on LongMemEval); Karpathy's optional `qmd` search tool | `scripts/wiki-search.sh` — grep over the git-tracked pages (auto-excludes ignored clones), grouped by page + title. The cheap first cut; embeddings/`qmd` later if it outgrows grep. | **applied** 2026-06-02 (`scripts/wiki-search.sh`) |
| 19 | [[patterns/quality-bar/skill-pack-bundle]] + [[artifacts/plugins/gbrain]] — `gbrain doctor --remediate --target-score 90 --max-usd 5` + the `[AGENT]` cost banner | `scripts/wiki-doctor.py` is the LINT autopilot: runs the deterministic checks + health score, `--strict` for CI. Deliberately **report-only** (no silent prose edits — a doctor that rewrites pages is a Foxconn cage); remediation stays a reviewed REFLECT/LINT step. | **applied** 2026-06-02 (`scripts/wiki-doctor.py`) |
| 20 | [[artifacts/plugins/gbrain]] — cross-modal eval (multiple models score each other) caught book-mirror's factual errors | Added `analyses/_eval-rubric.md`: a 5-dimension rubric + procedure to run every `analyses/` draft past 2–3 judge models from different families before it ships. | **applied** 2026-06-02 (`analyses/_eval-rubric.md`) |
| 21 | [[patterns/composition/resolver-routing-table]] + [[patterns/quality-bar/skill-pack-bundle]] — "skills that build skills" (skillify is a meta-skill) | Named **skillify** as a reflex inside REFLECT: a *repetition* trigger (3rd time you do an ad-hoc move → codify it as a schema/operation/Routing row/`(det)` script with a definition of done). | **applied** 2026-06-02 (`CLAUDE.md` REFLECT) |

### [2026-06-02] Pass 4 — the completion-contract lens (OpenAI Codex Goals ingest)

REFLECT over the [[sources/openai--using-goals-in-codex|Codex Goals]] ingest, which produced [[concepts/completion-contract]] + the proposed [[patterns/behavioral/evidence-gated-completion]] — both about *how a task declares itself done*, which is exactly what our page-level "definition of done" governs. The first non-Garry, non-Anthropic source to land on our own machinery.

| # | Learning (cited) | Wiki change | Status |
| --- | --- | --- | --- |
| 22 | [[concepts/completion-contract]] / [[patterns/behavioral/evidence-gated-completion]] — a completion contract must name a **blocked stop condition** (if you can't finish honestly: stop, mark the gap, report what would unlock it, never fake done); budget-exhaustion ≠ done | `_schemas/_definition-of-done.md` was a purely *positive* checklist (what must be present) with no "blocked" path — so a half-finished page had no defined honest exit. Added an **"If blocked"** section: mark the gap inline + in `## Open questions` + log why; "done" is checked (LINT/`wiki-doctor`), not self-assessed; out of budget ≠ done. | **applied** 2026-06-02 (`_schemas/_definition-of-done.md`) |
| 23 | [[patterns/behavioral/evidence-gated-completion]] — "done" is decided by an external assertable surface, not self-assessment | No change: already embodied. `scripts/wiki-doctor.py` *is* the deterministic verification surface for a page's done-ness (a page passes when the doctor is clean). Recorded so we don't re-propose it — and noted in the new "If blocked" clause so the link is explicit. | **embodied** 2026-06-02 (`scripts/wiki-doctor.py`) |
| 24 | [[concepts/completion-contract]] — preserve epistemic levels (confirmed / approximate / blocked / uncertain), never flatten to one success claim | No change: already embodied across the wiki's hedging conventions — claims marked *asserted vs. demonstrated*, `status:` fields, `proposed`-vs-`confirmed` patterns, `as-of` signal dating. The Codex research case study is external corroboration of a discipline we already run. | **embodied** 2026-06-02 |

Cross-check (not a new change): [[patterns/behavioral/skill-as-method-call]], promoted to confirmed this ingest, validates ledger **#7**'s "operations are parameterized calls" framing from a *second creator* — our `INGEST(<source>)` / `QUERY(<question>)` operations are method-calls, now cross-confirmed against Codex's `/goal <contract>` (a documented six-slot signature). #7 stays `applied`; this just retires its single-creator caveat.

### [2026-06-02] Pass 5 — the compound-engineering ingest

REFLECT over the [[artifacts/plugins/compound-engineering]] ingest (Every / Kieran Klaassen) — the first non-Garry tested skill pack, whose `/ce-compound` skill *is* a knowledge-compounding mechanism much like this wiki's own INGEST→log→ratchet loop. The richest mine for self-application since gbrain.

| # | Learning (cited) | Wiki change | Status |
| --- | --- | --- | --- |
| 25 | [[patterns/quality-bar/complexity-ratchet]] via `compound-engineering`'s `/ce-compound` — score overlap on **5 dimensions before writing**; high overlap → *update* the existing doc, don't create a duplicate ("two docs on the same problem will inevitably drift apart") | We had LINT #16 (DRY/overlap audit) but only *after the fact*. Added a **dedup-before-create** guard to INGEST step 3: score a candidate page against existing ones (subject + mechanism + role) and extend rather than duplicate. The pre-creation twin of #16 — cheaper to never make the duplicate. | **applied** 2026-06-02 (`CLAUDE.md` INGEST 3) |
| 26 | [[patterns/behavioral/latent-vs-deterministic-split]] via CE's `AGENTS.md` — "skills are guardrails for an intelligent agent, not a controller for a dumb one; **calibrate prescription level to the failure mode**" (hard rules for deterministic safety, trust for judgment) | No change: already embodied. The `(det)`/`(latent)` step tagging (ledger #4) + the hard anti-rules vs. latent judgment steps already calibrate how prescriptive `CLAUDE.md` is per step. Recorded so we don't re-propose it; CE is external corroboration of the discipline. | **embodied** 2026-06-02 (`CLAUDE.md` INGEST legend + anti-rules) |
| 27 | `compound-engineering`'s `/ce-compound` Discoverability Check — "the knowledge store only compounds value when agents can *find* it"; edit the instruction file so a fresh agent discovers the store | No change: already embodied. `index.md` is the mandated front door (INGEST step 7 + LINT #15 reachability: every page reachable from `index.md`). The Discoverability Check is exactly what step 7 + #15 enforce. | **embodied** 2026-06-02 (`index.md`, LINT #15) |

Cross-check (not a new change): this ingest promoted [[patterns/quality-bar/complexity-ratchet]] proposed→confirmed and **retired the same-creator caveat** on [[patterns/quality-bar/skill-pack-bundle]] + [[patterns/behavioral/latent-vs-deterministic-split]] (CE = the non-Garry witness). Those are pattern-page changes, not machinery changes — but they harden the *grounding* of ledger #2/#5/#6, which cited those very patterns to justify the ratchet/harness-bloat/detection-recipe machinery. Our own machinery now rests on cross-creator-confirmed patterns, not one author's house style.

### [2026-06-02] Pass 6 — portable skills, release gates, and compounding budget

REFLECT over the newest wiki learnings after the OpenAI Plugins ingest and this LINT pass: [[concepts/convergent-agent-plugin-spec]], the run-natively variant of [[patterns/composition/single-source-multi-surface-distribution]], [[patterns/quality-bar/version-as-update-gate]], and [[concepts/compound-engineering]]. The pass adds principles for future skillification and fixes stale front-door prose found during review.

| # | Learning (cited) | Wiki change | Status |
| --- | --- | --- | --- |
| 28 | [[concepts/convergent-agent-plugin-spec]] + [[patterns/composition/single-source-multi-surface-distribution]] — skills/plugins now have a shared cross-lab core; the cheapest multi-surface distribution is "run natively" when the artifact stays inside that core | Added a REFLECT rule: when skillifying a repeated move for reuse outside this wiki, prefer the lab-agnostic `SKILL.md` core (`name`, "Use when…" `description`, body, `references/`, `scripts/`) and isolate platform-specific hooks/connectors/env vars. Also extended `for-builders.md` so skill/plugin builders read the convergence concept up front. | **applied** 2026-06-02 (`CLAUDE.md`, `for-builders.md`) |
| 29 | [[patterns/quality-bar/version-as-update-gate]] — for installable artifacts, `version` is the update-delivery trigger, so human hand-bumps cause delivery drift | Added a future-facing anti-rule: if this wiki ever emits an installable skill/plugin/marketplace package, do **not** hand-bump versions; require release automation plus drift/parity validation before treating it as distributable. | **applied** 2026-06-02 (`CLAUDE.md`) |
| 30 | [[concepts/compound-engineering]] + [[patterns/quality-bar/complexity-ratchet]] — each unit of work should make the next one easier; the 50/50 rule protects system-building from being crowded out by feature/page accumulation | Added a REFLECT budget check: after ingest/lint batches, explicitly ask whether the next highest-leverage move is a schema, script, routing row, skill, or principle rather than another page; if not, log why no compounding improvement was made. | **applied** 2026-06-02 (`CLAUDE.md`) |
| 31 | [[patterns/quality-bar/complexity-ratchet]] — stale front doors lower the next agent's floor because the next session loads the wrong map | Fixed stale front-door prose found in this review: `README.md` now names all four operations, and `index.md`'s Meta row reflects the current ledger instead of the original seed count. | **applied** 2026-06-02 (`README.md`, `index.md`) |

### [2026-06-02] Pass 7 — schema-level reflections from the openai/plugins ingest

The INGEST step-9 quick pass for [[sources/openai--plugins]], reconciled with the concurrent Pass 6 above (which handled the `CLAUDE.md` skillify-to-the-cross-lab-core rule, the version-gate anti-rule, the compounding-budget check, and the `for-builders.md` extension). This pass records the distinct **schema-level** changes that ingest forced — the first time a second lab tested an assumption baked into our own `_schemas/`.

| # | Learning (cited) | Wiki change | Status |
| --- | --- | --- | --- |
| 32 | [[concepts/convergent-agent-plugin-spec]] — OpenAI Codex ships a near-identical plugin spec, so "plugins are a Claude Code thing" is now false | `_schemas/plugin.md`'s `ecosystem:` field literally read *"plugins are Claude Code only as of 2026"* — a stale assumption the ingest falsified. Updated to `claude-code \| codex \| cross-lab` with a pointer to the concept, so future plugin pages classify by lab instead of silently defaulting to Claude Code. | **applied** 2026-06-02 (`_schemas/plugin.md`) |
| 33 | [[concepts/convergent-agent-plugin-spec]] — both labs auto-discover the same component set (skills/commands/agents/hooks/mcp) | No change: already embodied. Our `_schemas/plugin.md` `components:` block *is* the cross-lab shared shape — the second lab validates the schema we already use, so no "Codex-specific schema" is warranted. Divergent surfaces (`.app.json` hosted connectors, the productized storefront) are captured in page prose, not new required fields. Recorded so we don't re-propose a schema fork. | **embodied** 2026-06-02 (`_schemas/plugin.md`) |
| 34 | [[patterns/quality-bar/skill-pack-bundle]] via `plugin-eval` ([[sources/openai--plugins#plugin-eval]]) — an evaluator that not only *scores* a pack but explains *why* and says *what to fix first*, under explicit **token-budget** accounting | `scripts/wiki-doctor.py` (ledger #16/#19) computes a health score and lists findings but does not **prioritize** them ("fix-first" ordering) or estimate remediation cost. Candidate enhancement: a ranked "fix these first" ordering + a rough effort note. **Held `proposed`, not applied** — it should be grounded in `plugin-eval`'s actual rubric (`references/{benchmark-harness,metric-pack-manifest,evaluation-result-schema}.md`, a bounded QUERY) before changing the LINT autopilot. Don't port a rubric we haven't read. | **proposed** 2026-06-02 (next: QUERY `plugin-eval` references → `scripts/wiki-doctor.py`) |

Cross-check (not a new change): this ingest made [[patterns/structural/marketplace-as-multi-plugin]] **cross-lab** (3rd example, first non-Claude-Code) and added a 3rd-creator witness to [[patterns/structural/thin-harness-fat-skills]]'s fat-skills half — hardening the grounding of ledger **#5** (harness-bloat check) and **#9** (index-as-marketplace). Our machinery now rests on cross-*lab*-confirmed patterns. Still un-ingested: a real harness *loop* (the thin-harness middle) — now *named* (Codex) but not inspected.

### [2026-06-04] Pass 8 — the convergent core is now a formal standard

The INGEST step-9 quick pass for the OpenAI skills-distribution sources ([[sources/agentskills--specification]], [[sources/openai--codex-skills-doc]], [[sources/openai--chatgpt-skills-help]]).

| # | Learning (cited) | Wiki change | Status |
| --- | --- | --- | --- |
| 35 | [[sources/agentskills--specification#governance]] + [[sources/openai--codex-skills-doc#open-standard]] — the "convergent agent-plugin core" our skillify-for-reuse rule (ledger #28) targets is no longer informal convergence: it's the **Agent Skills open standard** (agentskills.io, AAIF/Linux Foundation, 40+ clients, `skills-ref` validator) | Updated `CLAUDE.md`'s "When skillifying for external reuse" rule: author to the named standard, validate with `skills-ref`, and ship per-harness placement notes because **discovery paths aren't standardized** (`.agents/skills` vs `.claude/skills` — a portability gap the old rule didn't know about, per [[concepts/workspace-skill-distribution]]) | **applied** 2026-06-04 (`CLAUDE.md`) |
| 36 | [[concepts/workspace-skill-distribution]] — the restrictive/additive split: enforcement pipes only subtract, content pipes only add | No machinery change yet: the wiki has no enforcement pipe (it's all content). Recorded as a design invariant to honor if we ever add managed config to wiki tooling: never make a policy mechanism able to inject behavior. | **embodied** 2026-06-04 (note only) |

Compounding budget check (ledger #30): this ingest's system improvement is the #35 `CLAUDE.md` rule hardening; no new schema/script warranted — the 3 sources fit existing `docs-page` machinery cleanly. The secondary-fidelity capture of help.openai.com exposed a tooling gap (no browser-based snapshot path for Cloudflare-gated pages) — noted as a future `(det)` tooling candidate rather than built now (1st occurrence; skillify on the 3rd).

### [2026-06-11] Pass 9 — reflections from the pm-os ingest

The INGEST step-9 quick pass for [[sources/prodmgmt-world--pm-os-cowork]] (the wiki's first paid, ZIP-distributed, private-upstream source).

| # | Learning (cited) | Wiki change | Status |
| --- | --- | --- | --- |
| 37 | The ingest itself hit a routing gap: a packaged release (paid ZIP, no clonable upstream) fit neither the repo row (no git) nor the article row (not a page). Per [[patterns/composition/resolver-routing-table]] applied to ourselves — an unroutable source type is a "dark" capability | Added a **Packaged release** row to `CLAUDE.md`'s source-type table + a step-1 branch (commit the extracted tree like an article; version stamp = package version, not SHA), and a "Release artifacts" section to `sources/_index.md` | **applied** 2026-06-11 (`CLAUDE.md`, `sources/_index.md`) |
| 38 | [[patterns/behavioral/session-start-directive]] (pm-os) — passive hook/context phrasing gets silently absorbed; imperative, position-pinned, persistence-bounded directives survive | Recorded as a design rule for any future wiki automation that injects session context (e.g. a future hook reminding "run LINT — N ingests since last"): phrase it as a directive with a no-loop bound, never as passive context. No machinery to change yet (the wiki ships no hooks). | **embodied** 2026-06-11 (note only) |
| 39 | [[artifacts/plugins/pm-os]]'s count drift (manifest says 237/10, disk says 235/12) *despite* stated release gates — gates that don't run on the distribution build protect the dev repo, not the shipped artifact (per [[patterns/quality-bar/version-as-update-gate]]) | Sharpens ledger #28/#29: if this wiki ever emits an installable package, the drift/parity check must run **on the packaged output**, not the source tree. Recorded as a constraint on the future release path. | **embodied** 2026-06-11 (note only) |

Compounding budget check (ledger #30): this ingest's system improvement is the #37 routing-table row — a true routing fix, not page accumulation. Also worth noting: pm-os's per-agent I/O contract (Inputs / Allowed reads / Writes / Output format / Failure behavior) is a candidate shape for any future wiki subagent definitions; 1st sighting, skillify on recurrence.

### [2026-06-19] Pass 10 — reflections from the mattpocock/skills ingest

The INGEST step-9 quick pass for [[sources/mattpocock--skills]] — the wiki's first individual-engineer pack, and unusually rich in *self-applicable* skill-craft (its [[artifacts/skills/writing-great-skills]] is a manual for the exact artifacts this wiki is made of).

| # | Learning (cited) | Wiki change | Status |
| --- | --- | --- | --- |
| 40 | [[artifacts/skills/writing-great-skills]] — the **no-op test** (read each sentence in isolation; if the model already obeys it by default, delete the *whole sentence*) + **leading words** (collapse a restated idea into one pretrained token instead of a sentence) | LINT #13 (harness bloat) flagged *where* bloat lives but not *how* to cut it. Added the no-op test + leading-word collapse as the concrete cutting technique to LINT #13. | **applied** 2026-06-19 (`CLAUDE.md` LINT #13) |
| 41 | [[artifacts/skills/writing-great-skills]] — a **completion criterion** must be *checkable* and *exhaustive* ("every modified model accounted for", not "produce a change list") or you get **premature completion** | No change: already embodied. `_schemas/_definition-of-done.md` + the (det)/(latent) step tagging + INGEST step 5 ("propagate to *every* entity the source touches") already demand exhaustive, checkable completion. Recorded so we don't re-propose it, and **named the failure** ("premature completion") so LINT can call it by name — e.g. an ingest that cross-links *some* but not *every* touched entity. | **embodied** 2026-06-19 (note only) |
| 42 | [[concepts/skill-invocation-axis]] — user-invoked skills are unreachable by the model; piled cognitive load is cured by a **router skill**, and a forgotten user-invoked skill is a *dead* skill | No change: already embodied. `index.md` (master catalog) and `for-builders.md` (consumer front door) *are* the wiki's human-facing routers over pages the auto-context can't load — the "user-invoked router" role exactly. Recorded as a design invariant: keep the router current or a page goes dark (the human-side twin of the resolver essay's "invisible skill", per [[patterns/composition/resolver-routing-table]]). | **embodied** 2026-06-19 (note only) |

Compounding budget check (ledger #30): this ingest's system improvement is the **#40 LINT #13 sharpening** — a real harness check grounded in a freshly-ingested artifact, not page accumulation. Noted for a future pass: `writing-great-skills`' full vocabulary (the information-hierarchy ladder, sediment/sprawl/duplication, granularity-by-invocation/by-sequence) is a candidate lens for a deeper LINT of `CLAUDE.md` + the `_schemas/` themselves — deferred (1st deep articulation in-wiki; revisit if a 2nd skill-craft source lands).

### [2026-06-20] Pass 11 — reflections from the loop-library ingest

The INGEST step-9 quick pass for [[sources/forward-future--loop-library]] — a source whose entire subject (the bounded agent loop with named terminal states) is self-applicable, since this wiki's four operations *are* loops over its own content.

| # | Learning (cited) | Wiki change | Status |
| --- | --- | --- | --- |
| 43 | [[artifacts/skills/loop-library]]'s **six named terminal states** (success / clean no-op / blocked / approval-required / exhausted / **stagnated**) + the rule "use a no-progress stop instead of inventing a time/iteration/cost limit" ([[sources/forward-future--loop-library#skill-terminal-states]]) — richer than the wiki's existing blocked/exhausted pair | `_schemas/_definition-of-done.md`'s "If blocked" section knew *blocked* and *out-of-budget* but conflated "found nothing" with failure and had no *stagnated* state. Added the named-terminal-state checklist item (incl. **clean no-op** = a lint/page that genuinely needed nothing is a *success*, and **stagnated** = stop a fruitless re-pass instead of looping) — the per-page twin of [[patterns/behavioral/evidence-gated-completion]]. | **applied** 2026-06-20 (`_schemas/_definition-of-done.md`) |
| 44 | The Loop Library confirms [[patterns/behavioral/evidence-gated-completion]] as a **cross-creator** pattern (OpenAI + Forward Future), and the wiki's own LINT/`wiki-doctor.py` is exactly an evidence gate ("a page passes when a doctor pass is clean — not because it *reads* finished") | No change: already embodied. Recorded so the pattern's promotion is traceable, and the wiki's self-application (doctor-as-verification-surface) is named as a worked instance of the now-confirmed pattern. | **embodied** 2026-06-20 (note only) |
| 45 | The Loop Library's anti-pattern: "Recommend a one-shot workflow instead of manufacturing a loop when no new feedback can change the next action" ([[sources/forward-future--loop-library#skill-feedback-cycle]]) | Recorded as a check on REFLECT itself: don't manufacture a machinery change when no observed pattern would change it — the ledger's own grounding rule ("no improvements from generic knowledge") is the same instinct. No edit. | **embodied** 2026-06-20 (note only) |

Compounding budget check (ledger #30): this ingest's system improvement is **#43** — a real `_definition-of-done` sharpening (the named terminal states), grounded in a freshly-ingested artifact, not page accumulation. No new schema/script: the source fit existing `repo` machinery cleanly. Candidate for a future pass — the generator–verifier separation seen across four loops could, with a 2nd in-wiki artifact, become a pattern the wiki applies to its *own* persona-reviewer machinery.

### [2026-06-20] Pass 12 — reflections from the eve ingest (the first ingested *harness*)

The INGEST step-9 quick pass for [[sources/vercel--eve]] — uniquely self-applicable, because eve is the wiki's **first ingested harness** and this wiki *is* one: `CLAUDE.md` is its harness, the `_schemas/` its skills, the four operations its loop, `index.md`/`log.md` its memory. A pattern about how a great harness is built is, here, almost always a pattern about our own machinery.

| # | Learning (cited) | Wiki change | Status |
| --- | --- | --- | --- |
| 46 | [[concepts/filesystem-first-agent-framework]] — **identity comes from the path; there is no separate registry to keep in sync** ([[sources/vercel--eve#docs-project-layout]]). The wiki's `index.md` *is* a hand-maintained registry that can drift from the actual page tree — exactly the drift eve designs away by *discovering* the tree. | Recorded as a concrete `(det)` tooling candidate: a `scripts/build-index.*` that *derives* `index.md` rows from page frontmatter (the wiki's "discovery"), making the master catalog a rendered surface ([[patterns/composition/single-source-multi-surface-distribution]]) rather than a parallel copy. Not built now (1st framework source; `wiki-doctor.py` #2 orphans + #15 reachability already *guard* the drift). Build it if index drift recurs or a 2nd discovery-based source lands. | **proposed** 2026-06-20 |
| 47 | eve **refutes the literal "thin" harness** — a production harness accretes into a full framework (durability, compaction, channels), not "~200 lines" ([[sources/vercel--eve#docs-default-harness]], per the reframed [[patterns/structural/thin-harness-fat-skills]]). `CLAUDE.md` is our harness, and it has likewise accreted (operations + routing + anti-rules + a 17-item LINT checklist). | No new machinery: this *sharpens the lens* on the existing LINT #13 (harness bloat). The eve finding gives the honest frame — harnesses fatten under real use, so #13 isn't "keep `CLAUDE.md` at 200 lines," it's "every accretion must be *operations/routing*, justified, and no-op-pruned" (the #40 cutting technique). Recorded so #13 is read as *justified-fat*, not *thin-at-all-costs*. | **embodied** 2026-06-20 (note only) |
| 48 | eve ships its **docs inside the package** + a pointer `SKILL.md` ("read the bundled docs, don't trust me"), and `docs:check` **validates the code snippets inside the docs** ([[sources/vercel--eve#README]], [[sources/vercel--eve#docs-check]]). | No change: already embodied, with one named gap. The wiki is already single-source (pages) with rendered surfaces, and `wiki-doctor.py` is the `docs:check` analogue — but it checks links/sections, **not whether cited source anchors still exist in the source's `## Anchor map`** (the wiki's version of "snippets that can rot"). Recorded as the highest-value future `wiki-doctor` check: *anchor-validity* (every `[[sources/x#anchor]]` resolves to a registered anchor) — the exact rot eve's snippet-check prevents. | **embodied** 2026-06-20 (note + named future check) |

Compounding budget check (ledger #30): the highest-leverage next move surfaced here is **#48's anchor-validity check** for `wiki-doctor.py` (mechanizes LINT #1's "links to source anchors that aren't in the Anchor map are *de facto* broken") and **#46's derive-index-from-frontmatter** script — both are *discovery/verification* tooling (eve's two strengths) rather than more pages. Neither built this pass (kept the ingest focused; both are real candidates, not page accumulation). Recorded so the next REFLECT/LINT picks them up.

### [2026-07-22] Pass 13 — reflections from the skill-diffs ingest

The INGEST step-9 quick pass for [[sources/SHL0MS--skill-diffs]] — a source that studies, empirically, how a corpus of maintained artifacts should be validated, which is exactly the question this wiki's own LINT operation answers for itself.

| # | Learning (cited) | Wiki change | Status |
| --- | --- | --- | --- |
| 49 | [[patterns/quality-bar/defect-derived-validation]] — `skill_linter.py`'s rules are mined from what real maintainers actually fixed in merged commits, then *validated* by running the rule set back over the corpus and reporting hit rates ([[sources/SHL0MS--skill-diffs#skill_linter]]) — a different origin than `wiki-doctor.py`'s checklist, which was authored from generic reasoning about wiki hygiene (Karpathy's pattern + our own judgment), never mined from this wiki's *own* historical defects | Added **LINT #18** to `CLAUDE.md`: periodically mine `log.md`'s ratchet tallies and ingest-time corrections (broken citations, drift findings, orphans caught late) for recurring defect classes; if the same class recurs across ≥2 ingests, propose it as a new mechanical check in `wiki-doctor.py` rather than relying on the original checklist indefinitely. The wiki's own defect-derived-validation loop. | **applied** 2026-07-22 (`CLAUDE.md` LINT #18) |
| 50 | Hermes Agent's **Curator** feature (referenced, unstudied — [[sources/SHL0MS--skill-diffs#root]]'s named downstream consumer) is "a background maintenance pass for agent-created skills" that tracks usage and moves skills active→stale→archived, consolidating overlaps — independently arrived at, in a different ecosystem, at the exact discipline this wiki's own LINT operation (orphan pages #2, DRY/overlap audit #16) performs on wiki pages | No change: already embodied. Recorded as third-party validation that "a periodic maintenance pass with named lifecycle states, run over a corpus of agent-authored artifacts" is a real, independently-converged-on discipline — not an idiosyncratic choice of this wiki's design. Strengthens confidence in LINT's shape rather than changing it. | **embodied** 2026-07-22 (note only) |
| 51 | [[concepts/imitation-vs-correctness-eval]] — when your reference/gold isn't guaranteed correct, split the eval into imitation (matches the accepted distribution) vs. correctness (an independent, gold-free signal) ([[sources/SHL0MS--skill-diffs#gold-caveat]]) | No change: already embodied. QUERY step 4 ("verify before recommending... confirm the cited source still says what we claimed") is this wiki's existing correctness check — it never lets "the wiki page says X" (imitation of our own prior claim) substitute for "the source still says X" (independent verification). Recorded so the parallel is traceable; the discipline predates this source. | **embodied** 2026-07-22 (note only) |

Compounding budget check (ledger #30): this ingest's system improvement is **#49** — a real LINT-checklist addition (mine our own historical defects, not just generic hygiene reasoning) grounded in a freshly-ingested, self-applicable pattern, not page accumulation. The source's low popularity signal (0★, 75 HF downloads/month) didn't reduce the machinery payoff — a reminder that this ledger's grounding bar is pattern quality, not source traction.

### [2026-10-23] Pass 14 — evidence classes and guarantee scope

| # | Learning (cited) | Wiki change | Status |
| --- | --- | --- | --- |
| 52 | [[patterns/behavioral/evidence-gated-completion]] and [[patterns/behavioral/latent-vs-deterministic-split]] applied to the HumanLayer investigation: prompt review gates are not runtime ACLs; an append-idempotent event log is not atomic external execution; a model-matrix label need not vary the actual invocation ([[sources/humanlayer--humanlayer#permissions]], [[sources/humanlayer--humanlayer#runtime-boundary]], [[sources/humanlayer--humanlayer#eval-pipeline]]) | Added [[_schemas/project]], the previously missing project template, and routed `artifacts/projects/_index.md` to it. Load-bearing claims must name evidence class, guarantee scope, and material code/docs conflicts. Keeps the core harness unchanged while making future project investigations harder to overstate. | **applied** 2026-10-23; uncommitted research update |

Compounding budget check: this ingest adds a reusable project schema, not only pages. The source-anchor validator remains a candidate for permanent tooling; this pass checks the new source map mechanically without silently changing the existing doctor's scope.

## Open meta-questions

- ~~Should REFLECT run automatically every N ingests, or only on demand?~~ **Resolved 2026-06-02:** REFLECT applies grounded changes directly (no human gate); the lightweight INGEST step-9 nudge runs every ingest, and a deeper pass runs on demand / after lint.
- Is `meta/` itself in scope for LINT's orphan/staleness checks? (Yes — it's a wiki page like any other.)
