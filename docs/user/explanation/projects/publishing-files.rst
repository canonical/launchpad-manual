.. _making-your-project-files-available-for-download:

Making your project files available for download
================================================

.. include:: /includes/important_not_revised_help.rst

After all the work that's gone into a release, you want to make sure
people can get hold of it. One way to distribute your software through
Launchpad is to publish files for download.

First up, you need to record the :ref:`release <releases>` in Launchpad.
You can register a release from a series milestone; or, from the series
page, you can register a release and create the milestone at the same
time. Next, make sure your files fall into one of the following
categories:

-  code release tarball
-  installer files
-  README or other documentation
-  changelog file
-  release notes.

Each individual file must be no more than 1 GiB and you must be the:

-  project maintainer
-  project driver
-  or the series release manager.

To upload a file, visit the release's overview page and click ``Add
download file``.

Downloading files
-----------------

Let's take a look at `launchpadlib's downloads page <https://launchpad.net/launchpadlib/+download>`_.

Here, files are grouped by series (major lines of development) and then
by release. An MD5 checksum and the GPG signature of the uploader -
where they've made it available - are available for each file.


Further information
-------------------

Keeping people up to date with your project's news is an important way
of building community around and interest in your project. Launchpad's
:ref:`project announcements <publishing-project-announcements>` let you publish news
both on Launchpad and more widely by Atom feed.
