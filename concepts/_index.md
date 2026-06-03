---
domain: concepts
type: index
last-reviewed: 2026-06-01
---

# Concepts

Ideas and techniques worth their own page — especially from essays, papers, and threads where the durable output is a *concept*, not a runnable artifact. Each page uses [../\_schemas/concept.md](../_schemas/concept.md).

A concept becomes a **pattern** (in `patterns/`) once we've observed it as a concrete technique across **≥2 artifacts** in this wiki. Until then it lives here (or as a `proposed` pattern on an artifact page).

## Cataloged concepts

- [[concepts/compound-engineering]] — **the wiki's first concept page.** Every's (Kieran Klaassen's) AI-native development methodology: structure work so each unit makes the next easier; 80/20 planning-vs-execution, the 50/50 features-vs-systems budget, "taste belongs in systems, not review." The named, productized, *independently-arrived-at* twin of [[patterns/quality-bar/complexity-ratchet]]; embodied by [[artifacts/plugins/compound-engineering]]. Sources: [[sources/every--compound-engineering]], [[sources/every--compound-engineering-gets-an-upgrade]].
- [[concepts/completion-contract]] — an agent objective specified as a persistent, evidence-verified *contract* (outcome + verification surface + constraints + boundaries + iteration policy + blocked stop condition), so the agent runs "work → check → continue or complete" and "done" is decided by **evidence, not confidence**. OpenAI's term, productized as Codex Goals; embodied by [[artifacts/projects/codex-goals]]. Source: [[sources/openai--using-goals-in-codex]].
- [[concepts/convergent-agent-plugin-spec]] — two frontier labs independently shipped **near-identical agent plugin formats**: Anthropic `.claude-plugin/` and OpenAI `.codex-plugin/` share the same auto-discovered `skills/`/`commands/`/`agents/`, an identical `hooks.json` (`PostToolUse`/`matcher`) grammar, `.mcp.json`, and a `marketplace.json` registry — diverging mainly on connectors (`.app.json` hosted apps vs self-config MCP) and storefront. The plugin/skill shape is consolidating into a cross-lab standard. `status: emerging`. Sources: [[sources/openai--plugins]], [[sources/anthropic--plugins-reference]].

- [[concepts/dynamic-workflows]] — Claude Code's model-generated JS harnesses for multi-agent orchestration. The model writes a custom harness per task, spawning subagents with isolated context windows to defeat three named failure modes: agentic laziness, self-preferential bias, goal drift. Six composable patterns cataloged. Extends the skill spec into orchestration (workflows distributed via skills). `status: active`. Source: [[sources/anthropic--dynamic-workflows]].
- [[concepts/ai-search-as-parallel-discovery-layer]] — AI chatbots (ChatGPT, Google AI Overviews, AI Mode) form a **parallel discovery layer** independent of Google organic search — different sources, different citation patterns, different content format preferences. Based on 1 billion data points across 14 Ahrefs studies. YouTube mentions have the highest correlation (0.737) with AI brand visibility; 28.3% of most-cited pages have zero Google visibility. `status: emerging`. Source: [[sources/ahrefs--ai-search-optimization-research]].

## Candidate list (not yet paged)

Add candidates here as one-line entries before promoting to a full page. Keep a `source:` link on each so future-you knows where to look.

- *Candidates surfaced by the Garry Tan "AI Explainer" series are currently tracked as proposed **patterns** (see [patterns/_index.md](../patterns/_index.md)); promote any that are better described as standalone ideas than as cross-artifact techniques.*
