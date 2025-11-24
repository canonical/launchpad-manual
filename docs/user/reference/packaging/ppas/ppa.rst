.. _personal-package-archive:

Personal Package Archive
========================

.. include:: /includes/important_not_revised_help.rst

Using a Personal Package Archive (PPA), you can distribute software and
updates directly to Ubuntu users. Create your source package, upload it
and Launchpad will build binaries and then host them in your own apt
repository.

That means Ubuntu users can install your packages in just the same way
they install standard Ubuntu packages and they'll automatically receive
updates as and when you make them.

Every individual and team in Launchpad can have one or more PPAs, each
with its own URL.

Packages you publish in your PPA will remain there until you remove
them, they're superseded by another package that you upload or the
version of Ubuntu against which they're built becomes obsolete.

.. note::
    :ref:`consumer-hosting` allow you to have private PPAs.

.. note:: 
    We do not allow uploading pre-built binary packages.

Size and transfer limits
------------------------

New PPAs get 8 GiB of disk space. If you need more space for a
particular PPA, `ask us <https://answers.launchpad.net/soyuz>`_.

While we don't enforce a strict limit on data transfer, we will get in
touch with you if your data transfer looks unusually high.

Supported architectures
-----------------------

When Launchpad builds a source package in a PPA, by default it creates
binaries for amd64.

You may also request builds for arm64, armhf, i386, powerpc, ppc64el, riscv64
and/or s390x. Use the "Change details" page for the PPA to enable the
architectures you want.

Changing the set of architectures for which a PPA builds does not create
new builds for source packages that are already published in that PPA;
it only affects which builds will be created for new uploads. If you
need to create builds for newly-enabled architectures without
reuploading, go to "View package details" and then "Copy packages",
select all the packages for which you want to create builds, select
"This PPA", "The same series", and "Copy existing binaries", and submit
the form using the "Copy Packages" button.

We use OpenStack clouds for security during the build process,
ensuring that each build has a clean build environment and different
developers cannot affect one another's builds accidentally. These clouds
do not yet have support for the powerpc and s390x architectures; when
they do, it will also be possible to request those architectures in
PPAs.

Supported series
----------------

When building a source package you can specify one of the supported series in your `changelog file <https://canonical-ubuntu-packaging-guide.readthedocs-hosted.com/en/latest/reference/debian-dir-overview/#the-changelog-file>`_, which are listed at `the Launchpad PPA page <https://launchpad.net/ubuntu/+ppas>`_.

If you specify a different series the build will fail.

Supporting multiple series
--------------------------

If you want to provide a package for multiple series, you can do one of
the following:

-  build the package for the oldest of the releases you care about, then once the build has finished and been published, :ref:`copy <copying-packages>` the binaries forward to the newer releases (e.g. build for bionic and then publish those binaries for focal and jammy as well).

-  create one source package version per release. People taking the "one source package version per release" approach often end up automating it using :ref:`source-package recipes <building-a-source-package>`.

Activating a PPA
----------------

Before you can start using a PPA, whether it's your own or it belongs to a team, you need to activate it on your `profile page <https://launchpad.net/people/+me/>`_ or the team's overview page. If you already have one or more PPAs, this is also where you'll be able to create additional archives.

Your PPA's key
~~~~~~~~~~~~~~

Launchpad generates a unique key for the user's default PPA and reuses it to
sign any packages built in the user's PPAs.

This means that people downloading/installing packages from your PPA can
verify their source. After you've activated your PPA, uploading its
first package causes Launchpad to start generating your key, which can
take up to a couple of hours to complete.

Your key, and instructions for adding it to Ubuntu, are shown on the
PPA's overview page.

Deleting a PPA
--------------

When you no longer need your PPA, you can delete it. This deletes all of
the PPA's packages, and removes the repository from
``ppa.launchpad.net``. You'll have to wait up to an hour before you can
recreate a PPA with the same name.

Upload permissions
------------------

Upload permissions are usually bound to the ppa-owning team. If you want
to grant upload permissions to somebody, but you do not want to add them
to the team, you can use the https://code.launchpad.net/ubuntu-archive-tools as following:

