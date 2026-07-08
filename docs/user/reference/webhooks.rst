.. meta::
   :description: Set up webhooks in Launchpad to receive real-time HTTP 
      notifications.

.. _webhooks:

Webhooks
########

Some objects in Launchpad support
`webhooks <https://en.wikipedia.org/wiki/Webhook>`__. When these objects
change, Launchpad will send an HTTP POST request to the delivery URL
configured for each webhook with some information about the event that
prompted the notification. You can use this to integrate with different
external services. If you control an HTTP server reachable from the
Internet, it's easy to write your own webhook endpoint.

Objects and events
------------------

You can create webhooks on any of these target objects, grouped here by
the kind of activity they notify you about:

+-------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------+
| Object                                                                                                | Events                                                                 |
+=======================================================================================================+========================================================================+
| **Code hosting**                                                                                                                                                               |
+-------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------+
| `Git repository <https://launchpad.net/+apidoc/devel.html#git_repository>`_                           | ci:build:0.1, git:push:0.1, merge-proposal:0.1                         |
+-------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------+
| **Build recipes**                                                                                                                                                              |
+-------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------+
| `Live filesystem <https://launchpad.net/+apidoc/devel.html#livefs>`_                                  | livefs:build:0.1                                                       |
+-------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------+
| `Snap package <https://launchpad.net/+apidoc/devel.html#snap>`_                                       | snap:build:0.1                                                         |
+-------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------+
| `OCI recipe <https://launchpad.net/+apidoc/devel.html#oci_recipe>`_                                   | ocirecipe:build:0.1                                                    |
+-------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------+
| `Charm recipe <https://launchpad.net/+apidoc/devel.html#charm_recipe>`_                               | charm-recipe:build:0.1                                                 |
+-------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------+
| `Craft recipe <https://launchpad.net/+apidoc/devel.html#craft_recipe>`_                               | craft-recipe:build:0.1                                                 |
+-------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------+
| **Bug tracking**                                                                                                                                                               |
+-------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------+
| `Project <https://launchpad.net/+apidoc/devel.html#project>`_                                         | bug:0.1, bug:comment:0.1                                               |
+-------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------+
| `Distribution <https://launchpad.net/+apidoc/devel.html#distribution>`_                               | bug:0.1, bug:comment:0.1                                               |
+-------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------+
| `Distribution Source Package <https://launchpad.net/+apidoc/devel.html#distribution_source_package>`_ | bug:0.1, bug:comment:0.1                                               |
+-------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------+
| **Package publishing**                                                                                                                                                         |
+-------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------+
| `Archive <https://launchpad.net/+apidoc/devel.html#archive>`_                                         | source-package-upload:0.1, binary-package-upload:0.1, binary-build:0.1 |
+-------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------+

Events have a type (used in the API) and a name (shown in the web UI).
The types are versioned. If an event payload is ever changed in an
incompatible way, the version will be bumped so that you can adapt your
code gracefully. More key/value pairs may be added to dictionaries without
bumping the version. Events are grouped below by the kind of activity
they relate to.

