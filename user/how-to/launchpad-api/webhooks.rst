########
Webhooks
########

Some objects in Launchpad support
`webhooks <https://en.wikipedia.org/wiki/Webhook>`__. When these objects
change, Launchpad will send an HTTP POST request to the delivery URL
configured for each webhook with some information about the event that
prompted the notification. You can use this to integrate with all kinds
of external services, and if you control an HTTP server reachable from
the Internet it's easy to write your own webhook endpoint.

Objects and events
------------------

You can create webhooks on any of these target objects:

+-------------------------------------------------------------------------------------------------------+------------------------------------------------+
| Object                                                                                                | Events                                         |
+=======================================================================================================+================================================+
| `Bazaar branch <https://launchpad.net/+apidoc/devel.html#branch>`_                                    | bzr:push:0.1, merge-proposal:0.1               |
+-------------------------------------------------------------------------------------------------------+------------------------------------------------+
| `Git repository <https://launchpad.net/+apidoc/devel.html#git_repository>`_                           | ci:build:0.1, git:push:0.1, merge-proposal:0.1 |
+-------------------------------------------------------------------------------------------------------+------------------------------------------------+
| `Live filesystem <https://launchpad.net/+apidoc/devel.html#livefs>`_                                  | livefs:build:0.1                               |
+-------------------------------------------------------------------------------------------------------+------------------------------------------------+
| `Snap package <https://launchpad.net/+apidoc/devel.html#snap>`_                                       | snap:build:0.1                                 |
+-------------------------------------------------------------------------------------------------------+------------------------------------------------+
| `OCI recipe <https://launchpad.net/+apidoc/devel.html#oci_recipe>`_                                   | ocrecipe:build:0.1                             |
+-------------------------------------------------------------------------------------------------------+------------------------------------------------+
| `Project <https://launchpad.net/+apidoc/devel.html#project>`_                                         | bug:0.1, bug:comment:0.1                       |
+-------------------------------------------------------------------------------------------------------+------------------------------------------------+
| `Distribution <https://launchpad.net/+apidoc/devel.html#distribution>`_                               | bug:0.1, bug:comment:0.1                       |
+-------------------------------------------------------------------------------------------------------+------------------------------------------------+
| `Distribution Source Package <https://launchpad.net/+apidoc/devel.html#distribution_source_package>`_ | bug:0.1, bug:comment:0.1                       |
+-------------------------------------------------------------------------------------------------------+------------------------------------------------+

Events have a type (used in the API) and a name (shown in the web UI).
The types are versioned: if we ever change an event payload in an
incompatible way, we'll bump the version so that you can adapt your code
gracefully. We may add more key/value pairs to dictionaries without
bumping the version.

+-------------------------------------------------------------------------------------+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Event type                                                                          | Event name            | When                                                                                                        |
+=====================================================================================+=======================+=============================================================================================================+
| `bzr:push:0.1 <https://help.launchpad.net/API/Webhooks#bzr-push-0.1>`_              | Bazaar push           | Any time a Bazaar branch is pushed                                                                          |
+-------------------------------------------------------------------------------------+-----------------------+-------------------------------------------------------------------------------------------------------------+
| `ci:build:0.1 <https://help.launchpad.net/API/Webhooks#ci-build-0.1>`_              | CI build              | Any time the status of a CI build changes                                                                   |
+-------------------------------------------------------------------------------------+-----------------------+-------------------------------------------------------------------------------------------------------------+
| `git:push:0.1 <https://help.launchpad.net/API/Webhooks#git-push-0.1>`_              | Git push              | Any time a Git repository is pushed; this includes creating or deleting branches                            |
+-------------------------------------------------------------------------------------+-----------------------+-------------------------------------------------------------------------------------------------------------+
| `livefs:build:0.1 <https://help.launchpad.net/API/Webhooks#livefs-build-0.1>`_      | Live filesystem build | Any time the status of a live filesystem build changes                                                      |
+-------------------------------------------------------------------------------------+-----------------------+-------------------------------------------------------------------------------------------------------------+
| `merge-proposal:0.1 <https://help.launchpad.net/API/Webhooks#merge-proposal-0.1>`_  | Merge proposal        | Any time a merge proposal that has this branch or repository as the target is created, modified, or deleted |
+-------------------------------------------------------------------------------------+-----------------------+-------------------------------------------------------------------------------------------------------------+
| `ping <https://help.launchpad.net/API/Webhooks#ping>`_                              | Ping                  | A test event was requested manually                                                                         |
+-------------------------------------------------------------------------------------+-----------------------+-------------------------------------------------------------------------------------------------------------+
| `snap:build:0.1 <https://help.launchpad.net/API/Webhooks#snap-build-0.1>`_          | Snap build            | Any time the status of a snap package build changes                                                         |
+-------------------------------------------------------------------------------------+-----------------------+-------------------------------------------------------------------------------------------------------------+
| `ocirecipe:build:0.1 <https://help.launchpad.net/API/Webhooks#ocirecipe-build-0.1>`_| OCI recipe build      | Any time the status of an OCI image build changes                                                           |
+-------------------------------------------------------------------------------------+-----------------------+-------------------------------------------------------------------------------------------------------------+
| `bug:0.1 <https://help.launchpad.net/API/Webhooks#bug-0.1>`_                        | Bug                   | When a bug or bug task changes                                                                              |
+-------------------------------------------------------------------------------------+-----------------------+-------------------------------------------------------------------------------------------------------------+
| `bug:comment:0.1 <https://help.launchpad.net/API/Webhooks#bug-comment-0.1>`_        | Bug Comment           | When a comment is added to a bug                                                                            |
+-------------------------------------------------------------------------------------+-----------------------+-------------------------------------------------------------------------------------------------------------+

