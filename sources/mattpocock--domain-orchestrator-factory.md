---
domain: sources
type: article
url: null
retrieved: 2026-11-04
published: unknown (relative timestamp in screenshot only)
snapshot-location: sources/mattpocock--domain-orchestrator-factory/
upstream-commit: n/a (screenshot of a proposed architecture)
last-reviewed: 2026-11-04
---

# Matt Pocock — local domain orchestrator plus software factory

> A proposed combination: a local, long-running, domain-specific orchestrator converses with the human and manages a software factory through its CLI; sandboxed workers handle implementation and exploration.

## Snapshot details

- **Received:** 2026-11-04 as a supplied screenshot of a public X post.
- **Visible attribution:** Matt Pocock / `@mattpocockuk`; linked to the existing [[creators/matt-pocock]] page. The GitHub handle on that page is a different platform identifier.
- **Raw evidence:** [screenshot.jpg](mattpocock--domain-orchestrator-factory/screenshot.jpg), [snapshot.md](mattpocock--domain-orchestrator-factory/snapshot.md) with a visible-text transcription, and [asset.json](mattpocock--domain-orchestrator-factory/asset.json) with byte count and SHA-256. No EXIF fields present.
- **Canonical URL / publication date:** unavailable. The screenshot shows only `15h`; its capture time is unknown. A bounded exact-phrase public search did not recover the post. Receipt date is not publication date.
- **Evidence class:** proposal. The author says he is considering a trial. No implementation, completed trial, performance evaluation, sandbox configuration or CLI contract is shown.
- **Named but not inspected:** `/chief-of-staff` is a possible orchestrator skill. The factory is not identified as a particular product. Neither was installed, run or independently investigated in this ingest.

## Anchor map

- `#root` — supplied screenshot and full visible-post transcription.
- `#proposal-status` — `snapshot.md`, opening and closing sentences: considering a trial and expressing optimism, not reporting demonstrated success.
- `#domain-orchestrator` — first bullet: local, long-running orchestrator thread for one domain, possibly using `/chief-of-staff`.
- `#sandboxed-factory` — second bullet: attachment to a software factory with sandboxed implementers and exploration.
- `#cli-control` — paragraph following the bullets: orchestrator communicates with the factory through the CLI and manages threads.
- `#operating-loop` — same paragraph: retrospectives and building up cron jobs are proposed responsibilities.
- `#human-interface` — same paragraph: the human communicates in plain language.
- `#traction` — visible screenshot metrics: 116 replies, 12 reposts, 434 likes, 56K views; actual observation time unknown.
- `#provenance-limits` — no original URL, absolute timestamp, named factory implementation, skill files or trial evidence visible.

## Why we cite this

Adds a domain-scoped variant to [[concepts/agent-control-plane]] and a comparison to [[concepts/super-agent-architecture]]. The distinctive bundle is local continuity + one domain + CLI-managed sandboxed workers + retrospectives/recurring work + a plain-language human interface. It is not evidence that a long-running thread provides crash recovery or that an unspecified sandbox enforces a particular permission boundary.

## Popularity signals (if this source provides them)

- **Signal type:** visible screenshot metrics.
- **Value:** 434 likes and 56K views; full visible counts at `#traction`.
- **As-of:** screenshot received 2026-11-04; capture time unknown. Indicates attention, not measured architecture quality.

## Related sources

- [[sources/mattpocock--skills]] — separately investigated, pinned skills pack. This post does not update its inventory or establish where `/chief-of-staff` is distributed.
- [[sources/humanlayer--humanlayer]] — implemented task/session/host separation; useful contrast to this proposal's unspecified persistence and worker contracts.
- [[sources/deepseek--super-agent-design]] — continuous routing and worker architecture; different scope and coordinator responsibilities.