+-----------------------------------------------------------------+-----------------------+-----------------------------------------------------------------------------------------------------------+
| Event type                                                      | Event name            | Triggers                                                                                                  |
+=================================================================+=======================+===========================================================================================================+
| **Code hosting**                                                                                                                                                                                    |
+-----------------------------------------------------------------+-----------------------+-----------------------------------------------------------------------------------------------------------+
| :ref:`ci:build:0.1 <ci-build>`                                  | CI build              | When the status of a CI build changes                                                                     |
+-----------------------------------------------------------------+-----------------------+-----------------------------------------------------------------------------------------------------------+
| :ref:`git:push:0.1 <git-push>`                                  | Git push              | When a Git repository is pushed; this includes creating or deleting branches                              |
+-----------------------------------------------------------------+-----------------------+-----------------------------------------------------------------------------------------------------------+
| :ref:`merge-proposal:0.1 <merge-proposal>`                      | Merge proposal        | When a merge proposal that has this branch or repository as the target is created, modified, or deleted   |
+-----------------------------------------------------------------+-----------------------+-----------------------------------------------------------------------------------------------------------+
| **Build recipes**                                                                                                                                                                                   |
+-----------------------------------------------------------------+-----------------------+-----------------------------------------------------------------------------------------------------------+
| :ref:`livefs:build:0.1 <live-filesystem-build>`                 | Live filesystem build | When the status of a live filesystem build changes                                                        |
+-----------------------------------------------------------------+-----------------------+-----------------------------------------------------------------------------------------------------------+
| :ref:`snap:build:0.1 <snap-build>`                              | Snap build            | When the status of a snap package build changes                                                           |
+-----------------------------------------------------------------+-----------------------+-----------------------------------------------------------------------------------------------------------+
| :ref:`ocirecipe:build:0.1 <oci-recipe-build>`                   | OCI recipe build      | When the status of an OCI image build changes                                                             |
+-----------------------------------------------------------------+-----------------------+-----------------------------------------------------------------------------------------------------------+
| :ref:`charm-recipe:build:0.1 <charm-recipe-build>`              | Charm recipe build    | When the status of a charm recipe build changes                                                           |
+-----------------------------------------------------------------+-----------------------+-----------------------------------------------------------------------------------------------------------+
| :ref:`craft-recipe:build:0.1 <craft-recipe-build>`              | Craft recipe build    | When the status of a craft recipe build changes                                                           |
+-----------------------------------------------------------------+-----------------------+-----------------------------------------------------------------------------------------------------------+
| **Bug tracking**                                                                                                                                                                                    |
+-----------------------------------------------------------------+-----------------------+-----------------------------------------------------------------------------------------------------------+
| :ref:`bug:0.1 <bug-created-updated>`                            | Bug                   | When a bug or bug task changes                                                                            |
+-----------------------------------------------------------------+-----------------------+-----------------------------------------------------------------------------------------------------------+
| :ref:`bug:comment:0.1 <bug-comment-created>`                    | Bug Comment           | When a comment is added to a bug                                                                          |
+-----------------------------------------------------------------+-----------------------+-----------------------------------------------------------------------------------------------------------+
| **Package publishing**                                                                                                                                                                              |
+-----------------------------------------------------------------+-----------------------+-----------------------------------------------------------------------------------------------------------+
| :ref:`archive:source-package-upload:0.1 <source-package-upload>`| Source package upload | When the status of a source package upload changes                                                        |
+-----------------------------------------------------------------+-----------------------+-----------------------------------------------------------------------------------------------------------+
| :ref:`archive:binary-package-upload:0.1 <binary-package-upload>`| Binary package upload | When the status of a binary package upload changes                                                        |
+-----------------------------------------------------------------+-----------------------+-----------------------------------------------------------------------------------------------------------+
| :ref:`archive:binary-build:0.1 <binary-build>`                  | Binary build          | When the status of a binary build changes                                                                 |
+-----------------------------------------------------------------+-----------------------+-----------------------------------------------------------------------------------------------------------+
| **Testing**                                                                                                                                                                                         |
+-----------------------------------------------------------------+-----------------------+-----------------------------------------------------------------------------------------------------------+
| :ref:`ping <id3>`                                               | Ping                  | When a test event is requested manually                                                                   |
+-----------------------------------------------------------------+-----------------------+-----------------------------------------------------------------------------------------------------------+

Sub-event types
~~~~~~~~~~~~~~~

Some events have sub-event types that allow users to filter more specifically
which events they want to receive. A webhook with a sub-event type will only
be triggered by a more specific event, but will have the same payload as the
parent event. When selecting event types for a webhook, you can choose either
the parent event type or specific sub-event types, but not both.

For example, a ``merge-proposal:0.1`` event has sub-event types:

- ``merge-proposal:0.1::create`` - triggered when a merge proposal is created
- ``merge-proposal:0.1::push`` - triggered when a new commit is pushed to the
  source branch of a merge proposal
- ``merge-proposal:0.1::review`` - triggered when a merge proposal is reviewed
- ``merge-proposal:0.1::edit`` - triggered when a merge proposal is edited
- ``merge-proposal:0.1::status-change`` - triggered when the status changes
- ``merge-proposal:0.1::delete`` - triggered when a merge proposal is deleted

If a webhook is subscribed to `merge-proposal:0.1`, it will be triggered by all
of the above events.
If a webhook is subscribed to `merge-proposal:0.1::create`, it will only be
triggered when a merge proposal is created.