Creating webhooks
-----------------

You can create new webhooks by visiting a supported object in the
Launchpad web UI and following the "Manage webhooks" link, or by using
the \`newWebhook\` method on one of those objects via the `Launchpad
API <API>`__.

Authentication
--------------

When you create a webhook, you will be asked for a secret. You don't
have to provide one, but if you do, Launchpad will add an
\`X-Hub-Signature\` HTTP header to each webhook delivery containing an
HMAC-SHA1 signature of the body with that secret, as in the
`PubSubHubbub
specification <https://pubsubhubbub.github.io/PubSubHubbub/pubsubhubbub-core-0.4.html#rfc.section.8>`__.

You can't currently change the secret for an existing webhook using the
Launchpad web UI, but you can use the
`setSecret <https://launchpad.net/+apidoc/devel.html#webhook-setSecret>`__
API method to change it. Launchpad will never divulge an existing
webhook secret by any means; this is a write-only property.

Testing
-------

You can use the
`ping <https://launchpad.net/+apidoc/devel.html#webhook-ping>`__ API
method to send a test event:

::

   obj = launchpad.load('/path/to/object')
   webhook = obj.webhooks[0]
   webhook.ping()

Recent deliveries of a webhook are shown on its page in the Launchpad
web UI. They are also available in the \`webhook.deliveries\` API
collection, and you can look at `various attributes of the
delivery <https://launchpad.net/+apidoc/devel.html#webhook_delivery>`__
there.

Delivery ordering
-----------------

