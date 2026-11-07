# Capture: readme-mcp

Canonical URL: https://docs.readme.com/main/docs/mcp
Resolved URL: https://docs.readme.com/main/docs/mcp
Retrieved: 2026-11-05
Representation: server-provided textual representation
Content-Type: text/markdown; charset=utf-8

---

---
updatedAt: 2026-10-29T05:26:08.000Z
agentTools:
  siteIndex: https://docs.readme.com/llms.txt
  siteSearch: https://docs.readme.com/agentSearch?query=term1%20term2
  projectIndex: https://docs.readme.com/main/llms.txt
  projectSearch: https://docs.readme.com/main/agentSearch?query=term1%20term2
---

# MCP

Give your users' AI tools live access to your API spec and docs.

Your MCP server gives AI assistants and agents a live connection to your API spec and documentation. It works with any MCP client, including Cursor, Claude Code, VS Code Copilot, ChatGPT, Gemini CLI, and agents you build yourself. Once enabled, AI tools connect to your MCP URL and can list endpoints, inspect schemas, make API calls, and search your docs directly, so they generate accurate code instead of guessing at your endpoints and parameters.

<br />

## Getting Started

1. Open your project in ReadMe.
2. Open **AI** → **MCP** and toggle **MCP Server** on.
3. Share the URL with your users: `https://your-project.readme.io/mcp`

Your hub's AI dropdown gives readers quick options to connect to Cursor, VS Code, or copy the MCP config directly. You can also write a custom guide page with connection instructions if you'd like to tailor the experience.

