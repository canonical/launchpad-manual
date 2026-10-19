.. meta::
   :description: Protect your Launchpad API credentials with a USB FIDO2
      security key by using hardware-bound API tokens with launchpadlib.

.. _use-hardware-bound-api-tokens:

Use hardware-bound API tokens
=============================

**Hardware-bound API tokens** let you tie your Launchpad API access to a USB
FIDO2 security key, such as a YubiKey. Instead of storing a usable secret on
disk or in your keyring, launchpadlib stores a long-lived OAuth *refresh grant*
that is useless on its own: exchanging it for a short-lived access token
requires a WebAuthn assertion from your registered security key. This protects
your stored credentials against opportunistic theft, for example by
supply-chain scanners or malware that reads files and keyrings.

.. note::

   This feature secures **programmatic access through launchpadlib** (scripts
   and tools such as ``lp-shell`` and ``ubuntu-archive-tools``). It is not a way
   to log in to the Launchpad website in a browser, and it does not apply to
   automation or bot accounts, which should use ordinary tokens.

Hardware binding protects the stored grant, not each access token. A minted
access token is an ordinary OAuth token for its short lifetime, but the stored
grant cannot mint a new one without the security key.

Prerequisites
-------------

- A USB (HID) FIDO2 security key. NFC authenticators and platform passkeys are
  not supported.
- launchpadlib with the optional ``fido2`` extra::

      pip install 'launchpadlib[fido2]'

  On Debian and Ubuntu you can instead install::

      apt install python3-fido2

  The supported versions are ``fido2>=1.1.2,<3``.
- A keyring is recommended for storing the grant, but you can use a file
  instead (see `Where grants are stored`_).

Talking to a USB key needs access to its ``hidraw`` device. If a connected key
is not found or cannot be opened, check the device permissions and the FIDO2
udev rules from your distribution or key vendor. Running as root is not
required.

Register your security key
--------------------------

You can register a security key from the Launchpad website, or from
launchpadlib with an authenticated client.
To register from launchpadlib, touch the key when prompted:

.. code-block:: python

    from launchpadlib.launchpad import Launchpad

    launchpad = Launchpad.login_with(
        "hardware-key-registration", "production", version="devel"
    )
    authenticator = launchpad.register_hardware_key("My security key")

The returned ``authenticator`` is an API entry. Its ``id`` identifies the key
when you issue a grant.

Issue a hardware-bound grant
----------------------------

Issuing a grant is separate from logging in with it. Use an authenticated
client:

.. code-block:: python

    grant = launchpad.issue_hardware_bound_oauth_token(
        consumer_key="hardware-client",
        authenticator_id=authenticator.id,
        permission="Change Anything",
    )

The result is a dictionary with ``oauth_token`` and ``oauth_token_secret``.
Launchpad returns the secret only once, so pass the dictionary straight to
``login_with_hardware_token`` or keep it secret. A grant cannot be broader than
the permission of the credentials used to issue it, and it defaults to, and is
limited to, 365 days.

Log in with the grant
---------------------

Pass the issued grant to ``Launchpad.login_with_hardware_token``. The consumer
must match the ``consumer_key`` used to issue the grant:

.. code-block:: python

    from launchpadlib.launchpad import Launchpad

    launchpad = Launchpad.login_with_hardware_token(
        "my-application",
        "production",
        account="example-user",
        consumer_name="hardware-client",
        grant=grant,
    )
    print(launchpad.me.name)

The login mints an access token straight away, so expect to touch the key once
during login. The grant is stored once it has authenticated a request as
``account``, so later logins can omit ``grant`` and load it from the credential
store:

.. code-block:: python

    launchpad = Launchpad.login_with_hardware_token(
        "my-application",
        "production",
        account="example-user",
        consumer_name="hardware-client",
    )

If no grant is stored, ``HardwareTokenError`` is raised; there is no fallback to
browser authorization.

Remove the classic bootstrap token
----------------------------------

Registering a key and issuing a grant both need an authenticated client created
with the classic ``Launchpad.login_with``. That bootstrap step stores an
ordinary, long-lived OAuth access token in your keyring (or credentials file) --
exactly the kind of credential that hardware binding is meant to protect you
from. It keeps working even after you switch to ``login_with_hardware_token``,
so once you have confirmed that hardware-bound login works, remove it:

#. Revoke it server-side. Visit your `list of authorized applications
   <https://launchpad.net/people/+me/+oauth-tokens>`_, find the authorization
   for the consumer you bootstrapped with (for example
   ``hardware-key-registration``), and click **Revoke authorization**. This
   stops the token from being used even if a copy of it remains on disk.
#. Remove the stored copy so launchpadlib does not keep a now-useless secret
   around. If launchpadlib used the keyring, delete its entry for that consumer;
   if you passed ``credentials_file``, delete that file.

.. note::

   Use a consumer name for the bootstrap login that is different from your
   hardware-bound ``consumer_name`` (as in the examples above,
   ``hardware-key-registration`` versus ``hardware-client``). The classic token
   and the hardware-bound grant are then stored separately, so revoking the
   classic token does not affect the grant.

Where grants are stored
-----------------------

Grants are stored in the system keyring by default, and only in memory under
``sudo``. To store the grant in a file instead, pass ``credentials_file`` or set
the ``LP_HARDWARE_CREDENTIALS_FILE`` environment variable. The file is written
atomically and holds the grant's secret.

The stored record never contains access tokens, challenges, assertions or PINs,
and the private key never leaves the security key.

Day-to-day use
--------------

An access token is reused until it is close to expiry, so ordinary requests do
not each need a key touch. launchpadlib renews the token while signing a
request, shortly before it expires, which is when you are prompted to touch the
key again. This lets a long-running process make multiple requests between key
touches. Access tokens are not persisted beyond the process lifetime, so each
new invocation needs a key touch to obtain its access token.

Revoke a grant or key
---------------------

To revoke a grant:

.. code-block:: python

    authenticator.revoke()

This also expires access tokens already minted from the grant. Revoking on the
server does not remove a stored copy of the grant; logins using it are
rejected.

To revoke the key itself:

.. code-block:: python

    authenticator.revoke()

Revoking a key prevents its grants from minting new access tokens, but does not
revoke tokens already minted from those grants; they stay valid until they
expire. To expire them immediately, revoke the grant.

Troubleshooting
---------------

- **No security key found or cannot be opened.** Check the USB connection, the
  ``hidraw`` device permissions, and your distribution's or vendor's FIDO2 udev
  rules.
- **No keyring available.** Pass ``credentials_file`` or set
  ``LP_HARDWARE_CREDENTIALS_FILE`` to store the grant in a file.
- **python-fido2 is not installed.** Install the ``fido2`` extra, as shown in
  `Prerequisites`_.

See also
--------

- The `launchpadlib reference for hardware-bound API tokens
  <https://documentation.ubuntu.com/launchpadlib/hardware-tokens.html>`_, which
  documents the full API, storage format, token renewal and the exchange
  protocol.
- :ref:`Using launchpadlib <using-launchpadlib>` for ordinary authentication.
