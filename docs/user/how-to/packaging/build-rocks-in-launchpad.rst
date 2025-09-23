.. _build-rocks-in-launchpad:

Build Rocks in Launchpad
========================

Rocks are Ubuntu LTS-based `OCI <https://opencontainers.org/>`_-compliant
container images designed for security, stability, and reliability in
cloud-native environments. To learn more about rocks, check out the official 
`Rockcraft documentation <https://documentation.ubuntu.com/rockcraft/stable/explanation/rocks/>`_.

Building rocks on Launchpad ensures clean builds across multiple architectures, 
without needing to manage your own build infrastructure.

In this guide, we will create a new rock build in Launchpad using the API.


Pre-requisites
--------------

To build a rock in Launchpad, you will need:

- A :ref:`Launchpad account <create-and-personalise-your-launchpad-account>`.

- A Git repository on Launchpad with a valid ``rockcraft.yaml`` file. 

- A `project on Launchpad <https://launchpad.net/projects/+new>`_ for the rock recipe.

- The `lp-shell
  <https://documentation.ubuntu.com/launchpad/developer/how-to/use-lp-shell/>`_
  tool. 

Log into Launchpad using `lp-shell`
-----------------------------------
Use the `lp-shell` command to log into Launchpad. Since we are pointing to 
production and want to use the devel APIs (`API documentation <https://api.launchpad.net/devel.html>`_)
production::

    $ lp-shell production devel

Verify your connection by running the following command, which should
return your own ``Person`` object::

    >>> lp.me
    <person at https://api.launchpad.net/devel/~username>

Create the Rock Recipe
----------------------

Creating a rock recipe in Launchpad means telling Launchpad from where to fetch
the source code needed to build the rock.

Load the Git ref where your rockcraft.yaml file is::

    >>> git_reference = lp.load("~username/+git/repository_name/+ref/master")

    >>> git_reference
    <git_ref at https://api.launchpad.net/devel/~username/+git/repository_name/+ref/master>

Load the project you want to associate your rock recipe with::

    >>> project = lp.load("project_name")

    >>> project
    <project at https://api.launchpad.net/devel/project_name>

Create a buildable rock recipe::

    >>> rock_recipe = lp.rock_recipes.new(owner=lp.me, project=project,
    ... name="test-rock", git_ref=git_reference)

    >>> rock_recipe
    <rock_recipe at https://api.launchpad.net/devel/~username/project_name/+rock/test-rock>

The full list of parameters that can be passed in the API can be found in the
`rock recipes API documentation <https://api.launchpad.net/devel.html#rock_recipes>`_.

Once created, fetch the URL of the rock's Launchpad page where you can view the
rock and build information::

    >>> rock_recipe.web_link
    'https://launchpad.net/~username/project_name/+rock/test-rock'

To get the attributes associated with the object::

    >>> rock_recipe.lp_attributes

To get the methods associated with the object::

    >>> rock_recipe.lp_operations

To learn more about what you can do with the ``rock_recipe`` object, check the
`rock recipe API documentation <https://api.launchpad.net/devel.html#rock_recipe>`_.

Build the Rock Recipe
---------------------

Requesting a build instructs Launchpad to compile and package the rock. This
produces a build record and, if successful, ``.rock`` artifacts that can be
installed and used::

    >>> build_request = rock_recipe.requestBuilds()

    >>> build_request
    <rock_recipe_build_request at https://api.launchpad.net/devel/~username/project/+rock/test-rock/+build-request/id>

The web link to view the build request::

    >>> build_request.web_link
    'https://launchpad.net/~username/project_name/+rock/test-rock/+build-request/id'

You will not be notified in the CLI when the build is completed. You'll need to
query Launchpad to obtain the status of your build request (`Pending`, `Failed`,
`Completed`)::

    >>> build_request.status
    'Completed'

You can also refresh the object state at any time by running::
    
    >>> build_request.lp_refresh()

To learn more about what you can do with the build object, refer to the
`rock recipe build request API documentation <https://api.launchpad.net/devel.html#rock_recipe_build_request>`_.

To get the builds produced by the build request::

    >>> rock_build = build_request.builds

    >>> rock_build
    <lazr.restfulclient.resource.Collection at 0x...>

``rock_build`` is a collection of builds based on the distribution series
and architecture set.

Once again, you will not be notified in the CLI when the build is completed. 
You must query Launchpad to obtain the status of your build:

    >>> for build in rock_build:
    ...     build.lp_refresh()
    ...     print(build.web_link, build.buildstate)
    https://launchpad.net/~username/project_name/+rock/test-rock/+build/id Successfully built

To learn more about what you can do with the build object, refer to the
`rock recipe build API documentation <https://api.launchpad.net/devel.html#rock_recipe_build>`_.

Download the Rock
-----------------

Once the build has completed successfully, fetch the build artifacts::

    >>> for build in rock_build:
    ...     print(build.getFileUrls(), build.build_log_url)
    ['https://launchpad.net/~username/project_name/+rock/test-rock/+build/id/+files/hello_latest_arm64.rock']
    https://launchpad.net/~username/project_name/+rock/test-rock/+build/id/+files/buildlog_rock_ubuntu_..._test-rock-1_BUILDING.txt.gz


Then, use `urllib.request <https://docs.python.org/3/library/urllib.request.html#module-urllib.request>`_
to download the rock::

    >>> for build in rock_build:
    ...   for url in build.getFileUrls():
    ...     filename = url.split("/")[-1]
    ...     urllib.request.urlretrieve(url, filename)
    ...     print(f"Downloaded {filename}")
    ... 
    Downloaded hello_latest_arm64.rock

Build Failures
--------------

In case a build fails, ensure the rock can be built locally by running the 
``rockcraft pack`` command. You can go through the buildlog (``build.build_log_url``) 
and retry the build::

    >>> for build in rock_build:
    ...     build.retry()

Next Steps
----------

- Check out this tutorial on `running your rock <https://documentation.ubuntu.com/rockcraft/stable/tutorial/hello-world/>`_
- :ref:`Build snaps on Launchpad <build-snaps-in-launchpad>`

