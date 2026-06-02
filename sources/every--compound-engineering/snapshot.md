# Compound Engineering (the guide) — PARTIAL CAPTURE

> ⚠ **This is a PARTIAL capture, not a full verbatim snapshot.** `every.to` is a
> subscription publication; the complete article text was not retrievable. Below is
> (a) confirmed metadata, (b) **verbatim-quoted fragments** extracted via WebFetch on
> 2026-06-02 (marked with quotation marks — these are as-close-to-verbatim as the
> retrieval allowed), and (c) a **structural outline** (paraphrased). Treat the
> quoted fragments as near-verbatim evidence and the outline as a faithful summary,
> NOT as the author's exact prose.
> **TODO:** paste the full verbatim guide text from a subscriber session and replace
> this capture (then drop the PARTIAL banner).

---

## Metadata

- **Title:** Compound Engineering (guide)
- **Publisher:** Every (every.to), guides section
- **URL:** https://every.to/guides/compound-engineering
- **Type:** living guide page (updated alongside the plugin; the companion essay
  [[sources/every--compound-engineering-gets-an-upgrade]] of 2026-05-29 says "An
  updated compound engineering guide provides further details," i.e. the guide
  tracks the methodology as it evolves).
- **Associated with:** Kieran Klaassen (GM of Cora at Every; originator of "compound
  engineering" and author of the plugin) and Every's editorial (Dan Shipper, CEO).
- **Retrieved:** 2026-06-02 (WebFetch, partial).

---

## Core thesis (verbatim fragment)

> "Each unit of engineering work should make subsequent units easier—not harder."

Compound engineering inverts traditional development, where every feature adds
complexity and technical debt. Instead, each unit of work *teaches the system*, so
the next unit is cheaper. Stated split: **80% planning + review, 20% execution.**

---

## The loop (verbatim fragment)

> "Ideate → brainstorm → plan → work → review → polish → compound → repeat"

One-line role of each phase (outline, paraphrased from the guide):

- **Ideate** — turns ambiguity into product options
- **Brainstorm** — turns promising ideas into concrete requirements
- **Plan** — transforms idea into blueprint
- **Work** — execution follows the plan
- **Review** — catches issues, captures learnings
- **Polish** — turns working software into a quality experience
- **Compound** — documents solved problems for system improvement
- **Repeat** — next cycle starts with better context

---

## The eight beliefs to "unlearn" (verbatim fragments)

The guide lists beliefs engineers must discard:

1. "The code must be written by hand"
2. "Every line must be manually reviewed"
3. "Solutions must originate from the engineer"
4. "Code is the primary artifact"
5. "Writing code is the core job function"
6. "First attempts should be good"
7. "Code is self-expression"
8. "More typing equals more learning"

Plus the higher-order beliefs:

- "The code is what matters"
- "Engineering thinking is separate from product thinking"

---

## The 50/50 rule + taste-in-systems (verbatim fragments)

> "you should allocate 50 percent of engineering time to building features, and 50
> percent to improving the system—in other words, any work that helps build
> institutional knowledge rather than shipping something specific."

(The inverse of the traditional ~90/10 feature/infrastructure split.)

> "Taste belongs in systems, not in review. Bake your judgment into configuration,
> schemas, and automated checks."

---

## The adoption ladder — 5 stages (outline, paraphrased)

- **Stage 0: Manual development** — writing code line by line without AI
- **Stage 1: Chat-based assistance** — AI as reference; copy-pasting snippets
- **Stage 2: Agentic tools with line-by-line review** — AI reads/changes files; human approves everything
- **Stage 3: Plan-first, PR-only review** — detailed planning collaboration; AI implements unsupervised; human reviews the PR *(where compound engineering begins)*
- **Stage 4: Idea to PR (single machine)** — agent handles research → PR; human does ideation, review, merge
- **Stage 5: Parallel cloud execution** — multiple agents work simultaneously on remote infrastructure

---

## Stated statistics (verbatim fragments)

- "95 percent garbage rate" on first attempts; "50 percent" on second attempts.
- Plugin contents (as the guide states them): "40+ specialized agents," "30+ slash
  entry points," "35+ skills." *(Repo filesystem at commit `3e77a7b` shows 43 agent
  files + 38 skill dirs — see [[sources/every--compound-engineering-plugin]]; the
  "30+ slash entry points" are the skills invoked as `/ce-*` slash commands.)*

---

## Practical guidance (outline, paraphrased)

- Match your current competency to a ladder stage; don't skip stages.
- Build safety nets (tests, automated review) so unsupervised execution is safe.
- Resist over-supervising — trust the loop; the **Compound** step is the most
  critical (capture reusable patterns/learnings in `CLAUDE.md`/`AGENTS.md` and a
  documented-solutions store).
