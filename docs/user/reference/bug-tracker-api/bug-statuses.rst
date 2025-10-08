.. _bug-status-in-launchpad:

Bug statuses in Launchpad
=========================

.. include:: /includes/important_not_revised_help.rst

Launchpad's bug tracker offers you seven main bug statuses that reflect
each stage of a bug's lifecycle, from initial report to resolution.

Optionally, if your project has a high number of bug reports, you may
want to add an extra layer of quality control to your bug triage.
Whereas anyone can set most of the bug statuses, which makes it easy for
new contributors to get involved, there are two additional bug statuses

-  *Triaged*, *Won't Fix* and *Deferred* - that are available only to your project's
   owner, bug supervisor and the relevant drivers.

Available to everyone
---------------------

-  ``New``
-  ``Incomplete``: the bug report is incomplete and needs more
   information before it can be triaged. Bugs in this state are
   considered for :ref:`expiry <bug-expiry>`.
-  ``Invalid``: the report describes the software's normal behavior, or
   is unsuitable for any other reason.
-  ``Confirmed``: a member of the community other than the original
   reporter believes that this report describes a genuine bug in enough
   detail that a developer could start work on a fix.
-  ``In Progress``: a developer has taken responsibility to fix the bug
   and has begun work.
-  ``Fix Committed``: a developer has committed his/her fix to the
   project's codebase.
-  ``Does Not Exist``: custom status used by the security team for
   specifying the impact of a CVE/vulnerability on a package.
-  ``Fix Released``: a new version of the software, featuring the bug
   fix, has been released.
-  *Under consideration for removal:* ``Opinion``: there is a difference
   of opinion about the bug and everyone is free to continue the
   discussion, however, the project maintainers consider the issue
   closed.

Only available to the bug supervisor
------------------------------------

-  ``Triaged``: the bug supervisor considers that the bug report
   contains all information a developer needs to start work on a fix.
-  ``Won't Fix``: this is acknowledged as a genuine bug but the project
   has no plans to fix it.
-  ``Deferred``: the bug supervisor considers that the bug fix will be deferred
   to a later date.

Translating external bug statuses
---------------------------------

When Launchpad watches a bug report in an external tracker - such as
Bugzilla or Sourceforge - it translates that bug's status information
into the equivalent Launchpad status.

See our :ref:`page on external bug statuses <external-bug-statuses>`.

Further information
-------------------
If you're working on a fix to a bug and hosting that code in Launchpad, you can :ref:`link from the bug report directly to the branch of code <link-a-bug-reports-to-a-branch>`.
