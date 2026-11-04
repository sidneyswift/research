# Authentication | Developer Hub

URL: https://developer.ftrack.com/api/authentication/index.html
Retrieved: 2026-11-04
Version: n/a (living page). Rendered-text capture; images/layout not preserved.

---

On this page
API keys are used to control access to resources through the API. There are two types of API keys in ftrack, personal and global.
Please note that API keys need to be used together with the username of an ftrack user. For personal API keys, the key must belong to the username, but for global API keys, the username could be any active user. When using a global key, permissions are assigned according to the role of the API key.
Personal API keys
​
Each user has a personal API key which has the same permissions as the user when logged into the ftrack web interface. The user API key can be found in
My Account > Security
.
Global API keys
​
Typically, it makes sense to restrict specific API key permissions to just those required by specific scripts and/or users. This is possible by linking permission roles to API keys.
For example, it is possible to have an API key that can only perform read-only operations for general use, whilst a separate API key might have full write permissions.
The roles for API keys work the same as the roles for users.
To add a new API role, navigate to
System settings > Security > Roles
. Click Create, enter a name for the role, and select API in the Role type drop-down. Next, select the permissions you would like to include and click Save.
For example, if you would like to restrict a role only to be able to create new projects, check the box next to Create and update projects and leave the rest as is.
To select a role for an API key, navigate to
System settings > Security > API
keys and either create or edit an existing key. In the dialog that appears, select at least one role in the Roles drop-down to set or edit which role(s), and corresponding permissions, are applied for the key.
By default, a global API key can only access data in projects with private access turned off, also known as open projects.
A global API key will be able to access a
private project
if it is awarded access to the project. (You can do this in system settings by adding the project to the Projects attribute of the API key.)
Only private projects are visible in the Projects drop-down of an API key’s edit dialog box because only private projects must be explicitly specified.
note
Global API keys must have at least one role set.
Example usage
​
To auhtorize to the ftrack API you need to provide
server url
,
api user
and the
api key
.
cURL
Python
JavaScript
curl
https://ftrack-test.ftrackapp.com/api
\
-X
POST
\
-H
"Content-Type: application/json"
\
-H
"ftrack-user: john"
\
-H
"ftrack-api-key: cdd5dcbc-d0bd-435c-8f9d-6ed6902cdd9a"
\
--data
'[]'
# Create session with credentials.
session
=
ftrack_api
.
Session
(
server_url
=
"https://mycompany.ftrackapp.com"
,
api_key
=
"7434384e-b653-11f1-a84d-f44c22dd25eu"
api_user
=
"john.doe@example.com"
)
#
Create
session
with
credentials
.
var
session
=
new
ftrack
.
Session
(
"https://mycompany.ftrackapp.com"
,
"john.doe@example.com"
,
"7434384e-b653-11f1-a84d-f44c22dd25eu"
)
;
