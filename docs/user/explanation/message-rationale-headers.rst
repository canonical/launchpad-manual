Rationale headers in Launchpad email
====================================

.. include:: /includes/important_not_revised_help.rst

When sending out most email, Launchpad will include
``X-Launchpad-Message-Rationale`` and ``X-Launchpad-Notification-Type``
headers which you can filter with.

In all cases where it includes ``X-Launchpad-Message-Rationale`` for a
notification directed at a person or a team, Launchpad will also include
an ``X-Launchpad-Message-For`` header identifying the person or team that
the notification is for: for example, if your username is ``some-user``
and you are subscribed directly to a bug, then the notification will
have ``X-Launchpad-Message-For: some-user``, while if you are a member of
``ubuntumembers`` and you receive bug mail because that team is
subscribed to a bug, then the notification will have
``X-Launchpad-Message-For: ubuntumembers``.

Bugmail
-------

The basic rationale headers are for the cases where you are directly
related to a bug:

::

       X-Launchpad-Message-Rationale: Assignee
       X-Launchpad-Message-Rationale: Subscriber

If you are related to a bug through a team, an @ notation is added:

::

       X-Launchpad-Message-Rationale: Assignee @ubuntu-kernel-bugs
       X-Launchpad-Message-Rationale: Subscriber @ubuntu-core-dev

Bug Contacts and Registrants, which are implicitly subscribed to public
bugs, have their own headers:

::

       X-Launchpad-Message-Rationale: Bug Contact (mozilla-firefox in ubuntu)
       X-Launchpad-Message-Rationale: Registrant (kiwi)

This is combined with the @ notation when you are a member of a team who
is bug contact:

::

       X-Launchpad-Message-Rationale: Bug Contact (ubuntu) @ubuntu-bugs

If the notification was generated in a duplicate bug, we tack on a via
string:

::

       X-Launchpad-Message-Rationale: Assignee via Bug 1332

This one is worth explaining a bit further. Let's say this bugmail is
for bug 2129; the header here means you are the assignee of "master bug"
1332, of which 2129 is a duplicate. You can use this header to filter
away bug that you are receiving from duplicates of a bug you are
subscribed to.

All bugmail also has:

::

       X-Launchpad-Notification-Type: bug

Answer Tracker Mail
-------------------

The basic rationale headers are for the cases where you are directly
related to a question:

::

       X-Launchpad-Message-Rationale: Assignee
       X-Launchpad-Message-Rationale: Subscriber

The other possibility is when you are receiving the notification because
you are an answer contact for the question's target:

::

       X-Launchpad-Message-Rationale: Answer Contact (mozilla-firefox in ubuntu)
       X-Launchpad-Message-Rationale: Answer Contact (Ubuntu)

This is combined with the @ notation when you are a member of a team who
is an answer contact:

::

       X-Launchpad-Message-Rationale: Answer Contact (Launchpad) @launchpad-qa

Code Hosting Mail
-----------------

Mail is only sent to subscribers of branches. If you are directly
subscribed to a branch the rationale header is:

::

       X-Launchpad-Message-Rationale: Subscriber

This is combined with the @ notation when you are a member of a team who
is subscribed to the branch:

::

       X-Launchpad-Message-Rationale: Subscriber @ubuntu-core-dev

There are various notification types for code. When the properties of a
branch are modified (for example using "Change details"):

::

       X-Launchpad-Notification-Type: branch-updated

When new revisions are found on a branch:

::

       X-Launchpad-Notification-Type: branch-revision

For notifications related to merge proposals:

::

       X-Launchpad-Notification-Type: code-review

Build Mail
----------

Notifications regarding the various types of builds that Launchpad can
perform for you have associated rationales. If you requested a source
package recipe, :ref:`live filesystem <live-file-systems>`, or snap package
build:

::

       X-Launchpad-Message-Rationale: Requester

If you created the source package (you are listed in its \`Changed-By\`
field for a direct upload, or you requested a copy):

::

       X-Launchpad-Message-Rationale: Creator

If you did not create the source package but you signed it:

::

       X-Launchpad-Message-Rationale: Signer

If you did not create or sign the source package, but the build is in a
PPA that you own:

::

       X-Launchpad-Message-Rationale: Owner

Any of these may have the @ notation appended if the relation is through
a team, as above.

The notification type indicates which kind of build prompted the
notification. It will be one of:

::

       X-Launchpad-Notification-Type: package-build-status
       X-Launchpad-Notification-Type: recipe-build-status
       X-Launchpad-Notification-Type: livefs-build-status
       X-Launchpad-Notification-Type: snap-build-status

Upload Mail
-----------

Launchpad sends notifications in response to source package uploads. If
you signed a source package or requested a copy (these may be separated
into distinct rationales in future):

::

       X-Launchpad-Message-Rationale: Requester

For primary archives, if you did not sign the source package or request
the copy, but you are listed in its \`Maintainer\` field:

::

       X-Launchpad-Message-Rationale: Maintainer

For primary archives, if you did not sign the source package or request
the copy and are not listed in its \`Maintainer\` field, but are listed
in its \`Changed-By\` field:

::

       X-Launchpad-Message-Rationale: Changed-By

For PPAs, if you did not sign the source package or request the copy,
but you have been manually configured as an additional uploader to the
PPA (this is an unusual configuration):

::

       X-Launchpad-Message-Rationale: PPA-Uploader

Any of these may have the @ notation appended if the relation is through
a team, as above.

All package upload mail also has:

::

       X-Launchpad-Notification-Type: package-upload

Team Membership Mail
--------------------

Launchpad sends notifications of team membership changes. For an
invitation to a team you administer to join another team:

::

       X-Launchpad-Message-Rationale: Invitation (target-team-name) @name-of-team-you-administer
       X-Launchpad-Notification-Type: team-membership-invitation

For all other team membership notifications, the rationale depends on
your relationship to the team containing the membership:

::

       X-Launchpad-Message-Rationale: Member (team-name)
       X-Launchpad-Message-Rationale: Admin (team-name)
       X-Launchpad-Message-Rationale: Owner (team-name)

Your relationship to the team containing the membership may be by way of
another team. For instance, if you are a member of \`project-leader`,
and \`project-leader\` is the owner of \`project-dev`, then a
notification that a new member has been added to \`project-dev\` would
have this rationale:

::

       X-Launchpad-Message-Rationale: Owner (project-dev) @project-leader

In each case, the notification type describes the event that caused the
notification, which may be a new member joining a team, a pending new
membership that needs approval, a changed membership status, an expired
membership, an accepted invitation to join a team, a declined invitation
to join a team, a membership that will expire soon, or a member
extending the term of their own membership:

::

       X-Launchpad-Notification-Type: team-membership-new
       X-Launchpad-Notification-Type: team-membership-pending
       X-Launchpad-Notification-Type: team-membership-change
       X-Launchpad-Notification-Type: team-membership-expired
       X-Launchpad-Notification-Type: team-membership-invitation-accepted
       X-Launchpad-Notification-Type: team-membership-invitation-declined
       X-Launchpad-Notification-Type: team-membership-expiration-warning
       X-Launchpad-Notification-Type: team-membership-renewed