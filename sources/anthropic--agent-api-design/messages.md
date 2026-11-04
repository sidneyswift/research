# Anthropic API documentation — messages

Canonical URL: https://platform.claude.com/docs/en/api/messages/create
Retrieved: 2026-11-04
Capture: rendered HTML text; navigation removed where structurally identifiable; no runtime tests.

---


Copy page

API version 2026-10-21

cURL
CLI
TypeScript
Python
Java
Go
Ruby
C#
PHP
cURL


A beta version of this method exists and may have additional functionality.
View the beta version
.
Create a Message

Copy page

API version 2026-10-21

cURL
CLI
TypeScript
Python
Java
Go
Ruby
C#
PHP
cURL


POST
/v1/messages
Send a structured list of input messages with text and/or image content, and the model will generate the next message in the conversation.
The Messages API can be used for either single queries or stateless multi-turn conversations.
Learn more about the Messages API in our
user guide
Headers

"anthropic-version"
:
optional
string

The version of the Claude API you want to use.
Read more about versioning and our version history
here
.
"anthropic-user-profile-id"
:
optional
string

The user profile ID to attribute this request to. Use when acting on behalf of a party other than your organization.

"anthropic-workspace-id"
:
optional
string

Optional header to select the Workspace for this request. The value is a Workspace ID (for example,
wrkspc_011CZkZaBF1tNoB5wlCeusgy
).
Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.
Body

max_tokens
:
number

The maximum number of tokens to generate before stopping.
Note that our models may stop
before
reaching this maximum. This parameter only specifies the absolute maximum number of tokens to generate.
Set to
0
to populate the
prompt cache
without generating a response.
Different models have different maximum values for this parameter.  See
models
for details.
minimum
0

messages
:
array of
MessageParam

Input messages.
Our models are trained to operate on alternating
user
and
assistant
conversational turns. When creating a new
Message
, you specify the prior conversational turns with the
messages
parameter, and the model then generates the next
Message
in the conversation. Consecutive
user
or
assistant
turns in your request will be combined into a single turn.
Each input message must be an object with a
role
and
content
. You can specify a single
user
-role message, or you can include multiple
user
and
assistant
messages.
If the final message uses the
assistant
role, the response content will continue immediately from the content in that message. This can be used to constrain part of the model's response. This is called prefill. On models that don't support prefill, creating a message that ends with a partial
assistant
response returns a 400 error. See
Prefill not supported
.
Example with a single
user
message:
[{"role": "user", "content": "Hello, Claude"}]

Example with multiple conversational turns:
[
  {"role": "user", "content": "Hello there."},
  {"role": "assistant", "content": "Hi, I'm Claude. How can I help you?"},
  {"role": "user", "content": "Can you explain LLMs in plain English?"},
]

Example with a partially-filled response from Claude, for models that support prefill:
[
  {"role": "user", "content": "What's the Greek name for Sun? (A) Sol (B) Helios (C) Sun"},
  {"role": "assistant", "content": "The best answer is ("},
]

Each input message
content
may be either a single
string
or an array of content blocks, where each block has a specific
type
. Using a
string
for
content
is shorthand for an array of one content block of type
"text"
. The following input messages are equivalent:
{"role": "user", "content": "Hello, Claude"}

{"role": "user", "content": [{"type": "text", "text": "Hello, Claude"}]}

See
input examples
.
Note that if you want to include a
system prompt
, you can use the top-level
system
parameter.
There is a limit of 100,000 messages in a single request.
One of the following:

UserMessageParam
object
{
content
,
role
}


content
:
MessageContentParam

One of the following:
role
:
"user"


AssistantMessageParam
object
{
content
,
role
}


content
:
MessageContentParam

One of the following:
role
:
"assistant"


SystemMessageParam
object
{
content
,
role
}


model
:
Model

The model that will complete your prompt.
See
models
for additional details and options.
One of the following:
"claude-haiku-5-5"

Fastest model for high-volume, real-time tasks
"claude-sonnet-5-5"

Efficient model for coding and agents
"claude-fable-5-1"

Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows
"claude-opus-5-5"

