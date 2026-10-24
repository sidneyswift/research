---
domain: patterns
type: pattern
name: persona-lens-review-panel
category: behavioral
status: confirmed
last-reviewed: 2026-06-11
example-count: 3
---

# persona-lens-review-panel

> Review a document or diff by fanning it out to multiple narrow **persona/lens reviewers** (each
> with one stake: engineering, design, security, devil's advocate…), each returning a structured
> report, which an orchestrator merges into one decision-ready review.

*Done when it passes the [page checklist](_definition-of-done.md).*

## Longer definition

Instead of one "review this" pass — where the model averages all concerns into mush — the work is
split into named lenses, each defined as its own agent/skill file with a tight persona, an explicit
scope of concerns, and (in the strongest examples) a constrained read surface and a fixed output
contract. The orchestrator selects the relevant lenses, runs them (in parallel where the harness
supports subagents), then merges, dedups, and severity-ranks the findings. The persona is not
decoration: it licenses *partiality* — a devil's advocate is allowed to only attack, an optimist
only to find strengths — which surfaces findings a balanced single pass suppresses.

## Mechanism

1. Each lens is one file (`agents/<lens>.md` or a skill) with: persona framing, the 3–6 concern
   areas it owns, and example challenge phrasings.
2. Lenses are **read-only**: they return findings, never edit the artifact (PM OS marks them
   `readonly: true`; CE's reviewers return JSON to the orchestrator).
3. A workflow step enumerates which lenses fire for which document type (CE selects dynamically;
   PM OS's `/prd` fixes a 2-persona + 7-cross-functional roster; gstack makes each lens its own
   slash command).
4. Output is a **fixed structure** so reports merge mechanically — CE: JSON → merge/dedup →
   confidence gate; PM OS: `STATUS / SCOPE / FINDINGS (severity-ranked) / OPEN_QUESTIONS /
   RECOMMENDED_NEXT_ACTION` shared across all 9 reviewers.
5. Portability fallback: if the harness can't spawn subagents, run each persona **inline** from the
   same persona file (PM OS states this explicitly).

## When to use

- High-stakes documents/diffs where missed objections are expensive (PRDs, launch plans, security-relevant code).
- When a single review pass keeps producing bland "looks good, minor nits" output.
- When different stakeholders genuinely evaluate the artifact differently (exec vs. legal vs. UX).

## When NOT to use

- Low-stakes or short artifacts — N subagent passes cost N× tokens/time for marginal lift.
- When lenses can't be given genuinely distinct concerns — two overlapping personas produce
  duplicate findings the merge step must clean up.
- When no structured output contract exists yet — without it the orchestrator gets N essays it
  can't merge, which is worse than one essay.

## Why it works

LLMs regress to balanced, agreeable output when asked to "review"; a persona with permission to be
partial shifts the sampling distribution toward that persona's failure-finding mode. Narrow scope
also keeps each context window small and the instruction pressure high (one file = one job — same
force behind [[patterns/structural/thin-harness-fat-skills]]'s fat-skill decomposition). Structured
returns make the fan-in deterministic rather than another judgment call.

## Detection recipe

- **Look for**: multiple `agents/*reviewer*.md` (or `*-review` skills) whose frontmatter/prose names
  a role or stake; an orchestrating workflow step listing several of them; a shared output template.
- **Confirm with**: lenses are read-only and partial by design (an "only flaws" or "only strengths"
  lens is the strongest tell); findings are merged by a parent, not appended verbatim.
- **Rule out**: a single reviewer prompt with a list of concern *categories* (one pass, no fan-out);
  or multi-agent *research* (the workers gather facts rather than judge an artifact — that's closer
  to CE's researcher agents).

## Examples in this wiki

- [[artifacts/plugins/pm-os]] — **the fixed-roster, contract-first example (3rd creator).** `/prd`
  Steps 7–8 dispatch 9 read-only reviewers: 2 PRD-specific personas (`prd-strengths-reviewer`
  optimist + `prd-flaws-reviewer` critic) and 7 cross-functional lenses (engineering, design,
  executive, legal-risk, UX-research, devil's advocate, customer voice). Every agent file carries
  `readonly: true`, an allowed-reads list, and the shared `STATUS/SCOPE/FINDINGS/…` contract; the
  workflow ships an explicit inline-persona fallback for harnesses without subagent dispatch. —
  citation: [[sources/prodmgmt-world--pm-os-cowork#prd-workflow]], [[sources/prodmgmt-world--pm-os-cowork#reviewer-agents]]
- [[artifacts/plugins/compound-engineering]] — **the dynamic-selection + JSON-merge example.**
  `/ce-code-review` selects reviewer personas per diff (tiered lenses ×43 incl. named-expert
  personas like `ce-julik-frontend-races-reviewer`), spawns them in parallel, gets structured JSON
  back, merges/dedups into a confidence-gated report. — citation: [[sources/every--compound-engineering-plugin#ce-code-review]], [[sources/every--compound-engineering-plugin#agents]]
- [[artifacts/plugins/gstack]] — **the lens-as-slash-command example.** The plan-review family
  (`/plan-ceo-review`, `/plan-eng-review`, `/plan-design-review`, `/plan-devex-review`) plus `/qa`
  and `/cso` give each persona its own invocable skill; the user composes the panel manually rather
  than via an orchestrator. — citation: [[sources/garrytan--gstack#plan-ceo-review]], [[sources/garrytan--gstack#qa]], [[sources/garrytan--gstack#cso]]

Three creators (prodmgmt.world, Every, Garry Tan) across three verticals (PM docs, code review,
plan review) — confirmed at creation (2026-06-11); previously tracked as a proposed pattern on
[[artifacts/plugins/compound-engineering]].

## Counter-examples or anti-pattern

- A monolithic "review checklist" prompt — the same concern list crammed into one pass — is the
  baseline this pattern beats; it produces averaged, conflict-free output (the exact failure the
  optimist/critic split in PM OS's Step 7 is designed to break).
- **Panel bloat**: 9+ lenses on a one-page doc inverts the cost/benefit; PM OS partially mitigates
  by making Step 8's cross-functional pass follow only after Step 7's PRD-specific pass.

## Related patterns

- [[patterns/behavioral/diarization]] — both transform raw material via judgment passes; here the
  judgment is parallelized and partial by design.
- [[patterns/behavioral/latent-vs-deterministic-split]] — the lens reports are latent; the merge
  works best when the return format makes fan-in deterministic.
- [[patterns/composition/resolver-routing-table]] — lens *selection* (which reviewers fire for which
  doc type) is a routing decision; CE does it dynamically, PM OS by fixed table.
- **generator–verifier separation** *(proposed cousin)* — this panel runs *parallel* personas over one
  artifact; the two-role variant has one actor **build** and a *different* actor **verify/approve**
  ("Use independent verification when the same actor should not both create and approve high-impact
  output"). [[artifacts/skills/loop-library]] has four in-source instances (Codex reviews Claude #019,
  a 2nd Claude session verifies #020, critic vs builder + `redteam.md` #024, revert-or-mutate
  proof-of-test #027 — [[sources/forward-future--loop-library#loop-019-clodex]], [[sources/forward-future--loop-library#loop-027-autonomy]]).
  Needs a 2nd wiki *artifact* to graduate to its own page (CE `/ce-code-review` and PM OS reviewers are candidates).

## Open questions

- Does persona framing measurably outperform concern-category framing? (Same question as gstack's
  persona naming — no one has shipped an eval.)
- Optimal panel size before findings saturate/duplicate — CE dedups, PM OS severity-ranks, neither
  publishes numbers.
