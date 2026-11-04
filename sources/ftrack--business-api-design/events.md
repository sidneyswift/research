# Handling events | Developer Hub

URL: https://developer.ftrack.com/api-clients/python/handling-events/index.html
Retrieved: 2026-11-04
Version: n/a (living page). Rendered-text capture; images/layout not preserved.

---

On this page
Events are generated in ftrack when things happen such as a task being updated or a new version being published. Each
~ftrack_api.session.Session
can optionally connect to the event server and can be used to subscribe to specific events and perform an action as a result. That action could be updating another related entity based on a status change or generating folders when a new shot is created for example.
The
~hub.EventHub
for each
~ftrack_api.session.Session
is accessible via
Session.event_hub <~ftrack_api.session.Session.event_hub>
.
Subscribing to events
​
To listen to events, you register a function against a subscription using
Session.event_hub.subscribe <hub.EventHub.subscribe>
. The subscription uses the
expression
syntax and will filter against each
~base.Event
instance to determine if the registered function should receive that event. If the subscription matches, the registered function will be called with the
~base.Event
instance as its sole argument. The
~base.Event
instance is a mapping like structure and can be used like a normal dictionary.
The following example subscribes a function to receive all 'ftrack.update' events and then print out the entities that were updated:
import
ftrack_api
def
my_callback
(
event
)
:
'''Event callback printing all new or updated entities.'''
for
entity
in
event
[
'data'
]
.
get
(
'entities'
,
[
]
)
:
# Print data for the entity.
print
(
entity
)
# Subscribe to events with the update topic.
session
=
ftrack_api
.
Session
(
auto_connect_event_hub
=
True
)
session
.
event_hub
.
subscribe
(
'topic=ftrack.update'
,
my_callback
)
At this point, if you run this, your code would exit almost immediately. This is because the event hub listens for events in a background thread. Typically, you only want to stay connected whilst using the session, but in some cases you will want to block and listen for events solely - a dedicated event processor. To do this, use the
EventHub.wait <hub.EventHub.wait>
method:
# Wait for events to be received and handled.
session
.
event_hub
.
wait
(
)
You cancel waiting for events by using a system interrupt (
Ctrl-C
). Alternatively, you can specify a
duration
to process events for:
# Only wait and process events for 5 seconds.
session
.
event_hub
.
wait
(
duration
=
5
)
note
Events are continually received and queued for processing in the background as soon as the connection to the server is established. As a result you may see a flurry of activity as soon as you call
~hub.EventHub.wait
for the first time.
Subscriber information
​
When subscribing, you can also specify additional information about your subscriber. This contextual information can be useful when routing events, particularly when
targeting events
. By default, the
~hub.EventHub
will set some default information, but it can be useful to enhance this. To do so, simply pass in
subscriber
as a dictionary of data to the
~hub.EventHub.subscribe
method:
session
.
event_hub
.
subscribe
(
'topic=ftrack.update'
,
my_callback
,
subscriber
=
{
'id'
:
'my-unique-subscriber-id'
,
'applicationId'
:
'maya'
}
)
Sending replies
​
When handling an event it is sometimes useful to be able to send information back to the source of the event. For example,
ftrack.location.request-resolve
would expect a resolved path to be sent back.
You can craft a custom reply event if you want, but an easier way is just to return the appropriate data from your handler. Any non
None
value will be automatically sent as a reply:
def
on_event
(
event
)
:
# Send following data in automatic reply.
return
{
'success'
:
True
,
'message'
:
'Cool!'
}
session
.
event_hub
.
subscribe
(
'topic=test-reply'
,
on_event
)
tip
See
handling replies
note
Some events are published
synchronously
. In this case, any returned data is passed back to the publisher directly.
Stopping events
​
The
event
instance passed to each event handler also provides a method for stopping the event,
Event.stop <base.Event.stop>
.
Once an event has been stopped, no further handlers for that specific event will be called
locally
. Other handlers in other processes may still be called.
Combining this with setting appropriate priorities when subscribing to a topic allows handlers to prevent lower priority handlers running when desired.
import
ftrack_api
import
ftrack_api
.
event
.
base
def
callback_a
(
event
)
:
'''Stop the event!'''
print
(
'Callback A'
)
event
.
stop
(
)
def
callback_b
(
event
)
:
'''Never run.'''
print
(
'Callback B'
)
session
=
ftrack_api
.
Session
(
auto_connect_event_hub
=
True
)
session
.
event_hub
.
subscribe
(
'topic=test-stop-event'
,
callback_a
,
priority
=
10
)
session
.
event_hub
.
subscribe
(
'topic=test-stop-event'
,
callback_b
,
priority
=
20
)
session
.
event_hub
.
publish
(
ftrack_api
.
event
.
base
.
Event
(
topic
=
'test-stop-event'
)
)
session
.
event_hub
.
wait
(
duration
=
5
)
Publishing events
​
So far we have looked at listening to events coming from ftrack. However, you are also free to publish your own events (or even publish relevant ftrack events).
To do this, simply construct an instance of
ftrack_api.event.base.Event
and pass it to
EventHub.publish <hub.EventHub.publish>
via the session:
import
ftrack_api
.
event
.
base
event
=
ftrack_api
.
event
.
base
.
Event
(
topic
=
'my-company.some-topic'
,
data
=
{
'key'
:
'value'
}
)
session
.
event_hub
.
publish
(
event
)
The event hub will automatically add some information to your event before it gets published, including the
source
of the event. By default the event source is just the event hub, but you can customise this to provide more relevant information if you want. For example, if you were publishing from within Maya:
session
.
event_hub
.
publish
(
ftrack_api
.
event
.
base
.
Event
(
topic
=
'my-company.some-topic'
,
data
=
{
'key'
:
'value'
}
,
source
=
{
'applicationId'
:
'maya'
}
)
)
Remember that all supplied information can be used by subscribers to filter events so the more accurate the information the better.
Publish synchronously
​
It is also possible to call
~hub.EventHub.publish
synchronously by passing
synchronous=True
. In synchronous mode, only local handlers will be called. The result from each called handler is collected and all the results returned together in a list:
import
ftrack_api
import
ftrack_api
.
event
.
base
def
callback_a
(
event
)
:
return
'A'
def
callback_b
(
event
)
:
return
'B'
session
=
ftrack_api
.
Session
(
auto_connect_event_hub
=
True
)
session
.
event_hub
.
subscribe
(
'topic=test-synchronous'
,
callback_a
,
priority
=
10
)
session
.
event_hub
.
subscribe
(
'topic=test-synchronous'
,
callback_b
,
priority
=
20
)
results
=
session
.
event_hub
.
publish
(
ftrack_api
.
event
.
base
.
Event
(
topic
=
'test-synchronous'
)
,
synchronous
=
True
)
print
(
results
)
[
'A'
,
'B'
]
Handling replies
​
When publishing an event it is also possible to pass a callable that will be called with any
reply event
received in response to the published event.
To do so, simply pass in a callable as the
on_reply
parameter:
def
handle_reply
(
event
)
:
print
(
'Got reply: {}'
.
format
(
event
)
)
session
.
event_hub
.
publish
(
ftrack_api
.
event
.
base
.
Event
(
topic
=
'test-reply'
)
,
on_reply
=
handle_reply
)
Targeting events
​
In addition to subscribers filtering events to receive, it is also possible to give an event a specific target to help route it to the right subscriber.
To do this, set the
target
value on the event to an
expression
. The expression will filter against registered
subscriber information
.
For example, if you have many subscribers listening for a event, but only want one of those subscribers to get the event, you can target the event to the subscriber using its registered subscriber id:
session
.
event_hub
.
publish
(
ftrack_api
.
event
.
base
.
Event
(
topic
=
'my-company.topic'
,
data
=
{
'key'
:
'value'
}
,
target
=
'id=my-custom-subscriber-id'
)
)
Expressions
​
An expression is used to filter against a data structure, returning whether the structure fulfils the expression requirements. Expressions are currently used for subscriptions when
subscribing to events
and for targets when
publishing targeted events
.
The form of the expression is loosely groupings of 'key=value' with conjunctions to join them.
For example, a common expression for subscriptions is to filter against an event topic:
'topic=ftrack.location.component-added'
However, you can also perform more complex filtering, including accessing nested parameters:
'topic=ftrack.location.component-added and data.locationId=london'
note
If the structure being tested does not have any value for the specified key reference then it is treated as
not
matching.
You can also use a single wildcard
*
at the end of any value for matching multiple values. For example, the following would match all events that have a topic starting with
ftrack.
:
'topic=ftrack.*'
Using pushToken to filter generated events
​
The
pushToken
feature allows you to tag events generated by your session and filter them when subscribing to events. This is particularly useful when you want to avoid processing events that your own code generated, preventing unwanted reactions to your own changes.
Setting a pushToken
​
To use pushToken filtering, set the
ftrack-pushtoken
header when initializing your
ftrack_api
session:
import
uuid
import
ftrack_api
# Create a session with a custom pushToken
session
=
ftrack_api
.
Session
(
headers
=
{
'ftrack-pushtoken'
:
'TESTING'
}
)
project
=
session
.
query
(
'select id from Project'
)
.
first
(
)
# Any operations performed on this session that would
# generate events will also include the pushToken
session
.
create
(
'Task'
,
{
'parent'
:
project
,
'name'
:
str
(
uuid
.
uuid4
(
)
)
}
)
session
.
commit
(
)
Filtering events by pushToken
​
Once you've set a pushToken, all events generated by that session will include the token in their data. You can then filter events based on this token when subscribing:
# Subscribe to updates, excluding events generated by sessions with 'TESTING'
session
.
event_hub
.
subscribe
(
'topic=ftrack.update and data.pushToken!=TESTING'
,
callback
=
callback
)
