---
domain: sources
type: docs-page
url: https://frontier.replit.com/agent-habitat-architecture/
retrieved: 2026-11-06
snapshot-location: sources/replit--agent-habitat-architecture/
last-reviewed: 2026-11-06
---

# Replit — Agent Habitat Architecture

> A proposed reference architecture and eleven-track maturity rubric for agent identity, authority, isolation, recovery and containment.

## Snapshot details

- **Upstream:** https://frontier.replit.com/agent-habitat-architecture/
- **Version:** n/a (living white paper); captured 2026-11-06 01:51:07 UTC. No product build or standards release is established.
- **Evidence:** [snapshot.md](replit--agent-habitat-architecture/snapshot.md), [SHA-256/byte receipt](replit--agent-habitat-architecture/capture.json).
- **Reviewed:** full extracted text, component responsibilities, twelve core principles and eleven maturity tracks with their evidence requirements. Tables are flattened by readable extraction, figure captions retained but diagram pixels not captured; direct HTML fetch returned 403. Illustrative incident/vendor links inside this white paper were not exhaustively followed. The article's immediate references have separate dated captures.
- **Classification:** authored proposal, not a deployed Replit implementation, independent audit, accepted industry standard or validated risk score. Vendor exemplars and level-to-threat-class claims remain the author's assertions.

## Anchor map

### root

The full proposed architecture, scope and maturity rubric. See the captured [summary section](replit--agent-habitat-architecture/snapshot.md#summary).

### scope

Threats include hostile content, model behavior, tenants, dependencies, enforcement flaws and crashes. Model training, generated-app security, content safety and enterprise discovery are out of scope. See the captured [scope section](replit--agent-habitat-architecture/snapshot.md#scope).

### components

Trusted bootstrapper, durable executor, token service and broker; semi-trusted harness; untrusted sandbox. Identity issuance grants no authority. See the captured [components section](replit--agent-habitat-architecture/snapshot.md#components).

### ceiling

Static principal/org/trigger-scoped run ceiling; pre-run checks; default deny; policy outside writable agent state; compute/network/spend budgets. See the captured [core-principles section](replit--agent-habitat-architecture/snapshot.md#core-principles).

### attenuation

Permissions narrow monotonically; subagents derive from current parent token; revocation is separate. Human escalation wording must be reconciled with the prohibition on mid-run ceiling increases. See the captured [core-principles section](replit--agent-habitat-architecture/snapshot.md#core-principles).

### filters

Gate sees trigger and proposed action, monitor sees history; both deny/escalate, never grant. Exact history constraints become policy; unavailable controls fail closed. See the captured [core-principles section](replit--agent-habitat-architecture/snapshot.md#core-principles).

### identity

Attested short-lived workload identity and lineage; trigger provenance separate from identity; public triggers inherit least-trusted initiator authority. See the captured [core-principles section](replit--agent-habitat-architecture/snapshot.md#core-principles).

### persistent-input

Agent-written files remain untrusted across runs; instruction/config/hook changes require review or quarantine in this proposal. See the captured [core-principles section](replit--agent-habitat-architecture/snapshot.md#core-principles).

### isolation

Separate component boundaries; enforcement outside sandbox kernel; independent layers and every network path including ingress, DNS, metadata, IPv6 and provider-hosted tools. See the captured [core-principles section](replit--agent-habitat-architecture/snapshot.md#core-principles).

### broker

Per-request credential injection; reject caller-supplied credentials; workload/trigger binding; revocation checks; vault/redact newly returned credentials. See the captured [core-principles section](replit--agent-habitat-architecture/snapshot.md#core-principles).

### data-flow

Provenance labels across contexts/files/subagents, confidential data and output destinations, optional Rule of Two, model APIs and UI renderers as egress. See the captured [core-principles section](replit--agent-habitat-architecture/snapshot.md#core-principles).

### approval

Trusted actual-action display, authenticated separate approval, action binding; production proposal separated from privileged apply. See the captured [core-principles section](replit--agent-habitat-architecture/snapshot.md#core-principles).

### supply-chain

Brokered registries, release-age/known-malicious checks, pins, MCP/config change review, installations without service credentials. See the captured [core-principles section](replit--agent-habitat-architecture/snapshot.md#core-principles).

### durability

Journal model calls and effects before/after; idempotency or reconciliation; recorded model replay; preserve attenuations, spent budgets and used approvals on resume. See the captured [core-principles section](replit--agent-habitat-architecture/snapshot.md#core-principles).

### containment

Out-of-band stop, freeze and revocation including downstream delegations; new authorized trigger for resumption; containment drills and latency evidence. See the captured [core-principles section](replit--agent-habitat-architecture/snapshot.md#core-principles).

### audit

Enforcement-point, off-host tamper-evident records tied to identity/trigger/policy/build, with secret exclusion and residency/retention boundaries. See the captured [core-principles section](replit--agent-habitat-architecture/snapshot.md#core-principles).

### maturity

Eleven 0–3 tracks, evidence criteria, lowest-track aggregate and named examples. Author-designed evaluation heuristic, not empirical security ranking. See the captured [agent-habitat-maturity-scale section](replit--agent-habitat-architecture/snapshot.md#agent-habitat-maturity-scale).

## Why we cite this

Provides the named proposal compiled in [[concepts/agent-habitat-architecture]]. Identity, custody, authorization, recovery and effect revocation are separately testable contracts; this text does not supply execution evidence for any vendor.

## Popularity signals

No independent adoption or validated maturity-score signal captured. Replit publication and the linked Chávez article establish provenance and attention, not effectiveness.

## Related sources

- [[sources/lhchavez--managed-agent-environments]] — argument and incident/survey evidence motivating this proposal.
