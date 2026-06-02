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
|---|---|---|---|
| 1 | [[patterns/composition/resolver-routing-table]] — a tested table mapping *intent → which skill/doc to load* | Added an explicit **Routing** table to `CLAUDE.md` Operations: *request → operation* and *source type → citation `type:` + raw-material location + page schema*. | **applied** 2026-06-02 (`CLAUDE.md` §Routing) |
| 2 | [[patterns/quality-bar/complexity-ratchet]] — every session adds tests/docs that reload into context, so quality only rises (forward-only) | Ingests now **ratchet**: INGEST closes with a `ratchet: links +N · orphans +0 · patterns +N` tally; LINT check #12 flags any ingest that added a page but no links, or stranded an orphan. | **applied** 2026-06-02 (`CLAUDE.md` INGEST + LINT #12) |
| 3 | [[patterns/behavioral/diarization]] — read everything about a subject, write *one* page of distilled judgment | Added a "this page is a **judgment distillation**, not a transcription" reminder to every artifact + concept schema header. | **applied** 2026-06-02 (`_schemas/{skill,plugin,mcp-server,concept}.md`) |
| 4 | [[patterns/behavioral/latent-vs-deterministic-split]] — every step is model-judgment (latent) or same-in/same-out (deterministic) | Tagged each INGEST step **(det)** or **(latent)** with a legend; det steps (clone, index row, log) are flagged as future-tooling candidates. | **applied** 2026-06-02 (`CLAUDE.md` INGEST) |
| 5 | [[patterns/structural/thin-harness-fat-skills]] — push intelligence up into markdown, execution down into code, keep the harness thin | Added LINT check #13 (**harness bloat**): flag detailed how-to that crept into `CLAUDE.md` and belongs in a `_schemas/` template. | **applied** 2026-06-02 (`CLAUDE.md` LINT #13) |
| 6 | [[patterns/quality-bar/skill-pack-bundle]] — a skill isn't done until it ships with tests/evals | Added a `## Detection recipe` section to `_schemas/pattern.md` (look-for / confirm-with / rule-out); the ≥2 examples are the positive fixtures, the counter-example the negative test. | **applied** 2026-06-02 (`_schemas/pattern.md`) |

### [2026-06-02] Pass 2 — the remaining confirmed/with-page patterns

REFLECT over the patterns not covered by the seed pass. Applied immediately (grounded → ships).

| # | Learning (cited) | Wiki change | Status |
|---|---|---|---|
| 7 | [[patterns/behavioral/skill-as-method-call]] — a skill file is a parameterized procedure; same file + different args → different capability | Documented each operation as a **parameterized call** in `CLAUDE.md` Routing (`INGEST(<source>)`, `QUERY(<question>)`, `LINT(<scope?>)`, `REFLECT(<since?>)`); noted that a `_schemas/` template is likewise a parameterized page. | **applied** 2026-06-02 (`CLAUDE.md` §Routing) |
| 8 | [[patterns/composition/single-source-multi-surface-distribution]] — one definition, many runtime surfaces | Added an anti-rule: wiki pages are the single source; `DASHBOARD.html`, query deliverables, and any future `llms.txt` are *surfaces* rendered from them, never parallel copies that drift. | **applied** 2026-06-02 (`CLAUDE.md` anti-rules) |
| 9 | [[patterns/structural/marketplace-as-multi-plugin]] — one manifest registers N à-la-carte units | No change: already embodied. `index.md` (+ per-domain `_index.md`) is exactly this registry — it lists every page as an independently-linkable unit. Recorded so we don't re-propose it. | **embodied** 2026-06-02 (`index.md`) |

### [2026-06-02] Pass 3 — deep review of the Garry Tan corpus