::

   edit-acl -A ppa:OWNER/ubuntu/ARCHIVE -p PERSON -c main -t upload add



Further information
-------------------

You can familiarise yourself with how PPAs work by :ref:`installing a package from an existing PPA <install-software-from-ppas>`. You can also jump straight into :ref:`uploading your source packages <upload-a-package-to-a-ppa>`.


Frequently Asked Questions
--------------------------

Non-Technical Questions
~~~~~~~~~~~~~~~~~~~~~~~

Can anybody have a PPA?
^^^^^^^^^^^^^^^^^^^^^^^

Yes, this service is available to any developer who wants to publish packages
of their free software code. You need a Launchpad account, you will also need
a GPG key to sign your source code uploads and you will need to accept the Terms
of Service which include the Ubuntu Code of Conduct.

Can I publish any software in a PPA?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This is a free service for free software developers and licensing is limited to those which are specified in the :ref:`PPA terms of use <project-eligibility>`. We may make this service available to commercial software developers too, and would be happy to hear from you if you think that would be useful for you.

What other limitations apply to the PPA service?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Other than the expectation that packages in your PPA are free software, we do ask that you not abuse the build system with unnecessary builds or automated uploads of large numbers of packages. We will monitor the total amount of build time per user and ask folks to be reasonable in their use of the shared resources in the PPA pool. Developers and teams each start with 1 gigabyte of storage space freely available in their PPA's for source and binary packages. We will not accept uploads of packages that are unmodified from their original source in Ubuntu or Debian, only packages that include your own changes. We ask that people include useful changelogs for each package so that users and other developers can understand what new features they are exploring in their work. Read the :ref:`PPA terms of use <project-eligibility>` for more information.

How long are packages published?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Packages will remain published until either you remove them yourself, or you
supersede them with newer versions, or the underlying release of Ubuntu against which they
were built becomes obsolete and unmaintained.

What formats of packages are supported?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

At this stage only .deb packages are supported. If you are interested in 
building RPM or other package formats, please contact the :ref:`Launchpad team <get-help>` 
to discuss that in more detail!

How many users can download packages from my PPA?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

There are no limits on the number of users you can point at your PPA.
We would encourage you to build communities of users and testers around your PPA,
and there are no bandwidth restrictions on downloads from any PPA.

How many PPAs can I have?
^^^^^^^^^^^^^^^^^^^^^^^^^

Each user and team in Launchpad can have a single public PPA. If you want to have different
versions of the same package, testing different features or focused on different use cases,
then we would encourage you to create a new team and use the PPA for that team. That way,
for example, you can have a team of people interested in "server" issues that has one
version of the Apache package, and another interested in "workstation" issues that has
a different version of the same package, each in a different PPA. Please don't abuse this capability!

My PPA has reached the 8GB limit. What can I do?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If your PPA has reached the 8GB limit, there are a few things you can do.

The easiest option is to remove packages from it. While obvious, it isn't always obvious that packages may not have been automatically superseded in the archive; this happens, for instance, when the package name varies. Pay particular attention to packages that have ``.orig.tar.gz`` files that are used by multiple versions; those packages will only be superseded when all packages that use that ``.orig`` file have also been superseded.

If you believe you have good reason to request additional disk space, file a question with a written justification at `<https://answers.launchpad.net/soyuz>`_ and it will be considered. A Launchpad admin will consider your request and either defer it or provide you with alternative advice.


Technical Questions
~~~~~~~~~~~~~~~~~~~

Why do builds fail?
^^^^^^^^^^^^^^^^^^^

A build can failed for lot of reasons, obviously it will fail if the source or the package metadata is broken it it will be indicated in Launchpad as ``failed-to-build``, the only alternative available for such failures is to check the buildlog and fix the code accordingly. Another possible cause of failures is unsatisfied dependencies, indicated by the ``dep-wait`` , it means that one or more dependencies required by the source package could not be reached during the build. The uploader has to investigate if it is a transient failure, when the dependencies will be available in the near future, and in this case Launchpad will retry the package automatically when all dependencies get satisfied. On the other hand, it might be possible that you've got the dependencies wrong and them you have upload a fix for it. System failures, like ``chroot-wait`` or ``builder-failure`` are very rare and should be informed to the Launchpad developers if they happen. ``failed-to-upload`` in basic terms means that despite of built without errors the produced binaries do not fit the current PPA state, it usually means that the source have produced broken or duplicated binaries that can't be published, it usually required a new upload. Either way, Launchpad will inform the source uploader about any of the described failures via email.

