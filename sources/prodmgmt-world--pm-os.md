---
domain: sources
type: other # purchased proprietary plugin bundle (3 zips: claude-code, cursor, cowork)
url: https://prodmgmt.world
retrieved: 2026-06-10
snapshot-location: sources/prodmgmt-world--pm-os-bundle/ # LOCAL-ONLY, git-ignored (proprietary paid product — never committed/pushed; this repo is public)
upstream-commit: n/a # distributed as versioned zips; studied version 2.2.1
last-reviewed: 2026-06-11
---

# PM OS 2.2.1 (prodmgmt.world) — purchased plugin bundle

> **One-line:** the purchased "Product Manager's AI Operating System" bundle — 235 skills + 12 sub-agents + 2 hooks shipped as parallel Claude Code, Cursor, and Cowork packages — our first *paid, proprietary* artifact source.

*Done when it passes the [page checklist](_definition-of-done.md).*

## Snapshot details

- **Retrieved**: 2026-06-10 (purchased copy)
- **Where it lives in this wiki**: `sources/prodmgmt-world--pm-os-bundle/` — a **local-only, git-ignored** evidence copy (3 zips + extracted claude-code/cursor/cowork trees), same Option-B treatment as the cloned repos but with a stricter reason: PM OS is a proprietary paid product (`"license": "Proprietary"` in its manifest), so committing it to this public repo would republish paid material. It is **not** in `repos.manifest.tsv` (no public repo to re-clone from); rebuild by re-extracting the purchased zips. Claims below cite file paths inside that copy.
- **Upstream URL**: https://prodmgmt.world (product site); repo field in manifest: https://github.com/gnurio/pm-os (private/unverified)
- **Upstream identifier**: version `2.2.1` (from `.claude-plugin/plugin.json` and zip filenames)

## Anchor map

Paths are relative to `sources/prodmgmt-world--pm-os-bundle/claude-code/pm-os/plugins/pm-os/` unless noted.

- `#root` — the bundle as a whole (all three zips)
- `#plugin-manifest` — `.claude-plugin/plugin.json` (name, version 2.2.1, proprietary license, component description: 13 system + 11 workflow + 211 reusable skills, 12 sub-agents, 2 SessionStart hooks)
- `#skills-dir` — `skills/` (235 skill directories)
- `#agents-dir` — `agents/` (12 sub-agent persona files: pm-workflows router, knowledge-librarian, context-manager, 7 cross-functional reviewers, 2 PRD reviewers)
- `#hooks` — `hooks/hooks.json` + `tidy-reminder.sh` + `drip-reminder.sh` (2 SessionStart nudge hooks)
- `#mcp-config` — `.mcp.json` (6 servers: lenny-podcast HTTP, notion, linear, atlassian, github, perplexity)
- `#registry` — `registry/` (agents.json, commands.json, skills.json, workflows.json, CAPABILITIES.md — machine-readable component index)
- `#cursor-variant` — sibling cursor zip: `.cursor-plugin/marketplace.json`, `.cursor/hooks.json`, `.cursor/mcp.json`, emoji-named content dirs (📂 Context, 🧠 Knowledge, 📄 Templates, 💎 Examples)
- `#cowork-variant` — sibling cowork zip: `workspace/` layout for Anthropic Cowork
- `#knowledge-dir` — `🧠 Knowledge/` framework library shipped alongside skills (354 files: frameworks, prioritization, interview questions, metrics examples, writing styles, Lenny-Newsletter index; tag-metadata for filtering; root rule forces citing a Knowledge file before any PM opinion)
- `#workflow-chaining` — the 11 workflow SKILL.md files' chaining mechanism: inline prose steps, each a fixed 4-tuple (skill name → folder path → goal sentence → "Output to carry forward"); confirm-per-step header sentence; "Before starting" framework menus; uniform "Save output" trailer; mirrored in `registry/workflows.json` and validated by `bin/validate-workflow-registry.sh`
- `#skill-house-style` — reusable-skill authoring conventions: exactly 2 frontmatter fields (235/235), "Use when" trigger sentence (213/235) enforced by `bin/normalize-skill-descriptions.sh`, Required-Inputs/Instructions/Usage-Notes skeleton (183/235), 130 files retaining `{{HANDLEBARS}}` placeholders (bulk-converted prompt corpus; median 84 lines, hand-authored outliers to 1657)
- `#memory-schema` — `docs/memory/MEMORY-SCHEMA.md` + `bin/memory/*.sh` + system skills: 9-layer memory hierarchy; append-only `events.jsonl` (canonical) → `DECISION-LOG.md` (projection) → capped recall packets (consumer surface, `lookup_status` enum); per-path system-owned/user-owned upgrade boundary; preview-confirm writes with "stale yes" rule; untrusted-source/prompt-injection rules; daily-drip state machine with engagement-tapered cadence
- `#hook-directives` — `tidy-reminder.sh` `emit_directive()` + comments citing issue #8: passive nudges ("Consider running /tidy") were silently absorbed, replaced by imperative `[SESSION-START DIRECTIVE]` with mandated first action + no-re-offer clause; `drip-reminder.sh` dry-runs tidy and yields (single-nudge arbitration)
- `#telemetry` — `feedback-config.md` (Google Apps Script webhook, "The URL is the secret") + `pm-os-start/SKILL.md` 5 lifecycle curl pings (company/industry/funding/PM-level payloads, fail-silent, soft disclosure line) + ghost-written `/pm-os-testimonial` — the LLM as telemetry client
- `#templates-examples` — `📄 Templates/` (7 PRD formats with Use-When/Don't-Use-When/Detail/Time tags; `/prd` routes by 2-3 diagnostic questions matched to tags) + `💎 Examples/` ("calibrate the quality of your own thinking — not the format, but the substance")
- `#count-drift` — marketing prose vs validated registries: plugin.json/dirs = 235 skills & 12 agents; README says 237; Cowork README & cursor marketplace.json say 214 skills / 10 sub-agents — structure is CI-validated, narrative isn't

## Why we cite this

- Claims about how a commercial PM skill bundle is structured, priced-tier packaged, and distributed across three agent surfaces from one content set.
- Component inventory and composition claims for [[artifacts/plugins/pm-os]].
- Evidence for [[patterns/composition/single-source-multi-surface-distribution]] (one content set → claude-code + cursor + cowork zips) and [[patterns/quality-bar/skill-pack-bundle]].

## Popularity signals (if this source provides them)

- **Signal type**: commercial product (paid); no public star/install counts available.
- **Value at snapshot**: n/a — sold via prodmgmt.world; marketing claims on site not independently verifiable.
- **As-of**: 2026-06-10

## Related sources

- [[sources/anthropic--plugins-reference]] — the plugin format PM OS targets
- [[sources/every--compound-engineering]] — the other large multi-surface skill pack we've studied (38 skills/43 agents, converted to ~11 platforms)
