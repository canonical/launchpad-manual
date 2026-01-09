===================
Architectural guide
===================

All the code we write will meet these values to a greater or lesser degree.
Where you can, please make choices that make you code more strongly meet
these values.

Some existing code does not meet them well; this is simply an opportunity to
get big improvements - by increasing e.g. the transparency of existing code,
operational issues and debugging headaches can be reduced without a great
deal of work.

This guide is intended as a living resource: all Launchpad developers, and
other interested parties, are welcome to join in and improve it.

Goals
=====

The goal of the recommendations and suggestions in this guide are to help us
reach a number of big picture goals.  We want Launchpad to be:

* Blazingly fast
* Always available
* Change safely
* Simple to make, manage and use
* Flexible

However it's hard when making any particular design choice to be confident
that it drives us towards these goals: they are quite specific, and not
directly related to code structure or quality.

Related documents
-----------------

The :doc:`Python style guide <../reference/python>` specifies coding style guidelines.

Values
======

There are a number of things that are more closely related to code, which do
help drive us towards our goals.  The more our code meets these values, the
easier it will be to meet our goals.

The values are:

* Transparency
* Loose coupling
* Highly cohesive
* Testable
* Predictable
* Simple

Transparency
------------

Transparency speaks to the ability to analyse the system without dropping
into ``pdb`` or taking guesses.

Some specific things that aid transparency:

* For blocking calls (SQL, bzr, email, librarian, backend web services,
  memcache) use ``lp.services.timeline.requesttimeline`` to record the call.
  This includes it in OOPS reports.
* fine grained just-in-time logging (e.g. bzr's ``-Dhpssdetail`` option)

* live status information 
  * (+opstats, but more so)
  * cron script status
  * migration script status

* regular log files
* OOPS reports - lovely
* Which revisions/versions of the software & its dependencies are running

We already have a lot of transparency.  We can use more.

Aim for automation, developer usability, minimal SRE intervention, on-demand
access.

When adding code to the system, ask yourself "how will I troubleshoot this
when it goes wrong without access to the machine it is running on".

Loose coupling
--------------

The looser the coupling between different parts of the system the easier it
is to change them.  Launchpad is pretty good about this in some ways due to
the component architecture, but it's not the complete story: decreasing the
coupling more will help the system.  Consider examples such as the jobs
system and the build farm.

The acid test for the coupling of a component is "how hard is it to reuse?".

Of particular note, many changes in one area of the system (e.g. bugs) break
tests in other areas (e.g. blueprints) - this adds a lot of developer
friction and is a strong sign of overly tight coupling.

Highly cohesive
---------------

The more things a component does, the harder it is to reason about it and
performance-tune it.  This is "Do one thing well" in another setting.

A good way to assess this is to look inside the component and see if it is
doing one thing, or many things.

One common sign for a problem in this area is attributes (or persistent
data) that are not used in many methods - that often indicates there is a
separate component embedded in this one.

There are tradeoffs here due to database efficiency and normalisation, but
it's still worth thinking about: narrower tables can perform better and use
less memory, even if we do add extra tables to support them.

On a related note, the more clients using a given component, the wider its
responsibilities and the more critical it becomes.  That's an easy situation
to end up with too much in one component (lots of clients wanting things
decreases the cohesion), and then we have a large unwieldy critical
component - not an ideal situation.

Testable
--------

We write lots of unit and integration tests at the moment.  However it's not
always easy to test specific components - and the coupling of the components
drives this.

The looser the coupling, the better in terms of having a very testable
system.  However loose coupling isn't enough on its own, so we should
consider testability from a few angles:

Can it be tested in isolation? If it can, it can be tested more easily by
developers and locally without needing lots of testbed environment every
time.

Can we load test it? Not everything needs this, but if we can't load test a
component that we reasonably expect to see a lot of use, we may have
unpleasant surprises down the track.

Can we test it with broken backends/broken data? It is very nice to be
confident that when a dependency breaks (not if) the component will behave
nicely.

It's also good to make sure that someone else maintaining the component
later can repeat these tests and is able to assess the impact of their
changes.

Automation of this stuff rocks!

Predictable
-----------

An extension of stability - servers should stay up, database load should be
what it was yesterday, rollouts should move metrics in an expected
direction.

Predictability is pedestrian, but it's very useful: useful for capacity
planning, useful for changing safely, useful for being highly available, and
useful for letting us get on and do new/better things.

The closer to a steady state we can get, the more obvious it is when
something is wrong.

Simple
------

A design that allows for future growth is valuable, but it is not always
clear how much growth to expect, or in the case of code extension, what
kind.  In this case, it is better to design the simplest thing that will
work at the time being, and update the design when you have a better idea of
what's needed.  Simplicity also aids comprehension and reduces the surface
area for bugs to occur.

Related ideas are KISS, YAGNI, and avoiding premature optimization, but it
is always important to apply judgement.  For example, avoiding premature
optimization does not justify rolling your own inefficient sort function.

Make the design as simple as possible, but no simpler.  Note that simple
does not mean simplistic.

Performance
===========

Document how components are expected to perform.  Docstrings are great
places to put this.  E.g. "This component is expected to deal with < 100 bug
tracker types; if we have more this will need to be redesigned.", or "This
component compares two user accounts in a reasonable time, but when
comparing three or more it's unusable."

Try to be concrete.  For instance: "This component is O(N) in the number of
bug tasks associated with a bug." is OK, but better would be "This component
takes 40ms per bug task associated with a bug."

Testing
=======

Tests for a class should complete in under 2 seconds.  If they aren't, spend
at least a little time determining why.

Transparency
============

Behaviour of components should be analysable in lpnet without asking SREs:
that is, if a sysadmin is needed to determine what's wrong with something,
we've designed it wrong.  Let's make sure there is a bug for that particular
case, or if possible Just Fix It.

Emit Python logging messages at an appropriate importance level: warning or
error for things operators need to know about, info or debug for things that
don't normally indicate a problem.

Coupling
========

No more than 5 dependencies of a component.

Cohesion
========

Attributes should be used in more than 1/3 of interactions.  If they are
used less often than that, consider deleting or splitting into separate
components.

If you can split one class into two or more that would individually make
sense and be simpler, do it.

..
    The ideas in this document are open to discussion and change.  If you
    feel strongly about an issue, make a merge proposal with your
    suggestions.
