# Query language | Developer Hub

URL: https://developer.ftrack.com/api/query-language/index.html
Retrieved: 2026-11-04
Version: n/a (living page). Rendered-text capture; images/layout not preserved.

---

On this page
The API provides a straightforward, but powerful query language. Using queries correctly can often substantially speed up your code as well as reduce the amount of code written.
A query is issued as a string. It always has a single target entity type that the query is built against. This means that you cannot currently retrieve back a list of different entity types in one query, though using projections does allow retrieving related entities of a different type in one go.
The general syntax for a query is:
select
[
projection
]
from
[
where
]
[
ordering
]
[
offset
and
limit
]
Projections
​
Projections refer to the attributes that you want to have included in the returned data set for the specified entity type.
If a developer has not specified a custom set of projections, then it is recommended that the
default projections
for the entity type be inserted. Typically this would be the primary key. For example:
select
id
from
Asset
You can select multiple projections if desired:
select
id
,
name
from
Asset
It is also possible to select across relationships as a way to optimize loading of trees of data:
select
id
,
name
,
versions
.
version
,
versions
.
comment
from
Asset
Here we have specified to also include in the returned data a list of versions for the Asset with each version entry including the version and comment attribute values.
note
There are no arbitrary limits to the number (or depth) of projections, but do be aware that excessive projections can ultimately result in poor performance also. As always, it is about choosing the right tool for the job.
Criteria
​
Criteria allows the restricting of returned data to just entities that match the conditions specified. In this way you can avoid fetching more data than needed.
Each criteria follows the form:
[
not
]
[
attribute
]
[
operator
]
[
value
]
not
​
Optionally invert the criteria:
select
id
from
Project
where
not
status
is
active
Note that it is often more readable to use negating operators:
select
id
from
Project
where
status
is_not active
attribute
​
One of the specified entity type’s attribute names as described in the corresponding schema. Can use a dotted notation to stride across relationships.
operator
​
One of the supported operators that will be used to compare against value.
value
​
The expected value to compare against. Quotes should be used to enclose strings to help avoid ambiguity (for example when a string has spaces or special characters in int) and to separate it from keywords such as none.
Combining criteria
​
Multiple criteria can be applied in a single expression by joining them with either and or or:
select
id
from
Project
where
status
is
active
and
name
like
"%thrones"
Use parenthesis to control the precedence when compound criteria are used (by default and takes precedence):
select
id
from
Project
where
status
is
active
and
(
name
like
"%thrones"
or
full_name
like
"%thrones"
)
Filtering on relationships
​
Filtering on relationships is also supported by using a dotted notation:
select
id
from
Task
where
project
.
name
like
"%thrones"
This works even for multiple strides across relationships (though do note that excessive strides can affect performance):
select
id
from
Task
where
project
.
name
like
"%thrones"
and
status
.
type
.
name
is
"Done"
You can also check if a relationship exists using the none keyword:
select
name
from
Project
where
thumbnail is_not none
The same works for collections (where each entity in the collection is compared against the subsequent condition):
select
id
from
Task
where
timelogs
.
start
=
"2016-01-01"
In the above query, each Task that has at least one Timelog with a start time after the start of 2016 is returned.
When filtering on relationships, the conjunctions has and any can be used to specify how the criteria should be applied. This becomes important when querying using multiple conditions. The relationship condition can be written against the following form:
<
not
?
>
<
has
|
any
>
(
)
<
/
has
|
any
>
<
/
not
?
>
has
should be used for scalar relationships. For example, to find notes by a specific author when only name is known:
select
id
from
Note
where
author has
(
first_name
is
"Jane"
and
last_name
is
"Doe"
)
In contrast, if the query was written without has each condition would be tested separately. In that case, notes written by both Jane Smith and John Doe would have been returned in addition to those written by Jane Doe.
any
should be used for collection relationships. For example, to find all projects that have at least one metadata instance that has key=some_key and value=some_value the query would be:
select
id
from
Project
where
metadata
any
(
key
=
some_key
and
value
=
some_value
)
If the query was written without
any
, projects with one metadata matching key and another matching the value would be returned.
any
can also be used to query for empty relationship collections:
User
where
not
timelogs
any
(
)
Supported operators
​
This is the list of currently supported operators:
Operators
Description
Example
=
is
Exactly equal
first_name
=
"jane"
!=
is_not
Not equal
age
!=
30
<
Less than
age
<
25
<=
Less than or equal to
age
<=
30
>
Greater than
age
>
20
>=
Greater than or equal to
age
>=
18
in
Exists in
first_name
in
("jane", "john")
not_in
Does not exist in
first_name
not_in
("jane", "john")
like
Matches pattern
first_name
like
"ja%"
not_like
Does not match pattern
first_name
not_like
"ja%"
has
Test scalar relationship
author
has
(first_name is "Jane" and last_name is "Doe")
any
Test collection relationship
metadata
any
(key=some_key and value=some_value)
Ordering
​
By default, most queries will return entities ordered by their primary key. Often you will want to change this behavior and order by another attribute (such as a date). Ordering takes the form:
order
by
[
direction
]
For example:
select
id
,
name
from
Project
order
by
name
By default, ordering will be ascending. This can be controlled by explicitly specifying direction:
select
id
,
name
from
Project
order
by
name descending
asc
and
desc
are valid aliases for ascending and descending.
Offset & Limit (Paging)
​
A query will return all matching entities unless controlled by specifying offset and limit values using the form:
[
offset
]
[
limit
]
For both cases amount should be an integer greater than or equal to zero:
select
id
from
Project
offset
5
limit
10
Offset and limit may be used independently of each other. Offset defaults to zero and limit to unlimited.
When applying an offset and limit the server will endeavour to return the number of matching entities up to the limit value. However, due to permissions, this may mean that the server scans ahead more than the indicated range. As such the server returns as part of the query result a metadata parameter that contains the nextoffset to use to fetch the next page of results.
For example, consider a request for a limit of 10 results:
Initial query with limit 10 fetches 10 records.
4 records are pruned due to permissions leaving 6 records which is less than the requested limit.
Automatically, another query is made server side for the next page of results.
From the next page the first 3 records are pruned leaving 7.
Adding 7 records to the previous 6 totals 13 exceeding the original limit of 10.
The result is truncated to 10 records and returned.
The metadata will record a next page offset of 18 calculated from 10 (original request) + 3 (skipped in next page) + 4 (used from next page) + 1 (for page start).
warning
It is currently the clients responsibility to use sensible values for offset and limit. This is because we believe the client should understand its environment best and how to control load. However, we may introduce a hard limit on page size on the server at a later date if necessary.
Queries involving relations to subclasses
​
Some relations does not directly reference a specific (concrete) entity type. In programming this called polymorphism and an example of a polymorphic relation is the parent relation on Asset that can be either a Project, a Shot or something else. However, it is in most cases still possible to use attributes from the concrete class.
When selecting projects:
select
parent
.
type
from
Asset
And when filtering:
select
name
from
Shot
where
children
.
type
.
name
is
"Animation"
There are however some limitations that will result in an error:
You may however cast a relation to a concrete type, using the syntax attribute[Class], this allows you to use class specific attributes in your queries.
For example:
select
name
from
Project
where
allocations
.
resource
[
Group
]
.
memberships
any
(
user
.
username
is
"john_doe"
)
An other example:
select
id
from
TypedContext
where
parent
[
Project
]
.
status
is
"hidden"
Filtering with subqueries
​
For complex scenarios where there are no natural relations between entities, it is possible to use subqueries for filtering. A subquery filter is a query inside a filter condition that can be used to narrow down the result.
In this example, we fetch all notes that are posted on a AssetVersion or a related ReviewSessionObject given a version id:
select
id Note
where
parent_id
is
“{version_id}”
or
parent_id
in
(
select
id
from
ReviewSessionObject
where
version_id
is
“{version_id}“
)
