Host your project on Launchpad with Bazaar
==========================================

First step would be to install ``bzr``.

Open up a terminal and type:

.. terminal::
    sudo aptitude install bzr

Now we should make sure bzr knows who we are:

.. terminal::
    bzr whoami "Your Name <your@email>"

.. terminal::
    bzr launchpad-login USERNAME

To interact with launchpad in any way, you must have an account and a
SSH key registered, so make sure you have both.

Next you would need to register a product.

Once you have all of those steps covered, you have to create a
repository of what you want to upload, so go to the directory where all
the files are:

``cd project_dir``

and then create the initial local repository:

.. terminal::
    bzr init

.. terminal::
    bzr add

This adds all the files in the directory, see bazaar
documentation to exclude files or directories.

.. terminal::
    bzr commit -m "first commit"

Your local bzr repository is now ready to be sent to launchpad.

You would do this with:

.. terminal::
    bzr push lp:~launchpad_user_or_team/project_name/branch*

Your project is now hosted on Launchpad. Keep in mind it might take a
few minutes after the push is done succesfully for everything to work
correctly.

Any user who wants to work on the project has two different approaches:

Checkouts: Usually recommended for quick changes, it commits straight
into Launchpad

.. terminal::
    bzr checkout lp:~launchpad_user_or_team/project_name/branch

Branches: For bigger changes, it commits locally and you push the
changes to Launchpad when ready

.. terminal::
    bzr branch lp:~launchpad_user_or_team/project_name/branch

Whenever making changes to the files, both approaches need a:

.. terminal::
    bzr commit -m "a comment on what has been changed"

But when using branches, you also need send your changes:

.. terminal::
    bzr push lp:~launchpad_user_or_team/project_name/branch

More information
----------------

http://bazaar-vcs.org/Tutorials/CentralizedWorkflow
http://blogs.gnome.org/view/jamesh/2006/08/17/1