Powerful intelligence for coding, knowledge work, and long-running agents
"claude-mythos-5-1"

Our most capable model for cybersecurity and biology research, available through trusted access programs
"claude-sonnet-5"

Efficient model for coding and agents
"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems
"claude-mythos-5"

Most capable model for cybersecurity and biology research
"claude-opus-5"

Powerful intelligence for long-running agents and coding
"claude-opus-4-8"

Powerful intelligence for long-running agents and coding
"claude-opus-4-7"

Powerful intelligence for long-running agents and coding
"claude-opus-4-6"

Powerful intelligence for long-running agents and coding
"claude-sonnet-4-6"

Best combination of speed and intelligence
"claude-haiku-4-5"

"claude-haiku-4-5-20251001"

"claude-opus-4-5"

Powerful intelligence for long-running agents and coding
"claude-opus-4-5-20251101"

Powerful intelligence for long-running agents and coding

"claude-mythos-preview"
⁠
Deprecated

New class of intelligence, strongest in coding and cybersecurity
Will reach end-of-life on June 30, 2026. Please migrate to claude-mythos-5. Visit https://docs.anthropic.com/en/docs/resources/model-deprecations for more information.

"claude-sonnet-4-5"
⁠
Deprecated

High-performance model for agents and coding
Will reach end-of-life on November 30, 2026. Please migrate to claude-sonnet-5-5. Visit https://docs.anthropic.com/en/docs/resources/model-deprecations for more information.

"claude-sonnet-4-5-20250929"
⁠
Deprecated

High-performance model for agents and coding
Will reach end-of-life on November 30, 2026. Please migrate to claude-sonnet-5-5. Visit https://docs.anthropic.com/en/docs/resources/model-deprecations for more information.
string


cache_control
:
optional
CacheControlEphemeral
{
type
:
"ephemeral"
,
ttl
}
or
null

Top-level cache control automatically applies a cache_control marker to the last cacheable block in the request.
type
:
"ephemeral"


ttl
:
optional
"5m"
or
"1h"

The time-to-live for the cache control breakpoint.
This may be one the following values:
5m
: 5 minutes
1h
: 1 hour
Defaults to
5m
. See
prompt caching pricing
for details.
One of the following:
"5m"

"1h"


container
:
optional
MessageCreateParamsContainer
or
null

Container identifier for reuse across requests.
One of the following:

ContainerParams
object
{
id
,
skills
}

Container parameters with skills to be loaded.
id
:
optional
string
or
null

Container id

skills
:
optional
array of
SkillParams
{
type
,
skill_id
,
version
}
or
null

List of skills to load in the container
maxItems
20

type
:
"anthropic"
or
"custom"

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)
One of the following:
"anthropic"

"custom"


skill_id
:
string

Skill ID
minLength
1
maxLength
64

version
:
optional
string

Skill version or 'latest' for most recent version
minLength
1
maxLength
64
string


diagnostics
:
optional
DiagnosticsParam
{
previous_message_id
}
or
null

Request-level diagnostics. Supply
previous_message_id
to have the response include
diagnostics.cache_miss_reason
explaining any prompt-cache divergence from that prior request.

previous_message_id
:
optional
string
or
null

The
id
(
msg_...
) from this client's previous /v1/messages response. The server compares that request's prompt fingerprint against this one and returns
diagnostics.cache_miss_reason
when the prompt-cache prefix could not be reused. Pass
null
on the first turn to opt in without a prior message to compare.
maxLength
256
inference_geo
:
optional
string
or
null

Specifies the geographic region for inference processing. If not specified, the workspace's
default_inference_geo
is used.

metadata
:
optional
Metadata
{
user_id
}

An object describing metadata about the request.

user_id
:
optional
string
or
null

An external identifier for the user who is associated with the request.
This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.
maxLength
512

output_config
:
optional
OutputConfig
{
effort
,
format
}

Configuration options for the model's output, such as the output format.

effort
:
optional
"low"
or
"medium"
or
"high"
or
2
more
or
null

How much effort the model should put into its response. Higher effort levels may result in more thorough analysis but take longer.
Valid values are
low
,
medium
,
high
,
xhigh
, or
max
.
One of the following:
"low"

