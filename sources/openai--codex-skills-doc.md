---
domain: sources
type: docs-page
url: https://developers.openai.com/codex/skills
retrieved: 2026-06-04
snapshot-location: sources/openai--codex-skills-doc/
upstream-commit: n/a (living page)
last-reviewed: 2026-06-04
---

# OpenAI Codex docs — "Agent Skills" (developers.openai.com/codex/skills)

> OpenAI's canonical doc for the **Codex skills system**: skills "build on the open agent skills standard" (links agentskills.io directly), load by progressive disclosure under an explicit **context budget** (~2% of context window / 8,000 chars for the initial list), and are discovered from a four-tier **scope ladder** — repo (`.agents/skills`, scanned CWD→repo-root), user (`~/.agents/skills`), admin (`/etc/codex/skills`), system (bundled). The page also draws the line this wiki cares about: **"Skills are the authoring format… Plugins are the installable distribution unit."** Skills launched in Codex 2025-12-18 (per the Codex changelog); custom prompts were deprecated in their favor 2026-01-22.

## Snapshot details

- **Retrieved**: 2026-06-04 (verbatim article body; site nav stripped)
- **Where it lives in this wiki**: `sources/openai--codex-skills-doc/snapshot.md`
- **Upstream URL**: https://developers.openai.com/codex/skills
- **Upstream identifier**: n/a — living docs page; claims pinned to retrieval date. Corroborating dates from https://developers.openai.com/codex/changelog (skills launch 2025-12-18; custom prompts deprecated 2026-01-22; plugins launch 2026-03-25 — retrieved 2026-06-04 by research agents, changelog itself not snapshotted).

## Anchor map

- `#root` — the doc as a whole
- `#open-standard` — "Skills build on the open agent skills standard" with a direct link to agentskills.io — OpenAI's explicit, named adoption of the spec
- `#authoring-vs-distribution` — "Skills are the authoring format for reusable workflows. Plugins are the installable distribution unit for reusable skills and apps in Codex."
- `#surfaces` — "Skills are available in the Codex CLI, IDE extension, and Codex app." (Codex cloud/web conspicuously absent)
- `#context-budget` — initial skills list capped at ~2% of context window or 8,000 chars; descriptions shortened first, then skills omitted with a warning; budget applies only to the initial list
- `#invocation` — explicit (`/skills`, `$` mention) vs implicit (description matching); description-writing guidance ("front-load the key use case and trigger words")
- `#scope-ladder` — the discovery table: REPO `$CWD/.agents/skills` → parents → `$REPO_ROOT/.agents/skills`; USER `$HOME/.agents/skills`; ADMIN `/etc/codex/skills` ("default admin skills available to each user on the machine"); SYSTEM bundled
- `#repo-scope-teams` — the suggested-use column: "teams can check in skills relevant to a working folder"; "organizations can check in skills relevant to everyone using the repository"
- `#symlinks` — "Codex supports symlinked skill folders and follows the symlink target"
- `#skill-installer` — `$skill-installer` for curated skills + "prompt the installer to download skills from other repositories"; positioned for "local setup and experimentation"
- `#skills-config` — `[[skills.config]]` per-skill enable/disable in `~/.codex/config.toml`
- `#agents-openai-yaml` — the optional `agents/openai.yaml` extension: `interface{}` UI metadata, `policy.allow_implicit_invocation` (default true), `dependencies.tools` (MCP servers a skill declares)
- `#best-practices` — one job per skill; instructions over scripts unless determinism/external tooling needed; imperative steps; test trigger behavior

## Why we cite this

- **OpenAI's named adoption of the Agent Skills standard** (`#open-standard`) — the second lab formally on the spec; upgrades [[concepts/convergent-agent-plugin-spec]] from "convergence" to "standardization."
- **The authoring/distribution split** (`#authoring-vs-distribution`) — the cleanest first-party articulation of skills-vs-plugins roles; the same split this wiki's REFLECT guidance assumes.
- **The scope ladder** (`#scope-ladder`, `#repo-scope-teams`) — repo-committed skills as the zero-install team distribution mechanism ("cloning the repo *is* the install"); admin scope for machines/containers. Grounds [[concepts/workspace-skill-distribution]].
- **A quantified context budget for skill metadata** (`#context-budget`) — a concrete, citable number for the progressive-disclosure cost model.
- **`agents/openai.yaml`** (`#agents-openai-yaml`) — how a lab extends the shared spec without breaking it (UI + policy + tool dependencies live in a sibling file, not in SKILL.md frontmatter).

## Popularity signals

- **Signal type**: official vendor docs — authoritative by definition for the Codex skills surface. As-of 2026-06-04.
- Adjacent (not on this page): `openai/skills` catalog repo ≈13.4K★, `agentskills/agentskills` spec repo ≈19.9K★, both as-of 2026-06-04 (research-agent retrievals).

## Related sources

- [[sources/agentskills--specification]] — the open standard this doc implements (and links).
- [[sources/openai--plugins]] — the curated marketplace at the "distribution unit" end of this doc's authoring/distribution split.
- [[sources/openai--chatgpt-skills-help]] — the ChatGPT-side skills surface (same standard, consumer workspace distribution).
- [[sources/openai--using-goals-in-codex]] — the other Codex-behavioral source.