Mined the gstack/gbrain pages + all 8 essays (esp. #5 *Skillify Manifesto* and #6 *Meta-Meta-Prompting*, which credits Karpathy's LLM Wiki as gbrain's own origin). gbrain is our pattern realized with extras, so it's the richest mine. Small/safe items applied immediately; larger tooling items recorded as `proposed`.

**Applied this pass:**

| # | Learning (cited) | Wiki change | Status |
|---|---|---|---|
| 10 | [[patterns/composition/resolver-routing-table]] — "test the routing, not just the output" (gbrain ships `routing-eval.jsonl`) | Added a **Routing evals** table to `CLAUDE.md` (sample request → expected operation) so the resolver is spot-checkable, not just declared. | **applied** 2026-06-02 (`CLAUDE.md` §Routing) |
| 11 | [[patterns/behavioral/diarization]] — gbrain's "entity propagation": after ingest, walk every entity mentioned and update its page | INGEST step 5 now **propagates to every entity the source touches**, not just the creator — the real source of cross-link density. | **applied** 2026-06-02 (`CLAUDE.md` INGEST 5) |
| 12 | [[patterns/composition/resolver-routing-table]] — `check-resolvable` finds "dark" (unreachable) skills | LINT check #15: every routing request resolves to an operation, every schema is reachable from an operation, every page reachable from `index.md`. | **applied** 2026-06-02 (`CLAUDE.md` LINT #15) |
| 13 | [[patterns/composition/resolver-routing-table]] — gbrain's DRY audit catches duplicate/overlapping skills | LINT check #16: flag near-duplicate pages competing for the same role (distinct from contradictions). | **applied** 2026-06-02 (`CLAUDE.md` LINT #16) |
| 14 | [[patterns/quality-bar/complexity-ratchet]] — Garry's "search your history for where you said wtf" = the tests you're missing | LINT check #17: aggregate every `## Open questions` + `TODO` into one "what to chase next" backlog. | **applied** 2026-06-02 (`CLAUDE.md` LINT #17) |

**Proposed (bigger — genuine "could add" items):**

| # | Learning (cited) | Proposed change | Status |
|---|---|---|---|
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
|---|---|---|---|
| 22 | [[concepts/completion-contract]] / [[patterns/behavioral/evidence-gated-completion]] — a completion contract must name a **blocked stop condition** (if you can't finish honestly: stop, mark the gap, report what would unlock it, never fake done); budget-exhaustion ≠ done | `_schemas/_definition-of-done.md` was a purely *positive* checklist (what must be present) with no "blocked" path — so a half-finished page had no defined honest exit. Added an **"If blocked"** section: mark the gap inline + in `## Open questions` + log why; "done" is checked (LINT/`wiki-doctor`), not self-assessed; out of budget ≠ done. | **applied** 2026-06-02 (`_schemas/_definition-of-done.md`) |
| 23 | [[patterns/behavioral/evidence-gated-completion]] — "done" is decided by an external assertable surface, not self-assessment | No change: already embodied. `scripts/wiki-doctor.py` *is* the deterministic verification surface for a page's done-ness (a page passes when the doctor is clean). Recorded so we don't re-propose it — and noted in the new "If blocked" clause so the link is explicit. | **embodied** 2026-06-02 (`scripts/wiki-doctor.py`) |
| 24 | [[concepts/completion-contract]] — preserve epistemic levels (confirmed / approximate / blocked / uncertain), never flatten to one success claim | No change: already embodied across the wiki's hedging conventions — claims marked *asserted vs. demonstrated*, `status:` fields, `proposed`-vs-`confirmed` patterns, `as-of` signal dating. The Codex research case study is external corroboration of a discipline we already run. | **embodied** 2026-06-02 |

Cross-check (not a new change): [[patterns/behavioral/skill-as-method-call]], promoted to confirmed this ingest, validates ledger **#7**'s "operations are parameterized calls" framing from a *second creator* — our `INGEST(<source>)` / `QUERY(<question>)` operations are method-calls, now cross-confirmed against Codex's `/goal <contract>` (a documented six-slot signature). #7 stays `applied`; this just retires its single-creator caveat.

### [2026-06-02] Pass 5 — the compound-engineering ingest

REFLECT over the [[artifacts/plugins/compound-engineering]] ingest (Every / Kieran Klaassen) — the first non-Garry tested skill pack, whose `/ce-compound` skill *is* a knowledge-compounding mechanism much like this wiki's own INGEST→log→ratchet loop. The richest mine for self-application since gbrain.

| # | Learning (cited) | Wiki change | Status |
|---|---|---|---|
| 25 | [[patterns/quality-bar/complexity-ratchet]] via `compound-engineering`'s `/ce-compound` — score overlap on **5 dimensions before writing**; high overlap → *update* the existing doc, don't create a duplicate ("two docs on the same problem will inevitably drift apart") | We had LINT #16 (DRY/overlap audit) but only *after the fact*. Added a **dedup-before-create** guard to INGEST step 3: score a candidate page against existing ones (subject + mechanism + role) and extend rather than duplicate. The pre-creation twin of #16 — cheaper to never make the duplicate. | **applied** 2026-06-02 (`CLAUDE.md` INGEST 3) |
| 26 | [[patterns/behavioral/latent-vs-deterministic-split]] via CE's `AGENTS.md` — "skills are guardrails for an intelligent agent, not a controller for a dumb one; **calibrate prescription level to the failure mode**" (hard rules for deterministic safety, trust for judgment) | No change: already embodied. The `(det)`/`(latent)` step tagging (ledger #4) + the hard anti-rules vs. latent judgment steps already calibrate how prescriptive `CLAUDE.md` is per step. Recorded so we don't re-propose it; CE is external corroboration of the discipline. | **embodied** 2026-06-02 (`CLAUDE.md` INGEST legend + anti-rules) |
| 27 | `compound-engineering`'s `/ce-compound` Discoverability Check — "the knowledge store only compounds value when agents can *find* it"; edit the instruction file so a fresh agent discovers the store | No change: already embodied. `index.md` is the mandated front door (INGEST step 7 + LINT #15 reachability: every page reachable from `index.md`). The Discoverability Check is exactly what step 7 + #15 enforce. | **embodied** 2026-06-02 (`index.md`, LINT #15) |

Cross-check (not a new change): this ingest promoted [[patterns/quality-bar/complexity-ratchet]] proposed→confirmed and **retired the same-creator caveat** on [[patterns/quality-bar/skill-pack-bundle]] + [[patterns/behavioral/latent-vs-deterministic-split]] (CE = the non-Garry witness). Those are pattern-page changes, not machinery changes — but they harden the *grounding* of ledger #2/#5/#6, which cited those very patterns to justify the ratchet/harness-bloat/detection-recipe machinery. Our own machinery now rests on cross-creator-confirmed patterns, not one author's house style.

## Open meta-questions

- ~~Should REFLECT run automatically every N ingests, or only on demand?~~ **Resolved 2026-06-02:** REFLECT applies grounded changes directly (no human gate); the lightweight INGEST step-9 nudge runs every ingest, and a deeper pass runs on demand / after lint.
- Is `meta/` itself in scope for LINT's orphan/staleness checks? (Yes — it's a wiki page like any other.)
