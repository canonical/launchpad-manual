.. _view-supported-fields-and-methods:

View supported fields and methods
=================================

If you don't know the capabilities of one of the objects you've got, you can
call ``dir()`` on it. You'll see all of its fields and all the custom methods it
supports. Unfortunately, you'll also see a bunch of launchpadlib-specific junk
that you don't care about. That's why we've made available these four lists:

-  ``lp_attributes``: Data fields of this object. You can read from these
   might be able to write to some of them.
-  ``lp_collections``: List of launchpad objects associated with this
   object.
-  ``lp_entries``: Other Launchpad objects associated with this one.
-  ``lp_operations``: The names of Launchpad methods you can call on the
   object.

::

      print(sorted(bug_one.lp_attributes))
      # ['date_created', 'date_last_message', 'date_last_updated', ... 'tags', 'title']
      print(sorted(bug_one.lp_operations))
      # ['addAttachment', 'addWatch', 'subscribe', 'unsubscribe']

If you need more detailed help, you can look the object up in
`the API documentation <https://api.launchpad.net/devel.html>`_. First,
find out the type of the object.

::

       print(repr(bug_one))
       # <bug at https://api.staging.launchpad.net/beta/bugs/1>

This is a 'bug' type object. Now you use the type of the object as an anchor
into the API documentation. To find out the capabilities of this object
and what data is stored inside it, you'd visit
`<https://api.launchpad.net/devel.html#bug>`_.

The API documentation is more geared towards web service hackers than
launchpadlib users, but it will tell you about all of this object's
attributes and all the supported operations.

-  The "Default representation" section tells you about the available
   attributes.

-  The "Custom POST methods" and "Custom GET methods" sections tell you
   about methods the object supports other than the default methods
   described below. The methods take whatever parameters are listed in
   "Request query parameters". (You can ignore the "ws.op" parameter
   because you're using launchpadlib; that's just the name of the
   method.)