Webhooks will generally be delivered in roughly the order in which the
events happened, but (as with any distributed service) you cannot rely
on this. If ordering is important to your application, then you should
sort events by the numeric \`X-Launchpad-Delivery\` header.

Filter Git Repository Webhook deliveries
----------------------------------------

Git Repository Webhooks specifically have an optional
\`git_ref_pattern\` field that can be used to filter which events are
triggered according to the `git
references <https://git-scm.com/book/en/v2/Git-Internals-Git-References>`__
that originated them. This is relevant to all event types related to the
Git Repository: \`ci:build:0.1\` , \`git:push:0.1`,
\`merge-proposal:0.1\` (where for a merge proposal, we match against
both the source and target branches of a merge proposal).

Note: Regarding CI Builds events specifically, Launchpad doesn't re-run
the build if it has run already for a given commit. This could lead to a
scenario where commit A is pushed to a branch whose git reference
doesn't match the \`git_ref_pattern`, the CI Build is triggered and
finishes (webhook is not triggered), the same commit is later pushed to
a branch whose git reference match the \`git_ref_pattern\` but the
webhook is not triggered because there is no change to the CI Build.

Pattern Rules
~~~~~~~~~~~~~

You can use the following wildcards to create your pattern:

+-----------+-----------------------------------+
| Pattern   | Meaning                           |
+===========+===================================+
| \*        | Matches zero or more characters   |
+-----------+-----------------------------------+
| ?         | Matches any single character      |
+-----------+-----------------------------------+
| \[...\]   | Matches any character in \[\]     |
+-----------+-----------------------------------+
| \[\!...\] | Matches any character not in \[\] |
+-----------+-----------------------------------+

Examples
^^^^^^^^

-  \`refs/heads/main\` will match only the \`main\` branch
-  \`*foo*\` will match anything that contains the word \`foo\`
-  \`refs/heads/*\` will match any branch
-  \`refs/heads/foo[-_]bar\` will match both \`refs/heads/foo-bar\` and
   \`refs/heads/foo_bar\`
-  \`refs/heads/foo[!-]*\` will match all git refs that don't have a
   \`-\` character in front of \`refs/heads/foo\`

Network considerations
----------------------

You should ensure that your firewall allows HTTP/HTTPS access (as
appropriate) from all the IP addresses associated with
\`webhooks-proxy.launchpad.net`. If you are testing from the `qastaging
sandbox <https://qastaging.launchpad.net/>`__, you should also allow
\`webhooks-proxy.qastaging.paddev.net`.

The proxy used for delivering webhooks does not generally allow access
to Canonical's own IP space. If you are a Canonical employee and want to
set up a webhook-based integration with another service hosted by
Canonical, please `contact the Launchpad
team <https://answers.launchpad.net/launchpad/+addquestion>`__ with
details.

Event payloads
--------------

All webhook deliveries will have the following HTTP headers:

+------------------------+----------------------------------------------------------------------------------+
| Header name            | Content                                                                          |
+========================+==================================================================================+
| User-Agent             | Begins with launchpad.net-Webhooks/                                              |
+------------------------+----------------------------------------------------------------------------------+
| Content-Type           | application/json                                                                 |
+------------------------+----------------------------------------------------------------------------------+
| X-Launchpad-Event-Type | Event type                                                                       |
+------------------------+----------------------------------------------------------------------------------+
| X-Launchpad-Delivery   | Unique identifier for this delivery                                              |
+------------------------+----------------------------------------------------------------------------------+
| X-Hub-Signature        | HMAC-SHA1 signature of the body with the secret, if configured; otherwise absent |
+------------------------+----------------------------------------------------------------------------------+

The body of the request will be JSON.

Payloads will usually contain the path part of the target object's URL,
referred to as the "url-path" type below. You can use these to find the
object in the Launchpad web UI (prefix "https://launchpad.net") or in
the Launchpad API (for example, you can pass the path directly to
`launchpad.load <API/launchpadlib#Persistent_references_to_Launchpad_objects>`__
without any prefix). We recommend that you use the API if you need more
information about the object than the webhook payload provides, or if
you need to send notifications back to Launchpad (for example, after a
CI job completes).

Bazaar push
~~~~~~~~~~~

Triggered any time a Bazaar branch is pushed. The payload is:

+-------------------+----------+-------------------------------------------------------------------------------------------+
| Key               | Type     | Value                                                                                     |
+===================+==========+===========================================================================================+
| bzr\_branch       | url-path | The branch                                                                                |
+-------------------+----------+-------------------------------------------------------------------------------------------+
| bzr\_branch\_path | string   | A path to the branch; prefix with "lp:" to get a URL that can be used with the bzr client |
+-------------------+----------+-------------------------------------------------------------------------------------------+
| old               | dict     | Branch attributes before this push                                                        |
+-------------------+----------+-------------------------------------------------------------------------------------------+
| new               | dict     | Branch attributes after this push                                                         |
+-------------------+----------+-------------------------------------------------------------------------------------------+

