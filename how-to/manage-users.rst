Manage users and teams in development environments
==================================================

Create new users
----------------

Local
~~~~~

In environments that use the test OpenID provider, such as the development
appserver started via ``make run``, you can create a new account using the
``utilities/make-lp-user`` script and log into that account at
``https://launchpad.test/``.

For example, to add user ``~test-user``, navigate to your local Launchpad repo 
and run: ``utilities/make-lp-user test-user``.

Staging/Qastaging
~~~~~~~~~~~~~~~~~

Some development environments, such as those deployed using the :doc:`Mojo
spec <../explanation/charms>`, use production Single Sign-On for
authentication.  In these environments, you should not use
``utilities/make-lp-user``; instead, log into 
``https://{qastaging,staging}.launchpad.net/`` via SSO as you would on 
production to create your user.

Add user to a team
------------------
                    
Let's say we created a new ``~test-user`` user in the previous section, and
we want to add it to the ``~admins`` team. We can use the
``utilities/anoint-team-member`` script within the Launchpad repo for
this purpose.

For staging and qastaging we should:

1. SSH into ``launchpad-bastion-ps5``, and switch to the ``stg-launchpad``
user by running ``sudo -iu stg-launchpad``. 

2. SSH into the ``launchpad-admin`` juju unit, by running 
``in-model qastaging juju ssh launchpad-scripts/leader``.

3. Switch to ``launchpad`` user, by running 
``sudo su launchpad``.

4. Add the user to the team by running: 

.. code::
     
     LPCONFIG=launchpad-admin /srv/launchpad/code/utilities/anoint-team-member <username> <team-name>

In our example:

.. code::
     
     LPCONFIG=launchpad-admin /srv/launchpad/code/utilities/anoint-team-member test-user admins
