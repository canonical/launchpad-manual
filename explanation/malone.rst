============
About Malone
============

.. include:: ../includes/important_out_of_date.rst

The world has many excellent bug tracking tools already. It would not make
sense to create another bug tracker unless the vision behind that software
was substantially different to anything that had gone before it. This
document outlines that vision, explaining what it is that I hope Malone will
do for the open source community.

The Vision behind Malone
========================

Malone is a unified bug tracker for the entire open source world. It is
designed to allow the whole open source community to collaborate on software
defect management, especially when a single piece of code is being used
across many projects. Malone presents a single page which gathers together
the combined wisdom and knowledge of the open source world regarding a
specific software defect.

Upstream and Distributions
==========================

A unique feature of Malone is that it understands the structure of the open
source community::

  Software is developed by individuals or groups with a common interest in a
  specific problem. We call this group "upstream". That software is
  distributed in its pristine state ("tarballs", usually) and is usually
  designed to be compiled and run on a variety of platforms.

  However, most people who use that software will not get it directly from
  upstream, build it and install it locally. They will install a package
  that has already been prepared for the specific platform they are running
  on. For example, on Gentoo, they will type "emerge foo". On Ubuntu, they
  would type "apt install foo". And on RedHat they would install a
  custom RPM. So the same software code is being repackaged many times, for
  Gentoo, Ubuntu, RedHat, and many other platforms.

A natural consequence of this repackaging is that a bug in that software
might be detected and/or fixed by a variety of different people, without
upstream being aware of either the bug or the fix. In many cases, the people
doing the repackaging have entirely separate bug tracking tools to upstream,
and it is difficult for them to pass their information and patches to
upstream directly.

Malone explicitly tracks the status of a bug both upstream and in any
distributions registered in Launchpad. This makes it possible, for
example, to see immediately if a fix has been found for a given bug by any
of the participating distributions, or upstream. The bug page shows this
information very prominently.

Watches
=======

It's unlikely that the whole world will shift to Malone. Many larger
projects have their own bug tracking tools (Bugzilla, Sourceforge and
Roundup are commonly used) and some have even created custom tools for this
purpose. For that reason, Malone supports BugWatches. A BugWatch is a
reference to a different bugtracker that is tracking the same bug. Of course
it will have a different bug number in that system, and the integration
between Malone and that remote bug system is possibly limited, compared to
the richness of the Malone data model, but this still allows us to keep
track of a bug in a different bug tracker. For example, a bug in the Firefox
package on Ubuntu would be tracked in Malone. If the same bug has been
identified upstream, it would be recorded in bugzilla.mozilla.org, and we
would create a BugWatch in the Malone bug pointing at that upstream bug.

Email Integration
=================

It's important that Malone be usable entirely in email. Many open source
developers use their email to track work that needs to be done. So all of
Malone's features should be accessible via email, including changing the
status of a bug, adding and updating watches, and possibly also requesting
reports of bugs on a product or distribution.

Distribution Bugs
=================

Malone is designed to track bugs upstream, and in distributions. The
requirements for a distribution bugtracker are somewhat specialised. A
distribution consists of many source packages and binary packages, and it
must be possible to track bugs at a fine level of granularity such as at the
source/binary package level.

Malone allows us to create bugs that belong only to a distribution, or to a
sourcepackage in a distribution if we have that information. Bugs that are
not associated with a sourcepackage can be thought of as "untriaged" bugs.
In some cases, we should be able to know not only which source package, but
also the precise binary package that manifests the bug.

Milestones and DistroSeries
===========================

In addition, it's important to be able to know which bugs need to be fix for
a given release of the distribution, or a given milestone upstream. Malone
allows us to specify a milestone or a distroseries by which a bug needs to
be fixed, which allows QA teams to keep track of the progress they are
making towards a release.

Version Tracking
================

One very difficult problem faced by support teams in the open source world
is that users may not all be running the latest version of a piece of code.
In fact, that's pretty much guaranteed. So Malone needs to be able to say
whether a bug is found in a particular version of a package or not.

Future
======

Bazaar Integration
------------------

Malone is part of Launchpad, a web based portal for open source
developers. Another component of that portal is the Bazaar, a repository of
data and metadata about code stored in the Bazaar revision control system. We
hope that Bazaar will be embraced by the open source world, as it solves a
number of problems with traditional centralised revision control systems and
is again designed to support distributed disconnected operation.

Once more people start keeping their code in Bazaar, it should become possible
to streamline the cooperation process even further. For example, if the fix
for a particular Malone bug can be found in a Bazaar changeset, then it should
be possible for upstream and other distributions to merge in that fix to their
codebase automatically and easily. The integration could even be
bidirectional - once a fix had been merged in, Bazaar could possibly detect
that and mark the bug fixed in that codebase automatically.