\`old\` and \`new\` are dictionaries of attributes as follows:

+--------------+--------+---------------------+
| Key          | Type   | Value               |
+==============+========+=====================+
| revision\_id | string | The tip revision ID |
+--------------+--------+---------------------+

CI build
~~~~~~~~

Triggered any time the status of a CI build changes. The payload is:

+-----------------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Key             | Type     | Value                                                                                                                                                                                                                                                                            |
+=================+==========+==================================================================================================================================================================================================================================================================================+
| build           | url-path | The CI build                                                                                                                                                                                                                                                                     |
+-----------------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| action          | string   | "created" or "status-changed"                                                                                                                                                                                                                                                    |
+-----------------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| git\_repository | url-path | The repository                                                                                                                                                                                                                                                                   |
+-----------------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| commit\_sha1    | string   | The SHA-1 of the commit being built                                                                                                                                                                                                                                              |
+-----------------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| status          | string   | The current status of the build job: one of "Needs building", "Successfully built", "Failed to build", "Dependency wait", "Chroot problem", "Build for superseded Source", "Currently building", "Failed to upload", "Uploading build", "Cancelling build", or "Cancelled build" |
+-----------------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Git push
~~~~~~~~

Triggered any time a Git repository is pushed; this includes creating or
deleting branches. The payload is:

+-----------------------+----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Key                   | Type     | Value                                                                                                                                                                                     |
+=======================+==========+===========================================================================================================================================================================================+
| git\_repository       | url-path | The repository                                                                                                                                                                            |
+-----------------------+----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| git\_repository\_path | string   | A path to the repository; prefix with "git+ssh://git.launchpad.net/" or "[https://git.launchpad.net/](https://git.launchpad.net/)" to get a URL that can be used with the git client      |
+-----------------------+----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ref\_changes          | dict     | Maps ref names to old and new keys describing the previous and current state of each changed ref, each of which may be either None if the ref is/was absent or a ref description as below |
+-----------------------+----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Ref descriptions are dictionaries of attributes as follows:

+--------------+--------+------------------------------------------------+
| Key          | Type   | Value                                          |
+==============+========+================================================+
| commit\_sha1 | string | The SHA-1 of the commit that the ref points to |
+--------------+--------+------------------------------------------------+

Live filesystem build
~~~~~~~~~~~~~~~~~~~~~

Triggered any time the status of a live filesystem build changes. The
payload is:

+---------------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Key           | Type     | Value                                                                                                                                                                                                                                                                            |
+===============+==========+==================================================================================================================================================================================================================================================================================+
| livefs\_build | url-path | The live filesystem build                                                                                                                                                                                                                                                        |
+---------------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| action        | string   | "status-changed"                                                                                                                                                                                                                                                                 |
+---------------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| livefs        | url-path | The live filesystem                                                                                                                                                                                                                                                              |
+---------------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| status        | string   | The current status of the build job: one of "Needs building", "Successfully built", "Failed to build", "Dependency wait", "Chroot problem", "Build for superseded Source", "Currently building", "Failed to upload", "Uploading build", "Cancelling build", or "Cancelled build" |
+---------------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Merge proposal
~~~~~~~~~~~~~~

Triggered any time a merge proposal that has the target branch or
repository as the target is created, modified, or deleted. The payload
is:

+-----------------+----------+-------------------------------------------------------------------------------------------------------+
| Key             | Type     | Value                                                                                                 |
+=================+==========+=======================================================================================================+
| merge\_proposal | url-path | The merge proposal                                                                                    |
+-----------------+----------+-------------------------------------------------------------------------------------------------------+
| action          | string   | "created", "modified", or "deleted"                                                                   |
+-----------------+----------+-------------------------------------------------------------------------------------------------------+
| old             | dict     | Absent if action is "created"; otherwise, a dictionary of merge proposal attributes before this event |
+-----------------+----------+-------------------------------------------------------------------------------------------------------+
| new             | dict     | Absent if action is "deleted"; otherwise, a dictionary of merge proposal attributes after this event  |
+-----------------+----------+-------------------------------------------------------------------------------------------------------+

Merge proposal attributes are as follows:

+-------------------------------+----------+---------------------------------------------------------------------------------------------------------------------------------+
| Key                           | Type     | Value                                                                                                                           |
+===============================+==========+=================================================================================================================================+
| registrant                    | url-path | The person who registered the merge proposal                                                                                    |
+-------------------------------+----------+---------------------------------------------------------------------------------------------------------------------------------+
| source\_branch                | url-path | The Bazaar branch that has code to land                                                                                         |
+-------------------------------+----------+---------------------------------------------------------------------------------------------------------------------------------+
| source\_git\_repository       | url-path | The Git repository that has code to land                                                                                        |
+-------------------------------+----------+---------------------------------------------------------------------------------------------------------------------------------+
| source\_git\_path             | string   | Ref path of the Git branch that has code to land                                                                                |
+-------------------------------+----------+---------------------------------------------------------------------------------------------------------------------------------+
| target\_branch                | url-path | The Bazaar branch that the source branch will be merged into                                                                    |
+-------------------------------+----------+---------------------------------------------------------------------------------------------------------------------------------+
| target\_git\_repository       | url-path | The Git repository that the source branch will be merged into                                                                   |
+-------------------------------+----------+---------------------------------------------------------------------------------------------------------------------------------+
| target\_git\_path             | string   | Ref path of the Git branch that the source branch will be merged into                                                           |
+-------------------------------+----------+---------------------------------------------------------------------------------------------------------------------------------+
| prerequisite\_branch          | url-path | The Bazaar branch that the source branch branched from                                                                          |
+-------------------------------+----------+---------------------------------------------------------------------------------------------------------------------------------+
| prerequisite\_git\_repository | url-path | The Git repository containing the branch that the source branch branched from                                                   |
+-------------------------------+----------+---------------------------------------------------------------------------------------------------------------------------------+
| prerequisite\_git\_path       | string   | The path of the Git branch that the source branch branched from                                                                 |
+-------------------------------+----------+---------------------------------------------------------------------------------------------------------------------------------+
| queue\_status                 | string   | The current state of the proposal: one of "Work in progress", "Needs review", "Approved", "Rejected", "Merged", or "Superseded" |
+-------------------------------+----------+---------------------------------------------------------------------------------------------------------------------------------+
| commit\_message               | string   | The commit message that should be used when merging the source branch                                                           |
+-------------------------------+----------+---------------------------------------------------------------------------------------------------------------------------------+
| whiteboard                    | string   | Notes about the merge                                                                                                           |
+-------------------------------+----------+---------------------------------------------------------------------------------------------------------------------------------+
| description                   | string   | A detailed description of the changes that are being addressed by the branch being proposed to be merged                        |
+-------------------------------+----------+---------------------------------------------------------------------------------------------------------------------------------+
| preview\_diff                 | url-path | The current diff of the source branch against the target branch                                                                 |
+-------------------------------+----------+---------------------------------------------------------------------------------------------------------------------------------+

Ping
~~~~

A test event was `requested manually <#Testing>`__. The payload is:

