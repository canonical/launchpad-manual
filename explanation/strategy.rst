==================
Launchpad strategy
==================

*We want to make Ubuntu the world's best operating system. To do this, we need
to give Canonical an edge in productivity over and above other Linux vendors
and, just as importantly, help make the development of open source software
faster, more efficient and more innovative than its proprietary rivals.*

Launchpad does this by helping software developers share their work and
plans, not just within a project but also **between** projects.


Introduction
============

This document tries to answer two big questions:

1. *why* are we making Launchpad?
2. *who* is Launchpad for?

This is not our strategy for the year or the scope of Launchpad development
for the next six months.  Rather, it is our answer to these fundamental
questions.

When you are finished reading this document, you should know what problems we
want to solve, what we hope to gain from solving these problems and how we
know if Launchpad is doing well.


Audience
--------

This document is for everyone who cares about improving Launchpad. Primarily,
we've written it for Launchpad's stakeholders within Canonical and for the
developers of Launchpad, whether they are Canonical employees or not.


Why are we making Launchpad?
============================

The world we live in
--------------------

Open source software is bigger than you think.  It is much more than simply
writing the code.  Code has to be packaged, integrated and delivered to users
who can then give feedback and file bugs.  Distributions made up of tens of
thousands of different software packages need to be released to meet a
deadline.  Translations must be made into hundreds of different languages and
accumulated from a variety of sources.  Everywhere bugs need to be tracked,
fixed and checked.  Plans must be made and kept.  Distributions have to be
made to work on a wide variety of hardware platforms with varying degrees of
openness.

Those who make open source software and wish to profit commercially also face
unique challenges.  Contributors are scattered across the world, making
coordination, communication and alignment just that little bit more difficult.
Many contributors are volunteers, and so decisions must often be made by
consensus, deadlines enforced without the leverage of an employment contract
and quality maintained without formal training.  Users of open source software
use a widely heterogeneous stack of software and hardware, thus increasing the
burden of compatibility work.  All of these things make open source software
development more difficult, thus increasing the need for tools to aid
collaboration.

The Ubuntu community, together with Canonical, are dedicated to making the
very best open source operating system possible, one that far excels any
proprietary operating system.  To do this, we need to ensure that the process
of making Ubuntu is as effective as possible.  Moreover, we need to make the
process of making open source software as effective as possible, and then make
it easy, quick and desirable to get that software into Ubuntu.

Secondarily, Canonical's main business is the provision of premium services
built around Ubuntu.  Many of these services are based on proprietary
software, which Canonical must be able to make more quickly and at less cost
than any rival.

The word "effective" covers a multitude of concepts.  Here we mean doing the
*right* work with the highest possible *quality* as *quickly* and with as
little *waste* as possible.


Business goals
--------------

Launchpad exists to give Canonical a competitive advantage over other
operating system vendors and service providers, both proprietary and open
source.

To gain an advantage over *open source* operating system vendors, Canonical is
relying on Launchpad to:

* increase Canonical's effectiveness in making software
* grow and accelerate contributions to Ubuntu

To gain an advantage over proprietary operating system vendors, Canonical
needs Launchpad to do both of the above and:

* improve and accelerate open source software development in general beyond
  that of proprietary software so that the software in Ubuntu is better than
  the software in any rival proprietary operating system

The value flow of Launchpad can be summed up in this diagram:

.. image:: ../images/value-flow.svg


Who is Launchpad for?
=====================

Launchpad is aimed at many different groups of users.  They can be roughly
described as follows:

Software developers
  These are people who make or contribute to free and open source
  software. They are made up of both paid professionals and volunteers working
  in their spare time.  They vary widely in expertise and patience.  Any given
  software developer might be working on both open source software and
  proprietary software.

Expert users of software
  The sort of people who file bugs, try new releases, run the bleeding edge
  snapshot, are interested in following development plans, who help other
  people on mailing lists. Note that software developers are frequently but
  not always expert users of software.

End users of software
  People who download and install software and then use it.  These people have
  little understanding about what software actually is or how it is made.
  They use it, sometimes without noticing, sometimes enjoying it, sometimes
  hating it.

Translators
  A special class of software developer who is normally a native speaker of a
  language other than English.  They contribute to open source software
  projects not by submitting code, but by translating strings to new
  languages.

Managers
  These are managers in the broad sense of people who are responsible for the
  completion of a task and so need to know what many other people are doing
  towards that goal.  This includes release managers, project leads and
  traditional corporate project managers.  It does not necessarily mean people
  who are employed as managers.


User needs
----------

The people who use Launchpad, in whatever role, share one broad goal: “make
great software and get it to its users”.  To do this, they need:

* tools to facilitate collaboration on their proprietary and open source
  software projects
* a place to host and publish their open source software projects
* as little overhead as possible in maintaining these projects
* more contributors to their projects
* to be able to easily contribute to existing software projects

Some of our users have particular needs:

* managers need to be able to quickly get an overview of activity and
  progress for their teams and their projects
* expert users of software need to be able to give high quality feedback to
  the software developers

Further, we believe that providing tools for cross-project collaboration, we
can benefit our users by:

* giving them feedback from groups of their own users that they couldn't reach
  before
* reducing the time and effort required to publish software to actual end
  users
* pointing them to knowledge and fixes from other projects in their network
* helping OS-driven improvements reach them code faster, and their
  improvements reach the OS faster


Conflicts between business goals & user needs
---------------------------------------------

Canonical is primarily interested in open source software that runs on Linux
or lives within the Linux ecosystem.  Thus, even though Launchpad could be an
excellent, general platform for Windows, OS X, iOS and Android based software,
our main area of focus is software that is aimed to run natively on Linux.

Canonical is much more interested in quality assurance and release management
than many open source and even proprietary projects.


References
==========

* :doc:`scope`
* :doc:`values`
* `Feature checklist <https://dev.launchpad.net/FeatureChecklist>`_
