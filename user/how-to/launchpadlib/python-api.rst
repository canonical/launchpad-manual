Use the Python API
==================

This page has a bunch of examples of how to use \`launchpadlib\` and the
Python APIs. Think of it like a cookbook that you can add your favourite
recipe to.

If this duplicates `launchpadlib <API/launchpadlib>`__ or
`API/Uses <API/Uses>`__ too much, then please merge or edit pages as
needed.

Find out if your launchpadlib version is recent enough (>= 1.5.1)
-----------------------------------------------------------------

::

      import launchpadlib
      print(launchpadlib.__version__)

**1.5.1** or above is the answer you're looking for; almost all
subsequent examples assume you have at least that recent a launchpadlib.

Hello Launchpad!
----------------

Before an API client can do anything, it needs to login to Launchpad.
There are three possibilities:

-  "Anonymous login", which does not require user interaction but of
   course gives you only read-only access to public data
-  Access level requested by the client: the user must confirm they want
   to allow that level of access
-  Access level specified by the user. This may be confusing if the
   client program expects to be able to write but it's not allowed.

Ever wanted to have Launchpad greet you by your own name? Now you can,
in the comfort of your own home.

::

      from launchpadlib.launchpad import Launchpad
      launchpad = Launchpad.login_with('hello-world', 'production')
      print('Hello, %s!' % launchpad.me.display_name)

The \`hello-world\` bit is the name of the application and 'production'
means connect to the production server.

If your app is only going to read public data from launchpad, and not
write it you can make the process more user-friendly by telling
Launchpad that you only care about reading public data.

::

      from launchpadlib.launchpad import Launchpad
      launchpad = Launchpad.login_anonymously('just testing', 'production')

See also `guide to app login <API/launchpadlib#Getting_started>`__.

Does a bug have a release target?
---------------------------------

::

      from launchpadlib.launchpad import Launchpad
      
      def has_target(bug, series):
          series_url = str(series)
          for task in bug.bug_tasks:
              if str(task).startswith(series_url):
                  return True
          return False
      
      launchpad = Launchpad.login_with('hello-world', 'production')
      b = launchpad.bugs[324614]
      ubuntu = launchpad.distributions["ubuntu"]
      jaunty = ubuntu.getSeries(name_or_version="jaunty")
      has_target(b, jaunty)
      ### ==> should evalute to True

Listing the current package versions in a particular distroseries
-----------------------------------------------------------------

::

      from launchpadlib.launchpad import Launchpad
      
      launchpad = Launchpad.login_with('hello-world', 'production')
      ubuntu = launchpad.distributions["ubuntu"]
      archive = ubuntu.main_archive
      series = ubuntu.current_series
      archive.getPublishedSources(exact_match=True, source_name="apport", distro_series=series)[0].source_package_version
      ### ==> should return u'0.123'

Get dsc-files for sources in an archive
---------------------------------------

::

      import re

      ### See previous examples for how to get an archive.

      def get_dsc(archive):
          re_version = re.compile(r"^\d+\:")
          for spph in archive.getPublishedSources():
              version = spph.source_package_version
              version = re_version.sub("", version, spph)
              yield "%s/+files/%s_%s.dsc" \
                  % (archive.web_link, spph.source_package_name, version)

Copy an old version of a package into your PPA for a newer release
------------------------------------------------------------------

Sometimes you want to build the older version of a package from an
earlier Ubuntu release on the newest Ubuntu. You can use the API to
easily copy the old release's version into your PPA where it can be
re-published.

::

      from launchpadlib.launchpad import Launchpad
      
      launchpad = Launchpad.login_with('hello-world', 'production')
      ubuntu = launchpad.distributions["ubuntu"]
      archive = ubuntu.main_archive
      jaunty = ubuntu.getSeries(name_or_version="jaunty")
      jaunty_apport = archive.getPublishedSources(exact_match=True, source_name="apport", distro_series=series)[0]
      jaunty_apport.source_package_version
      ### ==> should return u'0.123'
      ppa = launchpad.me.getPPAByName(name="foobar")
      ppa.copyPackage(
         from_archive=archive,
         include_binaries=True, 
         source_name="apport",
         to_pocket=jaunty_apport.pocket, 
         to_series="karmic", 
         version=jaunty_apport.source_package_version)

Cache Launchpad credentials per application
-------------------------------------------

*This one is for older launchpadlibs. If you are using a current
version, just replace the code below with \`Launchpad.login_with`.*

From <https://launchpad.net/hydrazine> - use your own application name.

