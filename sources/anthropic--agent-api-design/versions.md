# Anthropic API documentation — versions

Canonical URL: https://platform.claude.com/docs/en/api/versioning
Retrieved: 2026-11-04
Capture: rendered HTML text; navigation removed where structurally identifiable; no runtime tests.

---


Copy page

For any given API version, Anthropic preserves:
Existing input parameters
Existing output parameters
However, Anthropic may do the following:
Add additional optional inputs
Add additional values to the output
Change conditions for specific error types
Add new variants to enum-like output values (for example, streaming event types)
Generally, if you are using the API as documented in this reference, Anthropic will not break your usage.
Version history

Anthropic recommends using the latest API version whenever possible.
2026-10-21
Migrating to API version 2026-10-21
shows how to upgrade.
Available on the Claude API,
Claude Platform on AWS
,
Claude Models on Google Cloud (Anthropic managed)
,
Microsoft Foundry
, and
Claude Models on Google Cloud (Google managed)
. On
Amazon Bedrock
, it’s available for Claude 4.7 and later models. For other models on Bedrock, see the
migration guide for API version 2026-10-21
.
Messages API:
A request that places a
document
block directly in an
assistant
message returns a 400 error.
Sending a
text
block with a non-empty
citations
array in a
user
message, directly or inside a
search_result
block, returns a 400 error.
The
temperature
,
top_p
, and
top_k
request parameters are removed. A request that sends any of them returns a 400 error on every model.
Admin API:
RBAC groups
no longer return
roles
. Use
role_ids
instead.
RBAC group members
, and the response to removing one, no longer return
group_id
. Use
rbac_group_id
instead.
RBAC roles
no longer return
name
. Use
display_name
instead.
Organization
and
workspace
rate-limit entries, and the response to
setting a workspace’s rate limits
, no longer return
group_type
. Use
group.type
instead.
API keys
no longer return
workspace_id
. Use
scope.workspace_id
instead, which gives the workspace’s real ID even for the Default Workspace (an all-workspaces key has no
workspace_id
in
scope
).
Claude Enterprise Analytics API:
The per-user
usage
and
cost
reports no longer have
actor.email
. Use
actor.email_address
instead.
The
activity summaries
response no longer has
summaries
. Use
data
instead.
2023-06-01
New format for
streaming
server-sent events (SSE):
Completions are incremental. For example,
" Hello"
,
" my"
,
" name"
,
" is"
,
" Claude."
instead of
" Hello"
,
" Hello my"
,
" Hello my name"
,
" Hello my name is"
,
" Hello my name is Claude."
.
All events are
named events
, rather than
data-only events
.
Removed unnecessary
data: [DONE]
event.
Removed legacy
exception
and
truncated
values in responses.
2023-01-01
: Initial release.
Was this page helpful?


