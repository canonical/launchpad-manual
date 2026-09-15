.. meta::
   :description: Use Launchpad's qastaging environment to experiment with real 
      data and functionality without affecting production.

.. _qastaging-environment:

Qastaging — Launchpad's sandbox
===============================

If you want to try Launchpad out, you can use the `Qastaging environment
<https://qastaging.launchpad.net/>`_ to experiment with real data and
functionality, but without affecting the day-to-day work of other
Launchpad users.

However, there are a few things to note about staging:

-  Qastaging's database is replaced with a fresh snapshot of
   Launchpad's production database: you will lose anything you do on
   qastaging. The update is ran manually.
-  Qastaging runs the latest bleeding edge code from the Launchpad
   developers — if things go wrong, please `let us
   know <https://bugs.launchpad.net/launchpad/+filebug>`__.
-  You can't create a new account on qastaging — instead, create one in
   Launchpad's production environment and then wait up to 24 hours for
   your account to be available on qastaging.
-  Timing interactions with SSO environment syncing and Launchpad
   environment syncing may mean you need the help of a Launchpad
   administrator to manually link up your account the first time
-  Qastaging does not send email.
-  You can upload translations and templates but not export them —
   uploaded translations/templates will disappear after 24 hours.
-  You can push code to qastaging.

