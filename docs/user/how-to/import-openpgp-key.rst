.. _import-an-openpgp-key:

Import an OpenPGP key
=====================

OpenPGP allows you to sign documents, such as emails or text files, using a
digital key. Launchpad uses this key during a small number of tasks where it's
important to confirm your identity.

You can use most of Launchpad without OpenPGP. However, if you want to sign the
Ubuntu Code of Conduct or use the Bug Tracker's email interface, you will need
to register an OpenPGP key in your Launchpad account.

You may occasionally receive an email from Launchpad that has been encrypted to
your OpenPGP key, or signed by someone else's OpenPGP key. If you need help
viewing such messages in your mail reader, please see this guide to
`reading OpenPGP signed mail <https://www.openpgp.org/software/>`_.

.. TODO: ReadingOpenPgpMail not in GH

OpenPGP uses two types of digital keys: one public, one private. Each time you
sign a document, OpenPGP appends a unique code to it, produced using the
private key. That unique code is your digital signature and can be verified
with the public key.

Manage OpenPGP keys
-------------------

The easiest way to generate a new OpenPGP key in Ubuntu is to use the
"Passwords and Encryption Keys" tool.

Alternatively, you can use the GPG command-line tool to create and manage your
OpenPGP keys, which is available on most operating systems.

If you're using any operating system that doesn't come with GPG, see the
`GPG download page <http://gnupg.org/download/index.en.html>`_. You may also
prefer to follow the
`GPG manual <http://www.gnupg.org/gph/en/manual.html#AEN26>`_.

For the purposes of this guide, we assume you're using the "Passwords and
Encryption Keys" tool in Ubuntu.

Creating your OpenPGP keys
^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Open "Passwords and Encryption Keys"

#. Create a new "PGP Key", and follow the on-screen instructions.

You should see your new key listed in the tool.

Publishing your key to a keyserver
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Open "Passwords and Encryption Keys".

#. With your key selected, go to the "Sync and Publish keys" option from
   the menu.

#. If it's the first time publishing your key, you may need to add a key
   server. Select the "Key Servers" button and select "Add keyserver": you
   should select  "HTTP Key Server" and enter ``keyserver.ubuntu.com`` as the
   server address.
   Once you have your server set up, select option
   ``hkp://keyserver.ubuntu.com`` from the "Publish keys to" drop-down.

#. Select "Sync"

It can take up to thirty minutes before your key is available to Launchpad.
After that time, you're ready to import the key into into Launchpad.

Importing your key into Launchpad
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. From the "Passwords and Encryption Keys" tool, retrieve the Fingerprint from
   your new key. You should see it be opening the new PGP key.

#. Visit your `OpenPGP keys <https://launchpad.net/~/+editpgpkeys>`_ page.
   This will prompt you to log in again.

#. Paste the fingerprint into the Fingerprint text-box, then import the key.
   Launchpad will use the fingerprint to check the Ubuntu key server for your
   key and, if successful, send you an encrypted email to your Launchpad email
   address asking you to confirm the key import.

#. Check the email account associated with your Launchpad account.
   If your email client supports OpenPGP encryption, it will prompt you for the
   password you chose for the new key.

   .. tip::
      Launchpad encrypts the email, using your public key, so that it can be
      sure that the key is yours. If your email software doesn't support
      OpenPGP encryption, copy the encrypted email's contents (including the 
      ``-----BEGIN PGP MESSAGE-----`` and ``-----END PGP MESSAGE-----`` lines),
      type ``gpg`` in your terminal, then paste the email contents into your
      terminal window, followed by ctrl-D (an 
      `EOF <http://en.wikipedia.org/wiki/End-of-file>`_ character).

#. Follow the instructions in the email to complete the key import process. The
   email will redirect you to a Launchpad page where you can confirm the key
   import.

You can now sign the Ubuntu Code of Conduct and use the Bug Tracker's email 
interface.

Renewing your key
^^^^^^^^^^^^^^^^^

You may have set your key to expire. You can update your key's expiration date
and republish it.

#. Open "Passwords and Encryption Keys".

#. Select the "GnuPG keys" tab, select your key and open the property window.

#. Update the "Expires" date.

#. With your key still selected, go to select "Sync and Publish Keys" from
   the menu, and select "Sync".