Creating webhooks
-----------------

You can create new webhooks by visiting a supported object in the
Launchpad web UI and following the "Manage webhooks" link, or by using
the ``newWebhook`` method on one of those objects via the 
:ref:`Launchpad API <launchpad-api>`.

Authentication
--------------

When you create a webhook, you can optionally add a secret. If you do,
Launchpad will add an ``X-Hub-Signature`` HTTP header to each webhook delivery
containing an HMAC-SHA1 signature of the body with that secret, as in the
`PubSubHubbub specification <https://pubsubhubbub.github.io/PubSubHubbub/pubsubhubbub-core-0.4.html#rfc.section.8>`_.

You can't currently change the secret for an existing webhook using the
Launchpad web UI, but you can use the
`setSecret <https://launchpad.net/+apidoc/devel.html#webhook-setSecret>`_
API method to change it. Launchpad will never divulge an existing
webhook secret by any means; this is a write-only property.

.. _testing:

Testing
-------

You can use the
`ping <https://launchpad.net/+apidoc/devel.html#webhook-ping>`__ API
method to send a test event. The examples on this page use the
:ref:`lp-shell tool <how-to-use-lp-shell>`, where ``lp`` is a
pre-authenticated Launchpad API object::

   obj = lp.load('/path/to/object')
   webhook = obj.webhooks[0]
   webhook.ping()

Launchpad then delivers a POST to your endpoint with the
``X-Launchpad-Event-Type: ping`` header and the body ``{"ping": true}``, and
records it under the webhook's recent deliveries so you can confirm your
endpoint is reachable and your signature verification works.

Deliveries
----------

Recent deliveries of a webhook are shown on its page in the Launchpad
web UI. Alternatively, you can query the ``webhook.deliveries`` API collection
to review `specific delivery details and attributes <https://launchpad.net/+apidoc/devel.html#webhook_delivery>`_.

Delivery ordering
~~~~~~~~~~~~~~~~~

Webhooks will generally be delivered in roughly the order in which the
events happened, but (as with any distributed service) you cannot rely
on this. If ordering is important to your application, then you should
sort events by the numeric ``X-Launchpad-Delivery`` header.

Filter Git repository webhook deliveries
----------------------------------------

Git Repository Webhooks have an optional ``git_ref_pattern`` field that
can be used to filter which events are triggered according to the `git
references <https://git-scm.com/book/en/v2/Git-Internals-Git-References>`_
that originated them. This is relevant to all event types related to the
Git Repository: ``ci:build:0.1`` , ``git:push:0.1``,
``merge-proposal:0.1`` (where for a merge proposal, we match against
both the source and target branches of a merge proposal).

.. note::

   Regarding CI Build events, specifically, Launchpad doesn't re-run
   the build if it has run already for a given commit. This could lead to a
   scenario where commit A is pushed to a branch whose git reference
   doesn't match the ``git_ref_pattern``, the CI Build is triggered and
   finishes (webhook is not triggered), the same commit is later pushed to
   a branch whose git reference match the ``git_ref_pattern`` but the
   webhook is not triggered because there is no change to the CI Build.

Pattern rules for Git repositories
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can use the following wildcards to create your pattern:

+---------------+-------------------------------------+
| Pattern       | Meaning                             |
+===============+=====================================+
| ``\*``        | Matches zero or more characters     |
+---------------+-------------------------------------+
| ``?``         | Matches any single character        |
+---------------+-------------------------------------+
| ``\[...\]``   | Matches any character in ``[]``     |
+---------------+-------------------------------------+
| ``\[\!...\]`` | Matches any character not in ``[]`` |
+---------------+-------------------------------------+

Examples
^^^^^^^^

