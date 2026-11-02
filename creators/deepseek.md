---
domain: creators
type: org
name: DeepSeek
handle: deepseek-ai / DeepSeekHarness
url: https://github.com/deepseek-ai
last-reviewed: 2026-11-02
---

# DeepSeek — Harness team

> Team behind the super-agent design essay and companion research prototype studied here; this page does not catalog all DeepSeek models or products.

## Attributes

The essay credits Yujia Qiao with implementation and authorship and names team reviewers. It frames agent concurrency as a human-attention problem and applies classic systems techniques. The public repository is explicitly a research prototype, not an official product or an identical internal-system release. [[sources/deepseek--super-agent-design#root]], [[sources/deepseek-ai--dsh-superagent-prototype#root]]

## Artifacts produced

- [[artifacts/projects/dsh-superagent-prototype]] — team agent control plane for GitHub and optional Feishu. [[sources/deepseek-ai--dsh-superagent-prototype#root]]
- [[concepts/super-agent-architecture]] — essay-derived architecture concept. [[sources/deepseek--super-agent-design#root]]

## Design philosophy

Minimize human attention while producing useful work; keep global coordination separate from isolated task execution; turn deterministic event operations into fast paths. Prototype defaults favor observation before autonomous admission. [[sources/deepseek-ai--dsh-superagent-prototype#philosophy]], [[sources/deepseek-ai--dsh-superagent-prototype#policy]], [[sources/deepseek--super-agent-design#triggers]]

## Timeline

- 2026-10-31 — Companion prototype's pinned Git commit. [[sources/deepseek-ai--dsh-superagent-prototype]]
- 2026-11-01 — Super-agent design essay published. [[sources/deepseek--super-agent-design]]
- 2026-11-02 — Essay/figures captured and selected repository paths investigated in this wiki.

## Related

[[creators/kody-hq]] provides a complementary infrastructure study, not an asserted partnership: [[artifacts/projects/kody]] addresses portable capabilities, state and credential use. [[sources/kody-hq--kody#intent]]
