.. _launchpad-web-service:

Launchpad web service
=====================

.. include:: /includes/important_not_revised_help.rst

Canonical provides a Python client, :ref:`launchpadlib`,
for reading and writing to Launchpad's web service. But there are many
situations where you wouldn't use ``launchpadlib``: if you're not a Python
programmer; if you want to write an Ajax client that runs in a web
browser; if launchpadlib is too heavyweight for what you want to do; or,
if you just want to understand what's going on between the client and
the server.

This document describes the HTTP resources published through Launchpad's
web service. It shows you how to read and write information about those
resources by making HTTP requests. It assumes you have basic knowledge
of how a web browser and web server interact.

Launchpad Resources
-------------------

Every object in Launchpad- everything you might think of as having a
separate identity- has its own URL in the Launchpad web service. You can
bookmark this URL and pass it around. You can also manipulate the
underlying Launchpad object by making HTTP requests to its URL.
Everything means everything: big things like people, teams, bugs, bug
tasks, and projects, all the way down to team memberships, bug watches,
and the languages people speak.

(This is the plan, anyway. We're still working to expose all of
Launchpad's objects through the web service, and many objects that are
exposed don't yet publish much useful information.)

In the following sections I'll show you HTTP requests you can make and
the responses you'll get back.

I'll be skipping over the fact that to make authenticated requests,
you'll need to digitally sign those requests using a set of OAuth
credentials.

Unauthenticated requests can see all public objects, which are the
majority, but they can't see private objects (such as hidden email
addresses, security-sensitive bugs, or private teams), they can't change
anything, and of course they have no concept of a "me" resource to start
from. Trying to access a private resource will give you a "401
Unauthenticated" error.

To see how to sign a request, see :ref:`Signing Requests <sign-web-requests>`.

The homepage
~~~~~~~~~~~~

Launchpad's website has a homepage that acts as a jumping-off point to
projects, bugs, people, answers, and so on. The web service has a
homepage, too. It's a lot more sparse than the web site's homepage but
it also makes a good jumping-off point.

The root of the web service is `<http://api.launchpad.net/1.0/>`_. I'll show
you the staging server for these examples so you don't accidentally
change something you don't mean to change. To get the service's
homepage, just sent an HTTP GET request to /1.0.

::

       GET /1.0 HTTP/1.1
       Host: api.staging.launchpad.net

The response you get back will look something like this:

::

       200 OK
       Content-type: application/json

       {"people_collection_link": "http:\/\/api.staging.launchpad.net\/1.0\/people", "bugs_collection_link": "http:\/\/api.staging.launchpad.net\/1.0\/bugs", "me_link": "http:\/\/api.staging.launchpad.net\/people/+me"}

That's a `JSON <http://json.org/>`_ document, which you can turn into a
native-language data structure using whatever libraries are available
for the programming language you're using. (In launchpadlib, we use the
Python simplejson library to process JSON documents.) Process it and
you'll have something like this Python data structure:

::

       { u"people_collection_link":
           u"http://api.staging.launchpad.net/1.0/people",
         u"bugs_collection_link":
           "http://api.staging.launchpad.net/1.0/bugs",
         u"me_link":
           "http://api.staging.launchpad.net/people/+me"}

.. note::

    If you're following along and you sent a GET to ``/1.0/``, you'll
    see that the "me_link" isn't actually present yet. The URL works, it's
    just that the web service homepage doesn't link to it yet. We're going
    to add that link soon, and it's very useful for purposes of discussion,
    so for now just pretend it's there.)

Almost all of the documents served through the Launchpad web service are
JSON documents. In fact, almost all of them describe dictionaries of
key-value pairs, like this one.

The Launchpad website's homepage contains links to other parts of
Launchpad. This homepage serves the same purpose: it tells you about the
major parts of the Launchpad web service. Once you've got the hang of
the web service you can bypass the web service's homepage, just as you
might bypass the Launchpad homepage, but it's a good place to start.

This document contains three links, and by following the links you can
explore the web service. As we expose more of Launchpad through the web
service, you'll see more links added to this document.

-  people_collection_link: This is the list of people tracked by
   Launchpad.
-  bugs_collection_link: This is the list of bugs tracked by Launchpad.
-  me_link: This is a link to your user account.

