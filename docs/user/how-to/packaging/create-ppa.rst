.. meta::
   :description: Guide on creating Personal Package Archives in Launchpad using
      the UI or web API.

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





