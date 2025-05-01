================
Launchpad values
================

Whenever we are thinking about what Launchpad should be, or how we should
implement a change, or whether something is a good idea or not, we have
recourse to three distinct sets of guidelines.

The first is :doc:`strategy`, which reminds us why we are making Launchpad and
helps us answer questions such as "How does this help Launchpad meet its
goals?".  The second is :doc:`scope`, which helps us answer questions like "Is
this in scope?".  Together, they sort out the 'matter' of Launchpad.

The third is this document, the Launchpad Values.  It tries to address the
'manner' of Launchpad.  It, perhaps, will not answer specific questions for
you.  Rather, it will rule out certain options and decisions before they are
even considered.

Like the :doc:`strategy`, this document is living: it should be changed and
improved as we learn more about how to make Launchpad.  It is also
aspirational: not all of Launchpad lives up to these values.


Better tools help
=================

Launchpad is fundamentally based on the principle that improving the tools
that we use to make things will help us make better things than we could
before and indeed make better things more cheaply than we could before.

Launchpad should be that "better tool" and be always aiming to smooth and
accelerate the process of making software.


Invisible.  If not, fun.
========================

Launchpad is a tool to help busy people get important stuff done.  It should
stay out of the way where possible.  Bugs, OOPSes, downtime and slowness all
draw attention to Launchpad and away from the interesting problems that our
users are trying to solve.

Where it is not possible to stay out of the way, Launchpad should be fun to
use.  We make next actions obvious and draw attention to users' achievements.


Example
-------

When a branch is merged into the trunk of a project, that's generally the end
of its story.  Launchpad quietly and silently detects that it has been merged
and marks the branch and any merge proposals as such.  The branch then no
longer appears on default listings.


Reveal opportunities
====================

One of the grand things about open source software is that it is open to
contributions from total strangers.

Launchpad makes those contributions possible by removing as many barriers as
possible to contribution, and highlights areas where contributions would be
especially welcome.

Example
-------

When you click the Translations tab of a project that's translatable, you see
a list of all of the languages you speak, together with a progress bar telling
you how much translation work is available.  You can click a language and
start translating right away.


Not our data
============

The data in Launchpad does not really belong to us, we are merely its
stewards.  We make sure that users can get their data easily and that they can
change it as they see fit.

Example
-------

You can access almost all of the data in Launchpad through the RESTful APIs.


Not just their data
===================

The data people store in Launchpad doesn't just belong to them, though.  It
also belongs to the wider open source community.  The data needs to be used to
link between other projects, and to allow Launchpad to act as a front-end of
open source.

Example
-------

Someone who is not actually a maintainer of a project might register that
project on Launchpad so they can import code or synchronize bugs or so forth.
If the project's actual maintainer comes along and wishes to take it down, we
will *not* do so.


Cross-project consistency
=========================

If you know how to contribute to one project on Launchpad, you ought to be
able to quickly and painlessly contribute to any other project on Launchpad.
Or, if you can't, it won't be Launchpad's fault.

Example
-------

You can get the trunk branch for any project with 'bzr branch lp:project', or
the source for any Ubuntu package using 'bzr branch lp:ubuntu/project'.


All of open source
==================

Any open source project ought to be able to host itself on Launchpad.  We do
not enforce workflows, rather we allow people to fit their project's existing
workflow into Launchpad.

However, when we can, we encourage people toward best practices.  After all,
we want to make open source software better.

Example
-------

Launchpad separates whether or not a reviewer approves of code from whether or
not a branch is approved to land.


All users are potential contributors
====================================

One of the glories of open source is that any user is a potential
contributor.  Launchpad guides new users toward the ways where they can begin
to contribute.


Close the loop
==============

Something magical happens when a feature or a workflow reaches all the way
back to where it began.  The feature begins to reinforce itself, and make
things possible that weren't possible before.

Another way of thinking about this is that the value is in the output, and
Launchpad is always concerned with the output of all of its features.

Example
-------

These are examples of where we aren't there yet.

Being able to attach patches to bugs is great, but it's not good enough until
developers can easily *find* those patches.  Finding the patches is only good
enough when you can merge, comment and reject those patches.

Likewise, importing translations from an upstream is great, but it becomes
much, much better when those translations can be improved in Launchpad and
then sent back to the upstream.


References
==========

* :doc:`strategy`
* :doc:`scope`
