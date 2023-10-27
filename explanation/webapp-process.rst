=========================================
How to go about writing a web application
=========================================

-- Steve Alexander <steve@z3u.com>

.. include:: ../includes/important_out_of_date.rst


Introduction
------------

This document presents an approach to constructing web applications,
emphazising well-designed user interaction.

In summary, we write a web application by

1. Design the database that lies behind the web application
   - Entity relationship models
   - SQL statements
2. Design the web application's user interface
   - Table of URLs (see later)
   - Page template mock-ups
3. Write the Interfaces that the application will use to access the database
   - interfaces.py files
4. Write the code and templates of the application
   - page templates
   - supporting classes
   - application components

Of course, this isn't a completely linear process.  Steps may be carried out
in parallel, and ongoing work in each step will feed into the other steps.

So that we can make rapid progress, and learn about the application as early
as possible, we should do steps 2, 3 and 4 focusing on just a few URLs at
a time (say, five or so).  Then, when those are finished, we can make any
necessary changes to the database model, and then repeat steps 2, 3 and 4
with some new URLs and new application functionality.



Web application architecture
----------------------------

For the purposes of this document, a web application is put together as
follows::

 +--------------------------------------------------------------------------+
 |              {  Amorphous cloud of URLs  }                               |
 |  URLS      {   /rosetta/foo/bar/baz.html   }                             |
 |             {                             }                              |
 |  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  |
 |                           { Pages       SubURLs                          |
 |            PRESENTATION   { Views       Templates                        |
 |                           { Traversal   Support classes                  |
 |                                                                          |
 |  WEB APP   ------------------------------------------------- Interfaces  |
 |                                                                          |
 |            APPLICATION    { Utilities   Components                       |
 |            COMPONENTS     { Adapters                                     |
 |                                                                          |
 |                                                                          |
 |            LIBRARIES      { Python standard library                      |
 |                           { Other libraries                              |
 |                                                                          |
 |  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~   |
 |                                                                          |
 |  DATABASE     relations, fields, constraints                             |
 +--------------------------------------------------------------------------+

The boundaries of our web application are URLs at the top and the database
at the bottom.  So, we must carefully define these things that lie at the
boundaries, so that we can work out what must go in the middle.

URLs
----

URLs are the boundary between the web application and web browsers.  When you
point a web browser at a URL, you'll get one of the following:

- page
- form
- image or other data
- redirect
- "not found" error
- "unauthorized" error

We'll be mostly concerned with pages, forms and redirects.  We'll be concerned
with image and other data only when they are "managed content" and not just
part of the skin of the site.  The photograph of a member of the site is an
example of managed content: it is stored in the database and may be
manipulated through using the application.  CSS files, javascript files,
icons and logos are typically elements that make up the "skin" of the
application, and are not managed through the application.

Another example of image or other data that is managed content is if we want
to allow users to download a .po or .pot file of translations.

Forms are rendered in HTML and will typically be "self-posting forms".  That
is, the address posted to when the [submit] button is pressed will be the
same as the address the page was got from.  This allows browsers' bookmarks
to work properly, allows us to straightforwardly validate data entered into
the form, and keeps the URL space neat.

The "not found" error is the familiar "404 Not Found" given when someone
tries to access a URL that is not known by our system.

An "unauthorized" error means that accessing the given URL requires some
authentication.  The browser will prompt the user to provide some additional
authentication.  Alternatively, if we use other login schemes than HTTP Basic
or HTTP Digest, then the web application may present a login form to the
user.

A "redirect" causes the browser to immediately fetch a different URL.  This
process is usually not noticed by the user.


The URL table
-------------

We need to construct a table describing the URLs used in our application. We
won't bother about the protocol part or any leading path segments of the URL.
In the table below, we'll assume all URLs start http://example.com/rosetta/...

The table has the following columns

- URL: The rest of the URL after /rosetta.  For clarity, we'll start it with
  a "./".  So, the rosetta application's main page might be "./index.html".
  If this table is written in HTML, this may be a link to a mock-up HTML page
  showing what will be found at that URL.

- Default: For application components, the default page to use.  More about
  this later.

- Type: This is one of "app component", "page", "form", "redirect", "data"

- Description: A textual description of what is found at this URL.
  This may be a link to further information about the functioning of that
  page, form validation constraints, and so on.

When you get an App Component at a particular URL, what does that mean?  At
certain points in our URL space, we want to expose a set of related
functionality under a particular URL.  For example, the URL
"./projects/mozilla/show-teams" might show the teams working on the Mozilla
project, while "./projects/mozilla/translations" might show the translations
of the mozilla project.  Users of the system will come to understand that
things related to Mozilla are to be found at URLs starting with
"./projects/mozilla".  We want to present some page at "./projects/mozilla".
Rather than make a special "no name" page for this, we choose one of the
other pages that we want to return.  Mozilla is a Project.  So, if the
default page for a Project is "translations", then going to
"./projects/mozilla" will return the same page as
"./projects/mozilla/translations".  The usual default page is "index.html".


Here's an example of a table for the Rosetta project::

  URL                 Default      Type            Description

  ./                  index.html   app component   The rosetta application

  ./index.html                     page            Initial navigation page

  ./intro.html                     page            Introductory page

  ./signup.html                    form            Allows a new user to
                                                   register with the system.

  ./projects          index.html   app component   Collection of rosetta
                                                   projects

  ./projects/index.html            form            Shows ways to search
                                                   through projects

  ./projects/$PROJECT translations app component   A particular project
                                                   $PROJECT is the name of
                                                   the project. See key below.

  ./projects/$PROJECT/translations page            Shows all translations
                                                   for this project.


  Key to $VARs
  ============
  $PROJECT    The name of the project.  This is the name attribute of
              the IProjectGroup interface, or the name field in the Project
              relation.  Case is not significant, and is normalized to
              lower-case in the UI.  Examples: 'mozilla', 'gtk+'.

We can use the URL table for simple automated functional testing of the web
application, given some suitable $VAR substitutions.


Structure of a web application URL
----------------------------------

We need to know what types of things are at a particular URL.  Here's an
example of a typical URL in a web application.  This time, I've included
the "rosetta" path segment at the root::

  /rosetta/projects/$PACKAGENAME/teams/$TEAM/add-member.html
   |       |        |            |     |     |
   |       |        |            |     |     page to add a new member
   |       |        |            |     Name of a particular team "22"
   |       |        |            The teams working on this project
   |       |        A particular project name, such as "mozilla"
   |       Collection of projects that can be queried
  The rosetta application


Guidelines for URLs
-------------------

* Make your URLs from lower-case letters, numbers, '-' and '+'.

* Avoid '_', capital letters, other symbols.
  Using these things makes the URL harder to read out over the phone or
  write down unambiguously.

* When you have a collection of things, such as people or projects, use
  a plural noun for that part of the URL.  For example, "./projects".

* Consider using "+" as the last URL segment for the URL that adds things
  to a collection.  For example, "./projects/+" to add a new project.

* Where possible, use self-posting forms.  So, you would go to the URL
  "./projects/+" to get a form asking you for the information needed to
  add a new project.  When you submit the form, it POSTs to the same
  URL.  If the provided information is invalid, you'll get the form back
  with an error message.  Otherwise, you'll get a "success" message, or be
  redirected to the next page in the workflow.



Development iterations
----------------------

When you're developing a new system, don't try to write the whole table of
URLs at once.  Instead, we can work in iterative cycles, designing pages
and URLs, and making these work in software.  That way, we can learn earlier
on if the URLs and pages we want will actually work in practice.

Here's the overall process of developing the application.

Overall Process
~~~~~~~~~~~~~~~

1. Lay out the total functionality of the system, and divide it into a number
   of iterations.
2. Pick the next iteration.  Go through the Iteration Process described below.
3. Review / refactor the specification for previous iterations based on what
   we learned during this iteration.
4. Refactor the whole application implemented so far to match the refactored
   specification.

Each iteration (that is, step 2 above) looks like this.

Iteration Process
~~~~~~~~~~~~~~~~~

1. Write the URLs required for this iteration into the URLs table.
   Ideally, there should be 3 to 7 URLs in each iteration.
2. Document the functionality required for each page.
3. Produce page template mockups.
4. Implement the functionality, using stub application components rather
   than real application components.
5. Connect the functionality to the real database, by replacing the stubs
   with real application components.


I will note that these processes are just guidelines on how to go about
writing the software.  You might choose to prototype the application in
order to learn about what URLs are required for some tricky interaction. Or,
you might decide to write two iterations' worth of URLs into the URLs table
all at once, but then implement them in two iterations.  The important thing
is to understand where you are in this process, and why you are doing what
you are doing at any particular stage.

Keep the iterations short!


Glossary
--------

Skin:
    The way the user interface looks in a web browser.  The elements of this
    user interface, including CSS, images and an overall site template.

    It is possible to provide multiple skins to the same web application,
    for example a simple one and a very complex one.

Published:
    Something that is made available at a particular URL is said to be
    published.

Presentation component:
    Some software that interacts with the browser's request and returns
    information to the browser.  This is typically a page template or a
    page template plus a supporting class.

    Other presentation components are traversers, which know what to do
    when further path segments are given in a URL; and resources, which
    are CSS files, javascript files, logos, icons, etc.

Application component:
    An object that represents application functionality, but not presentation
    functionality.  It should have a well-defined interface so that different
    implementations of a given application component can be presented by
    the same presentation components.

Component:
    An object that has clearly defined interfaces.

    These interfaces may represent what it offers, or what it requires in
    order to function.

Utility:
    A component that is looked up by the interface that it provides.

Adapter:
    A component that knows how to use a particular interface in order to
    provide a different interface.

Interface:
    A software-readable definition of an API provided by some object.

View:
    A kind of presentation component that provides a representation of
    some other component.

Browser presentation:
    Presentation intended for a web browser, as distinct from a presentation
    intended for XML-RPC or webdav.  Or even email.

Non-published {view,resource}:
    A {view,resource} that is used by other presentation components, but
    that is not itself addressable by a URL.

Page:
    An HTML document returned to a browser in response to a GET or POST
    request to some URL.

Form:
    A page that contains HTML form elements and at least one "submit"
    button.

Self-posting form:
    A form that's "action URL" is the same address that it was loaded from.
    So, a form that was loaded from "./projects/+" would start::

      <form action="http://example.com/rosetta/projects/+" method="POST">


