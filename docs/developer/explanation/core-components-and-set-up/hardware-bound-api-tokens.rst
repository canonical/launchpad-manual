.. meta::
   :description: How Launchpad's hardware-bound API tokens work, including the
      cryptographic system, the challenge-response flow, and the threat model.

.. _hardware-bound-api-tokens-explanation:

Hardware-bound API tokens
=========================

**Hardware-bound API tokens** tie a user's Launchpad API access to a USB FIDO2
security key. This page explains the design, the cryptographic flow, and the
threat model.

Why hardware binding
--------------------

launchpadlib normally stores a long-lived OAuth access token on disk or in a
keyring. Because the keyring is unlocked at session login, an attacker who can
read files or run code can use that token until it is revoked. This matters
most for accounts with elevated privileges, and for developers who routinely
run unaudited code.

A hardware-bound login stores a long-lived OAuth *refresh grant* instead of an
access token. Launchpad binds the grant to a registered security key, and
launchpadlib must prove that it holds the key to exchange the grant for a
short-lived access token.

The three ceremonies
--------------------

The feature is built from three separate steps:

#. **Registration** associates the FIDO2 security key with a Launchpad account.
   This is a WebAuthn registration ceremony, exposed as
   ``beginWebAuthnRegistration`` and ``completeWebAuthnRegistration`` on the
   person, and available from both the Launchpad API and launchpadlib's
   ``register_hardware_key``.
#. **Grant issuance** mints a long-lived refresh grant bound to a registered
   key, through ``issueHardwareBoundOAuthToken``. The grant is by default
   limited to 365 days, and can be adjusted by the user.
#. **Minting** exchanges the grant for a short-lived access token, which
   requires a WebAuthn assertion from the bound key.

The challenge-response flow
---------------------------

Token minting is a WebAuthn assertion ceremony. The client proves possession of
the key by signing a Launchpad-issued challenge; Launchpad verifies the
signature against the public key registered for that authenticator.

Assuming the user has registered a key and issued a grant:

#. The user runs a script, which starts ``login_with_hardware_token``.
#. launchpadlib loads the stored refresh grant from the keyring, a file, or
   memory.
#. The client ``POST``\ s the grant to ``<web root>/+hw-challenge``. Launchpad
   returns a ``challenge_id`` and WebAuthn request options.
#. The security key performs a WebAuthn assertion over the challenge, after a
   user-presence or PIN check.
#. The client ``POST``\ s the grant, the ``challenge_id`` and the assertion to
   ``<web root>/+hw-access-token``. Launchpad verifies the assertion against the
   registered public key and returns a short-lived access token with an expiry.
#. The client uses the access token for subsequent API requests, signed with
   ordinary OAuth 1.

::

    Script        launchpadlib        USB FIDO2 key        Launchpad API
      |  login_with_hardware_token() |                        |
      |----------->|                 |                        |
      |            | load grant      |                        |
      |            | (keyring/file)  |                        |
      |            |------ POST /+hw-challenge -------------->|
      |            |<----- challenge_id + WebAuthn options ---|
      |            | WebAuthn assertion (presence / PIN)      |
      |            |---------------->|                        |
      |            |<-- signed assertion                      |
      |            |------ POST /+hw-access-token ----------->|
      |            |            verify assertion vs public key|
      |            |<----- short-lived access token ----------|
      |            |------ API requests (OAuth 1) ----------->|

All requests use TLS. The WebAuthn challenge is random and single-use, which
protects against replay. The design assumes the operating system provides
process-level memory separation, which is the default on Ubuntu.

Token model and revocation
--------------------------

Two tokens with different lifetimes are involved:

- The **refresh grant** is long-lived, defaults to and is capped at 365 days,
  and is bound to a registered key. It cannot mint a token without the key.
- The **access token** is short-lived. Its expiry is set by the server, and
  launchpadlib reuses it until shortly before it expires.

Revocation works at both levels. Revoking a grant also expires access tokens
already minted from it. Revoking a key prevents all of its grants from minting
new tokens, though already-minted access tokens remain valid until they expire.

Threat model
------------

The goal is to protect against opportunistic, unprivileged attacks, such as a
large-scale supply-chain scanner that harvests unprotected secrets from files
and keyrings. Against those, a stolen grant is useless without the key.

A targeted user-level attacker who can run code as the user could still
exfiltrate a minted access token, or modify the client code before it signs a
request. Mitigating this fully is future work (for example, an authentication
daemon and sandboxed packaging) and is out of scope here. Targeted,
privileged, system-level attacks are explicitly out of scope.

See also
--------

- :ref:`Use hardware-bound API tokens <use-hardware-bound-api-tokens>` for the
  user-facing how-to.
- The `launchpadlib reference for hardware-bound API tokens
  <https://documentation.ubuntu.com/launchpadlib/hardware-tokens.html>`_, which
  documents the client API, storage format and the exchange protocol in detail.
