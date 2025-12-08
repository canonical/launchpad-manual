==============================
Launchpad installation details
==============================

What the installation process does
----------------------------------

The ``rocketfuel-setup`` script first determines what release of Ubuntu
you're running, then installs various lines into files under ``/etc``, to
enable you to run Launchpad services locally.  For example, it adds entries
for "launchpad.test", "git.launchpad.test" and others to your ``/etc/hosts`` 
file, so that after you build Launchpad you can browse to ``launchpad.test`` 
and see a locally-running instance.  It also installs some packages, 
dependencies that Launchpad needs in order to run.  This is why the ``sudo`` 
access is necessary; consult the script for details of what it's doing.

Once it's got the system preparation out of the way, the script clones
Launchpad's Git repository (that's the ``launchpad`` directory above).  That
will take a while.

After it gets that, it fetches the other dependencies, the third-party
libraries, by invoking a separate script,
``launchpad/utilities/rocketfuel-get``.  That will take a while too, as
there are over 200 such libraries.

Once it has all the dependencies, it links them into the trunk working tree,
using the script ``launchpad/utilities/link-external-sourcecode``.

Do-it-yourself installation
---------------------------

**We only support using rocketfuel-setup to set up Launchpad.**  It adjusts
a lot of things to get the development process running smoothly, as
summarized above.  However, sometimes you might want to just get a build of
Launchpad to run its tests, or to run a script packaged with Launchpad, or
to do your own manual changes of the files that ``rocketfuel-setup`` would
normally touch.  These are the basics of what needs to be done for that
route - **unsupported hints**.

You'll need packages from a PPA: ``ppa:launchpad/ubuntu/ppa``.

.. code-block:: shell-session

    $ sudo apt-add-repository ppa:launchpad/ubuntu/ppa

Install the ``launchpad-developer-dependencies`` package.

Get the code:

.. code-block:: shell-session

    $ git clone https://git.launchpad.net/launchpad
    $ cd launchpad
    $ git clone --depth=1 https://git.launchpad.net/lp-source-dependencies download-cache
    $ make

Are there Launchpad packages available?
---------------------------------------

No, Launchpad is not packaged as a ``.deb`` or a snap or anything like that,
and there are no plans to do so.  Launchpad deployment is done straight from
Git branches.  We don't want to increase complexity further by adding a
packaging method that we wouldn't use ourselves.
