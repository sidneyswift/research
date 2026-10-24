---
domain: sources
type: repo
url: https://github.com/cursor/plugins
retrieved: 2026-10-24
snapshot-location: sources/cursor--plugins-pstack/
upstream-commit: 9580c23696ac8d7abed0c166f2f9918800afb819
last-reviewed: 2026-10-24
---

# cursor/plugins — pstack

> Pinned evidence for Lauren Tan's pstack engineering principles, research methods, orchestration, verification, packaging, and automation templates.

## Snapshot details

- **Retrieved:** 2026-10-24, America/New_York.
- **Revision:** `9580c23696ac8d7abed0c166f2f9918800afb819`; latest repository commit is dated `2026-10-23T20:27:39-07:00` (23:27:39 Eastern on October 23).
- **Package:** pstack **0.15.32**, canonical source under `pstack/`, generated Claude Code tree under `harness/pstack/claude-code/`. MIT license, Lauren Tan copyright. This is a scoped ingest of pstack and relevant packaging machinery, not the entire marketplace.
- **Evidence clone:** `sources/cursor--plugins-pstack/`, canonical GitHub remote, independent Git object storage, git-ignored and listed in `repos.manifest.tsv`. A second user-facing checkout is in `Sources/cursor-plugins`.
- **Coverage:** 229 source-range anchors below cover 182 distinct files and 452 file-range entries. All 58 top-level skills, the 23 orchestration playbooks, and assigned verification/research/automation companion materials were investigated across four investigators; cited tests were selectively read and only the explicitly recorded offline subsets executed. This is not an exhaustive audit of every branch or marketplace plugin.
- **Method:** read-only pinned code/doc/prompt investigation, comparison with existing wiki entities, selected isolated local tests and negative probes, then INGEST → LINT → REFLECT.

## Evidence classes

**Prompt policy** describes instructions a host/model may follow. **Implementation** describes inspected code paths. **Test inspected** establishes a test's stated contract, not a passing run. **Local observation** is an explicitly bounded executed check below. **Synthesis/reuse** is our proposed application. None alone establishes deployed behavior, complete safety, cost savings, or agent-quality improvement.

## Anchor map

Each `###` heading below is a registered citation anchor. File links use immutable GitHub blob URLs at the pinned revision. PK = packaging/configuration/style; PP = principles; RE = research/reasoning/automation; VE = verification; OR = orchestration/runtime.

### root

