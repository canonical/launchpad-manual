==============================
Applying a cowboy to qastaging
==============================

.. note::

    A cowboy is a hotfix applied to an instance, avoiding a proper deployment
    by applying code changes directly on an instance.

.. caution::

    A cowboy is a valuable tool to either apply urgent hotfixes or test things
    quickly e.g. in a staging environment.

    As it avoids a proper deployment, it also comes with a couple of negative
    side effects:

    - a regular deployment overwrites the cowboy

    - the state of the instance is not clearly defined in the current code
      and/or deployment configuration

    - and probably some more reasons

    All in all a cowboy should be applied only in rare and extraordinary
    circumstances.

Before you apply a cowboy, please have a quick conversation with your team
where the reason for the cowboy is thoroughly discussed.

Applying the cowboy
===================

#. SSH into bastion ``ssh launchpad-bastion-ps5`` and switch to the
   ``stg-launchpad`` user by running ``sudo -iu stg-launchpad``.

#. Run ``source ~/.mojorc.qastaging``.

#. Run ``juju config launchpad-appserver build_label`` and take a note of the
   currently applied git commit id.

#. Checkout that commit id locally.

#. Apply the planned changes to your local checkout and create a local patch
   file via e.g. ``git diff > <description>.patch``.

#. Log into the appropriate unit where you want to apply the patch to.
   In this example, we will apply the patch to the application server
   (``launchpad-appserver``). Applying patches to e.g. cronscripts will differ
   as we might not need to restart the application server.

    - Get a list of units you need to apply the patches to. For the application
      server run ``juju status launchpad-appserver``.
      As we run more than one instance, we need to apply the next steps for
      each of the units.

    - ssh into one of the units via ``juju ssh launchpad-appserver/2``

    - Change into the directory with the source code via
      ``cd /srv/launchpad/code``.

    - Apply the patch via ``git apply <description>.patch``.

    - Restart the system via ``sudo systemctl restart launchpad``.

      .. note::

          The restart command occasionally times out. Just run it again until
          it works.

    - As already mentioned, repeat the previous steps for all units to make
      sure all units have your patch applied.


Related information
===================

Applying cowboys to production need to be performed by IS. Checkout the 
`cowboy requests page <https://docs.google.com/document/d/1lxQJJWL2VD3mgCLp-KqDRxPYrhHv-020hn9qd2wL07Q/edit?tab=t.ba9rhn9ws2d5>`__.

