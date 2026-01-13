.. _the-launchpad-bug-tracker:

The Launchpad bug tracker
=========================

.. include:: /includes/important_not_revised_help.rst

This document describes the extra data interface to
the bug tracker in Launchpad that can be used by bug reporting tools
such as `Apport <https://launchpad.net/Apport>`__. If you have questions
or comments about this document, please `reach out to us <get-help>`.

Overview
--------

Launchpad's bug tracker is unique: it can track how one bug affects
different communities.

When you share free software, you share its bugs. This means that free
software bugs may be reported in one project but originate in another
entirely, whilst affecting several more.

Launchpad handles this by making every bug available to every project
and distribution that uses the bug tracker. Rather than treating each
project as an island, with an isolated list of bug reports, Launchpad
allows interested groups to work together in search of a fix.

`Bug 98275 <https://bugs.launchpad.net/zope3/+bug/98275>`__ is a great
example. It is one bug report, with one bug number, but it has a
different status, importance and assignee in each context.

This table appears at the top of the bug report, showing that it affects
three projects and different series (lines of development towards a
release) within those projects. In this case, each of the affected
projects uses Launchpad's bug tracker. However, Launchpad can just as
happily monitor the progress of the same bug in external trackers, as
shown in `bug
122590 <https://bugs.launchpad.net/ubuntu/+source/gnome-panel/+bug/122590>`__.

Here, the bug report in Launchpad is about Ubuntu's package of the Gnome
Panel. However, there's also a link to the bug as tracked in Gnome's
Bugzilla, along with its status there. This lets the Ubuntu desktop bugs
team monitor the progress upstream and implement their fix when it

The bug tracker provides an extra interface for filing bugs. By
uploading a specifically formatted file to Launchpad prior to filing a
bug, data and fields contained in the file will be incorporated into the
bug during the filing process.

This file can be used to provide additional information like logs, dumps
and command outputs to bugs without burdening the users with finding and
uploading the relevant files/details.

File Format
-----------

The file containing the extra data should be a MIME multipart message.
The bug tracker uses the Content-Disposition to determine how to handle
each part.

Fields
~~~~~~

By placing certain fields in the header of the file, some initial values
and the behaviour of the filed bug can be determined prior to filing it.

::

   Subject: bar crashes foo

This will be used to populate the suggested title for the bug.

::

   Tags: foo bar

The filed bug will be tagged with supplied tags.

::

   informationtype: privatesecurity

The filed bug will be marked as private security (only the project's
trusted people will see it).

::

   Subscribers: launchpad-user user@example.com

The specified Launchpad users and/or registered e-mail addresses will be
subscribed to the filed bug.

Parts
~~~~~

The first part with a Content-Disposition of ``inline`` will be appended
to the bug description after it is filed.

Additional parts that have a Content-Disposition of ``inline`` will
become comments for the filed bug.

Parts with a Content-Disposition of ``attachment`` will have have their
contents added as attachments to the filed bug.

Sample File
~~~~~~~~~~~

::

   MIME-Version: 2.0 
   Content-type: multipart/mixed; boundary=boundary
   Subject: Initial bug summary
   Tags: foo bar
   Private: yes
   Subscribers: launchpad-user user@example.com

   --boundary
   Content-disposition: inline
   Content-type: text/plain; charset=utf-8

   This should be added to the description.

   --boundary
   Content-disposition: inline
   Content-type: text/plain; charset=utf-8

   This should be added as a comment.

   --boundary
   Content-disposition: attachment; filename='attachment1'
   Content-type: text/plain; charset=utf-8

   This is an attachment.

   --boundary
   Content-disposition: inline
   Content-type: text/plain; charset=utf-8

   This should be added as another comment.

   --boundary
   Content-disposition: attachment; filename='attachment2'
   Content-description: Attachment description.
   Content-Transfer-Encoding: base64
   Content-Type: application/x-gzip

   H4sICH5op0UAA3Rlc3QudHh0AAvJyCxWAKLEvPySjNQihcSSksTkjNzUvBIdhfLMkgyFRIWU1OLk
   osyCksz8PD0uAPiw9nkwAAAA

   --boundary--

