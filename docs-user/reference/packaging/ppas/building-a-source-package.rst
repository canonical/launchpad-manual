Building a source package
=========================

Ubuntu uses Debian's system of packaging software. To get software into
a PPA, you need to build a source package. That includes the source code
for the software you want to distribute, along with the instructions for
where the application should live in the file system and of any
dependencies it has on other software.

.. note::
    If you're already familiar with building .deb source packages
    for Ubuntu, you can skip straight to the `Versioning <#versioning>`__ section.

You can learn how to create .deb packages for Ubuntu by following the
`Ubuntu packaging guide <http://packaging.ubuntu.com/html/>`__.

There are a couple of aspects of PPAs that work slightly differently to
standard Ubuntu packages: **versioning** and **dependencies**. You
should also ensure that the email address and GPG key you use with dput
are the same as those associated with your Launchpad account.

Versioning
----------

Ubuntu package names are suffixed by the version number of the package.
This allows Ubuntu to distinguish newer packages from older ones and so
remain up to date.

If you're creating an alternative version of a package already available
in Ubuntu's repositories, you should ensure that:

-  your package supersedes the official Ubuntu version
-  future Ubuntu versions will supersede your package.

To do this, add the suffix ppa\ *n* (where *n* is your package's
revision number). Two examples:

-  Ubuntu package `myapp_1.0-1` → PPA package `myapp_1.0-1ppa1`
-  Ubuntu package ``myapp_1.0-1ubuntu3` → PPA package
   `myapp_1.0-1ubuntu3ppa1``

Version numbers must be unique. This has implications if you want to
provide packages for multiple Ubuntu series at once:

If your package can be used on different versions of Ubuntu *without
being recompiled* then use the naming scheme already described, and
start by uploading your package to the oldest series that you want to
support. When you have successfully uploaded your package to your PPA
you can copy the existing binaries to the new series; see `Copying
packages <Packaging/PPA/Copying>`__, and use the "Copy existing
binaries" option.

If your package does need to be recompiled to support multiple Ubuntu
series, then you should add a suffix of a tilde and the series version
to the version number. So a package for the Yakkety Yak (16.10) could be
named \``myapp_1.0-1ubuntu3ppa1~ubuntu16.10.1`\` and for the Xenial
Xerus (16.04) \``myapp_1.0-1ubuntu3ppa1~ubuntu16.04.1``. If you need to
release an updated package, increment the ppa\ *n* suffix. It is
important to note that specifying the version name here doesn't change
the series that you are targetting; this must still be set correctly as
described in the Ubuntu packaging guide's section on the `changelog
file <http://packaging.ubuntu.com/html/debian-dir-overview.html#the-changelog>`__.

Snapshots
~~~~~~~~~

You need snapshots when

-  you want to release previews of your software for interested people
-  you want to have a separation between stable code and code in
   development
-  released versions cannot be uploaded twice so version numbers are
   increasing too quickly
-  you want to test your uploads and do not want to clutter your stable
   versions PPA

For this purpose you must create a PPA dedicated for snapshots. You and
interested user can add this PPA to their update repositories.

For naming a snapshot you must assure that the final release version
will supersede the snapshot version and that any new snapshot version
supersedes a previous snapshot version. To do this you cannot name the
snapshot version like the final release version. You must use a *lower*
version number. Debian/Ubuntu versions are sorted by their ASCII code.
Because a snapshot is always heading to the next version use the pattern
\`+\` at the place where the version number will change, e.g. when
moving from \`1.0\` to \`1.1\` use \`1.0+1`. You cannot use \`1.1\`
directly because the release version number will not supersede the
snapshot version number in this case. To guarantee that each snapshot
version supersedes a previous snapshot version you should also attach a
\`SNAPSHOT\` qualifier.

To sum up a complete snapshot version number example would look like:

\`myapp_1.0+1SNAPSHOT20120613154859+0200-0ubuntu1ppa1~precise\`

Dependencies
------------

Launchpad satisfies your package's

::

   Build-Depends

using:

-  the most recent versions of the packages in the PPA you're uploading
   to
-  all sections of the primary Ubuntu archive -- i.e. main, restricted,
   universe and multiverse
-  **optionally:** other PPAs in Launchpad.

.. note::
    If you're already familiar with uploading to the Ubuntu primary archive, you should note that PPA builds do not have any build
    dependency restrictions, unlike a build in the primary Ubuntu archive. If you want to build the same package in the primary Ubuntu archive at a
    later point you may need to revise the package's component and/or pocket.

Depending on other PPAs
~~~~~~~~~~~~~~~~~~~~~~~

If you want Launchpad to satisfy your package dependencies using one or
more other PPAs, follow the ``Edit PPA dependencies`` link on `your
PPA <https://launchpad.net/people/+me/+archive>`__.

Options when building
---------------------

How you build your package depends on whether you're creating a brand
new package or you're creating a derivative of a package that's already
in Ubuntu's primary archive.

If you're creating an alternative version of a package that's already in
Ubuntu's primary archive, you don't need to upload the
``.orig.tar.gz`` file, i.e. the original source.

So, the ``debuild`` options you'd use are:

-  **alternative version of an existing package (will be uploaded
   without the .orig.tar.gz file):** ``debuild -S -sd``
-  **brand new package with no existing version in Ubuntu's repositories
   (will be uploaded with the .orig.tar.gz file):** ``debuild -S
   -sa``

.. note::
    If you get the error ``clearsign failed: secret key not available`` when signing the changes file, use an additional optionally
--list-secret-keys`` to get the key ID. Look for a line like ``sec 12345/12ABCDEF``; the part after the slash is the key ID.

Further information
-------------------

Now that you have a source package, you need to `upload
it <Packaging/PPA/Uploading>`__!