By convention, all fields that are links to other parts of the Launchpad
web service have names ending in '_link'. Other fields might have URLs
as values, and you can follow those URLs if you want, but they probably
don't have anything to do with the Launchpad web service.

Apart from the homepage, which you've just seen, there are two basic
types of objects in launchpad: *entries* and *collections*. An entry is
a single object, like a bug or your user account; a collection is a
group of entries. Links to collections always have names that end in
"_collection_link"; links to entries always have names that just end in
"_link".

An entry: your user account
~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you follow the "me_link" by making a GET request to
`<http://api.staging.launchpad.net/people/+me>`_.

::

       GET /1.0/people/+me HTTP/1.1
       Host: api.staging.launchpad.net

...you'll be redirected to the Launchpad web service's view of your user
account.

::

       302 Found
       Location: http://api.staging.launchpad.net/~your-user-name

Note the symmetry with the Launchpad website. If you visit
http://www.launchpad.net/people/+me in your web browser, you'll be
redirected to ``http://www.launchpad.net/~your-user-name``.

Your user account is an entry-type resource. It responds to a specific
HTTP interface that's common to all entry resources exposed by the
Launchpad web service: GET, PUT, and PATCH. Entry resources may also
respond to custom named GET and POST operations which are different for
every kind of entry; we'll cover those later.

Reading resources: GET
^^^^^^^^^^^^^^^^^^^^^^
The most basic operation on an entry resource is GET. To find out about
your user account you send a HTTP GET request to that URL:

::

      GET /1.0/~your-user-name HTTP/1.1
      Host: api.staging.launchpad.net

You'll get back a response document containing a JSON hash, just like
you did when you sent GET to the service root. Here's what the hash
looks like when I convert it to a Python dictionary.

::

   {u'admins_collection_link': u'http://api.staging.launchpad.net/1.0/~your-user-name/admins',
    u'confirmed_email_addresses_collection_link': u'http://api.staging.launchpad.net/1.0/~your-user-name/confirmed_email_addresses',
    u'date_created': u'2005-06-06T08:59:51.619713+00:00',
    u'deactivated_members_collection_link': u'http://api.staging.launchpad.net/1.0/~your-user-name/deactivated_members',
    u'display_name': 'Your name here',
    u'expired_members_collection_link': u'http://api.staging.launchpad.net/1.0/~your-user-name/expired_members',
    u'hide_email_addresses': False,
    u'homepage_content': None,
    u'indirect_participations_collection_link': u'http://api.staging.launchpad.net/1.0/~your-user-name/indirect_participations',
    u'invited_members_collection_link': u'http://api.staging.launchpad.net/1.0/~your-user-name/invited_members',
    u'irc_nicknames_collection_link': u'http://api.staging.launchpad.net/1.0/~your-user-name/irc_nicknames',
    u'is_team': False,
    u'is_valid': False,
    u'jabber_ids_collection_link': u'http://api.staging.launchpad.net/1.0/~your-user-name/jabber_ids',
    u'karma': 0,
    u'languages_collection_link': u'http://api.staging.launchpad.net/1.0/~your-user-name/languages',
    u'latitude': None,
    u'longitude': None,
    u'members_collection_link': u'http://api.staging.launchpad.net/1.0/~your-user-name/members',
    u'members_details_collection_link': u'http://api.staging.launchpad.net/1.0/~your-user-name/members_details',
    u'memberships_details_collection_link': u'http://api.staging.launchpad.net/1.0/~your-user-name/memberships_details',
    u'mugshot_link': u'http://api.staging.launchpad.net/1.0/~your-user-name/mugshot',
    u'name': u'your-user-name',
    u'open_membership_invitations_collection_link': u'http://api.staging.launchpad.net/1.0/~your-user-name/open_membership_invitations',
    u'participants_collection_link': u'http://api.staging.launchpad.net/1.0/~your-user-name/participants',
    u'participations_collection_link': u'http://api.staging.launchpad.net/1.0/~your-user-name/participations',
    u'preferred_email_address_link': u'http://api.staging.launchpad.net/~your-username/+email/your.address@foo.com',
    u'proposed_members_collection_link': u'http://api.staging.launchpad.net/1.0/~your-user-name/proposed_members',
    u'resource_type_link': u'http://api.staging.launchpad.net/1.0/#person',
    u'self_link': u'http://api.staging.launchpad.net/1.0/~your-user-name',
    u'sub_teams_collection_link': u'http://api.staging.launchpad.net/1.0/~your-user-name/sub_teams',
    u'super_teams_collection_link': u'http://api.staging.launchpad.net/1.0/~your-user-name/super_teams',
    u'team_owner_link': None,
    u'time_zone': None,
    u'visibility': u'Public',
    u'wiki_names_collection_link': u'http://api.staging.launchpad.net/1.0/~your-user-name/wiki_names'}

