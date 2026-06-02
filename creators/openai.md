---
domain: creators
type: org
name: OpenAI
handle: openai
url: https://openai.com
last-reviewed: 2026-06-02
---

# OpenAI

> The lab behind GPT and the **Codex** agentic-coding CLI. In this wiki, OpenAI is the **first non-Anthropic / non-Garry-Tan creator** — its entry begins with one deeply-studied artifact (Codex **Goals**) and the OpenAI Cookbook guide that documents it.

**Scope note:** this page is grounded in the *one* OpenAI source ingested so far ([[sources/openai--using-goals-in-codex]]). OpenAI's broader catalog (GPT model family, the API, ChatGPT, the rest of the Codex CLI) is **context, not yet studied** — claims below stay close to what that source supports.

## Attributes

- **What they ship (studied here)**: the **Codex CLI** — an agentic coding tool installed via `npm i -g @openai/codex` or `brew … codex` — and its **Goals** feature (persistent, evidence-verified objectives via `/goal`), shipped in Codex **0.128.0** ([[sources/openai--using-goals-in-codex#lifecycle-commands]]).
- **What they ship (context, unstudied)**: GPT model family, the OpenAI API, ChatGPT, and the **OpenAI Cookbook** (`developers.openai.com/cookbook`, backed by the public `openai/openai-cookbook` repo) — a widely-referenced library of first-party how-to guides.
- **Distribution channels**: `developers.openai.com` (docs + cookbook), `github.com/openai` (incl. `openai-cookbook`), npm (`@openai/codex`), Homebrew.
- **Position in ecosystem**: a frontier lab and the **counterweight to Anthropic** in this wiki's scope — useful precisely because it lets us check whether a "pattern" is field-level or just one ecosystem's house style. The Codex Goals source already did this work: it supplied the **non-Garry** documented-parameter-signature that promoted [[patterns/behavioral/skill-as-method-call]].
- **House style (discernible from one source)**: cookbook guides are authored (named bylines), versioned in a public repo, and notably **scope their own technique** — the Goals guide ships an explicit "when NOT to use" section and a weak→strong worked example ([[sources/openai--using-goals-in-codex#when-not-to-use]], [[sources/openai--using-goals-in-codex#weak-vs-strong-perf]]).

## Artifacts produced

### Projects
- [[artifacts/projects/codex-goals]] — the Goals feature of the Codex CLI: persistent, thread-scoped, evidence-gated objectives via the `/goal` command surface. *(The broader Codex CLI is queued in [[artifacts/projects/_index]] but unstudied.)*

### Concepts originated / popularized
- [[concepts/completion-contract]] — the crisp framing of an agent objective as a "scoped, user-controlled completion contract," named in the Goals guide.

## Design philosophy (discernible from artifacts)

- **Autonomy on a leash.** The standout choice in the one artifact we've studied: a "keep working until done" loop fenced by budget accounting, a conservative event-driven dispatcher (with explicit anti-spin), evidence-gated completion, and user-held lifecycle authority — foregrounding the *constraints*, not the autonomy ([[sources/openai--using-goals-in-codex#completion-contract-architecture]], [[sources/openai--using-goals-in-codex#event-driven-continuation]]).
- **Evidence over confidence.** Completion is defined as an audit against concrete artifacts, never the model's self-assessment ([[sources/openai--using-goals-in-codex#evidence-based-completion]]).
- **Documentation that scopes itself.** The Goals guide tells you when *not* to use the feature and grades research output by epistemic level (confirmed / approximate / blocked / uncertain) rather than flattening to "done" ([[sources/openai--using-goals-in-codex#when-not-to-use]], [[sources/openai--using-goals-in-codex#epistemic-levels]]).

## Source citations

- [[sources/openai--using-goals-in-codex#root]] — the Codex Goals cookbook guide (authors Raj Pathak, Stefano Fabbri; published 2026-05-09; notebook commit `9b4e627`).
- [[sources/openai--using-goals-in-codex#lifecycle-commands]] — Codex CLI version (0.128.0) + install channels (npm / Homebrew).
- [[sources/openai--using-goals-in-codex#completion-contract-architecture]] — the "completion contract" framing.

## Open questions / what to study next

- **The rest of the Codex CLI** — model, sandboxing, approval model, tool surface. One full ingest would let us compare Codex vs. Claude Code head-to-head.
- **Does OpenAI name patterns the way Anthropic/Garry do?** One source isn't enough to read a house vocabulary. More cookbook ingests would tell us whether "completion contract" is an OpenAI coinage or field-wide.
- **The OpenAI Cookbook as a source vein** — it's a large, first-party, repo-backed library of agent/AI guides; likely a rich future ingest target (it's how we found this one).
