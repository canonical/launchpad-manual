Staging — Launchpad's sandbox
=============================

If you want to try Launchpad out, you can use the `staging environment
<https://staging.launchpad.net/>`_ to experiment with real data and
functionality, but without affecting the day-to-day work of other
Launchpad users.

However, there are a few things to note about staging:

-  Every 7 days, staging's database is replaced with a fresh snapshot of
   Launchpad's production database: you will lose anything you do on
   staging. The update is scheduled to happen on Saturdays. See `Update
   logs <https://staging.launchpad.net/successful-updates.txt>`__
-  Staging runs the latest bleeding edge code from the Launchpad
   developers — if things go wrong, please `let us
   know <https://bugs.launchpad.net/launchpad/+filebug>`__.
-  You can't create a new account on staging — instead, create one in
   Launchpad's production environment and then wait up to 24 hours for
   your account to be available on staging.
-  Timing interactions with SSO environment syncing and Launchpad
   environment syncing may mean you need the help of a Launchpad
   administrator to manually link up your account the first time
-  Staging does not send email.
-  You can upload translations and templates but not export them —
   uploaded translations/templates will disappear after 24 hours.
-  To push code branches to staging you need use bzr push
   lp://staging/~your-id/branch-name.

If you don't need particularly up-to-date data, then there is also `the
qastaging environment <GetInvolved/BetaTesting>`__.
