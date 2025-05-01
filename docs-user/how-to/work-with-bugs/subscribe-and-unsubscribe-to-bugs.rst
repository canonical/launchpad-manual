Subscribe and unsubscribe to bugs
=================================

Launchpad uses notification emails and Atom feeds to help you stay on
top of the bugs that interest you.

Bug mail
--------

There are three ways to get bug notifications by email:

-  subscribe to a bug
-  subscribe to a milestone, project, package or distribution
-  take a role that results in bug mail:

   -  bug reporter
   -  assignee

Subscribing to an individual bug is as simple clicking ``Subscribe``
on the bug report page. You can also subscribe another individual or a
team to a bug. However, you should only do this if you're certain the
person or team members are happy for you to do so.

Subscribe to an entire milestone, project, package or distribution
------------------------------------------------------------------

To receive notifications about a milestone in a project, a distribution
(e.g. Ubuntu) or a package or project, click ``Subscribe to
bugmail`` on the milestone, project, package or distribution bugs
overview page.

What you'll receive
~~~~~~~~~~~~~~~~~~~

Launchpad sends bug notifications when:

-  a new bug is reported
-  someone makes a comment on a bug
-  a bug's status or importance changes
-  a bug is assigned to someone
-  a bug is targeted to a milestone
-  a bug is marked as affecting a new series, package or project.

Filter your bug mail
~~~~~~~~~~~~~~~~~~~~

You can filter bug mail based on both the subject and headers. A prefix
of ``[NEW]`` in the subject lets you distinguish emails about newly
reported bugs from updates about previous bugs.

Launchpad uses email headers to help you automatically filter bug mail.

-  **X-Launchpad-Bug:** See
   `X-Launchpad-Bug <Bugs/Subscriptions#x-launchpad-bug>`__ section
   below.
-  **X-Launchpad-Bug-Private:** ``yes`` or ``no``
-  **X-Launchpad-Bug-Security-Vulnerability:** ``yes`` or ``no``
-  **X-Launchpad-Bug-Commenters:** An alphabetical, space separated,
   list of everyone who has commented on the bug.
-  **X-Launchpad-Bug-Reporter:** The username of the person who reported
   the bug and created its first bug task.
-  **X-Launchpad-Bug-Modifier:** The display name and username of the
   person who modified the bug, in the form *Display Name (username)*.
-  **X-Launchpad-Bug-Tags:** An alphabetical, space separated, list of
   tags the bug currently possesses.
-  **X-Launchpad-Bug-Duplicate:** If the bug is a duplicate, this header
   is set to the number of the duplicate target bug.
-  **X-Launchpad-Message-Rationale:** See `Bug mail
   rationale <Bugs/Subscriptions#rationale>`__ section below.

Unsubscribe from bug notifications
----------------------------------

You can unsubscribe from bug notifications at any time.

-  **Individual bugs**: visit the bug report and click
   ``Unsubscribe``.
-  **All bugs in a particular context**: visit the context's overview
   page - such as a project's overview page - and select ``Subscribe
   to bug mail``.

.. note::
    If you receive bug mail because you're in a team that is a
    reporter, commenter or assignee, you must leave that team to stop
    receiving the notifications.

Subscribe to bug feeds
----------------------

You can subscribe to a feed of the bugs that affect a person, team,
project or distribution. You can also subscribe to individual bugs.

Most feed readers will automatically discover the bug feed if you give
them the URL of the bug report or the person, team, project or
distribution overview page.

Alternatively, you can build the bug feed URL by hand:

**Individual bugs:** ``http://feeds.launchpad.net/bugs//bug.atom``

Replace ``//`` with the bug number.

For example: http://feeds.launchpad.net/bugs/1/bug.atom

**Projects and distributions:**
``http://feeds.launchpad.net//latest-bugs.atom``

Replace ``//`` accordingly.

For example: http://feeds.launchpad.net/ubuntu/latest-bugs.atom

**People and teams:**
``http://feeds.launchpad.net/~/latest-bugs.atom``

Replace ``/~/`` accordingly.

For example: http://feeds.launchpad.net/~bzr/latest-bugs.atom

Next step
---------

As well as using email to send updates about the status of bugs,
Launchpad gives you a full :doc:`email interface to the bug
tracker <../../explanation/feature-highlights/email-interface>`.