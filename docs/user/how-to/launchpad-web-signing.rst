.. meta::
   :description: How to sign web requests to the Launchpad API using OAuth for
      secure, authenticated API access.

.. _sign-web-requests:

Sign web requests
=================

.. include:: /includes/important_not_revised_help.rst

Launchpad's web service only responds to requests that have been digitally
signed with a Launchpad user's authorization key. Unsigned requests receive a
``401 Unauthorized`` response.

This key has nothing to do with your Launchpad password. It's a way of
delegating a limited set of privileges to a program, using the
`OAuth standard <http://oauth.net>`__. If a program proves untrustworthy, the
user only needs to revoke that program's key.

If you're writing a console-based script with :ref:`launchpadlib`, you don't
need to handle any of this manually: launchpadlib opens a browser for the user
to grant access, then stores the resulting credentials for you. The workflow
below is only needed if you implement the OAuth exchange yourself, for example
in a website or GUI application.

Get credentials
---------------

The workflow to create a set of credentials is always the same, with minor
differences between standalone applications and websites.

Pick a consumer key
~~~~~~~~~~~~~~~~~~~

The consumer key identifies your application and should be hard-coded in your
code. Every user of your application sends the same consumer key. We recommend
using the name of your program without a version number (otherwise users get
new application keys for every release). This example uses ``just testing``.

Get a request token
~~~~~~~~~~~~~~~~~~~

The request token lets Launchpad track your program between steps. To obtain
one, send a form-URL-encoded POST request to
``<https://launchpad.net/+request-token>``_ (*not* ``api.launchpad.net``) with:

- ``oauth_consumer_key``: your consumer key
- ``oauth_signature_method``: the string ``PLAINTEXT``
- ``oauth_signature``: the string ``&``

::

   POST /+request-token HTTP/1.1
   Host: launchpad.net
   Content-type: application/x-www-form-urlencoded

   oauth_consumer_key=just+testing&oauth_signature_method=PLAINTEXT&oauth_signature=%26

The response contains an ``oauth_token`` and ``oauth_token_secret``:

::

   200 OK

   oauth_token=9kDgVhXlcVn52HGgCWxq&oauth_token_secret=jMth55Zn3pbkPGNht450XHNcHVGTJm9Cqf5ww5HlfxfhEEPKFflMqCXHNVWnj2sWgdPjqDJNRDFlt92f

Save both values; you'll need them when exchanging the request token.

Authenticate the user
~~~~~~~~~~~~~~~~~~~~~

The user now needs to log in to Launchpad and choose how much authority to
delegate to your program. Send them to the following URL, where ``{oauth_token}``
is the token from the previous step:

::

   https://launchpad.net/+authorize-token?oauth_token={oauth_token}

**If you're building a website**, add an ``oauth_callback`` field pointing to a
URL on your site. Launchpad redirects the user there once they've delegated
their privileges:

::

   https://launchpad.net/+authorize-token?oauth_token={oauth_token}&oauth_callback={URL within your website}

**If you're writing a standalone program**, there's no callback. Open the
``+authorize-token`` page in the user's browser (launchpadlib's
``open_url_in_browser()`` works well on most Linux systems), then have the user
tell you when they're done, for example by clicking a button or pressing Enter.

Exchange the request token for an access token
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once the user has delegated their authority (a website knows this when
Launchpad hits its ``oauth_callback``; a standalone program when the user
signals they're done), exchange the temporary token for permanent credentials.

Send a form-encoded POST request to ``<https://launchpad.net/+access-token>``_
(again, *not* ``api.launchpad.net``) with:

- ``oauth_token``: the ``oauth_token`` from the previous response
- ``oauth_consumer_key``: the consumer key you chose
- ``oauth_signature_method``: the string ``PLAINTEXT``
- ``oauth_signature``: the string ``&`` followed by the ``oauth_token_secret``
  from the previous step, calculated with the
  `PLAINTEXT algorithm <http://oauth.net/core/1.0/#anchor22>`_

::

   POST /+access-token
   Host: launchpad.net
   Content-type: application/x-www-form-urlencoded

   oauth_signature=%26jMth55Zn3pbkPGNht450XHNcHVGTJm9Cqf5ww5HlfxfhEEPKFflMqCXHNVWnj2sWgdPjqDJNRDFlt92f&oauth_consumer_key=just+testing&oauth_token=9kDgVhXlcVn52HGgCWxq&oauth_signature_method=PLAINTEXT

The response returns a new, more powerful ``oauth_token`` and
``oauth_token_secret``:

::

   200 OK

   oauth_token=PsK9cpbll1KwehhRDckr&oauth_token_secret=M2hsnmsfEIAjS3bTWg6t8X2GKhlm152PRDjLLmtQdr9C8KFZWPl9c8QbLfWddE0qpz5L56pMKKFKEfv1&lp.context=None

These replace the token and secret from the first step and are required for every
request you make on the user's behalf. Store them so the user doesn't have to
repeat this process.

Sign requests with the credentials
----------------------------------

Signing a request is standardized and mechanical, and OAuth libraries exist for
most languages, so this section only covers the Launchpad-specific details. See
the `OAuth standard <http://oauth.net/core/1.0/>`__ for the full algorithm.

Launchpad only supports OAuth's
`Authorization header method <http://oauth.net/core/1.0/#auth_header>`_ for
`encoding request parameters <http://oauth.net/core/1.0/#consumer_req_param>`_.
Parameters placed in the entity-body or query string are ignored. A signed
request looks like this:

::

   GET /beta/bugs/11
   Host: api.launchpad.net
   Accept: application/json
   Authorization: OAuth realm="https://api.launchpad.net/",
               oauth_consumer_key="just+testing",
               oauth_token="PsK9cpbll1KwehhRDckr",
               oauth_signature_method="PLAINTEXT",
               oauth_signature="%26M2hsnmsfEIAjS3bTWg6t8X2GKhlm152PRDjLLmtQdr9C8KFZWPl9c8QbLfWddE0qpz5L56pMKKFKEfv1",
               oauth_timestamp="1217548916",
               oauth_nonce="51769993",
               oauth_version="1.0"

Where:

- ``oauth_consumer_key`` identifies your application.
- ``oauth_token`` is the access token you got from the response.
- ``oauth_signature`` uses the PLAINTEXT algorithm with the
  ``oauth_token_secret`` you got along the access token.
- ``oauth_nonce`` and ``oauth_timestamp`` are as defined in the
  `OAuth docs <http://oauth.net/core/1.0/#nonce>`_.
