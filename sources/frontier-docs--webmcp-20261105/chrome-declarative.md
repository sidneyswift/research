# Capture: chrome-declarative

Canonical URL: https://developer.chrome.com/docs/ai/webmcp/declarative-api
Resolved URL: https://developer.chrome.com/docs/ai/webmcp/declarative-api
Retrieved: 2026-11-05
Representation: server-provided textual representation
Content-Type: text/markdown; charset=utf-8

---

![Alexandra Klepper](https://web.dev/images/authors/alexandraklepper.jpg) Alexandra Klepper [GitHub](https://github.com/alexandrascript) [Bluesky](https://bsky.app/profile/alexandrascript.com) ![François Beaufort](https://web.dev/images/authors/beaufortfrancois.jpg) François Beaufort [GitHub](https://github.com/beaufortfrancois)

<br />


Published: May 18, 2026, Last updated: September 25, 2026

<br />

| Explainer | Web | Extensions | Chrome Status | Intent |
|---|---|---|---|---|
| [GitHub](https://github.com/webmachinelearning/webmcp) | [![Origin trial](https://developer.chrome.com/static/images/experiment.svg) Origin trial](https://developer.chrome.com/origintrials/#/register_trial/4163014905550602241) |   | [View](https://chromestatus.com/feature/5117755740913664) | [Intent to Experiment](https://groups.google.com/a/chromium.org/g/blink-dev/c/gmYffo5WOE8/m/OJxuQRP3AAAJ) |

Use the Declarative API to transform standard HTML forms into WebMCP tools by
adding annotations. Annotations define the tool's name and purpose in the
`<form>` element, while the fields act as tool parameters. The browser
translates these elements into a structured representation that agents can use
similarly to [imperative tools](https://developer.chrome.com/docs/ai/webmcp/imperative-api).

Before using this API, read about [example use cases](https://developer.chrome.com/docs/ai/webmcp).

## Tool registration

Add the following HTML attributes to your form:

- `toolname`: Clearly name the tool, based on its purpose.
- `tooldescription`: Describe what action the tool takes and its purpose.

For example, the following form lives at `example.com/get-customer-support`:

    <form toolname="createSupportRequest" tooldescription="Submits a request for customer support.">
    </form>

When an agent calls `toolname`, the browser brings the form into focus and
populates its field. The form remains visible to the user.

If you remove either the `toolname` or `tooldescription` HTML attribute, the tool is unregistered.

### (Optional) Tool parameters

To improve accuracy, add the following HTML attributes to individual form elements:

- `toolparamdescription`: Map elements to a property description within the JSON Schema. Without this attribute, the browser uses the content within the associated `<label>` and skips descendants that are labelable. If there isn't a label, the browser refers to the `aria-description`.

The following form uses the optional parameters for the `<select>` element.

    <form toolname="supportRequestTool"
      tooldescription="Submit a request for support."
      action="/submit">

      <label for="firstName">First Name</label>
      <input type=text name=firstName>

      <label for="lastName">Last Name</label>
      <input type=text name=lastName>

      <select name="select" required
        toolparamdescription="Determines what team this request is routed to.">
        <option value="Customer happiness team">Return my purchase.</option>
        <option value="Distribution team">Check where my package is.</option>
        <option value="Website support team">Get help on the website.</option>
      </select>

      <button type=submit>Submit</button>
    </form>

The browser interprets this form as a tool, represented by the following JSON:

    [
      {
        "name": "supportRequestTool",
        "description": "Submit a request for support.",
        "inputSchema": {
          "type": "object",
          "properties": {
            "firstName": {
              "type": "string"
            },
            "lastName": {
              "type": "string"
            },
            "select": {
              "type": "string",
              "anyOf": [
                {
                  "type": "string",
                  "const": "Customer happiness team",
                  "title": "Return my purchase."
                },
                {
                  "type": "string",
                  "const": "Distribution team",
                  "title": "Check where my package is."
                },
                {
                  "type": "string",
                  "const": "Website support team",
                  "title": "Get help on the website."
                }
              ],
              "enum": [
                "Customer happiness team",
                "Distribution team",
                "Website support team"
              ],
              "description": "Determines what team this request is routed to."
            }
          },
          "required": [
            "select"
          ]
        }
      }
    ]

### Submit the form

You have two choices for form submission:

- The user must manually click **Submit** to complete the task.
- Add `toolautosubmit` to trigger submission and a navigation when the model invokes this tool.

The `SubmitEvent` interface introduces the `agentInvoked` boolean attribute. This attribute is set to true whenever a form is triggered by an AI agent, to adapt your web app's behavior specifically for agent-based interactions.

Additionally, the `SubmitEvent` includes the `respondWith(Promise<any>)` method,
so you can pass a promise to the browser that you resolve with the form's
results. The resulting value is then serialized and returned to the model as the
tool's output. To use this method, you must first call `preventDefault()` to
stop the browser's standard form submission.

    <form toolautosubmit toolname="search_tool"
      tooldescription="Search the web" action="/search">
      <input type=text name=query>
    </form>
    <script>
      document.querySelector("form").addEventListener("submit", (e) => {
        e.preventDefault();
        if (!myFormIsValid()) {
          if (e.agentInvoked) { e.respondWith(myFormValidationErrorPromise) };
          return;
        }
        if (e.agentInvoked) { e.respondWith(Promise.resolve("Search is done!")); }
      });
    </script>

The browser signals that an AI agent executed a tool with the `"toolactivated"`
event. This fires on the `document.modelContext` once form fields are pre-filled. Conversely, if
a user cancels the agentic operation or the `reset()` method is invoked, a
`"toolcancel"` event is triggered. Both of these events are non-cancelable and
provide a `toolName` attribute for identification.

    document.modelContext.addEventListener('toolactivated', ({ toolName }) => {
      console.log(`the tool "${toolName}" execution was activated.`);
      // TODO: Update UI or validate form if needed.
    });

    document.modelContext.addEventListener('toolcancel', ({ toolName }) => {
      console.log(`the tool "${toolName}" execution was cancelled.`);
      // TODO: Let the user know. Update UI.
    });

> [!NOTE]
> **Note:** `window.ontoolactivated` and `window.ontoolcancel` are not supported from Chrome 156.

## Modify focus indicator

A visible focus indicator is critical to inform users and agents where they're
on a page. When an agent successfully invokes a tool, focuses the associated
form, and auto-populates its fields, the browser triggers specific CSS
pseudo-classes for visual feedback:

- `:tool-form-active` is applied to the tool's HTML `form` element.
- `:tool-submit-active` is applied to the form's submit button, if one is present.

These classes are deactivated once the form submits, the agent cancels the
action, or the user resets the form. You can customize the CSS for these states
or rely on a default browser style.

    /* Chrome default declarative form styles. */
    form:tool-form-active {
      outline: light-dark(blue, cyan) dashed 1px;
      outline-offset: -1px;
    }

    input:tool-submit-active {
      outline: light-dark(red, pink) dashed 1px;
      outline-offset: -1px;
    }

Learn more about
[focus best practices and style](https://web.dev/learn/accessibility/focus).

## Engage and share feedback

WebMCP is under active discussion and subject to change in the future. If you
try this API and have feedback, we'd love to hear it.

- [Read the WebMCP explainer](https://github.com/webmachinelearning/webmcp), raise questions and participate in discussion.
- Read [WebMCP best practices](https://developer.chrome.com/docs/ai/webmcp/best-practices).
- Review the implementation for Chrome on [Chrome Status](https://chromestatus.com/feature/5117755740913664).
- [Join the early preview program](http://goo.gle/chrome-ai-dev-preview-join) for an early look at new APIs and access to our mailing list.
- If you have feedback on Chrome's implementation, file a [Chromium bug](https://crbug.com/new?component=2021259).