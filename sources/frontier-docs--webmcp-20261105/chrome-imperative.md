# Capture: chrome-imperative

Canonical URL: https://developer.chrome.com/docs/ai/webmcp/imperative-api
Resolved URL: https://developer.chrome.com/docs/ai/webmcp/imperative-api
Retrieved: 2026-11-05
Representation: server-provided textual representation
Content-Type: text/markdown; charset=utf-8

---

![Alexandra Klepper](https://web.dev/images/authors/alexandraklepper.jpg) Alexandra Klepper [GitHub](https://github.com/alexandrascript) [Bluesky](https://bsky.app/profile/alexandrascript.com) ![François Beaufort](https://web.dev/images/authors/beaufortfrancois.jpg) François Beaufort [GitHub](https://github.com/beaufortfrancois)

<br />


Published: May 18, 2026, Last updated: October 16, 2026

<br />

| Explainer | Web | Extensions | Chrome Status | Intent |
|---|---|---|---|---|
| [GitHub](https://github.com/webmachinelearning/webmcp) | [![Origin trial](https://developer.chrome.com/static/images/experiment.svg) Origin trial](https://developer.chrome.com/origintrials/#/register_trial/4163014905550602241) |   | [View](https://chromestatus.com/feature/5117755740913664) | [Intent to Experiment](https://groups.google.com/a/chromium.org/g/blink-dev/c/gmYffo5WOE8/m/OJxuQRP3AAAJ) |

You can use the WebMCP Imperative API to define many types of tools with
standard JavaScript. Your tools can execute different functions, such as form
input, site navigation, and state management.

Before using this API, read about [example use cases](https://developer.chrome.com/docs/ai/webmcp).

> [!TIP]
> **Tip:** Use the [webmcp-types](https://www.npmjs.com/package/webmcp-types) npm package to get TypeScript typings for the Imperative API for easier access in your codebase.

## Provide model context

Use the `modelContext` interface to register tools. Tool registration requires
a name, description, and input schema with relevant properties.

Use `registerTool` to add a single tool to the model context.

### WebMCPza Maker

    await document.modelContext.registerTool({
      name: 'toggle_layer',
      description: 'Control pizza layers (sauce, cheese). Use "add", "remove", or "toggle".',
      inputSchema: {
        type: 'object',
        properties: {
          layer: { type: 'string', enum: ['sauce-layer', 'cheese-layer'] },
          action: { type: 'string', enum: ['add', 'remove', 'toggle'] },
        },
        required: ['layer'],
      },
      execute: async ({ layer, action }) => {
        await toggleLayer(layer, action);
        return `Performed ${action || 'toggle'} on layer: ${layer}`;
      },
    });

### Get order status

    await document.modelContext.registerTool({
      name: 'get_order_status',
      description: 'Search orders in a given timeframe. Returns order number, shipping status and location',
      inputSchema: {
        "type": "object",
        "properties": {
          "timeframe": { "type": "string", "oneOf": [
            { "type": "string", "const": "today", "title": "Today" },
            { "type": "string", "const": "yesterday", "title": "Yesterday" },
            { "type": "string", "const": "last_7_days", "title": "Last 7 Days" },
            { "type": "string", "const": "last_30_days", "title": "Last 30 Days" },
            { "type": "string", "const": "last_6_months", "title": "Last 6 Months" }],
          "enum": [ "today", "yesterday", "last_7_days", "last_30_days", "last_6_months" ],
          "description": "Timeframe for the order lookup." }
        },
        "required": [ "timeframe" ]
      },
      execute: async ({ timeframe }) => {
        // Add your API or database logic here to fetch and return the order data as a string.
      },
    });

### Tool annotations (optional)

When registering a tool, you can add metadata in the `annotations` property.
These annotations help agents and browsers understand a tool's safety
characteristics, expected side effects, output trustworthiness, and intended
audience:

- **`readOnlyHint`** (boolean, defaults to `false`): When `true`, indicates that the tool only reads information and does not modify the state of the application or system (for example, searching a product catalog or retrieving order status). This helps agents determine whether the tool can be safely called without side effects.
- **`untrustedContentHint`** (boolean, defaults to `false`): When `true`, indicates that the tool's output contains untrusted data from the perspective of the tool author (for example, user-generated content, reviews, or external web data). This signals to the agent and client that the returned payload requires heightened security handling, such as sanitization or delimiting, to mitigate [indirect prompt injection](https://developer.chrome.com/docs/ai/webmcp/secure-tools).
- **`consequentialHint`** (boolean, defaults to `false`): When `true`, indicates that executing the tool results in significant, real-world, or non-reversible actions (for example, booking a flight, transferring money, or deleting data). This allows agents and browsers to enforce mandatory user confirmation prompts before executing high-stakes tools, mitigating the risk of accidental or malicious misrepresentation of user intent.
- **`debugging`** (boolean, defaults to `false`, available from Chrome 156): When `true`, indicates that the tool is designed specifically for inspection and developer tooling (for example, testing frameworks or Chrome DevTools AI assistance) rather than end-user interactions. This allows general-purpose and end-user agents to filter out developer-focused tools.

    await document.modelContext.registerTool({
      name: 'book_flight',
      description: 'Book a flight for the user with confirmed flight details.',
      inputSchema: {
        type: 'object',
        properties: {
          flightId: { type: 'string', description: 'ID of the flight to book' },
          passengers: { type: 'number', description: 'Number of tickets to purchase' },
        },
        required: ['flightId', 'passengers'],
      },
      annotations: {
        readOnlyHint: false,
        consequentialHint: true,
        untrustedContentHint: false,
        debugging: false,
      },
      execute: async ({ flightId, passengers }) => {
        // Add your flight booking transaction logic here.
        return `Booked ${passengers} passenger(s) on flight ${flightId}.`;
      },
    });

For examples of how annotations can influence agent behavior, see the [Example WebMCP extension](https://github.com/GoogleChromeLabs/webmcp-extension/).

### Unregister tools

You can remove a tool with `AbortSignal`, when passed as an optional parameter.

    const addTodoTool = {
      name: "addTodo",
      description: "Add a new item to the to-do list",
      inputSchema: {
        type: "object",
        properties: { text: { type: "string" } },
      },
      execute: async ({ text }) => {
        // You should handle the persistence logic here (omitted for demo)
        return `Added to-do: ${text}`;
      },
      annotations: {
        readOnlyHint: false,
        untrustedContentHint: true
      },
    };
    const controller = new AbortController();
    await document.modelContext.registerTool(addTodoTool, { signal: controller.signal });

    // Unregister the tool later...
    controller.abort();

As of Chrome 153, you can unregister a tool without cancelling and breaking in-flight
executions. This prevents unexpected side effects when managing tool lifecycles in
component frameworks.

### Handle tool cancellation

The `execute` function receives an `AbortSignal` parameter named `signal` as its second argument to gracefully handle execution cancellations initiated by the user or agent. Passing this signal to long-running asynchronous tasks or network operations (such as `fetch()`) helps prevent unnecessary work, improves overall resource management, and avoids potential leaks.

    await document.modelContext.registerTool({
      name: 'fetch_tool',
      description: 'Fetch the text content of a URL and stream the response.',
      inputSchema: {
        type: 'object',
        properties: {
          url: { type: 'string', description: 'The URL to fetch' },
          priority: { type: 'string', enum: ['high', 'low', 'auto'] },
        },
        required: ['url'],
      },
      execute: async ({ url, priority }, { signal }) => {
        // Abort the fetch request when tool execution is aborted.
        const response = await fetch(url, { priority, signal });
        const stream = response.body.pipeThrough(new TextDecoderStream());
        for await (const chunk of stream) {
          document.querySelector('pre').textContent += chunk;
        }
        return 'Success';
      },
    });

## Discover tools

Use `document.modelContext.getTools()` to retrieve available tools. This
asynchronous method returns an alphabetically ordered list of tools that the
calling document is authorized to access.

    const [tool] = await document.modelContext.getTools();
    console.log(tool);

    // {
    //   annotations: { consequentialHint: false, debugging: false, readOnlyHint: false, untrustedContentHint: true }, // Optional hints
    //   description: "Add a new item to the to-do list",
    //   inputSchema: {"type":"object","properties":{...}},
    //   name: "addTodo",
    //   origin: "https://example.com",
    //   title: ""
    //   window: Window {window: Window, self: Window, ...},
    // }

By default, `getTools()` returns only same-origin tools registered by the calling
document or other same-origin documents in the frame tree. To retrieve
cross-origin tools, you must explicitly list their origins in the `fromOrigins`
option. This array only supports secure origins.

Tools from cross-origin documents are only included if:

1. The hosting origin is listed in the `fromOrigins` option.
2. The tool has been explicitly [exposed to your origin](https://developer.chrome.com/docs/ai/webmcp/imperative-api#origin-exposure).

    // https://example.com

    // Get same-origin tools only
    const sameOriginTools = await document.modelContext.getTools();

    // Get same-origin tools plus tools from specific cross-origin documents
    const allTools = await document.modelContext.getTools({
      fromOrigins: ['https://partner.org']
    });

See the [WebMCP Page Agent demo](https://github.com/GoogleChromeLabs/webmcp-tools/tree/main/demos/page-agent)
for an example of how to retrieve tools from an iframe and execute them within a web-based chat interface.
Refer to the [Example WebMCP extension](https://github.com/GoogleChromeLabs/webmcp-extension/)
to see how an agent in a browser extension finds and runs tools across same-origin and cross-origin iframes.

## Execute tool

To manually execute a tool discovered in `getTools()`, call
`document.modelContext.executeTool()` with an optional JavaScript object for
input arguments that is serializable to a JSON string. This asynchronous method
returns the result of the tool execution, or null when a navigation is triggered.

    const result = await document.modelContext.executeTool(tool, { text: "Buy milk" });
    console.log(result);

    // 'Added to-do: Buy milk'

You can cancel a pending tool execution with `AbortSignal`, when passed as an
optional parameter.

    const controller = new AbortController();
    document.modelContext.executeTool(tool, { text: "Buy milk" }, { signal: controller.signal });

    // Cancel tool execution later...
    controller.abort();

> [!NOTE]
> **Note:** JSON stringified input arguments are deprecated from Chrome 155.

## Events

Frames can listen for the `toolchange` event on `document.modelContext` to be
notified when the list of available tools has changed.

    document.modelContext.addEventListener("toolchange", (event) => {
      // Tools have changed.
    });

## Cross-origin iframes

WebMCP supports cross-origin iframes that use both permission
policies and explicit origin gating.

### Permissions policy

Tool registration is disabled by default in cross-origin iframes. A page must
delegate access using the `tools`
[Permissions Policy](https://developer.chrome.com/docs/privacy-security/permissions-policy):

    <iframe src="https://example.com" allow="tools"></iframe>

### Origin exposure

Tools are unavailable to cross-origin documents by default. You can use the
`exposedTo` array within `registerTool` to list specific origins allowed to view
and execute a tool. This array only supports secure origins.

> [!NOTE]
> **Note:** Even if a tool is exposed to your origin, you must still explicitly request it from the hosting origin using the `fromOrigins` option in [`getTools()`](https://developer.chrome.com/docs/ai/webmcp/imperative-api#discover-tools).

    // https://partner.org

    await document.modelContext.registerTool({
      name: 'my_shared_tool',
      description: 'Shared across origins',
      // ...
    }, {
      exposedTo: ['https://example.com']
    });

## Support in common JavaScript frameworks

React, Angular, and Vue have experimental support for WebMCP.

- [**React**](https://www.npmjs.com/package/use-webmcp-tool): Use the `use-webmcp-tool` package. Register tools using the `useWebMCP` hook tied to your component's mount and unmount lifecycle. This hook supports conditional tool registration, and automatically normalizes execution results.
- [**Angular**](https://angular.dev/ai/webmcp): Register tools tied to the application's dependency injection lifecycle and turn your Signal Forms into WebMCP tools.
- [**Vue**](https://vueuse.org/core/usewebmcp): Use the `useWebMCP` composable from the `@vueuse/core` package. Register tools tied to the current Vue scope lifecycle. Vue's implementation supports reactive and conditional tool registration, and automatically normalizes execution results.

## Engage and share feedback

WebMCP is under active discussion and subject to change in the future. If you
try this API and have feedback, we'd love to hear it.

- [Read the WebMCP explainer](https://github.com/webmachinelearning/webmcp?tab=readme-ov-file), raise questions and participate in discussion.
- Read how to [build effective WebMCP tools](https://developer.chrome.com/docs/ai/webmcp/build-tools) and [WebMCP best practices](https://developer.chrome.com/docs/ai/webmcp/best-practices).
- Review the implementation for Chrome on [Chrome Status](https://chromestatus.com/feature/5117755740913664).
- [Join the early preview program](http://goo.gle/chrome-ai-dev-preview-join) for an early look at new APIs and access to our mailing list.
- If you have feedback on Chrome's implementation, file a [Chromium bug](https://crbug.com/new?component=2021259).