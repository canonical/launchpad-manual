launchpadlib
============

.. toctree::
  :hidden:
  :maxdepth: 2

  The Launchpad web service <launchpad-web-service>

launchpadlib is an open-source Python library that lets you treat the HTTP resources
published by Launchpad's web service as Python objects responding to a standard set of commands.
With launchpadlib you can integrate your applications into Launchpad without knowing a lot about
HTTP client programming.

Launchpad's web service currently exposes the following major parts of Launchpad:

* People and teams  
* Team memberships  
* Bugs and bugtasks  
* The project registry  
* Hosted files, such as bug attachments and mugshots.

As new features and capabilities are added to the web service, you'll be able to access most of
them without having to update your copy of launchpadlib. You *will* have to upgrade launchpadlib
to get new client-side features (like support for uploaded files). The Launchpad team will put
out an announcement whenever a server-side change means you should upgrade launchpadlib.

The top-level objects
---------------------

The Launchpad object has attributes corresponding to the major parts of Launchpad. These are:


* ``.bugs``: All the bugs in Launchpad  
* ``.people``: All the people in Launchpad  
* ``.me``: You  
* ``.distributions``: All the distributions in Launchpad  
* ``.projects``: All the projects in Launchpad  
* ``.project_groups``: All the project groups in Launchpad

As a super special secret, distributions, projects and project_groups are all actually the same thing.


* me \= launchpad.me  
* print(me.name)
  # This should be your user name, e.g. 'salgado'

The launchpad.people attribute gives you access to other people who use Launchpad.
This code uses launchpad.people to look up the person with the Launchpad name "salgado".


* people \= launchpad.people  
* salgado \= people['salgado']  
* print(salgado.display_name)
  # Guilherme Salgado

You can search for objects in other ways. Here's another way of finding "salgado".


* salgado \= people.getByEmail(email="guilherme.salgado@canonical.com")  
* print(salgado.display_name)
  # Guilherme Salgado

Some searches return more than one object.


* for person in people.find(text="salgado"):  
* print(person.name)  
* # agustin-salgado  
* # ariel-salgado  
* # axel-salgado  
* # bruno-salgado  
* # camilosalgado
  # ...

.. note::
    Unlike typical Python methods, these methods--find() and getByEmail()--don't support
    positional arguments, only keyword arguments. You can't call people.find("salgado");
    it has to be people.find(text="salgado").

Entries
-------

Bugs, people, projects, team memberships, and most other objects published through
Launchpad's web service, all work pretty much the same way. We call all these objects
"entries". Each corresponds to a single piece of data within Launchpad.

You can use the web service to discover various facts about an entry. ``launchpadlib``
makes the facts available as attributes of the entry object.

name and display_name are facts about people.


* print(salgado.name)  
* # salgado  
* 
* print(salgado.display_name)
  # Guilherme Salgado

private and description are facts about bugs.


* print(bug_one.private)  
* # False  
* 
* print(bug_one.description)  
* # Microsoft has a majority market share in the new desktop PC marketplace.  
* # This is a bug, which Ubuntu is designed to fix.
  # ...

Some of an object's attributes are links to other entries. Bugs have an attribute owner,
but the owner of a bug is a person, with attributes of its own.


