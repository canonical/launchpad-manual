.. _build-snaps-in-launchpad:

Build Snaps in Launchpad
========================

Snaps are containerised software packages that are designed to be simpler to 
create and install by bundling applications with their dependencies. They work 
across many Linux distributions without modification. Check out the Snapcraft 
documentation to `learn more about Snaps <https://snapcraft.io/docs/get-started>`_.

Building snaps on Launchpad ensures clean, reproducible builds across multiple
architectures, without needing to manage your own build infrastructure. It
provides an easy way to publish snaps directly to the `Snap Store <https://snapcraft.io/store>`_.

On Launchpad, snaps can be built using either the web interface or the API. 
This guide takes you through both approaches.

Prerequisites
--------------

To build a snap in Launchpad, you will need:

- A Launchpad account (:ref:`how to create an account <create-and-personalise-your-launchpad-account>`).

- A Git repository on Launchpad with your working snap recipe. If you do not
  have one, follow `Snapcraft's tutorial <https://documentation.ubuntu.com/snapcraft/stable/tutorials/craft-a-snap/>`_ 
  to create a simple one, and push to a repository using::

    git remote add origin git+ssh://username@git.launchpad.net/~username/+git/repository_name
    git push --set-upstream origin master

- To work with the API, you will also need the :ref:`lp-shell tool <how-to-use-lp-shell>`, which can be installed using::
  
    $ sudo apt install lptools

Build with the API or the web interface(UI)
-------------------------------------------

