.. _import-an-openpgp-key:

Import an OpenPGP key
=====================

.. include:: /includes/important_not_revised_help.rst


OpenPGP allows you to sign documents, such as emails or text files, using a digital key. Launchpad uses this key during a small number of tasks where it's important to confirm your identity.

You can use most of Launchpad without OpenPGP. However, if you want to sign the Ubuntu Code of Conduct or use the Bug Tracker's email interface, you will need to register an OpenPGP key in your Launchpad account.

You may occasionally receive an email from Launchpad that has been encrypted to your OpenPGP key, or signed by someone else's OpenPGP key. If you need help viewing such messages in your mail reader, please see this guide to `reading OpenPGP signed mail <https://www.openpgp.org/software/>`_.

.. TODO: ReadingOpenPgpMail not in GH

OpenPGP uses two types of digital keys: one public, one private. Each time you sign a document, OpenPGP appends a unique code to it, produced using the private key. That unique code is your digital signature and can be opened only with the public key.

Using Passwords and Encryption Keys to manage OpenPGP keys
----------------------------------------------------------

The easiest way to generate a new OpenPGP key in Ubuntu is to use the *Passwords and Encryption Keys* tool. If you are using Ubuntu 10.04 or an earlier version, it is located at *Applications & Accessories & Passwords and Encryption Keys*. In Ubuntu 10.10 and later versions, it is located at *System & Preferences & Passwords and Encryption Keys*

Creating your OpenPGP keys
^^^^^^^^^^^^^^^^^^^^^^^^^^

**Step 1:** Open *Passwords and Encryption Keys*.

**Step 2:** Select *File & New*, select *PGP Key*, and then follow the on-screen instructions.

Now you'll see your new key listed in the *Passwords and Encryption Keys* tool.

Publishing your key to a keyserver
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Step 1:** Open *Passwords and Encryption Keys*.

**Step 2:** Select the *My Personal Keys* tab, select your key.

