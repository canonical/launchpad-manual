Import your SSH keys
====================

To push code branches to Launchpad you first need to generate your SSH key. The key is made up of two parts: a private key that stays on your computer and a public key that you register with Launchpad. As you might expect, you shouldn't share the private key with anyone.

Why you need an SSH key
-----------------------

The trust that other people put in your Launchpad identity is no more important than when they use code that you've uploaded to Launchpad.

An SSH key secures the connection between your computer and Launchpad while you're pushing Bazaar branches up to Launchpad.

Creating the key
----------------

How you create your SSH key pair depends on which operating system you use.

If the instructions for your operating system are not here, `get in touch to request them <https://help.launchpad.net/Feedback>`_ or, if you know what to do, add them to this page.

At present, Launchpad only supports RSA, DSA, and ECDSA keys.

Linux/Cygwin/MacOS
^^^^^^^^^^^^^^^^^^

**Step 1:** Install OpenSSH. On Ubuntu, you can install OpenSSH by opening your terminal and typing:

sudo apt-get install openssh-client

With Cygwin you can follow the instructions here: `http://pigtail.net/LRP/printsrv/cygwin-ssh.html <http://pigtail.net/LRP/printsrv/cygwin-ssh.html>`_

**Step 2:** Once OpenSSH is installed, stay in the terminal and type:

ssh-keygen -t rsa

**Step 3:** When prompted, press Enter to accept the default file name for your key.

**Step 4:** Next, enter then confirm a password to protect your SSH key. Your key pair is stored in ~/.ssh/ as id_rsa.pub (public key) and id_rsa (private key)

Now you need to upload the public portion of your SSH key to Launchpad.

**Possible Step 5:** You may need to run ssh-add with the id file if you created an id file other than ~/.ssh/id_rsa. Do ssh-add /path/to/file/id_rsa_newfile . If you’re on the Mac, you can execute the following on the command line:


* cat ~/.ssh/id_rsa.pub | pbcopy

Windows (PuTTY)
^^^^^^^^^^^^^^^

**Step 1:** Download the PuTTY Key Generator from here: `http://www.chiark.greenend.org.uk/\~sgtatham/putty/download.html <http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html>`_

**Step 2:** Run puttygen.exe and click the generate button. PuTTYGen will ask you to move your mouse around in the blank area to generate entropy.

**Step 3:** Set a key passphrase and confirm it.

**Step 4:** Click "Save public key" and choose a location to save it. Click "Save private key" and choose a secure location to save it. **You must keep this secret key safe!**

**Step 5:** Do **\ *not*\ ** close Puttygen window just yet! Copy the public key from the Puttygen window.

This way you get key for the next step ("Registering the key with Launchpad").

.. note::
    Step 5 helps avoid the "Invalid public key" error. (Taken from launchpad `question 26705 <https://answers.launchpad.net/launchpad/+question/26705>`_\ )

**Step 6:** Run/Install `Pageant <http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html>`_ as either a standalone .exe or as part of the entire putty package. Make sure Pageant is running and rt+click the icon in the notification area. Add the private key you saved earlier. This step is crucial if you want to connect to launchpad from a Windows PC.

Cygwin/Windows (PuTTY)
^^^^^^^^^^^^^^^^^^^^^^

Follow these steps if you wish to use Pageant under Cygwin.

**Step 1:** Follow the procedure in the 'Windows (PuTTY)' section

**Step 2:** Add 'BZR_SSH' as an environment variable with full path to the plink.exe or just 'plink' if it's in PATH anyway.

**Step 3:** Close all existing bash terminals and open a new terminal.

**Step 4:** Run 'plink INSERT_YOUR_USERNAME_HERE@bazaar.launchpad.net' and accept 'yes' to store the server's host key

Registering the key with Launchpad
----------------------------------

**Step 1:** If you are using windows/putty/puttygen, go to step 2.

Open your public key in a text editor and copy its contents to your clipboard. The public key file has the extension .pub. For example: id_rsa.pub

**Step 2:** Visit `your SSH keys page <https://launchpad.net/~/+editsshkeys>`_.

**Step 3:** Paste your public key into the text box and then click the Import public key button to continue.

Using a custom SSH key for Launchpad
------------------------------------

You can safely use one SSH key per client machine to connect to multiple hosts. Some people choose to use a separate SSH keypair per service and per client, to have more flexibility about copying keys around or revoking them.

To do this:


#. You need to generate a key to a non-default name, perhaps id_rsa_launchpad (and .pub)  
#. Upload that key to Launchpad, as described above.  
#. You'll need to tell your SSH client to use this key. With OpenSSH, add these lines to your ~/.ssh/config file:

.. code-block::

    Host bazaar.launchpad.net
     IdentityFile  /home/me/.ssh/id_rsa_launchpad
     User launchpad-username    # the short name that appears in the URL when you visit https://launchpad.net/~

.. note::
    You need to upload the .pub file to Launchpad, and to specify the private-key file (with no .pub) in the SSH configuration.

Next step
---------

We're almost done setting up your Launchpad account! Before we explore more of Launchpad, let's look at one of the ways it helps other people to see your involvement in free software: `karma <https://help.launchpad.net/YourAccount/Karma>`_\ !
