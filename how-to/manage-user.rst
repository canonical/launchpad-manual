Manage users and teams in development environments
==================================================

Create new users
----------------

In environments that use the test OpenID provider, such as the development
appserver started via ``make run``, you can create a new account using the
``utilities/make-lp-user`` script and log into that account at
``https://launchpad.test/``.

Some development environments, such as those deployed using the :doc:`Mojo
spec <../explanation/charms>`, use production Single Sign-On for
authentication.  In these environments, you should not use
``utilities/make-lp-user``; instead, log into ``https://launchpad.test/``
via SSO as you would on production to create your user.

Add user to a team
------------------
                    
Let's say that we created a new user in the previous section, with the 
following handler ``~test-user``  and we want to add it to a team, in this 
example let's consider that we want to add it to the Launchpad Admins team,
so ``~admins``.

We will use ``utilities/anoint-team-member`` script to add it to teams.
For staging and qastaging we should log into ``launchpad-bastion-ps5`` using
the ``stg-launchpad`` user. Then ``. .mojorc.{qastaging,staging}`` the correct 
environment and ssh into the scripts unit ``juju ssh launchpad-scripts/leader``.

Then we can run: 

.. code::
     
     LPCONFIG=launchpad-admin /srv/launchpad/code/utilities/anoint-team-member <username> <team-name>

In our example:

.. code::
     
     LPCONFIG=launchpad-admin /srv/launchpad/code/utilities/anoint-team-member test-user admins
