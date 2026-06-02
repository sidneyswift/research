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
*(none yet)*

## By creator

### Anthropic official
*(none yet)*

### Community
*(none yet)*

## Candidate list (not yet deep-dived)

Add candidates here as one-line entries before promoting to a full page. Keep a `source:` URL on each candidate so future-you knows where to look.

**From `claude-for-financial-services`** (source: [[sources/anthropic--financial-services]]; ~55 skills across 7 verticals + 11 partner skills). High-value, pattern-bearing candidates to deep-dive:

- `comps-analysis` (financial-analysis) — *provenance-first* preamble ("⚠️ Data Source Priority — NEVER use web search as primary") + "Perfect for / Not ideal for" trigger anchoring. `…/financial-analysis/skills/comps-analysis/SKILL.md`
- `tear-sheet` (sp-global partner) — *audience-segmented* output (4 audiences, 4 reference files, "if unspecified, ask") + firm-customizable brand block. `…/partner-built/spglobal/skills/tear-sheet/SKILL.md`
- `gl-recon` + `break-trace` (bundled in gl-reconciler) — the reconciliation skills behind the trust-tiered worked example.
- `dcf-model` (financial-analysis) — ships a `scripts/validate_dcf.py` + `TROUBLESHOOTING.md`; example of a skill with executable validation.
- `ic-memo`, `returns-analysis`, `dd-checklist` (private-equity) — near-isomorphic to Sidney's catalog IC-memo / IRR-MOIC / diligence workflows.
- `pptx-author` / `xlsx-author` (financial-analysis) — *headless* document authoring skills, used in Managed Agent mode (no open Office doc).
- `skill-creator` (financial-analysis) — FSI's own copy of the meta-skill; compare to Anthropic's and gbrain's variants once deep-dived.
- *(full enumeration: 7 verticals × skills lists in [[sources/anthropic--financial-services#README]] skill+command reference)*