Launchpad Bug Tracking Highlights
---------------------------------

This is a brief introduction to the use of Launchpad for bug tracking.
It examines the unique features of the Launchpad bug tracker, which may
not be familiar to folks who have extensive experience with other bug
trackers like Bugzilla.

Cross-Project Collaboration
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Launchpad is a **platform for collaboration** - and crucially, that idea
extends to collaboration **between** projects as much as it covers
collaboration **within** projects. So Launchpad is designed to make it
easy to keep track of bugs within a project, and when necessary to let
completely different projects collaborate on fixing a particular issue.

Very often, projects themselves have very good bug trackers, and good
communities all of whom know the internal policies and practices of the
project (and of course all of whom already have the relevant accounts in
the bug tracker) to be able to collaborate with one another. But as soon
as an issue affects outsiders - people from other communities - there
are barriers to their ability to collaborate with one another. If I find
a bug in X.org, for example, I need to go and get an account on the
X.org bug tracker to be able to report it. That represents a
disincentive to my participation, and many bugs go unreported as a
result.

More importantly, there are often different and distinct communities
that work on the same codebases. Consider the Apache web server - there
is an "upstream" community that works on it, and of course there are
also many distro-specific teams that patch Apache. Launchpad is designed
to make it easy for those disparate groups to collaborate.

An example will help to make this clear.

* John is working on a new Plone product, Weathervane, which is supposed to
  make it easy to integrate Google Maps and weather data with Plone sites so
  that you can easily see whether your users are in general having a sunny day.

* He finds that a part of Plone is not working as expected when he uses a
  particular pattern of arguments to a Plone method, so he files a bug on
  Plone in Launchpad. The Plone community realise that they can reproduce
  the issue in Zope2, so they link the same bug to Zope, in Launchpad.
  And the Zope community then track it down as a bug in Python itself,
  so they record the bug as also occurring in the Python product in Launchpad.

* The same bug is now open in three places: Plone, Zope and Python.
  This means that three different projects are tracking the same bug.
  Anybody looking at the list of bugs in Plone, or Zope, or Python,
  will see this bug. And anybody from any of those projects who has
  further information can comment, add attachments etc, without needing
  any special new account. A comment made by any person is sent to the
  subscribers and assignees on the bug from  *all* of those projects.
  Essentially, a inter-project team has been formed to fix the bug.

* The moment this bug is marked fixed in *any* of these projects, developers
  from all of them will be notified. So awareness of a bug fix can propagate
  more quickly between projects - for example, from Ubuntu to Plone, or to Python.

* The idea is ensure that eyeballs that are all interested in a particular issue
  can be aggregated and can work together without having to go to any great trouble
  to do so. Each of these different projects - Ubuntu, Plone, Zope and Python may have
  their own sense of the priority of a particular issue, but if any of them fix it, or
  start work on a fix for it, the others can at least be aware of that progress.

Email Commands and Comments
~~~~~~~~~~~~~~~~~~~~~~~~~~~

An email interface to the Launchpad bug tracker lets you stay
productive, working through email, reviewing bug comments, updating bug
statuses and adding attachments to bugs. You can even report bugs
directly using the email interface.

Almost any operation - from marking a bug closed, to passing a bug
"upstream", to changing any tag or description or attribute of the bug,
can be done through the email interface. This makes developers extremely
productive, especially when combined with distributed revision control
which lets developers work entirely offline while still maintaining
version control integrity.

See UsingMaloneEmail for details of how you can use email to triage and
manage bugs.

Integration with existing bug trackers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Many projects have their own Bugzilla, or use SourceForge for bug
tracking. These projects can still get some of the collaborative
benefits of Launchpad's cross-project bug tracking, because of a feature
known as "bug watches". Essentially, it is possible to tell Launchpad
that a particular bug is also being tracked in, say, a particular bug
number of a Bugzilla instance. Launchpad can then monitor that Bugzilla
report, and provide notifications to the people subscribed to the
Launchpad bug when something changes in the remote bug tracker.

