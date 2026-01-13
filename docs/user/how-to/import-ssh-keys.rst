.. _import-your-ssh-keys:

Import your SSH keys
====================

To push code branches to Launchpad you first need to generate your SSH key.
The key is made up of two parts: a private key that stays on your computer
and a public key that you register with Launchpad. As you might expect,
you shouldn't share the private key with anyone.

Why you need an SSH key
-----------------------

The trust that other people put in your Launchpad identity is
no more important than when they use code that you've uploaded to Launchpad.

An SSH key secures the connection between your computer and
Launchpad when you push code to it.

Creating the key
----------------

How you create your SSH key pair depends on which operating system you use.

If the instructions for your operating system are not here, see
:ref:`get in touch to request them <get-help>`.
If you know how to do this, please add the instructions to this page.

Launchpad supports RSA, ECDSA and ED25519 key types.

.. tab-set::

   .. tab-item:: Linux / macOS
      :sync: os-ssh

      -   Install OpenSSH. On Ubuntu, install the client by opening your
          terminal and typing::

              sudo apt-get install openssh-client

      -   Once OpenSSH is installed, stay in the terminal and type::

              ssh-keygen -a 100 -t ed25519

      -   When prompted, press Enter to accept the default
          file name for your key.

      -   Next, enter then confirm a password to protect your SSH key. 
          Your key pair is stored in ``~/.ssh/`` as ``id_ed25519.pub``
          (public key) and ``id_ed25519`` (private key).

      Now you need to upload the public portion of your SSH key to Launchpad.

      .. note::
          You may need to run ``ssh-add`` with the id file if you created
          an id file other than ``~/.ssh/id_ed25519``.
          Do ``ssh-add /path/to/file/id_ed25519_newfile``.
          If you’re on the Mac, you can execute the following on the
          command line::

              cat ~/.ssh/id_ed25519.pub | pbcopy

   .. tab-item:: Windows (PuTTY)
      :sync: os-ssh

      -   Download the PuTTY Key Generator from here: `http://www.chiark.greenend.org.uk/\~sgtatham/putty/download.html <http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html>`_

      -   Run puttygen.exe and click the generate button.
          PuTTYgen will ask you to move your mouse around in the
          blank area to generate entropy.

      -   Set a key passphrase and confirm it.

      -   Click "Save public key" and choose a location to save it.
          Click "Save private key" and choose a secure location to save it.
          **You must keep this secret key safe!**

      -   Do **not** close the PuTTYgen window yet. Copy the public key
          from the PuTTYgen window and register it in Launchpad. This helps
          avoid the "Invalid public key" error (see launchpad
          `question 26705 <https://answers.launchpad.net/launchpad/+question/26705>`_).

      -   Run or install Pageant. See:

          `http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html`_

          You can install Pageant as a standalone program or as part of the
          PuTTY package. Make sure Pageant is running and rt+click its
          notification-area icon to add the private key you saved earlier.
          This step is necessary to connect to Launchpad from a Windows PC.

   .. tab-item:: Cygwin / Windows (Pageant)
      :sync: os-ssh

      Follow these steps if you wish to use Pageant under Cygwin.

      -   Follow the procedure in the 'Windows (PuTTY)' section.

      -   Add ``GIT_SSH`` as an environment variable with the full path to
          ``plink.exe`` or just ``plink`` if that is already in your ``PATH``.

      -   Close all existing bash terminals and open a new terminal.

      -   Run ``plink INSERT_YOUR_USERNAME_HERE@git.launchpad.net`` and 
          accept 'yes' to store the server's host key

Registering the key with Launchpad
----------------------------------

-   If you are using Windows/PuTTY/PuTTYgen, open your public key in a
    text editor and copy its contents to the clipboard. The public key file
    has the extension ``.pub`` (for example: ``id_ed25519.pub``).

-   Visit your `SSH keys page <https://launchpad.net/~/+editsshkeys>`_.

-   Paste your public key into the text box and click the
    `Import public key` button to continue.

Using a custom SSH key for Launchpad
------------------------------------

You can safely use one SSH key per client machine to connect to multiple
hosts. Some people prefer a separate SSH keypair per service or per client
for flexibility when copying or revoking keys.

To do this:


#.  Generate a key to a non-default name, perhaps ``id_ed25519_launchpad``.
#.  Upload that key to Launchpad, as described above.
#.  Configure your SSH client to use this key. With OpenSSH,
    add these lines to your ``~/.ssh/config`` file::

        Host git.launchpad.net
         IdentityFile  /home/me/.ssh/id_ed25519_launchpad
         User launchpad-username

.. note::

    You need to upload the public key file (with ``.pub``) to Launchpad,
    and specify the private-key file (with no ``.pub``)
    in the SSH configuration.

Support for FIDO2 SSH Keys
--------------------------

Launchpad supports FIDO2 hardware-backed SSH key types: ``ed25519-sk`` and
``ecdsa-sk``. These keys use a hardware device such as a YubiKey or
Nitrokey to perform cryptographic operations and keep private keys off your
computer. They work anywhere Launchpad accepts SSH authentication, including
git+ssh and SFTP PPA uploads.

To generate a new key, run

.. code::

    ssh-keygen -t ed25519-sk -C "your@email.com"

or use ``ecdsa-sk`` for backwards compatibility. You will be asked to touch
your security key during creation, and OpenSSH will store the resulting
files in ``~/.ssh/``. To make a key resident (stored on the hardware device
and retrievable later), use the ``-O resident`` option:

.. code::

    ssh-keygen -t ed25519-sk -O resident -C "your@email.com"

Resident keys are useful if you use multiple machines or want a portable
login method tied to your hardware key. To register a new key on your
Launchpad account, visit: https://launchpad.net/~/+editsshkeys .

These key types offer strong protection against theft and phishing, but they
require a physical device each time you connect. Keep a separate backup key
if you use them regularly.

Next step
---------

We're almost done setting up your Launchpad account!
Before we explore more of Launchpad,
let's look at one of the ways it helps other people to see
your involvement in free software: :ref:`karma <your-account-karma>`!
