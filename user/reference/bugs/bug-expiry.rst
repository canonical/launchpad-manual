Bug expiry
==========

While we all have the best of intentions to at least triage every bug
that is reported against a project we're involved with, there are just
some bugs that never get looked at.

Rather than allowing stale bugs to clutter your project's bugs list,
Launchpad offers you a pragmatic way of dealing with moribund bugs:
`old, unattended <Bugs/Expiry#definition>`__ bugs that have the ``Incomplete`` status are expired.

This gives you three benefits:

-  you can view a report of all bugs that are due to expiry and so deal
   with any that need your attention
-  once the bug's expired, Launchpad notifies all subscribers, which may
   prompt someone to clarify the report or otherwise deal with the bug
-  it removes stale bugs from your bug lists.

Launchpad also places a message on the report page of any bug that's due
to expire.

Disabling bug expiry
--------------------

You can choose to have Launchpad automatically expire bugs that have
become stale. Bug expiry is automatically enabled when you mark your project as using
Launchpad to track its bugs. However, if bug expiry doesn't suit your
project, visit

::

   "https://launchpad.net/<yourproject>/+edit"

to disable it.

Old, unattended and incomplete?
-------------------------------

Launchpad consider bugs ready for expiry if it appears that they have
been abandoned. It considers a bug to be abandoned if:

-  it has the "Incomplete" status
-  the last update was more than 60 days ago
-  it is not marked as a duplicate of another bug
-  it has not been assigned to anyone
-  it is not targeted to a milestone.

Only projects and distributions that use Launchpad as their bug tracker
and that have not disabled bug expiry are part of the bug expiration
process.

Bugs watched in external trackers are never candidates for expiry.

Bugs that affect several projects
---------------------------------

Bugs tracked in Launchpad can affect several communities (projects or
distributions) and each community has its own status for that bug.

Launchpad will consider these bugs for expiry only in those projects or
distributions that have chosen to use bug expiry. However, the bug will
be removed from the bug expiry process entirely as soon as one of those
communities marks it as confirmed.