::

      def create_session():
          lplib_cachedir = os.path.expanduser("~/.cache/launchpadlib/")
          hydrazine_cachedir = os.path.expanduser("~/.cache/hydrazine/")
          rrd_dir = os.path.expanduser("~/.cache/hydrazine/rrd")
          for d in [lplib_cachedir, hydrazine_cachedir, rrd_dir]:
              if not os.path.isdir(d):
                  os.makedirs(d, mode=0700)

          hydrazine_credentials_filename = os.path.join(hydrazine_cachedir,
              'credentials')
          if os.path.exists(hydrazine_credentials_filename):
              credentials = Credentials()
              credentials.load(file(
                  os.path.expanduser("~/.cache/hydrazine/credentials"),
                  "r"))
              trace('loaded existing credentials')
              return Launchpad(credentials, service_root,
                  lplib_cachedir)
              # TODO: handle the case of having credentials that have expired etc
          else:
              launchpad = Launchpad.get_token_and_login(
                  'Hydrazine',
                  service_root,
                  lplib_cachedir)
              trace('saving credentials...')
              launchpad.credentials.save(file(
                  hydrazine_credentials_filename,
                  "w"))
              return launchpad

Get date a user joined a team
-----------------------------

This is an example of using team_membership details

::

   def get_join_date(team, user):
       team = launchpad.people[team]
       members = team.members_details
       for member in members:
           if member.member.name == user:
               return member.date_joined
       return None

   print(get_join_date("zeitgeist", "thekorn"))
   ### ==> should return a datetime.datetime object like  2009-06-14 18:01:10.511369+00:00

Turn on debugging output
------------------------

::

   import httplib2
   httplib2.debuglevel = 1

This enables detailed traces of requests launchpadlib makes. This can be
worthwhile for debugging issues or optimizing performance. (See also
`bug 520219 <http://launchpad.net/bugs/520219>`__ asking for better
logging here.)

Get a useful error message from launchpadlib
--------------------------------------------

*Recent versions of launchpadlib include useful information in the str()
of the exception object, so you don't need to do this*

Because launchpadlib is just a simple wrapper for an HTTP API, when the
Launchpad server raises an error, this appears on the client side as an
HTTP error. However, there is useful information to be had!

::

   #!python
   try:
       do_something_errorful()
   except HTTPError as e:
       # e.content has the actual Launchpad error.
       print(e.content)

Fetching an object's raw JSON
-----------------------------

Launchpadlib provides a nice Python wrapper around JSON objects, but it
does allow you to directly access the JSON itself. Each launchpadlib
object has a \`[Iself_link\` property which you can use to view the JSON
in a regular web brower, but you can not do this while using
launchpadlib's access permissions. This recipe shows you how to fetch
the JSON for an object with the same permissions as the currently
running script.

We can use the semi-private \`_browser\` member of the current
\`Launchpad\` object to grab the raw JSON using the current
authentication. We can pass a launchpadlib object's \`self_link\` URL to
the browser, the same as launchpadlib itself does.

::

   #!python

   from launchpadlib.launchpad import Launchpad

   launchpad = Launchpad.login_with('lplib.cookbook.json_fetcher', 'production', '.lplib-json_fetcher-cache')

   # Our authenticated browser object
   browser = launchpad._browser

   def get_person_as_json(person_name):
       person = launchpad.people[person_name]
       if not person:
           # Oops, this person does not exist.
           return None
       
       return browser.get(person.self_link)

Get the type of requested code review
-------------------------------------

The trick here (`bug 526362 <https://bugs.launchpad.net/bugs/526362>`__)
is that the review type is actually an attribute of the pending review,
and the pending review is recorded as a 'vote' with no vote or comment.
So you need to iterate the

::

   votes

attribute of the merge proposal.

Get IDs of recent package builds
--------------------------------

::

       from launchpadlib.launchpad import Launchpad

       # Authenticate and create a Launchpad instance
       launchpad = Launchpad.login_anonymously("just testing", "production", version="devel")

       # Get the Ubuntu distribution
       ubuntu = launchpad.distributions["ubuntu"]

       # Get the archive (main repository in this case)
       archive = ubuntu.main_archive

       # Search for the source package by name and version
       source_name = "glirc"
       version = "2.39.0.1-1build1"
       source_package = archive.getPublishedSources(source_name=source_name, version=version)

       if source_package:
           # Assuming we want the first result in case there are multiple
           package_version = source_package[0]

           # Get the list of builds for this source package version
           builds = package_version.getBuilds()

           # Filter builds that doesn"t have a specific status
           # filtered_builds = [build for build in builds if build.buildstate != "some state"]

           # Print build IDs and statuses
           for build in builds:
               print(f"Build Title: {build.title}, Status: {build.buildstate}, Link: {build.web_link}")
       else:
           print(f"Source package version {version} not found.")