+------+---------+-------+
| Key  | Type    | Value |
+======+=========+=======+
| ping | boolean | true  |
+------+---------+-------+

Snap build
~~~~~~~~~~

Triggered any time the status of a snap package build changes. The
payload is:

+-----------------------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Key                   | Type     | Value                                                                                                                                                                                                                                                                            |
+=======================+==========+==================================================================================================================================================================================================================================================================================+
| snap\_build           | url-path | The snap build                                                                                                                                                                                                                                                                   |
+-----------------------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| action                | string   | "status-changed"                                                                                                                                                                                                                                                                 |
+-----------------------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| snap                  | url-path | The snap package                                                                                                                                                                                                                                                                 |
+-----------------------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| build\_request        | url-path | The associated snap build request, if any                                                                                                                                                                                                                                        |
+-----------------------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| status                | string   | The current status of the build job: one of "Needs building", "Successfully built", "Failed to build", "Dependency wait", "Chroot problem", "Build for superseded Source", "Currently building", "Failed to upload", "Uploading build", "Cancelling build", or "Cancelled build" |
+-----------------------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| store\_upload\_status | string   | The current status of uploading this build to the store: one of "Unscheduled", "Pending", "Failed to upload", "Failed to release to channels", or "Uploaded"                                                                                                                     |
+-----------------------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

OCI recipe build
~~~~~~~~~~~~~~~~

