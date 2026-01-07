.. _install-software-from-ppas:

Install software from PPAs
==========================

PPAs work like normal Ubuntu archives. You can install software in the
usual way -- for example, through ``apt-get`` or ``synaptic`` --
and whenever there's an update Ubuntu will prompt you to install it.

To start installing software from a PPA, you need to tell Ubuntu where
to find it and how to verify the integrity of the packages.

Add a PPA to your Ubuntu system
-------------------------------

.. important::
    This is not an endorsement of any of the software in
    PPAs. You must make sure you trust the PPA owner before installing their
    software.

- Visit the PPA's overview page in Launchpad and look for the
  heading that reads ``Adding this PPA to your system``. Make a note of the
  PPA's location, which looks like:

::

   ppa:gwibber-daily/ppa

- Open a terminal and enter:

::

   sudo add-apt-repository ppa:user/ppa-name

Replace ``ppa:user/ppa-name`` with the PPA's location that you noted
above.

Your system will now fetch the PPA's key. This enables your Ubuntu
system to verify that the packages in the PPA have not been interfered
with since they were built.

- Now, as a one-off, you should tell your system to pull down
  the latest list of software from each archive it knows about, including
  the PPA you just added:

::

   sudo apt-get update

Now you're ready to start installing software from the PPA! If you
already have the software installed and you're adding the PPA to get a
more recent/different version, you may just need to run:

::

   sudo apt-get dist-upgrade

Next steps
----------

To publish software in your own PPA, you need to :ref:`build a source package <building-a-source-package>`.
