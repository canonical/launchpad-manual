#################
Sign web requests
#################

The `Launchpad web service hacking document <launchpad-web>`__ describes a
lot of requests you can send to launchpad.net. But if you send them in
the simple form presented in that document, you'll get a response code
of 401 ("Unauthorized"). Launchpad's web service only responds to
requests that have been digitally signed with a particular Launchpad
user's authorization key.

This doesn't have to be *your* key. You can have a simple script that
uses your own Launchpad authorization key, but you can also run a
website that gathers its users' authorization keys and makes requests to
the web service on their behalf. This is safe because these
authorization keys have nothing to do with your Launchpad password.
They're a way of delegating a limited set of privileges to some other
program. If a program proves untrustworthy, the user only needs to
revoke that program's key.

The standard HTTP authentication mechanisms (Basic and Digest) aren't
sophisticated enough to handle these cases. That's why Launchpad has
adopted the `OAuth standard <http://oauth.net>`__ for authentication.
It's more work to set up than just sending your Launchpad username and
password to the web service, but it's safer and more versatile.

If you're writing a console-based script based on
`launchpadlib <../launchpadlib>`__, you don't have to worry much about
this. Launchpadlib will automatically open a browser window for your
end-user and ask them to hit Return once they've granted your program
access. All you have to worry about is putting the resulting credentials
into persistent storage, so you can pull them out the next time your
program runs instead of making the end-user generate a new set of
credentials every time.

If you're not writing a console-based script, you'll need to implement a
workflow like the one described below to get a set of Launchpad
credentials for each of your users. The actual request signing is a
mechanical process and there are lots of libraries to help you with it.

Getting credentials
===================

The basic workflow is always the same when you're creating a set of
credentials, but the details are different if you're writing a
standalone application, versus creating a website. I'll show you where
the paths diverge.

Step 0: Pick a consumer key
---------------------------

The consumer key identifies your application and it should be hard-coded
somewhere in your code. Everyone who uses your application will send the
same consumer key.

We recommend you choose the name of your program as the consumer key.
Don't append the version number unless you want your users to get new
application keys for every new version. For this example I'll use the
consumer key 'just testing'.

Step 1: Get a request token
---------------------------

Getting your program's user to create a new credential for the program
is a multi-step process. The request token is a unique string that
Launchpad uses to keep track of your program between steps.

To obtain a request token, send a POST request to
https://launchpad.net/+request-token. (Note: *not* api.launchpad.net!)
This is the same kind of POST a web browser does when it submits a form.
You should submit the following values in form-URL-encoded format.

-  oauth_consumer_key: Your consumer key
-  oauth_signature_method: The string "PLAINTEXT"
-  oauth_signature: The string "&".

So the HTTP request might look like this:

::

       POST /+request-token HTTP/1.1
       Host: launchpad.net
       Content-type: application/x-www-form-urlencoded

       oauth_consumer_key=just+testing&oauth_signature_method=PLAINTEXT&oauth_signature=%26

The response should look something like this:

::

       200 OK

       oauth_token=9kDgVhXlcVn52HGgCWxq&oauth_token_secret=jMth55Zn3pbkPGNht450XHNcHVGTJm9Cqf5ww5HlfxfhEEPKFflMqCXHNVWnj2sWgdPjqDJNRDFlt92f

Save these two pieces of information, *oauth_token* and
*oauth_token_secret*: you'll need them to sign the request in step 3.

Step 2: Authenticate the user
-----------------------------

Now the user needs to 1) log in to Launchpad, and 2) tell Launchpad how
much authority they'd like to delegate to your program. You need to get
them to visit the following URL in their web browser:

::

       https://launchpad.net/+authorize-token?oauth_token={oauth_token}

Where *oauth_token* is the string by that name that you got at the end
of step 1. So, something like this:

::

       https://launchpad.net/+authorize-token?oauth_token=9kDgVhXlcVn52HGgCWxq

Step 2a: If you're building a website
-------------------------------------

If your program is a website that your users visit, you can send them an
HTTP redirect. Be sure to also specify the *oauth_callback* field as a
URL on your website.

::

       https://launchpad.net/+authorize-token?oauth_token={oauth_token}&oauth_callback={URL to within your website}

So, something like this:

::

       https://launchpad.net/+authorize-token?oauth_token=9kDgVhXlcVn52HGgCWxq&oauth_callback=http%3A%2F%2Fwww.mysite.com%2Foauth-callback

Once the user delegates some of their privileges to your website
Launchpad will redirect the user back to that URL, so that they can
resume using your site. In the example above, that would be
"http://www.mysite.com/oauth-callback".

Step 2b: If you're writing a stand-alone program
------------------------------------------------

If your program runs on the clients' computer rather than through their
web browser, you don't have to worry about redirecting back to your web
page. You can just open
https://launchpad.net/+authorize-token?oauth_token=%7Boauth_token%7D in
the end-user's web browser. But you do have to worry about opening the
Launchpad page in their web browser in the first place. Take a look at
the open_url_in_browser() function defined in launchpadlib's
launchpad.py; it works well on most Linux systems. Just open up their
web browser to the +authorize-token page.

If your program isn't running in the web browser, how are you supposed
to know when the user is done with the +authorize-token page? There's no
'oauth_callback' equivalent that Launchpad can use to send a signal to
your client-side program. What you need to do is have the *end-user
themselves* tell you when they're done with the +authorize-token page.

