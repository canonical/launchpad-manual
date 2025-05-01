Monitoring bugs in other bug trackers
=====================================

Look at the "Assigned To" column for `bug
#86103 <https://launchpad.net/bugs/86103>`__ again:

The top two rows don't have a "person" assigned to fix them. Instead,
because they refer to instances of the bug in external communities, they
have a link to that bug as reported in the bug trackers used by those
communities. Launchpad determines the external bug's status by regularly
checking that external bug tracker.

Automatically monitor the status of external bugs
-------------------------------------------------

Open the bug in a new tab in your browser using this link, so you can
interact with it more directly:

   https://launchpad.net/bugs/86103

Mouse over those two links in the "assignee" column and you will see
URLs for the SUN Java and Debian bug trackers respectively:

- https://jdk-distros.dev.java.net/issues/show_bug.cgi?id=20
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=402165

This is one of the unique features of Launchpad. It allows you to track
the status of bugs in external trackers that run Bugzilla, Round``Up,
Sourceforge, the Debian BTS or Mantis. We will add support for
additional trackers, when that becomes necessary to facilitate
collaboration across the free software projects that use them.

This means that projects can leverage the benefits of Launchpad without
giving up their own bug tracker, if they prefer to use their own hosted
infrastructure. In some cases, we import ALL the bugs in a project bug
tracker into Launchpad automatically, because there are other
communities that want to be able to link to them trivially. In other
cases, project members can create those links when they need them.

Bug watches automatically notify Launchpad subscribers
------------------------------------------------------

We call such a link a "Bug Watch" and you can create them for any bug in
Launchpad. When you are telling Launchpad about a bug that affects
another community, simply provide the external bug report's URL and
Launchpad will automatically create the bug watch. If Launchpad doesn't
recognise the external bug tracker it will ask if you want to register
the new tracker at the same time.

Once created, Launchpad will monitor the remote bug report automatically
and notify subscribers to the Launchpad bug of any changes to the status
of the remote bug.

Incidentally, you can subscribe to any bug, and if you are the assignee
or the bug contact for this package or project then you will also be
treated as a subscriber, and hence also notified:

Now, scroll further down the page for `Bug
#86103 <https://launchpad.net/bugs/86103>`__. You may notice that some
of the comments on the bug look like emails. That's because Launchpad's
bug tracker allows you to interact with it completely via email. That's
the next stop on our tour: `the bug tracker email
interface <FeatureHighlights/BugsByEmail>`__.