+--------------------------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Key                      | Type     | Value                                                                                                                                                                                                                                                                            |
+==========================+==========+==================================================================================================================================================================================================================================================================================+
| ocirecipe\_build         | url-path | The OCI recipe build                                                                                                                                                                                                                                                             |
+--------------------------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| action                   | string   | "status-changed"                                                                                                                                                                                                                                                                 |
+--------------------------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ocirecipe                | url-path | The OCI recipe                                                                                                                                                                                                                                                                   |
+--------------------------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| build\_request           | url-path | The associated OCI recipe build request, if any                                                                                                                                                                                                                                  |
+--------------------------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| status                   | string   | The current status of the build job: one of "Needs building", "Successfully built", "Failed to build", "Dependency wait", "Chroot problem", "Build for superseded Source", "Currently building", "Failed to upload", "Uploading build", "Cancelling build", or "Cancelled build" |
+--------------------------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| registry\_upload\_status | string   | The current status of uploading this image to the registry: one of "Unscheduled", "Pending", "Failed to upload", or "Uploaded"                                                                                                                                                   |
+--------------------------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Bug created/updated
~~~~~~~~~~~~~~~~~~~

Triggered any time a Bug or Bug Task is created or updated. Both
creating a new bug and targeting an existing bug to a new project will
trigger the new event. The payload is:

+--------+----------+------------------------------------------------------------------------------------------+
| Key    | Type     | Value                                                                                    |
+========+==========+==========================================================================================+
| action | string   | What happened to the bug: "created" or "\<field\>-changed"                               |
+--------+----------+------------------------------------------------------------------------------------------+
| target | url-path | A path to the bug target (can be a product, distribution or distribution source package) |
+--------+----------+------------------------------------------------------------------------------------------+
| bug    | url-path | A path to the bug                                                                        |
+--------+----------+------------------------------------------------------------------------------------------+
| old    | dict     | Bug attributes before the update                                                         |
+--------+----------+------------------------------------------------------------------------------------------+
| new    | dict     | Bug attributes after the update                                                          |
+--------+----------+------------------------------------------------------------------------------------------+

\`old\` and \`new\` are dictionaries of attributes as follows:

+---------------+----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Key           | Type           | Value                                                                                                                                                        |
+===============+================+==============================================================================================================================================================+
| title         | string         | Title of the bug                                                                                                                                             |
+---------------+----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| description   | string         | Description of the bug                                                                                                                                       |
+---------------+----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| reported      | string         | A path to the user that reported the bug                                                                                                                     |
+---------------+----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| status        | string         | Status of the bug task for the given target                                                                                                                  |
+---------------+----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| importance    | string         | Importance of the bug task for the given target                                                                                                              |
+---------------+----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| assignee      | string         | A path to the user responsible for the bug task for the given target                                                                                         |
+---------------+----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| tags          | list\[string\] | List of tags added to the bug                                                                                                                                |
+---------------+----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| date\_created | string         | Date of creation of the bug for the given target (if a new target was added to an existing bug, this is the date the bug was targeted into the given target) |
+---------------+----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+

Note that if a bug with multiple targets is updated, assuming all
targets have bug webhooks set up, the system will trigger one webhook
per target, and their payloads will be different from each other in the
fields specific to the target (`status`, \`importance`, \`assignee\` and
\`date_created`).

Bug comment created
~~~~~~~~~~~~~~~~~~~

Triggered any time a new comment is added to a bug. The payload is:

+--------------+----------+------------------------------------------------------------------------------------------+
| Key          | Type     | Value                                                                                    |
+==============+==========+==========================================================================================+
| action       | string   | What happened to the bug: "created" or "\<field\>-changed"                               |
+--------------+----------+------------------------------------------------------------------------------------------+
| target       | url-path | A path to the bug target (can be a product, distribution or distribution source package) |
+--------------+----------+------------------------------------------------------------------------------------------+
| bug          | url-path | A path to the bug                                                                        |
+--------------+----------+------------------------------------------------------------------------------------------+
| bug\_comment | url-path | A path to the bug comment                                                                |
+--------------+----------+------------------------------------------------------------------------------------------+
| old          | dict     | Comment attributes before the update                                                     |
+--------------+----------+------------------------------------------------------------------------------------------+
| new          | dict     | Comment attributes after the update                                                      |
+--------------+----------+------------------------------------------------------------------------------------------+

\`old\` and \`new\` are dictionaries of attributes as follows:

+-----------+--------+-----------------------------------+
| Key       | Type   | Value                             |
+===========+========+===================================+
| commenter | string | A path to the user that commented |
+-----------+--------+-----------------------------------+
| content   | string | Comment message                   |
+-----------+--------+-----------------------------------+

