Getting the source code
=======================

.. include:: ../includes/important_not_revised.rst

Getting the Launchpad source code is fairly simple, but it's not the usual
process of "download a package, unpack, build, and install".  Since we do new
rollouts of Launchpad directly from Git repositories anyway, that's how we
distribute the source code to developers.  There are no plans to package
Launchpad; its deployment is quite complex.

Note that right now, Launchpad can only be built and run on Ubuntu 16.04 LTS or
newer. That's not a design decision, it's just a consequence of the fact that,
until now, all its developers have been running Ubuntu.  We'd be happy to see
Launchpad work on other platforms too; perhaps starting with
`Debian GNU/Linux`_ would be easiest, since Debian and Ubuntu are similar and
many Debian developers use Launchpad anyway.

.. _Debian GNU/Linux: http://debian.org/


The images/icons are still copyrighted traditionally, to protect Launchpad's
visual identity. But they're shipped with the code and are fine to use for
development and testing purposes. Just if you launch a production server, it
needs to look different -- and have a different name, of course, as "Launchpad"
is a trademark. From our point of view, we have open-sourced Launchpad to
improve our hosted service.

Overview
--------

Launchpad is a core of service-specific code surrounding various third-party
libraries, some of which are installed. So the process of fetching Launchpad to
build it looks something like this: grab the core code, grab all the libraries,
unpack them into the right places in the tree, and then build the whole thing.

Fortunately, we've written scripts to take care of most of that, and
instructions on using those scripts are below.

Getting it
----------

To build and run a Launchpad development instance, see
:doc:`Running <running>`.

If you just want to grab the development source code branch:

code::

    git clone https://git.launchpad.net/launchpad


To learn about alternative "trunk" branches, see XXX Trunk.


Where to get help
-----------------

We're standing by to help; see the XXX Help.