"medium"

"high"

"xhigh"

"max"


format
:
optional
JSONOutputFormat
{
type
:
"json_schema"
,
schema
}
or
null

A schema to specify Claude's output format in responses. See
structured outputs
type
:
"json_schema"

schema
:
map
[
unknown
]

The JSON schema of the format

service_tier
:
optional
"auto"
or
"standard_only"

Determines whether to use priority capacity (if available) or standard capacity for this request.
Anthropic offers different levels of service for your API requests. See
service-tiers
for details.
One of the following:
"auto"

"standard_only"


speed
:
optional
"standard"
or
"fast"
or
null

The inference speed mode for this request.
"fast"
enables high output-tokens-per-second inference.
Some models require the
fast-mode-2026-02-01
beta header for any
speed
value. See
fast mode
for which models.
One of the following:
"standard"

"fast"


stop_sequences
:
optional
array of
string

Custom text sequences that will cause the model to stop generating.
Our models will normally stop when they have naturally completed their turn, which will result in a response
stop_reason
of
"end_turn"
.
If you want the model to stop generating when it encounters custom strings of text, you can use the
stop_sequences
parameter. If the model encounters one of the custom sequences, the response
stop_reason
value will be
"stop_sequence"
and the response
stop_sequence
value will contain the matched stop sequence.

stream
:
optional
boolean

Whether to incrementally stream the response using server-sent events. When
true
, SDKs return a raw event stream.
In the TypeScript, Python and Ruby SDKs, the recommended way to stream is
messages.stream()
. It sets
stream
for you and accumulates the events into the final message. See
Streaming with SDKs
for an example in each language.

system
:
optional
string
or
array of
TextBlockParam

System prompt.
A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our
guide to system prompts
.
One of the following:
string


array of
TextBlockParam
{
type
:
"text"
,
text
,
cache_control
,
citations
}

type
:
"text"


text
:
string

minLength
1

cache_control
:
optional
CacheControlEphemeral
{
type
:
"ephemeral"
,
ttl
}
or
null

Create a cache control breakpoint at this content block.
type
:
"ephemeral"


ttl
:
optional
"5m"
or
"1h"

The time-to-live for the cache control breakpoint.
This may be one the following values:
5m
: 5 minutes
1h
: 1 hour
Defaults to
5m
. See
prompt caching pricing
for details.
One of the following:
"5m"

"1h"


citations
:
optional
array of
TextCitationParam
or
null

One of the following:

CitationCharLocationParam
object
{
type
:
"char_location"
,
cited_text
,
document_index
,
3
more
}

type
:
"char_location"

cited_text
:
string


document_index
:
number

minimum
0

document_title
:
string
or
null

minLength
1
maxLength
500
end_char_index
:
number


start_char_index
:
number

minimum
0

CitationPageLocationParam
object
{
type
:
"page_location"
,
cited_text
,
document_index
,
3
more
}

type
:
"page_location"

cited_text
:
string


document_index
:
number

minimum
0

document_title
:
string
or
null

minLength
1
maxLength
500
end_page_number
:
number


start_page_number
:
number

minimum
1

CitationContentBlockLocationParam
object
{
type
:
"content_block_location"
,
cited_text
,
document_index
,
3
more
}

type
:
"content_block_location"


cited_text
:
string

The full text of the cited block range, concatenated.
Always equals the contents of
content[start_block_index:end_block_index]
joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document_index
:
number

minimum
0

document_title
:
string
or
null

minLength
1
maxLength
500

end_block_index
:
number

Exclusive 0-based end index of the cited block range in the source's
content
array.
Always greater than
start_block_index
; a single-block citation has
end_block_index = start_block_index + 1
.

start_block_index
:
number

0-based index of the first cited block in the source's
content
array.
minimum
0

CitationWebSearchResultLocationParam
object
{
type
:
"web_search_result_location"
,
cited_text
,
encrypted_index
,
2
more
}

type
:
"web_search_result_location"

cited_text
:
string

encrypted_index
:
string


title
:
string
or
null

