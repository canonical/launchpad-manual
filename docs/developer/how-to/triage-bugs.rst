.. _triaging-launchpad-project-bugs:

Triaging Launchpad project bugs
===============================

.. include:: ../../includes/important_not_revised.rst

Our triage process is basically this: make sure that *Critical* and
*High* bugs are correctly marked.

We want:

-  *Critical* bugs to be those that need attention before all others.
   Right now: regressions, stakeholder-escalated bugs, operational
   issues (e.g. build breakage, code issues causing deployment failures,
   things preventing us detecting other failures such as cronspam,
   things that should oops but a lack of tooling prevents) and bugs that
   are dependencies of other critical bugs.
-  The *High* bugs list to be our main set of top priorities. Some
   specific sorts of bugs we always treat as high. Right now: OOPSes,
   timeouts, A and AA treat accessibility
   bugs.

We would prefer to be able to treat OOPSes and timeouts as critical, as it
was the case until 2020, but having a practically-usable Critical queue
takes priority.

We are currently reviewing previously-triaged bugs. Prior to 2020, the Critical
and High queues grew significantly, and many bugs that were marked as such due
to their urgency are less urgent when assessed today. By significantly pruning
these lists we can ensure that we're focusing our time and energy on the most
important priorities.

For a full understanding of why we triage bugs and how we came to
develop this process, please read our description of the :ref:`background to
our bug triage process <bug-triage-process-background>`.

How to triage
-------------

These are the questions we ask when triaging bug reports about
`launchpad-project <https://bugs.launchpad.net/launchpad-project>`__:

1. **Is this a bug in Launchpad-project?** If not, move it to the
   appropriate project or distribution (e.g. Ubuntu) and move to the
   next bug. Note that bugs in lazr.restful, loggerhead etc **are** bugs
   in launchpad-project. To move the bug, click the dropdown button in
   the left side of the *Affects* column and then move it to the
   appropriate project or distribution.
2. **Is this bug on the right subproject?** If not, move it to the right
   sub project.
3. **Is it a duplicate?** if there is a duplicate, mark the newer bugs
   as a duplicate of the older bug.
4. **Is it something we will not do and would not accept a patch to
   do?** If so, mark it as *Won't Fix*.
5. **Is it something we will not now and defer to a later date?** If so, mark
   it as *Deferred*.
6. **Is it an operational request?** If yes, convert it to a question.
7. **When are we likely to fix this?** Set the importance to show when
   we'll get to fixing this bug (`read more about choosing an
   importance <#importance>`__).
8. **Does the report have enough detail?** If we couldn't replicate or
   otherwise begin work on the bug with the information provided,
   request further information from the reporter and mark it as
   *Incomplete* and move to the next bug. If someone has already asked
   for more info and the reporter has replied, change the status from
   *Incomplete* to *Triaged*.
9. **Set the status to Triaged**.

If you're uncertain what importance to give a bug, chat with another
engineer. If there's a disagreement, let common sense and courtesy take
priority.

Importance
----------

We use three of Launchpad's bug importances and give each a specific
meaning.

Critical
~~~~~~~~

Any bug marked *Critical* takes priority over all other bugs.

At present, security bugs, regressions (including supported-browser
issues) and stakeholder escalations are all marked as *Critical*.
Non-security bugs should also be tagged "regression" etc. so that the
reason for their importance is clear. Other types of bug may also be
*Critical*; project leads will expect you to justify marking any other
type of bug as *Critical*.

If all is well with Launchpad, there should be no *Critical* bugs.

<<Anchor(high)>>

High
~~~~

These are bugs that will be our main focus in normal operation, `timeouts <https://bugs.launchpad.net/launchpad/+bugs?field.tag=timeout>`_
(tagged "timeout"), `OOPSes <https://bugs.launchpad.net/launchpad/+bugs?field.tag=oops>`_ , 
and A and AA conformance accessibility bugs.

Low
~~~

We mark as *Low* any bug that we recognise as legitimate but that is
**not** a priority for Canonical staff to fix. This is not the same as
planning not to fix the bug; it means that we don't know when we will
fix it, if at all. This includes AAA conformance accessibility
bugs.

Others
~~~~~~

We do not use *Medium* or *Wishlist*. This is primarily to avoid giving
false hope to people who are interested in a bug that is neither
*Critical* nor *High*: if it does not have one of these statuses, we
think it is unlikely we will focus effort on it.

Tagging bugs
------------

We tag bugs as part of the triage process. Read the :ref:`list of Launchpad
tags <tagging-bugs-about-launchpad>` to find out which
tags to use.

Assigning bugs
--------------

We do not assign bugs as part of the triage process. Only *In progress*
bugs should be assigned to someone.

Even *Critical* bugs do not need an assignee, unless they are being
worked on. Being at the top of the queue is all we need for *Critical*
bugs to get the attention they require.

Selecting bugs to work on
-------------------------

If you are working on Launchpad in your own time you'll most likely want
to fix those bugs that matter to you, regardless of what importance the
Launchpad project gives them. That's great and we welcome all bug fixes;
we encourage you to look at :doc:`our page about fixing bugs <fixing-bugs>` first.

Members of Canonical's Launchpad team will select bugs as seems
appropriate to them.

Quarterly review
----------------

Four times a year, we put all of the *High* bugs back through the triage
process. This lets us make sure that all those bugs really should be
*High* and to take account of anything that has changed since they were
last triaged.

Resolving disputes
------------------

Beyond these rules a bug is more important than another bug if fixing it
will make Launchpad more better than fixing the other bug.

Discretion and a feel for what's in the bug database will help a lot
here, as will awareness of our userbase and their needs. One sensible
heuristic is to look at five to ten existing *High* bugs and, if the new
bug is less important than all of them, mark it *Low* as it's probably
less important than all existing *High* bugs.

Engineers have discretion to decide any particular bug should be sorted
higher (or lower) than it has been; some change requests are very
important to many of our users while still not big enough to need a
dedicated team working on them.

When two engineers disagree, or if someone in the management chain
disagrees, common sense and courtesy should be used in resolving the
disagreement.
