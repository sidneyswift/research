---
domain: sources
type: repo
url: https://github.com/humanlayer/humanlayer
retrieved: 2026-10-23
snapshot-location: sources/humanlayer--humanlayer/
upstream-commit: 2f66a45b186d88488fa356862be0117db1ccae9f
last-reviewed: 2026-10-23
---

# humanlayer/humanlayer — collaborative coding-agent control plane

> Pinned source evidence for the HumanLayer system, RPI workflow, context management, collaboration, runtime reliability, and development practices.

## Snapshot details

- **Retrieved:** October 23, 2026 (America/New_York).
- **Revision:** `2f66a45b186d88488fa356862be0117db1ccae9f`; commit time October 23, 2026, 10:13:27 PM Eastern (Git author timestamp `2026-10-23T19:13:27-07:00`).
- **Evidence clone:** `sources/humanlayer--humanlayer/`, independent Git object storage, canonical upstream remote, git-ignored and listed in `repos.manifest.tsv`. Rebuild using `sources/clone-all.sh`.
- **Inventory:** 5,856 tracked files in the cloned revision; this anchor map covers **150 distinct files**. Coverage is a purposeful cross-section, not a claim to have read every file or audited every subsystem.
- **Method:** root investigator plus three focused read-only investigations; owning implementations checked against docs, prompts, schemas, and selected tests. Source text and line-range integrity verified at the pinned revision.
- **Not performed:** installation, application launch, live provider calls, benchmarks, security audit, model evals, or execution of HumanLayer's test suites. Tests cited below were inspected, not run.
- **Generation boundary:** this is the current Riptide-era monorepo, not a reconstruction of earlier HumanLayer SDK or CodeLayer generations. Git history shows a repository replacement/update and deprecated-package removal immediately before this snapshot; historical implementations were not ingested as current features.

## Evidence classes

**Implementation** supports a claim about inspected source paths. **Test inspected** supports the existence and intent of a test, not a passing result. **Prompt policy** means instructions packaged for an agent, not enforced authorization. **Documentation** states the maintainer's intended contract. **Inference / reuse** is our interpretation or proposed application. Production correctness and quantitative benefit require separate evidence.

## Anchor map

Each heading below is a registered citation anchor. All file links are immutable GitHub permalinks at `2f66a45b186d88488fa356862be0117db1ccae9f`. Friendly anchors group related evidence; WF, RT, and HP anchors allow precise ledger citations.

### repository-metadata

