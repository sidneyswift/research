---
domain: concepts
type: concept
name: skills-over-mcp
creators: ["[[creators/model-context-protocol]]"]
sources: ["[[sources/modelcontextprotocol--mcp-core-and-extensions-docs]]", "[[sources/agentskills--specification]]"]
status: emerging
last-reviewed: 2026-11-04
---

# Skills over MCP

> Serve the instructions for using a service with the service itself, while retaining origin, exact content identity and host-controlled activation.

## What it is

The official Skills extension defines discovery and retrieval of Agent Skills through MCP. It retains the Agent Skills file format; it does not create a competing SKILL.md standard or mandate a particular model/user selection UI. A server exposes `skills/list`, `skills/get` and resource reads, optionally directory reads. Reading a file is not the same operation as activating a skill. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#skills]]

## Where it came from

The Skills Over MCP Working Group's accepted SEP-2640 and released **Beta** specification target base revision `2026-07-28` or later. The pinned spec is at ext-skills `649f7aee87d631ac4d1fdd3b12eef0c6264fdb3a`. Final SEP status is distinct from extension lifecycle stage. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#skill-support]]

## Why it matters

[[concepts/workspace-skill-distribution]] studies filesystem and workspace distribution. This extension adds a **remote service distribution rail**, with instructions and references read only when needed. It solves discovery/retrieval and content consistency; it does not make all hosts load remote skills, confer tool permission, or make server-authored instructions trustworthy. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#skills]], [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#skill-integrity]]

## Evidence & claims

1. **Discovery:** server declares both `resources` and `io.modelcontextprotocol/skills`; `skills/list` returns complete entries with frontmatter and either a full file manifest or `resources: "dynamic"`. `skills/get` supports a known URI independently of listing, including unlisted skills. Optional `resources/directory/read` requires `directoryRead: true`. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#skills]]
2. **Identity:** a skill is identified by originating server plus SKILL.md URI. Display names and the `skill://` scheme are insufficient. Preserve that origin across registry, cache, approval and model context. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#skills]], [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#skill-integrity]]
3. **Progressive loading:** retain the entry, obtain approval when required, then read SKILL.md and needed references through the original server. Do not prefetch all files on connection/listing/approval. Relative references resolve within the skill root; directory results do not silently expand its approved manifest. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#skills]]
4. **Integrity:** verify raw byte size and SHA-256 for every manifest file before use and compare parsed frontmatter field by field. Reject mismatches; refresh the entry for recovery. Persisted approval binds to the full URI/digest set; additions, removals or changed files invalidate it. Integrity establishes consistency with the server's declaration, not benignness. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#skill-integrity]]
5. **Caches:** protect verified files against mutation or reverify on access; exclude the cache from ordinary filesystem-skill discovery so remote content does not lose its origin and approval history. Dynamic skills can be declined; accepted dynamic content does not gain blanket approval for arbitrary future bytes. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#skill-integrity]]
6. **Authority:** host-side code execution and grants such as `allowed-tools` require explicit per-skill approval. Nested skill activation needs fresh consent; reading another SKILL.md as reference data does not activate it. Cross-server reads need per-call approval naming both origins. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#skill-integrity]]
7. **Availability:** the pinned community implementation list distinguishes released, partial, pre-v1, prototype, in-progress and planned work. It reports TypeScript SDK/FastMCP releases and merged-but-unreleased implementations, while ChatGPT plugins are listed as partial submission-time import. Those statements locate investigation targets; this pass did not verify their releases or run hosts. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#skill-support]]

## Patterns demonstrated

- [[patterns/quality-bar/revision-bound-review]] — authorization binds exact complete manifest identity, not a friendly skill name. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#skill-integrity]]
- [[patterns/behavioral/context-is-not-authority]] — loading instructions does not itself grant tool rights. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#skill-integrity]]
- [[patterns/behavioral/latent-vs-deterministic-split]] — model/user chooses when instructions help; host code checks origin, size, digests and activation. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#skills]]
- [[patterns/composition/single-source-multi-surface-distribution]] — retain one skill format across local packages and remote serving. Actual host loading semantics remain separate. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#skills]]

## Tensions & counter-arguments

Remote service authors can update instructions more conveniently, but also place new untrusted text near powerful tools. Hashes prevent unnoticed inconsistency with an approved manifest; they do not assess intent. Dynamic content weakens the stable-manifest approval model. Host origin labeling, verification and permission gates are central requirements, not optional implementation polish. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#skill-integrity]]

Portability of the directory/file format does not imply portability of installation, activation, code execution or enterprise distribution. [[concepts/convergent-agent-plugin-spec]] and [[concepts/workspace-skill-distribution]] remain separate pages because these mechanisms answer different questions. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#skills]]

## Timeline

- 2026-11-04 — Captured released Beta transport spec, its origin/integrity requirements and the dated community implementation list. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#root]]

## Related

- [[concepts/model-context-protocol]], [[concepts/mcp-extension-architecture]], [[artifacts/projects/openai-mcp-extensions]], [[analyses/mcp-and-extensions]].
- [[concepts/workspace-skill-distribution]], [[concepts/convergent-agent-plugin-spec]], [[artifacts/skills/writing-great-skills]].

## What we'd steal

- ★ Serve operational instructions beside capabilities while retaining the existing open skill format. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#skills]]
- ★ Namespace skill identity by server and URI, not display name. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#skill-integrity]]
- ★ Approve exact complete manifests and reapprove on changes; verify fetched bytes before use. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#skill-integrity]]
- Load instructions and supporting files on demand; keep discovery metadata small. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#skills]]
- Support direct URI lookup for known workflows without requiring full catalog enumeration. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#skills]]
- Keep remote caches out of local automatic discovery; preserve origin through restarts. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#skill-integrity]]
- Separate reading a reference, activating a skill and granting execution rights. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#skill-integrity]]
- Treat directory browsing as discovery only; it cannot widen a retained authorization manifest. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#skills]]
- Expose dynamic content as a distinct policy choice rather than pretending it has immutable approval. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#skill-integrity]]

## Open questions

- Which of our intended hosts implement this contract end to end rather than import skills only at publication time?
- How should our instruction review policy evaluate malicious-but-consistently-hashed content?
- Which service workflows merit remote delivery versus a small version-controlled shared skill pack?