minLength
1
maxLength
512

url
:
string

minLength
1

CitationSearchResultLocationParam
object
{
type
:
"search_result_location"
,
cited_text
,
end_block_index
,
4
more
}

type
:
"search_result_location"


cited_text
:
string

The full text of the cited block range, concatenated.
Always equals the contents of
content[start_block_index:end_block_index]
joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

end_block_index
:
number

Exclusive 0-based end index of the cited block range in the source's
content
array.
Always greater than
start_block_index
; a single-block citation has
end_block_index = start_block_index + 1
.

search_result_index
:
number

0-based index of the cited search result among all
search_result
content blocks in the request, in the order they appear across messages and tool results.
Counted separately from
document_index
; server-side web search results are not included in this count.
minimum
0
source
:
string


start_block_index
:
number

0-based index of the first cited block in the source's
content
array.
minimum
0
title
:
string
or
null


thinking
:
optional
ThinkingConfigParam

Configuration for Claude's thinking.
With
{"type": "adaptive"}
, Claude decides when and how much to think. With
{"type": "enabled"}
(manual extended thinking), you set a
budget_tokens
of at least 1,024. Thinking tokens count toward your
max_tokens
limit.
Which
type
values are accepted, and what happens when you omit
thinking
, depend on the model. See
thinking
for each model's behavior.
One of the following:

tool_choice
:
optional
ToolChoice

How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.
One of the following:

tools
:
optional
array of
ToolUnion

Definitions of tools that the model may use.
If you include
tools
in your API request, the model may return
tool_use
content blocks that represent the model's use of those tools. You can then run those tools using the tool input generated by the model and then optionally return results back to the model using
tool_result
content blocks.
There are two types of tools:
client tools
and
server tools
. The behavior described below applies to client tools. For
server tools
, see their individual documentation as each has its own behavior (e.g., the
web search tool
).
Each tool definition includes:
name
: Name of the tool.
description
: Optional, but strongly-recommended description of the tool.
input_schema
:
JSON schema
for the tool
input
shape that the model will produce in
tool_use
output content blocks.
For example, if you defined
tools
as:
[
  {
    "name": "get_stock_price",
    "description": "Get the current stock price for a given ticker symbol.",
    "input_schema": {
      "type": "object",
      "properties": {
        "ticker": {
          "type": "string",
          "description": "The stock ticker symbol, e.g. AAPL for Apple Inc."
        }
      },
      "required": ["ticker"]
    }
  }
]

And then asked the model "What's the S&P 500 at today?", the model might produce
tool_use
content blocks in the response like this:
[
  {
    "type": "tool_use",
    "id": "toolu_01D7FLrfh4GYq7yT1ULFeyMV",
    "name": "get_stock_price",
    "input": { "ticker": "^GSPC" }
  }
]

You might then run your
get_stock_price
tool with
{"ticker": "^GSPC"}
as an input, and return the following back to the model in a subsequent
user
message:
[
  {
    "type": "tool_result",
    "tool_use_id": "toolu_01D7FLrfh4GYq7yT1ULFeyMV",
    "content": "259.75 USD"
  }
]

Tools can be used for workflows that include running client-side tools and functions, or more generally whenever you want the model to produce a particular JSON structure of output.
See our
guide
for more details.
One of the following:

Tool
object
{
type
,
input_schema
,
name
,
7
more
}


ToolBash20250124
object
{
type
:
"bash_20250124"
,
name
,
allowed_callers
,
4
more
}


CodeExecutionTool20250522
object
{
type
:
"code_execution_20250522"
,
name
,
allowed_callers
,
3
more
}


CodeExecutionTool20250825
object
{
type
:
"code_execution_20250825"
,
name
,
allowed_callers
,
3
more
}


CodeExecutionTool20260120
object
{
type
:
"code_execution_20260120"
,
name
,
allowed_callers
,
3
more
}

A
tools
entry for the code execution tool, version
code_execution_20260120
. It adds REPL state persistence to version
code_execution_20250825
.
REPL state persistence applies with programmatic tool calling. With it, the Python interpreter state, such as variable bindings, persists across requests that reuse the container.
See the
code execution tool guide
to learn what each tool version adds.

