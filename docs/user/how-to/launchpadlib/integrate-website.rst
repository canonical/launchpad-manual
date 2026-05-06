Authenticated access for website integration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you want to integrate Launchpad's functionality into your own website, you 
can't call ``Launchpad.login_with()``, because that will open up a web browser
on your webserver, not on your user's computer. Instead, you create a
``Credentials`` object identifying your website and call
``get_request_token()`` to ask Launchpad for a request token. 

Be sure to pass in the name of the Launchpad server you want to use
(probably "production") as ``web_root``.

::

       from launchpadlib.credentials import Credentials
       credentials = Credentials("my website")
       request_token_info = credentials.get_request_token(web_root="production")

You'll get back a string that looks like
``https://launchpad.net/+authorize-token?oauth_token=...``
This is the URL your end-user needs to visit in order to authorize your token.

At this point, you should redirect your user to that URL, then start
periodically calling ``exchange_request_token_for_access_token()``:

::

       from lazr.restfulclient.errors import HTTPError
       complete = False
       while not complete:
           try:
               credentials.exchange_request_token_for_access_token(
               web_root="production")
           complete = True
           except HTTPError:
           # The user hasn't authorized the token yet.

Once ``exchange_request_token_for_access_token()`` successfully executes, an
authorized access token will be present in ``credentials.access_token``. You
can then pass the ``Credentials`` object into the ``Launchpad`` constructor.

::

       from launchpadlib.launchpad import Launchpad
       launchpad = Launchpad(credentials, service_root="production")

While this system is not ideal, we don't know of any third-party websites that
are integrating Launchpad functionality in a way that requires OAuth tokens.