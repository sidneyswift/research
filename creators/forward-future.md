---
domain: creators
type: org
name: Forward Future
handle: forwardfuture
url: https://www.forwardfuture.ai/
country: US
last-reviewed: 2026-06-20
---

# Forward Future

> **One-line:** Matthew Berman's AI media brand ("Make the future legible"), which ships the open-source **Loop Library** — a curated, submission-driven catalog of repeatable agent loops plus an installable skill to find/adapt/design them. The wiki's first creator whose artifact is a *catalog of prompts* rather than a code-bearing skill pack.

*Page shape (gbrain's brain-page schema, per [[patterns/behavioral/diarization]] applied to ourselves): **compiled truth on top** + an **append-only `## Timeline`** below. Done when it passes the [page checklist](_definition-of-done.md).*

## Attributes

- **What they ship**: the [[artifacts/skills/loop-library]] skill + its public catalog site (`signals.forwardfuture.ai/loop-library`); a newsletter/media operation around AI. Distribution via `npx skills add Forward-Future/loop-library` (skills.sh) and a Codex `agents/openai.yaml`.
- **Distribution channel**: own GitHub org (`Forward-Future`), own domain, the skills.sh installer, and a Cloudflare Worker fronting submission forms. Deploy infra is named to **Matthew Berman** personally (`loop-library-forms.mberman84.workers.dev`) ([[sources/forward-future--loop-library#AGENTS.md-canonical]]).
- **Position in ecosystem**: a *curator/aggregator*, not a single-author pack. The Loop Library solicits and edits community submissions ("We review everything before publishing"), so the catalog is a cross-builder anthology — authors include Matthew Berman (~15 loops), Peter Steinberger, Hiten Shah, Pierson Marks, Lukas Kucinski, Istasha, Jose C. Munoz, and others ([[sources/forward-future--loop-library#loop-data]]).
- **Notable framings**: a **loop** is "a playbook with feedback built in"; "Loops are not permission for an agent to run forever" — the value is the *stopping condition* ([[sources/forward-future--loop-library#README-why-bounded]]). Tagline: "Make the future legible."

## Artifacts produced

### Skills
- [[artifacts/skills/loop-library]] — find / adapt / design a bounded agent loop; bundles the 31-loop catalog.

### Plugins
*(none — the Loop Library is distributed as a single skill, not a multi-skill marketplace plugin)*

### MCP servers
*(none)*

## Design philosophy (if discernible)

Two distinctive moves. **(1) Curation behind a quality bar, not authorship.** Loops are submitted, reviewed, and edited "for clarity" before publishing; the canonical dataset enforces that every loop carry a stable slug, unique title/description, attribution, dates, `useWhen`, verification criteria, and related links, or the build's drift check rejects it ([[sources/forward-future--loop-library#AGENTS.md-canonical]]). **(2) Plain-language onboarding.** The skill explicitly *hides* loop jargon from new users — "do not use terms such as trigger, success gate, terminal state, guardrail… unless the user asks" — and runs a one-question-at-a-time design interview ([[sources/forward-future--loop-library#skill-interview]]), the same align-before-execute shape as [[artifacts/skills/grilling]]. The house bias is toward **bounded autonomy**: every published loop names how it verifies and when it stops, and the skill refuses to treat designing a loop as permission to run it ([[sources/forward-future--loop-library#README-skill]]).

## Timeline (append-only)

- 2026-06-12 — `Forward-Future/loop-library` repository created ([[sources/forward-future--loop-library#github-stars]]).
- 2026-06-19 — catalog stands at 31 published loops; repo at 92★ / 14 forks, one week old ([[sources/forward-future--loop-library#github-stars]]).
- 2026-06-20 — ingested into the wiki (skill + catalog + the "loop" concept); supplied the 2nd artifact that confirmed [[patterns/behavioral/evidence-gated-completion]] ([[sources/forward-future--loop-library#root]]).

## Source citations

- [[sources/forward-future--loop-library#root]]
- [[sources/forward-future--loop-library#README-why-bounded]]
- [[sources/forward-future--loop-library#AGENTS.md-canonical]]
- [[sources/forward-future--loop-library#skill-interview]]
- [[sources/forward-future--loop-library#github-stars]]
