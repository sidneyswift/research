# Capture: self-updating-harness

Canonical URL: https://www.mintlify.com/blog/harness-and-memory-architecture-behind-self-updating-docs
Resolved URL: https://www.mintlify.com/blog/harness-and-memory-architecture-behind-self-updating-docs
Retrieved: 2026-11-05
Representation: server-provided textual representation
Content-Type: text/markdown; charset=utf-8

---

# The Harness and Memory Architecture Behind Self-Updating Docs

> [llms.txt](https://www.mintlify.com/llms.txt)

How using fixed schema memory can improve agent performance at complex work.

- URL: https://www.mintlify.com/blog/harness-and-memory-architecture-behind-self-updating-docs
- Published: October 30, 2026
- Category: Engineering
- Authors: patrick-foster

Before Mintlify was a platform for writing documentation, we [started off trying to make docs self-updating](https://techcrunch.com/2022/05/30/mintlify-taps-ai-to-automatically-generate-documentation-from-code/).

It's the holy grail of problems for a documentation company.

It's also a hard problem. Docs changes take many forms, context is scattered across tools, and every team works differently.

We recently rebuilt our self-updating docs architecture from the ground up. Internally our docs PR accept rate has gone from 70% to 90%. Getting there meant rethinking the harness, the infrastructure, and memory.

## High-level architecture

We split the system into a background agent and a runner agent. Both run as an agent loop with access to a sandbox, the ability to clone repos, read access to third-party integrations, and a shared memory. Memory is stored as a git-backed repo containing different memory files, with every agent run log stored as JSON.

We store a set of triggers, such as cron schedules, merges in a repo, or events in third-party integrations (e.g., a project being marked as done in Jira). Each trigger is associated with a skill.

When a trigger fires, a job is queued for a runner agent to execute that skill. Most often, the runner's output is a documentation PR, followed by a notification asking the right people to review the change.

Every day we run the background agent for each site. Its system prompt tells it to take ownership of the documentation's success. Its optimization function is to maximize the number of merged docs PRs while keeping the accept rate above 80%.

To do this, the background agent can perform CRUD operations on the runner agent's triggers, their skills, and the shared memory. It decides what to change by reviewing past run logs, information in connected integrations, analytics from the docs platform, and which PRs are getting accepted.

For instance, one trigger listened for PR merges in a code repo. Its CLI docs PRs kept getting closed because the CLI ships on a rolling release cycle. The background agent noticed, removed CLI changes from that trigger's skill, and created a monthly cron trigger to write CLI release notes.

### Harness

We decided to build the harness in-house. We had previously tried using OpenCode and Pi but found they abstracted away too many of the underlying engineering decisions for it to perform well in our environment and match our data models.

Building a harness is fairly straightforward. We use Vercel's AI SDK to loop LLM calls and expose a set of tools. We built custom tools for subagents, compaction, following up on other runs, forking the current session, using skills, and running shell commands that we pipe to a sandbox. We benchmarked ours against Pi on an offline docs eval suite and found they had similar performance, but Pi used 50% more tokens.

## Fixed schema memory

The infrastructure above is table stakes. The real challenge is tastefully designing the memory scaffolding, custom tools, and preset skills.

Take the PR-merge trigger example from earlier. Memory has to answer a lot: Which team owns this change, and where do they discuss it in Slack or Notion? Should the docs build on a rolling release? Who should review it, and how should we notify them? The list goes on.

To avoid being noisy and to write at a high quality, our agent needs to know all of this reliably. We do this by storing a set of fixed schema JSON memory files.

For instance, here's a simplified version of what we store for each large feature release:

```ts
type Release = {
  // Code and docs PRs that make up the release
  codePRs: string[];
  // People driving or reviewing it
  stakeholders: UserID[];
  // Specs and planning docs in Google Docs or Notion
  docs: string[];
  commitDirectlyOrCreateOtherPRs:
    | 'commitDirectly'
    | 'other-prs';
  // Don't start drafting docs before this date
  startDraftingChangesDate: string | null;
  communicationMessaging: {
    relevantChannels: string[];
    issueTrackingProjects: string[];
    relevantThreads: string[];
  } | null;
};
```

We apply the same level of granularity to memory for users, style guides, site-wide settings, and every integration.

The memory repo file structure looks roughly like this:

```text
site-wide.json
style-guide.json
users/
  <userId>.json
releases/
  # One file per large feature release being worked on
  <releaseName>.json
integrations/
  issue-management.json      # Linear, Jira
  knowledge-management.json  # Notion, Confluence, Drive
  support-platform.json      # Zendesk, Intercom
  communication.json         # Slack
  code-repos.json
```

We do expose a few free-form markdown files for areas where we struggle to break down what we expect the agent to store.

### Why structured memory

We see a few benefits to storing memory this way.

Deciding what's important to store for future runs is a challenging problem for an agent. It requires a high level of empathy for what each runner agent will need as context, and LLMs aren't particularly good at this. Free-form markdown memory files may get underused, become too verbose, accidentally lose important information over time, or miss core parts of the team's workflow.

With a structured schema, maintaining memory becomes a well-scoped task for an agent. For instance, asking an LLM loop to find all code PRs related to a release is something it could do well. We can also run offline evals against it. For instance, for user memory, we can manually label a dataset of users in an org with the attributes we expect, then measure what percentage of those fields the agent gets right and hill-climb on that.

A structured format also gives us as developers a better intuition for what information our agent has access to. That lets us build skills and tools that are more empathetic to the agent's context.

## Over-the-air updates

One issue we quickly ran into was how to ship code changes to our agent. Each agent's setup quickly becomes a web of interconnected skills, tools, and memory files, and even a small text change to a preset skill could break a customer's self-updating docs setup.

We solve this by writing a plain-text description of breaking changes that we send as a prompt to each background agent. It's instructed to audit its current setup for regressions, monitor going forward, and update its memory files to match the new schemas.

We just rolled out support for larger code releases. We sent instructions on how data models and skills have changed to each of the background agents that had repos connected. Each agent deleted legacy fields from artifacts and began scanning the codebase to index larger features, storing their memory artifacts, then spinning off runner agents to implement them.

### Rolling out new products

Being able to send instructions to the background agent has other benefits.

Let's say we roll out a feature that automates product screenshots in your docs, and setting it up requires each customer to give us a production test account. Traditionally, we'd send an email blast to all customers, have our customer success team track down power users, and add product banners.

Now we can send a doc about the new feature to each background agent instead. From there, it can decide whether the customer is likely to turn it on (e.g., do they have a UI, do their docs use screenshots, and are they already at a success state?). Since it has an org-wide map of people, it can work out who to notify, prioritizing the people it already has the best rapport with, and it has an intuition for which messaging will resonate.

## Storing run logs

For the background agent to make intelligent decisions about how to improve the setup, it needs context on how the runner agent implemented its instructions. We do this by treating each agent session as an array of messages and their outputs (e.g., PRs or Slack notifications) which we can store as JSON files in the memory repo in the following format.

```text
RunnerAgent/
  <sessionId>/
    runLog.json
    output-<id>.json
BackgroundAgent/
  <sessionId>/
    runLog.json
```

To fork the current session, we create a new agent session with a pointer to the most recent message in the current session. Since each session can recursively create many forked child sessions, sessions form a tree, mirrored as nested folders in the run logs. Any leaf session's complete session history can be derived by traversing up to the root and stitching together each session along the way. Here is an example of a larger session tree being stored:

```text
RunnerAgent/
  <sessionId>/
    runLog.json
    output-<id>.json          # agent-forked
    output-<id>.json          # agent-forked
    <childSessionId>/
      # This fork finished without an output
      runLog.json
    <childSessionId>/
      runLog.json
      output-<id>.json        # pr-created
      output-<id>.json        # agent-forked
      <childSessionId>/
        runLog.json
        output-<id>.json      # pr-created
```

## What's next

This architecture now powers [Autopilot](https://www.mintlify.com/blog/autopilot), which we just launched. Moving our internal accept rate from 70% to 90% is a solid start, and we're excited to see if it holds as we scale. If you're curious why we are investing so heavily here, read [why self-updating external docs will be an infinite market](https://www.mintlify.com/blog/self-updating-external-docs-is-an-infinite-market).
