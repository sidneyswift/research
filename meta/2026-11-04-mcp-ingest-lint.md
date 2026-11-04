---
domain: meta
type: lint-report
last-reviewed: 2026-11-04
---

# MCP ingest validation — 2026-11-04

## Scope and outcome

**Success for the bounded source ingest and wiki integration.** [[analyses/mcp-and-extensions]] remains draft because only same-family judges were available. No application, host, OAuth flow, deployment, benchmark or source test suite was executed. All changes are local wiki work; no publication or provider configuration is implied.

- Two artifact pages: [[artifacts/projects/mcp-apps]], [[artifacts/projects/openai-mcp-extensions]].
- Four concept pages: [[concepts/model-context-protocol]], [[concepts/mcp-extension-architecture]], [[concepts/mcp-enterprise-managed-authorization]], [[concepts/skills-over-mcp]].
- Creator: [[creators/model-context-protocol]]. Four citation maps and 54 named immutable document captures; OpenAI live clone retains `.git`, is ignored and pinned in the manifest.
- Sources: [[sources/modelcontextprotocol--mcp-core-and-extensions-docs]], [[sources/modelcontextprotocol--mcp-apps-docs]], [[sources/modelcontextprotocol--mcp-authorization-docs]], [[sources/openai--mcp-extensions]].

## Mechanical verification

- `scripts/wiki-doctor.py --json`: real tracked-index baseline **50/100**; because the doctor enumerates Git-indexed Markdown, a disposable index also included existing local drafts and then this ingest’s new pages: **2,407 → 2,465 pages**, **50 → 50**, no added findings in any reported category. The real Git index was unchanged. No new broken links, orphans, missing required sections or embedded gitlinks. Seven inherited broken-link occurrences remain in imported Every articles; inherited stale-review and attention signals remain reported. No broad cleanup was performed.
- `python3 scripts/check-document-captures.py <three receipts>`: **54/54 captures**, byte counts and SHA-256 match; **0 errors**. Eight temporary failure/acceptance scenarios cover valid list/object receipts, same-size byte corruption, size mismatch, missing file, duplicate file, path escape and empty receipt.
- `./setup.sh --only openai--mcp-extensions`: **1/1 source ready** at `9e6d418439cca0790bece62f6cd886ad4c04f133`; no source applications or dependencies executed.
- `scripts/check-source-citations.py` on the OpenAI source: **26 registered anchors, 38 immutable GitHub line ranges across 14 source files, 0 errors**. Invocation included new pages explicitly; indexed/tracked backlinks were also inspected.
- Independent scoped audit: **442 anchored source citations** in the seven main research pages plus four citation maps resolved; **91 anchors** across the four new maps. Numeric Apps/auth/core local ranges and OpenAI pinned Git ranges were checked. Creator, indexes, appended backlinks and this report received additional local-link checks. Raw evidence links were not treated as newly researched wiki assertions.
- `git diff --check`: no whitespace errors from this ingest. Existing uncommitted work was preserved; unrelated changes were not committed or reverted.

## Judgment review and corrections

All three reviewers used [[analyses/_eval-rubric]] and checked primary captured spans. Rubric order: citation integrity / faithfulness / completeness / non-genericness / decision usefulness.

| Review scope | Scores | Result |
| --- | --- | --- |
| OpenAI + core | 4 / 4 / 4 / 5 / 5 | No score at or below 3 |
| Apps | 4 / 4 / 5 / 5 / 5 | No score at or below 3 |
| Auth + core | 5 / 4 / 4 / 5 / 5 | No score at or below 3 |

Applied ingest corrections:

- [[concepts/model-context-protocol]] — authenticated state handles are names, while unauthenticated handles may be bearer tokens; fixed an overbroad rule. MRTR retry results must not be cached at all. Elicitation is a server-requested interaction, distinct from the three server primitives.
- [[artifacts/projects/mcp-apps]] and [[analyses/mcp-and-extensions]] — tool-result `structuredContent` and explicit model-context updates are different channels; corrected a potentially misleading same-field comparison and its anchor.
- Source reconciliation — current/legacy initialization, Beta versus Stable schema labels, and spec/overview disagreements remain explicit; no invented resolution or host test.

**Cross-family review remains pending.** Independent agents share the same model family. The synthesis has not been marked published or review-complete.

## Remaining findings and next evidence

| Finding | Owning file | Next evidence / one-line action |
| --- | --- | --- |
| Runtime support not tested | [[analyses/mcp-and-extensions]] | Run a two-host pilot with exact core/extension/SDK/build matrix and fallback cases |
| Enterprise revocation stronger in overview than inspected mechanism | [[concepts/mcp-enterprise-managed-authorization]] | Test an already-issued token after employee access removal; record cutoff and policy |
| ID-JAG revision dependency differs from current draft | [[sources/modelcontextprotocol--mcp-authorization-docs]] | Verify the exact supported profile/draft pair for intended IdP and resource AS |
| Server Cards stage disagreement | [[sources/modelcontextprotocol--mcp-core-and-extensions-docs]] | Resolve Beta catalog versus Experimental repo with maintainers/released specification |
| UI/model disclosure needs host-specific evidence | [[artifacts/projects/mcp-apps]] | Trace each data channel in the target host; don't treat field names as secrecy contracts |
| Tasks SDK/core generations differ | [[concepts/mcp-extension-architecture]] | Verify modern receiver implementation and recovery/cancellation behavior |
| Seven historical link occurrences | imported `articles/every/` pages | Review editorial bracket text before any repair; outside this ingest |

No near-duplicate concept or new confirmed pattern was introduced. [[patterns/composition/negotiated-capability-intersection]] remains proposed because MCP feature checks do not prove the exact Shopify profile/dependency mechanism. [[meta/self-improvements]] records the applied schema refinement and repeated-capture verifier.
