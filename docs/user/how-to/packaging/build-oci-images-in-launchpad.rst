.. _build-oci-images-in-launchpad:

Build OCI images in Launchpad
=============================

.. note::
    This feature is not yet available to everyone. Please reach out to the 
    Launchpad team if you're interested in building OCI images in Launchpad.
    
OCI images are standardized, containerized application images that ensure 
consistent runtime behavior across container runtimes such as Docker, Podman, 
and Kubernetes.

By building `OCI <https://opencontainers.org/>`_ images on Launchpad, you get 
clean, reproducible builds across multiple architectures without having to 
manage your own infrastructure. You'll also be able to publish directly to 
container registries.

This guide shows you how to build OCI images on Launchpad using the API.

Prerequisites
------------------------------------------

To build an OCI image in Launchpad, you will need:

- A Launchpad account (:ref:`how to create an account <create-and-personalise-your-launchpad-account>`).

- A Git repository hosted on Launchpad. The repository must include a branch
  named in the format ``v1.0-24.04``, and the branch must contain a valid 
  ``Dockerfile``.

- To work with the API, you will also need
  the :ref:`lp-shell tool <how-to-use-lp-shell>`,
  which can be installed using::
  
    $ sudo apt install lptools

Log into Launchpad using `lp-shell`
------------------------------------------
Use the `lp-shell` command to log into Launchpad. Since we are pointing to 
production and want to use
the `devel API <https://api.launchpad.net/devel.html>`_, run::

    $ lp-shell production devel

Verify your connection by running the following command, which should
return your own ``Person`` object::

    >>> lp.me
    <person at https://api.launchpad.net/devel/~username>

Create an OCI project
------------------------------------------

An OCI project acts as a container for your recipes and builds. Explore the 
available distributions in Launchpad::

    >>> [distribution.name for distribution in lp.distributions]
    ['ubuntu', 'elbuntu', 'fluxbuntu', 'nubuntu', 'ubuntu-leb', 'ubuntu-rtm', 'zubuntu', 'altlinux', 'archlinux', 'baltix', 'bardinux', 'bayanihan', 'bilimbitest', 'boss', 'centos', 'charms', 'debian', 'fedora', 'fink', 'freespire', 'frugalware', 'gentoo', 'guadalinex', 'guadalinexedu', 'kairos', 'kiwilinux', 'lfs', 'mandriva', 'nexenta', 'nexradix', 'opensuse', 'pld-linux', 'redflag-midinux', 'slackware', 'soss', 'suse', 'tilix', 'tuxlab', 'unity-linux']

Pick your preferred distribution (e.g. Ubuntu), and create a new OCI project 
under it::

    >>> ubuntu = lp.distributions["ubuntu"]
    >>> oci_project = ubuntu.newOCIProject(name="test-oci-project")
    <oci_project at https://api.launchpad.net/devel/ubuntu/+oci/test-oci-project>


Create an OCI recipe
------------------------------------------

An OCI recipe tells Launchpad how to build an OCI image from a Git branch.

Load the Git reference that contains your ``Dockerfile``::

    >>> git_ref = lp.load("~username/+git/repository_name/+ref/<branch name in format v1.0-24.04>")

Create the recipe::

    >>> oci_recipe = oci_project.newRecipe(build_file="Dockerfile", git_ref=git_ref, name="test-oci-recipe", owner=lp.me)

Select build processors
-----------------------

Launchpad supports multiple CPU architectures. To see which ones are available::

    >>> [processor.name for processor in lp.processors]
    ['ia64', 'sparc', 'hppa', 'amd64', 'armel', 'armhf', 'lpia', 'ppc64el', 's390x', 'arm64', 'powerpc', 'i386', 'riscv64']

To set processors on which your recipe will be built::

    >>> oci_recipe.setProcessors(processors=[processor.self_link for processor in lp.processors if processor.name in ["amd64", "arm64"]])

Push OCI images to a registry (optional)
-------------------------------------------

You can configure Launchpad to push your OCI image directly to registries like 
Docker Hub:

- Create a repository on your chosen registry.

- Generate a Personal Access Token.

- Configure a push rule in Launchpad::

    >>> oci_recipe.newPushRule(registry_url="https://registry-1.docker.io", image_name="username/test-image", credentials_owner=lp.me, credentials={"username": "username", "password": "password"})

The image will be automatically uploaded at the end of the next successful 
build.

Build an OCI image
------------------------------------------

Request a build of your recipe::

    >>> oci_build_request = oci_recipe.requestBuilds()

You will not be notified when the build is complete. To manually check its 
status (`Pending`, `Failed`, `Completed`)::

    >>> oci_build_request.status

If the initial status is `Pending`, refresh the object before rechecking the
status::

    >>> oci_build_request.lp_refresh()

Download artifacts
------------------------------------------

Once the build is successful, i.e., the status check returns `Completed`, 
download the image artifacts::

    >>> oci_builds = lp.load(oci_build_request.builds_collection_link)
    >>> oci_build = lp.load(oci_builds.entries[0]["self_link"])
    >>> import urllib
    >>> for url in oci_build.getFileUrls():
    ...     filename = url.split("/")[-1]
    ...     urllib.request.urlretrieve(url, filename)
    ...     print(f"Downloaded {filename}")

This will retrieve all build outputs (image layers, manifests, etc.).

Handling build failures
------------------------------------------

In case your build fails, you can:

- Verify if the image builds locally::

    docker build .

- Download and check the build log::

    >>> urllib.request.urlretrieve(oci_build.build_log_url, oci_build.build_log_url.split("/")[-1])

- Retry the build::

    >>> oci_build.retry()

Next Steps
------------------------------------------

- :ref:`Build snaps on Launchpad <build-snaps-in-launchpad>`
- :ref:`Build rocks on Launchpad <build-rocks-in-launchpad>`
