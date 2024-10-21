================================
Creating a Rock build using APIs
================================

In this tutorial, we will be creating a new ``Rock`` build in Launchpad that points to
an existing repository using APIs (no UI). Note that this tutorial can be used also to
crete other kinds of builds.

Pre-requisites
==============

1. You have ``lp-shell`` installed. Can be installed using ``sudo apt-get install lptools``.
2. You have a Launchpad account.
3. You have a test project in Launchpad. You can create one `here <https://launchpad.net/projects/+new>`_.
4. You have a repository containing a Rock recipe. You can fork the `hellowork-rock <https://launchpad.net/~pelpsi/+git/helloworld-rock>`_ repository.

If you want to create a new repository from scratch, you can start from `there <https://documentation.ubuntu.com/rockcraft/en/latest/how-to/get-started>`_.

Creating the recipe
===================

At this point we are able to create the recipe.
The recipe is a set of instructions that will be used to tell the build system 
how to build the package.

First of all we need to log in to Launchpad using the ``lp-shell`` command.
We are pointing to ``production`` and we want to use the ``devel`` APIs.
(`API Documentation <https://api.launchpad.net/devel.html>`_)

.. code-block:: shell

    $ lp-shell production devel


.. code-block:: python

    # lp.me returns the current user
    >>> lp.me
    <person at https://api.launchpad.net/devel/~pelpsi>
    # let's load the repository we want to use
    >>> gitref = lp.load("~pelpsi/+git/helloworld-rock/+ref/main")
    >>> gitref
    <git_ref at https://api.launchpad.net/devel/~pelpsi/+git/helloworld-rock/+ref/main>
    # let's load the project created before, in this case I will use mine.
    >>> project = lp.load("pelpsi-testing")
    >>> project
    <project at https://api.launchpad.net/devel/pelpsi-testing>
    # Now we are able to create a new Rock recipe
    >>> recipe = lp.rock_recipes.new(owner=lp.me, project=project, name="testrockpelpsi", git_ref=gitref)
    >>> recipe
    <rock_recipe at https://api.launchpad.net/devel/~pelpsi/pelpsi-testing/+rock/testrockpelpsi>

Build the recipe
================

Once we have our recipe we should be able to build it.

.. code-block:: python

    # Let's create a build request for that recipe
    >>> br = recipe.requestBuilds()
    >>> br
    <rock_recipe_build_request at https://api.launchpad.net/devel/~pelpsi/pelpsi-testing/+rock/testrockpelpsi/+build-request/93165288>
    # After that we can query the builds collection that will contain the builds scheduled for that recipe.
    >>> br.builds[0]
    <rock_recipe_build at https://api.launchpad.net/devel/~pelpsi/pelpsi-testing/+rock/testrockpelpsi/+build/65>

.. note:: 

    You can check your build at `https://launchpad.net/~pelpsi/pelpsi-testing/+rock/testrockpelpsi/+build/65 <https://launchpad.net/~pelpsi/pelpsi-testing/+rock/testrockpelpsi/+build/65>`_


Fetch service
=============

If you want to use our fetch service for your builds, you can reach out the Launchpad team
and ask them to enabled it for your recipe! 