- ``refs/heads/main`` will match only the ``main`` branch
- ``*foo*`` will match anything that contains the word ``foo``
- ``refs/heads/*`` will match any branch
- ``refs/heads/foo[-_]bar`` will match both ``refs/heads/foo-bar`` and
  ``refs/heads/foo_bar``
- ``refs/heads/foo[!-]*`` will match all git refs that don't have a ``-``
  character after ``refs/heads/foo``

Network considerations
----------------------

You should ensure that your firewall allows HTTP/HTTPS access (as
appropriate) from all the IP addresses associated with
``webhooks-proxy.launchpad.net``. If you are testing from `qastaging
<https://qastaging.launchpad.net/>`_, you should also allow
``webhooks-proxy.qastaging.paddev.net``.

The proxy used for delivering webhooks does not generally allow access to
Canonical's own IP space. If you are a Canonical employee and want to set
up a webhook-based integration with another service hosted by Canonical,
please contact the Launchpad team with the details.

Event payloads
--------------

All webhook deliveries will have the following HTTP headers:

+----------------------------+----------------------------------------------------------------------------------+
| Header name                | Content                                                                          |
+============================+==================================================================================+
| ``User-Agent``             | Begins with launchpad.net-Webhooks/                                              |
+----------------------------+----------------------------------------------------------------------------------+
| ``Content-Type``           | application/json                                                                 |
+----------------------------+----------------------------------------------------------------------------------+
| ``X-Launchpad-Event-Type`` | Event type, including version (for example, ``git:push:0.1``)                    |
+----------------------------+----------------------------------------------------------------------------------+
| ``X-Launchpad-Delivery``   | Unique identifier for this delivery                                              |
+----------------------------+----------------------------------------------------------------------------------+
| ``X-Hub-Signature``        | HMAC-SHA1 signature of the body with the secret, if configured; otherwise absent |
+----------------------------+----------------------------------------------------------------------------------+

The body of the request will be JSON.

Many payload fields contain only the path part of an object's URL rather
than a full URL. These are marked as the "url-path" type in the tables
below. You can use such a path in two ways:

- To open the object in the Launchpad web UI, prepend
  ``https://launchpad.net`` to the path.
- To fetch the object from the Launchpad API, pass the path directly to
  ``lp.load`` in the :ref:`lp-shell tool <how-to-use-lp-shell>`
  - no prefix is needed.

We recommend using the API when you need more information about an object
than the payload provides, or when you need to send data back to Launchpad
(for example, after a CI job completes).

.. _ci-build:

CI build
~~~~~~~~

Triggered any time the status of a CI build changes. The payload is:

+--------------------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Key                | Type     | Value                                                                                                                                                                                                                                                                            |
+====================+==========+==================================================================================================================================================================================================================================================================================+
| ``build``          | url-path | The CI build                                                                                                                                                                                                                                                                     |
+--------------------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``action``         | string   | "created" or "status-changed"                                                                                                                                                                                                                                                    |
+--------------------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``git_repository`` | url-path | The repository                                                                                                                                                                                                                                                                   |
+--------------------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``commit_sha1``    | string   | The SHA-1 of the commit being built                                                                                                                                                                                                                                              |
+--------------------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| status             | string   | The current status of the build job: one of "Needs building", "Successfully built", "Failed to build", "Dependency wait", "Chroot problem", "Build for superseded Source", "Currently building", "Failed to upload", "Uploading build", "Cancelling build", or "Cancelled build" |
+--------------------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _git-push:

Git push
~~~~~~~~

Triggered any time a Git repository is pushed; this includes creating or
deleting branches. The payload is:

+-------------------------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Key                     | Type     | Value                                                                                                                                                                                                                                                                                          |
+=========================+==========+================================================================================================================================================================================================================================================================================================+
| ``git_repository``      | url-path | The repository                                                                                                                                                                                                                                                                                 |
+-------------------------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``git_repository_path`` | string   | A path to the repository; prefix with ``git+ssh://git.launchpad.net/`` or `<https://git.launchpad.net/>`_ to get a URL that can be used with the git client                                                                                                                                    |
+-------------------------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``ref_changes``         | dict     | Maps each changed ref name to an object with ``old`` and ``new`` keys giving the ref's state before and after the push. Either key is ``null`` when the ref was absent then (``old: null`` for a newly created ref, ``new: null`` for a deleted one); otherwise it's a ref description (below) |
+-------------------------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

A ref (short for "reference") is a named pointer to a commit, such as a
branch (``refs/heads/main``) or a tag (``refs/tags/v1.0``). Each ``old``
or ``new`` value above is a *ref description*: a dictionary describing
where a ref pointed at that moment. It has the following attributes:

+-----------------+--------+------------------------------------------------+
| Key             | Type   | Value                                          |
+=================+========+================================================+
| ``commit_sha1`` | string | The SHA-1 of the commit that the ref points to |
+-----------------+--------+------------------------------------------------+

.. _live-filesystem-build:

Live filesystem build
~~~~~~~~~~~~~~~~~~~~~

Triggered any time the status of a live filesystem build changes. The
payload is:

+------------------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Key              | Type     | Value                                                                                                                                                                                                                                                                            |
+==================+==========+==================================================================================================================================================================================================================================================================================+
| ``livefs_build`` | url-path | The live filesystem build                                                                                                                                                                                                                                                        |
+------------------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``action``       | string   | "status-changed"                                                                                                                                                                                                                                                                 |
+------------------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``livefs``       | url-path | The live filesystem                                                                                                                                                                                                                                                              |
+------------------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``status``       | string   | The current status of the build job: one of "Needs building", "Successfully built", "Failed to build", "Dependency wait", "Chroot problem", "Build for superseded Source", "Currently building", "Failed to upload", "Uploading build", "Cancelling build", or "Cancelled build" |
+------------------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _merge-proposal:

Merge proposal
~~~~~~~~~~~~~~

Triggered any time a merge proposal that has the target branch or
repository as the target is created, modified, or deleted. The payload
is:

+--------------------+----------+-------------------------------------------------------------------------------------------------------+
| Key                | Type     | Value                                                                                                 |
+====================+==========+=======================================================================================================+
| ``merge_proposal`` | url-path | The merge proposal                                                                                    |
+--------------------+----------+-------------------------------------------------------------------------------------------------------+
| ``action``         | string   | "created", "modified", or "deleted"                                                                   |
+--------------------+----------+-------------------------------------------------------------------------------------------------------+
| ``old``            | dict     | Absent if action is "created"; otherwise, a dictionary of merge proposal attributes before this event |
+--------------------+----------+-------------------------------------------------------------------------------------------------------+
| ``new``            | dict     | Absent if action is "deleted"; otherwise, a dictionary of merge proposal attributes after this event  |
+--------------------+----------+-------------------------------------------------------------------------------------------------------+

Merge proposal attributes are as follows:

+---------------------------------+----------+---------------------------------------------------------------------------------------------------------------------------------+
| Key                             | Type     | Value                                                                                                                           |
+=================================+==========+=================================================================================================================================+
| ``registrant``                  | url-path | The person who registered the merge proposal                                                                                    |
+---------------------------------+----------+---------------------------------------------------------------------------------------------------------------------------------+
| ``source_git_repository``       | url-path | The Git repository that has code to land                                                                                        |
+---------------------------------+----------+---------------------------------------------------------------------------------------------------------------------------------+
| ``source_git_path``             | string   | Ref path of the Git branch that has code to land                                                                                |
+---------------------------------+----------+---------------------------------------------------------------------------------------------------------------------------------+
| ``target_git_repository``       | url-path | The Git repository that the source branch will be merged into                                                                   |
+---------------------------------+----------+---------------------------------------------------------------------------------------------------------------------------------+
| ``target_git_path``             | string   | Ref path of the Git branch that the source branch will be merged into                                                           |
+---------------------------------+----------+---------------------------------------------------------------------------------------------------------------------------------+
| ``prerequisite_git_repository`` | url-path | The Git repository containing the branch that the source branch branched from                                                   |
+---------------------------------+----------+---------------------------------------------------------------------------------------------------------------------------------+
| ``prerequisite_git_path``       | string   | The path of the Git branch that the source branch branched from                                                                 |
+---------------------------------+----------+---------------------------------------------------------------------------------------------------------------------------------+
| ``queue_status``                | string   | The current state of the proposal: one of "Work in progress", "Needs review", "Approved", "Rejected", "Merged", or "Superseded" |
+---------------------------------+----------+---------------------------------------------------------------------------------------------------------------------------------+
| ``commit_message``              | string   | The commit message that should be used when merging the source branch                                                           |
+---------------------------------+----------+---------------------------------------------------------------------------------------------------------------------------------+
| ``whiteboard``                  | string   | Notes about the merge                                                                                                           |
+---------------------------------+----------+---------------------------------------------------------------------------------------------------------------------------------+
| ``description``                 | string   | A detailed description of the changes that are being addressed by the branch being proposed to be merged                        |
+---------------------------------+----------+---------------------------------------------------------------------------------------------------------------------------------+
| ``preview_diff``                | url-path | The current diff of the source branch against the target branch                                                                 |
+---------------------------------+----------+---------------------------------------------------------------------------------------------------------------------------------+

.. _id3:

Ping
~~~~

A test event was :ref:`requested manually <testing>`. The payload is:

+------+---------+-------+
| Key  | Type    | Value |
+======+=========+=======+
| ping | boolean | true  |
+------+---------+-------+

.. _snap-build:

Snap build
~~~~~~~~~~

Triggered any time the status of a snap package build changes. The
payload is:

+-------------------------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Key                     | Type     | Value                                                                                                                                                                                                                                                                            |
+=========================+==========+==================================================================================================================================================================================================================================================================================+
| ``snap_build``          | url-path | The snap build                                                                                                                                                                                                                                                                   |
+-------------------------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``action``              | string   | "created" or "status-changed"                                                                                                                                                                                                                                                    |
+-------------------------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``snap``                | url-path | The snap package                                                                                                                                                                                                                                                                 |
+-------------------------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``build_request``       | url-path | The associated snap build request, if any                                                                                                                                                                                                                                        |
+-------------------------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``status``              | string   | The current status of the build job: one of "Needs building", "Successfully built", "Failed to build", "Dependency wait", "Chroot problem", "Build for superseded Source", "Currently building", "Failed to upload", "Uploading build", "Cancelling build", or "Cancelled build" |
+-------------------------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``store_upload_status`` | string   | The current status of uploading this build to the store: one of "Unscheduled", "Pending", "Failed to upload", "Failed to release to channels", or "Uploaded"                                                                                                                     |
+-------------------------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _oci-recipe-build:

OCI recipe build
~~~~~~~~~~~~~~~~

Triggered any time the status of an OCI recipe build changes. The
payload is:

+----------------------------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Key                        | Type     | Value                                                                                                                                                                                                                                                                            |
+============================+==========+==================================================================================================================================================================================================================================================================================+
| ``ocirecipe_build``        | url-path | The OCI recipe build                                                                                                                                                                                                                                                             |
+----------------------------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``action``                 | string   | "created" or "status-changed"                                                                                                                                                                                                                                                    |
+----------------------------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``ocirecipe``              | url-path | The OCI recipe                                                                                                                                                                                                                                                                   |
+----------------------------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``build_request``          | url-path | The associated OCI recipe build request, if any                                                                                                                                                                                                                                  |
+----------------------------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``status``                 | string   | The current status of the build job: one of "Needs building", "Successfully built", "Failed to build", "Dependency wait", "Chroot problem", "Build for superseded Source", "Currently building", "Failed to upload", "Uploading build", "Cancelling build", or "Cancelled build" |
+----------------------------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``registry_upload_status`` | string   | The current status of uploading this image to the registry: one of "Unscheduled", "Pending", "Failed to upload", or "Uploaded"                                                                                                                                                   |
+----------------------------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _charm-recipe-build:

Charm recipe build
~~~~~~~~~~~~~~~~~~

Triggered any time the status of a charm recipe build changes. The
payload is:

+----------------------------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Key                        | Type     | Value                                                                                                                                                                                                                                                                            |
+============================+==========+==================================================================================================================================================================================================================================================================================+
| ``recipe_build``           | url-path | The charm recipe build                                                                                                                                                                                                                                                           |
+----------------------------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``action``                 | string   | "created" or "status-changed"                                                                                                                                                                                                                                                    |
+----------------------------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``recipe``                 | url-path | The charm recipe                                                                                                                                                                                                                                                                 |
+----------------------------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``build_request``          | url-path | The associated charm recipe build request, if any                                                                                                                                                                                                                                |
+----------------------------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``status``                 | string   | The current status of the build job: one of "Needs building", "Successfully built", "Failed to build", "Dependency wait", "Chroot problem", "Build for superseded Source", "Currently building", "Failed to upload", "Uploading build", "Cancelling build", or "Cancelled build" |
+----------------------------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``store_upload_status``    | string   | The current status of uploading this build to the store: one of "Unscheduled", "Pending", "Failed to upload", "Failed to release to channels", or "Uploaded"                                                                                                                     |
+----------------------------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _craft-recipe-build:

Craft recipe build
~~~~~~~~~~~~~~~~~~

Triggered any time the status of a craft recipe build changes. The
payload is:

+----------------------------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Key                        | Type     | Value                                                                                                                                                                                                                                                                            |
+============================+==========+==================================================================================================================================================================================================================================================================================+
| ``craft_build``            | url-path | The craft recipe build                                                                                                                                                                                                                                                           |
+----------------------------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``action``                 | string   | "status-changed"                                                                                                                                                                                                                                                                 |
+----------------------------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``recipe``                 | url-path | The craft recipe                                                                                                                                                                                                                                                                 |
+----------------------------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``build_request``          | url-path | The associated craft recipe build request, if any                                                                                                                                                                                                                                |
+----------------------------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``status``                 | string   | The current status of the build job: one of "Needs building", "Successfully built", "Failed to build", "Dependency wait", "Chroot problem", "Build for superseded Source", "Currently building", "Failed to upload", "Uploading build", "Cancelling build", or "Cancelled build" |
+----------------------------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _bug-created-updated:

Bug created/updated
~~~~~~~~~~~~~~~~~~~

Triggered any time a Bug or Bug Task is created or updated. Both
creating a new bug and targeting an existing bug to a new project will
trigger the new event. The payload is:

+------------+----------+------------------------------------------------------------------------------------------+
| Key        | Type     | Value                                                                                    |
+============+==========+==========================================================================================+
| ``action`` | string   | What happened to the bug: "created" or "\<field\>-changed"                               |
+------------+----------+------------------------------------------------------------------------------------------+
| ``target`` | url-path | A path to the bug target (can be a product, distribution or distribution source package) |
+------------+----------+------------------------------------------------------------------------------------------+
| ``bug``    | url-path | A path to the bug                                                                        |
+------------+----------+------------------------------------------------------------------------------------------+
| ``old``    | dict     | Bug attributes before the update                                                         |
+------------+----------+------------------------------------------------------------------------------------------+
| ``new``    | dict     | Bug attributes after the update                                                          |
+------------+----------+------------------------------------------------------------------------------------------+

``old`` and ``new`` are dictionaries of attributes as follows:

+-------------------+----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Key               | Type           | Value                                                                                                                                                        |
+===================+================+==============================================================================================================================================================+
| ``title``         | string         | Title of the bug                                                                                                                                             |
+-------------------+----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``description``   | string         | Description of the bug                                                                                                                                       |
+-------------------+----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``reported``      | string         | A path to the user that reported the bug                                                                                                                     |
+-------------------+----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``status``        | string         | Status of the bug task for the given target                                                                                                                  |
+-------------------+----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``importance``    | string         | Importance of the bug task for the given target                                                                                                              |
+-------------------+----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``assignee``      | string         | A path to the user responsible for the bug task for the given target                                                                                         |
+-------------------+----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``tags``          | list\[string\] | List of tags added to the bug                                                                                                                                |
+-------------------+----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``date_created``  | string         | Date of creation of the bug for the given target (if a new target was added to an existing bug, this is the date the bug was targeted into the given target) |
+-------------------+----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+

Note that if a bug with multiple targets is updated, assuming all
targets have bug webhooks set up, the system will trigger one webhook
per target, and their payloads will be different from each other in the
fields specific to the target (``status``, ``importance``, ``assignee``, and
``date_created``).

.. _bug-comment-created:

Bug comment created
~~~~~~~~~~~~~~~~~~~

Triggered any time a new comment is added to a bug. The payload is:

+-----------------+----------+------------------------------------------------------------------------------------------+
| Key             | Type     | Value                                                                                    |
+=================+==========+==========================================================================================+
| ``action``      | string   | What happened to the comment: ``created`` or ``<field>-changed``                         |
+-----------------+----------+------------------------------------------------------------------------------------------+
| ``target``      | url-path | A path to the bug target (can be a product, distribution or distribution source package) |
+-----------------+----------+------------------------------------------------------------------------------------------+
| ``bug``         | url-path | A path to the bug                                                                        |
+-----------------+----------+------------------------------------------------------------------------------------------+
| ``bug_comment`` | url-path | A path to the bug comment                                                                |
+-----------------+----------+------------------------------------------------------------------------------------------+
| ``old``         | dict     | Comment attributes before the update                                                     |
+-----------------+----------+------------------------------------------------------------------------------------------+
| ``new``         | dict     | Comment attributes after the update                                                      |
+-----------------+----------+------------------------------------------------------------------------------------------+

``old`` and ``new`` are dictionaries of attributes as follows:

+---------------+--------+-----------------------------------+
| Key           | Type   | Value                             |
+===============+========+===================================+
| ``commenter`` | string | A path to the user that commented |
+---------------+--------+-----------------------------------+
| ``content``   | string | Comment message                   |
+---------------+--------+-----------------------------------+

.. _source-package-upload:

Source package upload
~~~~~~~~~~~~~~~~~~~~~

Triggered when the status of a source package upload changes. The payload is:

+-------------------------+----------+---------------------------------------------------------------------------------------+
| Key                     | Type     | Value                                                                                 |
+=========================+==========+=======================================================================================+
| ``package_upload``      | url-path | The source package                                                                    |
+-------------------------+----------+---------------------------------------------------------------------------------------+
| ``action``              | string   | "status-changed"                                                                      |
+-------------------------+----------+---------------------------------------------------------------------------------------+
| ``status``              | string   | The status of the source package upload: one of "Accepted", "Rejected", "Unapproved"  |
+-------------------------+----------+---------------------------------------------------------------------------------------+
| ``archive``             | url-path | The archive associated with the source package                                        |
+-------------------------+----------+---------------------------------------------------------------------------------------+
| ``package_name``        | string   | Name of the accepted source package if it is available                                |
+-------------------------+----------+---------------------------------------------------------------------------------------+
| ``package_version``     | string   | Version of the accepted source package if it is available                             |
+-------------------------+----------+---------------------------------------------------------------------------------------+ 

.. _binary-package-upload:

Binary package upload
~~~~~~~~~~~~~~~~~~~~~

Triggered when the status of a binary package upload changes. The payload is:

+-------------------------+----------+---------------------------------------------------------------------------------------+
| Key                     | Type     | Value                                                                                 |
+=========================+==========+=======================================================================================+
| ``package_upload``      | url-path | The binary package                                                                    |
+-------------------------+----------+---------------------------------------------------------------------------------------+
| ``action``              | string   | "status-changed"                                                                      |
+-------------------------+----------+---------------------------------------------------------------------------------------+
| ``status``              | string   | The status of the binary package upload: one of "Accepted", "Rejected", "Unapproved"  |
+-------------------------+----------+---------------------------------------------------------------------------------------+
| ``archive``             | url-path | The archive associated with the binary package                                        |
+-------------------------+----------+---------------------------------------------------------------------------------------+
| ``source_package_name`` | string   | Name of the source package corresponding to this binary package                       |
+-------------------------+----------+---------------------------------------------------------------------------------------+

.. _binary-build:

Binary build
~~~~~~~~~~~~

Triggered when the status of a binary build changes. The payload is:

+-------------------------+----------+---------------------------------------------------------------------------------------------------------------------------------------+
| Key                     | Type     | Value                                                                                                                                 |
+=========================+==========+=======================================================================================================================================+
| ``build``               | url-path | The binary build                                                                                                                      |
+-------------------------+----------+---------------------------------------------------------------------------------------------------------------------------------------+
| ``action``              | string   | "status-changed"                                                                                                                      |
+-------------------------+----------+---------------------------------------------------------------------------------------------------------------------------------------+
| ``status``              | string   | The status of the binary build: one of "Fully built", "Failed to build", "Chroot wait", "Cancelled", "Failed to upload", "Superseded" |
+-------------------------+----------+---------------------------------------------------------------------------------------------------------------------------------------+
| ``archive``             | url-path | The archive associated with the binary package                                                                                        |
+-------------------------+----------+---------------------------------------------------------------------------------------------------------------------------------------+
| ``source_package_name`` | string   | Name of the source package corresponding to this binary build                                                                         |
+-------------------------+----------+---------------------------------------------------------------------------------------------------------------------------------------+
| ``buildlog``            | string   | The buildlog if it exists                                                                                                             |
+-------------------------+----------+---------------------------------------------------------------------------------------------------------------------------------------+

