Get started with launchpadlib
=============================

This document shows how to use a Python client to read and write Launchpad's
data using the launchpadlib library. It doesn't cover the HTTP requests and
responses that go back and forth behind the scenes: for that, see `the
"hacking" document <../Hacking>`__. This document also doesn't cover the full
range of what's possible with Launchpad's web service: for that, see the `web
service reference documentation <http://launchpad.net/+apidoc/>`__. Check out
the `API examples page <API/Examples>`__ if you would like to see more sample
code.

Installation
------------

Install on Ubuntu
^^^^^^^^^^^^^^^^^

If you have the latest version of Ubuntu then to install the launchpadlib
available in the Ubuntu repositories, open a terminal and run the command:

::

     sudo apt-get install python3-launchpadlib

And you are done!

If you have an older version of Ubuntu then parts of the instructions below may
not work with the version from the repositories but you should be able to
install the latest version of launchpadlib manually.

Install using pip
^^^^^^^^^^^^^^^^^

On any platform with a working Python and pip, you should be able to
say:

::

     pip install launchpadlib

Getting started
---------------

The first step towards using Launchpad's web service is to choose a cache
directory. The documents you retrieve from Launchpad will be stored here, which
will save you a lot of time. Run this code in a Python session, substituting an
appropriate directory on your computer:

::

       cachedir = "/home/me/.launchpadlib/cache/"

The next step is to set up credentials for your client. For quick read-only
access to Launchpad data, you can get anonymous access.  Otherwise, you'll need
to authenticate with Launchpad using OAuth.

Anonymous access
^^^^^^^^^^^^^^^^

The \`Launchpad.login_anonymously()\` method will give you automatic read-only
access to public Launchpad data.

::

       from launchpadlib.launchpad import Launchpad
       launchpad = Launchpad.login_anonymously('just testing', 'production', cachedir, version='devel')

The first argument to \`Launchpad.login_anonymously()\` is a string that
identifies the web service client. We use this string to gauge client
popularity and detect buggy or inefficient clients. Here, though, we're just
testing.

The second argument tells launchpadlib which Launchpad instance to run against.
Here, we're using \`production`, which is mapped to the web service root on the
production Launchpad server: "https://api.launchpad.net/". Anonymous access
cannot change the Launchpad dataset, so there's no concern about a bad test
program accidentally overwriting data. (If you want to play it safe, you could
use 'staging' instead - though staging is sometimes down for extended periods.)

The \`version\` argument specifies the API version to use. For historical
reasons the default is \`'1.0'\`, and you may want to use this in certain
special circumstances, but in most cases you should use \`'devel'\` so that you
get a reasonably complete and current interface.

The \`login_anonymously()\` method automatically negotiates a read-only
credential with Launchpad. You can use your \`Launchpad\` object right away.

::

       bug_one = launchpad.bugs[1]
       print(bug_one.title)
       # Microsoft has a majority market share

You'll get an error if you try to modify the dataset, access private
data, or access objects like \`launchpad.me\` which assume a particular
user is logged in.

Note that \`login_anonymously()\` is only available in launchpadlib
starting in version 1.5.4.

Authenticated access
^^^^^^^^^^^^^^^^^^^^

To get read-write access to Launchpad, or to see a user's private data, you'll
need to get an OAuth credential for that user. If you're writing an application
that the user will run on their own computer, this is easy: just call the
\`Launchpad.login_with()\` method.

This method takes two important arguments: the name of your application, and
the name of the Launchpad server you want to run against. The default server
name is 'staging', so that you don't destroy data by accident while developing.
When you do a release, you can change this to 'production'.

::

       from launchpadlib.launchpad import Launchpad
       launchpad = Launchpad.login_with('My Application', 'staging', version='devel')

*If this code complains that 'staging' isn't a URL, then you're not running the
most up-to-date launchpadlib. You can replace 'staging' with
\`launchpadlib.launchpad.STAGING_SERVICE_ROOT\` to make it work in Ubuntu
9.10's launchpadlib.*

If you have an existing desktop-wide Launchpad credential, launchpadlib will
find it and use it. If there's no existing desktop credential (because you've
never used a launchpadlib application on this computer, or because you had a
credential that expired), launchpadlib will guide you through authorizing a new
credential, as seen `here <API/ThirdPartyIntegration>`__.

There's one other important argument to \`login_with()`. You can pass in a
callback function as \`credential_save_failed`. That function will be invoked
if a desktop credential can't be created--either because the end-user refused
to perform the authorization, or because there was a problem storing the
credential after authorization.