.. tab-set:: 

  ..  tab-item:: Build a snap with the API
      :sync: key1

      **Log into Launchpad**

      Use the ``lp-shell`` command to log in. Since we are pointing to 
      production and want to use the devel APIs (`API documentation <https://api.launchpad.net/devel.html>`_),
      run::

        $ lp-shell production devel

      To verify your connection, run the following command, which should return 
      your own ``Person`` object::
      
        >>> lp.me
        <person at https://api.launchpad.net/devel/~username>

      **Create the Snap**

      Creating a snap in Launchpad refers to registering a snap package and
      associating it with a source repository which contains a ``snapcraft.yaml``
      file.

      Inside ``lp-shell``, run either of the following sets of commands to 
      create a buildable snap package:

      - If you have a Git repository and path::

        >>> git_repository = lp.load("~username/+git/repository_name")

        >>> git_repository
        <git_repository at https://api.launchpad.net/devel/~username/+git/repository_name>

        >>> snap = lp.snaps.new(name="test-snap", owner=lp.me, 
        ... git_repository_url=git_repository, git_path="master")

      - Using a Git reference::

        >>> git_reference = lp.load("~username/+git/repository_name/+ref/master")

        >>> git_reference
        <git_ref at https://api.launchpad.net/devel/~username/+git/repository_name/+ref/master>

        >>> snap = lp.snaps.new(name="test-snap", owner=lp.me, 
        ... git_ref=git_reference")

      The full list of parameters that can be passed in the API can be found in
      the `snaps API documentation <https://api.launchpad.net/devel.html#snaps>`_.

      Once the snap is created, you can obtain the URL of the snap's Launchpad 
      page where you can view the snap, see builds, and edit the snap package::

        >>> snap.web_link
        'https://launchpad.net/~username/+snap/test-snap'

      To get the attributes associated with the object::

        >>> snap.lp_attributes

      To get the methods associated with the object::

        >>> snap.lp_operations

    
      **Build the Snap**

      Requesting a build instructs Launchpad to compile and package the snap,
      producing a build record and, if successful, ``.snap`` artifacts that can
      be installed and used.

      The parameters used when requesting a snap build can be found in the `snap
      API documentation <https://api.launchpad.net/devel.html#snap>`_. 
      
      When requesting a build, you must specify the ``archive`` to be used to
      get the package sources needed to build the snap package. This can be the
      ``Primary Archive for Ubuntu`` or a :ref:`Personal Package Archive (PPA)
      <personal-package-archive>`.

      The ``pocket`` determines which package stream within the ``source archive``
      and ``distribution series`` is to be used. If the ``source archive`` is a
      PPA, the PPA's archive dependencies will be used to select the pocket 
      in the distribution's primary archive.

      In this guide, ``Primary Archive for Ubuntu`` is selected as the source 
      archive and ``Updates`` as the ``pocket``::

        >>> ubuntu_archive = lp.distributions["ubuntu"].main_archive

        >>> build_request = snap.requestBuilds(
        ... archive=ubuntu_archive.self_link,
        ... pocket="Updates",
        ... )

        >>> build_request
        <snap_build_request at https://api.launchpad.net/devel/~username/+snap/test-snap/+build-request/id>

        # The web link to view the build request
        >>> build_request.web_link
        'https://api.launchpad.net/devel/~username/+snap/test-snap/+build-request/id'

      ``requestBuilds()`` requests that the snap package be built for all 
      relevant architectures. However, you can specify an architecture to 
      build for by passing ``distro_arch_series`` in ``requestBuild()`` instead.

      You will not be notified in the CLI once the build is completed. To 
      obtain the status of your build (``Pending``, ``Failed``, ``Completed``),
      you'll need to query Launchpad::

        >>> build_request.status
        'Completed'

      You can refresh the object state at any time by running::

        >>> build_request.lp_refresh()

      To get the builds produced by the build request::

        >>> snap_build = build_request.builds

        >>> snap_build
        <lazr.restfulclient.resource.Collection at 0x...>

      Here, ``snap_build`` is a collection of builds based on the specified
      distribution series and architecture set.

      In this case as well, you'll need to query Launchpad to obtain the 
      status of your build::

        >>> for build in snap_build:
        ...   build.lp_refresh() # to refresh the object state
        ...   print(build.web_link, build.buildstate)
        https://launchpad.net/~username/+snap/test-snap/+build/id Successfully built
        
      To learn more about what can be done with the ``build`` object, refer to
      the `snap build API documentation <https://api.launchpad.net/devel.html#snap_build>`_.

      **Download the Snap**

      Once the build has completed successfully, the build artifacts can be
      obtained by::

        >>> for build in snap_build:
        ...   print(build.getFileUrls(), build.build_log_url)
        ['https://launchpad.net/~username/+snap/test-snap/+build/id/+files/hello_2.10_amd64.snap',
        'https://launchpadlibrarian.net/id/buildlog_snap_ubuntu_...test-snap_BUILDING.txt.gz']

      Use `urllib.request <https://docs.python.org/3/library/urllib.request.html#module-urllib.request>`_
      to download the snap::

        >>> for build in snap_build:
        ...   for url in build.getFileUrls():
        ...     filename = url.split("/")[-1]
        ...     urllib.request.urlretrieve(url, filename)
        ...     print(f"Downloaded {filename}")
        Downloaded hello_2.10_amd64.snap

      **Build Failures**

      In case a build fails, ensure that the snap can be built locally by
      running the ``snapcraft`` command. You can also go through the 
      ``buildlog`` (``build.build_log_url``) and retry the build::

        >>> for build in snap_build:
        ...   build.retry()

  ..  tab-item:: Build Snaps with the UI
      :sync: key2

      **Create the Snap**

      Creating a snap in Launchpad refers to registering a snap package and
      associating it with a source repository which contains a ``snapcraft.yaml``
      file.

      There are two options to create a buildable snap package on the UI:

      - Go to a branch in your source repository and navigate to::

          https://code.launchpad.net/~username/+git/repository_name/+ref/master.

      - Select or `register
        <https://launchpad.net/projects/+new>`_ a project on Launchpad and 
        navigate to::

          https://launchpad.net/project_name

      Select ``Create snap package``.

      Fill in the required details and click on ``Create snap package``. The 
      name of this snap is set to ``test-snap``.

      **Build the Snap**

      Requesting a build instructs Launchpad to compile and package the snap,
      producing a build record and, if successful, ``.snap`` artifacts that can
      installed and used.
      
      Navigate to the snap package page::

        https://launchpad.net/~username/+snap/test-snap

      When requesting a build, you must specify the ``archive`` to be used to
      get the package sources needed to build the snap package. This can be the
      ``Primary Archive for Ubuntu`` or a :ref:`Personal Package Archive (PPA)
      <personal-package-archive>`.

      The ``pocket`` determines which package stream within the ``source archive``
      and ``distribution series`` is to be used. If the ``source archive`` is a
      ``PPA``, then the PPA's archive dependencies will be used to select the
      pocket in the distribution's primary archive.

      In this guide, the build is requested with ``Primary Archive for Ubuntu`` 
      set as the source archive and ``Updates`` as the pocket.
      
      Build the .snap artifact by selecting ``Request builds``.

      **Download the Snap**

      Once the snap is built it can be accessed from::

        https://launchpad.net/~username/+snap/test-snap

      Navigate to the ``Latest Builds`` section to see the ``buildlog`` and 
      ``build files``. Select ``build files`` to download the snap to your 
      machine.

      **Build Failures**
      
      In case a build fails, ensure that the snap can be built locally by
      running the ``snapcraft`` command. You can also go through the 
      ``buildlog`` and retry the build by selecting ``Request builds`` again.

Next Steps
----------

- `Install and run your built snap <https://documentation.ubuntu.com/snapcraft/stable/tutorials/craft-a-snap/#test-the-snap>`_
- Learn how to :ref:`build rocks in Launchpad <build-rocks-in-launchpad>`