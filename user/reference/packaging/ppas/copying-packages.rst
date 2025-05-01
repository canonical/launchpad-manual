Copying packages
================

You can copy packages from other PPAs into any PPA that you can upload
to. You also have the option of copying packages between distro-series
(i.e different distribution releases).

For example: take a look at the `Launchpad team's PPA copy
packages <https://launchpad.net/~launchpad/+archive/ubuntu/ppa/+copy-packages>`__
page.

Here you can:

-  select one or more sources to copy
-  select the destination PPA - you must have upload permission for that
   archive
-  specify the destination series
-  choose whether or not to also copy the related binary package.

As soon as you request the copy, the source will be listed in your PPA
with details of it origin. However, it can take up to twenty minutes for
the files to actually appear in your archive.

If you only copy the source, the corresponding build records are created
in the destination PPA immediately.

Copy Errors
-----------

Version numbers need to be unique
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once a version number is used, you cannot reuse it for the same archive
/ PPA.

When you try to copy packages to an archive or a PPA where the version
number already exists, you will see an error message as following:

::

   Copying failed ... (binaries conflicting with the existing ones)

This holds true even when you remove the packages.

Now you can choose any of the following ways forward:

-  bump the version number
-  use a different archive / PPA
-  delete and recreate the PPA