So, for example, if you have a bug in Python being tracked in Launchpad,
and someone realises that the same bug has been reported in the Red Hat
Bugzilla, it is trivial to create a bug watch linking the Launchpad bug
report to the Red Hat Bugzilla report. If Red Hat marks the bug fixed,
then the Python community that is tracking this bug in Launchpad will
immediately receive an email notification of the change, and it will be
reflected on the Launchpad bug page too. That means that a member of
upstream immediately knows who to talk to at Red Hat about bring the fix
into the mainline.

These bug watches are integrated into Launchpad's usual mechanism for
tracking a single bug in multiple places. You can link a bug's status to
a watch, in effect saying that "this bugzilla report documents the state
of the bug for this product in Launchpad". So you can integrate the work
of other projects that are using totally separate infrastructure. Of
course, there is some loss of information, so projects that need to
collaborate closely are still better off both using Launchpad, but if
you need to collaborate with another project that has their own
infrastructure then Launchpad can still make that as easy as posible.

At the moment, Launchpad will only monitor remote bug status changes. In
future, Launchpad will also bring remote bug comments into the Launchpad
bug comment pool, so that subscribers to a Launchpad bug can follow
conversations going on in other bug trackers too (though they will not
trivially be able to reply unless they create accounts for themselves in
those remote bug trackers).

Security and privacy workflow
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Launchpad makes it easy to identify bugs that are security-related, and
deal with them appropriately. It also lets you mark bugs as private, and
ensure that only trusted people can see the bug details.

You can visit your project's Sharing page to share all "Private
Security" information with team you trust to work with security bugs and
branches. The members of the teams can choose to subscribe to bug email
and add a filter to get just "Private Security".

The collaborative nature of Launchpad is very useful for dealing with
security bugs, because such issues often impact on multiple projects.
For example, if a security issue arises in a commonly-used shared
library, such as zlib, Launchpad allows one to create tasks for the bug
on each of the projects that are affected, and privately to have a
conversation with all of them, keeping track of their individual
progress in addressing the issue before a public announcement is made.

CVE Integration
~~~~~~~~~~~~~~~

CVEs are a standard registry of security vulnerabilities, so they can be
tracked across multiple operating systems.

Launchpad can be told which CVE reports apply for a particular issue,
and can then help you keep track of which CVE issues are addressed or
not yet addressed for your project. The CVE tracking and reporting
features of Launchpad are simple, but nonetheless useful if security
reporting and audit are important to you.

Linking to feature specifications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Launchpad bug tracking is also integrated with other parts of Launchpad.
For example, Launchpad includes a system for planning features and
charting the course of development. Sometimes, users will report
"wishlist" bugs related to features that are planned - and Launchpad
makes it easy to link those bugs to the relevant feature requests. This
makes it easy for people working on the feature to keep track of
relevant bug reports, and of course lets the people who reported those
bugs keep track of changes to the specification of the feature.

Teams
~~~~~

Launchpad has quite a sophisticated team management system. This lets
you create arbitrary teams of people (and even teams of teams, for
finely structured management of diverse but related groups). You can
treat a team just like a person - which means you can assign bugs to
teams, or have a team be the "bug supervisor" for your project.

This turns out to be a very neat way to handle bugs. We have seen how
projects tend to form appropriate teams very quickly, and use the "teams
of teams" approach to aggregate them and to delegate team management to
the leaders of subteams. Typically, QA folks assign a new bug to a
relevant team, and someone on the team then claims the bug for
themselves. In this way people aren't arbitrarily made the assignee for
bugs they did not select themselves, but there is still a general sense
of the "group that is likely to want to fix this".

Planned Features
----------------

Some features of the Launchpad bug tracker are not yet complete, but
should be in place by the end of the year. I will discuss three of them
in particular. The list of planned features itself can be found here:

     https://launchpad.net/products/malone/+specs

Branch integration
~~~~~~~~~~~~~~~~~~

Launchpad can be used to keep track of development being done by your
community on multiple independent branches.

If they register their branches with Launchpad, and in doing so note that they 
are working on a particular bug in that branch, then Launchpad will notify the 
other subscribers to the bug that the branch exists and is being worked on. 
This allows people who have an interest in the bug either to pitch in and 
collaborate on the bug fix directly, or simply to know that they can find a fix
by merging from the relevant branch.

