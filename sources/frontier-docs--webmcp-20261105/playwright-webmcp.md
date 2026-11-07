# Capture: WebMCP | Playwright

Canonical URL: https://playwright.dev/docs/api/class-webmcp
Resolved URL: https://playwright.dev/docs/api/class-webmcp
Retrieved: 2026-11-05
Representation: HTML main/article converted to Markdown via markdownify; visual widgets and assets not captured
Content-Type: text/html; charset=utf-8

---

On this page

# WebMCP

[WebMCP](https://playwright.dev/docs/api/class-webmcp "WebMCP") exposes the tools that a frame registers through the experimental [WebMCP](https://webmachinelearning.github.io/webmcp/) browser API, `navigator.modelContext`. It lists the tools and calls them.

Instances are accessed through [frame.webmcp](https://playwright.dev/docs/api/class-frame#frame-webmcp). [page.webmcp](https://playwright.dev/docs/api/class-page#page-webmcp) is the instance of the main frame.

note

WebMCP is an experimental browser feature. Chromium enables it with the `--enable-features=WebMCP` launch argument, Firefox with the `dom.modelcontext.enabled` and `dom.modelcontext.testing.enabled` preferences. WebKit does not implement it.

Tool names, descriptions, input schemas and results are provided by the page, so treat them as untrusted input.

```
const browser = await chromium.launch({ args: ['--enable-features=WebMCP'] });



const page = await browser.newPage();



await page.goto('https://example.com');



for (const tool of await page.webmcp.tools())



console.log(tool.name, tool.description);



const result = await page.webmcp.callTool('add', { a: 2, b: 40 });
```

---

## Methods[​](https://playwright.dev/docs/api/class-webmcp#methods "Direct link to Methods")

### callTool[​](https://playwright.dev/docs/api/class-webmcp#web-mcp-call-tool "Direct link to callTool")

Added in: v1.64
webMCP.callTool

Calls a tool registered by the frame and returns its result. The result is whatever the tool's `execute` function resolved to, typically an object with a `content` array. A result with `isError: true` is returned as is. The method throws when the tool is not registered or its `execute` function throws.

```
const result = await page.webmcp.callTool('add', { a: 2, b: 40 });



console.log(result.content[0].text); // "42"
```

**Usage**

```
await webMCP.callTool(name);



await webMCP.callTool(name, input, options);
```

**Arguments**

* `name` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-webmcp#web-mcp-call-tool-option-name)

  Name of the tool, as reported by [webMCP.tools()](https://playwright.dev/docs/api/class-webmcp#web-mcp-tools).
* `input` [Serializable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#Description "Serializable") *(optional)*[#](https://playwright.dev/docs/api/class-webmcp#web-mcp-call-tool-option-input)

  Input for the tool, matching its `inputSchema`. Defaults to an empty object.
* `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") *(optional)*

  + `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") *(optional)*[#](https://playwright.dev/docs/api/class-webmcp#web-mcp-call-tool-option-timeout)

    Maximum time in milliseconds. Defaults to `0` - no timeout. The default value can be changed via `actionTimeout` option in the config, or by using the [browserContext.setDefaultTimeout()](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout) or [page.setDefaultTimeout()](https://playwright.dev/docs/api/class-page#page-set-default-timeout) methods.

**Returns**

* [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[Serializable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#Description "Serializable")>[#](https://playwright.dev/docs/api/class-webmcp#web-mcp-call-tool-return)

---

### tools[​](https://playwright.dev/docs/api/class-webmcp#web-mcp-tools "Direct link to tools")

Added in: v1.64
webMCP.tools

Returns the tools currently registered by the frame. Throws if the browser was launched without WebMCP support, see the note above for the launch options that enable it.

[page.webmcp](https://playwright.dev/docs/api/class-page#page-webmcp) covers the main frame only, child frames list their tools through their own [frame.webmcp](https://playwright.dev/docs/api/class-frame#frame-webmcp).

**Usage**

```
await webMCP.tools();



await webMCP.tools(options);
```

**Arguments**

* `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") *(optional)*
  + `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") *(optional)*[#](https://playwright.dev/docs/api/class-webmcp#web-mcp-tools-option-timeout)

    Maximum time in milliseconds. Defaults to `0` - no timeout. The default value can be changed via `actionTimeout` option in the config, or by using the [browserContext.setDefaultTimeout()](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout) or [page.setDefaultTimeout()](https://playwright.dev/docs/api/class-page#page-set-default-timeout) methods.

**Returns**

* [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")>>[#](https://playwright.dev/docs/api/class-webmcp#web-mcp-tools-return)
  + `name` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

    Tool name, unique within the frame.
  + `description` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

    Tool description.
  + `inputSchema` [Serializable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#Description "Serializable") *(optional)*

    JSON Schema of the tool input, when the page provides one.
  + `annotations` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") *(optional)*

    - `readOnly` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") *(optional)*

      The tool does not modify any state.
    - `untrustedContent` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") *(optional)*

      The tool output may contain third-party content.
    - `consequential` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") *(optional)*

      The tool takes a consequential action, such as placing an order.

    Hints the page provides about the tool.