**Step 3:** Select *Remote & Sync and Publish Keys* from the menu. Choose the Sync button (you may need to add ``hkp://keyserver.ubuntu.com`` to your key servers if you are not using Ubuntu).

It can take up to thirty minutes before your key is available to Launchpad. After that time, you're ready to import key into into Launchpad.

Importing your key into Launchpad
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

OpenPGP uses two types of digital keys: one public, one private. Each time you sign a document, OpenPGP appends a unique code to it, produced using the private key. That unique code is your digital signature and can be opened only with the public key.

**Step 1:** Open *Passwords and Encryption Keys*.

**Step 2:** Select the *My Personal Keys* tab, select your key and open the property window by pressing Space Bar or double clicking with your pointer. Select the *Details* tab of the property window.

**Step 3:** Select the *Fingerprint* text (the ten blocks of numbers and letter). Copy the text by pressing the control+c keys together.

**Step 4:** Visit your `OpenPGP keys <https://launchpad.net/people/+me/+editpgpkeys>`_ page.

**Step 5:** Paste the fingerprint that you copied in step 3 into the Fingerprint text-box, then click the Import Key button. Launchpad will use the fingerprint to check the Ubuntu key server for your key and, if successful, send you an encrypted email asking you to confirm the key import.

**Step 6:** Check the email account that Launchpad has sent the confirmation email to. If your email client supports OpenPGP encryption, it will prompt you for the password you chose for the key when GPG generated it. Enter the password, then click the link to confirm that the key is yours.


.. tip::
   Launchpad encrypts the email, using your public key, so that it can be sure that the key is yours. If your email software doesn't support OpenPGP encryption (for Thunderbird, try the Enigmail extension), copy the encrypted email's contents, type gpg in your terminal, then paste the email contents into your terminal window, followed by ctrl-D (an `EOF <http://en.wikipedia.org/wiki/End-of-file>`_ character).

**Step 7:** Back on the Launchpad website, use the Confirm button and Launchpad will complete the import of your OpenPGP key.

Launchpad will confirm that it has imported your key.

.. note::

   If you created the key id using an email address not registered in your Launchpad account, use the Confirm Them button to use it with Launchpad.

You can now sign the Ubuntu Code of Conduct and use the Bug Tracker's email interface.

Renewing your key
^^^^^^^^^^^^^^^^^

You may have set your key to expire. You can update your key's expiration date and republish it.

**Step 1:** Open *Passwords and Encryption Keys*.

**Step 2:** Select the *My Personal Keys* tab, select your key and open the property window by pressing Space Bar or double clicking with your pointer. Select the *Details* tab of the property window.

**Step 3:** Set a new expiration date or choose never. Close the property window

**Step 4:** With you key still selected, select *Remote & Sync and Publish Keys* from the menu. Choose the Sync button.

Using GPG to manage OpenPGP keys
--------------------------------

OpenPGP uses two types of digital keys: one public, one private. Each time you sign a document, OpenPGP appends a unique code to it, produced using the private key. That unique code is your digital signature and can be opened only with the public key.

You can create and manage OpenPGP keys using the GPG tool. If you're running Ubuntu, and most other Linux-based operating systems, GPG is ready to use.


.. note::
   If you're using any operating system that doesn't come with GPG, see the `GPG download page <http://gnupg.org/download/index.en.html>`_. You may also prefer to follow the `GPG manual <http://www.gnupg.org/gph/en/manual.html#AEN26>`_.

Creating your OpenPGP keys with gpg
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Step 1:** Open a terminal and type::

   gpg --gen-key

**Step 2:** GPG will now ask you a number of questions about the type of key you want to generate. Don't worry if you're unsure what to do, follow the steps below to select the default option each time. The first question asks what type of key you want to generate. Press `Enter` to select the default.

**Step 3:** Press `Enter` again, to select the default key size.

**Step 4:** You can choose to set an expiry date for your key. Expiry dates are useful if you're dealing with highly secure content. Press `Enter` to choose a non-expiring key, then press `y` followed by `Enter` to confirm.

**Step 5:** To help identify your key, GPG combines your name, email address and any comment you choose. Enter your real name, when prompted, then press `Enter`.

**Step 6:** Enter the email address that you're most likely to use with your Launchpad account, then press `Enter`.

**Step 7:** Optionally, you may enter a comment, such as ``My test OpenPGP key``, then press `Enter`.

**Step 8:** GPG will show you its proposed id for the key. For example::

   You selected this USER-ID:
       "John Doe (My test OpenPGP key) <john.doe@test.com>"


If you're happy with the id, press the letter `O` (for "Okay"), then `Enter`.

**Step 9:** You must protect your key with a password. Enter, then confirm, a password that other people can't easily guess but that is memorable to you.

.. important::

   If you forget this password there is no way to retrieve it and your key will become useless.

**Step 10:** GPG will now generate your keys. To increase the strength of your keys, you should type randomly on your keyboard. This gives GPG extra entropy from which to generate your keys.

Your keys are now stored as ``public.key`` and ``private.key`` in the current directory.

**Step 11:** Check that your key has been generated by typing ``gpg --list-keys`` and, if successful, you'll see a message similar to::

    pub   1024D/12345678 2007-01-26
    uid                  John Doe (My test OpenPGP key) <john.doe@test.com>
    sub   2048g/9ABCDEF1 2007-01-26

Make a note of the *pub* id, which is ``12345678`` in the example above.

**Step 12:** Launchpad doesn't store your key directly, so you need to export your public key to a key server, such as ``keyserver.ubuntu.com``::

    gpg --keyserver keyserver.ubuntu.com --send-keys 12345678

Replace ``12345678`` with the pub id you noted in step 11.

If successful, GPG will display a message similar to::
   
    gpg: sending key 12345678 to hkp server keyserver.ubuntu.com

Importing your key into Launchpad with gpg
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can generate both keys using the GPG tool. If you're running Ubuntu, and most other Linux-based operating systems, GPG is ready to use.

**Step 1:** Launchpad identifies your OpenPGP key by its fingerprint. In your terminal, you can ask GPG for your key's fingerprint by typing::

    gpg --fingerprint

GPG will display a message similar to::

    pub   1024D/12345678 2007-01-26
    Key fingerprint = 0464 39CD 2486 190A 2C5A  0739 0E68 04DC 16E7 CB72
    uid   John Doe (My test OpenPGP key) <john.doe@test.com>
    sub   2048g/ABCDEF12 2007-01-26

Highlight and copy only the numeric fingerprint: ``0464 39CD 2486 190A 2C5A 0739 0E68 04DC 16E7 CB72`` in the example above.

**Step 2:** Visit your `OpenPGP keys <https://launchpad.net/people/+me/+editpgpkeys>`_ page

**Step 3:** Paste the fingerprint that you copied in step 1 into the Fingerprint text-box, then click the Import Key button. Launchpad will use the fingerprint to check the Ubuntu key server for your key and, if successful, send you an encrypted email asking you to confirm the key import.

**Step 4:** Check the email account that Launchpad has sent the confirmation email to. If your email client supports OpenPGP encryption, it will prompt you for the password you chose for the key when GPG generated it. Enter the password, then click the link to confirm that the key is yours.

.. tip::

   Launchpad encrypts the email, using your public key, so that it can be sure that the key is yours. If your email software doesn't support OpenPGP encryption, copy the encrypted email's contents, type gpg in your terminal, then paste the email contents into your terminal window.

**Step 6:** Back on the Launchpad website, click the Confirm button and Launchpad will complete the import of your OpenPGP key.

Launchpad will confirm that it has imported your key.

.. note::

   If you created the key id using an email address not registered in your Launchpad account, click confirm them to use it with Launchpad.

You can now sign the Ubuntu Code of Conduct and use the Bug Tracker's email interface.

Next step
---------

Similarly, if you want to use some aspects of Launchpad's code hosting or Personal Package Archives, you need to :ref:`tell Launchpad about your SSH keys <import-your-ssh-keys>`.
