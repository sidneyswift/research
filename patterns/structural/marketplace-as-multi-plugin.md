---
domain: patterns
type: pattern
name: marketplace-as-multi-plugin
category: structural
status: confirmed
last-reviewed: 2026-06-01
example-count: 2
---

# marketplace-as-multi-plugin

> One repository registers as a *marketplace* via `.claude-plugin/marketplace.json` and declares **N installable plugins** inside it, each with its own source path, name, and description. Users install plugins à la carte from the single repo URL — no fork, no separate publish per plugin.

## Longer definition

A marketplace manifest turns a monorepo into a catalog. Instead of one repo = one plugin, the repo's `marketplace.json` lists many child plugins, each pointing at a subdirectory that holds its own `plugin.json` (and skills/commands/agents/hooks/MCP). The repo becomes the *distribution unit*; the plugin becomes the *installation unit*. This lets a creator group related work, share repo-level tooling (CI, linters, a sync script), and let users take only the pieces they need — while keeping everything versioned and shipped together.

## Mechanism

`.claude-plugin/marketplace.json` carries a `name`, an `owner`, and a `plugins[]` array; each entry is `{name, displayName, source, description}` where `source` is a path into the repo ([[sources/anthropic--financial-services#marketplace.json]]). Install is two steps: add the marketplace once, then install plugins by `<plugin>@<marketplace-name>`:

```bash
claude plugin marketplace add anthropics/financial-services
claude plugin install financial-analysis@claude-for-financial-services
claude plugin install gl-reconciler@claude-for-financial-services
```

In `financial-services` the catalog is large and *typed by directory*: 7 vertical plugins (`plugins/vertical-plugins/`), 10 agent plugins (`plugins/agent-plugins/`), 2 partner plugins (`plugins/partner-built/`), and 1 admin installer — **20 entries** total, all from one `marketplace.json` ([[sources/anthropic--financial-services#marketplace.json]], [[sources/anthropic--financial-services#repo-layout]]). The simpler precedent, `anthropics/skills`, registers **3** child plugins (`document-skills`, `example-skills`, `claude-api`) the same way ([[sources/anthropic--skills#marketplace.json]]).

## When to use

- You have **several related plugins** a user might want independently (install `financial-analysis` core, skip `wealth-management`) but that share context, tooling, and release cadence.
- You want **repo-level CI and shared scripts** (one `check.py`, one sync script, one secret-scan workflow) over many plugins without N repos to maintain.
- You're shipping a **reference/demonstration set** where browsing the whole catalog in one place is the point.
- **Partners or sub-teams** contribute plugins that should live alongside yours but stay independently installable and licensed (LSEG, S&P Global in their own `partner-built/` dirs, S&P shipping per-skill `LICENSE` files — [[sources/anthropic--financial-services#partner-spglobal]]).

## When NOT to use

- **One cohesive product, many internal parts.** If the parts are never installed separately, ship **one plugin with many skills inside it** (cf. gstack/gbrain) — a marketplace manifest just adds ceremony.
- **Unrelated plugins.** A marketplace implies a coherent collection. Grouping unrelated tools to inflate a catalog confuses discovery.
- **Independent release cadences that fight the monorepo.** If child plugins must version and ship on wildly different schedules with conflicting dependencies, separate repos may hurt less than a shared one. (FSI mitigates this with *per-plugin* `version` fields and a per-plugin patch-bump hook — [[sources/anthropic--financial-services#scripts-version-bump]].)

## Why it works

Discovery and trust both favor "one URL, many parts." A user adds a single marketplace they trust (`anthropics/financial-services`) and then composes their own install from its catalog, rather than hunting N repos of unknown provenance. For the author, the monorepo is where shared discipline lives — the FSI repo's whole single-source-of-truth + drift-check machinery only works *because* the verticals and the agents that vendor their skills sit in one tree ([[sources/anthropic--financial-services#scripts-sync]]). The manifest is also tiny and declarative: adding a plugin is one array entry pointing at a directory, so the catalog scales from 3 to 20 with no new mechanism.

## Examples in this wiki

- [[artifacts/plugins/anthropic-financial-services-marketplace]] — 20 plugins (7 vertical + 10 agent + 2 partner + 1 installer) registered from one `marketplace.json`; installed à la carte by `<plugin>@claude-for-financial-services`. — citation: [[sources/anthropic--financial-services#marketplace.json]]
- [[artifacts/plugins/anthropic-skills-marketplace]] — 3 child plugins (`document-skills`, `example-skills`, `claude-api`) registered from one repo's manifest; the minimal form of the same pattern. — citation: [[sources/anthropic--skills#marketplace.json]]

## Counter-examples or anti-pattern

- [[artifacts/plugins/gstack]] and [[artifacts/plugins/gbrain]] — both are **single plugins that bundle many skills internally** rather than registering many plugins. gbrain's 40+ skills install as *one* skillpack, not 40 marketplace entries. The choice is deliberate: those skills are interdependent parts of one system (gbrain even uses a `RESOLVER.md` to route among them — [[sources/garrytan--gbrain#skills-resolver]]), so à-la-carte installation would break the whole. This is the precise fork in the road: **independent parts → marketplace-as-multi-plugin; interdependent parts → one plugin, many skills.**

## Related patterns

- [[patterns/composition/single-source-multi-surface-distribution]] — composes-with. FSI stacks them: a multi-plugin marketplace *and* a second (Managed Agent) runtime for the agent plugins.
- *(proposed)* license-segmentation-within-one-repo — marketplaces enable per-plugin and even per-skill licensing (S&P's per-skill `LICENSE` files); tracked pending a clean 2nd example.

## Open questions

- Is there a practical ceiling where a marketplace becomes too big to browse? 20 typed-by-directory entries still reads cleanly; 200 flat ones might not. FSI's answer is *directory typing* (vertical / agent / partner) — is that itself the scaling pattern?
- How do install *ordering* dependencies surface? FSI's README tells users to install `financial-analysis` "first" because it carries the shared connectors ([[sources/anthropic--financial-services#README]]) — the manifest itself doesn't encode that ordering. Should it?