That's a lot of information. You can consult `the reference documentation <https://launchpad.net/+apidoc/devel.html>`_ for more information on
what each of the fields of this hash mean. What's important is that
there are three and only three kinds of fields:

1. Atomic chunks of data. Examples here include 'date_created',
   'display_name', and 'time_zone'. These may be of any JSON data type.
   Some of these can be modified: you can change your own
   'display_name', but you can't change 'date_created'. (How do you know
   which fields can be modified? See "WADL Description" below.)

2. Links to other entry-type resources. These work the same way as the
   "me_link" in the JSON representation of the Launchpad server root.
   'mugshot_link' points to your mugshot image.
   'preferred_email_address_link' points to a resource that represents
   your preferred email address. Remember, every object in Launchpad has
   its own URL, even tiny objects like email addresses and languages.
   Again, by Launchpad convention, all links between resources have
   field names that end in '_link'. Two of these links are especially
   important, and you'll find them present in every representation of an
   entry-type resource.

   -  'self_link' is the URL to the resource itself. You can keep track
      of this URL and come back to it later to find this resource again.
      It's just like bookmarking a web page.

   -  'resource_type_link' is a link to a machine-readable description
      of this resource. You can use this to do introspection on the
      resource, finding out what special operations are available, or
      which of the fields in the representation can be modified. For
      more on this see "WADL Description" below.

3. Links to collection-type resources. A person in Launchpad can be
   associated with more than one email address, but only one of those
   can be the 'preferred' address at any one time. The
   'preferred_email_address_link' field points to whatever address is
   currently preferred. The 'confirmed_email_addresses_collection_link'
   field points to a list containing all the addresses. For more on
   collections, see "The list of bugs" below.

Modifying resources: PUT
^^^^^^^^^^^^^^^^^^^^^^^^

(To make any changes, you must send a signed request.)

It's your user account; you should be able to change it through the web
service. The simplest way to do this is to take the document you
received from a GET request, modify it so that it says what you want,
and send it back to the server with a PUT request.

Let's say I want to change my display name. The document I got in the
previous section looks like this:

::

       {
          ...
         u'display_name': 'Your name here',
          ...
       }

Since I parsed that document into a data structure (call it 'person'),
it's easy for me to change that data structure with code. Here's Python
code that will work:

::

       person['display_name'] = 'New display name'

Then I can turn the data structure back into a JSON string. Now the
string looks like this:

::

       {..., "display_name": "New display name", ...}

Now I can send the document back to the server with PUT:

::

       PUT /1.0/~your-user-name HTTP/1.1
       Host: api.staging.launchpad.net
       Content-type: application/json

       {..., "display_name": "New display name", ...}

The response should indicate that the changes were made:

::

       200 OK

Modifying resources: PATCH
^^^^^^^^^^^^^^^^^^^^^^^^^^

The PUT technique is very convenient when you already have a document
describing the resource you want to modify. If you don't have such a
document, you don't have to create the whole thing. You can create a
smaller document from scratch, and only mention the fields you want to
change:

::

       {"display_name": "New display name"}

You can send this document to the server as part of a PATCH request:

::

       PATCH /people/~your-user-name HTTP/1.1
       Host: api.staging.launchpad.net
       Content-type: application/json

       {"display_name": "New display name"}

Again, the response should be simple:

::

       200 OK

Changing links
^^^^^^^^^^^^^^

Some of a resource's fields are links to other resource: for instance,
your preferred email address.

::

       print person['preferred_email_address_link']
       # http://api.staging.launchpad.net/~your-username/+email/your.address@foo.com

Since the value is shown as a URL, you change the value by changing the
URL. In this PATCH request I change my preferred_email_address_link so
that it points to another of the 'email address' type resources
associated with my user account.

::

       PATCH /people/~{your-user-name} HTTP/1.1
       Host: api.staging.launchpad.net
       Content-type: application/json

       {"preferred_email_address_link":
        "http://api.staging.launchpad.net/~your-username/+email/another.address@bar.com"}

