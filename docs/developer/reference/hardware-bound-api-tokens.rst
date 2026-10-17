.. meta::
   :description: Reference for Launchpad's hardware-bound API tokens, including
      the exchange endpoints, token model, grant storage, and error types.

.. _hardware-bound-api-tokens-reference:

Hardware-bound API tokens
=========================

This page is a reference for the server-side and protocol details of
:ref:`hardware-bound API tokens <hardware-bound-api-tokens-explanation>`. For
the client-side API, grant storage format and the full exchange protocol, see
the `launchpadlib reference for hardware-bound API tokens
<https://documentation.ubuntu.com/launchpadlib/hardware-tokens.html>`_.

Person API methods
-------------------

The following methods are exposed on a person in the ``devel`` web service
version:

``beginWebAuthnRegistration``
    Start a WebAuthn registration ceremony and return the creation options.
``completeWebAuthnRegistration``
    Finish registration and return the new authenticator entry.
``revokeWebAuthnRegistration``
    Revoke a registered authenticator by its ``id``.
``issueHardwareBoundOAuthToken``
    Issue a refresh grant bound to a registered authenticator. Returns the
    ``oauth_token`` and ``oauth_token_secret``; the secret is returned only
    once.
``revokeHardwareBoundOAuthToken``
    Revoke a grant by its token key. Access tokens already minted from the
    grant expire as well.

Exchange endpoints
------------------

Two public browser endpoints on the web root of the service root exchange a
refresh grant for a short-lived access token. The exchange is authenticated by
the grant itself, not signed with OAuth.

``POST <web root>/+hw-challenge``
    Accepts ``oauth_token`` and ``oauth_token_secret``, form encoded. Returns
    JSON with a positive integer ``challenge_id`` and WebAuthn request options
    under ``publicKey``.
``POST <web root>/+hw-access-token``
    Accepts ``oauth_token``, ``oauth_token_secret``, ``challenge_id`` and the
    JSON-encoded WebAuthn ``assertion``, form encoded. Returns a form-encoded
    ``oauth_token``, ``oauth_token_secret``, an ISO 8601 ``expires_at`` and an
    optional ``lp.context``.

The challenge is 32 bytes, and its relying party ID must match the WebAuthn
origin. Redirects are not followed and assertions are never retried. HTTP 401,
403 and 410 indicate a rejected grant.

Token model
-----------

- **Refresh grant**: long-lived, defaults to and is capped at 365 days, bound
  to a registered authenticator. Cannot mint a token without the key.
- **Access token**: short-lived, with a server-set ``expires_at``. Reused by
  the client until shortly before it expires.

Grant storage (client side)
----------------------------

launchpadlib stores only the grant, never access tokens, challenges, assertions
or PINs. The private key never leaves the security key.

- Default store: the system keyring, service ``launchpadlib.hardware-token.v2``.
- Under ``sudo``: memory only.
- Optional file store: ``credentials_file`` or the
  ``LP_HARDWARE_CREDENTIALS_FILE`` environment variable, written atomically.

A stored record holds the refresh token and its secret, the account, the
optional credential ID, the service root, the WebAuthn origin and the consumer
key. Records are keyed by ``v2:`` followed by the SHA-256 digest of a JSON list
of the service root and consumer key.

Error types
-----------

``HardwareKeyError``
    A security-key operation failed.
``HardwareKeyCancelledError``
    The user or the key cancelled the operation.
``HardwareKeyTimeoutError``
    The security-key operation timed out.
``Fido2SupportError``
    python-fido2 is not installed.
``HardwareTokenError``
    A grant or access token could not be issued, stored or minted. Subclass of
    ``HardwareKeyError``.
``HardwareTokenGrantError``
    Launchpad rejected a grant during the exchange.

See also
--------

- :ref:`Hardware-bound API tokens <hardware-bound-api-tokens-explanation>` for
  the design and cryptographic flow.
- :ref:`Use hardware-bound API tokens <use-hardware-bound-api-tokens>` for the
  user-facing how-to.
