Creating additional user accounts in the development environment
================================================================

In environments that use the test OpenID provider, such as the development
appserver started via ``make run``, you can create a new account using the
``utilities/make-lp-user`` script and log into that account at
``https://launchpad.test/``.

Some development environments, such as those deployed using the :doc:`Mojo
spec <../explanation/charms>`, use production Single Sign-On for
authentication.  In these environments, you should not use
``utilities/make-lp-user``; instead, log into ``https://launchpad.test/``
via SSO as you would on production to create your user, and then use
``utilities/anoint-team-member`` as needed to add yourself to teams.  For
example, you might want to temporarily add yourself to the ``admins`` team
in order to edit feature rules.
