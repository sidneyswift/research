---
domain: patterns
type: pattern
name: session-start-directive
category: behavioral
status: proposed
last-reviewed: 2026-06-11
example-count: 1
---

# session-start-directive

> A session-start hook that injects an **imperative, position-pinned instruction** ("your FIRST
> user-facing action MUST be…") instead of passive context ("consider running /tidy") — because
> passive hook payloads get silently absorbed as background context and never surface.

*Done when it passes the [page checklist](_definition-of-done.md).*

## Longer definition

Hooks can add context at session start, but context is not behavior: an LLM treats "consider X" as
one more fact and routinely proceeds without acting on it. The pattern upgrades the payload to a
directive with three properties: (1) **imperative voice** with an explicit position in the response
("first user-facing action"), (2) a **verbatim script** for what to say (down to the exact question
and y/n form), and (3) **bounded persistence** ("if the user declines, acknowledge briefly and
proceed — do NOT loop or re-offer"). A sibling discipline arbitrates between multiple hooks: only
one directive may fire per session, since two competing "FIRST action" instructions recreate the
original failure.

## Mechanism

PM OS's `tidy-reminder.sh` detects drift deterministically (orphan files, staleness >12h, modified
files since last run), then emits JSON `additional_context` beginning `[SESSION-START DIRECTIVE —
/tidy drift]`, containing: the exact question to ask, the skill file to read if accepted, and the
no-loop rule if declined. The hook's comment block documents the *evidence* for the pattern:
passive phrasing "was being silently absorbed by the LLM as background context" (gnurio/pm-os
issue #8; fix shipped in PR #10). `drip-reminder.sh` then implements the arbitration rule: it
re-runs tidy's detection logic first and stays silent if tidy would fire — "only one nudge
directive per session." Hooks read state but never write it ("the hook never mutates state" — a
single designated script owns each state file).

## When to use

- Maintenance actions that decay silently (index sync, cleanup, memory filing) and need the *user's*
  consent, not just the agent's awareness.
- Any hook payload you've observed the model "knowing about" but not acting on.

## When NOT to use

- Information that genuinely is background context — directive-izing everything turns session start
  into a wall of competing imperatives (the arbitration rule exists precisely because even two is
  too many).
- Actions the agent can safely take without asking — then just do the work in the hook itself
  (deterministically) instead of directing the model to ask.

## Why it works

Instruction-following pressure is strongest for imperative, position-anchored, verbatim-scripted
text; declarative facts compete with the user's actual message for salience and lose. Bounding the
persistence ("don't re-offer") prevents the opposite failure — the directive hijacking the whole
session. This is the hook-layer cousin of why harnesses pin critical rules at fixed positions in
system prompts.

## Detection recipe

- **Look for**: SessionStart/session-start hooks emitting `additional_context` (or equivalent) with
  imperative phrasing, an explicit "first action" position claim, and a scripted question.
- **Confirm with**: a documented or implied contrast with passive phrasing; a single-directive
  arbitration rule if multiple hooks exist.
- **Rule out**: hooks that *perform* the action themselves (that's deterministic automation, not a
  directive); hooks that merely add facts ("the repo has 3 stale branches") — that's the baseline
  this pattern replaces.

## Examples in this wiki

- [[artifacts/plugins/pm-os]] — `tidy-reminder.sh` + `drip-reminder.sh`: imperative
  `[SESSION-START DIRECTIVE]` payloads, verbatim y/n script, no-loop bound, drip-defers-to-tidy
  arbitration, and an in-comment citation of the passive-phrasing failure (issue #8 / PR #10). —
  citation: [[sources/prodmgmt-world--pm-os-cowork#tidy-reminder]], [[sources/prodmgmt-world--pm-os-cowork#drip-reminder]], [[sources/prodmgmt-world--pm-os-cowork#hooks.json]]

*Status `proposed` — one artifact, one creator. Promotion candidates: any future ingest with
session hooks (check whether gstack/gbrain's hook layer or FSI's marketplace hooks phrase payloads
imperatively or passively; the passive ones double as counter-examples).*

## Counter-examples or anti-pattern

- **The documented baseline**: PM OS's own earlier passive phrasing ("Consider running /tidy") —
  absorbed silently, never surfaced; preserved as a comment in the shipped hook. The rare case of an
  artifact carrying its own before/after evidence. — citation: [[sources/prodmgmt-world--pm-os-cowork#tidy-reminder]]
- **Anti-pattern to watch**: multiple unarbitrated directives — two hooks each demanding "FIRST
  user-facing action" — which PM OS explicitly engineers against.

## Related patterns

- [[patterns/behavioral/latent-vs-deterministic-split]] — detection is fully deterministic (file
  counts, timestamps); only the *ask* is delegated to the latent layer, with state writes reserved
  to a single deterministic owner.
- [[patterns/quality-bar/complexity-ratchet]] — the hook exists to stop silent decay of the
  workspace's organized state; same forward-only instinct at the user-workspace layer.

## Open questions

- Does the directive's force degrade as harnesses get better at acting on passive hook context?
  (The pattern may be a 2026-era workaround.)
- Cowork reportedly may not surface SessionStart hooks visibly ([[sources/prodmgmt-world--pm-os-cowork#readme]])
  — what's the graceful-degradation story when the hook layer itself is unreliable?
