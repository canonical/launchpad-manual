.. _builds-rocks-in-launchpad:

Build Rocks in Launchpad
========================

Rocks are Ubuntu LTS-based `OCI <https://opencontainers.org/>`_-compliant
container images designed for security, stability, and reliability in
cloud-native environments. Read more about rocks `here
<https://documentation.ubuntu.com/rockcraft/stable/explanation/rocks/>`_.

Building rocks on Launchpad ensures clean, reproducible builds across multiple
architectures, without needing to manage your own build infrastructure.

In this tutorial, we will create a new rock build in Launchpad using the API.


Pre-requisites
--------------

To build a rock in Launchpad, you will need:

- A Launchpad account (:ref:`how to create an account <create-and-personalise-your-launchpad-account>`).

- A Git repository on Launchpad with your valid ``rockcraft.yaml`` file.

- A project on Launchpad to associate the rock recipe with (`register a project
  <https://launchpad.net/projects/+new>`_).

- The `lp-shell
  <https://documentation.ubuntu.com/launchpad/developer/how-to/use-lp-shell/>`_
  tool. 

- To log in to Launchpad using the ``lp-shell`` command. Since we are pointing
  to production and want to use the devel APIs (`API documentation <https://api.launchpad.net/devel.html>`_),
  production::

    $ lp-shell production devel

- To verify your connection by runing the following command, which should
  return your own ``Person`` object::

    >>> lp.me
    <person at https://api.launchpad.net/devel/~username>

For more information on how to get your Pre-requisites in place, refer to the
Build Snaps in Launchpad tutorial. [TODO: ADD LINK]

Create the Rock Recipe
----------------------

Creating a rock recipe in Launchpad refers to telling Launchpad from where to
fetch your source code and build the rock.

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

Once created, you can obtain the URL of the rock's Launchpad page where you can
view the rock information and build information::

    >>> rock_recipe.web_link
    'https://launchpad.net/~username/project_name/+rock/test-rock'

To get the attributes and methods associated with the object::

    >>> rock_recipe.lp_attributes

    >>> rock_recipe.lp_operations

To learn more about what can be done with the ``rock_recipe``, refer to the
`rock recipe API documentation <https://api.launchpad.net/devel.html#rock_recipe>`_.

Build the Rock Recipe
---------------------

Requesting a build instructs Launchpad to compile and package the rock,
producing a build record and, if successful, ``.rock`` artifacts that can
installed and used::

    >>> build_request = rock_recipe.requestBuilds()

    >>> build_request
    <rock_recipe_build_request at https://api.launchpad.net/devel/~username/project/+rock/test-rock/+build-request/id>

    # The web link to view the build request
    >>> build_request.web_link
    'https://launchpad.net/~username/project_name/+rock/test-rock/+build-request/id'

You will need to query Launchpad to obtain the status of your build request
(Pending, Failed, Completed), you will not be notified in the CLI once the
build is completed::

    >>> build_request.status
    'Completed'

You can try refreshing the object state at any time by running::
    
    >>> build_request.lp_refresh()

To learn more about what can be done with the build object, refer to the
`rock recipe build request API documentation <https://api.launchpad.net/devel.html#rock_recipe_build_request>`_.

To get the builds produced by the build request::

    >>> rock_build = build_request.builds

    >>> rock_build
    <lazr.restfulclient.resource.Collection at 0x...>

Here, ``rock_build`` is a collection of builds based on the distribution series
and architecture set.

Again, you will need to query Launchpad to obtain the status of your build, you
will not be notified in the CLI once the build is completed:

    >>> for build in rock_build:
    ...     build.lp_refresh()
    ...     print(build.web_link, build.buildstate)
    https://launchpad.net/~username/project_name/+rock/test-rock/+build/id Successfully built

To learn more about what can be done with the build object, refer to the
`rock recipe build API documentation
<https://api.launchpad.net/devel.html#rock_recipe_build>`_.

Download the Rock
-----------------

Once the build has completed successfully, the build artifacts can be obtained
by::

    for build in rock_build:
    ...     print(build.getFileUrls(), build.build_log_url)
    ['https://launchpad.net/~username/project_name/+rock/test-rock/+build/id/+files/hello_latest_arm64.rock']
    https://launchpad.net/~username/project_name/+rock/test-rock/+build/id/+files/buildlog_rock_ubuntu_..._test-rock-1_BUILDING.txt.gz


To download the rock, you can use `urllib.request
<https://docs.python.org/3/library/urllib.request.html#module-urllib.request>`_::

    >>> for build in rock_build:
    ...   for url in build.getFileUrls():
    ...     filename = url.split("/")[-1]
    ...     urllib.request.urlretrieve(url, filename)
    ...     print(f"Downloaded {filename}")
    ... 
    Downloaded hello_latest_arm64.rock

Build Failures
--------------

In the case a build fails, ensure that the rock can be built locally by running
the ``rockcraft pack`` command. You can go through the buildlog
(``build.build_log_url``) and retry the build::

    >>> for build in rock_build:
    ...     build.retry()

Next Steps
----------

- `Run your rock by following these steps
  <https://documentation.ubuntu.com/rockcraft/stable/tutorial/hello-world/>`_
- Learn how to build snaps and charms on Launchpad

