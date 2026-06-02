---
domain: artifacts
type: skill
name: # kebab-case skill name (matches the SKILL.md `name:` field)
creator: # [[creators/anthropic]] or [[creators/individual--handle]]
source: # [[sources/<creator>--<repo>]] — the cloned snapshot
ecosystem: # claude-code | claude-general | both
discovered-via: # how we heard about it — official-docs | marketplace | tweet | reddit | colleague | other
status: # active | deprecated | community-fork | archived
last-reviewed: # YYYY-MM-DD
popularity-signals:
  # - signal: official-anthropic   # one of: official-anthropic | install-count | github-stars | marketplace-rank | quoted-by | tweet-traction
  #   value: # raw number or text
  #   as-of: YYYY-MM-DD
  #   source: # [[sources/...#anchor]]
---

# {skill-name}

> **One-line:** what this skill does in plain English.

## Attributes

- **What it does**: 1–3 sentences. Behavioral, not just descriptive.
- **Trigger conditions**: the literal phrasing the skill uses to anchor itself — copy the `description:` field from SKILL.md verbatim.
- **Bundled resources**: which of `scripts/`, `references/`, `assets/`, sub-skills it ships with. Quantify (e.g., "12 reference files totalling ~4k lines").
- **SKILL.md size**: lines / approximate tokens.
- **Progressive disclosure depth**: how many levels of file-loading before the model has full context (SKILL.md → referenced files → sub-references)?
- **External dependencies**: MCP servers required, CLI tools assumed, network access needed.
- **License**: MIT / Apache / proprietary / unclear.

## Relationships

- **Creator**: [[creators/...]]
- **Source**: [[sources/...#root]]
- **Depends on**: [[artifacts/mcp-servers/...]], external CLIs, etc.
- **Composes with**: [[artifacts/skills/...]] — skills it explicitly invokes or pairs with
- **Inspired-by / forked-from**: [[artifacts/skills/...]] if applicable

## What problem it solves

2–4 sentences. The user-facing job-to-be-done, not the technical mechanism. If you can't state the problem crisply, the skill probably doesn't either — note that.

## How it works (mechanism)

The actual approach the SKILL.md takes — workflow steps, decision trees, how it uses its bundled resources, how it handles edge cases. Cite specific lines from the source clone.

## Patterns demonstrated

- [[patterns/structural/...]] — *how this skill uses the pattern*, with citation to specific lines
- [[patterns/behavioral/...]] — *how this skill uses the pattern*, with citation to specific lines

(Mandatory section. If empty, the deep-dive is incomplete.)

## Source citations

Bullet list of every non-obvious claim above with its `[[sources/...#anchor]]`.

## What makes it great

2–6 sentences. Specific. Not "it's well-written" — *what* is well-written, and what would have been the lazy alternative?

## What we'd steal

Bulleted, concrete. Each bullet should be something we could actually port to a skill we build. "Use a top-of-file decision table" not "be organized."

## Open questions / what's unclear

Things we'd want to ask the creator or test ourselves before copying.