GitHub repository API read on October 23, 2026: **11,977 stars**, **971 forks**, public, Apache-2.0, default branch `main`. [API source](https://api.github.com/repos/humanlayer/humanlayer). These counts measure repository attention, not active users, safety, or effectiveness. The values are captured here as dated metadata; the API URL remains live.

### root

- [README.md:1–50](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/README.md#L1-L50)

### workflow-phases

- [apps/docs/explanation/workflow-phases.md:1–128](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/docs/explanation/workflow-phases.md#L1-L128)

### remote-hosts

- [apps/docs/explanation/remote-daemons.md:68–121](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/docs/explanation/remote-daemons.md#L68-L121)
- [apps/docs/explanation/remote-daemons.md:157–173](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/docs/explanation/remote-daemons.md#L157-L173)

### ui-copy

- [.claude/skills/ui-copy/SKILL.md:10–43](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/.claude/skills/ui-copy/SKILL.md#L10-L43)
- [.claude/skills/ui-copy/SKILL.md:85–140](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/.claude/skills/ui-copy/SKILL.md#L85-L140)

### automation

- [apps/docs/guide/automation-sessions.md:3–35](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/docs/guide/automation-sessions.md#L3-L35)
- [apps/docs/guide/automation-sessions.md:151–159](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/docs/guide/automation-sessions.md#L151-L159)

### eval-pipeline

- [packages/ai/eval/doc-researcher/runner.ts:13–83](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/packages/ai/eval/doc-researcher/runner.ts#L13-L83)
- [packages/ai/eval/doc-researcher/judge.ts:35–77](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/packages/ai/eval/doc-researcher/judge.ts#L35-L77)
- [packages/ai/eval/doc-researcher/doc-research.test.ts:27–77](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/packages/ai/eval/doc-researcher/doc-research.test.ts#L27-L77)
- [packages/ai/eval/_lib/matrix.ts:15–27](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/packages/ai/eval/_lib/matrix.ts#L15-L27)

### WF01

- [apps/docs/explanation/workflow-phases.md:3–34](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/docs/explanation/workflow-phases.md#L3-L34)
- [apps/docs/explanation/workflow-phases.md:94–126](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/docs/explanation/workflow-phases.md#L94-L126)

### WF02

- [apps/docs/guide/skills-workflows.md:9–20](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/docs/guide/skills-workflows.md#L9-L20)
- [apps/docs/reference/skills-workflows.md:13–20](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/docs/reference/skills-workflows.md#L13-L20)
- [apps/docs/reference/skills-workflows.md:300–325](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/docs/reference/skills-workflows.md#L300-L325)
- [apps/riptide-humanlayer-claude-plugin/skills/orchestrate/references/launch-task.md:11–27](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-humanlayer-claude-plugin/skills/orchestrate/references/launch-task.md#L11-L27)

### WF03

- [apps/riptide-rpi-claude-plugin/skills/create-research-questions/SKILL.md:8–24](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-rpi-claude-plugin/skills/create-research-questions/SKILL.md#L8-L24)
- [apps/riptide-rpi-claude-plugin/skills/create-research-questions/SKILL.md:46–78](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-rpi-claude-plugin/skills/create-research-questions/SKILL.md#L46-L78)

### WF04

- [apps/riptide-rpi-claude-plugin/skills/create-research/SKILL.md:10–40](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-rpi-claude-plugin/skills/create-research/SKILL.md#L10-L40)
- [apps/riptide-rpi-claude-plugin/skills/create-research/SKILL.md:50–82](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-rpi-claude-plugin/skills/create-research/SKILL.md#L50-L82)
- [apps/riptide-rpi-claude-plugin/skills/create-research/SKILL.md:102–112](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-rpi-claude-plugin/skills/create-research/SKILL.md#L102-L112)

### WF05

- [apps/riptide-rpi-claude-plugin/skills/create-research/references/research_template.md:1–17](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-rpi-claude-plugin/skills/create-research/references/research_template.md#L1-L17)
- [apps/riptide-rpi-claude-plugin/skills/create-research/references/research_template.md:36–77](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-rpi-claude-plugin/skills/create-research/references/research_template.md#L36-L77)
- [apps/riptide-rpi-claude-plugin/skills/create-research/SKILL.md:124–175](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-rpi-claude-plugin/skills/create-research/SKILL.md#L124-L175)

### WF06

- [apps/riptide-daemon/src/agents/claudecode/agents/codebase-locator.ts:3–35](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/agents/claudecode/agents/codebase-locator.ts#L3-L35)
- [apps/riptide-daemon/src/agents/claudecode/agents/codebase-locator.ts:96–120](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/agents/claudecode/agents/codebase-locator.ts#L96-L120)
- [apps/riptide-daemon/src/agents/claudecode/agents/codebase-analyzer.ts:3–58](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/agents/claudecode/agents/codebase-analyzer.ts#L3-L58)
- [apps/riptide-daemon/src/agents/claudecode/agents/codebase-analyzer.ts:115–143](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/agents/claudecode/agents/codebase-analyzer.ts#L115-L143)

### WF07

- [apps/riptide-rpi-claude-plugin/skills/create-design-discussion/SKILL.md:68–93](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-rpi-claude-plugin/skills/create-design-discussion/SKILL.md#L68-L93)
- [apps/riptide-rpi-claude-plugin/skills/create-design-discussion/SKILL.md:127–133](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-rpi-claude-plugin/skills/create-design-discussion/SKILL.md#L127-L133)

### WF08

- [apps/riptide-rpi-claude-plugin/skills/create-prd/SKILL.md:8–28](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-rpi-claude-plugin/skills/create-prd/SKILL.md#L8-L28)
- [apps/riptide-rpi-claude-plugin/skills/create-prd/SKILL.md:43–54](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-rpi-claude-plugin/skills/create-prd/SKILL.md#L43-L54)
- [apps/riptide-rpi-claude-plugin/skills/create-prd/SKILL.md:93–116](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-rpi-claude-plugin/skills/create-prd/SKILL.md#L93-L116)

### WF09

- [apps/riptide-rpi-claude-plugin/skills/create-prd/SKILL.md:138–145](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-rpi-claude-plugin/skills/create-prd/SKILL.md#L138-L145)
- [apps/riptide-rpi-claude-plugin/skills/create-tdd/SKILL.md:8–33](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-rpi-claude-plugin/skills/create-tdd/SKILL.md#L8-L33)
- [apps/riptide-rpi-claude-plugin/skills/create-tdd/SKILL.md:160–167](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-rpi-claude-plugin/skills/create-tdd/SKILL.md#L160-L167)
- [apps/riptide-rpi-claude-plugin/skills/create-tdd/SKILL.md:268–275](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-rpi-claude-plugin/skills/create-tdd/SKILL.md#L268-L275)

### WF10

- [apps/riptide-rpi-claude-plugin/skills/create-tdd/SKILL.md:95–143](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-rpi-claude-plugin/skills/create-tdd/SKILL.md#L95-L143)
- [apps/riptide-rpi-claude-plugin/skills/create-tdd/SKILL.md:172–258](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-rpi-claude-plugin/skills/create-tdd/SKILL.md#L172-L258)

### WF11

- [apps/riptide-humanlayer-claude-plugin/skills/show-me/SKILL.md:6–58](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-humanlayer-claude-plugin/skills/show-me/SKILL.md#L6-L58)
- [apps/riptide-humanlayer-claude-plugin/skills/show-me/SKILL.md:108–123](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-humanlayer-claude-plugin/skills/show-me/SKILL.md#L108-L123)
- [apps/riptide-rpi-claude-plugin/skills/create-prd/SKILL.md:49–54](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-rpi-claude-plugin/skills/create-prd/SKILL.md#L49-L54)
- [apps/riptide-rpi-claude-plugin/skills/create-prd/SKILL.md:120–133](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-rpi-claude-plugin/skills/create-prd/SKILL.md#L120-L133)

### WF12

- [apps/riptide-rpi-claude-plugin/skills/create-structure-outline/SKILL.md:38–82](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-rpi-claude-plugin/skills/create-structure-outline/SKILL.md#L38-L82)
- [apps/riptide-rpi-claude-plugin/skills/create-structure-outline/SKILL.md:157–181](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-rpi-claude-plugin/skills/create-structure-outline/SKILL.md#L157-L181)

### WF13

- [apps/riptide-rpi-claude-plugin/skills/implement-outline/SKILL.md:8–52](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-rpi-claude-plugin/skills/implement-outline/SKILL.md#L8-L52)
- [apps/riptide-rpi-claude-plugin/skills/implement-outline/SKILL.md:69–113](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-rpi-claude-plugin/skills/implement-outline/SKILL.md#L69-L113)
- [apps/riptide-daemon/src/agents/claudecode/agents/outline-implementer-agent.ts:14–30](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/agents/claudecode/agents/outline-implementer-agent.ts#L14-L30)
- [apps/riptide-daemon/src/agents/claudecode/agents/outline-implementer-agent.ts:44–78](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/agents/claudecode/agents/outline-implementer-agent.ts#L44-L78)

### WF14

- [apps/docs/explanation/tasks.md:3–10](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/docs/explanation/tasks.md#L3-L10)
- [apps/docs/explanation/tasks.md:46–102](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/docs/explanation/tasks.md#L46-L102)
- [apps/docs/guide/skills-workflows.md:45–88](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/docs/guide/skills-workflows.md#L45-L88)
- [apps/docs/reference/skills-workflows.md:24–31](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/docs/reference/skills-workflows.md#L24-L31)
- [apps/docs/reference/skills-workflows.md:534–572](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/docs/reference/skills-workflows.md#L534-L572)

### WF15

- [apps/riptide-rpi-claude-plugin/skills/review-artifact-comments/SKILL.md:10–42](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-rpi-claude-plugin/skills/review-artifact-comments/SKILL.md#L10-L42)
- [apps/riptide-rpi-claude-plugin/skills/review-artifact-comments/SKILL.md:61–71](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-rpi-claude-plugin/skills/review-artifact-comments/SKILL.md#L61-L71)

### WF16

- [apps/riptide-daemon/src/lib/artifact-sync-utils.ts:38–58](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/lib/artifact-sync-utils.ts#L38-L58)
- [apps/riptide-daemon/src/lib/artifact-sync-utils.ts:84–154](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/lib/artifact-sync-utils.ts#L84-L154)
- [apps/riptide-daemon/test/unit/lib/artifact-sync-utils.test.ts:18–87](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/test/unit/lib/artifact-sync-utils.test.ts#L18-L87)
- [apps/riptide-daemon/test/unit/lib/artifact-sync-utils.test.ts:116–146](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/test/unit/lib/artifact-sync-utils.test.ts#L116-L146)

### WF17

- [apps/riptide-daemon/src/lib/artifact-sync-utils.ts:60–76](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/lib/artifact-sync-utils.ts#L60-L76)
- [apps/riptide-daemon/src/agents/claudecode/hooks/workflow-routing-hook.ts:13–16](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/agents/claudecode/hooks/workflow-routing-hook.ts#L13-L16)

### WF18

- [apps/riptide-daemon/src/agents/claudecode/hooks/workflow-routing-hook.ts:18–166](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/agents/claudecode/hooks/workflow-routing-hook.ts#L18-L166)
- [apps/riptide-daemon/src/agents/claudecode/hooks/workflow-routing-hook.test.ts:16–79](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/agents/claudecode/hooks/workflow-routing-hook.test.ts#L16-L79)
- [apps/riptide-daemon/test/unit/agents/claudecode/hooks/workflow-routing-hook.test.ts:16–52](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/test/unit/agents/claudecode/hooks/workflow-routing-hook.test.ts#L16-L52)

### WF19

- [packages/ai/src/agents/extract-next-step/extract-next-step.ts:8–35](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/packages/ai/src/agents/extract-next-step/extract-next-step.ts#L8-L35)
- [packages/ai/src/agents/extract-next-step/extract-next-step.ts:42–133](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/packages/ai/src/agents/extract-next-step/extract-next-step.ts#L42-L133)
- [apps/riptide-api/src/orpc/daemon/sessions/update.ts:310–332](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-api/src/orpc/daemon/sessions/update.ts#L310-L332)
- [apps/riptide-api/src/orpc/daemon/sessions/update.ts:440–531](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-api/src/orpc/daemon/sessions/update.ts#L440-L531)

### WF20

- [apps/riptide-api/src/orpc/daemon/sessions/check-auto-advance.ts:17–85](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-api/src/orpc/daemon/sessions/check-auto-advance.ts#L17-L85)
- [apps/riptide-api/src/orpc/daemon/sessions/check-auto-advance.ts:124–150](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-api/src/orpc/daemon/sessions/check-auto-advance.ts#L124-L150)
- [apps/riptide-api/src/orpc/daemon/sessions/check-auto-advance.ts:273–341](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-api/src/orpc/daemon/sessions/check-auto-advance.ts#L273-L341)
- [apps/docs/reference/skills-workflows.md:597–611](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/docs/reference/skills-workflows.md#L597-L611)

### WF21

- [apps/riptide-api/src/orpc/daemon/sessions/check-auto-advance.ts:225–260](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-api/src/orpc/daemon/sessions/check-auto-advance.ts#L225-L260)
- [apps/riptide-api/src/orpc/daemon/sessions/check-auto-advance.ts:485–545](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-api/src/orpc/daemon/sessions/check-auto-advance.ts#L485-L545)
- [apps/riptide-api/test/procedures/auto-advance.test.ts:663–724](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-api/test/procedures/auto-advance.test.ts#L663-L724)
- [apps/riptide-api/test/procedures/auto-advance.test.ts:2860–2937](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-api/test/procedures/auto-advance.test.ts#L2860-L2937)

### WF22

- [apps/riptide-api/src/orpc/daemon/sessions/check-auto-advance.ts:343–435](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-api/src/orpc/daemon/sessions/check-auto-advance.ts#L343-L435)
- [apps/riptide-api/test/procedures/auto-advance.test.ts:432–510](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-api/test/procedures/auto-advance.test.ts#L432-L510)

### WF23

- [apps/riptide-api/src/orpc/daemon/sessions/check-auto-advance.ts:416–434](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-api/src/orpc/daemon/sessions/check-auto-advance.ts#L416-L434)
- [apps/riptide-api/src/orpc/daemon/sessions/check-auto-advance.ts:476–482](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-api/src/orpc/daemon/sessions/check-auto-advance.ts#L476-L482)
- [apps/riptide-api/test/procedures/auto-advance.test.ts:95–129](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-api/test/procedures/auto-advance.test.ts#L95-L129)

### WF24

- [packages/ai/src/agents/context-shards/generate-context-shard-candidates.ts:64–85](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/packages/ai/src/agents/context-shards/generate-context-shard-candidates.ts#L64-L85)
- [packages/ai/src/agents/context-shards/generate-context-shard-candidates.ts:122–150](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/packages/ai/src/agents/context-shards/generate-context-shard-candidates.ts#L122-L150)
- [packages/ai/src/agents/context-shards/generate-context-shard-candidates.ts:173–195](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/packages/ai/src/agents/context-shards/generate-context-shard-candidates.ts#L173-L195)
- [packages/db/src/tables/context-shards.ts:9–29](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/packages/db/src/tables/context-shards.ts#L9-L29)
- [packages/db/src/tables/context-shards.ts:44–52](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/packages/db/src/tables/context-shards.ts#L44-L52)

### WF25

- [apps/riptide-api/src/orpc/daemon/context-shards/list-enabled.effect.ts:11–47](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-api/src/orpc/daemon/context-shards/list-enabled.effect.ts#L11-L47)
- [apps/riptide-api/test/procedures/daemon-context-shards.test.ts:117–190](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-api/test/procedures/daemon-context-shards.test.ts#L117-L190)
- [apps/riptide-daemon/src/agents/shared/context-shards.ts:12–55](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/agents/shared/context-shards.ts#L12-L55)
- [apps/riptide-daemon/test/effect/claude-context-shards.vi.test.ts:38–70](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/test/effect/claude-context-shards.vi.test.ts#L38-L70)

### WF26

- [packages/ai/src/agents/context-shards/generate-context-shard-candidates.vi.test.ts:140–194](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/packages/ai/src/agents/context-shards/generate-context-shard-candidates.vi.test.ts#L140-L194)
- [packages/ai/eval/context-shards/generate-context-shard-candidates.test.ts:10–12](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/packages/ai/eval/context-shards/generate-context-shard-candidates.test.ts#L10-L12)
- [packages/ai/eval/context-shards/generate-context-shard-candidates.test.ts:36–79](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/packages/ai/eval/context-shards/generate-context-shard-candidates.test.ts#L36-L79)
- [packages/ai/eval/context-shards/fixtures.ts:6–28](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/packages/ai/eval/context-shards/fixtures.ts#L6-L28)

### WF27

- [apps/docs/reference/subagent-models.md:5–10](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/docs/reference/subagent-models.md#L5-L10)
- [apps/docs/reference/subagent-models.md:18–92](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/docs/reference/subagent-models.md#L18-L92)
- [apps/riptide-daemon/src/agents/claudecode/agents/codebase-analyzer.ts:3–8](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/agents/claudecode/agents/codebase-analyzer.ts#L3-L8)
- [apps/riptide-daemon/src/agents/claudecode/agents/outline-implementer-agent.ts:3–8](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/agents/claudecode/agents/outline-implementer-agent.ts#L3-L8)

### WF28

- [apps/riptide-rpi-claude-plugin/skills/describe-pr/SKILL.md:8–47](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-rpi-claude-plugin/skills/describe-pr/SKILL.md#L8-L47)
- [apps/riptide-rpi-claude-plugin/skills/describe-pr/SKILL.md:54–76](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-rpi-claude-plugin/skills/describe-pr/SKILL.md#L54-L76)

### WF29

- [apps/docs/reference/skills-workflows.md:626–640](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/docs/reference/skills-workflows.md#L626-L640)
- [apps/riptide-rpi-claude-plugin/skills/describe-pr/SKILL.md:29–40](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-rpi-claude-plugin/skills/describe-pr/SKILL.md#L29-L40)
- [apps/riptide-rpi-claude-plugin/skills/describe-pr/SKILL.md:60–76](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-rpi-claude-plugin/skills/describe-pr/SKILL.md#L60-L76)

### WF30

- [apps/docs/guide/automation-sessions.md:3–15](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/docs/guide/automation-sessions.md#L3-L15)
- [apps/docs/guide/automation-sessions.md:31–35](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/docs/guide/automation-sessions.md#L31-L35)
- [apps/docs/guide/automation-sessions.md:62–68](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/docs/guide/automation-sessions.md#L62-L68)
- [apps/docs/guide/automation-sessions.md:151–159](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/docs/guide/automation-sessions.md#L151-L159)

### WF31

- [apps/riptide-humanlayer-claude-plugin/skills/orchestrate/SKILL.md:6–25](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-humanlayer-claude-plugin/skills/orchestrate/SKILL.md#L6-L25)
- [apps/docs/reference/skills-workflows.md:520–530](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/docs/reference/skills-workflows.md#L520-L530)

### WF32

- [apps/riptide-humanlayer-claude-plugin/skills/orchestrate/references/launch-task.md:1–3](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-humanlayer-claude-plugin/skills/orchestrate/references/launch-task.md#L1-L3)
- [apps/riptide-humanlayer-claude-plugin/skills/orchestrate/references/launch-task.md:115–131](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-humanlayer-claude-plugin/skills/orchestrate/references/launch-task.md#L115-L131)
- [apps/riptide-humanlayer-claude-plugin/skills/orchestrate/references/launch-task.md:175–183](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-humanlayer-claude-plugin/skills/orchestrate/references/launch-task.md#L175-L183)
- [apps/riptide-humanlayer-claude-plugin/skills/orchestrate/references/launch-session.md:14–23](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-humanlayer-claude-plugin/skills/orchestrate/references/launch-session.md#L14-L23)

### WF33

- [apps/riptide-rpi-claude-plugin/.claude-plugin/plugin.json:1–24](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-rpi-claude-plugin/.claude-plugin/plugin.json#L1-L24)
- [apps/riptide-humanlayer-claude-plugin/.claude-plugin/plugin.json:1–10](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-humanlayer-claude-plugin/.claude-plugin/plugin.json#L1-L10)
- [apps/riptide-rpi-claude-plugin/README.md:1–14](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-rpi-claude-plugin/README.md#L1-L14)

### WF34

- [apps/riptide-daemon/src/plugins/bundled-rpi-plugin.ts:1–16](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/plugins/bundled-rpi-plugin.ts#L1-L16)
- [apps/riptide-daemon/src/plugins/bundled-rpi-plugin.ts:169–305](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/plugins/bundled-rpi-plugin.ts#L169-L305)
- [apps/riptide-daemon/src/plugins/bundled-humanlayer-plugin.ts:30–49](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/plugins/bundled-humanlayer-plugin.ts#L30-L49)
- [apps/riptide-humanlayer-claude-plugin/skills/teleport/SKILL.md:1–48](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-humanlayer-claude-plugin/skills/teleport/SKILL.md#L1-L48)

### RT-I01

- [packages/session-sdk-sessions/src/commands.ts:1–43](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/packages/session-sdk-sessions/src/commands.ts#L1-L43)

### RT-I02

- [apps/riptide-daemon/src/start.ts:192–214](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/start.ts#L192-L214)

### RT-I03

- [apps/riptide-daemon/src/subscriptions.ts:158–210](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/subscriptions.ts#L158-L210)

### RT-I04

- [apps/riptide-daemon/src/effects/services/workspace-session-launch/workspace-session-launch.machine.ts:15–69](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/effects/services/workspace-session-launch/workspace-session-launch.machine.ts#L15-L69)
- [apps/riptide-daemon/src/effects/services/workspace-session-launch/workspace-session-launch.machine.ts:76–148](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/effects/services/workspace-session-launch/workspace-session-launch.machine.ts#L76-L148)
- [apps/riptide-daemon/src/effects/services/workspace-session-launch/workspace-session-launch.machine.ts:176–261](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/effects/services/workspace-session-launch/workspace-session-launch.machine.ts#L176-L261)

### RT-I05

- [apps/riptide-daemon/src/effects/services/workspace-session-launch/workspace-session-launch-actors.layer.ts:71–134](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/effects/services/workspace-session-launch/workspace-session-launch-actors.layer.ts#L71-L134)

### RT-I06

- [apps/riptide-daemon/src/effects/services/workspace-repository-setup/workspace-repository-setup.machine.ts:12–105](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/effects/services/workspace-repository-setup/workspace-repository-setup.machine.ts#L12-L105)

### RT-I07

- [packages/db/src/tables/sessions.ts:31–37](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/packages/db/src/tables/sessions.ts#L31-L37)
- [packages/db/src/tables/sessions.ts:115–122](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/packages/db/src/tables/sessions.ts#L115-L122)

### RT-I08

- [apps/riptide-daemon/src/start.ts:216–240](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/start.ts#L216-L240)

### RT-I09

- [apps/riptide-daemon/src/lib/heartbeat.ts:14–23](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/lib/heartbeat.ts#L14-L23)
- [apps/riptide-daemon/src/lib/heartbeat.ts:75–106](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/lib/heartbeat.ts#L75-L106)
- [apps/riptide-daemon/src/lib/heartbeat.ts:120–160](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/lib/heartbeat.ts#L120-L160)

### RT-I10

- [contracts/riptide-api-contract/src/daemon/heartbeat.ts:8–67](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/contracts/riptide-api-contract/src/daemon/heartbeat.ts#L8-L67)

### RT-I11

- [packages/db/src/tables/sessions.ts:55–92](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/packages/db/src/tables/sessions.ts#L55-L92)

### RT-I12

- [apps/riptide-daemon/src/handlers/sessions/on-session-continue.ts:40–66](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/handlers/sessions/on-session-continue.ts#L40-L66)
- [apps/riptide-daemon/src/handlers/sessions/on-session-continue.ts:74–122](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/handlers/sessions/on-session-continue.ts#L74-L122)

### RT-I13

- [apps/riptide-daemon/src/effects/services/fold-sessions/fold-model-selection.ts:8–50](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/effects/services/fold-sessions/fold-model-selection.ts#L8-L50)

### RT-I14

- [packages/db/src/tables/fold-session-events.ts:14–32](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/packages/db/src/tables/fold-session-events.ts#L14-L32)

### RT-I15

- [apps/riptide-api/src/orpc/daemon/fold-session-events/append.effect.ts:25–29](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-api/src/orpc/daemon/fold-session-events/append.effect.ts#L25-L29)
- [apps/riptide-api/src/orpc/daemon/fold-session-events/append.effect.ts:14–18](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-api/src/orpc/daemon/fold-session-events/append.effect.ts#L14-L18)
- [apps/riptide-api/src/orpc/daemon/fold-session-events/append.effect.ts:31–131](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-api/src/orpc/daemon/fold-session-events/append.effect.ts#L31-L131)

### RT-I16

- [apps/riptide-daemon/src/effects/services/fold-event-log/fold-event-log-session.ts:52–128](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/effects/services/fold-event-log/fold-event-log-session.ts#L52-L128)

### RT-I17

- [apps/riptide-daemon/src/effects/services/fold-sessions/fold-event-processor.layer.ts:55–86](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/effects/services/fold-sessions/fold-event-processor.layer.ts#L55-L86)
- [apps/riptide-daemon/src/effects/services/fold-sessions/fold-event-processor.layer.ts:198–215](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/effects/services/fold-sessions/fold-event-processor.layer.ts#L198-L215)
- [apps/riptide-daemon/src/effects/services/fold-sessions/fold-event-processor.layer.ts:224–280](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/effects/services/fold-sessions/fold-event-processor.layer.ts#L224-L280)

### RT-I18

- [apps/riptide-daemon/src/effects/services/stream-producer/durable-stream-writer.ts:91–110](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/effects/services/stream-producer/durable-stream-writer.ts#L91-L110)
- [apps/riptide-daemon/src/effects/services/stream-producer/durable-stream-writer.ts:125–163](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/effects/services/stream-producer/durable-stream-writer.ts#L125-L163)
- [apps/riptide-daemon/src/effects/services/stream-producer/durable-stream-writer.ts:165–233](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/effects/services/stream-producer/durable-stream-writer.ts#L165-L233)
- [apps/riptide-daemon/src/effects/services/stream-producer/durable-stream-writer.ts:235–260](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/effects/services/stream-producer/durable-stream-writer.ts#L235-L260)

### RT-I19

- [apps/riptide-daemon/src/effects/services/stream-producer/stream-producer.service.ts:125–177](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/effects/services/stream-producer/stream-producer.service.ts#L125-L177)

### RT-I20

- [apps/riptide-daemon/src/effects/services/stream-producer/stream-producer.service.ts:146–159](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/effects/services/stream-producer/stream-producer.service.ts#L146-L159)
- [apps/riptide-daemon/src/effects/services/stream-producer/stream-producer.service.ts:257–273](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/effects/services/stream-producer/stream-producer.service.ts#L257-L273)

### RT-I21

- [apps/riptide-daemon/src/effects/services/claude-sessions/workflows/process-events.ts:112–127](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/effects/services/claude-sessions/workflows/process-events.ts#L112-L127)

### RT-I22

- [packages/session-sdk-sessions/src/events.ts:14–48](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/packages/session-sdk-sessions/src/events.ts#L14-L48)
- [packages/session-sdk-sessions/src/events.ts:51–66](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/packages/session-sdk-sessions/src/events.ts#L51-L66)

### RT-I23

- [apps/riptide-daemon/src/effects/services/fold-sessions/fold-session-runner.layer.ts:215–229](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/effects/services/fold-sessions/fold-session-runner.layer.ts#L215-L229)
- [apps/riptide-daemon/src/effects/services/fold-sessions/fold-session-runner.layer.ts:250–290](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/effects/services/fold-sessions/fold-session-runner.layer.ts#L250-L290)

### RT-I24

- [apps/riptide-api/src/orpc/daemon/sessions/update.ts:121–150](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-api/src/orpc/daemon/sessions/update.ts#L121-L150)

### RT-I25

- [apps/riptide-daemon/src/effects/services/daemon-instance-lock/daemon-instance-lock.layer.ts:28–103](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/effects/services/daemon-instance-lock/daemon-instance-lock.layer.ts#L28-L103)

### RT-I26

- [apps/riptide-daemon/src/effects/services/session-runs/session-run-registry.ts:12–48](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/effects/services/session-runs/session-run-registry.ts#L12-L48)

### RT-I27

- [apps/riptide-daemon/src/effects/services/fold-sessions/fold-session-runner.layer.ts:64–84](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/effects/services/fold-sessions/fold-session-runner.layer.ts#L64-L84)
- [apps/riptide-daemon/src/effects/services/fold-sessions/fold-session-runner.layer.ts:215–224](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/effects/services/fold-sessions/fold-session-runner.layer.ts#L215-L224)
- [apps/riptide-daemon/src/effects/services/fold-sessions/fold-session-runner.layer.ts:386–487](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/effects/services/fold-sessions/fold-session-runner.layer.ts#L386-L487)
- [apps/riptide-daemon/src/effects/services/fold-sessions/fold-session-runner.layer.ts:490–583](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/effects/services/fold-sessions/fold-session-runner.layer.ts#L490-L583)
- [apps/riptide-daemon/src/effects/services/fold-sessions/fold-session-runner.layer.ts:586–605](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/effects/services/fold-sessions/fold-session-runner.layer.ts#L586-L605)

### RT-I28

- [apps/riptide-daemon/src/effects/services/fold-sessions/fold-session-opener.layer.ts:525–555](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/effects/services/fold-sessions/fold-session-opener.layer.ts#L525-L555)

### RT-I29

- [apps/riptide-daemon/src/subscriptions.ts:42–100](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/subscriptions.ts#L42-L100)
- [apps/riptide-daemon/src/subscriptions.ts:128–156](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/subscriptions.ts#L128-L156)
- [apps/riptide-daemon/src/subscriptions.ts:211–222](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/subscriptions.ts#L211-L222)

### RT-I30

- [apps/riptide-daemon/src/effects/services/stream-producer/stream-producer-recovery.ts:7–58](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/effects/services/stream-producer/stream-producer-recovery.ts#L7-L58)

### RT-I31

- [apps/riptide-daemon/src/effects/services/claude-sessions/workflows/process-events.ts:75–109](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/effects/services/claude-sessions/workflows/process-events.ts#L75-L109)
- [apps/riptide-daemon/src/effects/services/claude-sessions/workflows/process-events.ts:168–208](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/effects/services/claude-sessions/workflows/process-events.ts#L168-L208)

### RT-I32

- [packages/sync/src/health-tracker.ts:26–37](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/packages/sync/src/health-tracker.ts#L26-L37)
- [packages/sync/src/health-tracker.ts:104–168](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/packages/sync/src/health-tracker.ts#L104-L168)
- [packages/sync/src/health-tracker.ts:171–226](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/packages/sync/src/health-tracker.ts#L171-L226)

### RT-I33

- [apps/riptide-daemon/src/orpc/retry-policy.ts:4–34](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/orpc/retry-policy.ts#L4-L34)

### RT-I34

- [packages/sync/src/sync-error-handler.ts:77–93](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/packages/sync/src/sync-error-handler.ts#L77-L93)
- [packages/sync/src/sync-error-handler.ts:117–174](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/packages/sync/src/sync-error-handler.ts#L117-L174)

### RT-I35

- [packages/y-durable-streams/src/yjs-provider.ts:114–193](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/packages/y-durable-streams/src/yjs-provider.ts#L114-L193)

### RT-I36

- [apps/stale-daemon-sweeper/stale-daemons.ts:7–8](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/stale-daemon-sweeper/stale-daemons.ts#L7-L8)
- [apps/stale-daemon-sweeper/stale-daemons.ts:44–115](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/stale-daemon-sweeper/stale-daemons.ts#L44-L115)

### RT-I37

- [apps/stale-daemon-sweeper/lost-sessions.ts:9–47](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/stale-daemon-sweeper/lost-sessions.ts#L9-L47)
- [apps/stale-daemon-sweeper/lost-sessions.ts:98–155](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/stale-daemon-sweeper/lost-sessions.ts#L98-L155)
- [apps/stale-daemon-sweeper/lost-sessions.ts:166–215](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/stale-daemon-sweeper/lost-sessions.ts#L166-L215)

### RT-I38

- [apps/riptide-daemon/src/lifecycle/graceful-shutdown.ts:42–90](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/lifecycle/graceful-shutdown.ts#L42-L90)

### RT-I39

- [apps/riptide-daemon/src/lib/orphan-detection.ts:3–29](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/lib/orphan-detection.ts#L3-L29)

### RT-I40

- [apps/riptide-api/src/auth/context.ts:11–20](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-api/src/auth/context.ts#L11-L20)
- [apps/riptide-api/src/auth/context.ts:49–79](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-api/src/auth/context.ts#L49-L79)

### RT-I41

- [apps/riptide-api/src/db/host-auth.ts:6–31](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-api/src/db/host-auth.ts#L6-L31)

### RT-I42

- [apps/riptide-api/src/db/task-auth.ts:223–270](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-api/src/db/task-auth.ts#L223-L270)

### RT-I43

- [apps/riptide-api/src/lib/session-multiplayer-prompting-auth.ts:12–84](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-api/src/lib/session-multiplayer-prompting-auth.ts#L12-L84)

### RT-I44

- [apps/riptide-electric-proxy/src/routes/response-editor-collaboration.ts:20–49](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-electric-proxy/src/routes/response-editor-collaboration.ts#L20-L49)

### RT-I45

- [apps/riptide-daemon/src/effects/services/claude-sessions/workflows/approvals.ts:62–158](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/effects/services/claude-sessions/workflows/approvals.ts#L62-L158)

### RT-I46

- [apps/riptide-daemon/src/effects/services/claude-sessions/query-options.ts:74–119](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/effects/services/claude-sessions/query-options.ts#L74-L119)

### RT-I47

- [apps/riptide-daemon/src/agents/claudecode/permission-mode.ts:7–17](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/agents/claudecode/permission-mode.ts#L7-L17)

### RT-I48

- [apps/riptide-api/src/auth/daemon-token-core.ts:52–91](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-api/src/auth/daemon-token-core.ts#L52-L91)
- [apps/riptide-api/src/auth/daemon-token-core.ts:104–144](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-api/src/auth/daemon-token-core.ts#L104-L144)

### RT-I49

- [apps/riptide-api/src/auth/daemon-tokens.ts:52–96](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-api/src/auth/daemon-tokens.ts#L52-L96)

### RT-I50

- [apps/riptide-daemon/src/effects/services/workspace-setup-executor/probe-target-worktree.ts:17–76](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/effects/services/workspace-setup-executor/probe-target-worktree.ts#L17-L76)

### RT-I51

- [apps/riptide-daemon/src/effects/services/workspace-setup-executor/create-or-adopt-worktree.ts:105–127](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/effects/services/workspace-setup-executor/create-or-adopt-worktree.ts#L105-L127)
- [apps/riptide-daemon/src/effects/services/workspace-setup-executor/create-or-adopt-worktree.ts:130–190](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/effects/services/workspace-setup-executor/create-or-adopt-worktree.ts#L130-L190)
- [apps/riptide-daemon/src/effects/services/workspace-setup-executor/create-or-adopt-worktree.ts:193–226](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/effects/services/workspace-setup-executor/create-or-adopt-worktree.ts#L193-L226)

### RT-I52

- [apps/riptide-daemon/src/effects/services/workspace-path-resolver/workspace-copy-path.ts:1–13](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/effects/services/workspace-path-resolver/workspace-copy-path.ts#L1-L13)

### RT-I53

- [apps/riptide-daemon/src/effects/services/workspace-setup-executor/copy-configured-files.ts:43–87](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/effects/services/workspace-setup-executor/copy-configured-files.ts#L43-L87)

### RT-I54

- [apps/riptide-daemon/src/effects/services/managed-repository-cache/safe-repository-remote.ts:11–18](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/effects/services/managed-repository-cache/safe-repository-remote.ts#L11-L18)

### RT-I55

- [apps/riptide-daemon/src/effects/services/workspace-setup-executor/run-setup-command.ts:21–89](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/effects/services/workspace-setup-executor/run-setup-command.ts#L21-L89)

### RT-I56

- [packages/y-durable-streams/src/yjs-provider.ts:210–247](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/packages/y-durable-streams/src/yjs-provider.ts#L210-L247)
- [packages/y-durable-streams/src/yjs-provider.ts:264–327](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/packages/y-durable-streams/src/yjs-provider.ts#L264-L327)

### RT-I57

- [apps/riptide-electric-proxy/src/middleware.ts:107–125](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-electric-proxy/src/middleware.ts#L107-L125)
- [apps/riptide-electric-proxy/src/middleware.ts:129–145](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-electric-proxy/src/middleware.ts#L129-L145)

### RT-I58

- [apps/riptide-api/src/effects/project-workspace/repository-progress.ts:45–151](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-api/src/effects/project-workspace/repository-progress.ts#L45-L151)
- [apps/riptide-api/src/effects/project-workspace/repository-progress.ts:156–203](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-api/src/effects/project-workspace/repository-progress.ts#L156-L203)
- [apps/riptide-api/src/effects/project-workspace/repository-progress.ts:245–255](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-api/src/effects/project-workspace/repository-progress.ts#L245-L255)

### RT-I59

- [apps/riptide-daemon/src/effects/services/workspace-repository-actor-operations/workspace-repository-actor-operations.layer.ts:62–76](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/effects/services/workspace-repository-actor-operations/workspace-repository-actor-operations.layer.ts#L62-L76)

### RT-I60

- [apps/riptide-api/src/effects/project-workspace/repository-recovery.ts:43–107](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-api/src/effects/project-workspace/repository-recovery.ts#L43-L107)
- [apps/riptide-api/src/effects/project-workspace/repository-recovery.ts:125–158](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-api/src/effects/project-workspace/repository-recovery.ts#L125-L158)
- [apps/riptide-api/src/effects/project-workspace/repository-recovery.ts:164–196](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-api/src/effects/project-workspace/repository-recovery.ts#L164-L196)

### RT-T01

- [apps/riptide-daemon/test/effect/workspace-session-launch-actors.vi.test.ts:117–190](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/test/effect/workspace-session-launch-actors.vi.test.ts#L117-L190)

### RT-T02

- [apps/riptide-api/test/procedures/fold-session-events.test.ts:182–226](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-api/test/procedures/fold-session-events.test.ts#L182-L226)
- [apps/riptide-api/test/procedures/fold-session-events.test.ts:290–351](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-api/test/procedures/fold-session-events.test.ts#L290-L351)

### RT-T03

- [apps/riptide-daemon/test/effect/fold-event-log-session.vi.test.ts:204–273](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/test/effect/fold-event-log-session.vi.test.ts#L204-L273)
- [apps/riptide-daemon/test/effect/fold-event-log-session.vi.test.ts:564–594](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/test/effect/fold-event-log-session.vi.test.ts#L564-L594)

### RT-T04

- [apps/riptide-daemon/test/effect/fold-session-runner.vi.test.ts:583–698](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/test/effect/fold-session-runner.vi.test.ts#L583-L698)
- [apps/riptide-daemon/test/effect/fold-session-runner.vi.test.ts:753–790](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/test/effect/fold-session-runner.vi.test.ts#L753-L790)
- [apps/riptide-daemon/test/effect/fold-session-runner.vi.test.ts:851–887](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/test/effect/fold-session-runner.vi.test.ts#L851-L887)
- [apps/riptide-daemon/test/effect/fold-session-runner.vi.test.ts:893–927](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/test/effect/fold-session-runner.vi.test.ts#L893-L927)

### RT-T05

- [apps/riptide-daemon/test/effect/fold-session-runner.vi.test.ts:257–323](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/test/effect/fold-session-runner.vi.test.ts#L257-L323)
- [apps/riptide-daemon/test/effect/fold-session-runner.vi.test.ts:336–354](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/test/effect/fold-session-runner.vi.test.ts#L336-L354)
- [apps/riptide-daemon/test/effect/fold-session-runner.vi.test.ts:525–580](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/test/effect/fold-session-runner.vi.test.ts#L525-L580)

### RT-T06

- [apps/riptide-api/test/procedures/project-workspace-recovery.test.ts:100–122](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-api/test/procedures/project-workspace-recovery.test.ts#L100-L122)
- [apps/riptide-api/test/procedures/project-workspace-recovery.test.ts:172–205](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-api/test/procedures/project-workspace-recovery.test.ts#L172-L205)

### RT-D01

- [packages/y-durable-streams/README.md:3–44](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/packages/y-durable-streams/README.md#L3-L44)

### HP01-task-policy

- [packages/db/src/tables/tasks.ts:59–98](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/packages/db/src/tables/tasks.ts#L59-L98)

### HP02-session-identity

- [packages/db/src/tables/sessions.ts:55–88](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/packages/db/src/tables/sessions.ts#L55-L88)

### HP03-host-setup

- [packages/db/src/tables/task-workspace-setup-for-host.ts:31–66](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/packages/db/src/tables/task-workspace-setup-for-host.ts#L31-L66)

### HP04-artifact-retention

- [packages/db/src/tables/artifacts.ts:21–40](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/packages/db/src/tables/artifacts.ts#L21-L40)

### HP05-comment-contract

- [packages/db/src/tables/artifact-comments.ts:81–120](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/packages/db/src/tables/artifact-comments.ts#L81-L120)

### HP06-anchor-resolution

- [packages/ui/src/artifact-viewer-v2/anchor/resolve.ts:35–80](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/packages/ui/src/artifact-viewer-v2/anchor/resolve.ts#L35-L80)

### HP07-anchor-approximation

- [packages/ui/src/artifact-viewer-v2/anchor/resolve.ts:182–230](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/packages/ui/src/artifact-viewer-v2/anchor/resolve.ts#L182-L230)

### HP08-anchor-tests

- [packages/ui/src/artifact-viewer-v2/anchor/resolve.test.ts:56–123](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/packages/ui/src/artifact-viewer-v2/anchor/resolve.test.ts#L56-L123)

### HP09-feedback-compiler

- [packages/ui/src/artifact-viewer-v2/export/export-feedback.ts:27–76](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/packages/ui/src/artifact-viewer-v2/export/export-feedback.ts#L27-L76)

### HP10-feedback-delivery

- [apps/riptide-ui/src/components/artifact-viewer-v2/delivery/executeBulkArtifactDelivery.ts:24–56](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-ui/src/components/artifact-viewer-v2/delivery/executeBulkArtifactDelivery.ts#L24-L56)

### HP11-feedback-tests

- [apps/riptide-ui/src/components/artifact-viewer-v2/delivery/executeBulkArtifactDelivery.test.ts:32–73](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-ui/src/components/artifact-viewer-v2/delivery/executeBulkArtifactDelivery.test.ts#L32-L73)

### HP12-feedback-partial

- [apps/riptide-ui/src/components/artifact-viewer-v2/delivery/executeBulkArtifactDelivery.test.ts:96–109](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-ui/src/components/artifact-viewer-v2/delivery/executeBulkArtifactDelivery.test.ts#L96-L109)

### HP13-review-watermark

- [apps/riptide-ui/src/hooks/stores/taskDiffReviewMarksStore.ts:8–66](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-ui/src/hooks/stores/taskDiffReviewMarksStore.ts#L8-L66)

### HP14-review-local-only

- [apps/riptide-ui/src/hooks/stores/taskDiffReviewMarksStore.ts:270–280](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-ui/src/hooks/stores/taskDiffReviewMarksStore.ts#L270-L280)

### HP15-diff-two-sides

- [packages/ui/src/lib/diff-review/project-diff-comments.ts:158–192](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/packages/ui/src/lib/diff-review/project-diff-comments.ts#L158-L192)

### HP16-shared-prompt

- [apps/riptide-ui/src/hooks/session-detail/use-response-editor-collaboration.ts:25–73](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-ui/src/hooks/session-detail/use-response-editor-collaboration.ts#L25-L73)

### HP17-access-state

- [apps/riptide-ui/src/hooks/session-detail/use-response-editor-collaboration.ts:124–159](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-ui/src/hooks/session-detail/use-response-editor-collaboration.ts#L124-L159)

### HP18-read-only-proof

- [packages/y-durable-streams/test/provider-read-only.test.ts:10–52](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/packages/y-durable-streams/test/provider-read-only.test.ts#L10-L52)

### HP19-recovery-proof

- [packages/y-durable-streams/test/provider-recovery.test.ts:64–147](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/packages/y-durable-streams/test/provider-recovery.test.ts#L64-L147)

### HP20-file-artifacts

- [packages/session-sdk-artifacts/src/sync.ts:1–5](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/packages/session-sdk-artifacts/src/sync.ts#L1-L5)

### HP21-outbox-isolation

- [packages/session-sdk-artifacts/src/sync.ts:204–267](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/packages/session-sdk-artifacts/src/sync.ts#L204-L267)

### HP22-task-position

- [apps/riptide-ui/src/lib/kanban/columnEngine.ts:104–147](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-ui/src/lib/kanban/columnEngine.ts#L104-L147)

### HP23-task-attention

- [apps/riptide-ui/src/lib/taskStatus.ts:11–67](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-ui/src/lib/taskStatus.ts#L11-L67)

### HP24-next-step-dedup

- [apps/riptide-ui/src/hooks/task-detail/useTaskNextStep.ts:40–89](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-ui/src/hooks/task-detail/useTaskNextStep.ts#L40-L89)

### HP25-notification-projection

- [apps/riptide-ui/src/lib/notifications/notification-rows.ts:11–21](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-ui/src/lib/notifications/notification-rows.ts#L11-L21)

### HP26-notification-calm

- [apps/riptide-ui/src/components/notifications/NotificationArrivals.tsx:35–101](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-ui/src/components/notifications/NotificationArrivals.tsx#L35-L101)

### HP27-progressive-disclosure

- [apps/riptide-ui/src/components/conversation-stream/WiredConversationStream.tsx:223–245](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-ui/src/components/conversation-stream/WiredConversationStream.tsx#L223-L245)

### HP28-stream-ownership

- [apps/riptide-ui/src/components/conversation-stream/streamingHandoffSuppression.ts:14–70](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-ui/src/components/conversation-stream/streamingHandoffSuppression.ts#L14-L70)

### HP29-leaf-queries

- [apps/riptide-ui/src/components/conversation-stream/WiredConversationEventRow.tsx:67–102](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-ui/src/components/conversation-stream/WiredConversationEventRow.tsx#L67-L102)

### HP30-virtualization

- [apps/riptide-ui/src/components/conversation-stream/WiredConversationStream.tsx:391–408](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-ui/src/components/conversation-stream/WiredConversationStream.tsx#L391-L408)

### HP31-ui-boundaries

- [apps/riptide-ui/CLAUDE.md:26–40](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-ui/CLAUDE.md#L26-L40)

### HP32-ui-experiment

- [apps/riptide-ui/src/minimalist/CLAUDE.md:5–14](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-ui/src/minimalist/CLAUDE.md#L5-L14)

### HP33-devstack-plan

- [apps/devstack/src/sync/stack-sync-plan.ts:146–203](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/devstack/src/sync/stack-sync-plan.ts#L146-L203)

### HP34-devstack-apply

- [apps/devstack/src/sync/stack-sync-apply.ts:8–78](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/devstack/src/sync/stack-sync-apply.ts#L8-L78)

### HP35-devstack-isolation

- [CLAUDE.md:255–271](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/CLAUDE.md#L255-L271)

### HP36-quiet-quality

- [package.json:48–65](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/package.json#L48-L65)

### HP37-learning-tests

- [apps/devstack/src/test/learning/caddy-multiple-durable-streams.test.ts:79–153](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/devstack/src/test/learning/caddy-multiple-durable-streams.test.ts#L79-L153)

### HP38-quality-constraints

- [tools/oxlint/anti-slop/index.ts:3–22](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/tools/oxlint/anti-slop/index.ts#L3-L22)

### HP39-learning-questions

- [packages/ai/src/agents/generate-learn-questions/generate-learn-questions.ts:5–50](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/packages/ai/src/agents/generate-learn-questions/generate-learn-questions.ts#L5-L50)

### HP40-onboarding-value

- [apps/riptide-ui/src/components/onboarding/onboarding-progress.ts:10–49](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-ui/src/components/onboarding/onboarding-progress.ts#L10-L49)

### HP41-onboarding-proxy

- [apps/riptide-api/src/effects/services/onboarding/onboarding-milestones.ts:108–117](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-api/src/effects/services/onboarding/onboarding-milestones.ts#L108-L117)

### HP42-onboarding-direction

- [apps/riptide-api/src/effects/services/onboarding/onboarding-milestones.ts:158–208](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-api/src/effects/services/onboarding/onboarding-milestones.ts#L158-L208)

### HP43-usage-dedup

- [apps/riptide-api/src/orpc/daemon/sessions/update.ts:121–162](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-api/src/orpc/daemon/sessions/update.ts#L121-L162)

### HP44-storybook-policy

- [apps/riptide-ui/CLAUDE.md:3–24](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-ui/CLAUDE.md#L3-L24)

### HP45-artifact-metadata

- [packages/db/src/tables/artifacts.ts:32–40](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/packages/db/src/tables/artifacts.ts#L32-L40)
- [packages/db/src/tables/artifacts.ts:64–85](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/packages/db/src/tables/artifacts.ts#L64-L85)

### HP47-user-autonomy-defaults

- [packages/db/src/tables/task-user-settings.ts:37–44](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/packages/db/src/tables/task-user-settings.ts#L37-L44)

### HP48-eval-pipeline

- [packages/ai/eval/doc-researcher/runner.ts:13–83](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/packages/ai/eval/doc-researcher/runner.ts#L13-L83)
- [packages/ai/eval/doc-researcher/judge.ts:35–77](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/packages/ai/eval/doc-researcher/judge.ts#L35-L77)
- [packages/ai/eval/doc-researcher/doc-research.test.ts:27–77](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/packages/ai/eval/doc-researcher/doc-research.test.ts#L27-L77)
- [packages/ai/eval/_lib/matrix.ts:15–27](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/packages/ai/eval/_lib/matrix.ts#L15-L27)

### HP49-intent-evaluation

- [packages/ai/eval/classify-task-intent/classify-task-intent.test.ts:6–35](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/packages/ai/eval/classify-task-intent/classify-task-intent.test.ts#L6-L35)
- [packages/ai/eval/_lib/matrix.ts:15–26](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/packages/ai/eval/_lib/matrix.ts#L15-L26)
- [packages/ai/src/agents/classify-task-intent/classify-task-intent.ts:10–40](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/packages/ai/src/agents/classify-task-intent/classify-task-intent.ts#L10-L40)

### task-model

- [apps/docs/explanation/tasks.md:1–111](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/docs/explanation/tasks.md#L1-L111)

### runtime-boundary

- [apps/riptide-daemon/package.json:60–66](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/package.json#L60-L66)
- [apps/riptide-daemon/test/effect/fold-event-log-session.vi.test.ts:245–273](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/test/effect/fold-event-log-session.vi.test.ts#L245-L273)
- [apps/riptide-daemon/src/handlers/sessions/on-session-continue.ts:40–66](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/handlers/sessions/on-session-continue.ts#L40-L66)
- [apps/riptide-daemon/src/handlers/sessions/on-session-continue.ts:74–122](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/handlers/sessions/on-session-continue.ts#L74-L122)
- [apps/riptide-daemon/src/effects/services/fold-sessions/fold-session-opener.layer.ts:525–555](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/effects/services/fold-sessions/fold-session-opener.layer.ts#L525-L555)

### objective-research

- [apps/riptide-rpi-claude-plugin/skills/create-research-questions/SKILL.md:8–24](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-rpi-claude-plugin/skills/create-research-questions/SKILL.md#L8-L24)
- [apps/riptide-rpi-claude-plugin/skills/create-research-questions/SKILL.md:46–78](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-rpi-claude-plugin/skills/create-research-questions/SKILL.md#L46-L78)
- [apps/riptide-rpi-claude-plugin/skills/create-research/SKILL.md:10–40](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-rpi-claude-plugin/skills/create-research/SKILL.md#L10-L40)
- [apps/riptide-rpi-claude-plugin/skills/create-research/SKILL.md:50–82](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-rpi-claude-plugin/skills/create-research/SKILL.md#L50-L82)
- [apps/riptide-rpi-claude-plugin/skills/create-research/SKILL.md:102–112](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-rpi-claude-plugin/skills/create-research/SKILL.md#L102-L112)
- [apps/riptide-rpi-claude-plugin/skills/create-research/references/research_template.md:1–17](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-rpi-claude-plugin/skills/create-research/references/research_template.md#L1-L17)
- [apps/riptide-rpi-claude-plugin/skills/create-research/references/research_template.md:36–77](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-rpi-claude-plugin/skills/create-research/references/research_template.md#L36-L77)
- [apps/riptide-rpi-claude-plugin/skills/create-research/SKILL.md:124–175](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-rpi-claude-plugin/skills/create-research/SKILL.md#L124-L175)

### implementation-gates

- [apps/riptide-rpi-claude-plugin/skills/create-structure-outline/SKILL.md:38–82](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-rpi-claude-plugin/skills/create-structure-outline/SKILL.md#L38-L82)
- [apps/riptide-rpi-claude-plugin/skills/create-structure-outline/SKILL.md:157–181](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-rpi-claude-plugin/skills/create-structure-outline/SKILL.md#L157-L181)
- [apps/riptide-rpi-claude-plugin/skills/implement-outline/SKILL.md:8–52](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-rpi-claude-plugin/skills/implement-outline/SKILL.md#L8-L52)
- [apps/riptide-rpi-claude-plugin/skills/implement-outline/SKILL.md:69–113](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-rpi-claude-plugin/skills/implement-outline/SKILL.md#L69-L113)
- [apps/riptide-daemon/src/agents/claudecode/agents/outline-implementer-agent.ts:14–30](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/agents/claudecode/agents/outline-implementer-agent.ts#L14-L30)
- [apps/riptide-daemon/src/agents/claudecode/agents/outline-implementer-agent.ts:44–78](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/agents/claudecode/agents/outline-implementer-agent.ts#L44-L78)

### auto-advance

- [apps/riptide-daemon/src/agents/claudecode/hooks/workflow-routing-hook.ts:18–166](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/agents/claudecode/hooks/workflow-routing-hook.ts#L18-L166)
- [apps/riptide-daemon/src/agents/claudecode/hooks/workflow-routing-hook.test.ts:16–79](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/agents/claudecode/hooks/workflow-routing-hook.test.ts#L16-L79)
- [apps/riptide-daemon/test/unit/agents/claudecode/hooks/workflow-routing-hook.test.ts:16–52](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/test/unit/agents/claudecode/hooks/workflow-routing-hook.test.ts#L16-L52)
- [packages/ai/src/agents/extract-next-step/extract-next-step.ts:8–35](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/packages/ai/src/agents/extract-next-step/extract-next-step.ts#L8-L35)
- [packages/ai/src/agents/extract-next-step/extract-next-step.ts:42–133](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/packages/ai/src/agents/extract-next-step/extract-next-step.ts#L42-L133)
- [apps/riptide-api/src/orpc/daemon/sessions/update.ts:310–332](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-api/src/orpc/daemon/sessions/update.ts#L310-L332)
- [apps/riptide-api/src/orpc/daemon/sessions/update.ts:440–531](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-api/src/orpc/daemon/sessions/update.ts#L440-L531)
- [apps/riptide-api/src/orpc/daemon/sessions/check-auto-advance.ts:17–85](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-api/src/orpc/daemon/sessions/check-auto-advance.ts#L17-L85)
- [apps/riptide-api/src/orpc/daemon/sessions/check-auto-advance.ts:124–150](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-api/src/orpc/daemon/sessions/check-auto-advance.ts#L124-L150)
- [apps/riptide-api/src/orpc/daemon/sessions/check-auto-advance.ts:273–341](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-api/src/orpc/daemon/sessions/check-auto-advance.ts#L273-L341)
- [apps/docs/reference/skills-workflows.md:597–611](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/docs/reference/skills-workflows.md#L597-L611)
- [apps/riptide-api/src/orpc/daemon/sessions/check-auto-advance.ts:225–260](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-api/src/orpc/daemon/sessions/check-auto-advance.ts#L225-L260)
- [apps/riptide-api/src/orpc/daemon/sessions/check-auto-advance.ts:485–545](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-api/src/orpc/daemon/sessions/check-auto-advance.ts#L485-L545)
- [apps/riptide-api/test/procedures/auto-advance.test.ts:663–724](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-api/test/procedures/auto-advance.test.ts#L663-L724)
- [apps/riptide-api/test/procedures/auto-advance.test.ts:2860–2937](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-api/test/procedures/auto-advance.test.ts#L2860-L2937)
- [apps/riptide-api/src/orpc/daemon/sessions/check-auto-advance.ts:343–435](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-api/src/orpc/daemon/sessions/check-auto-advance.ts#L343-L435)
- [apps/riptide-api/test/procedures/auto-advance.test.ts:432–510](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-api/test/procedures/auto-advance.test.ts#L432-L510)
- [apps/riptide-api/src/orpc/daemon/sessions/check-auto-advance.ts:416–434](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-api/src/orpc/daemon/sessions/check-auto-advance.ts#L416-L434)
- [apps/riptide-api/src/orpc/daemon/sessions/check-auto-advance.ts:476–482](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-api/src/orpc/daemon/sessions/check-auto-advance.ts#L476-L482)
- [apps/riptide-api/test/procedures/auto-advance.test.ts:95–129](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-api/test/procedures/auto-advance.test.ts#L95-L129)

### artifact-authority

- [apps/riptide-rpi-claude-plugin/skills/create-design-discussion/SKILL.md:68–93](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-rpi-claude-plugin/skills/create-design-discussion/SKILL.md#L68-L93)
- [apps/riptide-rpi-claude-plugin/skills/create-design-discussion/SKILL.md:127–133](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-rpi-claude-plugin/skills/create-design-discussion/SKILL.md#L127-L133)
- [apps/riptide-rpi-claude-plugin/skills/create-prd/SKILL.md:8–28](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-rpi-claude-plugin/skills/create-prd/SKILL.md#L8-L28)
- [apps/riptide-rpi-claude-plugin/skills/create-prd/SKILL.md:43–54](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-rpi-claude-plugin/skills/create-prd/SKILL.md#L43-L54)
- [apps/riptide-rpi-claude-plugin/skills/create-prd/SKILL.md:93–116](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-rpi-claude-plugin/skills/create-prd/SKILL.md#L93-L116)
- [apps/riptide-rpi-claude-plugin/skills/create-prd/SKILL.md:138–145](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-rpi-claude-plugin/skills/create-prd/SKILL.md#L138-L145)
- [apps/riptide-rpi-claude-plugin/skills/create-tdd/SKILL.md:8–33](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-rpi-claude-plugin/skills/create-tdd/SKILL.md#L8-L33)
- [apps/riptide-rpi-claude-plugin/skills/create-tdd/SKILL.md:160–167](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-rpi-claude-plugin/skills/create-tdd/SKILL.md#L160-L167)
- [apps/riptide-rpi-claude-plugin/skills/create-tdd/SKILL.md:268–275](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-rpi-claude-plugin/skills/create-tdd/SKILL.md#L268-L275)
- [apps/docs/explanation/tasks.md:3–10](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/docs/explanation/tasks.md#L3-L10)
- [apps/docs/explanation/tasks.md:46–102](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/docs/explanation/tasks.md#L46-L102)
- [apps/docs/guide/skills-workflows.md:45–88](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/docs/guide/skills-workflows.md#L45-L88)
- [apps/docs/reference/skills-workflows.md:24–31](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/docs/reference/skills-workflows.md#L24-L31)
- [apps/docs/reference/skills-workflows.md:534–572](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/docs/reference/skills-workflows.md#L534-L572)

### context-handoff

- [apps/riptide-rpi-claude-plugin/skills/implement-outline/SKILL.md:8–52](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-rpi-claude-plugin/skills/implement-outline/SKILL.md#L8-L52)
- [apps/riptide-rpi-claude-plugin/skills/implement-outline/SKILL.md:69–113](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-rpi-claude-plugin/skills/implement-outline/SKILL.md#L69-L113)
- [apps/riptide-daemon/src/agents/claudecode/agents/outline-implementer-agent.ts:14–30](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/agents/claudecode/agents/outline-implementer-agent.ts#L14-L30)
- [apps/riptide-daemon/src/agents/claudecode/agents/outline-implementer-agent.ts:44–78](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/agents/claudecode/agents/outline-implementer-agent.ts#L44-L78)
- [apps/docs/explanation/tasks.md:3–10](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/docs/explanation/tasks.md#L3-L10)
- [apps/docs/explanation/tasks.md:46–102](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/docs/explanation/tasks.md#L46-L102)
- [apps/docs/guide/skills-workflows.md:45–88](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/docs/guide/skills-workflows.md#L45-L88)
- [apps/docs/reference/skills-workflows.md:24–31](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/docs/reference/skills-workflows.md#L24-L31)
- [apps/docs/reference/skills-workflows.md:534–572](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/docs/reference/skills-workflows.md#L534-L572)
- [apps/riptide-humanlayer-claude-plugin/skills/orchestrate/references/launch-task.md:1–3](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-humanlayer-claude-plugin/skills/orchestrate/references/launch-task.md#L1-L3)
- [apps/riptide-humanlayer-claude-plugin/skills/orchestrate/references/launch-task.md:115–131](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-humanlayer-claude-plugin/skills/orchestrate/references/launch-task.md#L115-L131)
- [apps/riptide-humanlayer-claude-plugin/skills/orchestrate/references/launch-task.md:175–183](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-humanlayer-claude-plugin/skills/orchestrate/references/launch-task.md#L175-L183)
- [apps/riptide-humanlayer-claude-plugin/skills/orchestrate/references/launch-session.md:14–23](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-humanlayer-claude-plugin/skills/orchestrate/references/launch-session.md#L14-L23)

### context-shards

- [packages/ai/src/agents/context-shards/generate-context-shard-candidates.ts:64–85](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/packages/ai/src/agents/context-shards/generate-context-shard-candidates.ts#L64-L85)
- [packages/ai/src/agents/context-shards/generate-context-shard-candidates.ts:122–150](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/packages/ai/src/agents/context-shards/generate-context-shard-candidates.ts#L122-L150)
- [packages/ai/src/agents/context-shards/generate-context-shard-candidates.ts:173–195](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/packages/ai/src/agents/context-shards/generate-context-shard-candidates.ts#L173-L195)
- [packages/db/src/tables/context-shards.ts:9–29](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/packages/db/src/tables/context-shards.ts#L9-L29)
- [packages/db/src/tables/context-shards.ts:44–52](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/packages/db/src/tables/context-shards.ts#L44-L52)
- [apps/riptide-api/src/orpc/daemon/context-shards/list-enabled.effect.ts:11–47](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-api/src/orpc/daemon/context-shards/list-enabled.effect.ts#L11-L47)
- [apps/riptide-api/test/procedures/daemon-context-shards.test.ts:117–190](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-api/test/procedures/daemon-context-shards.test.ts#L117-L190)
- [apps/riptide-daemon/src/agents/shared/context-shards.ts:12–55](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/agents/shared/context-shards.ts#L12-L55)
- [apps/riptide-daemon/test/effect/claude-context-shards.vi.test.ts:38–70](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/test/effect/claude-context-shards.vi.test.ts#L38-L70)
- [packages/ai/src/agents/context-shards/generate-context-shard-candidates.vi.test.ts:140–194](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/packages/ai/src/agents/context-shards/generate-context-shard-candidates.vi.test.ts#L140-L194)
- [packages/ai/eval/context-shards/generate-context-shard-candidates.test.ts:10–12](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/packages/ai/eval/context-shards/generate-context-shard-candidates.test.ts#L10-L12)
- [packages/ai/eval/context-shards/generate-context-shard-candidates.test.ts:36–79](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/packages/ai/eval/context-shards/generate-context-shard-candidates.test.ts#L36-L79)
- [packages/ai/eval/context-shards/fixtures.ts:6–28](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/packages/ai/eval/context-shards/fixtures.ts#L6-L28)

### file-artifacts

- [packages/session-sdk-artifacts/src/sync.ts:1–5](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/packages/session-sdk-artifacts/src/sync.ts#L1-L5)
- [packages/session-sdk-artifacts/src/sync.ts:204–267](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/packages/session-sdk-artifacts/src/sync.ts#L204-L267)
- [apps/riptide-daemon/src/lib/artifact-sync-utils.ts:38–58](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/lib/artifact-sync-utils.ts#L38-L58)
- [apps/riptide-daemon/src/lib/artifact-sync-utils.ts:84–154](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/lib/artifact-sync-utils.ts#L84-L154)
- [apps/riptide-daemon/test/unit/lib/artifact-sync-utils.test.ts:18–87](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/test/unit/lib/artifact-sync-utils.test.ts#L18-L87)
- [apps/riptide-daemon/test/unit/lib/artifact-sync-utils.test.ts:116–146](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/test/unit/lib/artifact-sync-utils.test.ts#L116-L146)

### feedback-targets

- [packages/db/src/tables/artifact-comments.ts:81–120](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/packages/db/src/tables/artifact-comments.ts#L81-L120)
- [packages/ui/src/artifact-viewer-v2/anchor/resolve.ts:35–80](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/packages/ui/src/artifact-viewer-v2/anchor/resolve.ts#L35-L80)
- [packages/ui/src/artifact-viewer-v2/anchor/resolve.ts:182–230](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/packages/ui/src/artifact-viewer-v2/anchor/resolve.ts#L182-L230)
- [packages/ui/src/artifact-viewer-v2/export/export-feedback.ts:27–76](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/packages/ui/src/artifact-viewer-v2/export/export-feedback.ts#L27-L76)
- [packages/ui/src/lib/diff-review/project-diff-comments.ts:158–192](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/packages/ui/src/lib/diff-review/project-diff-comments.ts#L158-L192)

### feedback-delivery

- [apps/riptide-ui/src/components/artifact-viewer-v2/delivery/executeBulkArtifactDelivery.ts:24–56](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-ui/src/components/artifact-viewer-v2/delivery/executeBulkArtifactDelivery.ts#L24-L56)
- [apps/riptide-ui/src/components/artifact-viewer-v2/delivery/executeBulkArtifactDelivery.test.ts:32–73](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-ui/src/components/artifact-viewer-v2/delivery/executeBulkArtifactDelivery.test.ts#L32-L73)
- [apps/riptide-ui/src/components/artifact-viewer-v2/delivery/executeBulkArtifactDelivery.test.ts:96–109](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-ui/src/components/artifact-viewer-v2/delivery/executeBulkArtifactDelivery.test.ts#L96-L109)

### review-watermarks

- [apps/riptide-ui/src/hooks/stores/taskDiffReviewMarksStore.ts:8–66](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-ui/src/hooks/stores/taskDiffReviewMarksStore.ts#L8-L66)
- [apps/riptide-ui/src/hooks/stores/taskDiffReviewMarksStore.ts:270–280](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-ui/src/hooks/stores/taskDiffReviewMarksStore.ts#L270-L280)

### domain-model

- [packages/db/src/tables/tasks.ts:59–98](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/packages/db/src/tables/tasks.ts#L59-L98)
- [packages/db/src/tables/sessions.ts:55–88](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/packages/db/src/tables/sessions.ts#L55-L88)
- [packages/db/src/tables/task-workspace-setup-for-host.ts:31–66](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/packages/db/src/tables/task-workspace-setup-for-host.ts#L31-L66)
- [packages/db/src/tables/artifacts.ts:21–40](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/packages/db/src/tables/artifacts.ts#L21-L40)

### authoritative-recheck

- [apps/riptide-daemon/src/subscriptions.ts:158–210](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/subscriptions.ts#L158-L210)
- [apps/riptide-daemon/src/effects/services/workspace-session-launch/workspace-session-launch.machine.ts:15–69](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/effects/services/workspace-session-launch/workspace-session-launch.machine.ts#L15-L69)
- [apps/riptide-daemon/src/effects/services/workspace-session-launch/workspace-session-launch.machine.ts:76–148](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/effects/services/workspace-session-launch/workspace-session-launch.machine.ts#L76-L148)
- [apps/riptide-daemon/src/effects/services/workspace-session-launch/workspace-session-launch.machine.ts:176–261](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/effects/services/workspace-session-launch/workspace-session-launch.machine.ts#L176-L261)
- [apps/riptide-daemon/src/effects/services/workspace-session-launch/workspace-session-launch-actors.layer.ts:71–134](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/effects/services/workspace-session-launch/workspace-session-launch-actors.layer.ts#L71-L134)
- [apps/riptide-daemon/test/effect/workspace-session-launch-actors.vi.test.ts:117–190](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/test/effect/workspace-session-launch-actors.vi.test.ts#L117-L190)

### session-ownership

- [apps/riptide-daemon/src/effects/services/daemon-instance-lock/daemon-instance-lock.layer.ts:28–103](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/effects/services/daemon-instance-lock/daemon-instance-lock.layer.ts#L28-L103)
- [apps/riptide-daemon/src/effects/services/session-runs/session-run-registry.ts:12–48](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/effects/services/session-runs/session-run-registry.ts#L12-L48)
- [apps/riptide-daemon/src/effects/services/fold-sessions/fold-session-runner.layer.ts:64–84](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/effects/services/fold-sessions/fold-session-runner.layer.ts#L64-L84)
- [apps/riptide-daemon/src/effects/services/fold-sessions/fold-session-runner.layer.ts:215–224](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/effects/services/fold-sessions/fold-session-runner.layer.ts#L215-L224)
- [apps/riptide-daemon/src/effects/services/fold-sessions/fold-session-runner.layer.ts:386–487](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/effects/services/fold-sessions/fold-session-runner.layer.ts#L386-L487)
- [apps/riptide-daemon/src/effects/services/fold-sessions/fold-session-runner.layer.ts:490–583](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/effects/services/fold-sessions/fold-session-runner.layer.ts#L490-L583)
- [apps/riptide-daemon/src/effects/services/fold-sessions/fold-session-runner.layer.ts:586–605](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/effects/services/fold-sessions/fold-session-runner.layer.ts#L586-L605)
- [apps/riptide-daemon/test/effect/fold-session-runner.vi.test.ts:583–698](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/test/effect/fold-session-runner.vi.test.ts#L583-L698)
- [apps/riptide-daemon/test/effect/fold-session-runner.vi.test.ts:753–790](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/test/effect/fold-session-runner.vi.test.ts#L753-L790)
- [apps/riptide-daemon/test/effect/fold-session-runner.vi.test.ts:851–887](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/test/effect/fold-session-runner.vi.test.ts#L851-L887)
- [apps/riptide-daemon/test/effect/fold-session-runner.vi.test.ts:893–927](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/test/effect/fold-session-runner.vi.test.ts#L893-L927)

### event-log

- [packages/db/src/tables/fold-session-events.ts:14–32](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/packages/db/src/tables/fold-session-events.ts#L14-L32)
- [apps/riptide-api/src/orpc/daemon/fold-session-events/append.effect.ts:25–29](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-api/src/orpc/daemon/fold-session-events/append.effect.ts#L25-L29)
- [apps/riptide-api/src/orpc/daemon/fold-session-events/append.effect.ts:14–18](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-api/src/orpc/daemon/fold-session-events/append.effect.ts#L14-L18)
- [apps/riptide-api/src/orpc/daemon/fold-session-events/append.effect.ts:31–131](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-api/src/orpc/daemon/fold-session-events/append.effect.ts#L31-L131)
- [apps/riptide-daemon/src/effects/services/fold-event-log/fold-event-log-session.ts:52–128](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/effects/services/fold-event-log/fold-event-log-session.ts#L52-L128)
- [apps/riptide-api/test/procedures/fold-session-events.test.ts:182–226](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-api/test/procedures/fold-session-events.test.ts#L182-L226)
- [apps/riptide-api/test/procedures/fold-session-events.test.ts:290–351](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-api/test/procedures/fold-session-events.test.ts#L290-L351)
- [apps/riptide-daemon/test/effect/fold-event-log-session.vi.test.ts:204–273](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/test/effect/fold-event-log-session.vi.test.ts#L204-L273)
- [apps/riptide-daemon/test/effect/fold-event-log-session.vi.test.ts:564–594](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/test/effect/fold-event-log-session.vi.test.ts#L564-L594)

### stream-recovery

- [apps/riptide-daemon/src/effects/services/stream-producer/durable-stream-writer.ts:91–110](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/effects/services/stream-producer/durable-stream-writer.ts#L91-L110)
- [apps/riptide-daemon/src/effects/services/stream-producer/durable-stream-writer.ts:125–163](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/effects/services/stream-producer/durable-stream-writer.ts#L125-L163)
- [apps/riptide-daemon/src/effects/services/stream-producer/durable-stream-writer.ts:165–233](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/effects/services/stream-producer/durable-stream-writer.ts#L165-L233)
- [apps/riptide-daemon/src/effects/services/stream-producer/durable-stream-writer.ts:235–260](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/effects/services/stream-producer/durable-stream-writer.ts#L235-L260)
- [apps/riptide-daemon/src/effects/services/stream-producer/stream-producer.service.ts:125–177](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/effects/services/stream-producer/stream-producer.service.ts#L125-L177)
- [apps/riptide-daemon/src/effects/services/stream-producer/stream-producer-recovery.ts:7–58](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/effects/services/stream-producer/stream-producer-recovery.ts#L7-L58)

### auth-boundaries

- [apps/riptide-api/src/auth/context.ts:11–20](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-api/src/auth/context.ts#L11-L20)
- [apps/riptide-api/src/auth/context.ts:49–79](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-api/src/auth/context.ts#L49-L79)
- [apps/riptide-api/src/db/host-auth.ts:6–31](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-api/src/db/host-auth.ts#L6-L31)
- [apps/riptide-api/src/db/task-auth.ts:223–270](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-api/src/db/task-auth.ts#L223-L270)
- [apps/riptide-api/src/lib/session-multiplayer-prompting-auth.ts:12–84](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-api/src/lib/session-multiplayer-prompting-auth.ts#L12-L84)
- [apps/riptide-electric-proxy/src/routes/response-editor-collaboration.ts:20–49](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-electric-proxy/src/routes/response-editor-collaboration.ts#L20-L49)

### permissions

- [apps/riptide-daemon/src/effects/services/claude-sessions/workflows/approvals.ts:62–158](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/effects/services/claude-sessions/workflows/approvals.ts#L62-L158)
- [apps/riptide-daemon/src/effects/services/claude-sessions/query-options.ts:74–119](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/effects/services/claude-sessions/query-options.ts#L74-L119)
- [apps/riptide-daemon/src/agents/claudecode/permission-mode.ts:7–17](https://github.com/humanlayer/humanlayer/blob/2f66a45b186d88488fa356862be0117db1ccae9f/apps/riptide-daemon/src/agents/claudecode/permission-mode.ts#L7-L17)

## Why we cite this

The source exposes both workflow instructions and the machinery that executes, synchronizes, reviews, and recovers agent work. That enables sharper distinctions than a README-only ingest: fact versus design, suggestion versus decision, read versus prompt access, retry versus conflicting intent, local review versus approval, and durable history versus durable external effects.

## Related sources

- [[sources/vercel--eve#docs-execution-model]] — checkpointed workflow execution, a different durability contract; do not infer equivalent guarantees from persistence alone.
- [[sources/every--compound-engineering-plugin#plugin-AGENTS.md]] — calibrate prescriptiveness to the actual failure mode.
- [[artifacts/projects/humanlayer]] — full product/runtime extraction.
- [[artifacts/plugins/humanlayer-rpi]] — full workflow/context extraction.