I get an error about a orig.tar.gz mismatch
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Your uploaded source package may refer to an orig.tar.gz file in the primary Ubuntu archive (which saves upload time and bandwidth). If the checksum or file size provided in the ``.dsc`` file of the source package does not match those of the file already known to Launchpad, your upload will be rejected.

I get an error about versions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When you upload a package, its version must exceed that of any existing package of the same name in the same Ubuntu distribution in your PPA. For more information, see the `Debian Policy Manual on versioning <https://www.debian.org/doc/debian-policy/ch-controlfields.html#version>`_. You can also use ``dpkg --compare-version`` to check version numbers before uploading your package.

Why can't I upload the same version for multiple releases?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The PPA disk topology (``debian pool``) groups all files, sources and binaries, in a name-based location, allowing multiple indexes (``dists``) to refer to the same source/binaries indicating they are published in multiple releases. It implies that the user only have to upload a source version once to a PPA/distribution and it is possible handle publication **copies** across all releases. The ability to copy publications across releases is already available by requests (ask a question at `<https://answers.launchpad.net/soyuz>`_) and will be soon provided for PPA owner, see `bug 189233 <https://bugs.launchpad.net/soyuz/+bug/189223>`_

I'm trying to upload a binary. Why does it get rejected?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

PPA only supports uploading source packages. PPA will build binary
packages for you from the uploaded source.

I get an error about no orig.tar.gz in archive
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

All source packages must contain an ``orig.tar.gz`` file, or
refer to an existing one in the Ubuntu archive or your PPA.

My build is in DEPWAIT. What does that mean? What do I do?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Your source package requires another package to be able to build successfully, which does not exist yet. This can be caused by your source package having incorrect dependencies, or can be caused because a dependent source package has not been uploaded and built yet. In the latter case, your package will be automatically re-built (as of Launchpad 1.1.12) as soon as the dependencies are available.

Does my stuff get automatically copied over to the Ubuntu archive? Why not?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Your PPA is totally separate to the Ubuntu archive and is for your personal use only, where you are free to upload any package you like. In contrast, the Ubuntu archive is very carefully maintained for security and updates, and each uploaded package there is approved by the archive administrators.

Why does my package not have an orig.tar.gz?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If a package does not have an ``orig.tar.gz`` file it's because it's not the first version of the package. When uploading newer versions of a package, we can refer to the existing ``orig.tar.gz`` because it never changes.

Does PPA only do one release? How do I make it do another release?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

PPA supports all active Ubuntu releases. To upload to another release, you need to specify
this in the Distribution field of your source package's debian/changelog file.

What's this dput.cf stuff? What do I have to modify? I can't seem to follow the how-to guide correctly.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``dput.cf`` configures the ``dput`` tool, as suggested in the :ref:`Upload a package to a PPA <upload-a-package-to-a-ppa>` you have to modify the given template to match your Launchpad details (user-name). Be sure that you refer to the specific target you've edited when uploading your source (``dput my-ppa <source>.changes``) and also don't forget to sign it with a key already referenced in Launchpad as yours.

How does this stuff differ from the Ubuntu archive? and REVU?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

PPA infrastructure is identical to the Ubuntu Primary archive, but it's a separate setup. It ie meant to provide a flat-learning-curve for users already used to the ubuntu/debian development tools. All the tools, procedures and features tend to be the same and shared between PPAs and ubuntu Primary archive. Our goal is to provide the shortest path between developers able to get things fixed or to add innovation to ubuntu context and the ubuntu users. `REVU <https://wiki.ubuntu.com/MOTU/Packages/REVU/>`_ is a parallel system currently maintained and used by `MOTU <https://wiki.ubuntu.com/MOTU/>`_ members to have structured and transparent procedures for "producing and reviewing new packages". PPAs will be soon provide similar features.

Additional information about upload issues is a available at :ref:`troubleshoot-package-upload-errors`.
