---
domain: patterns
type: pattern
name: # short, memorable, reusable-in-conversation (e.g., "progressive-disclosure", "trigger-anchor-phrasing")
category: # structural | behavioral | composition | quality-bar
status: # confirmed | proposed | disputed
last-reviewed: # YYYY-MM-DD
example-count: # integer — must be ≥2 to be `confirmed`, else `proposed`
---

# {pattern-name}

> **Short definition** (≤2 sentences). If a teammate reads only this, they should understand the pattern well enough to spot it in a new artifact.

## Longer definition

3–6 sentences. The shape of the pattern, what it operates on, what it produces, and why a creator would reach for it.

## Mechanism

How the pattern works in practice. Concrete. If the pattern is "progressive disclosure," explain: SKILL.md is short and self-contained → it references files in `references/` → those files are only loaded when the model needs them → ... This section should be specific enough that someone could implement the pattern from this description alone.

## When to use

Bullets — concrete situations where this pattern earns its keep.

## When NOT to use

Bullets — situations where this pattern is overkill, premature, or actively harmful. This section is mandatory and is the actual test of whether the pattern is well-understood.

## Why it works

The underlying principle — usually a constraint of LLMs, a property of how Claude Code loads context, a property of how users interact with agents, or a property of how the artifact gets installed/discovered. Reference primary sources where possible (Anthropic docs, MCP spec, published research).

## Detection recipe

A falsifiable test for spotting this pattern in a *new* artifact — the pattern's analogue of a skill's eval (see [[patterns/quality-bar/skill-pack-bundle]]: "a skill isn't done until it ships with tests"). Make it concrete enough to apply without re-reading the whole page:

- **Look for**: the observable tells (file names, frontmatter keys, structural shapes, phrasing) that indicate the pattern is present.
- **Confirm with**: what must be true for it to really be this pattern and not a look-alike.
- **Rule out**: the nearest neighbor it's most often confused with, and the distinguishing question.

The `## Examples` below are the positive fixtures; the `## Counter-examples` are the negative test.

## Examples in this wiki

At least 2 required. Each entry must cite specific source lines:

- [[artifacts/skills/X]] — *one-line description of how X uses the pattern* — citation: [[sources/...#anchor]]
- [[artifacts/skills/Y]] — *one-line description of how Y uses the pattern* — citation: [[sources/...#anchor]]
- [[artifacts/plugins/Z]] — *one-line description of how Z uses the pattern* — citation: [[sources/...#anchor]]

## Counter-examples or anti-pattern

Where this pattern was misapplied, or an artifact that *could* have used it but chose differently — and what we learn from that choice. Also mandatory.

- [[artifacts/...]] — *what they did instead and why it's worth noting*

## Related patterns

- [[patterns/.../...]] — relationship (composes-with / opposite-of / supersedes / specializes)

## Open questions

What we're still unsure about. Edge cases. Things that would change our confidence in calling this a "pattern."
