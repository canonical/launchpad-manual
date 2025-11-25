.. _troubleshoot-package-upload-errors:

Troubleshoot package upload errors
==================================

.. include:: /includes/important_not_revised_help.rst

Once you've made an upload either to your PPA or the official Ubuntu
archive, Launchpad will send you a success or failure notice by email.

.. note::
    If you do not receive a success or failure notice, please confirm that
    you have correctly signed your package and have used your corresponding
    email address in ``debian/changelog``.

Once a package is accepted you can check the status of your builds on your PPA's package listing (navigate to the relevant PPA from `your Launchpad page <https://launchpad.net/~>`_ and then "View package details"), or the `Ubuntu build queue <https://launchpad.net/ubuntu/+builds?build_text=&build_state=all>`_ if you're producing official Ubuntu packages.

Common errors
-------------

The upload appears to work but I don't get any email about it
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are two main reasons for this:

1. You failed to sign the .changes file on the source package that you uploaded.
2. The signing key that you used is not known to Launchpad, `you need to add it to your account <https://launchpad.net/~/+editpgpkeys>`_.

clearsign failed: secret key not available
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you get an error when signing the changes file (``clearsign failed: secret key not available``), pass an additional option ``-k[key_id]`` to debuild. You can use ``gpg --list-keys`` to get the key ID. Look for line similar to ``pub 12345/12ABCDEF``; the key is the alphanumeric section after the forward slash.

Source/binary (i.e. mixed) uploads are not allowed
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you get the following error when uploading the packages:

``Rejected: Source/binary (i.e. mixed) uploads are not allowed. This upload queue does not permit SECURITY uploads.``

pass the ``-S`` flag to ``debuild``.

Apparently successful upload followed by a rejection email
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you're uploading to a PPA, your upload may appear to succeed,
followed by an email with the following:

::

   Rejected:
   Signer has no upload rights at all to this distribution.
   Not permitted to upload to the RELEASE pocket in a series in the 'CURRENT' state.

This means that you forgot to specify your PPA's name on the
command-line (that is, the "my-ppa" part) and dput sent your upload to
the primary Ubuntu archive, for which you don't have authorisation. You
can disable that behaviour by adding these lines to your ``~/.dput.cf``:

::

   [DEFAULT]
   default_host_main = notspecified

   [notspecified]
   fqdn = SPECIFY.A.PPA.NAME
   incoming = .

Now, if you omit the PPA name you'll immediately get an error.

The rejection email may also say something like:

::

   Rejected:
   File <UPLOADED_FILE> already exists in <LOCATION>, but uploaded version has different contents.
   See more information about this error in https://documentation.ubuntu.com/launchpad/user/explanation/packaging/package-upload-errors/

This mean you have uploaded a file that already exists in the pointed
'LOCATION' (your PPA or Ubuntu primary archive) but with different
contents. Please note that you **must** give every upload a new version
number; Launchpad never permits reusing version numbers in the same
archive, even if they have been deleted.

If you did change the version number, this usually happens for re-packaged ``orig.tar.gz``. The
`Gzip <http://en.wikipedia.org/wiki/Gzip>`_ header includes a timestamp, resulting in files with different checksums for each individual compression step.

The solution for this problem consists of:

-  downloading the pristine original tarball from the location pointed in the rejection message;
-  regenerate the source upload using it, ``debuild -S`` will do it, note that there is no need to include the original tarball in the upload, a reference to the right file will suffice;
-  reupload the just created source package as usual, ``dput \``.

Or, the rejection e-mail may say something like:

::

   Rejected:
   Unable to find distroseries: unstable
   Further error processing not possible because of a critical previous error.

The problem here is that your debian/changelog file specifies a
distribution that is not present in Ubuntu. To solve this problem, edit
your debian/changelog file, and change the distribution at the top line
from "unstable" to something that fits Ubuntu (e.g. jaunty). Rebuild
your package and try to upload again.

Already uploaded to on ppa.launchpad.net
----------------------------------------

If after a rejected upload you try to upload the same source package
again and dput complains that the source package has already been
uploaded, it's because the logfile ``_source..upload`` exists. Just
remove the ``.upload`` file and re-run ``dput``, or invoke ``dput`` with the flag
``-f``.

Other errors
------------

If you come across other errors when uploading a package to Launchpad,
:ref:`contact the Launchpad team <get-help>`.
