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

## Pstack — 2026-10-24

| # | Source-grounded learning | Applied change | Status |
| --- | --- | --- | --- |
| 53 | [[patterns/quality-bar/rerunnable-work-artifact]] and pstack's negative-fixture discipline ([[sources/cursor--plugins-pstack#PP03]], [[sources/cursor--plugins-pstack#PK18]], [[sources/cursor--plugins-pstack#packaging-negative-probe]]) apply to repeated manual source-map checking, already identified in entries 47–48 and the HumanLayer ingest. | Added dependency-free `scripts/check-source-citations.py`, eleven fixture tests, source-schema instructions, and a thin tooling route. Checks anchor membership, repository/revision pinning, blob existence, and line bounds using immutable Git objects. Explicitly excludes semantic entailment and unsupported historical map formats. | **applied** 2026-10-24; fixture tests pass; ingest-specific runs recorded in log. |

## Open meta-questions

- ~~Should REFLECT run automatically every N ingests, or only on demand?~~ **Resolved 2026-06-02:** REFLECT applies grounded changes directly (no human gate); the lightweight INGEST step-9 nudge runs every ingest, and a deeper pass runs on demand / after lint.
- Is `meta/` itself in scope for LINT's orphan/staleness checks? (Yes — it's a wiki page like any other.)

## [2026-11-02] Pass 16 — context and authority boundaries

| # | Source-grounded learning | Applied change | Status |
| --- | --- | --- | --- |
| 54 | [[patterns/behavioral/context-is-not-authority]]: DeepSeek subscriptions deliver context without new Mandates; Kody derives enabled actor/credential authority outside generated code. Admission, OS authority and permitted credential use have different guarantees. | Added a context → authority → enforcement → revalidation/recovery map prompt to [[_schemas/project]]. Applied it to both new project studies; retained existing evidence-class requirements and thin harness. | **applied** 2026-11-02; local research update |

Compounding budget: a reusable schema check plus builder routing ships with the research. No new background agent or external service is needed to apply it.

### [2026-11-02] Internal projects as a separate research surface

- Grounding: [[patterns/composition/single-source-multi-surface-distribution]] and [[concepts/imitation-vs-correctness-eval]].
- Change: created [[projects/_index]] and the linked [[projects/conversation-learning/README]] design with [[projects/conversation-learning/data-contract]] and [[projects/conversation-learning/review-protocol]]. One evidence base supplies future derived views, while annotations distinguish acceptance from correctness.
- Expected benefit: preserve the wiki's external artifact catalog while making research-to-build work reachable; avoid maintaining separate incompatible datasets per training consumer.
- Status: **applied** 2026-11-02, local design/navigation only. Corpus ingestion, export adapters and evaluation results remain future work. No global conversation-collection rule or new confirmed pattern added.

### [2026-11-02] Real conversation evidence sharpens the annotation machinery

