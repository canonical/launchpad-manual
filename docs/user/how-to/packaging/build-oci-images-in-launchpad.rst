.. _build-oci-images-in-launchpad:

Build OCI images in Launchpad
==========================================

`OCI <https://opencontainers.org/>`_ images are standardized, containerized application images 
that ensure consistent runtime behavior across container runtimes such as Docker, Podman, and Kubernetes.

By building OCI images on Launchpad, you gain:

- Clean, reproducible builds across multiple architectures.

- Freedom from managing your own build infrastructure.

- Direct publishing capabilities to container registries.

Launchpad supports OCI image builds via its API.

Prerequisites
------------------------------------------

To build an OCI image in Launchpad, you will need:

- A Launchpad account (:ref:`how to create an account <create-and-personalise-your-launchpad-account>`).

- A Git repository hosted on Launchpad. The repository must include a branch named in the format ``v1.0-24.04``.
  That branch must contain a valid ``Dockerfile``.

- To work with the API, you will also need the :ref:`lp-shell tool <how-to-use-lp-shell>`, which can be installed using::
  
    $ sudo apt install lptools

Log into Launchpad using `lp-shell`
------------------------------------------
Use the `lp-shell` command to log into Launchpad. Since we are pointing to 
production and want to use the `devel API <https://api.launchpad.net/devel.html>`_, run::

    $ lp-shell production devel

Verify your connection by running the following command, which should
return your own ``Person`` object::

    >>> lp.me
    <person at https://api.launchpad.net/devel/~username>

Create an OCI project
------------------------------------------

First, explore the available distributions in Launchpad::

    >>> [distribution.name for distribution in lp.distributions]
    ['ubuntu', 'elbuntu', 'fluxbuntu', 'nubuntu', 'ubuntu-leb', 'ubuntu-rtm', 'zubuntu', 'altlinux', 'archlinux', 'baltix', 'bardinux', 'bayanihan', 'bilimbitest', 'boss', 'centos', 'charms', 'debian', 'fedora', 'fink', 'freespire', 'frugalware', 'gentoo', 'guadalinex', 'guadalinexedu', 'kairos', 'kiwilinux', 'lfs', 'mandriva', 'nexenta', 'nexradix', 'opensuse', 'pld-linux', 'redflag-midinux', 'slackware', 'soss', 'suse', 'tilix', 'tuxlab', 'unity-linux']

Pick one (e.g. Ubuntu) and create a new OCI project under it::

    >>> ubuntu = lp.distributions["ubuntu"]
    >>> oci_project = ubuntu.newOCIProject(name="test-oci-project")
    <oci_project at https://api.launchpad.net/devel/ubuntu/+oci/test-oci-project>

An OCI project acts as a container for your recipes and builds.

Create an OCI recipe
------------------------------------------

An OCI recipe defines how to build an OCI image from a Git branch.

Load the Git reference that contains your ``Dockerfile``::

    >>> git_ref = lp.load("~username/+git/repository_name/+ref/<branch name in format v1.0-24.04>")

Create the recipe::

    >>> oci_recipe = oci_project.newRecipe(build_file="Dockerfile", git_ref=git_ref, name="test-oci-recipe", owner=lp.me)

Build an OCI image
------------------------------------------

Request a build of your recipe::

    >>> oci_build_request = oci_recipe.requestBuilds()

Check its status::

    >>> oci_build_request.status

Refresh the object to see updates::

    >>> oci_build_request.lp_refresh()

Download artifacts
------------------------------------------

When the build completes, you can download the produced image artifacts::

    >>> oci_builds = lp.load(oci_build_request.builds_collection_link)
    >>> oci_build = lp.load(builds.entries[0]["self_link"])
    >>> import urllib
    >>> for url in oci_build.getFileUrls():
    ...     filename = url.split("/")[-1]
    ...     urllib.request.urlretrieve(url, filename)
    ...     print(f"Downloaded {filename}")

This retrieves all build outputs (image layers, manifests, etc.).

Selecting build processors
------------------------------------------

Launchpad supports multiple CPU architectures. To see which ones are available::

    >>> [processor.name for processor in lp.processors]
    ['ia64', 'sparc', 'hppa', 'amd64', 'armel', 'armhf', 'lpia', 'ppc64el', 's390x', 'arm64', 'powerpc', 'i386', 'riscv64']

To set processors on which your recipe will be built::

    >>> oci_recipe.setProcessors(processors=[processor.self_link for processor in lp.processors if processor.name in ["amd64", "arm64"]])

Pushing OCI images to a registry
------------------------------------------

Launchpad can push your OCI image directly to registries like Docker Hub:

- Create a repository on your chosen registry.

- Generate a Personal Access Token.

- Configure a push rule in Launchpad::

    >>> oci_recipe.newPushRule(registry_url="https://registry-1.docker.io", image_name="username/test-image", credentials_owner=lp.me, credentials={"username": "username", "password": "password"})

At the end of the next successful build, the image will be automatically uploaded.

Handling build failures
------------------------------------------

In case your build fails, verify the image builds locally::

    docker build .

Download the build log::

    >>> urllib.request.urlretrieve(oci_build.build_log_url, oci_build.build_log_url.split("/")[-1])

Fix and retry the build::

    >>> oci_build.retry()

Next Steps
------------------------------------------

- Continue exploring the :ref:`Launchpad API <launchpad-api>`