CodeExecutionTool20260521
object
{
type
:
"code_execution_20260521"
,
name
,
allowed_callers
,
3
more
}

Code execution tool with REPL state persistence.

BrowserToolset20260801
object
{
type
:
"browser_toolset_20260801"
,
cache_control
,
configs
}

The browser toolset: a single
tools[]
entry (carrying no
name
) that declares the browser tool family. The model is served
the family's tool with any members disabled via
configs
removed
from its schema.

MemoryTool20250818
object
{
type
:
"memory_20250818"
,
name
,
allowed_callers
,
4
more
}


ComputerToolset20260801
object
{
type
:
"computer_toolset_20260801"
,
cache_control
,
configs
}

The computer toolset: a single
tools[]
entry (carrying no
name
) that declares the computer tool family. The model is
served the family's tool with any members disabled via
configs
removed from its schema. Every member is enabled by default, zoom
included. The single-tool options
display_number
and
enable_zoom
are not fields of a toolset entry — it carries only
type
,
configs
, and
cache_control
; zoom is controlled
via
configs.zoom.enabled
.

ToolTextEditor20250124
object
{
type
:
"text_editor_20250124"
,
name
,
allowed_callers
,
4
more
}


ToolTextEditor20250429
object
{
type
:
"text_editor_20250429"
,
name
,
allowed_callers
,
4
more
}


ToolTextEditor20250728
object
{
type
:
"text_editor_20250728"
,
name
,
allowed_callers
,
5
more
}


WebSearchTool20250305
object
{
type
:
"web_search_20250305"
,
name
,
allowed_callers
,
7
more
}


WebFetchTool20250910
object
{
type
:
"web_fetch_20250910"
,
name
,
allowed_callers
,
9
more
}


WebSearchTool20260209
object
{
type
:
"web_search_20260209"
,
name
,
allowed_callers
,
7
more
}


WebFetchTool20260209
object
{
type
:
"web_fetch_20260209"
,
name
,
allowed_callers
,
9
more
}


WebFetchTool20260309
object
{
type
:
"web_fetch_20260309"
,
name
,
allowed_callers
,
10
more
}

Web fetch tool with use_cache parameter for bypassing cached content.

WebSearchTool20260318
object
{
type
:
"web_search_20260318"
,
name
,
allowed_callers
,
8
more
}


WebFetchTool20260318
object
{
type
:
"web_fetch_20260318"
,
name
,
allowed_callers
,
11
more
}


ToolSearchToolBm25_20251119
object
{
type
,
name
,
allowed_callers
,
3
more
}


ToolSearchToolRegex20251119
object
{
type
,
name
,
allowed_callers
,
3
more
}

Returns

Message
object
{
type
:
"message"
,
id
,
container
,
8
more
}


RawMessageStreamEvent
=
RawMessageStartEvent
or
RawMessageDeltaEvent
or
RawMessageStopEvent
or
3
more

One of the following:

Create a Message
cURL


curl
https://api.anthropic.com/v1/messages
\
-H
'
Content-Type
:
application/json'
\
-H
'
anthropic-version
:
2026-10-21
'
\
-H
"
Authorization
:
Bearer
$ANTHROPIC_API_KEY
"
\
--max-time
600
\
-d
'
{
"max_tokens"
:
1024
,
"messages"
: [
{
"content"
:
"Hello, world"
,
"role"
:
"user"
}
],
"model"
:
"claude-opus-5-5"
,
"stream"
:
false
,
"system"
: [
{
"text"
:
"Today'
\'
's date is 2024-06-01."
,
"type"
:
"text"
}
],
"thinking"
: {
"type"
:
"adaptive"
},
"tools"
: [
{
"input_schema"
: {
"type"
:
"object"
,
"properties"
: {
"location"
:
"bar"
,
"unit"
:
"bar"
},
"required"
: [
"location"
]
},
"name"
:
"name"
}
]
}
'
Response 200

