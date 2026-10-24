---
domain: concepts
type: concept
name: workspace-skill-distribution
creators:
  - "[[creators/openai]]"
sources:
  - "[[sources/openai--codex-skills-doc]]"
  - "[[sources/openai--chatgpt-skills-help]]"
  - "[[sources/openai--plugins]]"
  - "[[sources/agentskills--specification]]"
status: emerging
last-reviewed: 2026-06-04
popularity-signals:
  - signal: official-product-surface
    value: "First-party in ChatGPT Business/Enterprise (workspace skill library, 5 admin permissions) and Codex (4-tier scope ladder, plugin workspace sharing)"
    as-of: 2026-06-04
    source: "[[sources/openai--chatgpt-skills-help#five-permissions]]"
---

# workspace-skill-distribution

> **One-line:** How an organization gets agent skills in front of *every* member without per-machine installs — OpenAI's stack (the deepest yet shipped) resolves into four distinct **rails**: (1) **repo-as-install** (skills committed at `.agents/skills/`; cloning the repo *is* the install), (2) **admin push** (ChatGPT's "Enable skills installing" — install skills *for other workspace members*, auto-applied), (3) **marketplace sharing** (plugins shared via the workspace, one-click "Shared with you", or `INSTALLED_BY_DEFAULT` policy in a repo marketplace), and (4) **machine/container scope** (`/etc/codex/skills` via MDM or image bake-in) — while admin *enforcement* config stays deliberately **restrictive-only** (it can constrain, never distribute).

## What it is

The distribution problem is the org-scale version of skill installation: one team maintains a canonical skill set; every member's agent should load it automatically, and updates should propagate without anyone touching laptops. As of 2026-06, OpenAI ships first-party answers on two surfaces:

