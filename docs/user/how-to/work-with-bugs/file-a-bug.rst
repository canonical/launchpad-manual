.. _file-a-bug-in-launchpad:

File a bug in Launchpad
=======================

.. include:: /includes/important_not_revised_help.rst

Prior to filing a bug the extra data file needs to be stored in
Launchpad. This can be done via the page
`<https://launchpad.net/+storeblob>`_. Upon successful storing of the file a
token will be provided both within the page and contained in the HTTP
headers as ``X-Launchpad-Blob-Token``.

Filing a bug can be achieved by accessing the page
``https://launchpad.net/bugs/+filebug/<token>`` replacing ``<token>`` with the token
received previously. However this page requires the user to specify the
Distribution/Package or Project. An alternative is to use the URL syntax
``https://bugs.launchpad.net/<distribution>/+source/<package>/+filebug/`` or
``https://bugs.launchpad.net/<project>/+filebug/`` replacing ``<distribution>``, ``<package>``, ``<project>`` as appropriate.

The process after this point is the same as filing a bug normally except
that certain fields may be pre-populated.

Getting started
---------------

When you :ref:`registered your project <how-to-register-your-project>` in
Launchpad, you had the option to specify where its bugs are tracked. If
you chose an option other than ``Bugs are tracked in Launchpad``, you
now need to activate the Launchpad bug tracker for your project.

Follow the ``Change details`` link on your project's overview page.

You can also choose whether Launchpad should automatically expire
inactive bugs. There's more on what Launchpad considers an inactive bug
in our article on :ref:`bug-expiry`.

Importing your existing bug history
-----------------------------------

In some cases, the Launchpad team can import your existing bug history
from another bug tracker. This may mean you can switch to Launchpad's
bug tracker without having to maintain your previous bug tracker in a
read-only mode.

:ref:`Get in touch <get-help>` to see if we can help.

Setting roles
---------------

- A bug supervisor handles day to day management and triage

Many projects :ref:`create specific teams <creating-and-running-launchpad-teams>` to act as
the bug supervisor, allowing several people to triage bugs without gain.

If you'd prefer not to set these - perhaps because your project is small
enough not to need specific contacts - you, as project owner, take them
by default.

The bug supervisor's role
~~~~~~~~~~~~~~~~~~~~~~~~~

You may want to give some people extra bug editing privileges: The bug
supervisor's role is to manage the planning of bug work and the triage
of newly reported bugs.

Launchpad helps them do this by giving them access to:

-  target bugs to a milestone
-  set the importance of a bug
-  set certain :ref:`bug statuses <old-unattended-and-incomplete>`.

To set your project's bug supervisor, visit its bug overview page - for
example: https://bugs.launchpad.net/inkscape - then choose the edit link
next the the bug supervisor role listed on the page.

Next step
---------
Now you've set up the basics, you're ready to start managing your
project's bug reports in Launchpad. However, let's first look at how
Launchpad :ref:`tracks the hottest bugs <bug-heat>`.