This is the MCP server your readers use with your API. To create and edit your own docs from an AI agent, use [ReadMe's MCP server](https://docs.readme.com/main/docs/readme-mcp) instead.

MCP gives agents tools to call. [LLMs.txt](https://docs.readme.com/main/docs/llmstxt) gives agents that read before they act a map of your docs, and most projects turn on both. Agents that fetch your pages directly get clean Markdown through [Markdown for Agents](https://docs.readme.com/main/docs/ai-discoverability#markdown-availability). For how all of these fit together, see [AI-Ready Docs](https://docs.readme.com/main/docs/ai-ready-docs).

<br />

## Configure

### Available tools

**OpenAPI tools** — available on all plans:

| Tool                   | What it does                                                                 |
| ---------------------- | ---------------------------------------------------------------------------- |
| `list-endpoints`       | Returns all API paths and HTTP methods with summaries                        |
| `get-endpoint`         | Returns full detail on one endpoint: parameters, security, description       |
| `search-endpoints`     | Case-insensitive search across paths, operations, and schemas                |
| `execute-request`      | Makes a live API call and returns the response                               |
| `list-specs`           | Lists all API specifications (for projects with more than one specification) |
| `get-server-variables` | Returns server variables                                                     |

**Documentation tools** — require AI Booster Pack:

| Tool     | What it does                                                                                        |
| -------- | --------------------------------------------------------------------------------------------------- |
| `search` | Full-text search across every visible guide section, recipes, and non-endpoint reference pages      |
| `fetch`  | Returns the full content of a guide, recipe, or non-endpoint reference page by its ID from `search` |

### Authentication

**Public projects** — no auth needed. Users connect with just the URL.

**API execution** — the `execute-request` tool forwards headers from the user's MCP config to your API. If your API requires an `Authorization` header:

```json
{
  "mcpServers": {
    "My API": {
      "url": "https://your-project.readme.io/mcp",
      "headers": {
        "Authorization": "Bearer user-api-key-here"
      }
    }
  }
}
```

**Private projects** — users must pass an `x-readme-auth` header:

| Access type            | Header          | Value                              |
| ---------------------- | --------------- | ---------------------------------- |
| Password protected     | `x-readme-auth` | The site password                  |
| Teammates only         | `x-readme-auth` | `Bearer rdme_xxx` (ReadMe API key) |
| Custom login (JWT/SSO) | `x-readme-auth` | `Bearer rdme_xxx` (ReadMe API key) |

For clients that don't support custom headers (like the Claude web UI), pass the same value as a `token` query parameter instead:

```
https://your-project.readme.io/mcp?token=your-site-password
https://your-project.readme.io/mcp?token=rdme_xxxxxxxxxxxx
```

### MCP server URLs

The standard URL is `https://your-project.readme.io/mcp`. Append parameters to customize behavior:

| Parameter          | Example                        | Description                                                                                                                                          |
| ------------------ | ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| `branch`           | `?branch=v2.0_my-branch`       | Connect to a specific version or branch. Doc search tools are not available on branches.                                                             |
| `projects`         | `?projects=projecta, projectb` | Enterprise only. Limit to one or more projects.                                                                                                      |
| `token`            | `?token=rdme_xxx`              | Authenticate to a private project without setting a header. Accepts the site password or a ReadMe API key — same value you'd use in `x-readme-auth`. |
| `server`           | `?server=1`                    | Select a server from your API spec by index (zero-based). Only this server is exposed, and requests to others are rejected.                          |
| `server_variables` | `?server_variables=region=eu`  | Override a server variable. Format: `KEY=VALUE`. Repeat the parameter for multiple variables.                                                        |

<Accordion title="Enterprise and custom domain URLs" icon="fa-building">
  | Scenario              | URL                                                                                                |
  | --------------------- | -------------------------------------------------------------------------------------------------- |
  | Custom domain         | `https://your-custom-domain.com/mcp`                                                               |
  | All projects merged   | `https://your-enterprise.readme.io/mcp`                                                            |
  | Filter to one project | `https://your-enterprise.readme.io/mcp?projects=projecta`                                          |
  | Set server vars       | `https://your-enterprise.readme.io/mcp?server_variables=region=eu&server_variables=host=stage.com` |
</Accordion>

### Custom tools

Define your own tools that users' AI assistants can call. Go to **AI** → **MCP** → **Custom Tools** and click **New Tool**.

Each tool requires a title, a description (when should the AI use it), and a body (instructions to follow). Tool titles cannot match built-in tool names.

### Controlling which endpoints are exposed

All endpoints in your OpenAPI spec are available by default. Toggle individual endpoints on or off in **AI** → **MCP** → **Enabled MCP Routes**.

<br />

## Connect From AI Tools

Your MCP server works with any MCP client, so connecting is a matter of giving the client your MCP URL. The AI Dropdown already handles Cursor and VS Code, and the sections below show setup for a few other common clients. Each client changes its menus often, so every section links to that client's own setup guide.

<Callout icon="⚠️" theme="warn">
  ### Treat any URL with a `token` as a secret

  Clients that can't send custom headers connect to private projects with `?token=` in the URL. Anyone who has that URL can read your private docs, so share it the way you'd share a password.
</Callout>

### ChatGPT

ChatGPT connects to remote MCP servers as a custom connector once **Developer mode** is on. Availability depends on your ChatGPT plan and workspace settings.

1. In ChatGPT, open **Settings** and turn on **Developer mode**.
2. Add a new connector and paste your MCP URL: `https://your-project.readme.io/mcp`
3. For a private project, add your token to the URL: `https://your-project.readme.io/mcp?token=rdme_xxxxxxxxxxxx`

ChatGPT connectors don't send custom headers, so `execute-request` calls reach your API without an `Authorization` header. Read-only tools like `list-endpoints` and `get-endpoint` work normally. See OpenAI's [MCP guide](https://developers.openai.com/api/docs/mcp) for current menu names.

### Gemini CLI

Gemini CLI reads MCP servers from `~/.gemini/settings.json`. Use the `httpUrl` field for a remote server:

```json
{
  "mcpServers": {
    "my-api": {
      "httpUrl": "https://your-project.readme.io/mcp",
      "headers": {
        "Authorization": "Bearer user-api-key-here"
      }
    }
  }
}
```

Or add it from the terminal:

```bash
gemini mcp add --transport http my-api https://your-project.readme.io/mcp
```

For a private project, add an `x-readme-auth` header with the value from the [Authentication](#authentication) table. See Google's [Gemini CLI MCP guide](https://geminicli.com/docs/tools/mcp-server/) for every option.

### Custom Agents

If you're building your own agent, point any MCP client library at your MCP URL and pass the same headers described in [Authentication](#authentication). This example uses the official [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) (v2, installed with `pip install mcp`) to connect and list the available tools:

```python
import asyncio

import httpx2

from mcp import Client
from mcp.client.streamable_http import streamable_http_client

MCP_URL = "https://your-project.readme.io/mcp"


async def main() -> None:
    # Headers are only needed if your API requires them
    async with httpx2.AsyncClient(
        headers={"Authorization": "Bearer user-api-key-here"},
    ) as http_client:
        transport = streamable_http_client(MCP_URL, http_client=http_client)
        async with Client(transport) as client:
            result = await client.list_tools()
            for tool in result.tools:
                print(tool.name)


asyncio.run(main())
```

The script prints the tool names from [Available tools](#available-tools), such as `list-endpoints` and `get-endpoint`. Agent frameworks that accept a remote MCP server URL, including the [OpenAI Responses API](https://developers.openai.com/api/docs/mcp) and Anthropic's [MCP connector](https://docs.claude.com/en/docs/agents-and-tools/mcp-connector), can use the same URL.

<br />

## Use Cases

These examples use the Petstore API to show what users can do with your MCP server.

### Build an API client

A developer connects their coding assistant to your MCP server and prompts:

```text
Write a Python script that lists all pets with status "available"
and lets me add a new pet by name.
```

The AI calls `list-endpoints` to discover the relevant paths, `get-endpoint` to read the schemas, and generates working code with correct fields and auth.

```python
import requests

BASE_URL = "https://petstore.swagger.io/v2"
API_KEY  = "your-api-key"

def list_available_pets():
    resp = requests.get(
        f"{BASE_URL}/pet/findByStatus",
        params={"status": "available"},
        headers={"api_key": API_KEY},
    )
    resp.raise_for_status()
    return resp.json()

def add_pet(name: str, status: str = "available") -> dict:
    payload = {"name": name, "status": status, "photoUrls": []}
    resp = requests.post(
        f"{BASE_URL}/pet",
        json=payload,
        headers={"api_key": API_KEY, "Content-Type": "application/json"},
    )
    resp.raise_for_status()
    return resp.json()
```

### Explore an unfamiliar API

```text
I've never used this API before. Use MCP tools to give me a quick-start
guide: what endpoints exist, what auth I need, and a curl example.
```

The AI calls `list-endpoints` and assembles an overview without you writing any additional documentation.

### Generate tests from your spec

```text
Look at the POST /pet endpoint and generate a Jest test suite covering:
a successful create, missing required fields, and an invalid status value.
```

The AI reads the request body schema, finds enum values for `status`, and writes tests against the actual contract.

### Automated API monitoring

```text
Check that the API is behaving correctly:
1. Call GET /pet/1 and verify the response matches the schema
2. Try POST /pet with an invalid status and confirm it returns a 400
3. Report any discrepancies
```

The agent uses `get-endpoint` to know what a valid response looks like, then `execute-request` to make the calls and compare.

## FAQ

<Accordion title="Can I show different information to different users?" icon="fa-users">
  Yes. You can scope the documentation and spec content itself per URL today using the `projects` parameter (Enterprise only) which lets you hand different users a URL covering only the project(s) relevant to them. Additionally, you can set a password per-project. Per-viewer personalization beyond that is on the roadmap.&#x20;
</Accordion>

<Accordion title="What plan do I need?" icon="fa-credit-card">
  OpenAPI tools are available on all plans. Documentation tools (search, fetch) require the [AI Booster Pack](https://readme.com/pricing) add-on. Upgrade from **Settings > Billing**.
</Accordion>

<Accordion title="Can I disable specific endpoints?" icon="fa-toggle-off">
  Yes. Go to **AI** (sparkle icon) → **MCP** → **Enabled MCP Routes** to toggle individual endpoints on or off.
</Accordion>

# Sub pages

* [MCP Metrics](https://docs.readme.com/main/docs/mcp-metrics.md)

# Sibling pages

* [Restless by ReadMe](https://docs.readme.com/main/docs/restless.md)
* [Agent](https://docs.readme.com/main/docs/aiagent.md)
* [Linter](https://docs.readme.com/main/docs/linter.md)
* [Docs Audit](https://docs.readme.com/main/docs/docs-audit.md)
* [AI Writer](https://docs.readme.com/main/docs/github-ai-writer.md)
* [Ask AI](https://docs.readme.com/main/docs/ask-ai.md)
* [AI-Ready Docs](https://docs.readme.com/main/docs/ai-ready-docs.md)
* [AI Discoverability](https://docs.readme.com/main/docs/ai-discoverability.md)
* [LLMs.txt](https://docs.readme.com/main/docs/llmstxt.md)
* [AI Dropdown](https://docs.readme.com/main/docs/askai.md)
* [ReadMe's MCP Server](https://docs.readme.com/main/docs/readme-mcp.md)

# What's Next

* [AI-Ready Docs](https://docs.readme.com/main/docs/ai-ready-docs.md)
* [LLMs.txt](https://docs.readme.com/main/docs/llmstxt.md)
* [MCP Metrics](https://docs.readme.com/main/docs/mcp-metrics.md)