{
"id"
:
"msg_013Zva2CMHLNnXjNJJKqJ2EF"
,
"container"
: {
"id"
:
"container_011CpZohnwH4vuy7gazohgSP"
,
"expires_at"
:
"2019-12-27T18:11:19.117Z"
,
"skills"
: [
{
"skill_id"
:
"pdf"
,
"type"
:
"anthropic"
,
"version"
:
"latest"
}
]
},
"content"
: [
{
"citations"
: [
{
"cited_text"
:
"The grass is green. The sky is blue."
,
"document_index"
:
0
,
"document_title"
:
"My Document"
,
"end_char_index"
:
0
,
"file_id"
:
"file_011CNha8iCJcU1wXNR6q4V8w"
,
"start_char_index"
:
0
,
"type"
:
"char_location"
}
],
"text"
:
"Hi! My name is Claude."
,
"type"
:
"text"
}
],
"diagnostics"
: {
"cache_miss_reason"
: {
"cache_missed_input_tokens"
:
0
,
"type"
:
"model_changed"
}
},
"model"
:
"claude-opus-5-5"
,
"role"
:
"assistant"
,
"stop_details"
: {
"category"
:
"cyber"
,
"explanation"
:
"This request was declined because it conflicts with Anthropic's Usage Policy."
,
"type"
:
"refusal"
},
"stop_reason"
:
"end_turn"
,
"stop_sequence"
:
null
,
"type"
:
"message"
,
"usage"
: {
"cache_creation"
: {
"ephemeral_1h_input_tokens"
:
0
,
"ephemeral_5m_input_tokens"
:
0
},
"cache_creation_input_tokens"
:
2051
,
"cache_read_input_tokens"
:
2051
,
"inference_geo"
:
"global"
,
"input_tokens"
:
2095
,
"output_tokens"
:
503
,
"output_tokens_details"
: {
"thinking_tokens"
:
0
},
"server_tool_use"
: {
"web_fetch_requests"
:
2
,
"web_search_requests"
:
0
},
"service_tier"
:
"standard"
,
"speed"
:
"standard"
}
}
Returns Examples
Response 200

{
"id"
:
"msg_013Zva2CMHLNnXjNJJKqJ2EF"
,
"container"
: {
"id"
:
"container_011CpZohnwH4vuy7gazohgSP"
,
"expires_at"
:
"2019-12-27T18:11:19.117Z"
,
"skills"
: [
{
"skill_id"
:
"pdf"
,
"type"
:
"anthropic"
,
"version"
:
"latest"
}
]
},
"content"
: [
{
"citations"
: [
{
"cited_text"
:
"The grass is green. The sky is blue."
,
"document_index"
:
0
,
"document_title"
:
"My Document"
,
"end_char_index"
:
0
,
"file_id"
:
"file_011CNha8iCJcU1wXNR6q4V8w"
,
"start_char_index"
:
0
,
"type"
:
"char_location"
}
],
"text"
:
"Hi! My name is Claude."
,
"type"
:
"text"
}
],
"diagnostics"
: {
"cache_miss_reason"
: {
"cache_missed_input_tokens"
:
0
,
"type"
:
"model_changed"
}
},
"model"
:
"claude-opus-5-5"
,
"role"
:
"assistant"
,
"stop_details"
: {
"category"
:
"cyber"
,
"explanation"
:
"This request was declined because it conflicts with Anthropic's Usage Policy."
,
"type"
:
"refusal"
},
"stop_reason"
:
"end_turn"
,
"stop_sequence"
:
null
,
"type"
:
"message"
,
"usage"
: {
"cache_creation"
: {
"ephemeral_1h_input_tokens"
:
0
,
"ephemeral_5m_input_tokens"
:
0
},
"cache_creation_input_tokens"
:
2051
,
"cache_read_input_tokens"
:
2051
,
"inference_geo"
:
"global"
,
"input_tokens"
:
2095
,
"output_tokens"
:
503
,
"output_tokens_details"
: {
"thinking_tokens"
:
0
},
"server_tool_use"
: {
"web_fetch_requests"
:
2
,
"web_search_requests"
:
0
},
"service_tier"
:
"standard"
,
"speed"
:
"standard"
}
}
