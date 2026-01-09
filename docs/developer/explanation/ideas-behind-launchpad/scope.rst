.. _what-is-launchpad:

What is Launchpad?
==================

Launchpad is a complete system for gathering changes from different types of
sources and collaboratively organizing them into packaged software for the end
user, delivered as part of an operating system that can be downloaded or that
comes already installed on purchased hardware.

If you start by thinking of Launchpad as a traditional software “forge” - a
web service that provides bug tracking, code hosting and other related
services - then you are not too far off understanding what Launchpad is.
However, Launchpad has many distinctive traits that combine to put it into an
entirely different category of software.

But at its core, it is best to think of Launchpad as a service that meshes
together two important networks:

1. Networks of people making software
2. The network of dependencies between software

But first, a story.


The Story of a Bug
==================

*Arnold* writes software for a living, and he runs Ubuntu on his desktop. He
wishes he could contribute to open source, but he doesn't have much spare
time, and when he gets home from his job the last thing he wants to do is
program. However, the spirit of willingness is there.

One day, Arnold notices that Tomboy loses his formatting if he alt-tabs at the
wrong time. Arnold knows that a well-filed bug report is a thing of beauty to
most programmers, so he decides to spend a few moments to file a bug against
Tomboy.

Rather than search the net to find where Tomboy tracks its bugs, Arnold uses
Ubuntu's built-in bug filing mechanism. It asks him a bunch of questions,
invites Arnold to write his bug report and then files the bug on Launchpad
against the Tomboy package in Ubuntu.

*Becca* has been dabbling in Ubuntu contribution for a while, mostly by
helping new users solve their problems or turn them into good bug reports. She
notices Arnold's bug, sees that it's well written and thinks that it would be
easy enough to test against trunk. She opens up the Tomboy source package in
Ubuntu and sees that there is a known-good daily build of Tomboy's trunk
hosted in a trusted user archive. Becca installs Tomboy from this archive and
tests to see if the bug is still there in the latest version of the code. It
is. Becca sees this, opens up the original bug report and clicks a button to
forward the bug to the upstream bug tracker.

*Carlos* is one of the Tomboy developers. He sees the bug in the tracker, sees
that it has been tested against trunk, realizes that it's an annoying bug
that's easy to fix and decides to fix it. He does the fix, applies it to the
Tomboy trunk and marks the bug as fixed.

At this point, both Arnold and Becca are notified that the bug is fixed in
Tomboy trunk, and that they can try a version of Tomboy that has the fix by
using the known-good daily build archive for Tomboy. They are warned that this
is dangerous and may cause data loss, but they are also told how they can try
the bug fix for free using a cloud-based Ubuntu desktop. They both try the
bug, see that it's fixed, and are happy, albeit a little impatient for the fix
to be actually released and part of stock Ubuntu.

Meanwhile, *Dalia* is an Ubuntu developer who takes a special interest in
desktop productivity applications like Tomboy. She checks on the Ubuntu source
package for Tomboy from time to time. The last time she checked, she saw that
quite a few bugs have been fixed in trunk but not yet released. Since she
knows the Tomboy release manager from long hours of IRC chat, she contacts him
and gently suggests that he do a release.

*Edmund*, the Tomboy release manager, takes Dalia's hint well and realizes
that a release is way overdue. He makes a release of Tomboy following his
normal procedure.

Launchpad detects that Tomboy has a new, official release and alerts
interested distribution maintainers that the release has been made and now
would be a good time to package a new version. Dalia packages up a new
version, requests that an Ubuntu core developer sponsor the change and then
waits for the new version to be uploaded. Dalia also uploads the fixed version
to one of her personal archives so that others can easily get it without
waiting for the next release of Ubuntu.

*Fiona* the Ubuntu core developer sees Dalia's patch in the sponsorship queue
on Launchpad, notes that it's all good and then uploads the patch to the
official Ubuntu archive. (Fiona might also choose to upload the patch to
Debian).

Launchpad sees that this upload fixes a number of bugs, including the one
originally filed by Arnold, and automatically includes those bugs in the list
of bugs that will be fixed by the next release of Ubuntu.

Two months later, the next release of Ubuntu is actually released. Arnold
upgrades on release day, and tries out Tomboy to see if his bug was really,
actually fixed. It is, and all is right with the world.




Distinctive traits
==================

Launchpad is different from other "forges" in a few important ways:


Cross-project collaboration
---------------------------

No project lives in isolation.  Each project is part of an ecosystem of
software.  Projects must be able to interact with each other, share bugs,
teams, goals and code with each other.

.. image:: ../images/cross-project-collab.png

Launchpad takes every chance it gets to show the connections between projects
and to bring the opportunities created by those connections to light.

By encompassing the entire process, all the way to operating system delivery,
Launchpad can provide a unique service: enable each contributor to focus on
the work they care about, while giving them an ambient awareness of how their
work fits into a larger picture, and providing a path by which they can
participate in other parts of that picture when they feel the need.


Front-end to open source
------------------------

Launchpad aims to be a front-end to open source.  Whether or not a project
chooses to host on Launchpad, opportunistic developers can use Launchpad to
navigate bugs, get code and send patches.  Likewise, we aim to present a
uniform interface to the projects we have.


Centralized service
-------------------

Because Launchpad emphasizes cross-project collaboration, and because
Launchpad aims to be a front-end to all of open source, it necessarily has to
be a centralized service rather than a product that users deploy on their own
servers.


Networks of collaborators
-------------------------

Launchpad understands that much of the human interaction around open source is
not primarily social, but rather collaborative: many people working together
in different ways toward the same goals.

