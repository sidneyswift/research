---
domain: sources
type: docs-page
url: https://help.openai.com/en/articles/20001066-skills-in-chatgpt
retrieved: 2026-06-04
snapshot-location: sources/openai--chatgpt-skills-help/ (⚠ partial — search-extracted, Cloudflare-gated upstream)
upstream-commit: n/a (living page)
last-reviewed: 2026-06-04
capture-fidelity: secondary (search-engine extraction of the exact article URL; quoted strings verbatim across two independent passes; browser re-capture TODO)
---

# OpenAI Help Center — "Skills in ChatGPT" (article 20001066)

> The doc that puts **agent skills inside ChatGPT itself** (beta: Business, Enterprise, Edu, Teachers, Healthcare) — same SKILL.md open standard ("download them from one product and install them in another"), invoked **automatically**, with a workspace skill library and **five admin permissions**, the standout being **"Enable skills installing": install skills *for other workspace members* so they're used automatically**. The first first-party mechanism we've seen for *pushing* skills to an organization rather than waiting for each user to pull.

## Snapshot details

- **Retrieved**: 2026-06-04 — **partial capture**. help.openai.com blocks automated fetch (Cloudflare/Intercom); content reconstructed from search-engine extraction of this exact article URL via two independent research passes that agreed on all quoted items. Quoted strings are verbatim; surrounding prose may paraphrase. ⚠ Re-capture from a browser is a TODO before leaning harder on this source.
- **Where it lives in this wiki**: `sources/openai--chatgpt-skills-help/snapshot.md`
- **Upstream URL**: https://help.openai.com/en/articles/20001066-skills-in-chatgpt
- **Upstream identifier**: n/a — living help-center page.

## Anchor map

- `#root` — the article as a whole
- `#open-standard` — "OpenAI skills follow the Agent Skills open standard, so you can download them from one product and install them in another"
- `#availability` — beta plans (Business, Enterprise, Edu, Teachers, Healthcare); also Codex + OpenAI API; off-by-default for Enterprise/Edu early access
- `#auto-invocation` — "ChatGPT can automatically use one or more skills when they are helpful" (no manual activation)
- `#five-permissions` — the Permissions & roles set: Enable skills / Enable skill uploading / Share skills / Publish skills to workspace / Enable skills installing
- `#install-for-others` — "Enable skills installing": install skills "for other workspace members so they are used automatically" — the admin-push mechanism
- `#admin-skills-page` — the separate admin Skills page for reviewing/managing every skill in the workspace
- `#shared-with-you` — member install flow: Skills > Shared with you > ••• > Install

## Why we cite this

- **The admin-push distribution mechanism** (`#install-for-others`) — centrally installing skills for an entire workspace, auto-applied. Grounds [[concepts/workspace-skill-distribution]]; the consumer-side counterpart to Codex's repo-scope skills.
- **Cross-product portability as a product promise** (`#open-standard`) — OpenAI marketing the open standard to end users, not just developers; further evidence for [[concepts/convergent-agent-plugin-spec]]'s standardization turn.
- **Governance shape** (`#five-permissions`, `#admin-skills-page`) — a worked example of role-based capability permissions + a separate inventory/review surface for org-distributed agent assets.

## Popularity signals

- **Signal type**: official vendor help-center doc — authoritative for the ChatGPT skills surface. As-of 2026-06-04. (Feature is beta; plan list per `#availability`.)

## Related sources

- [[sources/openai--codex-skills-doc]] — the developer-side skills surface (same standard, repo/user/admin scope ladder instead of workspace library).
- [[sources/agentskills--specification]] — the open standard both surfaces implement.
- [[sources/openai--plugins]] — the Codex marketplace; its "Shared with you" workspace-sharing category is the plugin-level sibling of this article's skill sharing.