- [pstack/README.md:1–57](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/README.md#L1-L57)

### repository-metadata

GitHub API metadata captured 2026-10-24: **13,812 stars**, **1,367 forks**, public repository, default branch `main`. [Repository API](https://api.github.com/repos/cursor/plugins). These are whole-marketplace attention counts, not pstack installs, users, efficacy, or reliability. The API's repository-level license field was null; pstack's own MIT license is explicit in PK01.

### inventory

Pinned `git ls-tree`/filesystem inventory: **200 tracked files under pstack/**; **58 top-level skills = 34 commands + 24 principles**; **23 playbooks** under poteto-mode; **2 agents**; **3 additional nested Benny skills** excluded from the 58. 57 top-level SKILL.md files set `disable-model-invocation: true`; setup-pstack is the exception. No pstack hook/MCP configuration was found in the scoped tracked inventory. The source manifests are in PK01, generator classification in PK04, and independently derived docs counts in PK08. These are tree counts, not installed/active capabilities.

### local-checks

All checks recorded here were local source investigation on 2026-10-24. No plugin install, live agent workflow, provider/model evaluation, external message, automation activation, or real PR operation was performed. The upstream checkouts remain unchanged.

- `node scripts/generate-pstack-harness-trees.mjs --check` in the clean source: exit 0, generated tree up to date.
- `node scripts/check-pstack-docs.mjs`: exit 0; 58 skills, 23 playbooks, 2 agents, 12 docs, 358 slash mentions, 256 relative links, 34/34 commands in guide, 0 problems.
- Type negative probe below: strict TypeScript accepts a negative duration; running it produces an end before the start.
- Packaging mutation below: broken skill-local link goes undetected by both generator parity and docs checker.
- Verification and orchestration subset results are separate anchors below. Full host/tool/provider integration was not executed. Root schema validation was not run because its dependencies were absent.

### type-negative-probe

Local negative fixture, Node **23.6.1** and installed TypeScript compiler, copied from the PK12 representation:

```ts
type TimeRange = { start: Date; durationMs: number };
const backwards: TimeRange = { start: new Date(0), durationMs: -1 };
const end = new Date(backwards.start.getTime() + backwards.durationMs);
if (!(end < backwards.start)) throw new Error('Expected a backwards range');
```

`tsc --strict --noEmit` exited 0; `node --experimental-strip-types` exited 0. This disproves the example's claimed representational guarantee for plain `number`, not the general usefulness of domain types. The fixture was outside the source tree.

### packaging-negative-probe

An isolated copy appended `[Missing contract](./references/does-not-exist.md)` to `pstack/skills/bro/SKILL.md`. Running the generator produced 58 skills with 23 adapter insertions; subsequent generator `--check` and docs checker both exited 0. The generator's resolver omits nonexistent targets from link validation; the docs checker focuses README/guide files rather than every skill reference. Thus parity and guide coverage pass without establishing whole-plugin link integrity. Canonical source was not edited. Mechanism: PK04–PK08.

### verification-local-checks


2026-10-24, macOS, Node v23.6.1. Read-only source investigation; execution only from an isolated scratch copy. No dependency installation/network/TLC/PNG/app runs.

1. Copied pstack/skills/statechart/scripts into the scratch folder. node --check on all 21 top-level .mjs modules: 21 passed.
2. Offline source test subset: original test file lines 1–1675, plus original hoisted flatEdges helper lines 3975–3997; no assertion changes. Excludes optional tool installation at lines1676–1687 and subsequent integration tests. node --test scripts/test/statechart-offline.test.mjs: 44 tests, 43 pass, 1 fail, zero skipped. Sole final failure: piped help output missing Exit codes. Original source 894–896 prints help then immediately process.exit(0).
3. Independent spawnSync of statechart.mjs --help: exit0, stdout8192bytes, expected25747bytes from HELP plus newline, no installation output. Local inference: forced exit can leave piped console output unflushed. Not evidence of a TLC/model-checking failure.
4. Five local semantic probes: large Number representation collision, set-order-sensitive stateKey, nonexistent source-citation-shaped comment accepted, same-label parallel events synchronized, modified relative import detected by Inputs. All expected observations reproduced. The numeric/set-order cases are direct parser boundaries; whether such values/order occur in pinned TLC output was not established.
5. 150 source test names and dependency gates inventoried; selected relevant bodies inspected. Remaining TLC/PNG/platform integration tests were not run.

Scratch logs were used for these observations but are not included in the evidence clone; the method, extracted line ranges, and results above are the durable record. The initial extraction omitted a hoisted helper and had an artificial ReferenceError; final corrected extraction includes it and that extra failure disappears.

### runtime-local-checks

Bun **1.1.26**, isolated scratch copy, no real GitHub calls. Offline PATH blockers shadowed network-facing commands; watcher fixtures provided their own fake GitHub CLI.

- `watch-pr/github.test.ts`, `watch-pr/policy.test.ts`, and `check-plan.test.ts`: **52 passed, 0 failed, 133 assertions**.
- A later `bun test orch/orch.test.ts --test-name-pattern '^(?!prints commander|accepts ORCH_STORE|maps user)'` run, with `GIT_CONFIG_NOSYSTEM=1 GIT_CONFIG_GLOBAL=/dev/null`, intended to select Store tests but did not exclude other tests on this Bun version: **8 passed, 13 failed**. Frontier tests encountered the offline blockers; a stale-PID fixture and CLI tests also failed. The temporary CLI copy reached its dependency-bootstrap path, leaving a cache but no installed commander. These constrained-run failures are not classified as confirmed upstream defects, and this is not a clean Store/CLI suite result.
- No production PR, scheduler, agent, or cloud integration was exercised. Source-derived lifecycle limits are documented separately in [[artifacts/skills/poteto-mode]].

### PK01

- [pstack/plugin.json:1–21](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/plugin.json#L1-L21)
- [pstack/.cursor-plugin/plugin.json:1–31](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/.cursor-plugin/plugin.json#L1-L31)
- [pstack/LICENSE:1–21](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/LICENSE#L1-L21)

### PK02

- [pstack/README.md:1–57](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/README.md#L1-L57)

### PK03

- [.claude-plugin/marketplace.json:1–19](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/.claude-plugin/marketplace.json#L1-L19)
- [.cursor-plugin/marketplace.json:76–85](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/.cursor-plugin/marketplace.json#L76-L85)

### PK04

- [scripts/generate-pstack-harness-trees.mjs:25–122](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/scripts/generate-pstack-harness-trees.mjs#L25-L122)

### PK05

- [scripts/generate-pstack-harness-trees.mjs:118–165](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/scripts/generate-pstack-harness-trees.mjs#L118-L165)

### PK06

- [scripts/generate-pstack-harness-trees.mjs:167–188](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/scripts/generate-pstack-harness-trees.mjs#L167-L188)

### PK07

- [pstack/docs/harness/claude-code.md:1–67](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/docs/harness/claude-code.md#L1-L67)

### PK08

- [scripts/check-pstack-docs.mjs:1–152](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/scripts/check-pstack-docs.mjs#L1-L152)

### PK09

- [.github/workflows/validate-plugins.yml:1–35](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/.github/workflows/validate-plugins.yml#L1-L35)
- [pstack/skills/poteto-mode/scripts/package.json:1–16](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/scripts/package.json#L1-L16)

### PK10

- [pstack/skills/setup-pstack/SKILL.md:1–78](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/setup-pstack/SKILL.md#L1-L78)

### PK11

- [pstack/skills/typescript-best-practices/SKILL.md:1–31](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/typescript-best-practices/SKILL.md#L1-L31)
- [pstack/skills/typescript-best-practices/references/patterns.md:1–328](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/typescript-best-practices/references/patterns.md#L1-L328)

### PK12

- [pstack/skills/typescript-best-practices/references/patterns.md:78–91](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/typescript-best-practices/references/patterns.md#L78-L91)

### PK13

- [pstack/skills/technical-writing/SKILL.md:1–106](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/technical-writing/SKILL.md#L1-L106)

### PK14

- [pstack/skills/unslop/SKILL.md:1–62](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/unslop/SKILL.md#L1-L62)

### PK15

- [pstack/skills/no-comments/SKILL.md:1–24](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/no-comments/SKILL.md#L1-L24)

### PK16

- [pstack/skills/make-bot-ui/SKILL.md:1–115](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/make-bot-ui/SKILL.md#L1-L115)

### PK17

- [pstack/skills/sharpen/SKILL.md:1–16](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/sharpen/SKILL.md#L1-L16)

### PK18

- [pstack/skills/correct/SKILL.md:1–32](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/correct/SKILL.md#L1-L32)

### PK19

- [pstack/skills/bro/SKILL.md:1–7](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/bro/SKILL.md#L1-L7)

### PK20

- [pstack/docs/guide/08-principles.md:1–72](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/docs/guide/08-principles.md#L1-L72)

### PK21

- [pstack/docs/guide/09-make-it-yours.md:1–100](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/docs/guide/09-make-it-yours.md#L1-L100)

### PK22

- [pstack/docs/guide/10-recipes-and-pitfalls.md:1–182](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/docs/guide/10-recipes-and-pitfalls.md#L1-L182)

### PK23

- [scripts/validate-plugins.mjs:115–154](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/scripts/validate-plugins.mjs#L115-L154)

### PP01

- [pstack/skills/principle-attack-the-premise/SKILL.md:1–21](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/principle-attack-the-premise/SKILL.md#L1-L21)

### PP02

- [pstack/skills/principle-boundary-discipline/SKILL.md:1–34](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/principle-boundary-discipline/SKILL.md#L1-L34)

### PP03

- [pstack/skills/principle-build-the-lever/SKILL.md:1–23](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/principle-build-the-lever/SKILL.md#L1-L23)

### PP04

- [pstack/skills/principle-encode-lessons-in-structure/SKILL.md:1–11](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/principle-encode-lessons-in-structure/SKILL.md#L1-L11)

### PP05

- [pstack/skills/principle-exhaust-the-design-space/SKILL.md:1–9](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/principle-exhaust-the-design-space/SKILL.md#L1-L9)

### PP06

- [pstack/skills/principle-experience-first/SKILL.md:1–19](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/principle-experience-first/SKILL.md#L1-L19)

### PP07

- [pstack/skills/principle-explain-the-number/SKILL.md:1–17](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/principle-explain-the-number/SKILL.md#L1-L17)

### PP08

- [pstack/skills/principle-fix-root-causes/SKILL.md:1–21](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/principle-fix-root-causes/SKILL.md#L1-L21)

### PP09

- [pstack/skills/principle-foundational-thinking/SKILL.md:1–21](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/principle-foundational-thinking/SKILL.md#L1-L21)

### PP10

- [pstack/skills/principle-guard-the-context-window/SKILL.md:1–12](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/principle-guard-the-context-window/SKILL.md#L1-L12)

### PP11

- [pstack/skills/principle-laziness-protocol/SKILL.md:1–10](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/principle-laziness-protocol/SKILL.md#L1-L10)

### PP12

- [pstack/skills/principle-make-operations-idempotent/SKILL.md:1–22](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/principle-make-operations-idempotent/SKILL.md#L1-L22)

### PP13

- [pstack/skills/principle-migrate-callers-then-delete-legacy-apis/SKILL.md:1–14](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/principle-migrate-callers-then-delete-legacy-apis/SKILL.md#L1-L14)

### PP14

- [pstack/skills/principle-minimize-reader-load/SKILL.md:1–18](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/principle-minimize-reader-load/SKILL.md#L1-L18)

### PP15

- [pstack/skills/principle-model-the-domain/SKILL.md:1–24](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/principle-model-the-domain/SKILL.md#L1-L24)

### PP16

- [pstack/skills/principle-never-block-on-the-human/SKILL.md:1–15](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/principle-never-block-on-the-human/SKILL.md#L1-L15)

### PP17

- [pstack/skills/principle-outcome-oriented-execution/SKILL.md:1–21](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/principle-outcome-oriented-execution/SKILL.md#L1-L21)

### PP18

- [pstack/skills/principle-prove-it-works/SKILL.md:1–22](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/principle-prove-it-works/SKILL.md#L1-L22)

### PP19

- [pstack/skills/principle-redesign-from-first-principles/SKILL.md:1–16](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/principle-redesign-from-first-principles/SKILL.md#L1-L16)

### PP20

- [pstack/skills/principle-separate-before-serializing-shared-state/SKILL.md:1–16](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/principle-separate-before-serializing-shared-state/SKILL.md#L1-L16)

### PP21

- [pstack/skills/principle-sequence-verifiable-units/SKILL.md:1–17](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/principle-sequence-verifiable-units/SKILL.md#L1-L17)

### PP22

- [pstack/skills/principle-subtract-before-you-add/SKILL.md:1–18](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/principle-subtract-before-you-add/SKILL.md#L1-L18)

### PP23

- [pstack/skills/principle-test-behavior-not-implementation/SKILL.md:1–20](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/principle-test-behavior-not-implementation/SKILL.md#L1-L20)

### PP24

- [pstack/skills/principle-type-system-discipline/SKILL.md:1–13](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/principle-type-system-discipline/SKILL.md#L1-L13)

### RE01

- [pstack/skills/how/SKILL.md:3–9](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/how/SKILL.md#L3-L9)
- [pstack/skills/why/SKILL.md:7–9](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/why/SKILL.md#L7-L9)
- [pstack/skills/blast-radius/SKILL.md:9–17](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/blast-radius/SKILL.md#L9-L17)
- [pstack/skills/teach/SKILL.md:9–14](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/teach/SKILL.md#L9-L14)

### RE02

- [pstack/skills/how/SKILL.md:13–28](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/how/SKILL.md#L13-L28)
- [pstack/skills/why/SKILL.md:29–31](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/why/SKILL.md#L29-L31)
- [pstack/skills/teach/SKILL.md:13–14](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/teach/SKILL.md#L13-L14)

### RE03

- [pstack/skills/how/references/explorer-prompt.md:7–35](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/how/references/explorer-prompt.md#L7-L35)
- [pstack/skills/how/references/explainer-prompt.md:17–23](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/how/references/explainer-prompt.md#L17-L23)

### RE04

- [pstack/skills/how/SKILL.md:30–36](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/how/SKILL.md#L30-L36)
- [pstack/skills/how/references/explainer-prompt.md:25–55](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/how/references/explainer-prompt.md#L25-L55)

### RE05

- [pstack/skills/why/SKILL.md:25–27](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/why/SKILL.md#L25-L27)
- [pstack/skills/why/SKILL.md:94–98](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/why/SKILL.md#L94-L98)
- [pstack/skills/why/references/sources/code-archaeology.md:3–51](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/why/references/sources/code-archaeology.md#L3-L51)

### RE06

- [pstack/skills/why/SKILL.md:29–75](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/why/SKILL.md#L29-L75)
- [pstack/skills/why/references/source-playbook.md:1–17](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/why/references/source-playbook.md#L1-L17)
- [pstack/skills/why/references/synthesizer-prompt.md:88–107](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/why/references/synthesizer-prompt.md#L88-L107)

### RE07

- [pstack/skills/why/references/investigator-prompt.md:34–51](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/why/references/investigator-prompt.md#L34-L51)
- [pstack/skills/why/references/investigator-prompt.md:53–84](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/why/references/investigator-prompt.md#L53-L84)
- [pstack/skills/why/references/synthesizer-prompt.md:38–45](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/why/references/synthesizer-prompt.md#L38-L45)

### RE08

- [pstack/skills/why/references/epistemics.md:5–43](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/why/references/epistemics.md#L5-L43)
- [pstack/skills/why/SKILL.md:86–94](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/why/SKILL.md#L86-L94)
- [pstack/skills/why/references/synthesizer-prompt.md:29–36](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/why/references/synthesizer-prompt.md#L29-L36)
- [pstack/skills/teach/SKILL.md:9–14](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/teach/SKILL.md#L9-L14)

### RE09

- [pstack/skills/why/references/epistemics.md:53–71](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/why/references/epistemics.md#L53-L71)
- [pstack/skills/why/references/investigator-prompt.md:41–51](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/why/references/investigator-prompt.md#L41-L51)
- [pstack/skills/why/references/synthesizer-prompt.md:78–95](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/why/references/synthesizer-prompt.md#L78-L95)

### RE10

- [pstack/skills/why/references/sources/linear.md:15–48](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/why/references/sources/linear.md#L15-L48)
- [pstack/skills/why/references/sources/notion.md:16–55](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/why/references/sources/notion.md#L16-L55)
- [pstack/skills/why/references/sources/slack.md:3–17](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/why/references/sources/slack.md#L3-L17)

### RE11

- [pstack/skills/why/references/sources/datadog.md:3–79](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/why/references/sources/datadog.md#L3-L79)
- [pstack/skills/why/references/sources/databricks.md:3–12](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/why/references/sources/databricks.md#L3-L12)
- [pstack/skills/why/references/sources/sentry.md:7–45](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/why/references/sources/sentry.md#L7-L45)
- [pstack/skills/why/references/sources/incident-postmortem.md:1–5](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/why/references/sources/incident-postmortem.md#L1-L5)

### RE12

- [pstack/skills/why/references/sources/datadog.md:81–97](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/why/references/sources/datadog.md#L81-L97)
- [pstack/skills/why/references/sources/databricks.md:52–70](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/why/references/sources/databricks.md#L52-L70)
- [pstack/skills/why/references/sources/slack.md:11–17](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/why/references/sources/slack.md#L11-L17)

### RE13

- [pstack/skills/why/references/sources/databricks.md:14–43](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/why/references/sources/databricks.md#L14-L43)
- [pstack/skills/why/references/sources/databricks.md:62–70](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/why/references/sources/databricks.md#L62-L70)

### RE14

- [pstack/skills/why/references/sources/sentry.md:47–66](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/why/references/sources/sentry.md#L47-L66)
- [pstack/skills/why/references/synthesizer-prompt.md:40–45](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/why/references/synthesizer-prompt.md#L40-L45)
- [pstack/skills/why/SKILL.md:90–94](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/why/SKILL.md#L90-L94)

### RE15

- [pstack/skills/why/SKILL.md:11–17](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/why/SKILL.md#L11-L17)
- [pstack/skills/why/references/synthesizer-prompt.md:40–45](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/why/references/synthesizer-prompt.md#L40-L45)
- [pstack/skills/reflect/SKILL.md:23–39](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/reflect/SKILL.md#L23-L39)

### RE16

- [pstack/skills/architect/SKILL.md:7–9](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/architect/SKILL.md#L7-L9)
- [pstack/skills/architect/SKILL.md:77–79](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/architect/SKILL.md#L77-L79)
- [pstack/skills/architect/references/rationale-template.md:5–35](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/architect/references/rationale-template.md#L5-L35)
- [pstack/skills/architect/references/runner-prompt.md:7–18](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/architect/references/runner-prompt.md#L7-L18)

### RE17

- [pstack/skills/architect/SKILL.md:21–25](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/architect/SKILL.md#L21-L25)
- [pstack/skills/architect/SKILL.md:41–49](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/architect/SKILL.md#L41-L49)
- [pstack/skills/why/SKILL.md:90–94](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/why/SKILL.md#L90-L94)

### RE18

- [pstack/skills/architect/SKILL.md:27–39](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/architect/SKILL.md#L27-L39)
- [pstack/skills/architect/references/runner-prompt.md:3–5](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/architect/references/runner-prompt.md#L3-L5)
- [pstack/skills/architect/references/runner-prompt.md:20–20](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/architect/references/runner-prompt.md#L20-L20)
- [pstack/skills/arena/SKILL.md:15–24](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/arena/SKILL.md#L15-L24)

### RE19

- [pstack/skills/architect/SKILL.md:33–37](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/architect/SKILL.md#L33-L37)
- [pstack/skills/architect/references/design-red-flags.md:5–57](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/architect/references/design-red-flags.md#L5-L57)

### RE20

- [pstack/skills/architect/SKILL.md:51–75](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/architect/SKILL.md#L51-L75)

### RE21

- [pstack/skills/architect/SKILL.md:41–49](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/architect/SKILL.md#L41-L49)
- [pstack/skills/figure-it-out/SKILL.md:15–23](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/figure-it-out/SKILL.md#L15-L23)

### RE22

- [pstack/skills/arena/SKILL.md:11–18](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/arena/SKILL.md#L11-L18)
- [pstack/skills/arena/SKILL.md:26–34](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/arena/SKILL.md#L26-L34)

### RE23

- [pstack/skills/arena/SKILL.md:30–40](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/arena/SKILL.md#L30-L40)

### RE24

- [pstack/skills/arena/SKILL.md:20–24](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/arena/SKILL.md#L20-L24)
- [pstack/skills/arena/SKILL.md:42–48](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/arena/SKILL.md#L42-L48)

### RE25

- [pstack/skills/interrogate/SKILL.md:7–38](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/interrogate/SKILL.md#L7-L38)
- [pstack/skills/interrogate/references/reviewer-prompt.md:7–15](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/interrogate/references/reviewer-prompt.md#L7-L15)

### RE26

- [pstack/skills/interrogate/references/reviewer-prompt.md:29–45](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/interrogate/references/reviewer-prompt.md#L29-L45)
- [pstack/skills/interrogate/references/lead-judgment.md:5–28](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/interrogate/references/lead-judgment.md#L5-L28)
- [pstack/skills/interrogate/references/rubric.md:5–17](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/interrogate/references/rubric.md#L5-L17)

### RE27

- [pstack/skills/interrogate/SKILL.md:40–74](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/interrogate/SKILL.md#L40-L74)
- [pstack/skills/interrogate/references/lead-judgment.md:30–39](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/interrogate/references/lead-judgment.md#L30-L39)

### RE28

- [pstack/skills/interrogate/references/rubric.md:14–17](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/interrogate/references/rubric.md#L14-L17)
- [pstack/skills/interrogate/references/rubric.md:19–77](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/interrogate/references/rubric.md#L19-L77)

### RE29

- [pstack/skills/interrogate/references/code-quality-review.md:19–43](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/interrogate/references/code-quality-review.md#L19-L43)
- [pstack/skills/interrogate/references/lead-judgment.md:13–19](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/interrogate/references/lead-judgment.md#L13-L19)
- [pstack/skills/interrogate/references/rubric.md:41–43](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/interrogate/references/rubric.md#L41-L43)

### RE30

- [pstack/skills/reflect/SKILL.md:11–21](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/reflect/SKILL.md#L11-L21)
- [pstack/skills/reflect/references/judgment-reviewer.md:3–7](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/reflect/references/judgment-reviewer.md#L3-L7)
- [pstack/skills/reflect/references/synthesizer.md:1–3](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/reflect/references/synthesizer.md#L1-L3)

### RE31

- [pstack/skills/reflect/SKILL.md:23–39](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/reflect/SKILL.md#L23-L39)
- [pstack/skills/reflect/references/judgment-reviewer.md:9–16](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/reflect/references/judgment-reviewer.md#L9-L16)
- [pstack/skills/reflect/references/tooling-reviewer.md:7–27](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/reflect/references/tooling-reviewer.md#L7-L27)
- [pstack/skills/reflect/references/divergent-reviewer.md:1–17](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/reflect/references/divergent-reviewer.md#L1-L17)

### RE32

- [pstack/skills/reflect/references/synthesizer.md:13–22](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/reflect/references/synthesizer.md#L13-L22)
- [pstack/skills/reflect/references/judgment-reviewer.md:18–33](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/reflect/references/judgment-reviewer.md#L18-L33)
- [pstack/skills/reflect/references/divergent-reviewer.md:19–34](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/reflect/references/divergent-reviewer.md#L19-L34)
- [pstack/skills/reflect/references/tooling-reviewer.md:29–44](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/reflect/references/tooling-reviewer.md#L29-L44)

### RE33

- [pstack/skills/reflect/references/synthesizer.md:13–34](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/reflect/references/synthesizer.md#L13-L34)
- [pstack/skills/reflect/SKILL.md:41–43](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/reflect/SKILL.md#L41-L43)

### RE34

- [pstack/skills/reflect/SKILL.md:45–69](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/reflect/SKILL.md#L45-L69)
- [pstack/skills/reflect/references/synthesizer.md:36–56](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/reflect/references/synthesizer.md#L36-L56)

### RE35

- [pstack/skills/recall/SKILL.md:9–22](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/recall/SKILL.md#L9-L22)

### RE36

- [pstack/skills/recall/SKILL.md:15–21](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/recall/SKILL.md#L15-L21)

### RE37

- [pstack/skills/recall/SKILL.md:24–35](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/recall/SKILL.md#L24-L35)

### RE38

- [pstack/skills/automate-me/SKILL.md:27–63](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/automate-me/SKILL.md#L27-L63)
- [pstack/skills/automate-me/SKILL.md:85–96](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/automate-me/SKILL.md#L85-L96)

### RE39

- [pstack/skills/automate-me/SKILL.md:15–25](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/automate-me/SKILL.md#L15-L25)
- [pstack/skills/automate-me/SKILL.md:65–98](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/automate-me/SKILL.md#L65-L98)

### RE40

- [pstack/skills/automate-me/SKILL.md:7–11](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/automate-me/SKILL.md#L7-L11)
- [pstack/skills/automate-me/SKILL.md:75–83](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/automate-me/SKILL.md#L75-L83)
- [pstack/skills/automate-me/SKILL.md:100–103](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/automate-me/SKILL.md#L100-L103)

### RE41

- [pstack/skills/ketchup/SKILL.md:9–19](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/ketchup/SKILL.md#L9-L19)
- [pstack/skills/ketchup/SKILL.md:23–29](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/ketchup/SKILL.md#L23-L29)

### RE42

- [pstack/skills/ketchup/SKILL.md:17–33](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/ketchup/SKILL.md#L17-L33)

### RE43

- [pstack/skills/ketchup/SKILL.md:27–43](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/ketchup/SKILL.md#L27-L43)

### RE44

- [pstack/skills/ketchup-video/SKILL.md:9–23](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/ketchup-video/SKILL.md#L9-L23)

### RE45

- [pstack/skills/teach/SKILL.md:9–21](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/teach/SKILL.md#L9-L21)

### RE46

- [pstack/skills/in-your-own-words/SKILL.md:1–7](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/in-your-own-words/SKILL.md#L1-L7)

### RE47

- [pstack/skills/blast-radius/SKILL.md:15–29](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/blast-radius/SKILL.md#L15-L29)
- [pstack/skills/blast-radius/SKILL.md:33–50](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/blast-radius/SKILL.md#L33-L50)

### RE48

- [pstack/skills/blast-radius/SKILL.md:31–48](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/blast-radius/SKILL.md#L31-L48)

### RE49

- [pstack/skills/figure-it-out/SKILL.md:7–34](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/figure-it-out/SKILL.md#L7-L34)

### RE50

- [pstack/skills/figure-it-out/SKILL.md:36–52](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/figure-it-out/SKILL.md#L36-L52)

### RE51

- [pstack/skills/show-me-your-work/SKILL.md:9–22](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/show-me-your-work/SKILL.md#L9-L22)
- [pstack/skills/show-me-your-work/SKILL.md:34–48](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/show-me-your-work/SKILL.md#L34-L48)
- [pstack/skills/show-me-your-work/SKILL.md:76–82](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/show-me-your-work/SKILL.md#L76-L82)
- [pstack/skills/show-me-your-work/references/decision-log-template.tsv:1–1](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/show-me-your-work/references/decision-log-template.tsv#L1-L1)

### RE52

- [pstack/skills/show-me-your-work/SKILL.md:40–63](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/show-me-your-work/SKILL.md#L40-L63)

### RE53

- [pstack/skills/show-me-your-work/scripts/log.sh:1–42](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/show-me-your-work/scripts/log.sh#L1-L42)
- [pstack/skills/show-me-your-work/SKILL.md:38–42](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/show-me-your-work/SKILL.md#L38-L42)

### RE54

- [pstack/skills/show-me-your-work/SKILL.md:55–74](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/show-me-your-work/SKILL.md#L55-L74)

### RE55

- [pstack/automations/benny/README.md:3–23](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/automations/benny/README.md#L3-L23)
- [pstack/automations/benny/FOR_AGENTS.md:55–89](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/automations/benny/FOR_AGENTS.md#L55-L89)
- [pstack/automations/benny/skills/setup-benny/SKILL.md:17–30](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/automations/benny/skills/setup-benny/SKILL.md#L17-L30)
- [pstack/automations/benny/skills/setup-benny/SKILL.md:71–92](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/automations/benny/skills/setup-benny/SKILL.md#L71-L92)

### RE56

- [pstack/automations/benny/skills/setup-benny/SKILL.md:34–69](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/automations/benny/skills/setup-benny/SKILL.md#L34-L69)
- [pstack/automations/benny/FOR_AGENTS.md:77–87](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/automations/benny/FOR_AGENTS.md#L77-L87)

### RE57

- [pstack/automations/benny/skills/setup-benny/SKILL.md:94–138](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/automations/benny/skills/setup-benny/SKILL.md#L94-L138)
- [pstack/automations/benny/skills/setup-benny/SKILL.md:167–266](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/automations/benny/skills/setup-benny/SKILL.md#L167-L266)
- [pstack/automations/benny/FOR_AGENTS.md:83–89](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/automations/benny/FOR_AGENTS.md#L83-L89)

### RE58

- [pstack/automations/benny/templates/configuration.example.yaml:1–84](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/automations/benny/templates/configuration.example.yaml#L1-L84)
- [pstack/automations/benny/skills/setup-benny/SKILL.md:94–116](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/automations/benny/skills/setup-benny/SKILL.md#L94-L116)

### RE59

- [pstack/automations/benny/skills/triage-issue-reports/SKILL.md:13–42](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/automations/benny/skills/triage-issue-reports/SKILL.md#L13-L42)
- [pstack/automations/benny/skills/triage-issue-reports/SKILL.md:200–228](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/automations/benny/skills/triage-issue-reports/SKILL.md#L200-L228)
- [pstack/automations/benny/skills/reproduce-and-fix-issues/SKILL.md:34–54](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/automations/benny/skills/reproduce-and-fix-issues/SKILL.md#L34-L54)
- [pstack/automations/benny/skills/reproduce-and-fix-issues/SKILL.md:105–124](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/automations/benny/skills/reproduce-and-fix-issues/SKILL.md#L105-L124)

### RE60

- [pstack/automations/benny/skills/triage-issue-reports/SKILL.md:20–24](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/automations/benny/skills/triage-issue-reports/SKILL.md#L20-L24)
- [pstack/automations/benny/skills/reproduce-and-fix-issues/SKILL.md:18–23](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/automations/benny/skills/reproduce-and-fix-issues/SKILL.md#L18-L23)
- [pstack/automations/benny/skills/reproduce-and-fix-issues/SKILL.md:242–256](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/automations/benny/skills/reproduce-and-fix-issues/SKILL.md#L242-L256)
- [pstack/automations/benny/templates/reproduce-automation-prompt.md:29–33](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/automations/benny/templates/reproduce-automation-prompt.md#L29-L33)
- [pstack/automations/benny/templates/triage-automation-prompt.md:25–29](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/automations/benny/templates/triage-automation-prompt.md#L25-L29)

### RE61

- [pstack/automations/benny/skills/triage-issue-reports/SKILL.md:214–240](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/automations/benny/skills/triage-issue-reports/SKILL.md#L214-L240)
- [pstack/automations/benny/skills/reproduce-and-fix-issues/SKILL.md:56–78](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/automations/benny/skills/reproduce-and-fix-issues/SKILL.md#L56-L78)
- [pstack/automations/benny/templates/triage-automation-prompt.md:31–39](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/automations/benny/templates/triage-automation-prompt.md#L31-L39)
- [pstack/automations/benny/templates/reproduce-automation-prompt.md:25–29](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/automations/benny/templates/reproduce-automation-prompt.md#L25-L29)

### RE62

- [pstack/automations/benny/templates/triage-automation-prompt.md:13–25](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/automations/benny/templates/triage-automation-prompt.md#L13-L25)
- [pstack/automations/benny/templates/reproduce-automation-prompt.md:13–25](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/automations/benny/templates/reproduce-automation-prompt.md#L13-L25)
- [pstack/automations/benny/skills/triage-issue-reports/SKILL.md:30–39](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/automations/benny/skills/triage-issue-reports/SKILL.md#L30-L39)
- [pstack/automations/benny/skills/reproduce-and-fix-issues/SKILL.md:34–42](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/automations/benny/skills/reproduce-and-fix-issues/SKILL.md#L34-L42)

### RE63

- [pstack/automations/benny/skills/triage-issue-reports/SKILL.md:44–81](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/automations/benny/skills/triage-issue-reports/SKILL.md#L44-L81)

### RE64

- [pstack/automations/benny/skills/triage-issue-reports/SKILL.md:83–125](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/automations/benny/skills/triage-issue-reports/SKILL.md#L83-L125)
- [pstack/automations/benny/skills/triage-issue-reports/references/routing.example.md:3–5](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/automations/benny/skills/triage-issue-reports/references/routing.example.md#L3-L5)
- [pstack/automations/benny/skills/triage-issue-reports/references/routing.example.md:39–61](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/automations/benny/skills/triage-issue-reports/references/routing.example.md#L39-L61)

### RE65

- [pstack/automations/benny/skills/triage-issue-reports/SKILL.md:144–169](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/automations/benny/skills/triage-issue-reports/SKILL.md#L144-L169)

### RE66

- [pstack/automations/benny/skills/triage-issue-reports/SKILL.md:127–142](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/automations/benny/skills/triage-issue-reports/SKILL.md#L127-L142)
- [pstack/automations/benny/skills/triage-issue-reports/SKILL.md:171–198](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/automations/benny/skills/triage-issue-reports/SKILL.md#L171-L198)
- [pstack/automations/benny/templates/configuration.example.yaml:27–39](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/automations/benny/templates/configuration.example.yaml#L27-L39)

### RE67

- [pstack/automations/benny/skills/triage-issue-reports/SKILL.md:171–181](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/automations/benny/skills/triage-issue-reports/SKILL.md#L171-L181)
- [pstack/automations/benny/skills/triage-issue-reports/SKILL.md:200–228](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/automations/benny/skills/triage-issue-reports/SKILL.md#L200-L228)

### RE68

- [pstack/automations/benny/skills/reproduce-and-fix-issues/SKILL.md:80–103](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/automations/benny/skills/reproduce-and-fix-issues/SKILL.md#L80-L103)
- [pstack/automations/benny/skills/reproduce-and-fix-issues/references/verify-existing-fix.md:3–17](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/automations/benny/skills/reproduce-and-fix-issues/references/verify-existing-fix.md#L3-L17)

### RE69

- [pstack/automations/benny/skills/reproduce-and-fix-issues/SKILL.md:105–124](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/automations/benny/skills/reproduce-and-fix-issues/SKILL.md#L105-L124)
- [pstack/automations/benny/skills/reproduce-and-fix-issues/SKILL.md:200–216](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/automations/benny/skills/reproduce-and-fix-issues/SKILL.md#L200-L216)
- [pstack/automations/benny/skills/reproduce-and-fix-issues/SKILL.md:297–310](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/automations/benny/skills/reproduce-and-fix-issues/SKILL.md#L297-L310)
- [pstack/automations/benny/skills/triage-issue-reports/SKILL.md:230–240](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/automations/benny/skills/triage-issue-reports/SKILL.md#L230-L240)

### RE70

- [pstack/automations/benny/skills/reproduce-and-fix-issues/SKILL.md:144–196](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/automations/benny/skills/reproduce-and-fix-issues/SKILL.md#L144-L196)

### RE71

- [pstack/automations/benny/skills/reproduce-and-fix-issues/SKILL.md:126–142](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/automations/benny/skills/reproduce-and-fix-issues/SKILL.md#L126-L142)
- [pstack/automations/benny/skills/reproduce-and-fix-issues/references/control-adapter.md:3–33](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/automations/benny/skills/reproduce-and-fix-issues/references/control-adapter.md#L3-L33)
- [pstack/automations/benny/skills/reproduce-and-fix-issues/references/control-adapter.md:53–68](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/automations/benny/skills/reproduce-and-fix-issues/references/control-adapter.md#L53-L68)
- [pstack/automations/benny/skills/reproduce-and-fix-issues/references/feature-map.example.md:3–57](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/automations/benny/skills/reproduce-and-fix-issues/references/feature-map.example.md#L3-L57)
- [pstack/automations/benny/skills/reproduce-and-fix-issues/references/feature-map.example.md:195–205](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/automations/benny/skills/reproduce-and-fix-issues/references/feature-map.example.md#L195-L205)

### RE72

- [pstack/automations/benny/skills/reproduce-and-fix-issues/references/control-adapter.md:35–83](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/automations/benny/skills/reproduce-and-fix-issues/references/control-adapter.md#L35-L83)
- [pstack/automations/benny/skills/reproduce-and-fix-issues/references/feature-map.example.md:13–52](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/automations/benny/skills/reproduce-and-fix-issues/references/feature-map.example.md#L13-L52)

### RE73

- [pstack/automations/benny/skills/reproduce-and-fix-issues/references/control-adapter.md:85–109](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/automations/benny/skills/reproduce-and-fix-issues/references/control-adapter.md#L85-L109)
- [pstack/automations/benny/skills/reproduce-and-fix-issues/references/feature-map.example.md:59–193](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/automations/benny/skills/reproduce-and-fix-issues/references/feature-map.example.md#L59-L193)

### RE74

- [pstack/automations/benny/skills/reproduce-and-fix-issues/references/control-adapter.md:141–153](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/automations/benny/skills/reproduce-and-fix-issues/references/control-adapter.md#L141-L153)

### RE75

- [pstack/automations/benny/skills/reproduce-and-fix-issues/references/verify-existing-fix.md:19–93](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/automations/benny/skills/reproduce-and-fix-issues/references/verify-existing-fix.md#L19-L93)
- [pstack/automations/benny/skills/reproduce-and-fix-issues/SKILL.md:218–224](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/automations/benny/skills/reproduce-and-fix-issues/SKILL.md#L218-L224)

### RE76

- [pstack/automations/benny/skills/reproduce-and-fix-issues/SKILL.md:214–216](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/automations/benny/skills/reproduce-and-fix-issues/SKILL.md#L214-L216)
- [pstack/automations/benny/skills/reproduce-and-fix-issues/SKILL.md:226–265](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/automations/benny/skills/reproduce-and-fix-issues/SKILL.md#L226-L265)

### RE77

- [pstack/automations/benny/skills/reproduce-and-fix-issues/SKILL.md:267–299](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/automations/benny/skills/reproduce-and-fix-issues/SKILL.md#L267-L299)

### RE78

- [pstack/automations/benny/skills/reproduce-and-fix-issues/references/control-adapter.md:111–139](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/automations/benny/skills/reproduce-and-fix-issues/references/control-adapter.md#L111-L139)
- [pstack/automations/benny/skills/reproduce-and-fix-issues/references/control-adapter.md:155–169](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/automations/benny/skills/reproduce-and-fix-issues/references/control-adapter.md#L155-L169)
- [pstack/automations/benny/skills/reproduce-and-fix-issues/SKILL.md:301–310](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/automations/benny/skills/reproduce-and-fix-issues/SKILL.md#L301-L310)
- [pstack/automations/benny/templates/configuration.example.yaml:47–52](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/automations/benny/templates/configuration.example.yaml#L47-L52)

### VE01

- [pstack/skills/create-verification-skill/SKILL.md:9–21](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/create-verification-skill/SKILL.md#L9-L21)

### VE02

- [pstack/skills/create-verification-skill/SKILL.md:25–32](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/create-verification-skill/SKILL.md#L25-L32)

### VE03

- [pstack/skills/create-verification-skill/SKILL.md:34–44](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/create-verification-skill/SKILL.md#L34-L44)
- [pstack/skills/create-verification-skill/references/feature-map-example/README.md:5–42](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/create-verification-skill/references/feature-map-example/README.md#L5-L42)

### VE04

- [pstack/skills/create-verification-skill/references/feature-map-example/create-note.md:12–39](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/create-verification-skill/references/feature-map-example/create-note.md#L12-L39)
- [pstack/skills/create-verification-skill/references/feature-map-example/search.md:14–45](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/create-verification-skill/references/feature-map-example/search.md#L14-L45)

### VE05

- [pstack/skills/maintain-verification-skill/SKILL.md:9–21](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/maintain-verification-skill/SKILL.md#L9-L21)

### VE06

- [pstack/skills/maintain-verification-skill/SKILL.md:25–39](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/maintain-verification-skill/SKILL.md#L25-L39)

### VE07

- [pstack/skills/create-formal-verification-skill/SKILL.md:9–19](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/create-formal-verification-skill/SKILL.md#L9-L19)

### VE08

- [pstack/skills/create-formal-verification-skill/SKILL.md:23–29](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/create-formal-verification-skill/SKILL.md#L23-L29)

### VE09

- [pstack/skills/create-formal-verification-skill/SKILL.md:31–43](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/create-formal-verification-skill/SKILL.md#L31-L43)

### VE10

- [pstack/skills/maintain-formal-verification-skill/SKILL.md:9–24](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/maintain-formal-verification-skill/SKILL.md#L9-L24)

### VE11

- [pstack/skills/maintain-formal-verification-skill/SKILL.md:28–44](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/maintain-formal-verification-skill/SKILL.md#L28-L44)

### VE12

- [pstack/skills/maintain-formal-verification-skill/SKILL.md:46–58](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/maintain-formal-verification-skill/SKILL.md#L46-L58)

### VE13

- [pstack/skills/statechart/SKILL.md:9–17](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/statechart/SKILL.md#L9-L17)

### VE14

- [pstack/skills/statechart/SKILL.md:21–26](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/statechart/SKILL.md#L21-L26)

### VE15

- [pstack/skills/statechart/SKILL.md:28–36](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/statechart/SKILL.md#L28-L36)

### VE16

- [pstack/skills/statechart/scripts/statechart.mjs:123–152](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/statechart/scripts/statechart.mjs#L123-L152)
- [pstack/skills/statechart/scripts/statechart.mjs:183–231](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/statechart/scripts/statechart.mjs#L183-L231)
- [pstack/skills/statechart/scripts/statechart.mjs:279–351](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/statechart/scripts/statechart.mjs#L279-L351)

### VE17

- [pstack/skills/statechart/scripts/statechart.mjs:354–367](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/statechart/scripts/statechart.mjs#L354-L367)
- [pstack/skills/statechart/scripts/statechart.mjs:548–558](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/statechart/scripts/statechart.mjs#L548-L558)
- [pstack/skills/statechart/scripts/statechart-help.mjs:304–325](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/statechart/scripts/statechart-help.mjs#L304-L325)

### VE18

- [pstack/skills/statechart/scripts/chart-to-tla.mjs:49–143](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/statechart/scripts/chart-to-tla.mjs#L49-L143)
- [pstack/skills/statechart/scripts/chart-to-tla.mjs:145–202](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/statechart/scripts/chart-to-tla.mjs#L145-L202)
- [pstack/skills/statechart/scripts/statechart.mjs:846–889](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/statechart/scripts/statechart.mjs#L846-L889)

### VE19

- [pstack/skills/statechart/scripts/lib.mjs:545–651](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/statechart/scripts/lib.mjs#L545-L651)
- [pstack/skills/statechart/scripts/lib.mjs:742–902](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/statechart/scripts/lib.mjs#L742-L902)
- [pstack/skills/statechart/scripts/compare-charts.mjs:29–74](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/statechart/scripts/compare-charts.mjs#L29-L74)

### VE20

- [pstack/skills/statechart/scripts/tlc-to-chart.mjs:133–160](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/statechart/scripts/tlc-to-chart.mjs#L133-L160)
- [pstack/skills/statechart/scripts/tlc-to-chart.mjs:180–230](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/statechart/scripts/tlc-to-chart.mjs#L180-L230)
- [pstack/skills/statechart/scripts/bug-states.mjs:5–27](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/statechart/scripts/bug-states.mjs#L5-L27)

### VE21

- [pstack/skills/statechart/scripts/bug-states.mjs:29–81](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/statechart/scripts/bug-states.mjs#L29-L81)
- [pstack/skills/statechart/scripts/tlc-to-chart.mjs:270–310](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/statechart/scripts/tlc-to-chart.mjs#L270-L310)

### VE22

- [pstack/skills/statechart/scripts/second-replay.mjs:16–122](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/statechart/scripts/second-replay.mjs#L16-L122)
- [pstack/skills/statechart/scripts/tlc-to-chart.mjs:614–639](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/statechart/scripts/tlc-to-chart.mjs#L614-L639)

### VE23

- [pstack/skills/statechart/scripts/read-check.mjs:5–79](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/statechart/scripts/read-check.mjs#L5-L79)
- [pstack/skills/statechart/scripts/tlc-to-chart.mjs:97–130](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/statechart/scripts/tlc-to-chart.mjs#L97-L130)

### VE24

- [pstack/skills/statechart/scripts/map-view.mjs:3–92](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/statechart/scripts/map-view.mjs#L3-L92)
- [pstack/skills/statechart/scripts/spec-text.mjs:57–78](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/statechart/scripts/spec-text.mjs#L57-L78)

### VE25

- [pstack/skills/statechart/scripts/chart-edges.mjs:13–68](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/statechart/scripts/chart-edges.mjs#L13-L68)
- [pstack/skills/statechart/scripts/tlc-to-chart.mjs:319–335](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/statechart/scripts/tlc-to-chart.mjs#L319-L335)
- [pstack/skills/statechart/scripts/tlc-to-chart.mjs:703–791](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/statechart/scripts/tlc-to-chart.mjs#L703-L791)

### VE26

- [pstack/skills/statechart/scripts/regions-chart.mjs:30–95](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/statechart/scripts/regions-chart.mjs#L30-L95)
- [pstack/skills/statechart/scripts/regions-chart.mjs:174–181](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/statechart/scripts/regions-chart.mjs#L174-L181)
- [pstack/skills/statechart/scripts/regions-chart.mjs:269–307](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/statechart/scripts/regions-chart.mjs#L269-L307)

### VE27

- [pstack/skills/statechart/scripts/tlc-to-chart.mjs:360–414](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/statechart/scripts/tlc-to-chart.mjs#L360-L414)
- [pstack/skills/statechart/scripts/tlc-to-chart.mjs:574–610](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/statechart/scripts/tlc-to-chart.mjs#L574-L610)
- [pstack/skills/statechart/scripts/render.mjs:489–530](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/statechart/scripts/render.mjs#L489-L530)

### VE28

- [pstack/skills/statechart/scripts/property-loop.mjs:7–60](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/statechart/scripts/property-loop.mjs#L7-L60)
- [pstack/skills/statechart/scripts/statechart.mjs:420–457](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/statechart/scripts/statechart.mjs#L420-L457)
- [pstack/skills/statechart/scripts/lib.mjs:340–364](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/statechart/scripts/lib.mjs#L340-L364)

### VE29

- [pstack/skills/statechart/scripts/lib.mjs:196–205](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/statechart/scripts/lib.mjs#L196-L205)
- [pstack/skills/statechart/scripts/lib.mjs:298–337](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/statechart/scripts/lib.mjs#L298-L337)
- [pstack/skills/statechart/scripts/statechart.mjs:797–842](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/statechart/scripts/statechart.mjs#L797-L842)

### VE30

- [pstack/skills/statechart/scripts/rule-book.mjs:20–84](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/statechart/scripts/rule-book.mjs#L20-L84)
- [pstack/skills/statechart/scripts/lib.mjs:250–295](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/statechart/scripts/lib.mjs#L250-L295)
- [pstack/skills/statechart/scripts/ways-in.mjs:4–69](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/statechart/scripts/ways-in.mjs#L4-L69)

### VE31

- [pstack/skills/statechart/scripts/snapshot.mjs:6–74](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/statechart/scripts/snapshot.mjs#L6-L74)
- [pstack/skills/statechart/scripts/statechart.mjs:688–728](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/statechart/scripts/statechart.mjs#L688-L728)

### VE32

- [pstack/skills/statechart/scripts/statechart.mjs:581–624](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/statechart/scripts/statechart.mjs#L581-L624)
- [pstack/skills/statechart/scripts/statechart.mjs:626–686](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/statechart/scripts/statechart.mjs#L626-L686)
- [pstack/skills/statechart/scripts/statechart-help.mjs:136–147](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/statechart/scripts/statechart-help.mjs#L136-L147)

### VE33

- [pstack/skills/statechart/scripts/tlc-tools.mjs:7–63](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/statechart/scripts/tlc-tools.mjs#L7-L63)
- [pstack/skills/statechart/scripts/render.mjs:9–71](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/statechart/scripts/render.mjs#L9-L71)

### VE34

- [pstack/skills/statechart/scripts/lib.mjs:455–496](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/statechart/scripts/lib.mjs#L455-L496)
- [pstack/skills/statechart/scripts/statechart.mjs:155–180](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/statechart/scripts/statechart.mjs#L155-L180)
- [pstack/skills/statechart/scripts/statechart.mjs:369–375](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/statechart/scripts/statechart.mjs#L369-L375)

### VE35

- [pstack/skills/benchmark-checklist/SKILL.md:9–27](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/benchmark-checklist/SKILL.md#L9-L27)
- [pstack/skills/benchmark-checklist/SKILL.md:29–39](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/benchmark-checklist/SKILL.md#L29-L39)

### VE36

- [pstack/skills/tdd/SKILL.md:3–42](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/tdd/SKILL.md#L3-L42)

### VE37

- [pstack/skills/statechart/scripts/test/statechart.test.mjs:76–147](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/statechart/scripts/test/statechart.test.mjs#L76-L147)
- [pstack/skills/statechart/scripts/test/statechart.test.mjs:425–800](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/statechart/scripts/test/statechart.test.mjs#L425-L800)
- [pstack/skills/statechart/scripts/test/statechart.test.mjs:968–1316](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/statechart/scripts/test/statechart.test.mjs#L968-L1316)

### VE38

- [pstack/skills/statechart/scripts/test/statechart.test.mjs:1416–1674](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/statechart/scripts/test/statechart.test.mjs#L1416-L1674)
- [pstack/skills/statechart/scripts/statechart.mjs:892–903](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/statechart/scripts/statechart.mjs#L892-L903)

### VE39

- [pstack/skills/statechart/scripts/test/statechart.test.mjs:1676–1687](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/statechart/scripts/test/statechart.test.mjs#L1676-L1687)
- [pstack/skills/statechart/scripts/test/statechart.test.mjs:2987–3130](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/statechart/scripts/test/statechart.test.mjs#L2987-L3130)
- [pstack/skills/statechart/scripts/test/statechart.test.mjs:4077–4327](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/statechart/scripts/test/statechart.test.mjs#L4077-L4327)

### VE40

- [pstack/skills/statechart/scripts/test/statechart.test.mjs:4984–5303](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/statechart/scripts/test/statechart.test.mjs#L4984-L5303)
- [pstack/skills/statechart/scripts/test/statechart.test.mjs:5925–6011](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/statechart/scripts/test/statechart.test.mjs#L5925-L6011)
- [pstack/skills/statechart/scripts/test/statechart.test.mjs:6377–6413](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/statechart/scripts/test/statechart.test.mjs#L6377-L6413)
- [pstack/skills/statechart/scripts/test/statechart.test.mjs:6791–6854](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/statechart/scripts/test/statechart.test.mjs#L6791-L6854)

### VE41

- [pstack/skills/statechart/scripts/lib.mjs:7–101](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/statechart/scripts/lib.mjs#L7-L101)
- [pstack/skills/statechart/scripts/lib.mjs:121–132](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/statechart/scripts/lib.mjs#L121-L132)

### VE42

- [pstack/skills/statechart/scripts/statechart-help.mjs:203–273](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/statechart/scripts/statechart-help.mjs#L203-L273)

### VE43

- [pstack/skills/statechart/scripts/test/statechart.test.mjs:5925–5955](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/statechart/scripts/test/statechart.test.mjs#L5925-L5955)
- [pstack/skills/statechart/scripts/statechart.mjs:155–180](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/statechart/scripts/statechart.mjs#L155-L180)

### VE44

- [pstack/skills/statechart/scripts/test/statechart.test.mjs:6427–6477](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/statechart/scripts/test/statechart.test.mjs#L6427-L6477)
- [pstack/skills/statechart/scripts/statechart.mjs:295–309](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/statechart/scripts/statechart.mjs#L295-L309)
- [pstack/skills/statechart/scripts/statechart.mjs:354–367](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/statechart/scripts/statechart.mjs#L354-L367)

### VE45

- [pstack/skills/statechart/scripts/statechart.mjs:748–795](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/statechart/scripts/statechart.mjs#L748-L795)
- [pstack/skills/statechart/scripts/statechart-help.mjs:29–49](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/statechart/scripts/statechart-help.mjs#L29-L49)

### VE46

- [pstack/skills/statechart/scripts/spec-text.mjs:25–43](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/statechart/scripts/spec-text.mjs#L25-L43)
- [pstack/skills/statechart/scripts/statechart.mjs:327–351](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/statechart/scripts/statechart.mjs#L327-L351)

### VE47

- [pstack/skills/statechart/scripts/statechart-help.mjs:287–325](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/statechart/scripts/statechart-help.mjs#L287-L325)
- [pstack/skills/statechart/scripts/test/statechart.test.mjs:6544–6754](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/statechart/scripts/test/statechart.test.mjs#L6544-L6754)

### VE48

- [pstack/skills/statechart/scripts/render.mjs:74–131](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/statechart/scripts/render.mjs#L74-L131)
- [pstack/skills/statechart/scripts/render.mjs:254–331](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/statechart/scripts/render.mjs#L254-L331)
- [pstack/skills/statechart/scripts/render.mjs:469–530](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/statechart/scripts/render.mjs#L469-L530)

### VE49

- [pstack/.cursor-plugin/plugin.json:1–11](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/.cursor-plugin/plugin.json#L1-L11)
- [pstack/LICENSE:1–21](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/LICENSE#L1-L21)
- [pstack/skills/statechart/SKILL.md:1–36](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/statechart/SKILL.md#L1-L36)
- [harness/pstack/claude-code/skills/create-verification-skill/SKILL.md:7–11](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/harness/pstack/claude-code/skills/create-verification-skill/SKILL.md#L7-L11)

### VE50

- [pstack/skills/statechart/scripts/statechart.mjs:369–378](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/statechart/scripts/statechart.mjs#L369-L378)
- [pstack/skills/statechart/scripts/statechart.mjs:812–842](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/statechart/scripts/statechart.mjs#L812-L842)
- [pstack/skills/statechart/scripts/statechart.mjs:249–265](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/statechart/scripts/statechart.mjs#L249-L265)

### OR01

- [pstack/skills/poteto-mode/SKILL.md:1–7](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/SKILL.md#L1-L7)
- [pstack/skills/poteto-mode/SKILL.md:15–36](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/SKILL.md#L15-L36)
- [pstack/skills/poteto-mode/SKILL.md:121–149](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/SKILL.md#L121-L149)

### OR02

- [pstack/skills/poteto-mode/SKILL.md:18–20](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/SKILL.md#L18-L20)
- [pstack/skills/poteto-mode/SKILL.md:81–89](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/SKILL.md#L81-L89)
- [pstack/skills/poteto-mode/playbooks/prototype.md:3–14](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/playbooks/prototype.md#L3-L14)

### OR03

- [pstack/skills/poteto-mode/SKILL.md:91–101](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/SKILL.md#L91-L101)
- [pstack/agents/poteto-agent.md:1–9](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/agents/poteto-agent.md#L1-L9)

### OR04

- [pstack/skills/poteto-mode/playbooks/feature.md:5–19](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/playbooks/feature.md#L5-L19)
- [pstack/skills/poteto-mode/SKILL.md:59–60](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/SKILL.md#L59-L60)

### OR05

- [pstack/skills/poteto-mode/playbooks/orchestrate.md:13–19](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/playbooks/orchestrate.md#L13-L19)
- [pstack/skills/poteto-mode/playbooks/orchestrate.md:38–57](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/playbooks/orchestrate.md#L38-L57)

### OR06

- [pstack/skills/poteto-mode/playbooks/orchestrate.md:59–76](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/playbooks/orchestrate.md#L59-L76)

### OR07

- [pstack/skills/poteto-mode/playbooks/orchestrate.md:21–36](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/playbooks/orchestrate.md#L21-L36)
- [pstack/skills/poteto-mode/scripts/orch/store.ts:1642–1681](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/scripts/orch/store.ts#L1642-L1681)

### OR08

- [pstack/skills/poteto-mode/scripts/orch/store.ts:297–347](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/scripts/orch/store.ts#L297-L347)
- [pstack/skills/poteto-mode/scripts/orch/store.ts:444–473](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/scripts/orch/store.ts#L444-L473)

### OR09

- [pstack/skills/poteto-mode/scripts/orch/store.ts:369–441](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/scripts/orch/store.ts#L369-L441)
- [pstack/skills/poteto-mode/scripts/orch/store.ts:1288–1314](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/scripts/orch/store.ts#L1288-L1314)

### OR10

- [pstack/skills/poteto-mode/scripts/orch/store.ts:1317–1368](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/scripts/orch/store.ts#L1317-L1368)

### OR11

- [pstack/skills/poteto-mode/scripts/orch/store.ts:1404–1450](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/scripts/orch/store.ts#L1404-L1450)
- [pstack/skills/poteto-mode/playbooks/orchestrate.md:78–92](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/playbooks/orchestrate.md#L78-L92)

### OR12

- [pstack/skills/poteto-mode/scripts/orch/orch.ts:370–382](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/scripts/orch/orch.ts#L370-L382)
- [pstack/skills/poteto-mode/scripts/orch/orch.ts:572–585](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/scripts/orch/orch.ts#L572-L585)
- [pstack/skills/poteto-mode/scripts/orch/store.ts:1431–1450](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/scripts/orch/store.ts#L1431-L1450)

### OR13

- [pstack/skills/poteto-mode/scripts/orch/store.ts:1453–1500](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/scripts/orch/store.ts#L1453-L1500)
- [pstack/skills/poteto-mode/playbooks/orchestrate.md:69–76](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/playbooks/orchestrate.md#L69-L76)

### OR14

- [pstack/skills/poteto-mode/scripts/orch/store.ts:1158–1271](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/scripts/orch/store.ts#L1158-L1271)
- [pstack/skills/poteto-mode/scripts/orch/store.ts:1556–1585](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/scripts/orch/store.ts#L1556-L1585)

### OR15

- [pstack/skills/poteto-mode/scripts/orch/store.ts:765–881](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/scripts/orch/store.ts#L765-L881)

### OR16

- [pstack/skills/poteto-mode/playbooks/orchestrate.md:78–108](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/playbooks/orchestrate.md#L78-L108)

### OR17

- [pstack/skills/poteto-mode/playbooks/autopilot-full.md:3–25](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/playbooks/autopilot-full.md#L3-L25)
- [pstack/skills/poteto-mode/playbooks/autopilot-stack.md:3–12](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/playbooks/autopilot-stack.md#L3-L12)

### OR18

- [pstack/skills/poteto-mode/playbooks/shipping.md:3–12](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/playbooks/shipping.md#L3-L12)
- [pstack/skills/poteto-mode/playbooks/orchestrate.md:78–92](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/playbooks/orchestrate.md#L78-L92)

### OR19

- [pstack/skills/poteto-mode/playbooks/babysit.md:3–23](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/playbooks/babysit.md#L3-L23)

### OR20

- [pstack/skills/poteto-mode/scripts/watch-pr/github.ts:29–49](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/scripts/watch-pr/github.ts#L29-L49)
- [pstack/skills/poteto-mode/scripts/watch-pr/github.ts:613–646](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/scripts/watch-pr/github.ts#L613-L646)
- [pstack/skills/poteto-mode/scripts/watch-pr/policy.ts:59–139](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/scripts/watch-pr/policy.ts#L59-L139)

### OR21

- [pstack/skills/poteto-mode/scripts/watch-pr/policy.ts:8–31](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/scripts/watch-pr/policy.ts#L8-L31)
- [pstack/skills/poteto-mode/scripts/watch-pr/policy.ts:145–173](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/scripts/watch-pr/policy.ts#L145-L173)
- [pstack/skills/poteto-mode/scripts/watch-pr/github.ts:253–270](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/scripts/watch-pr/github.ts#L253-L270)
- [pstack/skills/poteto-mode/playbooks/babysit.md:10–14](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/playbooks/babysit.md#L10-L14)

### OR22

- [pstack/skills/poteto-mode/scripts/watch-pr/github.ts:325–389](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/scripts/watch-pr/github.ts#L325-L389)
- [pstack/skills/poteto-mode/scripts/watch-pr/github.ts:529–585](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/scripts/watch-pr/github.ts#L529-L585)
- [pstack/skills/poteto-mode/scripts/watch-pr/github.ts:613–646](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/scripts/watch-pr/github.ts#L613-L646)

### OR23

- [pstack/skills/poteto-mode/scripts/watch-pr/types.ts:1–105](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/scripts/watch-pr/types.ts#L1-L105)
- [pstack/skills/poteto-mode/scripts/watch-pr/types.ts:211–344](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/scripts/watch-pr/types.ts#L211-L344)
- [pstack/skills/poteto-mode/scripts/watch-pr/types.compile.ts:1–93](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/scripts/watch-pr/types.compile.ts#L1-L93)

### OR24

- [pstack/skills/poteto-mode/scripts/watch-pr/policy.ts:214–269](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/scripts/watch-pr/policy.ts#L214-L269)

### OR25

- [pstack/skills/poteto-mode/scripts/watch-pr/policy.ts:526–612](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/scripts/watch-pr/policy.ts#L526-L612)
- [pstack/skills/poteto-mode/scripts/watch-pr/policy.ts:613–711](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/scripts/watch-pr/policy.ts#L613-L711)

### OR26

- [pstack/skills/poteto-mode/scripts/watch-pr/policy.ts:266–269](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/scripts/watch-pr/policy.ts#L266-L269)
- [pstack/skills/poteto-mode/scripts/watch-pr/policy.ts:365–420](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/scripts/watch-pr/policy.ts#L365-L420)
- [pstack/skills/poteto-mode/scripts/watch-pr/github.ts:29–49](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/scripts/watch-pr/github.ts#L29-L49)
- [pstack/skills/poteto-mode/scripts/watch-pr/cli.ts:20–136](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/scripts/watch-pr/cli.ts#L20-L136)

### OR27

- [pstack/skills/poteto-mode/scripts/watch-pr/github.ts:672–726](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/scripts/watch-pr/github.ts#L672-L726)
- [pstack/skills/poteto-mode/scripts/orch/store.ts:1188–1238](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/scripts/orch/store.ts#L1188-L1238)

### OR28

- [pstack/skills/poteto-mode/scripts/watch-pr/render.ts:1–169](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/scripts/watch-pr/render.ts#L1-L169)
- [pstack/skills/poteto-mode/scripts/watch-pr/types.ts:259–414](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/scripts/watch-pr/types.ts#L259-L414)
- [pstack/skills/poteto-mode/scripts/watch-pr/cli.ts:137–223](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/scripts/watch-pr/cli.ts#L137-L223)

### OR29

- [pstack/skills/poteto-mode/scripts/bootstrap.ts:1–62](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/scripts/bootstrap.ts#L1-L62)
- [pstack/skills/poteto-mode/scripts/package.json:1–16](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/scripts/package.json#L1-L16)
- [pstack/skills/poteto-mode/scripts/watch-pr/cli.ts:1–18](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/scripts/watch-pr/cli.ts#L1-L18)
- [pstack/skills/poteto-mode/scripts/orch/orch.ts:1–20](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/scripts/orch/orch.ts#L1-L20)

### OR30

- [pstack/skills/poteto-mode/scripts/check-plan.mjs:5–29](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/scripts/check-plan.mjs#L5-L29)
- [pstack/skills/poteto-mode/scripts/check-plan.mjs:48–81](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/scripts/check-plan.mjs#L48-L81)
- [pstack/skills/poteto-mode/scripts/check-plan.mjs:129–205](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/scripts/check-plan.mjs#L129-L205)

### OR31

- [pstack/skills/poteto-mode/playbooks/multi-phase-plan.md:3–48](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/playbooks/multi-phase-plan.md#L3-L48)
- [pstack/skills/poteto-mode/playbooks/multi-phase-plan.md:84–155](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/playbooks/multi-phase-plan.md#L84-L155)

### OR32

- [pstack/skills/swarm/SKILL.md:18–41](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/swarm/SKILL.md#L18-L41)

### OR33

- [pstack/skills/poteto-mode/playbooks/eval.md:3–25](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/playbooks/eval.md#L3-L25)

### OR34

- [pstack/skills/poteto-mode/playbooks/hillclimb.md:3–21](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/playbooks/hillclimb.md#L3-L21)

### OR35

- [pstack/skills/poteto-mode/playbooks/perf-issue.md:3–25](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/playbooks/perf-issue.md#L3-L25)

### OR36

- [pstack/skills/poteto-mode/playbooks/bug-fix.md:3–15](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/playbooks/bug-fix.md#L3-L15)

### OR37

- [pstack/skills/poteto-mode/playbooks/refactoring.md:3–16](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/playbooks/refactoring.md#L3-L16)

### OR38

- [pstack/skills/poteto-mode/playbooks/prototype.md:3–14](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/playbooks/prototype.md#L3-L14)
- [pstack/skills/poteto-mode/playbooks/investigation.md:3–14](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/playbooks/investigation.md#L3-L14)

### OR39

- [pstack/skills/poteto-mode/playbooks/runtime-forensics.md:3–11](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/playbooks/runtime-forensics.md#L3-L11)
- [pstack/skills/poteto-mode/playbooks/trace-forensics.md:3–14](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/playbooks/trace-forensics.md#L3-L14)

### OR40

- [pstack/skills/poteto-mode/playbooks/visual-parity.md:3–11](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/playbooks/visual-parity.md#L3-L11)

### OR41

- [pstack/skills/poteto-mode/playbooks/authoring-a-skill.md:3–12](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/playbooks/authoring-a-skill.md#L3-L12)

### OR42

- [pstack/agents/comment-sicko.md:1–32](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/agents/comment-sicko.md#L1-L32)

### OR43

- [pstack/skills/poteto-mode/references/bugbot-triage.md:5–54](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/references/bugbot-triage.md#L5-L54)
- [pstack/skills/poteto-mode/references/bugbot-triage.md:81–142](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/references/bugbot-triage.md#L81-L142)
- [pstack/skills/poteto-mode/playbooks/babysit.md:17–21](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/playbooks/babysit.md#L17-L21)

### OR44

- [pstack/skills/poteto-mode/playbooks/session-pickup.md:3–11](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/playbooks/session-pickup.md#L3-L11)

### OR45

- [pstack/skills/poteto-mode/playbooks/pause-safely.md:3–10](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/playbooks/pause-safely.md#L3-L10)

### OR46

- [pstack/skills/poteto-mode/playbooks/worktree-cleanup.md:3–12](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/playbooks/worktree-cleanup.md#L3-L12)
- [pstack/skills/poteto-mode/scripts/worktree-audit.sh:74–134](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/scripts/worktree-audit.sh#L74-L134)

### OR47

- [pstack/skills/poteto-mode/scripts/worktree-audit.sh:1–73](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/scripts/worktree-audit.sh#L1-L73)
- [pstack/skills/poteto-mode/scripts/worktree-audit.sh:80–81](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/scripts/worktree-audit.sh#L80-L81)

### OR48

- [pstack/skills/poteto-mode/playbooks/opening-a-pr.md:3–34](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/playbooks/opening-a-pr.md#L3-L34)

### OR49

- [pstack/skills/poteto-mode/playbooks/autonomous-run.md:3–13](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/playbooks/autonomous-run.md#L3-L13)

### OR50

- [pstack/skills/poteto-help/SKILL.md:1–41](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-help/SKILL.md#L1-L41)
- [pstack/skills/poteto-help/SKILL.md:111–163](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-help/SKILL.md#L111-L163)

### OR51

- [pstack/skills/poteto-help/references/prompting.md:1–51](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-help/references/prompting.md#L1-L51)
- [pstack/skills/poteto-help/references/recipes.md:1–51](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-help/references/recipes.md#L1-L51)

### OR52

- [pstack/skills/poteto-mode/scripts/watch-pr/github.test.ts:1–498](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/scripts/watch-pr/github.test.ts#L1-L498)
- [pstack/skills/poteto-mode/scripts/watch-pr/policy.test.ts:1–482](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/scripts/watch-pr/policy.test.ts#L1-L482)
- [pstack/skills/poteto-mode/scripts/check-plan.test.ts:1–110](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/scripts/check-plan.test.ts#L1-L110)

### OR53

- [pstack/skills/poteto-mode/scripts/orch/orch.test.ts:1–795](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/scripts/orch/orch.test.ts#L1-L795)
- [pstack/skills/poteto-mode/scripts/watch-pr/cli.test.ts:1–224](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/scripts/watch-pr/cli.test.ts#L1-L224)

### OR54

- [.github/workflows/validate-plugins.yml:15–35](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/.github/workflows/validate-plugins.yml#L15-L35)
- [pstack/skills/poteto-mode/scripts/package.json:1–16](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/scripts/package.json#L1-L16)
- [pstack/skills/poteto-mode/scripts/watch-pr/tsconfig.json:1–13](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/pstack/skills/poteto-mode/scripts/watch-pr/tsconfig.json#L1-L13)

## Why we cite this

A coherent system linking engineering principles, bounded investigation, orchestration, and verification maintenance. Source and local observations support mechanisms and limits; comparative quality, adoption, and deployed reliability remain unmeasured.

## Related sources

- [[sources/humanlayer--humanlayer]] — artifact-centered context, review, and control-plane comparison.
- [[sources/mattpocock--skills]] — engineering craft and skill invocation/discovery comparison.
- [[sources/every--compound-engineering-plugin]] — compounding workflow and cross-harness distribution comparison.
