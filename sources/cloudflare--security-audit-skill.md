---
domain: sources
type: repo
url: https://github.com/cloudflare/security-audit-skill
retrieved: 2026-11-06
snapshot-location: sources/cloudflare--security-audit-skill/
upstream-commit: c1c8a8c1471069fb0e188eeaff69b8e8db6564a8
last-reviewed: 2026-11-06
---

# Cloudflare security-audit skill — evidence-led, coverage-accounted vulnerability review

> Pinned source evidence for [[artifacts/skills/security-audit]], by [[creators/cloudflare]].

## Snapshot details

- **Revision:** `c1c8a8c1471069fb0e188eeaff69b8e8db6564a8`, committed 2026-09-14T20:28:54+01:00; retrieved 2026-11-06.
- **Preservation:** all 22 tracked files with shallow `.git` history are saved locally under `sources/cloudflare--security-audit-skill/`. The checkout is ignored, not published. This citation page, [all-file hash and range manifest](cloudflare--security-audit-skill-evidence/capture.json), [validator test output](cloudflare--security-audit-skill-evidence/validator-tests.txt), analysis and restore registration are committed.
- **Restore:** `./setup.sh --only cloudflare--security-audit-skill`; verify with `./setup.sh --check --only cloudflare--security-audit-skill`. This depends on upstream availability; it is not an independent archival mirror.
- **Reading scope:** all 15 skill Markdown files, README and license; report schema and both validator implementations, with close inspection of identity, ownership, verdict/state invariants, input bounds and CLI behavior. Selected fixture bodies plus all test names reviewed. Not a claim that every test body was line-reviewed.
- **Executed:** the two bundled Node validator suites, **65 passed / 0 failed / 0 skipped**, Node v25.9.0 on macOS arm64. No dependencies installed, skill activated, target code audited, live service probed, or full multi-agent workflow exercised. The tests do not establish detection accuracy or sandbox/promotion enforcement.

## Popularity signals

