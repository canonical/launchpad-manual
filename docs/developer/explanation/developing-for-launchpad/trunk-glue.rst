.. _branches-trunk-glue:


How the 4 trunk branches and buildbot work together
===================================================

.. include:: ../../../includes/important_not_revised.rst

This page aims to explain the mechanisms that make the wonderful diagrams on the :ref:`about-launchpad-branches` page work. You'll need to read that page for this one to make any sense at all.

There are three main components:

* `Jenkins <https://jenkins.ols.canonical.com/online-services/job/launchpad/>`__ (private) -- this is how changes get into the master and db-devel branches
* `buildbot <https://lpbuildbot.canonical.com/>`__ -- this is what runs the tests.
* buildbot-poll.py -- this script monitors the branches and builds on buildbot and implements much of our policy. 

There is a (currently private) `branch on Launchpad <https://code.launchpad.net/~canonical-launchpad-branches/lpbuildbot/production>`__ that contains the buildbot config and the buildbot-poll.py script.

The buildbot UI is currently also private, but this will change, hopefully soon.

Jenkins
-------

We use the `Canonical Online Services team's Jenkins instance <https://jenkins.ols.canonical.com/online-services/>`__ to process requests to merge branches into either master or db-devel. It is currently private.

At the moment, Jenkins merges any merge proposal that has an Approve vote from at least one Launchpad reviewer, whose status is Approved ("top-approved"), and that has no conflicts against its target branch. It does not run any tests itself, leaving that to buildbot.

Buildbot
--------

Buildbot is our continuous integration tool of choice.

At one level, it's fairly simple: when a change is detected on the master or db-devel branches on Launchpad, the tests are run on that branch and their success or failure noted.

In general in buildbot, a "change source" produces "changes" that are fed to a "scheduler" which can examine the change to determine whether to trigger a build.

The change source we use is the customized version of "GitPoller" in bzrbuildbot/poller.py in the lpbuildbot branch. It is configured with a list of URLs to watch, and when it sees a new revision in one of these branches, it feeds it to buildbot.

The scheduler we use for the two trunk builders is "AggregatingScheduler". An AggregatingScheduler is configured with a branch and watches for changes that affect this branch. When it sees a change that affects its branch, it checks to see if the last build succeeded or failed. If it failed, then it only starts a new build if the commit message contains '[testfix]'.

We have a custom web UI that adds a page that lets you force a build. (Buildbot's built-in "Force Build" button doesn't work for us for rather boring reasons.)

Builds forced using our page have a distinctive "reason" attribute that the buildbot-poll.py script looks for using the JSON API.

buildbot-poll.py
----------------

This script checks the status of the builds (via the JSON API) on buildbot, and may push to the stable and/or db-stable branches depending on what it finds.

For each development branch (i.e., master or db-devel), if the most recent build succeeded, the script pushes the revision of the development branch that was tested into the corresponding stable branch (i.e., stable or db-stable).

It runs out of cron every 5 minutes, on the Patch Queue Manager (PQM) box.