The launchpadlib library prints an explanatory message after it opens
+authorize-token in your web browser. It waits for the end-user to
authorize access through their web browser, and then switch back to the
launchpadlib window and hit return. If you're writing a GUI program, you
can have the end-user click a button once they're done authorizing your
program to talk to Launchpad on their behalf.

Step 3: Exchange the request token for an access token
------------------------------------------------------

The *oauth_token* and *oauth_token_secret* you got in Step 1 are real
OAuth keys that can be used to sign requests, but you're only going to
use them once. Their only purpose is to remind Launchpad who you are;
remember, it hasn't heard from you since step 1. Once the user has
delegated some of their authority to you, you need to exchange these
temporary credentials for permanent credentials that have the end-user's
permissions associated with them.

If you're writing a website, you'll know you're ready when Launchpad
redirects your user back to the URL you specified as *oauth_callback*.
If you're writing a client-side program, you'll know when your user
clicks the "Complete Authorization" button or hits enter or whatever it
was you told them to do when they were done on the Launchpad side.

Now you make a POST request to https://launchpad.net/+access-token
(again, *not* api.launchpad.net!). The body should be a set of
form-encoded parameters, as in Step 1. You need to provide the following
parameters:

-  

   -  oauth_token: The same as *oauth_token* from step 1
   -  oauth_consumer_key: The consumer key you chose in step 0
   -  oauth_signature_method: The string "PLAINTEXT"
   -  oauth_signature: The OAuth signature, calculated using `the
      PLAINTEXT algorithm <http://oauth.net/core/1.0/#anchor22>`__ and
      the *oauth_token_secret* from step 1

The last one is the tricky one. The OAuth standard has the details, but
basically you take the string '&' and stick the *oauth_token_secret* you
got at the end of step 1 onto the end. (The reason you start with the
string '&' is that Launchpad doesn't use OAuth Consumer Secrets--it's
pretty useless when most clients will be open-source--so there's nothing
to go before the ampersand.)

So your POST request should look like this:

::

       POST /+access-token
       Host: launchpad.net
       Content-type: application/x-www-form-urlencoded

       oauth_signature=%26jMth55Zn3pbkPGNht450XHNcHVGTJm9Cqf5ww5HlfxfhEEPKFflMqCXHNVWnj2sWgdPjqDJNRDFlt92f&oauth_consumer_key=just+testing&oauth_token=9kDgVhXlcVn52HGgCWxq&oauth_signature_method=PLAINTEXT

Basically, you're looking up a record using the request token as a key.
The record was created when the end-user told Launchpad it was okay to
delegate their authorization to you. The request token secret proves
that you're the same client as went through step 1.

You should get a response that looks something like this:

::

       200 OK

       oauth_token=PsK9cpbll1KwehhRDckr&oauth_token_secret=M2hsnmsfEIAjS3bTWg6t8X2GKhlm152PRDjLLmtQdr9C8KFZWPl9c8QbLfWddE0qpz5L56pMKKFKEfv1&lp.context=None

It looks just like the response you got in step 1. But these two pieces
of information, *oauth_token* and *oauth_token_secret*, are much more
powerful than the token and token secret you got in step 1. They'll
allow you to make requests to the Launchpad web service on behalf of
your end-user. They replace the *oauth_token* and *oauth_token_secret*
you got in step 1, and you'll need them as part of every request you
make to Launchpad's web service.

Using the credentials
=====================

Now that you've got an token and a token secret for a particular
Launchpad user, you won't have to go through the again for that user (so
long as you store the token and secret somewhere to use it later!). But
now you need to know how to digitally sign your web service requests
with that token.

The process of getting credentials is pretty specific to Launchpad, but
the process of digitally signing a request is completely standardized
and mechanical. The mechanics are covered in detail in `the OAuth
standard <http://oauth.net/core/1.0/>`__, and there are also OAuth
libraries in most popular programming languages that can sign an HTTP
request given an *oauth_token* and an *oauth_token_secret*. It's also
very similar to the request signing you did in step 3. So I'm not going
to go into much detail on how to actually sign a request. It's a general
problem and there are plenty of places to go if you need help, and lots
of sample code to look at.

I will say that right now, Launchpad only supports the first of OAuth's
`three ways of encoding the consumer request
parameters <http://oauth.net/core/1.0/#consumer_req_param>`__. You'll
need to put your digital signatures into the Authorization header, using
the `OAuth HTTP Authorization
Scheme <http://oauth.net/core/1.0/#auth_header>`__. That means making
HTTP requests that look like this:

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

If you put that *oauth_\** data into the entity-body of your POST
requests or the query strings of your GET requests (OAuth's other two
ways of encoding request parameters), Launchpad won't pick it up and you
won't be able to access the web service.

What does all that data in the Authorization header mean?

-  The *oauth_consumer_key* identifies your client software; it's the
   sa[Ime string you've been using since step 0.
-  The *oauth_token* is the one you got in step 3.
-  The *oauth_signature* is generated using the same PLAINTEXT algorithm
   as in step 3, but using the *oauth_token_secret* you got in step 3,
   rather than the now-abandoned *oauth_token_secret* you got in step 1.
-  The *oauth_nonce* and *oauth_timestamp* are as defined
   `here <http://oauth.net/core/1.0/#nonce>`__.