As such, Launchpad highlights actions and opportunities rather than
conversations and status. It answers questions like, “what can I do for you?”,
“who could help me do this?”, “who is waiting on me in order to get their
thing done?”, “can I rely on the advice offered by this person?” and so forth.


Distributions are projects too
------------------------------

Launchpad hosts Linux distributions in much the same way as it hosts projects,
allowing for developers to feel at home when interacting with distributions.


Gated development
-----------------

Sometimes, secrets are necessary.  Launchpad understands that sometimes
development needs to be done privately, and the results only later shared with
the world.  Security fixes, OEM development for new hardware, proprietary
services with open source clients are all examples of these.


Hardware matters
----------------

Many software developers like to pretend that hardware does not really
exist. When people distribute software as part of an operating system, they
don't have the luxury of forgetting. Launchpad understands that developers
often need to acknowledge and work around differences thrown up by hardware.


We don't care if you use Launchpad, sort of
-------------------------------------------

Many other forges define their success by how many users they have.  Although
we love our users and welcome every new user, Launchpad does not judge its
success by the number of users.  If one project wishes to host its development
on another platform, Launchpad acts as a front-end to that platform.


One project, many communities
-----------------------------

Any given project can have many distinct communities interested in it.  These
communities have different interests and different motivations, but all work
in the same project space so that they can easily benefit from each others'
efforts.


Scope
=====

Launchpad has many major components. These can be broken up into four major
areas of functionality:

1. where work is done; developers interact with other developers
2. where plans are made and reviewed; expert users interact with expert users
   and developers
3. where projects engage with their communities; developers interact with end
   users and other developers, and vice-versa
4. major supporting features

.. image:: ../images/scope.png

Work
----

At the core of every software project is the actual code that makes up that
project. Here "code" is a broad term that also includes the project's
documentation, the translatable and translated strings that make up its user
interface, the packaging and integration scripts required to get the software
installed on end user's systems and so forth.

Launchpad is built to be able to take contributions from anybody, regardless
of how involved they are in a project. For packages, translations and code
proper we provide mechanisms to allow people to review changes from others and
then merge them into the official parts of the project.

Launchpad pulls in changes that happen in the upstreams and downstreams of a
project, whether those changes are patches to code, new translations or
packaging updates. It makes contributors to a project aware of the work that's
going on upstream and downstream and helps them take advantage of that work.

And, of course, all work is for nothing if it does not get to the people who
might want to actually use its results. As such, project maintainers can
publish released versions of their code, any contributor can publish Ubuntu
packages to unofficial archives or even set up Launchpad to automatically
build and publish packages of latest snapshots of code.


Plans
-----

People who are interested in doing something great will need to coordinate
their work, keep track of the defects in the things they have already done and
describe the things that they aren't doing yet but wish they could.

Every software product in the world has bugs. For some projects, the rate of
incoming bugs is fairly low, and each bug can expect to receive some attention
from a core developer.  For other projects, the rate of new bugs filed is so
high that the core development team can never hope to keep up with it.
Launchpad supports both kinds of projects.

If every software product has bugs, every software user has great ideas about
how a product can be improved. Project maintainers need to get at these ideas,
evaluate them, and develop them into workable concepts.

Often, a problem is so tricky that those concerned need to have a detailed,
managed discussion about what exactly the problem is.  At other times, the
problem is easy enough to define, but there are so many solutions with
difficult trade-offs or difficult implementations that it is better to talk
about them and plan them out before proceeding with any of them. Launchpad
acknowledges that this can happen on any project, and that becoming clear on a
problem or becoming clear on the “best” solution can be helped a great deal
using tools.

Crucially, all of these different types of "plans" - bugs, specifications,
blueprints, ideas - can span more than one code base and more than one
conceptual project. These plans need to be drafted, discussed, clarified and
reviewed before work starts, monitored, evaluated and changed as work
progresses, and then the results of that work need to be checked against the
plan when the work is finished.


Community
---------

Not everything that's done on a project is work toward a particular outcome,
or plans for how to get there. Every project needs to have some things that
are more general and stable.

Projects need to be able to present themselves to the world, confident in
their identity and communicating exactly what they are about. Project
maintainers need to be able to announce important news, such as releases,
license changes or new practices. Contributors need to get a sense of who is
working on which parts of the project. Users need to be able to ask questions,
get support and give feedback.

Contributors also need to share documentation about the project and how the
project runs. They need to be able to discuss general topics about the
project.

Launchpad supports all of these things, and also makes it clear how any
project fits into the broader ecosystem of projects. It shows which projects
are upstreams or downstreams, which projects are affiliated with other
projects, which projects share contributors with other projects and so forth.


Supporting features
-------------------

Launchpad has many major areas of functionality that are best considered as
“supporting features”: APIs, migration services, privacy, the mail UI,
synchronizing with external systems.


New World
=========

When Launchpad is really doing all of these things and doing them well, the
world of open source software will be significantly changed.

Patches will no longer lie decaying in someone else's bug tracker, waiting to
be noticed. Instead, they will all be synced into a central code review system
and queued for review and approval.

Instead of a distribution tracking one set of bugs and upstream projects
tracking their own set of sometimes duplicated bugs, both upstream and
downstream developers can seamlessly access both sets of bugs.


Glossary
========

Upstream
  A software project itself, as opposed to the packaged version of a software
  project that is included in a distribution. Note, can also be used as a
  relative term, e.g. “Debian is upstream of Ubuntu”.

Downstream
  The opposite of an upstream. Can be used to refer either to a packaged
  version of a specific software project, or the entire distribution where
  that package occurs.


References
==========

* :doc:`strategy`
* :doc:`values`
* :ref:`Feature highlights <launchpad-feature-highlights>`
