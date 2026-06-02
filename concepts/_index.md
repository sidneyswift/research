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

## Candidate list (not yet paged)

Add candidates here as one-line entries before promoting to a full page. Keep a `source:` link on each so future-you knows where to look.

- *Candidates surfaced by the Garry Tan "AI Explainer" series are currently tracked as proposed **patterns** (see [patterns/_index.md](../patterns/_index.md)); promote any that are better described as standalone ideas than as cross-artifact techniques.*