How did I find that link? Well, you can get a collection of all your
confirmed email addresses by following the
"confirmed_email_addresses_collection_link". (See "the list of bugs"
below to learn what a collection looks like.) Each email address has its
own permanent URL, accessible as its 'self_link' field. Look through the
collection, find the address you want, and stick its 'self_link' URL
into the document describing your user account. Then you can make a
request that changes which email address is your 'preferred' one. In
Python code the link change might look like this:

::

       person['preferred_email_address_link'] = new_email_address['self_link']

Then you'd make a PUT or PATCH request to send the change to the server.

The WADL description (again, see below) tells you which links you're
allowed to modify. This information is also in the reference
documentation.

You can never change a link to a collection. The link to the collection
of your confirmed email addresses will always be
``http://api.staging.launchpad.net/1.0/~{your-user-name}/confirmed_email_addresses``.

Error handling
^^^^^^^^^^^^^^

If something goes wrong with your request, you'll probably get a
response code of 400 ("Bad Request") instead of 200 ("OK"). The body of
the response will tell you what was wrong with your request. For
instance, if you try to send PUT or PATCH data in a format other than
JSON...

::

       PATCH /people/~{your-user-name} HTTP/1.1
       Host: api.staging.launchpad.net

       display_name=New display name

...you'll get this response:

::

       400 Bad Request
       Content-type: text/plain

       Entity-body was not a well-formed JSON document.

A collection: the list of bugs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The user account resource is a typical example of an entry-type
resource: one that represents one specific thing. The other main sort of
resource in the Launchpad web service is a collection-type resource: one
that acts as a container for a number of other resources.

As with entry resources, every container resource has its own URL that
you can bookmark or pass around. Send a GET request to a container
resource, and you'll get you a JSON document describing the collection.

One interesting collection is the collection of filed bugs. Remember the
homepage of the Launchpad web service? The 'bugs_collection_link' there
is the URL to the collection of bugs.

Send a GET request to that URL...

::

       GET /1.0/bugs HTTP/1.1
       Host: api.staging.launchpad.net

...and you'll get back a JSON document that looks like this:

::

       {
         u'total_size' : 252673,
         u'next_collection_link' :
           u'http://api.staging.launchpad.net/1.0/bugs?ws.start=75&ws.size=75',
         u'resource_type_link' : u'http://api.launchpad.dev/1.0/#bugs',
         u'entries' : [ ... ]
       }

All collection resources serve JSON documents that look like this,
whether they're collections of bugs, people, bug tasks, email addresses
languages, or whatever. It's always a JSON hash with keys called
'total_size', 'resource_type_link', and 'entries'. The 'total_size'
field is the number of items in the collection, 'resource_type_link' is
a machine-readable description of the collection (see "WADL Description"
below). The 'entries' field contains the actual entries.

Except of course it doesn't contain *all* the entries. Putting over
250,000 bugs in one document would be crazy. Launchpad's web service
does the same thing as the Launchpad website: it sends you one page of
bugs at a time, and includes links (where appropriate) to the next and
previous pages. So the 'entries' field here is a JSON list containing 75
JSON hashes, each describing one bug. Each hash contains the same
information as if you'd sent a GET request to that bug's 'self_link'.

If you need more than 75 bugs, you can send a GET request to the
'next_collection_link'. If you need some other number of bugs, or you
want to start from item 20 in the list instead of the first item, you
can manually vary the 'ws.start' and 'ws.size' parameters. Sending a GET
request to
`<http://api.staging.launchpad.net/1.0/bugs?ws.start=9&ws.size=3>`_ would get
you three bugs: the ones that would be accessible from
"collection['entries'][9:12]" if you'd sent GET to
`<http://api.staging.launchpad.net/1.0/bugs>`_ and retrieved the first 75.

For consistency's sake, *all* collection resources serve JSON hashes
with 'total_size' and the rest, even collections which are very unlikely
to have more than 75 entries, like someone's list of spoken languages.

Named operations
~~~~~~~~~~~~~~~~

All entry resources support GET, PUT, and PATCH. All collection
resources support GET. There are also custom operations available on
specific resources. We call these "named operations" because they're
identified by name rather than by the name of one of the standard HTTP
methods.