::

       import sys
       from launchpadlib.launchpad import Launchpad

       def no_credential():
           print("Can't proceed without Launchpad credential.")
       sys.exit()

       launchpad = Launchpad.login_with(
           'My Application', 'staging', credential_save_failed=no_credential, version='devel')

Authenticated access for website integration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Things are a little more difficult if you want to integrate Launchpad's
functionality into your own website. You can't call \`Launchpad.login_with()`,
because that will open up a web browser on your webserver--not on your user's
computer.

Instead, you create a \`Credentials\` object identifying your website and call
\`get_request_token()\` to ask Launchpad for a request token.  Be sure to pass
in the name of the Launchpad server you want to use (probably "production" as
\`web_root`.

::

       from launchpadlib.credentials import Credentials
       credentials = Credentials("my website")
       request_token_info = credentials.get_request_token(web_root="production")

You'll get back a string that looks like
'https://launchpad.net/+authorize-token?oauth_token=...' This is the URL your
end-user needs to visit in order to authorize your token.

At this point, you should redirect your user to that URL. Then, start
periodically calling \`exchange_request_token_for_access_token()`:

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

Once \`exchange_request_token_for_access_token()\` successfully executes, an
authorized access token will be present in \`credentials.access_token`. You can
then pass the \`Credentials\` object into the \`Launchpad\` constructor.

::

       from launchpadlib.launchpad import Launchpad
       launchpad = Launchpad(credentials, service_root="production")

While this system is not ideal, we don't know of any third-party websites that
are integrating Launchpad functionality in a way that requires OAuth tokens.

Getting help
^^^^^^^^^^^^

If you don't know the capabilities of one of the objects you've got, you can
call dir() on it. You'll see all of its fields and all the custom methods it
supports. Unfortunately, you'll also see a bunch of launchpadlib-specific junk
that you don't care about. That's why we've made available these four lists:

-  \`lp_attributes`: Data fields of this object. You can read from these
   might be able to write to some of them.
-  \`lp_collections`: List of launchpad objects associated with this
   object.
-  \`lp_entries`: Other Launchpad objects associated with this one.
-  \`lp_operations`: The names of Launchpad methods you can call on the
   object.

.. raw:: html

   <!-- end list -->

::

      print(sorted(bug_one.lp_attributes))
      # ['date_created', 'date_last_message', 'date_last_updated', ... 'tags', 'title']
      print(sorted(bug_one.lp_operations))
      # ['addAttachment', 'addWatch', 'subscribe', 'unsubscribe']

If you need more detailed help, you can look the object up in `the reference
documentation <http://launchpad.net/+apidoc>`__. First, find out the type of
the object.

::

       print(repr(bug_one))
       # <bug at https://api.staging.launchpad.net/beta/bugs/1>

This is a 'bug' type object. Now you use the type of the object as an anchor
into the reference documentation. To find out the capabilities of this object
and what data is stored inside it, you'd visit
https://api.launchpad.net/devel.html#bug.

As you'll see, the reference documentation still needs some work, and it's
geared more towards web service hackers than launchpadlib users, but it will
tell you about all of this object's attributes and all the supported
operations.

-  The "Default representation" section tells you about the available
   attributes.

.. raw:: html

   <!-- end list -->

-  The "Custom POST methods" and "Custom GET methods" sections tell you
   about methods the object supports other than the default methods
   described below. The methods take whatever parameters are listed in
   "Request query parameters". (You can ignore the "ws.op" parameter
   because you're using launchpadlib; that's just the name of the
   method.)