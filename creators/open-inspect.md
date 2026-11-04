---
domain: creators
type: org
name: Open Inspect
handle: open-inspect
url: https://github.com/open-inspect
last-reviewed: 2026-11-04
---

# Open Inspect

> Maintainers of an open-source background coding-agent system, with a durable session control plane and provider-managed sandboxes.

## Attributes

- **Ships:** the MIT `background-agents` monorepo; clients/integrations, control-plane lifecycle and a multi-harness sandbox runtime. The README attributes inspiration to Ramp's Inspect; this does not establish organizational affiliation. [[sources/open-inspect--background-agents#root]] [[sources/open-inspect--background-agents#harness]]
- **Distribution:** public GitHub source and self-hosting documentation. GitHub API recorded 3,453 stars / 504 forks on 2026-11-04, not a user count. [[sources/open-inspect--background-agents]]
- **Scope:** explicitly single-tenant trusted-organization deployment; Teams do not promise hostile-tenant isolation. [[sources/open-inspect--background-agents#authority]]

## Artifacts produced

### Projects

- [[artifacts/projects/background-agents]] — 43 portable principles; lifecycle, authority, skills, memory, automation and export investigation.

## Design philosophy

The inspected ADRs favor one owner per lifecycle responsibility, canonical state over a redundant view log, explicit recovery uncertainty and bounded abstractions. Managed skills/context are versioned; authority is checked separately. These are observations from this source, not a claim that every subsystem follows them perfectly. [[sources/open-inspect--background-agents#shutdown-design]] [[sources/open-inspect--background-agents#snapshot-handoff]] [[sources/open-inspect--background-agents#skills-pinning]]

## Timeline

- 2026-11-04 — Source-investigated at `4b7f4e4`; complete pinned tracked tree preserved locally, selected architecture/code/test evidence indexed. [[sources/open-inspect--background-agents]]

## Source citations

- [[sources/open-inspect--background-agents#root]]
- [[sources/open-inspect--background-agents#shutdown-design]]