Release management
~~~~~~~~~~~~~~~~~~

Launchpad understands that projects want to keep track both of
"mainline" development, and of specific releases. It allows you to
manage your bugs with that in mind.

Launchpad has a general mechanism to describe the overall structure of
the project:

- The **product** is the overall application or library. For example,
  :literal:`you will find products registered in Launchpad for Python, Zope, PyCrypto, Firefox, etc.`

- A **series** is a "series of releases" and generally represents a:

  - single line of development from which several releases might be made.
  - In the case of Python, you would expect to find a series for each of Python 2.3, Python 2.4, Python 2.5 etc.

Sometimes, a series represents "trunk" development, and sometimes it
represents a "stable release series". So I would also expect to find a
series for "Python trunk". The product can be told which series
represents the current "mainline" or "trunk". In many cases there is an
explicit branch which represents trunk all the time, but some products
tend to "leap from series to series" rather than having a trunk from
which they branch. For example, the old Linux kernel used to have "odd
numbered branches" which were "trunk" when they were the focus of
development, with "even numbered branches" representing stable release
series.

In general, all bugs are filed against the product and you can consider
those to represent "mainline". That's like saying "this is a bug in
Python, please fix it someday". But just as you can record that a bug
needs to be fixed in different places (upstream, and in downstreams that
depend on the same code, and in distributions which package the code)
and keep track of each of those "bugs" individually, you can also make a
note that a particular bug needs to be fixed in a particular series.

This is like saying "yes, this bug in Python needs to be fixed in this
specific release series". We call this "targeting a bug to a series" and
it can be used either for release management of the **next** stable
release, or to manage the decisions with regard to the backporting of
fixes to previous stable releases.

For example, say the project is working towards a stable release 1.2,
and a bug is reported that is judged by the release management team to
be one they want to ensure is fixed in version 1.2 (rather than getting
fixed later on). They can then target the fix to the 1.2 series, and it
will then appear both on general "product bug reports" and on the
specific "1.2 release management bug reports" listings. This allows the
1.2 release management team to manage their list of bugs that they hope
to address in the 1.2 release entirely separately from the general list
of bugs.

Now, imagine that it turns out that the bug is quite a significant
security issue. The team might think that the fix needs to be backported
to a previous release, so they could propose that it also be fixed in
the 1.0 and 1.1 series, which are still considered stable. In a very
large project, you could have different people responsible for
maintaining stable releases, so they would see that the bug had been
proposed for backporting and might choose either to accept or decline
it. If they accept it, then the bug will show up on the listing of open
issues on 1.1 and 1.0.

We expect Launchpad's release management bug features to be complete by
the end of October 2006.

XML-RPC interfaces
~~~~~~~~~~~~~~~~~~

Launchpad will support a full set of XML-RPC interfaces which will allow
you to read and write any data which you might have access to through
the web interface, programatically. We are committed to making any data
you can read or write through the web interface also accessible via
XML-RPC. This will have several benefits:

-  **No lock in.** You can extract all of your data from Launchpad

``without having to resort to screen scraping.``

-  **Integration with other systems.** To the extent that you have your

| ``own infrastructure for managing some of the things that Launchpad tracks,``
| ``you can integrate that with Launchpad behind the scenes.``

-  **Improved reporting and display.** If you prefer to list items in a

| ``different way, or to integrate listings of bugs etc on your web site rather``
| ``than point folks at the relevant pages on Launchpad, you can easily do so``
| ``while using Launchpad as a safe repository of the data.``

-  **Custom processes.** If you want to add additional data, say, to the

| ``bug tracker you can design your own bug reporting tool, capture the``
| ``relevant data and then store it all conveniently in Launchpad.``

The bug tracker is a primary focus area for us w.r.t. the XML-RPC
interfaces. We expect the first version of these to be available before
October 2006 and the API to mature over the course of the next year. We
will also publish client libraries for Python applications that wrap the
XML-RPC interface in a good Pythonic API.

The existing XML-RPC interface we have is documented at
:ref:`MaloneXMLRPC <malone-xmlrpc-interface>`; check it out for details.

Known issues
------------

Currently any errors within the extra data file are ignored with no
feedback provided.
