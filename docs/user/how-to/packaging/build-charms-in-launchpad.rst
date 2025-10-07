.. _build-charms-in-launchpad:

Build charms in Launchpad
=========================

Charms are software operators for cloud operations which use the Juju
orchestration engine. They can be deployed, integrated, scaled, and configured
on any Kubernetes cluster. Visit the `Charmcraft <https://documentation.ubuntu.com/charmcraft/stable/>`_ 
and `Juju <https://documentation.ubuntu.com/juju/3.6/reference/charm/#charm>`_ 
documentation to learn more about charms.

Building charms on Launchpad ensures you get clean builds for multiple 
architectures, including RISC-V 64, without having to manage any local
infrastructure. You also get the option of publishing builds directly to the 
`Charm store <https://charmhub.io/>`_.  

This guide will take you through the process of building charms on Launchpad
through the web interface.

.. note::

    Building of reactive charms and private charms, i.e., charms from private 
    repositories, is not supported on Launchpad.

Prerequisites
-------------
To build charms in Launchpad you need:

- A :ref:`Launchpad account <create-and-personalise-your-launchpad-account>`
- A Git repository with the files needed for your charm, including a charmcraft.yaml file. If you don't have one, follow `Charmcraft's tutorials <https://documentation.ubuntu.com/charmcraft/stable/tutorial/>`_ to create a charm from scratch, and push it to Launchpad:

.. code:: shell
        
        git remote add origin git+ssh://username@git.launchpad.net/~username/+git/repository_name
        git push --set-upstream origin main

Register a project in Launchpad
-------------------------------
:ref:`Register a new project <how-to-register-your-project>` for the charm 
build. When choosing a license, remember that building charms on Launchpad does
not work with private or proprietary projects and repositories.

Choose a Git repository
-----------------------
Go to the project page:

.. code:: shell

    https://launchpad.net/<project-name>

Open the ``Code`` tab and select ``Configure Code``. Choose a Git repository
on Launchpad or import one hosted elsewhere, e.g., GitHub.

Enter the required details and select ``Update``.

Create the charm recipe
-----------------------
Select ``Create charm recipe`` on the product page and enter the recipe details.
Use the search function when entering the repository name and branch if you 
don't remember these exactly. 

The branch name must be in the format ``refs/heads/<branch-name>``.

.. Note::
    You can also create a recipe by navigating to a specific branch in a 
    repository and selecting ``Create charm recipe``. This eliminates the need to
    specify a repository and branch when creating the recipe.

All other fields are optional. If you want to trigger new builds each time the 
branch changes, select the corresponding checkbox. You can also choose to 
automatically upload new builds to the store.

When all the details are set, create the recipe.

Request a recipe build 
----------------------
Navigate to the newly created charm recipe:

.. code:: shell

    https://launchpad.net/~<user-name>/<project-name>/+charm/<charm-name>/

Select ``Request builds``. You will be prompted to select a channel to use for 
build tools, but this is optional. Leave the fields blank and complete the 
build request. 

You will be redirected to the recipe with a message that says ``Builds will 
be dispatched soon.`` Refresh this page to check the status of the builds. 

When a build is ready, its status will change to ``Successfully built``.

Download the charm
------------------
Select one of the successful builds, e.g., ``amd64``, and locate the built 
files on the build page. Build files will be shown in the format, ``charm-name_distribution-architecture.charm(build size)``.

For example:

.. code:: shell

    my-new-charm_ubuntu-22.04-amd64.charm(11.3MiB)

Click on a build file to download your charm.

Build failures
--------------
In case one or all the builds fail, confirm the charm can be built locally::

    charmcraft pack

You can also go through the ``buildlog`` on the recipe page or repeat build 
step above.

Next steps 
----------
- Learn how to `deploy your charm with Juju <https://documentation.ubuntu.com/charmcraft/stable/tutorial/kubernetes-charm-django/#deploy-the-django-app>`_ 
- :ref:`Build snaps in Launchpad <build-snaps-in-launchpad>`
