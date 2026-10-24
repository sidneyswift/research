---
domain: artifacts
type: index
subdomain: skills
last-reviewed: 2026-05-21
---

# Skills

Individual skills cataloged. Each page uses [../../\_schemas/skill.md](../../_schemas/skill.md).

## By ecosystem

### Claude Code skills
*(none yet)*

### Claude.ai Skills (general)
*(none yet)*

### Skills that work in both
- [[artifacts/skills/grilling]] — Matt Pocock's relentless one-question-at-a-time alignment interview (model-invoked; the reusable loop behind `grill-me`/`grill-with-docs`). The wiki's **first individual skill page**.
- [[artifacts/skills/writing-great-skills]] — Matt Pocock's reference skill for *authoring* skills (predictability, the two loads, the information-hierarchy ladder, leading words, the five failure modes); the most self-applicable artifact in the wiki.
- [[artifacts/skills/loop-library]] — Forward Future's find/adapt/design skill for **bounded agent loops**; routes a request to the smallest path and bundles a 31-loop catalog. Installs via skills.sh + ships a Codex `agents/openai.yaml`. Grounds [[concepts/agentic-loop]]; confirming 2nd artifact for [[patterns/behavioral/evidence-gated-completion]].

## By creator

### Anthropic official
*(none yet)*

### Community
**Matt Pocock** ([[creators/matt-pocock]], from [[artifacts/plugins/mattpocock-skills]]):
- [[artifacts/skills/grilling]] — the align-before-execute interview loop.
- [[artifacts/skills/writing-great-skills]] — skill-authoring vocabulary; grounds [[concepts/skill-invocation-axis]].

**Forward Future** ([[creators/forward-future]], from [[sources/forward-future--loop-library]]):
- [[artifacts/skills/loop-library]] — find/adapt/design a bounded agent loop; bundles the 31-loop catalog.

## Candidate list (not yet deep-dived)

Add candidates here as one-line entries before promoting to a full page. Keep a `source:` URL on each candidate so future-you knows where to look.

**From `mattpocock/skills`** (source: [[sources/mattpocock--skills]]; 17 in `plugin.json`, ~34 across buckets; 2 deep-dived above). High-value un-deep-dived:

- `codebase-design` — the **deep-module** vocabulary (Module/Interface/Depth/Seam/Adapter/Leverage/Locality) + the deletion test + "one adapter = hypothetical seam, two = real"; discloses to `DEEPENING.md` + `DESIGN-IT-TWICE.md`. Grounds a candidate "deep-modules-for-AI-navigability" concept. `skills/engineering/codebase-design/SKILL.md`
- `domain-modeling` — the active build/sharpen discipline behind [[concepts/ubiquitous-language-for-agents]] (challenge terms, edge-case scenarios, the ADR three-test gate; `CONTEXT.md`/`ADR`/`CONTEXT-MAP` formats). `…/engineering/domain-modeling/SKILL.md`
- `ask-matt` — the human-facing **router** (worked example on [[patterns/composition/resolver-routing-table]]); the idea→ship "main flow" + the "smart zone" (~120k) budget. `…/engineering/ask-matt/SKILL.md`
- `tdd` / `diagnosing-bugs` — the feedback-loop pair (red-green-refactor; reproduce→minimise→hypothesise→instrument→fix→regression-test). `…/engineering/{tdd,diagnosing-bugs}/SKILL.md`
- `improve-codebase-architecture` — scan for deepening opportunities → HTML report → grill the pick; "run every few days." `…/engineering/improve-codebase-architecture/SKILL.md`
- `to-prd` / `to-issues` / `triage` — the plan→issues pipeline (vertical slices; state-machine triage roles). `…/engineering/{to-prd,to-issues,triage}/SKILL.md`
- `handoff` / `teach` / `prototype` / `setup-matt-pocock-skills` — context-bridge across windows, multi-session teaching, throwaway prototypes, the per-repo-config precondition. `…/{productivity,engineering}/…/SKILL.md`
- *Drift note:* `implement` + `resolving-merge-conflicts` exist in `engineering/` on disk but are absent from `plugin.json` *and* the README (flagged on [[artifacts/plugins/mattpocock-skills]]); `deprecated/ubiquitous-language` was folded into `domain-modeling`.

**From `pm-os`** (source: [[sources/prodmgmt-world--pm-os-cowork]]; 235 skills — 13 system + 11 workflow + ~214 reusable; sampled, not inventoried):

- `pm-os-start` — onboarding with per-platform structured-question tool table (Cursor `AskQuestion` vs CC `AskUserQuestion`) + inline fallback; cross-platform authoring exemplar.
- `prd` — the 9-step workflow orchestrating the 9-reviewer panel; subagent contract + inline-persona fallback.
- `pm-os-tidy` / `pm-os-capture-memory` / `pm-os-daily-drip` — the memory/maintenance trio behind the hook directives and consent-gated capture.
- Several reusable skills ship `references/` dirs (progressive disclosure) — e.g. `adversarial-roleplay`, `blind-spot-scan`; mine on a dedicated pass.
- *Adjacent free repo:* `gnurio/nurijanian-skills` (source: https://github.com/gnurio/nurijanian-skills) — same creator, open-source; compare against the paid pack.

**From `claude-for-financial-services`** (source: [[sources/anthropic--financial-services]]; ~55 skills across 7 verticals + 11 partner skills). High-value, pattern-bearing candidates to deep-dive:

- `comps-analysis` (financial-analysis) — *provenance-first* preamble ("⚠️ Data Source Priority — NEVER use web search as primary") + "Perfect for / Not ideal for" trigger anchoring. `…/financial-analysis/skills/comps-analysis/SKILL.md`
- `tear-sheet` (sp-global partner) — *audience-segmented* output (4 audiences, 4 reference files, "if unspecified, ask") + firm-customizable brand block. `…/partner-built/spglobal/skills/tear-sheet/SKILL.md`
- `gl-recon` + `break-trace` (bundled in gl-reconciler) — the reconciliation skills behind the trust-tiered worked example.
- `dcf-model` (financial-analysis) — ships a `scripts/validate_dcf.py` + `TROUBLESHOOTING.md`; example of a skill with executable validation.
- `ic-memo`, `returns-analysis`, `dd-checklist` (private-equity) — near-isomorphic to Sidney's catalog IC-memo / IRR-MOIC / diligence workflows.
- `pptx-author` / `xlsx-author` (financial-analysis) — *headless* document authoring skills, used in Managed Agent mode (no open Office doc).
- `skill-creator` (financial-analysis) — FSI's own copy of the meta-skill; compare to Anthropic's and gbrain's variants once deep-dived.
- *(full enumeration: 7 verticals × skills lists in [[sources/anthropic--financial-services#README]] skill+command reference)*
