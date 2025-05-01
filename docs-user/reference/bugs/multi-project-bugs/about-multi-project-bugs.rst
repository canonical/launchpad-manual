Multi-project bugs
==================

As we saw in the `introduction <Bugs/YourProject>`__ to the bugs section
of this user guide, Launchpad's bug tracker is special.

Launchpad can track how the same bug affects different communities, such
as free software projects or Linux distributions.

Each community shares the same bug number, report and comment history.
However, they can keep track of how the bug affects them and how they
plan to deal with it by setting their own `status <Bugs/Statuses>`__,
importance and assignee for each bug.

In effect, those communities come together and form an ad-hoc community
around the bug report. This is ideal for free software projects who rely
on code maintained by other communities.

Working with multi-project bugs
-------------------------------

Bugs affecting more than one community is a natural part of life in the
free software world. That's why Launchpad makes handling multi-project
bugs natural and effortless.

At the top of each bug report in Launchpad is a table that shows you
which communities are tracking that bug.

\||<tablestyle="font-size: 0.8em; background:#F1F1ED; margin: 1em 1em
1em 0;" style="padding:0.5em;">|\|

To tell Launchpad that the bug also affects your project, use the link
directly below the table. It's a simple as that.

As soon as Launchpad knows that you also want to track that bug, the
report shows up just like any other bug reported against your project.
The difference is that the bug has become much shallower than if your
bug tracker treated your project like an island.

Now it's not just people interested in your project who are looking for
a fix: it's people from every project that's tracking the bug in
Launchpad!

Bugs in external trackers
-------------------------

Of course, not every project that you work with uses Launchpad's bug
tracker.

Just as you can share a bug report with other projects inside Launchpad,
you can also monitor how other projects are tracking that same bug
outside of Launchpad.

Let's take a look at `an
example <https://bugs.launchpad.net/ubuntu/+source/mozilla-thunderbird/+bug/24220>`__.

\||<tablestyle="font-size: 0.8em; width:30%; background:#F1F1ED; margin:
1em 1em 1em 0;" style="padding:0.5em;">|\| \||<style="text-align:
center;">\ **Bugs in Ubuntu, Debian and upstream**\ \|\|

Here, the bug is tracked directly in Launchpad by the maintainers of the
Ubuntu Mozilla Thunderbird package. However, Launchpad is also importing
status information about the bug from two external bug trackers: Debian
BTS, for the Debian Thunderbird package, and Bugzilla for the upstream
Thunderbird project.

Watching externally tracked bugs is just as easy as marking a bug as
affecting multiple projects within Launchpad. Follow the link below the
table and choose the relevant project.

{i} **Note:** even though the project uses an external bug tracker, the
project must be `registered <Projects/Registering>`__ in Launchpad.

External trackers that Launchpad supports
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Launchpad can link to and, in most cases, import the status of bugs
reported in the following external trackers.

\|\| **Bug tracker** \|\| **Import status?** \|\| \|\| Bugzilla \|\| Yes
\|\| \|\| Debian BTS \|\| Yes \|\| \|\| Trac \|\| Yes \|\| \|\|
Sourceforge \|\| Yes \|\| \|\| Mantis \|\| Yes \|\| \|\| RT \|\| Yes
\|\| \|\| Savane \|\| Coming soon \|\| \|\| Gforge \|\| Coming soon \|\|
\|\| Git``Hub \|\| Yes \|\|

To ensure ease of use and consistency, Launchpad translates the statuses
used by external trackers.

Further information
-------------------

There's a table of the translations that Launchpad makes, along with an
explanation of Launchpad's approach to `bug statuses <Bugs/Statuses>`__.