These operations are described in the reference documentation (and in
the WADL file), and they're different for every kind of resource, so I
won't cover them all here. What I will do is give a couple examples and
talk about what all named operations have in common.

A named operation either modifies the Launchpad data set or it doesn't.
If it's read-only, then you access it with HTTP GET. If it's a write
operation, you need to access it with HTTP POST.

Read operations (GET)
^^^^^^^^^^^^^^^^^^^^^

The person search operation is a good example of a read operation.
Launchpad exposes a list of people at
`<http://api.staging.launchpad.net/1.0/people>`_, but for most applications
you don't want to page through the user accounts the way you would on
the Launchpad person list. Usually you want to *filter* that huge list
to find specific people.

To invoke the person search operation you make a GET request to this
URL:

::

       http://api.staging.launchpad.net/1.0/people?ws.op=find&text={text}

where "{text}" is the text you want to search for.

(Again, you can find out about this named operation by reading the
reference documentation or the WADL definition of
``http://api.staging.launchpad.net/1.0/people``. There's no secret here.)

The response to a read operation can be any JSON document, but it's
usually a JSON hash that looks exactly like the JSON representation of a
collection resource. It's got 'total_size', 'entries', possibly
'next_collection_link', and so on. So getting
``http://api.staging.launchpad.net/1.0/people?ws.op=find&text=foo`` gives
you the same kind of document as getting
``http://api.staging.launchpad.net/1.0/people``, but there'll be a lot less
data to process.

In general, you invoke a named operation on a resource by tacking the
query parameter "ws.op={operation name}" onto the resource's URL. In
this case, the resource was the collection of people and the name of the
operation was "find". It's just like calling a method in a programming
language: the resource is the object and the operation is the method.
Any arguments to the method are appended as additional query parameters.

Write operations (POST)
^^^^^^^^^^^^^^^^^^^^^^^

Team creation is a good example of a write operation. Launchpad treats
teams the same as people, so when you create a team you're adding to the
list of people. To invoke the team creation operation you make a POST
request to the list of people:

::

       POST /1.0/people HTTP/1.1
       Host: api.staging.launchpad.net
       Content-Type: application/x-www-form-urlencoded

       ws.op=newTeam&name={name}&display_name={display_name}

Where {name} is the name you want for the new team, and {display_name}
is how you want the team to be described. It's the same as for a read
operation, except all your query arguments go into the body of the POST
instead of into the URL.

Like read operations, write operations can return any JSON document.
Most often, they return nothing--only a status code of 200 ("OK") to
show that the operation was carried out. But operations that create new
Launchpad objects, like newTeam, do something different. If you manage
to create a team you'll see a response that looks like this:

::

       201 Created
       Location: http://api.staging.launchpad.net/1.0/~{name}

That's your indication that the team was created, and that you can find
the new team at ``http://api.staging.launchpad.net/1.0/~{name}``. Now you
can go over to the new team and make additional HTTP requests to
customize it, add memberships, and so on. In general, Launchpad's web
service gives you the URLs to newly minted resources, rather than making
you guess them.

A hosted file: a user's mugshot
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The fourth type of resource is the hosted file. This resource is a
front-end to a file stored in Launchpad's file library. The example I'll
use is a person's mugshot image. You can find the URL to this resource
by looking under 'mugshot_link' in the JSON representation of a person.
It should look like ``/1.0/~{person}/mugshot``.

Read (GET)
^^^^^^^^^^

When you send a GET request to a hosted file resource, you'll get back
an HTTP redirect to a file in Launchpad's file library.

::

       GET /1.0/~salgado/mugshot HTTP/1.1
       Host: api.staging.launchpad.net

You'll get back a response that looks like this:

::

       303 See Other
       Location: Location: http://staging.launchpad.net:58000/92/mugshot

Send a second GET request to the URL in Location, and you'll get the
image document itself.

::

       GET /92/mugshot HTTP/1.1
       Host: staging.launchpad.net:58000

::

       200 OK
       Content-Type: image/jpeg

       [image goes here]

Write (PUT)
^^^^^^^^^^^
To modify a hosted file resource, send a PUT request to its URL. (This
is the ``/1.0/~{person}`` URL on api.*.launchpad.net, not the library URL
you get back as a redirect.) Make sure to set the Content-Type header to
the MIME type of the file you're writing. You can also set the
Content-Disposition header to specify the server-side filename of the
file. Here's how to change a person's mugshot.

::

       PUT /1.0/~salgado/mugshot HTTP/1.1
       Host: api.staging.launchpad.net
       Content-Type: image/png
       Content-Disposition: attachment; filename=my-mugshot.png

       [image goes here]

Error handling
^^^^^^^^^^^^^^
Launchpad may enforce restrictions on the files you write. For instance,
a mugshot must be an image file, and the image must have a specific
height and width. If you send a bad file to Launchpad, you'll get a
response that looks something like this.

::

       400 Bad Request

       The file uploaded was not recognized as an image; please
       check it and retry.

Delete (DELETE)
^^^^^^^^^^^^^^^

To delete a hosted file, send a DELETE request to its URL:

::

       DELETE /1.0/~salgado/mugshot HTTP/1.1
       Host: api.staging.launchpad.net

This will not necessarily delete the file from the Launchpad library,
because there might be other references to it within Launchpad. But the
file will be disassociated from the hosted-file resource. In this case,
the "salgado" user will stop having a mugshot, and any future attempts
to GET /1.0/~salgado/mugshot will return HTTP 404 ("Not Found").

Using the reference documentation
---------------------------------

Throughout this document I've revealed seemingly secret information
about the capabilities of various resources. It makes intuitive sense
that you should send a GET to a resource's URL to find out more about
it, but how are you supposed to know that you can also send a GET to
that URL plus "?ws.op=find"? The HTTP standard says (more or less) that
if you PUT a document to a resource that supports PUT, the server should
try to apply your new document to the underlying dataset. But how are
you supposed to know that you're allowed to modify a person's "latitude"
but not their "karma"?

If you don't know the capabilities of a resource, you can look it up in
`the reference documentation <https://launchpad.net/+apidoc/devel.html>`_. First,
look at the resource's 'resource_type_link'. It'll be something like
``http://api.launchpad.dev/1.0/#bugs``. Take the anchor part of that URL
(here, ``#bugs``), and use it as an anchor into the reference
documentation.

That is, if the 'resource_type_link' is
``http://api.launchpad.dev/1.0/#bugs``, you can find human-readable
documentation about that resource by going to
``https://launchpad.net/+apidoc/devel.html#bugs`` in your web browser.

The reference documentation will tell you about all the fields in an
object's JSON representation, and all the HTTP methods it will respond
to.

Two ways to save time and bandwidth
-----------------------------------

Ask for compressed documents
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Launchpad's web service serves XML and JSON documents that compress very
well. You'll get the documents faster and save bandwidth if you ask
Launchpad to compress documents before sending them over the network.

You do this by specifying a compression algorithm in the "TE" request header. Launchpad's web service supports two compression algorithms: "gzip", the standard gzip algorithm handled by `Python's gzip module <https://docs.python.org/3/library/gzip.html>`_, and "deflate", the algorithm handled by `Python's zlib module <https://docs.python.org/3/library/zlib.html>`_. Both of these are as defined in `the HTTP standard <http://www.w3.org/Protocols/rfc2616/rfc2616-sec3.html#sec3.5>`_.

So your TE header will look like this:

::

     TE: deflate

or like this:

::

     TE: gzip

Launchpad will send you compressed data, and will set the
Transfer-Encoding response header to the name of the compression
algorithm it used. It'll either look like this:

::

      Transfer-Encoding: deflate

or like this:

::

      Transfer-Encoding: gzip

Most web servers use the Accept-Encoding and Content-Encoding headers to
handle compression. This isn't technically wrong, but it interferes with
other optimizations we want to make, so we do things differently.

Cache the documents you get
~~~~~~~~~~~~~~~~~~~~~~~~~~~

It's important that you cache the documents you get from Launchpad,
especially documents like the WADL file that are large and don't change
very often.

Here's how `httplib2 <http://code.google.com/p/httplib2/>`_ does
caching (launchpadlib is based on httplib2). When it makes a GET request
and gets a document back, it stores the document in a file, along with
all of the HTTP response headers. The next time it needs to make that
GET request, it uses the cached response instead of making another
request to get the same data back.

But how do you know that the document hasn't secretly changed since the
last time you retrieved it? Here's how to check without making the same
request again. When you get a document from Launchpad, you'll also get a
value for the HTTP response header "ETag". It'll look like this:

::

       ETag: "924eb0c15c911d64e633b5f012d046d04a83b571"

If you suspect the document has changed, make a GET request to the
document's URL, but include the ETag in the HTTP header "If-None-Match".

::

       If-None-Match: "924eb0c15c911d64e633b5f012d046d04a83b571"

If the document has changed, this will work just like a normal GET
request. You'll get back the changed version of the document, including
a new ETag. But if the document is the same as it used to be, you'll get
an HTTP response that looks like this:

::

       304 Not Modified

Instead of sending the document again, Launchpad is telling you that you
already have the most recent version. This is called "conditional GET",
and if you need more detail there's a lot more information about it on
the web.

Launchpad doesn't serve ETags for collections, only for individual
objects and for the server root.

Avoid stepping on other peoples' toes
-------------------------------------

Let's say I'm using the Launchpad website to change the details of a
bug, and you're using Launchpad's web service. I change the details of a
bug. A few seconds later, you make a contradictory change to the same
bug. You've overwritten my change without even knowing about it.

Here's how to avoid that problem. Remember the ETags from the previous
section? Whenever you make a PUT or PATCH request to an object, include
that object's ETag in the "If-Match" HTTP header.

::

       If-Match: "924eb0c15c911d64e633b5f012d046d04a83b571"

If no one has made a change to this object, your PUT or PATCH will go
through. If someone else made a change to the object that you haven't
seen, you'll get an HTTP response that looks like this:

::

       412 Precondition Failed

Launchpad is telling you that it didn't make your change because another
change happened that you don't know about. You'll have a chance to GET
the new version of the object (complete with a new ETag), work out any
contradictions between the other person's change and the change you want
to make, and re-submit with the new ETag.

WADL Description
----------------

Like most web service providers we publish `a prose document <http://launchpad.net/+apidoc/>`_ describing the capabilities
of all our resources. But we also publish a machine-readable document
containing the same information. It's written in
`WADL <https://www.w3.org/submissions/wadl/>`_ format, and you can use it as a
basis for tools that interact with the web service. In fact, the
reference documentation is just a human-readable transformation of the
WADL document. The launchpadlib Python library is a thin wrapper on top
of a generic WADL library: it becomes a Launchpad library when it reads
in Launchpad's WADL file.

Almost every interesting aspect of the web service is described in this
document. You can use it as a basis for your own tools that talk to
Launchpad. It's analogous to the HTML forms you use to manipulate a web
site, and it makes it possible to build tools that are loosely coupled
to the design of the web service.

The WADL document that describes Launchpad's resources is located at the
root of the web service: `<https://api.staging.launchpad.net/1.0/>`_. You'll
need to request a WADL representation instead of the JSON one we
retrieved in the first part of this tutorial:

::

       GET /1.0/ HTTP/1.1
       Host: api.staging.launchpad.net
       Accept: application/vd.sun.wadl+xml

By Launchpad convention, every entry resource has a 'resource_type_link'
that's an index into this document.
``http://api.staging.launchpad.net/1.0/#person``, for instance, is a
reference to the XML tag in this document with the ID "person". That's
the tag describing the capabilities of a "person" resource, and it's
what you'll find as 'resource_type_link' in the JSON representation of
every "person"-type resource.

What's not defined in this file? Mainly, there's a lack of information
about our URL structure. You've already seen that you can get a
description of any person in Launchpad by sending GET to
``http://api.staging.launchpad.net/1.0/~{name}`` and plugging in the name.
This is a useful shortcut that can often save you a few HTTP requests,
but the WADL file doesn't say anything about that. It's possible to put
this information into WADL; we just haven't implemented it yet.

You can get a WADL representation of most individual resources by
sending an appropriate GET request to the resource's URL:

::

       GET /1.0/~my-user-account HTTP/1.1
       Host: api.staging.launchpad.net
       Accept: application/vd.sun.wadl+xml

You'll get back a small WADL document that contains a reference to the
large WADL document at the service root. This can be useful if you're
lost and need to get back on track, or if you don't want to rely on the
Launchpad-specific 'resource_type_link' convention.

Miscellaneous tips and traps
----------------------------
-  When you pass parameters to methods, it is necessary to be aware of
   lazr.restful's data type marshalling - basically, data is represented
   as if it were fragments of JSON, which means string parameters need
   quotes around them.