* owner \= bug_one.owner  
* print(repr(owner))  
* # \<person at https://api.staging.launchpad.net/beta/\~sabdfl\>  
* print(owner.name)  
* # sabdfl  
* print(owner.display_name
  # Mark Shuttleworth

If you have permission, you can change an entry's attributes and write the data back
to the server using lp_save().


* me \= people['my-user-name']  
* me.display_name \= 'A user who edits through the Launchpad web service.'  
* me.lp_save()  
* 
* print(people['my-user-name'].display_name)
  # A user who edits through the Launchpad web service.

Having permission means not only being authorized to perform an operation on the
Launchpad side, but using a launchpadlib Credentials object that authorizes the operation.
If you've set up your launchpadlib Credentials for read-only access, you won't be able to
change data through launchpadlib.

self_link: the permanent ID
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Every entry has a self_link attribute. You can treat this as a permanent ID for the entry.
If your program needs to keep track of Launchpad objects across multiple runs, a simple way
to do it is to keep track of the self_links.


* print(salgado.self_link)  
* # https://api.staging.launchpad.net/beta/\~salgado  
* 
* 
  bug_one.self_link
  # https://api.staging.launchpad.net/beta/bugs/1

  ## web_link: the link to the Launchpad website

Most of the entries published by the web service correspond to pages on the Launchpad website.
You can get the website URL of an entry with the web_link attribute:


* print(salgado.web_link)  
* # https://staging.launchpad.net/\~salgado  
* 
* bug_one.web_link
  # https://bugs.staging.launchpad.net/bugs/1

Some entries don't correspond to any page on the Launchpad website: these entries won't have a web_link.

Named operations
~~~~~~~~~~~~~~~~

Entries can support special operations just like collections, but again note that,
these methods don't support positional arguments, only keyword arguments.

Errors
------

When the Launchpad web service encounters an error, it sends back an error message to launchpadlib,
which raises an HTTPError exception. You'll see information about the HTTP request that caused the error,
and the server-side error message. Depending on the error, you may be able to recover or change your code and try again.

If you're using an old version of launchpadlib, the HTTPError may not be this helpful.
To see the server-side error message, you'll need to print out the .content of the HTTPError exception.

`Toggle line numbers <https://help.launchpad.net/API/launchpadlib#>`_


* `1 <https://help.launchpad.net/API/launchpadlib#CA-fb78a48ac0526ee8649dc78bfa231d31edb45c55_1>`_ try:  
* `2 <https://help.launchpad.net/API/launchpadlib#CA-fb78a48ac0526ee8649dc78bfa231d31edb45c55_2>`_    failing_thing()  
* `3 <https://help.launchpad.net/API/launchpadlib#CA-fb78a48ac0526ee8649dc78bfa231d31edb45c55_3>`_ except HTTPError as http_error:  
* 
  `4 <https://help.launchpad.net/API/launchpadlib#CA-fb78a48ac0526ee8649dc78bfa231d31edb45c55_4>`_    print(http_error.content)

Collections
-----------

When Launchpad groups similar entries together, we call it a collection.
You've already seen one collection: the list of people you get back when you call ``launchpad.people.find``.


* for person in launchpad.people.find(text="salgado"):  
  .. code-block::

      print(person.name)

That's a collection of people-type entries. You can iterate over a collection as you can any Python list.

Some of an entry's attributes are links to related collections. Bug #1 has a number of associated bug tasks,
represented as a collection of 'bug task' entries.

* tasks \= bug_one.bug_tasks  
* print(len(tasks))  
* # 17  
* for task in tasks:  
* print(task.bug_target_display_name)  
* # Computer Science Ubuntu  
* # Ichthux  
* # JAK LINUX
  # ...

The person 'salgado' understands two languages, represented here as a collection of two language entries.

* for language in salgado.languages:  
* print(language.self_link)  
* # https://api.staging.launchpad.net/beta/+languages/en
  # https://api.staging.launchpad.net/beta/+languages/pt\_BR

Because collections can be very large, it's usually a bad idea to iterate over them.
Bugs generally have a manageable number of bug tasks, and people understand a manageable
number of languages, but Launchpad tracks over 250,000 bugs. If you just iterate over a list,
launchpadlib will just keep pulling down entries until it runs out, which might be forever
(or, realistically, until your client is banned for making too many requests).

That's why we recommend you slice Launchpad's collections into Python lists, and operate on the lists.
Here's code that prints descriptions for the 10 most recently filed bugs.


* bugs \= launchpad.bugs[:10]  
* for bug in bugs:  
  .. code-block::

     print(bug.description)

For performance reasons, we've put a couple restrictions on collection slices that don't apply
to slices on regular Python lists. You can only slice from the beginning of a collection, not the end.

* launchpad.bugs[-5:]
   # *** ValueError: Collection slices must have a nonnegative start point.

And your slice needs to have a definite end point: you can't slice to the end of a collection.

* bugs[10:]  
* # *** ValueError: Collection slices must have a definite, nonnegative end point.  
* 
* bugs[:-5]
  # *** ValueError: Collection slices must have a definite, nonnegative end point.

On the plus side, you can include a step number with your slice, as with a normal Python list:


* every_other_bug \= launchpad.bugs[0:10:2]  
* 
  len(every_other_bug)
  # 5

Hosted files
------------

Launchpad stores some data in the form of binary files. A good example is people's mugshots.
With launchpadlib, you can read and write these binary files programatically.

If you have a launchpadlib reference to one of these hosted files, you can read its data
by calling the open() method and treating the result as an open filehandle.

* mugshot \= launchpad.me.mugshot  
* mugshot_handle \= mugshot.open()  
* mugshot_handle.read()  
* # [binary data]  
* mugshot_handle.content_type  
* # 'image/jpeg'  
* mugshot_handle.last_modified
  # 'Wed, 12 Mar 2008 21:47:05 GMT'

You'll get an error if the file doesn't exist: for instance, if a person doesn't have a mugshot.


* launchpad.people['has-no-mugshot'].mugshot
   # *** HTTPError: HTTP Error 404: Not Found

To create or overwrite a file, open the hosted file object for write. You'll need to provide the
access mode ("w"), the MIME type of the file you're sending to Launchpad, and the filename you
want to give it on the server side.


* with mugshot.open("w", "image/jpeg", "my-image.jpg") as mugshot_handle:  
  .. code-block::

      mugshot\_handle.write("image data goes here")

If there's something wrong--maybe you provide a file of the wrong type--you'll get an HTTPError
with a status code of 400. The content attribute will contain an error message.

* print(http_error.content)  
* # This image is not exactly 192x192 pixels in size.  
* 
* print(http_error.content)  
* 
  # The file uploaded was not recognized as an image; please
  # check it and retry.

  # Persistent references to Launchpad objects

Every entry and collection has a unique ID: its URL. You can get this unique
ID by calling str() on the object.


* print(str(bug_one))
   # https://api.staging.launchpad.net/beta/bugs/1

If you need to keep track of Launchpad objects over time, or pass references to Launchpad
objects to other programs, use these strings. If you've got one of these strings, you can
turn it into the corresponding Launchpad object by calling launchpad.load().


* bug_one \= launchpad.load("https://api.staging.launchpad.net/beta/bugs/1")  
* print(bug_one.title)
  Microsoft has a majority market share

You're bookmarking the Launchpad objects and coming back to them later,
just like you'd bookmark pages in your web browser.

Three things to make your client faster
---------------------------------------

1. **Use the latest launchpadlib.** (The versions in the current Ubuntu release
should be fine; otherwise run from the branch or the latest tarball).

2. **Profile:**

* import httplib2
   httplib2.debuglevel \= 1

3. **Fetch objects only once**:

Don't do this:

* if bug.person is not None:  
  .. code-block::

      print(bug.person.name)

instead, do this:

* p \= bug.person  
* if p is not None:  
  .. code-block::

     print(p.name)

(From `the blog <http://blog.launchpad.net/api/three-tips-for-faster-launchpadlib-api-clients>`_).

Planned improvements
--------------------

launchpadlib still has deficiencies. We track bugs in the launchpadlib bug tracker
(`https://bugs.launchpad.net/launchpadlib <https://bugs.launchpad.net/launchpadlib>`_)
and will be working to improve launchpadlib throughout the limited beta.

Further information
-------------------

* `web service reference documentation <http://launchpad.net/+apidoc/>`_
  for a list of all objects, operations, etc