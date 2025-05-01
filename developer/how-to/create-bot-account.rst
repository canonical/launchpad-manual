=================================
Creating bot account in Launchpad
=================================

.. note::

   This process does **not** involve the Launchpad team - although the
   Launchpad team is happy to assist in the process.
   
   The IS team is the one that handles this setup.

1. Request an email alias (and mappings to a real email address).
   This requires filing an RT ticket
   (e.g: `RT#c162471 <https://portal.admin.canonical.com/C162471/>`_)
   with details about:

   - The alias email address.

   - Which emails addresses the alias maps to.

2. Create an SSO account using the email alias (every real email mapped will
   get the Ubuntu One emails with the link to validate the email).

   **Note:** in case multiple users have access to this email alias,
   anyone with access to the email alias will be able to reset the
   password of this account.

3. While still logged in with the new SSO account, go to https://launchpad.net
   and click login.

   If you are already logged in to your SSO account, you should be logged in
   to the new bot account automatically.