**Codex (developer surface)** — a four-tier *scope ladder* ([[sources/openai--codex-skills-doc#scope-ladder]]):

| Scope | Location | Distribution semantics |
| --- | --- | --- |
| REPO | `.agents/skills` (CWD → parents → repo root) | commit to the repo → every cloner gets them; "organizations can check in skills relevant to everyone using the repository" ([[sources/openai--codex-skills-doc#repo-scope-teams]]) |
| USER | `~/.agents/skills` | per-person; bootstrap-script / symlink territory (symlinks officially followed — [[sources/openai--codex-skills-doc#symlinks]]) |
| ADMIN | `/etc/codex/skills` | machine/container-wide; "default admin skills available to each user on the machine" — the MDM / golden-image rail |
| SYSTEM | bundled by OpenAI | vendor-controlled |

Above the ladder sits the *packaging* rail: "Skills are the authoring format… **plugins are the installable distribution unit**" ([[sources/openai--codex-skills-doc#authoring-vs-distribution]]) — plugins are shared through the ChatGPT workspace and surface under **"Shared with you"** in the plugin directory ([[sources/openai--plugins#marketplace.json]] documents the registry grammar; the marketplace `policy.installation: INSTALLED_BY_DEFAULT` value makes a repo-scoped plugin auto-install — [[sources/openai--plugins#plugin-json-spec]]).

**ChatGPT (consumer surface)** — a workspace skill library with five admin permissions, the standout being **"Enable skills installing": install skills "for other workspace members so they are used automatically"** ([[sources/openai--chatgpt-skills-help#install-for-others]]) — true central push, plus a separate admin Skills page for inventory/review ([[sources/openai--chatgpt-skills-help#admin-skills-page]]). Skills invoke automatically once installed ([[sources/openai--chatgpt-skills-help#auto-invocation]]).

What makes the rails composable is the **shared format**: both surfaces implement the Agent Skills open standard ([[sources/agentskills--specification#root]], [[sources/openai--codex-skills-doc#open-standard]], [[sources/openai--chatgpt-skills-help#open-standard]]) — one canonical skills repo can feed every rail.

## The restrictive/additive split

The sharpest design choice observed: OpenAI's admin *enforcement* layer (cloud-managed `requirements.toml` policies pushed from the workspace, plus MDM/system files) is **restrictive-only** — it can pin sandbox/approval floors, allowlist MCP servers, disable features, even disable plugin workspace-sharing, but it has **no mechanism to push skills out**. Distribution is always *additive* and flows through content channels (repos, marketplaces, workspace libraries); enforcement is *subtractive* and flows through policy channels. (Observed across the Codex enterprise managed-configuration docs in the 2026-06-04 research pass — citation page for that doc not yet snapshotted, flagged in Open questions; the skills doc's scope ladder shows the additive side first-party: [[sources/openai--codex-skills-doc#scope-ladder]].)

This split keeps the trust story legible: an admin can never silently inject behavior into a user's agent through the policy pipe; behavior arrives through inspectable content (a repo diff, a marketplace listing, a workspace library entry with a review page).

## Why it matters

- **It's the missing operational half of the skills story.** The wiki has studied how great skills are *built* ([[patterns/quality-bar/skill-pack-bundle]]) and *packaged* ([[patterns/structural/marketplace-as-multi-plugin]]); this is how they *reach an org* — the layer any company adopting skills hits immediately.
- **Repo-as-install is the cheapest rail and the most portable** — it's just git. The scope-ladder design means zero install tooling for the dominant case (engineers in shared repos), and the same committed directory serves Codex, Cursor, and Copilot (per the multi-client adoption on [[sources/agentskills--specification#governance]]).
- **The admin-push permission is genuinely new** ([[sources/openai--chatgpt-skills-help#install-for-others]]) — the first first-party "install on behalf of everyone, auto-applied" mechanism we've cataloged in any agent ecosystem. Watch for Anthropic's equivalent.

## Evidence & claims

- *Repo-committed skills are a first-party team-distribution mechanism* — **demonstrated**: the scope table's suggested-use column says so explicitly ([[sources/openai--codex-skills-doc#repo-scope-teams]]).
- *Plugins are the cross-repo distribution unit; skills are authoring* — **demonstrated**: literal doc text ([[sources/openai--codex-skills-doc#authoring-vs-distribution]]).
- *ChatGPT admins can install skills for all members, auto-applied* — **demonstrated, secondary-fidelity** (search-extracted help article; quoted verbatim across two passes): [[sources/openai--chatgpt-skills-help#install-for-others]].
- *Enforcement config is restrictive-only* — **asserted** from the 2026-06-04 research pass over the managed-configuration docs; needs its own snapshotted source before leaning harder (see Open questions).
- *Skills in Codex cloud/web are NOT documented* — **demonstrated by absence**: the surfaces list names only CLI/IDE/app ([[sources/openai--codex-skills-doc#surfaces]]); cloud relies on AGENTS.md.

## Patterns demonstrated

- [[patterns/composition/single-source-multi-surface-distribution]] — the whole concept is this pattern at org scale: one canonical skills repo rendered onto four rails (repo, workspace library, marketplace, machine image) instead of hand-copied per surface. ([[sources/openai--codex-skills-doc#scope-ladder]], [[sources/openai--chatgpt-skills-help#five-permissions]])
- [[patterns/structural/marketplace-as-multi-plugin]] — the marketplace rail's grammar ([[sources/openai--plugins#marketplace.json]]); workspace sharing adds a *private* distribution channel to the pattern's public-catalog story.
- **Proposed (1 example): restrictive/additive admin split** — enforcement pipes can only subtract, content pipes can only add. Needs a second ecosystem's example (Anthropic enterprise policy? Cursor teams?) before promotion.

## Tensions & counter-arguments

- **Push vs. provenance.** Admin-push ("installing for others") is exactly the mechanism prompt-injection reviewers worry about — a workspace admin can make every member's assistant run arbitrary skill instructions. The admin Skills review page ([[sources/openai--chatgpt-skills-help#admin-skills-page]]) is the mitigating control; whether it includes content audit (vs. inventory only) is unknown.
- **The rails don't fully meet.** Codex cloud reads AGENTS.md but (documentedly) not skills ([[sources/openai--codex-skills-doc#surfaces]]); workspace-shared plugins still need a per-user install click. "Auto appear everywhere" is ~95% achievable, not 100%.
- **n=1 ecosystem.** This page is grounded almost entirely in OpenAI surfaces. Claude Code has enterprise-managed settings and marketplaces (`extraKnownMarketplaces`) that rhyme, but we haven't ingested that side; the concept could look different once we do.

## Related

- [[concepts/convergent-agent-plugin-spec]] — the shared format that makes one repo feed every rail; this page is that concept's *operations* consequence.
- [[artifacts/plugins/openai-codex-plugins-marketplace]] — the public-catalog end of the marketplace rail.
- [[patterns/composition/single-source-multi-surface-distribution]] — the underlying pattern.
- `scratch/openai-private-skills-marketplace-deployment.md` — the operational deep-research report (2026-06-04) this page distills; full per-surface detail, gotchas, and the recommended 4-rail architecture for Swift-Response live there.

## What we'd steal

**Exhaustive ledger** (★ = highest-value):

- ★ **Repo-as-install as the default rail.** Put shared skills where the work already is (`.agents/skills` in the repo) so distribution is `git pull` — no installer, no registry, no drift. Steal for any team-shared agent assets, including this wiki's own future skill packs.
- ★ **The restrictive/additive split.** Keep "what admins can force" and "what admins can distribute" in separate channels with opposite signs. A clean trust invariant for any org-scale agent system.
- ★ **A scope ladder with named tiers** (repo → user → admin → system) and documented suggested-use per tier — makes "where should this skill live?" a routing decision, not a debate.
- **Authoring/distribution as distinct primitives** — "skills are the authoring format, plugins the installable distribution unit." Don't overload one artifact with both jobs.
- **Install-for-others as an explicit, separately-grantable permission** — central push exists but is its own toggle, not bundled into generic admin rights.
- **A dedicated review surface for org-distributed assets** (the admin Skills page) — inventory of everything members created/shared, separate from the permission switchboard.
- **Officially-blessed symlinks** — a one-line doc commitment ("follows the symlink target") that legitimizes the clone-once-symlink-everywhere fleet pattern.
- **A quantified metadata budget** (~2% of context / 8K chars) with graceful degradation (shorten descriptions → omit with warning) — capacity planning for skill catalogs ([[sources/openai--codex-skills-doc#context-budget]]).

## Open questions

- **Snapshot the managed-configuration doc** (developers.openai.com/codex/enterprise/managed-configuration) — the restrictive-only claim deserves its own citation page; ingest candidate.
- **What's Anthropic's equivalent stack?** Claude Code enterprise managed settings + `extraKnownMarketplaces` + Cowork plugin distribution — ingesting that side would test whether the 4-rail shape and the restrictive/additive split generalize (and could promote the proposed pattern).
- **Does Codex cloud load repo skills?** Documented surfaces omit it; no changelog entry adds it. Watch openai/codex#24517 ("team-level Skill Hub") and the changelog.
- **Does the admin Skills page audit content or just inventory it?** Determines how much the push mechanism's injection risk is actually mitigated.
- **Workspace-shared plugins: can the install click be removed?** `INSTALLED_BY_DEFAULT` exists for repo marketplaces; is there (or will there be) a workspace-marketplace equivalent?
