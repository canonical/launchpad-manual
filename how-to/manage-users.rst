Manage users and teams in development environments
==================================================

Create new users
----------------

In environments that use the test OpenID provider, such as the development
appserver started via ``make run``, you can create a new account using the
``utilities/make-lp-user`` script and log into that account at
``https://launchpad.test/``.

For example, to add user ``test-user``, navigate to your local Launchpad repo 
and run: ``utilities/make-lp-user test-user``.

Some development environments, such as those deployed using the :doc:`Mojo
spec <../explanation/charms>`, use production Single Sign-On for
authentication.  In these environments, you should not use
``utilities/make-lp-user``; instead, log into 
``https://{qastaging,staging}.launchpad.net/`` via SSO as you would on 
production to create your user.



Add user to a team
------------------
                    
Let's say that we created a new user in the previous section, with the 
following handler ``~test-user``  and we want to add it to a team. In this 
example let's consider that we want to add it to the Launchpad Admins team,
so ``~admins``.

We can use the ``utilities/anoint-team-member`` script within the Launchpad repo
to add a user to a team.
For staging and qastaging we should:

1. Log into ``launchpad-bastion-ps5`` using
the ``stg-launchpad`` user. 

2. Source ``. .mojorc.{qastaging,staging}`` the correct 
environment.

3. Ssh into the scripts unit ``juju ssh launchpad-scripts/leader``.

.. note:: 
     Alternatively, we can merge step 2,3 running this command:
     ``in-model qastaging juju ssh launchpad-scripts/leader``

4. Then we can run: 

.. code::
     
     /srv/launchpad/code/utilities/anoint-team-member <username> <team-name>

In our example:

.. code::
     
     /srv/launchpad/code/utilities/anoint-team-member test-user admins
