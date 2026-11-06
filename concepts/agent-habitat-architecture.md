---
domain: concepts
type: concept
name: agent-habitat-architecture
creators: ["[[creators/luis-hector-chavez]]", "[[creators/replit]]"]
sources: ["[[sources/lhchavez--managed-agent-environments]]", "[[sources/replit--agent-habitat-architecture]]"]
status: emerging
last-reviewed: 2026-11-06
---

# agent-habitat-architecture

> Put execution, authority and containment behind controls the agent cannot rewrite; cloud location, hidden secrets and convincing logs are not substitutes for those boundaries.

## What it is

Agent Habitat is Replit's **proposed** organization-controlled environment for autonomous agents. It separates the untrusted execution workspace from identity issuance, permission ceilings, credential brokerage, durable execution and independent containment. Luis Héctor Chávez's advisory advocates managed cloud execution as the default because employee workstations often mix unrelated credentials, code and network access; the architecture names what must actually be enforced to earn that isolation. This is a reference design and a research-backed argument—not a shipped-system inspection, certification or measured local-versus-cloud breach-rate comparison. [[sources/lhchavez--managed-agent-environments#thesis]] [[sources/lhchavez--managed-agent-environments#execution-boundary]] [[sources/replit--agent-habitat-architecture#root]]

**Distinct role:** [[concepts/agent-control-plane]] organizes work and worker lifecycles; this page specifies a proposed security boundary around them. [[concepts/mcp-enterprise-managed-authorization]] handles identity/token flows, not all execution effects. [[patterns/behavioral/context-is-not-authority]] is the general pattern; Habitat is one multi-component application of it. No duplicate generic sandbox concept or new confirmed pattern is being created.

## Where it came from

Chávez published the advisory on 2026-11-03 and linked the Replit white paper. Both were captured on 2026-11-06. His captured profile identifies a Replit leadership affiliation; the recommendation has a vendor perspective. These security mechanisms predate this naming—we do not attribute least privilege, brokerage or durable workflows to this article's invention. [[sources/lhchavez--managed-agent-environments#root]] [[sources/replit--agent-habitat-architecture#root]]

## Why it matters

The security question is not merely where the model runs. It is **which process can read which data, which principal authorized the action, which independent component checks the actual effect, and what can still happen after containment**. A local extension calling a remote model can retain workstation authority; a cloud sandbox holding broad connected-account tokens can remain dangerous. The Manus case is a direct counterexample to cloud location as sufficient protection. [[sources/lhchavez--managed-agent-environments#execution-boundary]] [[sources/lhchavez--managed-agent-environments#cloud-counterexample]]

## Evidence & claims

### Adoption and controls: do not merge denominators

| Reported observation | Interpretation boundary |
| --- | --- |
| Stack Overflow: 70% → 76% → 84% using/planning AI tools, 2023–2025 | Not autonomous-agent adoption. The 2025 page separately says agents are not yet mainstream. |
| Salt customer telemetry: 16.7% → 21.6% MCP-related infrastructure, Jan–Aug 2026 | 4.9 percentage points in a vendor-observed population; no established representative/stable cohort. |
| Salt survey: 86.4% agent deployment, 17.5% automatic stopping, 12.5% full-path tracing; >380 respondents | Independent self-reported measures, not a funnel. 49.8% unintended-action figure includes both confirmed and suspected events—not a confirmed breach rate. |
| CSA: 47% agent-related incident, 54% 1–100 unsanctioned agents, 31% formal policy; 445 respondents | Sep–Nov 2025 survey, April 2026 release, funded/co-developed with Zenity; different population/questions from Salt. |

These establish reported adoption/control gaps, not a causal estimate of security outcomes or a validated purchasing recommendation. The original article already qualifies several of these measures; the linked releases preserve the sampling context. [[sources/lhchavez--managed-agent-environments#adoption]] [[sources/lhchavez--managed-agent-environments#supporting-evidence]]

### Incident and demonstration ledger

| Example | Portable lesson | Evidence class / limit |
| --- | --- | --- |
| Personal agent in sensitive DoD environment | Borrowed employee authority can bypass the intended workflow | WIRED allegation explicitly disputed by Accenture; no demonstrated classified-system compromise. |
| Tampered marketplace extension | Trust distribution provenance, not familiar branding | Cursor vendor notice and partial WIRED capture; not an official Anthropic release. Uninstall alone does not establish absence of persistence. |
| Nx s1ngularity | Dependency installers can recruit installed AI tools with the host's authority | Wiz investigation; incident counts attributed, not reproduced here. |
| GitHub MCP injection | Trusted tools and allowed domains can compose an unauthorized data flow | Invariant research demonstration: public issue → private read → public PR. Not a compromised MCP server. |
| CodeRabbit RuboCop | Every execution path must cross the intended sandbox boundary | Vendor-confirmed research disclosure; reports fix within twelve hours and no evidence of customer exploitation. |
| Manus email injection | A warning after execution is detection, not pre-action prevention | Salt research; connected service credentials accessible; flaw reported resolved. Cloud-hosted counterexample. |
| Binance signing/delegation | Custody of a secret does not constrain the operations signed with it | Elliptic analysis; initial compromise unresolved, AI involvement not established. Analogy, not an AI-agent incident count. |

The same advisory intentionally includes malware, prompt injection, sandbox escape-path mistakes and signing-authority misuse. These mechanisms should not be collapsed into one measured failure category. Primary researcher/vendor accounts support the technical comparisons; the disputed contractor report stays an allegation. [[sources/lhchavez--managed-agent-environments#incidents]] [[sources/lhchavez--managed-agent-environments#supporting-evidence]]

## Proposed architecture

| Component | Proposed trust and responsibility | What it does not establish |
| --- | --- | --- |
| Identity bootstrapper | Trusted attestation-based workload identity and lineage | Identity alone grants no permissions. |
| Harness | Semi-trusted model-output parser, holds only the run token | Cannot be the sole trusted boundary around arbitrary tools. |
| Token service | Trusted root, run ceiling and revocation list | An opaque token is not proof that every allowed effect is intended. |
| Durable executor | Trusted journal, retry/replay/reconciliation ownership | Journal persistence is not universal exactly-once external execution. |
| Sandbox | Untrusted tool/code execution with bounded mounts/network | A separate thread, working directory or cloud label is not isolation. |
| Broker | Trusted per-request policy and credential injection, all network directions | Credential secrecy alone does not prevent authorized-channel abuse. |

These are the white paper's proposed responsibilities, not components we inspected in deployed Replit code. The enforcement components are themselves attack surfaces; their correctness, independence and availability need evidence. [[sources/replit--agent-habitat-architecture#components]] [[sources/replit--agent-habitat-architecture#scope]]

### Authority calculation

The design intersects **run ceiling ∩ organization policy ∩ trigger policy ∩ accumulated attenuations ∩ filter decisions**. A subagent derives from the parent's *current* token, not its original maximum. Identity and trigger are separate: a public issue may arrive through an authenticated integration yet still carry an anonymous initiator's authority. Received content cannot promote itself into a new authorized trigger. [[sources/replit--agent-habitat-architecture#ceiling]] [[sources/replit--agent-habitat-architecture#attenuation]] [[sources/replit--agent-habitat-architecture#identity]]

The paper also permits exceptional human escalation while saying ceilings never increase mid-run. An implementation must resolve this explicitly—e.g. a newly authorized, re-verified policy version and well-defined transition—not silently reset the run's constraints. This is an unresolved specification boundary, not a demonstrated defect in deployed code. [[sources/replit--agent-habitat-architecture#attenuation]]

### Eleven-track maturity rubric

| Track | Evidence to request at the boundary |
| --- | --- |
| Sandbox isolation | Tested host/kernel/tenant separation, not just a container label |
| Network controls | Denied bypass paths, including DNS, direct IP, IPv6, metadata and inbound previews |
| External credential identity | Per-request brokerage, workload/trigger binding and rejection of foreign credentials |
| Policy | Static ceiling, monotonic narrowing, deny-only adaptive controls and fail-closed behavior |
| Data flow | Provenance and destination controls across context, files and subagents |
| Human approval | Trusted actual-action display, action binding and separate production apply |
| Supply chain | Approved/pinned inputs, change review and verified provenance |
| Durability | Side-effect reconciliation and restoration of limits, spent budgets and consumed approvals |
| Containment | Independent stop/revoke/freeze path with measured latency and drills |
| Observability | Off-host enforcement records tied to workload, trigger, policy and build |
| Workload identity | Attested short-lived identity and least-trusted-trigger attribution |

The source assigns levels 0–3 to each track and uses the lowest track as the overall level. That is an **author-proposed conservative assessment heuristic**, not an empirically calibrated score or formal certification. Preserve the evidence profile; do not advertise a level as proof of resistance to every prompt injection or escape. The paper's physical-host hierarchy and named vendor examples do not independently establish comparative risk. [[sources/replit--agent-habitat-architecture#maturity]]

## Patterns demonstrated

- [[patterns/behavioral/context-is-not-authority]] — content, identity and opaque credentials do not grant action-specific authority. Proposed specialization, not another independently tested implementation. [[sources/replit--agent-habitat-architecture#identity]] [[sources/lhchavez--managed-agent-environments#credential-authority]]
- [[patterns/behavioral/latent-vs-deterministic-split]] — adaptive judgments can deny/escalate beneath a machine-checkable ceiling; exact historical constraints become deterministic policy. [[sources/replit--agent-habitat-architecture#filters]]
- [[patterns/behavioral/evidence-gated-completion]] — maturity claims need boundary evidence; containment and successful recovery require different observations. [[sources/replit--agent-habitat-architecture#maturity]] [[sources/replit--agent-habitat-architecture#durability]]
- [[patterns/quality-bar/revision-bound-review]] — bind approvals/audits to actual action and policy/build revision; preserve consumed approvals across restart. [[sources/replit--agent-habitat-architecture#approval]] [[sources/replit--agent-habitat-architecture#audit]]

## Tensions & counter-arguments

1. **Placement versus controls.** Cloud centralization can make governance easier but also concentrates trust in brokers, issuers and operators. The cited evidence does not show all managed clouds outperform all controlled local/on-prem deployments. [[sources/lhchavez--managed-agent-environments#adoption-limits]] [[sources/replit--agent-habitat-architecture#scope]]
2. **Intent is not just authentication.** Even an attested agent can request a harmful but permitted action; signing authority and long-lived delegated effects require separate checks. [[sources/lhchavez--managed-agent-environments#signing-authority]] [[sources/lhchavez--managed-agent-environments#credential-authority]]
3. **Proposed mechanisms need implementation evidence.** Formal ceiling checks, complete mediation, response redaction and provenance tracking are hard obligations, not satisfied by naming a prover, broker or Rule of Two. Fail-closed semantics have availability costs. [[sources/replit--agent-habitat-architecture#ceiling]] [[sources/replit--agent-habitat-architecture#broker]] [[sources/replit--agent-habitat-architecture#data-flow]]
4. **Recovery preserves authority constraints as well as work.** Restarts must not refresh budgets or approvals. Destination idempotency is conditional; compensation is not atomic rollback, and unknown external outcomes require reconciliation. These limits are our synthesis of the proposed contract and existing [[concepts/durable-agent-execution]] evidence. [[sources/replit--agent-habitat-architecture#durability]]
5. **Detection, stopping and undoing differ.** Killing the runtime cannot retract leaked data or necessarily revoke a downstream grant already created. Migrating new work does not clean a compromised endpoint. [[sources/lhchavez--managed-agent-environments#containment]] [[sources/lhchavez--managed-agent-environments#adoption-limits]]
6. **Commercial and measurement limits.** Vendor reports, survey self-reports, disputed journalism and researcher demonstrations provide different evidence. No runtime benchmark or comparative breach-rate study was performed in this ingestion. [[sources/lhchavez--managed-agent-environments#supporting-evidence]]

## Timeline (append-only)

- 2026-11-03 — Chávez published the managed-environment advisory, linking Agent Habitat. [[sources/lhchavez--managed-agent-environments#root]]
- 2026-11-06 — Captured the article, all three images, twelve supporting references and the separate living white paper; compiled proposal/evidence boundaries without changing installed tools or policies. [[sources/replit--agent-habitat-architecture#root]]

## Related

- [[concepts/agent-control-plane]] — coordination versus independent enforcement.
- [[concepts/durable-agent-execution]] — resumed work must preserve authority state too.
- [[concepts/mcp-enterprise-managed-authorization]] — identity/token mediation is narrower than effect authorization.
- [[concepts/trace-lake]] — useful investigation traces versus independent enforcement logs.
- [[concepts/review-cost-aware-workflows]] — verify concrete boundary claims rather than rely on abstract assurance.
- [[artifacts/projects/kody]] — implemented credential-resolution interface; not Habitat compliance.
- [[artifacts/projects/codex]] — runtime permission and sandbox boundaries inspected in code.
- [[artifacts/projects/background-agents]] — snapshot credentials, residual context and uncertain worker termination.
- [[artifacts/projects/superplane]] — revision-bound approvals and PR mutation ownership.
- [[artifacts/skills/security-audit]] — evidence lifecycle for assessing claims, not enforcement infrastructure.

## What we'd steal

Portable research/adoption criteria below—not a blanket instruction to install controls or change the user's environment. Prioritize a mechanism when the corresponding capability/exposure exists; the full reference architecture is not a prerequisite for a bounded, low-authority read-only task.

1. **★ Separate model placement from execution authority.** Inventory where tools, installers and generated code actually execute; a cloud model does not isolate a local extension. [[sources/lhchavez--managed-agent-environments#execution-boundary]]

2. **★ Make the boundary survive agent non-cooperation.** Locate policy, credentials and stop controls outside agent-writable state, and verify the bypass paths. [[sources/lhchavez--managed-agent-environments#controls]]

3. **Use task-scoped workspaces instead of ambient workstation access.** Separate unrelated repositories, browser sessions, keys and internal networks from the task. [[sources/lhchavez--managed-agent-environments#execution-boundary]]

4. **Treat dependency installation as execution.** Keep installers and helper tools inside the same intended boundary; one unsandboxed helper breaks the claim. [[sources/lhchavez--managed-agent-environments#sandbox-gap]]

5. **★ Separate identity, custody and authorized effect.** A valid principal and hidden credential do not establish approval for the requested operation, resource or destination. [[sources/lhchavez--managed-agent-environments#credential-authority]]

6. **Use platform-attested workload identity.** Bind short-lived identity to launch evidence and lineage, not claims supplied by the untrusted workload. [[sources/replit--agent-habitat-architecture#identity]]

7. **Carry trigger provenance separately.** A trusted integration delivering a public issue must not lend its broad authority to the anonymous initiator. [[sources/replit--agent-habitat-architecture#identity]]

8. **Keep content from becoming authority.** Treat retrieved pages, issues, tool outputs and subagent reports as inputs, not new permission grants. [[sources/replit--agent-habitat-architecture#identity]]

9. **Define a machine-checkable run ceiling.** Bound organization, principal, resources, operations, compute, network volume and spending before execution. [[sources/replit--agent-habitat-architecture#ceiling]]

10. **★ Intersect constraints; do not union conveniences.** Default deny and explicit deny should dominate; agent autonomy must not expand the run ceiling. [[sources/replit--agent-habitat-architecture#ceiling]]

11. **Make attenuation monotonic and portable.** Carry narrowing constraints with the token; specify revocation separately and preserve restrictions across hosts. [[sources/replit--agent-habitat-architecture#attenuation]]

12. **Derive children from current authority.** Subagents inherit no more than the current parent token; avoid sharing parent credentials or writable state by accident. [[sources/replit--agent-habitat-architecture#attenuation]]

13. **Make escalation a distinct authorized transition.** Resolve the paper’s ceiling/escalation tension with an explicit new policy version rather than a silent mid-run reset. [[sources/replit--agent-habitat-architecture#attenuation]]

14. **Separate deny-only monitors from permission issuers.** Use adaptive checks to block or escalate under an independent ceiling; do not let a model assessment grant authority. [[sources/replit--agent-habitat-architecture#filters]]

15. **Convert exact historical restrictions into executable policy.** For example, a forbidden destination after sensitive reads is a state constraint, not a request for the model to remember. [[sources/replit--agent-habitat-architecture#filters]]

16. **Treat filter outages and stale policy as explicit states.** The proposal fails closed; test that behavior and document the resulting availability tradeoff. [[sources/replit--agent-habitat-architecture#filters]]

17. **Keep agent-written persistence untrusted.** Carry provenance into later runs and review instruction/config/hook changes before they gain authority. [[sources/replit--agent-habitat-architecture#persistent-input]]

18. **Test isolation at the real enforcement layer.** Check host, kernel, tenant and control-plane boundaries; name independent layers instead of relying on sandbox labels. [[sources/replit--agent-habitat-architecture#isolation]]

19. **Enumerate every outbound and inbound path.** Include DNS, direct IP, IPv6, metadata, non-HTTP traffic, previews and provider-hosted tools—not just ordinary web requests. [[sources/replit--agent-habitat-architecture#isolation]]

20. **Keep enforcement components small and inspectable.** The proposal calls for signed builds, fuzzing and memory-safe implementation; record actual build/policy evidence rather than assuming those properties. [[sources/replit--agent-habitat-architecture#isolation]]

21. **Broker credentials per authorized request.** Keep long-lived external secrets out of agent files, environment and memory, and inject only for the intended destination. [[sources/replit--agent-habitat-architecture#broker]]

22. **Reject alternate credential paths.** Check caller-supplied headers, cookies, query/body credentials and unexpected auth channels, not only the credential the broker injected. [[sources/replit--agent-habitat-architecture#broker]]

23. **Handle newly returned secrets too.** Vault/redact fresh tokens and protocol-specific signing or database credentials; input secrecy alone leaves response leakage. [[sources/replit--agent-habitat-architecture#broker]]

24. **★ Constrain operations within allowed services.** A permitted GitHub host can still support private-data exfiltration to a public PR; model the whole read/write flow. [[sources/lhchavez--managed-agent-environments#toxic-flow]]

25. **Propagate data provenance across representations.** Context, files and subagent outputs retain confidentiality/untrusted-input labels; spell out what transformations break tracking. [[sources/replit--agent-habitat-architecture#data-flow]]

26. **Count model APIs and rendered UI as egress.** Data sent to inference endpoints or remotely loaded UI content crosses a boundary too. [[sources/replit--agent-habitat-architecture#data-flow]]

27. **Use the Rule of Two as an explicit policy choice.** If untrusted input, private data and external writes coexist, require an appropriate per-write gate rather than assuming the combination is harmless. [[sources/replit--agent-habitat-architecture#data-flow]]

28. **★ Bind approval to the actual action.** Show normalized operation, target, destination and delegation through a trusted channel the agent cannot forge; avoid vague session-wide consent. [[sources/replit--agent-habitat-architecture#approval]]

29. **Separate production proposal from privileged apply.** Keep standing production-write authority out of the ordinary agent run; the execution owner checks the authorized change. [[sources/lhchavez--managed-agent-environments#controls]]

30. **Pin tools and review changes at the capability boundary.** Registries, packages, MCP descriptors and configuration are part of the supply chain; installations do not need production credentials. [[sources/replit--agent-habitat-architecture#supply-chain]]

31. **Do not confuse provenance or age with benign behavior.** Treat those supply-chain signals as filters, not proof; test actual authority and runtime behavior. [[sources/replit--agent-habitat-architecture#supply-chain]]

32. **Journal intentions and observed results separately.** Durable state should distinguish planned, dispatched, completed and uncertain side effects; a log entry is not success. [[sources/replit--agent-habitat-architecture#durability]]

33. **Use idempotency where the destination supports it.** Otherwise reconcile unknown outcomes before repeating; recorded model replay does not undo an external action. [[sources/replit--agent-habitat-architecture#durability]]

34. **★ Restore limits along with progress.** Resume attenuations, consumed approvals, action history and spent budgets so crashes cannot replenish authority. [[sources/replit--agent-habitat-architecture#durability]]

35. **Measure compensation against real-world state.** Reconciliation is needed after partial effects; compensating actions cannot promise atomic rollback. [[sources/replit--agent-habitat-architecture#durability]]

36. **★ Contain independently of the compromised process.** Stop model/network access, freeze execution and revoke identities/tokens via a path that does not require agent cooperation. [[sources/replit--agent-habitat-architecture#containment]]

37. **Revoke downstream grants, not just the original key.** Delegations and authorized effects may persist after the runtime stops; inventory and test their actual revocation path. [[sources/lhchavez--managed-agent-environments#containment]]

38. **Practice containment and controlled resumption.** Measure end-to-end stop latency and require a fresh authorized trigger rather than an automatic restart of a contained run. [[sources/replit--agent-habitat-architecture#containment]]

39. **Collect evidence where policy is enforced.** Off-host tamper-evident logs need workload, trigger, policy and build identifiers; agent self-report is a different evidence class. [[sources/replit--agent-habitat-architecture#audit]]

40. **Exclude credentials from audit and bound retention.** Treat model, log, tool and storage destinations separately; hosting location alone does not establish residency/compliance. [[sources/lhchavez--managed-agent-environments#adoption-limits]]

41. **Keep incident categories and survey denominators intact.** Distinguish allegations, demonstrations, confirmed compromise, suspected events, cohort telemetry and analogies. [[sources/lhchavez--managed-agent-environments#supporting-evidence]]

42. **Use the maturity profile as a question set, not a certificate.** Demand boundary-specific evidence and retain weak tracks; a numerical level or vendor example is not verified security. [[sources/replit--agent-habitat-architecture#maturity]]

43. **Verify the control before expanding autonomy.** Use unauthorized-action, bypass, crash and containment tests appropriate to the capability; do not infer performance from a vendor diagram. [[sources/lhchavez--managed-agent-environments#adoption-limits]]

44. **Separate future migration from existing compromise cleanup.** Moving new work to an isolated environment does not erase endpoint persistence, leaked data or previously granted authority. [[sources/lhchavez--managed-agent-environments#adoption-limits]]

## Open questions

- What concrete prover, policy language, attestation chain and protocol brokers implement these proposed invariants, and under what threat model?
- How are exceptional escalation, static ceilings and restart transitions reconciled without replaying spent authority?
- Which irreversible downstream effects can actually be revoked, and what remains after containment?
- Can data-flow tracking survive model transformations, encoding and multihop tools without unacceptable false positives or leaks?
- What negative tests, independent reviews and comparative outcome data would justify a specific product's claimed maturity level?
- Which controls earn their implementation cost at the required scope, rather than recreating the entire proposal before a bounded use case exists?
