.. _personal-package-archives-highlights:

Personal Package Archives
=========================

.. include:: /includes/important_not_revised_help.rst

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

Your friends can then add your PPA's URL to their
``/etc/apt/sources.list`` file then install your packages just like
any other and receive automatic updates when you upload an updated
version.

Ubuntu versions
---------------

You can compile the package against any currently supported version of
Ubuntu. At the time of writing, that included Ubuntu 6.06 (Dapper),
Ubuntu 6.10 (Edgy), ubuntu 7.04 (Feisty) and Ubuntu 7.10 (Gutsy).
When you upload the package, you specify which version it is designed to
be built for.

Team PPAs
---------

A team can have their own PPA too. This allows a group of developers to
collaborate on a set of packages. Anyone in the team can upload to the
team PPA, so it is a convenient way for a group to work together on a
whole bunch of packages which work together as a set.

Activating your PPA
-------------------

On your home page, look for an option to "Activate Personal Package
Archive". You will need to accept the terms of service, which basically
say that you will only use the free PPA system for free software
packages. At this point you can start uploading your source packages
immediately. You can watch the build farm, which turns those source
packages into binaries, at work at https://launchpad.net/+builds

Try the :ref:`Quick Start Guide for PPAs <personal-package-archive>` if you want to
learn more!
