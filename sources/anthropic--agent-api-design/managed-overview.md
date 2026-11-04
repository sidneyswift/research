# Anthropic API documentation — managed-overview

Canonical URL: https://platform.claude.com/docs/en/managed-agents/overview
Retrieved: 2026-11-04
Capture: rendered HTML text; navigation removed where structurally identifiable; no runtime tests.

---


Copy page


Managed Agents
Status
Beta
Cloud platforms

Claude API
Available

Claude Platform on AWS
Available

Claude Models on Google Cloud
Anthropic managed
Available
Beta header
managed-agents-2026-04-01

Data handling

Not ZDR eligible

Not HIPAA eligible
Anthropic offers two ways to build with Claude, each suited to different use cases:
Messages API
Claude Managed Agents
What it is
Direct model prompting access
Pre-built, configurable agent harness that runs in managed infrastructure
Best for
Custom agent loops and fine-grained control
Long-running tasks and asynchronous work
Claude Managed Agents provides the harness and infrastructure for running Claude as an autonomous agent. Instead of building your own agent loop, tool execution, and runtime, you get a fully managed environment where Claude can read files, run commands, browse the web, and run code securely. The harness supports built-in prompt caching, compaction, and other performance optimizations for high-quality, efficient agent outputs. To build your own agent loop with direct model access instead, see
Using the Messages API
.

Claude Managed Agents is also available on Claude Models on Google Cloud (Anthropic managed) and Claude Platform on AWS, with some differences in feature availability and session behavior. See the
Claude Models on Google Cloud (Anthropic managed)
guide or
Claude Managed Agents
in the Claude Platform on AWS guide.

Quickstart
Create your first agent session

Start a session
Create a session and send your first event

Reference
Event types, rate limits, CLI flags, and other lookup tables
Core concepts

Claude Managed Agents is built around four concepts:
Concept
Description
Agent
The model, system prompt, tools, MCP servers, and skills
Environment
Configuration for where sessions run: an Anthropic-managed cloud sandbox, or a self-hosted sandbox on your own infrastructure
Session
A running agent instance within an environment, performing a specific task and generating outputs
Events
Messages exchanged between your application and the agent (user turns, tool results, status updates)
How it works

1
Create an agent
Define the model, system prompt, tools, MCP servers, and skills. Create the agent once and reference it by ID across sessions.
2
Create an environment
Configure where the agent runs
: a cloud sandbox, or a
self-hosted sandbox
on your own infrastructure.
3
Start a session
Launch a session that references your agent and environment configuration.
4
Send events and stream responses
Send user messages as events. Claude autonomously runs tools and streams back results through server-sent events (SSE). Event history is persisted server-side and can be fetched in full.
5
Steer or interrupt
Send additional user events to guide the agent while it runs, or interrupt it to change direction.
When to use Claude Managed Agents

Claude Managed Agents is best for workloads that need:
Long-running execution:
Tasks that run for minutes or hours with multiple tool calls
Cloud infrastructure:
Secure sandboxes with pre-installed packages and network access
Self-hosted execution:
Sandboxes on infrastructure you control for compliance or data-residency requirements
Minimal infrastructure:
No need to build your own agent loop, sandbox, or tool execution layer
Stateful sessions:
Persistent filesystems and conversation history across multiple interactions
Scheduled execution:
Recurring agent runs on a cron schedule through
scheduled deployments
Supported tools

Claude Managed Agents gives Claude access to a set of built-in tools:
Bash:
Run shell commands in the sandbox
File operations:
Read, write, edit, glob, and grep files in the sandbox
Web search and fetch:
Search the web and retrieve content from URLs, optionally restricted to an allowlist or blocklist of domains
MCP servers:
Connect to external tool providers
See
Tools
for the full list and configuration options.
Beta access


Claude Managed Agents is in beta. All Managed Agents endpoints require the
managed-agents-2026-04-01
beta header. The SDK sets the beta header automatically. Behaviors may be refined between releases to improve outputs.
To get started, you need:
A
Claude API key
from the Claude Console
The
managed-agents-2026-04-01
beta header on all requests
Access to Claude Managed Agents (enabled by default for all API accounts)
Within the beta,
MCP tunnels
and
dreaming
are in a more limited research preview.
Request access
to enable them.
Claude Managed Agents is stateful by design: sessions are long-running, resume cleanly after pauses, and store conversation history, sandbox state, and outputs server-side. Because of this, Managed Agents is not currently eligible for
Zero Data Retention
or HIPAA Business Associate Agreement (BAA) coverage. You retain control over this data: you can
delete sessions
, and separately delete any
files
you uploaded, at any time through the API. For eligibility across all features, see
API and data retention
.
See
Rate limits
and
Branding guidelines
in the reference.
Availability

Managed Agents are in beta on every model.
API support

Status
Beta
Cloud platforms

Claude API

Claude Platform on AWS

Claude Models on Google Cloud
Anthropic managed
Models

All models
Required beta headers

Beta headers overview

Beta headers allow you to access experimental features and new model capabilities before they become part of the standard API.
Header
managed-agents-2026-04-01

Data handling

Data handling overview

Applicable endpoints
/v1/agents
/v1/sessions
/v1/environments
Zero data retention

Not eligible
Sessions are stateful resources; transcripts persist until you delete them. Applies to all Managed Agents sub-features, including Self-hosted sandboxes.
HIPAA

Not eligible
Applies to all Managed Agents sub-features, including Self-hosted sandboxes.
Was this page helpful?



Managed Agents
Status
Beta
Cloud platforms

Claude API
Available

Claude Platform on AWS
Available

Claude Models on Google Cloud
Anthropic managed
Available
Beta header
managed-agents-2026-04-01

Data handling

Not ZDR eligible

Not HIPAA eligible
