.. meta::
   :description: Guide on creating, editing, and managing dependencies of
      Personal Package Archives in Launchpad using the UI or web API.

.. _create-ppa:

Create a Personal Package Archive (PPA)
=======================================

Personal Package Archives (commonly called PPAs) are software repositories that
allow users to distribute free software packages. PPAs are built and hosted on
Launchpad and can be installed just like any package in the official Ubuntu
archive.

.. warning::
    Launchpad does not endorse any software in PPAs. Make sure you trust the
    PPA owner before installing their software.

Create a PPA
------------

Launchpad users can create PPAs via the web user interface or using the API.

.. tab-set::

    .. tab-item:: Web interface

        #. Log into Launchpad and go to your profile page at ``https://launchpad.net/~``.
           For team PPA's, go to the team's overview page.
        #. Select :guilabel:`create a new PPA`
        #. On the :guilabel:`Activate a Personal Package Archive` page, read
           the PPA terms of use and fill in the details of your new PPA.
        #. You must check the :guilabel:`I have read and accepted the PPA Terms of Use`
           box before activating your first PPA.
        #. Select :guilabel:`Activate`.

        You should see the new PPA under :guilabel:`Personal Package Archives`
        on your profile or team overview page.


    .. tab-item:: Web service API

        #. Open lp-shell on the terminal::

            lp-shell production devel

        #. Fetch your user or team profile and store it in a variable. For a
           team, replace ``lp.me.name`` with the team's Launchpad name::

            owner = lp.people[lp.me.name]

        #. Using the ``createPPA`` endpoint, define and create your new PPA::

            owner.createPPA(name="test-ppa", displayname="Test PPA", description="Create new PPA using API.", distribution=lp.load('ubuntu'))

        #. Verify the PPA has been created by checking the list of PPAs
           associated with your profile::

            [print(ppa.name) for ppa in owner.ppas]

        All parameters used to create PPAs are optional. However, you can't
        create a PPA with the same name as an existing one. If ``distribution``
        is not declared, Ubuntu is used by default.


Edit an existing PPA
--------------------

After creating a PPA, you can change its details either through the web user
interface or using the API.

.. tab-set::

    .. tab-item:: Web interface

        #. Log into Launchpad and go to the PPA's overview page, for example
           ``https://launchpad.net/~/+archive/ubuntu/test-ppa``.
        #. Select :guilabel:`Change details`.
        #. On the edit page you can change the following:

           - :guilabel:`Display name` -- a short title for the PPA.
           - :guilabel:`Description` -- a short description of the PPA. URLs are
             allowed and rendered as links.
           - :guilabel:`Enabled` -- whether the PPA accepts and builds uploaded
             packages.
           - :guilabel:`Publish` -- whether the apt repository is updated. If
             disabled, nothing is published; for a private PPA no builds are
             dispatched either.
           - :guilabel:`Build debug symbols` -- create debug symbol packages for
             builds in the PPA.
           - :guilabel:`Publish debug symbols` -- publish debug symbol packages
             in the apt repository.
           - :guilabel:`Processors` -- the architectures on which the PPA can
             build. Some architectures are restricted and may only be enabled or
             disabled by administrators.

        #. Save any changes you've made.


    .. tab-item:: Web service API

        #. Open lp-shell on the terminal::

            lp-shell production devel

        #. Fetch the PPA you want to edit and store it in a variable. Replace
           ``owner`` with ``lp.people[lp.me.name]`` (or the team) and adjust the
           PPA name::

            ppa = lp.people[lp.me.name].getPPAByName(name="test-ppa")

        #. Change one or more of the editable attributes::

            ppa.displayname = "Renamed Test PPA"
            ppa.description = "Updated description for the PPA."
            ppa.build_debug_symbols = True
            ppa.publish_debug_symbols = True

        #. Save your changes back to Launchpad::

            ppa.lp_save()

        #. To change the architectures the PPA can build on, use the
           ``setProcessors`` endpoint (the ``processors`` attribute is read-only
           and cannot be set directly)::

            amd64 = lp.processors.getByName(name="amd64")
            arm64 = lp.processors.getByName(name="arm64")
            ppa.setProcessors(processors=[amd64.self_link, arm64.self_link])

        .. note::

            The :guilabel:`Enabled` and :guilabel:`Publish` options are only
            available through the web interface; they are not currently exposed
            via the API.


Manage archive dependencies
---------------------------

A PPA can depend on other archives, so that packages published in those
archives are available when building packages in your PPA. Dependencies can be
managed either through the web user interface or using the API.

.. tab-set::

    .. tab-item:: Web interface

        #. Log into Launchpad and go to the PPA's overview page, for example
           ``https://launchpad.net/~/+archive/ubuntu/test-ppa``.
        #. Select :guilabel:`Edit PPA dependencies`.
        #. On the :guilabel:`Edit PPA dependencies` page you can:

           - Choose which packages of the distribution's primary archive are
             used as build dependencies (for example :guilabel:`Basic`,
             :guilabel:`Security`, :guilabel:`Default`, :guilabel:`Proposed`
             or :guilabel:`Backports`).
           - Add another PPA as a dependency by entering it in the
             :guilabel:`Add PPA dependency` field.
           - Remove existing dependencies by selecting them under
             :guilabel:`Extra dependencies`.

        #. Save any changes you've made.

        .. note::

            Pin priorities cannot currently be set through the web interface.
            To assign a custom pin priority to a dependency, use the API as
            described in the next tab.


    .. tab-item:: Web service API

        #. Open lp-shell on the terminal::

            lp-shell production devel

        #. Fetch the PPA you want to add a dependency to, and the archive it
           should depend on::

            ppa = lp.people[lp.me.name].getPPAByName(name="test-ppa")
            dependency = lp.people["some-owner"].getPPAByName(name="other-ppa")

        #. Add the dependency using the ``addArchiveDependency`` endpoint. The
           ``pocket`` is given as a string, for example ``"Release"``::

            ppa.addArchiveDependency(dependency=dependency, pocket="Release")

        **Pin priorities**

        When adding a dependency you can optionally set a ``pin_priority``, an
        integer that controls the APT pin priority used for packages provided
        by the dependency. Higher values make packages from the dependency
        preferred over others. The value must be in the range ``-100`` to
        ``2000``; if omitted, it defaults to ``500``. Pin priorities can only
        be set through the API; the web interface does not yet expose them.

        .. seealso::

            For details on how APT interprets pin priority values, see the
            `apt_preferences(5) manual page
            <https://manpages.ubuntu.com/manpages/resolute/man5/apt_preferences.5.html>`_.

        #. To add a dependency with a custom pin priority, include a value for
           `pin_priority` when declaring the dependency::

            ppa.addArchiveDependency(dependency=dependency, pocket="Release", pin_priority=1000)

        #. You can also change the pin priority of an existing dependency by
           editing the ``IArchiveDependency`` record directly and saving it::

            archive_dependency = ppa.getArchiveDependency(dependency=dependency)
            archive_dependency.pin_priority = 900
            archive_dependency.lp_save()

        .. note::

            Custom pin priorities are only supported for PPA dependencies. If
            the dependency points to a non-PPA archive (such as the primary
            Ubuntu archive), the pin priority must be left at its default
            value of ``500``. Attempting to set any other value for a non-PPA
            dependency is rejected with an error, because a custom pin
            priority would never take effect for such archives.




