---
domain: _schemas
type: shared-rules
last-reviewed: 2026-06-02
---

# Definition of Done — page checklists

The page analogue of Garry Tan's 10-step "skillify" checklist (per [[patterns/quality-bar/skill-pack-bundle]]: *"a feature that doesn't pass all ten is not a skill"*). A page that doesn't pass its checklist below is **not done** — it's a draft that happens to render.

This is an underscore-prefixed shared-rules file (gbrain's `_brain-filing-rules.md` convention): every page-type schema references it instead of copying the checklist, so the gate lives in one place. LINT enforces it (required-section checks #3, reachability #15).

## Source page (`source.md`)

- [ ] Snapshot captured — repo cloned (`.git` kept) + git-ignored + a row in `repos.manifest.tsv`; **or** article/paper/docs committed to `snapshot.md`.
- [ ] Frontmatter complete: `type`, `url`, `retrieved`, version stamp (commit SHA *or* publish date).
- [ ] `## Anchor map` defines every anchor that wiki pages will cite (no inventing anchors later).
- [ ] Popularity/credibility signals captured with an `as-of` date.
- [ ] Listed in `index.md` Sources table.

## Artifact page (`skill.md` / `plugin.md` / `mcp-server.md` / `project.md`)

- [ ] `## Attributes` and `## Relationships` filled.
- [ ] Every non-obvious claim cites `[[sources/...#anchor]]`.
- [ ] `## Patterns demonstrated` non-empty (or an explicit "none yet, because…").
- [ ] `## What we'd steal` is the **exhaustive ledger**, ★-marking the best (never a curated top-3).
- [ ] Creator page, domain `_index.md`, and `index.md` updated; **every entity the source touches** propagated (INGEST step 5).
- [ ] Reads as a judgment distillation, not a transcription of the README.

## Concept page (`concept.md`)

- [ ] `## What it is`, `## Where it came from`, `## Why it matters` filled.
- [ ] Claims cited; `## Tensions & counter-arguments` present (the other side of the debate).
- [ ] `## Patterns demonstrated` + `## What we'd steal` (exhaustive).
- [ ] Listed in `index.md` Concepts section.

## Pattern page (`pattern.md`)

- [ ] ≥2 `## Examples in this wiki`, each citing specific source lines (else `status: proposed`).
- [ ] `## Detection recipe` filled (look-for / confirm-with / rule-out).
- [ ] `## Counter-examples or anti-pattern` and `## When NOT to use` filled.
- [ ] `status` + `example-count` frontmatter match reality.

## If blocked (any page type)

The completion contract's *negative* half ([[concepts/completion-contract]] / [[patterns/behavioral/evidence-gated-completion]]): a page you **can't** honestly finish is **not done** — and must not be dressed up to look done.

- [ ] **Can't verify a claim / a needed source anchor is missing / a signal won't fetch?** Mark the gap *inline* (`TODO`, "unknown", "unverified") **and** in the page's `## Open questions`, and note why in `log.md`. Don't silently drop the claim, and don't assert it anyway.
- [ ] **"Done" is decided by evidence, not confidence.** A page passes when a LINT / `scripts/wiki-doctor.py` pass over it is clean — not because it *reads* finished. Run the check; don't self-assess.
- [ ] **Out of budget/time ≠ done.** Stop, leave the gaps marked, and log what remains + what would unlock it (the blocked stop condition) — never a fake completion.