- Grounding: [[patterns/quality-bar/defect-derived-validation]], [[patterns/quality-bar/revision-bound-review]], [[patterns/behavioral/latent-vs-deterministic-split]]; observed evidence at [[sources/codex--commercial-redline-pilot#artifact-state]], [[sources/codex--commercial-redline-pilot#commitment-evolution]] and [[sources/codex--commercial-redline-pilot#execution-status]].
- Applied: [[projects/conversation-learning/data-contract]] and [[projects/conversation-learning/review-protocol]] now require capture-projection boundaries, repair-verification classes, prior-approval/intent-evolution checks, paired-artifact/process findings and development-only treatment of studied cases. Added `scripts/check-conversation-learning.py` for record envelopes, lineage and source-anchor checks.
- Expected benefit: prevent partial source capture, user reconsideration and agent-reported recovery from turning into falsely certain training labels; spend model judgment on interpretation rather than ID bookkeeping.
- Status: **applied** 2026-11-02 locally. Model behavior improvement, actual export authorization and full private-corpus storage remain unimplemented/unverified. Lessons are not installed as instructions in other projects.

### [2026-11-02] Accessible-chat corpus — provenance and executable review integrity

- Grounding: [[patterns/quality-bar/defect-derived-validation]], [[patterns/quality-bar/revision-bound-review]], [[patterns/behavioral/latent-vs-deterministic-split]] and [[patterns/composition/single-source-multi-surface-distribution]]; observed failure mechanisms at [[sources/codex--conversation-corpus-20261102#C0136]] and [[sources/codex--conversation-corpus-20261102#C0221]].
- Applied: read-only private capture, exact repeated-instruction factoring, per-chat review recording, validated shard consolidation, canonical-ledger-derived views and a completion/lineage checker. The contract now preserves feedback authorship, executed-prompt bindings, independent grading axes, cost attribution and unresolved contradictions. Tests reject duplicated coverage, uninspected user-facing tool payloads, numeric triage counts as annotations and dropped restrictions. Final review exposed a recorder that silently discarded optional annotations; it now preserves typed supported fields and rejects unknown fields, with regression coverage.
- Expected benefit: mechanical checks guard coverage and provenance while interpretation remains explicit model judgment. A polished catalog cannot turn source-agent assertions into human approval or measured improvement.
- Status: **applied** 2026-11-02 locally. Frozen run: [[projects/conversation-learning/runs/all-chats-20261102/README]]. No global agent rules, public corpus release, model training or executed behavior evaluation.

Compounding budget: this batch ships reusable capture/review/validation machinery and deterministic views, rather than promoting unadjudicated lessons into more confirmed patterns.

### [2026-11-02] Code Mode ingest — selective emission already embodied

- **Grounding:** [[patterns/behavioral/latent-vs-deterministic-split]], extended by [[sources/philschmid--code-mode#typed-interface]].
- **Mapping:** combine independent mechanical research checks in code and return bounded results; keep semantic evidence assessment with the model. Existing exec orchestration and doctor/citation scripts already support this.
- **Status:** embodied, 2026-11-02. Applied during this ingest; no new harness rule or script. A single article capture does not justify a new abstraction or a global migration. Next useful work is primary implementation/benchmark verification, not another overlapping concept page.

### [2026-11-04] API boundaries applied to wiki operations

- **Grounding:** [[concepts/business-platform-api-design]], [[patterns/composition/resolver-routing-table]], [[patterns/quality-bar/complexity-ratchet]].
- **Mapping:** QUERY is retrieval plus durable gap filing; INGEST is the explicit evidence-changing operation. The existing routing already names these separate responsibilities; source snapshots are evidence, not editable analysis.
- **Disposition:** **embodied**. No new operation, generic API-review template, or duplicate schema added: one research session does not establish a repeated wiki procedure. Current contracts remain adequate; links into existing lifecycle and vocabulary pages provide reuse.
- **Expected benefit:** retain a small discoverable interface and avoid adding machinery without observed repetition.

### [2026-11-04] Skillify repeated API contract investigations

- **Grounding:** [[patterns/quality-bar/defect-derived-validation]], [[patterns/composition/single-source-multi-surface-distribution]], and the nine documentation case studies in [[analyses/frontier-and-business-api-design]].
- **Observed repetition/defects:** repeated vendor comparisons needed the same contract dimensions; a first Gusto extraction omitted its introductory effect contract, static SAP retrieval returned a shell, and job/idle/envelope labels could overstate completion. These are ingestion/review hazards, not measured provider defects.
- **Change:** added [[_schemas/api-case-study]] with a matrix, collection/supplement capture rules, and a definition of done; registered its source route in AGENTS.md and its existing CLAUDE.md mirror and linked the project template and hub.
- **Status:** **applied**, 2026-11-04, local uncommitted wiki changes. No installable package/version or live integration changed.
- **Expected benefit:** subsequent systems use one comparable evidence contract; source extraction and guarantee gaps stay explicit. No new confirmed pattern inferred from documentation agreement.

### [2026-11-04] API discovery needs three sets, not one catalog

- **Grounding:** [[artifacts/projects/shopify-api]], [[patterns/composition/negotiated-capability-intersection]], [[patterns/behavioral/context-is-not-authority]].
- **Change:** refined [[_schemas/api-case-study]] discovery dimension to record declared capabilities, negotiated compatibility, actually callable operations, and refresh/invalidation triggers.
- **Status:** **applied**, 2026-11-04, local uncommitted schema change.
- **Expected benefit:** prevent future studies from mistaking advertised support for execution authority, or a cached tool list for current page capabilities. No runtime enforcement or new confirmed pattern inferred.

### [2026-11-04] Protocol studies need separate compatibility and disclosure contracts

- **Grounding:** [[patterns/quality-bar/revision-bound-review]], [[patterns/behavioral/context-is-not-authority]] and [[patterns/behavioral/latent-vs-deterministic-split]], observed in [[artifacts/projects/mcp-apps]], [[artifacts/projects/openai-mcp-extensions]] and [[concepts/skills-over-mcp]].
- **Observed defect risks:** modern core versus legacy initialization, stable UI wire versus SDK migration, host-surface support, and conflicting structuredContent guidance can produce a fluent but incompatible or overbroad claim. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#documentation-conflicts]], [[sources/modelcontextprotocol--mcp-apps-docs#messages-context]], [[sources/openai--mcp-extensions#platforms]].
- **Applied change:** added a compact versioned-protocol supplement to [[_schemas/source]], requiring separate core/extension/SDK/host/exercised contracts and model/host/view disclosure. Existing INGEST citation routing reaches this schema; no new operation or duplicate template.
- **Status:** **applied**, 2026-11-04, local uncommitted wiki change.
- **Expected benefit:** future protocol studies preserve exact compatibility, evidence class and disclosure boundaries. No runtime support or secrecy guarantee is created by the schema.

- **Repeated deterministic move:** three parallel source collections each required the same hash/size verification. Skillified it as `scripts/check-document-captures.py`, documented through the existing INGEST/source-schema route and Tooling. Definition of done: reject digest/size mismatch, missing/duplicate/escaping entries and malformed/empty receipts; accept both receipt forms; never fetch/edit evidence. Eight temporary validation scenarios passed, and all 54 real captures verify.

Compounding budget: refined one existing schema and factored repeated integrity checks into one read-only script, without adding another operation or promoting an overlapping capability pattern.

## [2026-11-03] Pass 17 — complete social-source evidence

| # | Source-grounded learning | Applied change | Status |
| --- | --- | --- | --- |
| 55 | [[patterns/behavioral/evidence-gated-completion]] at ingestion: the tibo API preview omitted most principles, and meaningful counterexamples were only in attachments. [[sources/poteto--tibo-engineering#capture]], [[sources/poteto--tibo-engineering#auto-pick-counterexamples]] | Added a compact completeness gate to [[_schemas/source]]: expanded text, relevant parent/quote context, meaningful attachments, dated linked-page differences, and screenshot-versus-execution evidence class. Applied it to [[artifacts/projects/tibo-dog]]. | **applied** 2026-11-03; full expanded text and four images preserved and inspected. |

Compounding budget: a small schema guard addresses the observed truncation failure without adding new tools or a duplicate engineering-principles page. Existing related concepts/patterns were extended; the corpus-scale defect-validation pattern remains proposed.

## [2026-11-03] Pass 18 — route verification-budget decisions

- Applied the review-budget principle from [[concepts/review-cost-aware-workflows#principle-verification-over-abstract-adversarial-review]] to the consumer front door: `for-builders.md` now routes that decision directly to its canonical principle and fidelity limits, rather than making builders infer it from the older Interrogate ledger. [[sources/poteto--verification-over-adversarial-review#verification-first]]
- Status: **applied** 2026-11-03. Compounding budget: extended an existing concept and a routing row; no duplicate concept, new workflow, installed-skill change or additional review agents.

## [2026-11-04] Pass 19 — route domain-orchestrator designs

- Applied the explicit separation of human steering, domain coordination and worker execution from [[concepts/agent-control-plane#principle-persistent-domain-orchestration-with-sandboxed-execution]] as a focused build-intent route in `for-builders.md`. The row sends builders to the canonical principle, related architecture and durability boundaries, with the screenshot clearly labeled a proposal. [[sources/mattpocock--domain-orchestrator-factory#root]]
- Status: **applied** 2026-11-04. Extended existing concepts instead of creating a near-duplicate architecture page. No orchestrator, worker, cron or installed skill was created; this is research ingestion, not authorization to build the proposed system.

## [2026-11-04] Pass 20 — route production evidence into evals

- Applied [[concepts/trace-lake]] to the consumer routing table: builders seeking production-feedback loops now land on the trace corpus, verification-first review and model-fidelity pages together. [[sources/ankrgyl--trace-lake#trace-to-eval]]
- Existing wiki practice already preserves source evidence and validator fixtures. No trace database or background investigation is justified by this ingest alone. For a recurring ingestion defect, the concrete next step remains an evidence-backed fixture/check under the existing LINT #18 trigger, not a new prose-only review loop.
- Status: **applied** 2026-11-04 (builder route). No installed skills, scheduled jobs, accounts or runtime infrastructure changed.

## [2026-11-04] Pass 21 — library-relative routing checks

- Applied [[concepts/lifelong-skill-routing]] through existing [[patterns/composition/resolver-routing-table]] and [[patterns/quality-bar/complexity-ratchet]]: `_schemas/skill.md` now asks for neighboring competitors, body-faithful distinguishing scope, and separate evidence for old-route retention, new-skill discovery and task success. It preserves the literal captured trigger instead of rewriting source evidence. [[sources/zhang--skill-plus-plus#method]] [[sources/zhang--skill-plus-plus#task-success]]
- Added a growing-library build-intent route to `for-builders.md`. Kept existing pattern counts/statuses; a reported routing benchmark is not an additional inspected production routing-table artifact.
- Status: **applied** 2026-11-04. No installed skill, router, model or production configuration changed. Promotion trigger for an automated refiner: observed collisions in the actual library plus a routing/outcome fixture set that can compare it with a simpler manual metadata correction. The paper alone does not justify a new multi-model maintenance pipeline.
- Preservation boundary: documented a narrow paper-source exception in both maintainer entry points and `remote-setup.md`: full Skill++ reproductions stay local, while version pins, hashes, restoration notes and original research are public. This is a source-handling rule, not evidence that the experiments were reproduced.

## [2026-11-04] Pass 22 — statuses are not guarantees

- Applied [[patterns/behavioral/evidence-gated-completion]] from [[artifacts/projects/auto-ontology]] to `_schemas/project.md`: distinguish configured readiness, entity coverage, certification, executable validation and persisted publication. The concrete source gaps are connection-count readiness, entity-fraction answerability and non-atomic certification flags. [[sources/nvidia--auto-ontology#readiness]] [[sources/nvidia--auto-ontology#coverage]] [[sources/nvidia--auto-ontology#publication]]
- Added the semantic-data-query build-intent route to `for-builders.md`. Extended existing vocabulary, context, routing and evaluation pages instead of inventing an overlapping ontology concept page.
- Status: **applied** 2026-11-04. No service installed, source connected, runtime skill changed or model/evaluation job launched. Promotion trigger for a local ontology experiment: a scoped set of real business questions that currently fail on ambiguity, plus gold results and a matched agent baseline with cost/latency tracking. Research alone does not justify deploying the stack.

## [2026-11-04] Pass 23 — observation and recovery boundaries

- Applied [[patterns/behavioral/evidence-gated-completion]] and [[patterns/behavioral/context-is-not-authority]] from [[artifacts/projects/codex]] to `_schemas/project.md`: identify model-visible input, runtime activity, persisted state and recovery unit, rather than treating all as one transcript or completion signal. [[sources/openai--codex#trace]] [[sources/openai--codex#goal-provenance]] [[sources/openai--codex#storage]]
- Added a focused builder route to the runtime investigation and promoted Codex out of the project candidate queue. Kept the older Goals and marketplace accounts version-scoped while adding implementation corrections.
- Status: **applied** 2026-11-04. No installed skills, local Codex configuration or production runtime changed. Promotion trigger for additional tooling: an actual mismatch between saved source identity, model-visible evidence and a claimed recovered result; no new tracing service built merely because the source contains one.

## [2026-11-04] Pass 24 — uncertain outcomes and retained authority

- Applied [[patterns/behavioral/evidence-gated-completion]] and [[patterns/behavioral/context-is-not-authority]] from [[artifacts/projects/background-agents]] to the project schema: record the no-retry cutoff, execution identity, accepted/saved/retired distinction, and content/credentials that survive revocation. Concrete grounding is ambiguous first-prompt delivery, provider checkpoint uncertainty and pinned memory/cache persistence. [[sources/open-inspect--background-agents#automation-retry]] [[sources/open-inspect--background-agents#shutdown-design]] [[sources/open-inspect--background-agents#memory-boundary]]
- Added the hosted-background-agent builder route; extended existing concepts/patterns rather than making near-duplicate durability/memory pages. Status: **applied** 2026-11-04. No installed skills, production permissions, runtime or deployment changed.
- Promotion trigger for a local experiment: actual background tasks with a defined acceptance fixture and observed interruption/retry cost. Research alone does not justify another agent hosting stack.

## [2026-11-04] Pass 25 — snapshot granularity, not versioning by implication

- Applied [[patterns/behavioral/evidence-gated-completion]] from [[artifacts/projects/superplane]] to `_schemas/project.md`: distinguish the task/run/node/action snapshot units and enumerate live dependencies. Grounding: node configuration is copied but subsequent event routing reads live graph edges. [[sources/superplanehq--superplane#execution-state]] [[sources/superplanehq--superplane#event-routing]]
- Added the issue-to-PR/repair-loop builder route; extended existing durability/review concepts rather than creating a second software-factory concept page. Narrow analogues did not inflate proposed pattern counts.
- Status: **applied** 2026-11-04. No installed skills, runtime, infrastructure or deployment changed. Promotion trigger for an implementation experiment: repeated issue-to-PR work with measurable review/repair cost and explicit acceptance fixtures. Research alone does not justify installing a new orchestration stack.

### [2026-11-05] Documentation collections retain reading scope

**Applied** 2026-11-05 to [[_schemas/source]]. [[patterns/quality-bar/revision-bound-review]] applies to the evidence actually reviewed, not merely the files captured. [[concepts/developer-documentation-design]] exposed this distinction in long multi-language product pages and HTML text extraction. Added a citation-page requirement for reviewed sections, representation limitations and guidance/documented/runtime/outcome boundaries. Expected benefit: prevent capture count from being mistaken for comprehensive inspection; no new harness or duplicate validator needed.

### [2026-11-05] Skillify the documentation investigation matrix

**Applied** 2026-11-05. [[patterns/composition/resolver-routing-table]] and [[patterns/quality-bar/revision-bound-review]] apply to repeated documentation-system studies: [[projects/writing-amazing-developer-docs/README]] now compares task docs, internal architecture, operational docs, executable reference and discovery. Added [[_schemas/documentation-case-study]] with an explicit input/output, review matrix and definition of done; registered it in both harness Routing tables and root/builder routes. It preserves the distinctions observed in [[concepts/developer-documentation-design]], including hidden fixtures, mixed migration states, policy differences and empirical denominators. Expected benefit: future studies spend effort on evidence and interpretation rather than re-deriving the same matrix; no new generic lint gate or duplicate fact catalog needed.

### [2026-11-05] Reproducibility claims require an artifact inventory

**Applied**2026-11-05 to [[_schemas/documentation-case-study]]. [[patterns/quality-bar/revision-bound-review]] and [[patterns/behavioral/evidence-gated-completion]] apply to [[sources/mintlify--docs-url-discovery-bench#reproducibility-gap]]: the published report names committed proxy logs that are absent at the pinned tree. Added a study-matrix row and completion check for actual preserved inputs, excluded attempts and regeneration versus restoration. Expected benefit: prevent documented reproduction commands from being reported as available replay evidence. Existing capture/link/source checks were reused; no unsupported generic new linter added.

### [2026-11-05] Classify the interface and isolate the treatment

**Applied** 2026-11-05 to [[_schemas/documentation-case-study]]. [[patterns/behavioral/context-is-not-authority]] maps to documentation servers that can execute APIs or trigger indexing; [[patterns/behavioral/evidence-gated-completion]] maps to forced versus discovered context, grounded versus ungrounded scoring and PASS with unmeasured checks. Added two matrix rows for interface role/effects/version/caller and controlled treatment/accounting. Grounding: [[sources/frontier-docs--platforms-20261105#readme-mcp]], [[sources/frontier-docs--platforms-20261105#context7-search-contract]], [[sources/frontier-docs--tool-design-evaluation-20261105#dokimi-methodology]]. Expected benefit: future investigations will not mistake a transport label or overall score for an authority/completion guarantee. Existing receipt/link scripts suffice; no speculative new linter or installed skill.

## [2026-11-06] Pass 26 — verification belongs to the claim actually checked

- Applied [[patterns/behavioral/evidence-gated-completion]] and the narrower claim-revision analogue of [[patterns/quality-bar/revision-bound-review]] to `_schemas/skill.md`: distinguish unchecked candidates from reviewed unresolved claims; separate structural validators from semantic or runtime evidence; identify edits that invalidate verification. [[sources/cloudflare--security-audit-skill#verdict-contract]] [[sources/cloudflare--security-audit-skill#material-reverification]] [[sources/cloudflare--security-audit-skill#findings-code]] [[sources/cloudflare--security-audit-skill#coverage-code]]
- Added a security-review evidence/coverage builder route and extended existing concepts instead of inventing another verification concept. Preserved the earlier verification-first argument: concrete falsification is not abstract adversarial nitpicking.
- Status: **applied**. No installed skill, permission, production configuration or full audit changed. The only upstream execution was the dependency-free validator fixture suites (65 passing tests).
- Promotion trigger for additional automation: actually adopt a scoped audit with a supplied sandbox and evidence-promoter implementation; then test cross-file completeness and worker identity with fixtures. Research alone does not justify building a new security harness.

## [2026-11-06] Pass 27 — restore constraints, revoke effects

- **Learning:** a resumed task may restore its work but accidentally renew authority; stopping/revoking the initiator may leave downstream grants. [[sources/replit--agent-habitat-architecture#durability]] [[sources/lhchavez--managed-agent-environments#containment]]
- **Applied:** added a scoped security-state/residual-delegation question to `_schemas/project.md`, grounded in [[patterns/behavioral/context-is-not-authority]] and [[patterns/behavioral/evidence-gated-completion]]. Added a builder route to [[concepts/agent-habitat-architecture]].
- **Expected benefit:** future source studies name the actual restore/revocation boundary instead of upgrading credential custody or process termination into stronger guarantees. No installed skill, runtime policy or approval flow changed.
- **Status:** applied 2026-11-06; schema criteria only, with proposal status retained.

## [2026-11-06] Pass 28 — route time-shifted work to its real contracts

- **Grounding:** [[artifacts/projects/vercel-schedules]], [[patterns/behavioral/context-is-not-authority]] and [[patterns/behavioral/evidence-gated-completion]] separate permission revalidation and accepted/dispatched/completed work. [[sources/vercel--schedules-docs#eve-identity]] [[sources/vercel--schedules-docs#eve-occurrence]]
- **Applied:** added a builder routing row for agent/user-created future work, and preserved documentation conflicts plus coverage/read scope in the source map. Existing project/API schemas already require lifecycle, retry and frozen/live contract inspection; no duplicate schema section added.
- **Expected benefit:** future builders find target-specific retry, cancellation and current-permission evidence before treating “scheduled” as “done.” No installed skill or scheduler configuration changed.
- **Status:** applied 2026-11-06.

## [2026-11-06] Pass 29 — route model-adaptation decisions to their evidence

- **Grounding:** [[artifacts/projects/inkling-2-small]], [[patterns/behavioral/evidence-gated-completion]] and [[patterns/quality-bar/revision-bound-review]] distinguish held-out results, changed budgets and actual release state. [[sources/thinking-machines--inkling-2-small#forecasting]] [[sources/thinking-machines--inkling-2-small#benchmark-contract]] [[sources/thinking-machines--inkling-2-small#availability]]
- **Applied:** a builder route for choosing/customizing models; source maps preserve benchmark conditions, normalization, uneven seed counts, API-versus-model limits and capture omissions. Raw HTML/table/replay data retained where readable extraction loses interactive evidence.
- **Expected benefit:** prevent a good leaderboard score or future license promise from substituting for task-specific adaptation and deployment evidence. Existing evidence/guarantee schemas already cover these questions; no redundant schema section, installed skill or agent configuration added.
- **Status:** applied 2026-11-06.

## [2026-11-07] Pass 30 — route memory design through evidence and retrieval baselines

- **Grounding:** [[concepts/agent-memory-consolidation]], [[patterns/quality-bar/complexity-ratchet]] and [[patterns/behavioral/evidence-gated-completion]]; wiki growth can outstrip source size, and reported wiki-only gains can still trail search. [[sources/anthropic--components-of-agent-memory#expansion]] [[sources/anthropic--components-of-agent-memory#wiki-search]] [[sources/anthropic--components-of-agent-memory#compute-budget]]
- **Applied:** a builder route to memory layers, search/wiki/hybrid comparisons, actual build/maintenance cost, and adoption/consistency/retention contracts. The concept specifies a promotion trigger: repeated cross-document work plus held-out evidence that consolidation improves the existing retrieval workflow.
- **Expected benefit:** prevent token-budget charts, graph density or a stored summary from substituting for demonstrated task benefit. Existing citation/link checks remain structural, not a semantic quality metric.
- **Status:** applied 2026-11-07. No automatic dreaming job, installed skill edit or speculative new pattern; existing schemas cover evidence boundaries.

## [2026-11-07] T3 Code — partial views cannot authorize destructive inference

**Applied**2026-11-07. [[patterns/behavioral/evidence-gated-completion]] maps to two concrete T3 boundaries: partial shell membership is not deletion, and absent/empty/null file-revision answers differ. Extended [[_schemas/project]]'s existing observation/persistence questions with completeness/authoritative-absence and applied-state/cursor checks. Grounding: [[sources/pingdotgg--t3code#client-consistency]] and [[sources/pingdotgg--t3code#review-revision-absence]]. This is a focused schema refinement; no new pattern promotion, installable skill or generic linter. The existing source/link checks already cover preservation; runtime semantics still need actual acceptance tests.

## [2026-11-08] Rubric — route proactive behavior through responsibility and evidence

- **Grounding:** [[concepts/proactive-agent-discernment]], [[patterns/behavioral/context-is-not-authority]] and [[patterns/behavioral/latent-vs-deterministic-split]]; a classifier can predict relevance without a mandate, and some events should be deferred. [[sources/rubriclabs--always-on-agents#discernment]] [[sources/rubriclabs--always-on-agents#triage]] [[sources/rubriclabs--jev-use-cases#notifications]]
- **Applied:** builder route for always-on/event-triage/notification decisions, with explicit limits on classifier evidence. The concept defines a concrete adoption trigger and separate missed-opportunity, intervention and interruption measures.
- **Expected benefit:** distinguish useful autonomy from activity and token volume; carry existing authorization without inferring new authority from reaction memory.
- **Status:** applied 2026-11-08. Existing schemas suffice; no new installed skill, heartbeat or local message-transport rule. The source's proposal is research, not a command to reconfigure this agent.

## [2026-11-09] Decision cascades — pin the statistic and comparison contract

- **Grounding:** [[concepts/typed-decision-cascades]], [[patterns/quality-bar/revision-bound-review]] and [[patterns/behavioral/latent-vs-deterministic-split]]. The gateway can substitute selected-answer probability for normalized confidence; savings also change with the baseline and escalation rate. [[sources/typesafe--decision-model-docs#confidence]] [[sources/nutlope--jev-fraud#pipeline]] [[sources/buzzoni--jev-engineering#economics]]
- **Applied:** a conditional evidence question in [[_schemas/concept]] and a builder route for bounded decisions/cascade economics. Future studies should state statistic semantics, calibration coverage and the full comparison/billing contract.
- **Expected benefit:** prevent unlike confidence fields, historical runs or unequal-quality cost baselines from being silently combined. Existing structural validators suffice; no speculative new test framework.
- **Status:** applied 2026-11-09 to repository research guidance only. No installed skill, provider integration or live routing policy changed. Production adoption remains conditional on a recurring costly decision and held-out evidence.
