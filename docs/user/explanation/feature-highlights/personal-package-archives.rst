.. meta::
   :description: Highlight of Personal Package Archives (PPAs) for publishing 
      Ubuntu software packages.

.. _personal-package-archives-highlights:

Personal Package Archives
=========================


Personal Package Archives (PPAs) are one of Launchpad's most popular
and exceptional features. Using a PPA you can publish your own software
packages that are installable in Ubuntu. They can be based on existing
Ubuntu packages or you can create completely new packages of any free
software project.

Creating and distributing a package using your PPA is simple:

1. Create a source package.
2. Verify that it builds on your own machine.
3. Upload it to Launchpad, where it will be built and published for the
   world to see.
4. Give your PPA's public archive URL to friends.

Managing PPAs
-------------

To install a PPA, you can add it to your apt sources:
``add-apt-repository ppa:user/ppa-name``

Make sure to update your apt packages before installing:
``apt update``

Removing a PPA can be done with: 
``add-apt-repository --remove ppa:user/ppa-name``

Supported Ubuntu Versions
-------------------------
You can build your package against any currently supported version of Ubuntu, including active Long Term Support (LTS) releases and active interim releases. Launchpad automatically manages the build environments for these active targets.

For example, this includes target distributions such as Ubuntu 22.04 (Jammy), Ubuntu 24.04 (Noble), and Ubuntu 26.04 (Resolute), as well as current interim versions.

When you upload your source package, you specify the exact target distribution codename in your Debian changelog file to dictate which version it will be built for.

Note: While older releases transitioning into Expanded Security Maintenance (ESM) may still exist in corporate environments, Launchpad building capabilities generally mirror the actively maintained distribution cycles.

Team PPAs
---------

A team can have their own PPA too. This allows a group of developers to
collaborate on a set of packages. Anyone in the team can upload to the
team PPA, so it is a convenient way for a group to work together on a
whole bunch of packages which work together as a set.

Activating your PPA
-------------------

On your Launchpad profile page, look for an option to "Activate Personal Package
Archive". You will need to accept the terms of service, which basically
say that you will only use the free PPA system for free software
packages. At this point you can start uploading your source packages
immediately. Package builds can be actively monitored from the **Builds** page found in your PPA's Launchpad page.

Try the :ref:`Quick Start Guide for PPAs <personal-package-archive>` if you want to
learn more!
