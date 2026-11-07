# Capture: readme-ai-ready

Canonical URL: https://docs.readme.com/main/docs/ai-ready-docs
Resolved URL: https://docs.readme.com/main/docs/ai-ready-docs
Retrieved: 2026-11-05
Representation: server-provided textual representation
Content-Type: text/markdown; charset=utf-8

---

---
updatedAt: 2026-10-29T22:37:01.000Z
agentTools:
  siteIndex: https://docs.readme.com/llms.txt
  siteSearch: https://docs.readme.com/agentSearch?query=term1%20term2
  projectIndex: https://docs.readme.com/main/llms.txt
  projectSearch: https://docs.readme.com/main/agentSearch?query=term1%20term2
---

# AI-Ready Docs

Make your API docs usable by the AI agents and assistants your developers already work in.

Your docs have two audiences now: the developers who read them, and the AI agents those developers ask for help. ReadMe publishes your hub in the formats agents use, so a developer working in Cursor, Claude, ChatGPT, Gemini, or VS Code Copilot gets answers from your actual API spec and guides instead of guessing.

Each surface below does a different job, and most projects turn on more than one.

## What Each Surface Does

| Surface                                                                                           | What agents get                                                                                                                                                             | Where it's used                                                                                        | Plan                                                                                                                                                                         |
| ------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Markdown for Agents](https://docs.readme.com/main/docs/ai-discoverability#markdown-availability) | Clean Markdown instead of HTML whenever an agent asks for it (`Accept: text/markdown`), with links to sub pages, sibling pages, and What's Next so agents can crawl deeper. | Every agent that fetches your pages                                                                    | All plans                                                                                                                                                                    |
| [Project MCP](https://docs.readme.com/main/docs/mcp)                                              | A live connection to your API spec and docs. Agents list endpoints, read schemas, make API calls, and search your guides.                                                   | Any MCP client, including Cursor, Claude Code, VS Code Copilot, ChatGPT, Gemini CLI, and custom agents | OpenAPI tools on all plans. Doc search and fetch need the AI Add-on                                                                                                          |
| [LLMs.txt](https://docs.readme.com/main/docs/llmstxt)                                             | A Markdown index at `/llms.txt` that lists your guides and API Reference pages.                                                                                             | Any agent or crawler that requests the file                                                            | All plans                                                                                                                                                                    |
| [AI Dropdown](https://docs.readme.com/main/docs/askai)                                            | A menu on each guide page that opens the page in ChatGPT or Claude, or copies it as Markdown.                                                                               | ChatGPT, Claude, and any tool that accepts pasted Markdown                                             | All plans                                                                                                                                                                    |
| [AI Discoverability](https://docs.readme.com/main/docs/ai-discoverability)                        | The settings page for every agent-facing option, plus a grade against the Agent-Friendly Docs spec.                                                                         | Your project settings                                                                                  | All plans                                                                                                                                                                    |
| [Ask AI](https://docs.readme.com/main/docs/ask-ai)                                                | Answers to reader questions, drawn from your published content, inside your hub.                                                                                            | Your hub                                                                                               | [Ask AI Lite](https://docs.readme.com/main/docs/ask-ai#plans--availability) (All Plans) [Full Ask AI ](https://docs.readme.com/main/docs/ask-ai#plans--availability)(Add-on) |

<br />

## Choosing a Surface

Turning on **Markdown for Agents** is one of the most useful things you can do for AI readers. When an agent requests one of your pages, ReadMe returns clean Markdown instead of HTML, so the agent reads your content rather than your navigation, scripts, and styling. Browsers still get HTML, so your human readers see no change. Turn it on under **AI** → **AI Discoverability** in the **Markdown Availability** group, then enable **Show Sub Pages** and **Show Sibling Pages** so agents can follow links to the rest of your docs.

Enabling your project's **MCP Server** gives developers a live connection to your API from inside their AI coding assistant or agent. The assistant calls your spec directly, so it works from your current endpoints and parameters rather than whatever it picked up in training. Start here if your readers are building integrations.

Turning on **LLMs.txt** gives agents a map of your docs, so they can find the right page before they start reading. ReadMe builds the file from your sidebar and publishes it at `https://your-project.readme.io/llms.txt`. You'll find the toggle under **AI** → **AI Discoverability**. If you want to choose exactly which pages it lists, switch to a [custom LLMs.txt](https://docs.readme.com/main/docs/llmstxt#custom-llmstxt) and commit your own file to the root of your repo.

Turning o&#x6E;**&#x20;AI Dropdown** adds a menu to every guide page. From it, readers can open the page in ChatGPT or Claude with the content already loaded, or copy it as Markdown for any other tool. It's the quickest way for someone already reading your docs to keep going in their own assistant. To enable it, go to **AI** → **AI Dashboard**, toggle **AI Dropdown** on under **Reader Tools**, and pick which tools to show.

## What These Don't Do

None of these surfaces change what a model learned in training, and ReadMe can't make an AI provider request your files. Whether an agent reads `llms.txt`, asks for Markdown, or honors a content signal is up to the agent.

MCP exposes the same content to every connected user. Per-user data scoping comes from your API's own authentication, which the `execute-request` tool passes through. Private projects need a token to connect; see [MCP authentication](https://docs.readme.com/main/docs/mcp#authentication).

## Where to Start

1. Open **AI** → **AI Discoverability**, turn on **Markdown for Agents**, and check your current grade.
2. On the same page, confirm **LLMs.txt** is on.
3. Open **AI** → **MCP**, turn on your MCP Server, and copy the URL you'll share with your users.

# Sibling pages

* [Restless by ReadMe](https://docs.readme.com/main/docs/restless.md)
* [Agent](https://docs.readme.com/main/docs/aiagent.md)
* [Linter](https://docs.readme.com/main/docs/linter.md)
* [Docs Audit](https://docs.readme.com/main/docs/docs-audit.md)
* [AI Writer](https://docs.readme.com/main/docs/github-ai-writer.md)
* [Ask AI](https://docs.readme.com/main/docs/ask-ai.md)
* [MCP](https://docs.readme.com/main/docs/mcp.md)
* [AI Discoverability](https://docs.readme.com/main/docs/ai-discoverability.md)
* [LLMs.txt](https://docs.readme.com/main/docs/llmstxt.md)
* [AI Dropdown](https://docs.readme.com/main/docs/askai.md)
* [ReadMe's MCP Server](https://docs.readme.com/main/docs/readme-mcp.md)

# What's Next

* [MCP](https://docs.readme.com/main/docs/mcp.md)
* [Discoverability](https://docs.readme.com/main/docs/ai-discoverability.md)
* [LLMs.txt](https://docs.readme.com/main/docs/llmstxt.md)