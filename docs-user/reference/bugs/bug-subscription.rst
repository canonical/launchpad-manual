Bug subscription
================

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

What you'll receive
~~~~~~~~~~~~~~~~~~~

Launchpad sends bug notifications when:

-  a new bug is reported
-  someone makes a comment on a bug
-  a bug's status or importance changes
-  a bug is assigned to someone
-  a bug is targeted to a milestone
-  a bug is marked as affecting a new series, package or project.

You can filter bug mail based on both the subject and headers. A prefix
of ``[NEW]`` in the subject lets you distinguish emails about newly
reported bugs from updates about previous bugs.

Bug mail headers
~~~~~~~~~~~~~~~~

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

X-Launchpad-Bug
^^^^^^^^^^^^^^^

The ``X-Launchpad-Bug`` header collates most of the other
information about a bug's status, importance, etc. It gives you slightly
different information, depending on whether you're dealing with a
distribution package or a project:

Project
........

-  ``product``
-  ``status``
-  ``importance``
-  ``assignee``
-  **For example:** ``X-Launchpad-Bug: product=terminator;
   status=Confirmed; importance=Low; assignee=None;``

Package
.......

-  ``distribution``
-  ``sourcepackage```
-  ``component``
-  ``status``
-  ``importance``
-  ``assignee``
-  **For example:** ``X-Launchpad-Bug: distribution=ubuntu;
   sourcepackage=exaile; component=universe; status=Confirmed;
   importance=Medium; assignee=None;``

Bug mail rationale
~~~~~~~~~~~~~~~~~~

The ``X-Launchpad-Message-Rationale`` header tells you why you've
received the notification.

You can be either:

-  ``Assignee``
-  ``Subscriber``
-  ``Registrant``

For example: ``X-Launchpad-Message-Rationale: Assignee``

An ``@`` symbol shows that you're related to the bug through
membership of a team:

::

       X-Launchpad-Message-Rationale: Assignee @ubuntu-kernel-bugs
       X-Launchpad-Message-Rationale: Subscriber @ubuntu-core-dev

If you're the project/package owner, the product/package name is show in
parentheses:

::

       X-Launchpad-Message-Rationale: Registrant (kiwi)

If the notification is about a duplicate bug, the rationale shows you
which bug this report duplicates:

::

       X-Launchpad-Message-Rationale: Assignee via Bug 1332

This makes it easy to filter out bug mail about duplicate bugs. For
example: let's say this bug notification is for bug 2129. This header
means you are the assignee of bug 1332, of which 2129 is a duplicate.

Atom feeds
----------

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

Further information
-------------------

As well as using email to send updates about the status of bugs,
Launchpad gives you a full `email interface to the bug
tracker <Bugs/EmailInterface>`__.
