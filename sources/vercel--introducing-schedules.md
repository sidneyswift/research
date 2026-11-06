---
domain: sources
type: article
url: https://vercel.com/blog/introducing-vercel-schedules
retrieved: 2026-11-06
snapshot-location: sources/vercel--introducing-schedules/
last-reviewed: 2026-11-06
---

# Vercel — Introducing Vercel Schedules

> Announcement of runtime-managed recurring and one-time triggers, distinct from the application work they start.

## Snapshot details

- **Published:** 2026-11-04, per captured article. Authors: Elliot Dauber, Casey Gowrie, Mitul Shah, Nate Rajlich, Karthik Kalyanaraman and Colton Padden; contributor Ben Sabic.
- **Retrieved:** 2026-11-06. [Full readable article](vercel--introducing-schedules/snapshot.md), including both TypeScript/JSON examples; [byte/hash receipt](vercel--introducing-schedules/capture.json).
- **Read scope:** entire article text and examples. Official Markdown extraction; web browser tool failed but readable primary-source fetch succeeded. No media playback or visual-only content inspection claimed.
- **Linked context:** seventeen separately preserved documents/resources in [[sources/vercel--schedules-docs]], with [coverage and unvisited-link inventory](vercel--schedules-docs/coverage.json). Not every navigation/integration link was independently read. Source code examples were not executed.

## Anchor map

### root

Complete [announcement](vercel--introducing-schedules/snapshot.md). Public-beta product framing, not performance or reliability evidence from this ingest.

### static-dynamic

Static configuration syncs on deployment; runtime-managed schedules avoid redeployment and target queue topics. See “What are Vercel Schedules?” in the capture.

### agent-example

The AI SDK example captures tenant/user identity in the tool closure, accepts task/time/timezone and creates a queue schedule. The receiving app checks the user's **current permissions** before starting the agent; the saved task is not a permanent authorization grant. Random names in the example do not establish retry-safe creation.

### private-target

Recurring cleanup uses `function: api/cleanup`, `schedule/v1beta`, an IANA timezone and no public URL. The application still supplies executable work.

### integrations

Article points to experimental eve/Nitro support and suggests equivalent tools for libfx/Pi. Only eve's dynamic-scheduling document was deeply read; no compatibility test is claimed for any integration.

## Why we cite this

Motivates [[artifacts/projects/vercel-schedules]]: turn future intent into an inspectable scheduling resource, then treat delivery, authorization and business completion as separate contracts.

## Popularity signals

Official Vercel engineering announcement; no independent adoption, latency or reliability metric captured. The separate changelog is dated November 5, one day after the article; preserve both dates rather than inventing a single precise launch timestamp.

## Related sources

- [[sources/vercel--schedules-docs]] — current beta contracts and documented disagreements.
- [[sources/vercel--eve]] — older pinned eve research; later docs supplement does not rewrite historical implementation claims.
