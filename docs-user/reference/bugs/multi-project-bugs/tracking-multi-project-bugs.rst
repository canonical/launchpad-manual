Tracking bugs across multiple projects
======================================

Launchpad's bug tracker is unique in that it allows you to track the
status of **the same bug as it affects multiple different communities**.
This gives you a one-page overview of the work that is ongoing in all of
those communities to engineer a fix to the problem.

Bugs that affect multiple communities
-------------------------------------

Here's an example:

`` ``\ https://launchpad.net/bugs/86103

The screen-shot shows that this bug currently affects at least three
communities:

-  Java upstream
-  Debian
-  Ubuntu.

In Ubuntu's case, the bug has been recorded in two places: the sun-java5
and sun-java6 packages.

Each row in this table corresponds to a "place" where the bug has been
detected, and so needs to be assessed and possibly fixed.

At the highest level, a "place" is a community, such as an upstream
project or a distribution. There are also specialised types of place,
which offer a finer level of granularity: for example, a major version
of an application or a specific package within a distribution.

Several occurrences of the same bug in one project
--------------------------------------------------

It's possible for a bug to appear in many places in the same project.
For example, this bug affects fifteen different packages in Ubuntu:

`` ``\ https://launchpad.net/bugs/85124

You can see that the issue has now been addressed in all packages. As a
team works on a bug like that, they will fix different packages at
different times. The bug page provides a useful overview of the real
work still required before the bug can be considered to be fixed.

Fixing bugs in previous versions of software
--------------------------------------------

Sometimes, a bug is severe enough that you need to fix it in previous
versions of the software, perhaps as a security fix or an update to the
stable and supported releases.

Here's an example of a bug that was deemed important enough to go back
and fix in Dapper and Edgy (two previous releases of Ubuntu):

`` ``\ https://launchpad.net/bugs/81782

Note that this bug needed to be fixed in two packages: in the current
development release and two stable releases of the distribution. This
gives us a total of six rows in the table.

It's clear, however, that many of the projects we need to collaborate
with already have their own bug trackers, and many will continue to use
those rather than adopt Launchpad. How can we coordinate with them? That
takes us to the next step in our tour - `monitoring bugs in other bug
trackers <FeatureHighlights/BugWatches>`__.