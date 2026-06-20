---
domain: creators
type: index
last-reviewed: 2026-06-11
---

# Creators

The people and orgs producing the artifacts we study. Context, not the main event — but useful for spotting house styles and tracking who's worth following.

Each creator page uses [../_schemas/creator.md](../_schemas/creator.md).

## Orgs

- [[creators/anthropic]] — sets the Agent Skills spec; ships demonstration skills + plugins + Cowork marketplace + the Claude API + the Managed Agents API + the financial-services reference marketplace
- [[creators/every]] — a media-and-software company that both writes about and builds with agents; origin and home of **compound engineering**. Ships [[artifacts/plugins/compound-engineering]] (Kieran Klaassen, GM of Cora) + the essays/guide behind it (amplified by CEO Dan Shipper). The wiki's first non-Garry tested skill pack.
- [[creators/openai]] — frontier lab behind GPT and the **Codex** agentic-coding CLI. The wiki's first OpenAI entry, via the Codex **Goals** feature ([[artifacts/projects/codex-goals]]) and the cookbook guide documenting it; supplied the non-Garry example that confirmed [[patterns/behavioral/skill-as-method-call]]. Counterweight to Anthropic for testing whether a "pattern" is field-level or one ecosystem's house style.
- [[creators/vercel]] — the frontend-cloud company behind Next.js, the AI SDK, and the Workflow SDK; ships **eve** ([[artifacts/projects/eve]]), an open-source filesystem-first framework for durable backend AI agents ("Next.js for agents"). The wiki's first **platform/infra** creator (not a model lab, not a skill author) and first artifact at the **harness/runtime tier** — the long-missing "thin harness" middle. Grounds [[concepts/filesystem-first-agent-framework]] + [[concepts/durable-agent-execution]].
- [[creators/forward-future]] — **Matthew Berman**'s AI media brand ("Make the future legible"). Ships the open-source **Loop Library** ([[artifacts/skills/loop-library]]) — a curated, submission-driven catalog of repeatable agent **loops** + an installable find/adapt/design skill. The wiki's first **curator/aggregator** creator (a cross-builder anthology, not a single-author pack) and first whose artifact is a *catalog of prompts*. House style: bounded autonomy (every loop names how it verifies and when it stops), plain-language onboarding that hides the jargon.

- [[creators/ahrefs]] — the largest SEO tooling company; publishes large-scale data studies on AI search citation behavior. Tim Soulo (CMO) is the public voice. Contributes research/data (not agents/skills) that informs how content and documentation should be designed for AI discoverability.
- [[creators/prodmgmt-world]] — independent commercial publisher of [[artifacts/plugins/pm-os]] (paid PM skill bundle, claude-code + cursor + cowork). The wiki's first **commercial** creator — sells agent content as a versioned product (CHANGELOG, upgrade-migration skill) rather than sharing a repo.

## Individuals

- [[creators/garry-tan]] — President & CEO of Y Combinator. Ships `gstack` and `gbrain`; author of the 8-part **"AI Explainer" essay series** (the source for the wiki's `thin-harness-fat-skills` / `resolver-routing-table` / `latent-vs-deterministic` / `diarization` / `complexity-ratchet` / `skill-pack-bundle` patterns). Bridge between Anthropic's ecosystem and the founder/builder community.
- [[creators/prodmgmt-world]] — George Nurijanian (gnurio / @nurijanian), New Zealand. Sells **PM OS** ($99 one-time; [[artifacts/plugins/pm-os]]) — the wiki's first **commercial, closed-source** creator and first **non-engineering vertical** auteur. House style: *enforcement over suggestion* (pre-flight attestation, Context Guard, imperative hook directives) + a coach-not-doer product philosophy.
- [[creators/matt-pocock]] — Matt Pocock (@mattpocock, UK), TypeScript educator (Total TypeScript / AI Hero). Ships [[artifacts/plugins/mattpocock-skills]] — at **135K★**, the wiki's highest-starred source and first **individual-engineer pack via skills.sh**. House style: *fundamentals over frameworks*, small/composable/model-agnostic skills grounded in classic SWE books, **predictability** as the root virtue — the near-perfect inverse of prodmgmt.world's enforcement-heavy approach. Defines [[concepts/skill-invocation-axis]] + [[concepts/ubiquitous-language-for-agents]].