GitHub API at retrieval: **61,558 stars; 3,997 forks**. Attention signals, not deployment, correctness or recall measurements. MIT license. [[sources/cloudflare--security-audit-skill#license]]

## Anchor map

### root

- [README.md:1–106](https://github.com/cloudflare/security-audit-skill/blob/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8/README.md#L1-L106)

### modes

- [skills/security-audit/SKILL.md:1–29](https://github.com/cloudflare/security-audit-skill/blob/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8/skills/security-audit/SKILL.md#L1-L29)

### execution-boundary

- [skills/security-audit/SKILL.md:31–86](https://github.com/cloudflare/security-audit-skill/blob/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8/skills/security-audit/SKILL.md#L31-L86)

### prior-evidence

- [skills/security-audit/SKILL.md:88–105](https://github.com/cloudflare/security-audit-skill/blob/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8/skills/security-audit/SKILL.md#L88-L105)
- [skills/security-audit/RECONNAISSANCE.md:59–71](https://github.com/cloudflare/security-audit-skill/blob/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8/skills/security-audit/RECONNAISSANCE.md#L59-L71)

### profiles-budget

- [skills/security-audit/SKILL.md:107–134](https://github.com/cloudflare/security-audit-skill/blob/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8/skills/security-audit/SKILL.md#L107-L134)

### claim-standard

- [skills/security-audit/SKILL.md:136–192](https://github.com/cloudflare/security-audit-skill/blob/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8/skills/security-audit/SKILL.md#L136-L192)

### recon

- [skills/security-audit/RECONNAISSANCE.md:1–57](https://github.com/cloudflare/security-audit-skill/blob/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8/skills/security-audit/RECONNAISSANCE.md#L1-L57)

### context-selection

- [skills/security-audit/RECONNAISSANCE.md:73–88](https://github.com/cloudflare/security-audit-skill/blob/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8/skills/security-audit/RECONNAISSANCE.md#L73-L88)
- [skills/security-audit/HUNTING.md:11–25](https://github.com/cloudflare/security-audit-skill/blob/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8/skills/security-audit/HUNTING.md#L11-L25)

### coverage-contract

- [skills/security-audit/RECONNAISSANCE.md:90–156](https://github.com/cloudflare/security-audit-skill/blob/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8/skills/security-audit/RECONNAISSANCE.md#L90-L156)

### hunting

- [skills/security-audit/HUNTING.md:3–9](https://github.com/cloudflare/security-audit-skill/blob/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8/skills/security-audit/HUNTING.md#L3-L9)
- [skills/security-audit/HUNTING.md:27–97](https://github.com/cloudflare/security-audit-skill/blob/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8/skills/security-audit/HUNTING.md#L27-L97)

### promotion

- [skills/security-audit/HUNTING.md:99–136](https://github.com/cloudflare/security-audit-skill/blob/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8/skills/security-audit/HUNTING.md#L99-L136)

### candidate-gate

- [skills/security-audit/HUNTING.md:138–157](https://github.com/cloudflare/security-audit-skill/blob/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8/skills/security-audit/HUNTING.md#L138-L157)

### hunter-result

- [skills/security-audit/HUNTING.md:168–219](https://github.com/cloudflare/security-audit-skill/blob/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8/skills/security-audit/HUNTING.md#L168-L219)

### coverage-critics

- [skills/security-audit/HUNTING.md:221–251](https://github.com/cloudflare/security-audit-skill/blob/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8/skills/security-audit/HUNTING.md#L221-L251)

### independent-validation

- [skills/security-audit/VALIDATION-AND-REPORTING.md:3–93](https://github.com/cloudflare/security-audit-skill/blob/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8/skills/security-audit/VALIDATION-AND-REPORTING.md#L3-L93)

### verdict-contract

- [skills/security-audit/VALIDATION-AND-REPORTING.md:95–118](https://github.com/cloudflare/security-audit-skill/blob/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8/skills/security-audit/VALIDATION-AND-REPORTING.md#L95-L118)
- [skills/security-audit/report-schema.json:1–461](https://github.com/cloudflare/security-audit-skill/blob/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8/skills/security-audit/report-schema.json#L1-L461)

### material-reverification

- [skills/security-audit/VALIDATION-AND-REPORTING.md:120–149](https://github.com/cloudflare/security-audit-skill/blob/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8/skills/security-audit/VALIDATION-AND-REPORTING.md#L120-L149)

### reporting

- [skills/security-audit/VALIDATION-AND-REPORTING.md:151–186](https://github.com/cloudflare/security-audit-skill/blob/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8/skills/security-audit/VALIDATION-AND-REPORTING.md#L151-L186)

### attack-classes

- [skills/security-audit/ATTACK-CLASSES.md:1–130](https://github.com/cloudflare/security-audit-skill/blob/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8/skills/security-audit/ATTACK-CLASSES.md#L1-L130)

### ai-authority

- [skills/security-audit/AI-AND-LLM.md:1–83](https://github.com/cloudflare/security-audit-skill/blob/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8/skills/security-audit/AI-AND-LLM.md#L1-L83)

### data-lifecycle

- [skills/security-audit/DATA-ISOLATION-AND-LIFECYCLE.md:1–84](https://github.com/cloudflare/security-audit-skill/blob/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8/skills/security-audit/DATA-ISOLATION-AND-LIFECYCLE.md#L1-L84)

### supply-chain

- [skills/security-audit/SUPPLY-CHAIN-AND-RELEASE.md:1–73](https://github.com/cloudflare/security-audit-skill/blob/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8/skills/security-audit/SUPPLY-CHAIN-AND-RELEASE.md#L1-L73)

### cloud-policy

- [skills/security-audit/CLOUD-AND-DEPLOYMENT.md:1–86](https://github.com/cloudflare/security-audit-skill/blob/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8/skills/security-audit/CLOUD-AND-DEPLOYMENT.md#L1-L86)

### web-identity

- [skills/security-audit/WEB-PROTOCOL-AND-AUTH.md:1–105](https://github.com/cloudflare/security-audit-skill/blob/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8/skills/security-audit/WEB-PROTOCOL-AND-AUTH.md#L1-L105)

### browser

- [skills/security-audit/CLIENT-SIDE.md:1–83](https://github.com/cloudflare/security-audit-skill/blob/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8/skills/security-audit/CLIENT-SIDE.md#L1-L83)

### native

- [skills/security-audit/MEMORY-SAFETY-AND-BINARY.md:1–101](https://github.com/cloudflare/security-audit-skill/blob/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8/skills/security-audit/MEMORY-SAFETY-AND-BINARY.md#L1-L101)

### ipc

- [skills/security-audit/DESKTOP-MOBILE-AND-LOCAL-IPC.md:1–89](https://github.com/cloudflare/security-audit-skill/blob/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8/skills/security-audit/DESKTOP-MOBILE-AND-LOCAL-IPC.md#L1-L89)

### protocols

- [skills/security-audit/PROTOCOLS-RPC-AND-MESSAGING.md:1–81](https://github.com/cloudflare/security-audit-skill/blob/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8/skills/security-audit/PROTOCOLS-RPC-AND-MESSAGING.md#L1-L81)

### availability

- [skills/security-audit/RESOURCE-EXHAUSTION-AND-AVAILABILITY.md:1–78](https://github.com/cloudflare/security-audit-skill/blob/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8/skills/security-audit/RESOURCE-EXHAUSTION-AND-AVAILABILITY.md#L1-L78)

### findings-code

- [skills/security-audit/validate-findings.cjs:247–348](https://github.com/cloudflare/security-audit-skill/blob/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8/skills/security-audit/validate-findings.cjs#L247-L348)
- [skills/security-audit/validate-findings.cjs:361–595](https://github.com/cloudflare/security-audit-skill/blob/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8/skills/security-audit/validate-findings.cjs#L361-L595)

### findings-input

- [skills/security-audit/validate-findings.cjs:40–103](https://github.com/cloudflare/security-audit-skill/blob/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8/skills/security-audit/validate-findings.cjs#L40-L103)
- [skills/security-audit/validate-findings.cjs:604–773](https://github.com/cloudflare/security-audit-skill/blob/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8/skills/security-audit/validate-findings.cjs#L604-L773)

### coverage-code

- [skills/security-audit/validate-coverage-ledger.cjs:340–566](https://github.com/cloudflare/security-audit-skill/blob/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8/skills/security-audit/validate-coverage-ledger.cjs#L340-L566)
- [skills/security-audit/validate-coverage-ledger.cjs:568–719](https://github.com/cloudflare/security-audit-skill/blob/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8/skills/security-audit/validate-coverage-ledger.cjs#L568-L719)
- [skills/security-audit/validate-coverage-ledger.cjs:761–806](https://github.com/cloudflare/security-audit-skill/blob/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8/skills/security-audit/validate-coverage-ledger.cjs#L761-L806)

### coverage-input

- [skills/security-audit/validate-coverage-ledger.cjs:11–20](https://github.com/cloudflare/security-audit-skill/blob/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8/skills/security-audit/validate-coverage-ledger.cjs#L11-L20)
- [skills/security-audit/validate-coverage-ledger.cjs:141–319](https://github.com/cloudflare/security-audit-skill/blob/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8/skills/security-audit/validate-coverage-ledger.cjs#L141-L319)
- [skills/security-audit/validate-coverage-ledger.cjs:721–759](https://github.com/cloudflare/security-audit-skill/blob/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8/skills/security-audit/validate-coverage-ledger.cjs#L721-L759)

### validator-tests

- [skills/security-audit/validate-findings.test.cjs:151–232](https://github.com/cloudflare/security-audit-skill/blob/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8/skills/security-audit/validate-findings.test.cjs#L151-L232)
- [skills/security-audit/validate-findings.test.cjs:305–361](https://github.com/cloudflare/security-audit-skill/blob/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8/skills/security-audit/validate-findings.test.cjs#L305-L361)
- [skills/security-audit/validate-findings.test.cjs:465–652](https://github.com/cloudflare/security-audit-skill/blob/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8/skills/security-audit/validate-findings.test.cjs#L465-L652)
- [skills/security-audit/validate-coverage-ledger.test.cjs:407–491](https://github.com/cloudflare/security-audit-skill/blob/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8/skills/security-audit/validate-coverage-ledger.test.cjs#L407-L491)
- [skills/security-audit/validate-coverage-ledger.test.cjs:536–740](https://github.com/cloudflare/security-audit-skill/blob/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8/skills/security-audit/validate-coverage-ledger.test.cjs#L536-L740)

### license

- [LICENSE:1–21](https://github.com/cloudflare/security-audit-skill/blob/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8/LICENSE#L1-L21)

### test-execution

- [Local validator-suite output](cloudflare--security-audit-skill-evidence/validator-tests.txt) and the environment/hash receipt in [capture.json](cloudflare--security-audit-skill-evidence/capture.json). Fixtures test record mechanics, not real vulnerability discovery.

### harness-context

Supporting context read: [Build your own vulnerability harness](https://blog.cloudflare.com/build-your-own-vulnerability-harness/), June 18, 2026, by Dan Jones, Alexandra Godoi and Grant Bourzikas; retrieved November 6. This is a live external page, not a retained full article snapshot.

The article describes an earlier seven-phase skill and a separate fleet-wide system with persisted investigations, model-swapped validation, deduplication, dependency tracing and patch triage. The September repository pin instead prescribes six phases; it does not ship that enterprise harness. Fleet results are author-reported, not a benchmark reproduced here. Repeated-run yield is not recall against a labeled universe of all bugs. The article's broad workflow and throughput claims should not be imported as guarantees of the released skill; nor does model diversity establish statistical independence. Its rule requeuing zero-result hunters is not this repository's reporting rule, which explicitly accepts zero confirmed findings.

## Why we cite this

The repository makes evidence status, coverage identity, owner attribution, fresh-review obligations and partial-run reporting explicit. Its zero-dependency validators implement bounded input and record-consistency checks. They do not verify source-file existence, exploit truth, actual agent independence, cross-file completeness, sandbox configuration or race-safe artifact promotion. Those remain parent/agent obligations or integration work at this pin. [[sources/cloudflare--security-audit-skill#findings-code]] [[sources/cloudflare--security-audit-skill#coverage-code]] [[sources/cloudflare--security-audit-skill#promotion]]

## Related sources

- [[sources/poteto--verification-over-adversarial-review]] — empirical verification rather than abstract critique; concrete falsification is a scoped complement.
- [[sources/cursor--plugins-pstack]] — evidence calibration and reviewer independence distinctions.
- [[sources/openai--codex]] — executable harness authority and persistence boundaries.
- [[sources/open-inspect--background-agents]] — durable state and isolated execution.
