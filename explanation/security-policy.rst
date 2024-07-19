Launchpad Security Policy
=========================

.. include:: ../includes/important_not_revised.rst

Launchpad uses "permission" to control access to views, object
attributes and object methods.

Permission are granted based on the context object type (its interface)
by an ``IAuthorization`` adaptors. Traditionally these adaptors have
all been defined in the ``canonical.launchpad.security`` module, but
they are being moved out in the ``security.py`` module of the specific
application.

To find out who has a named permission on an object, the
``IAuthorization`` adapter named after the permission is looked for.
Simply put, to see if the "launchpad.Permission" is granted on an
``IFoo`` object, the answer will come from the object returned by

.. code:: python

   getAdapter(foo, IAuthorization, name='launchpad.Permission')

Common permissions
------------------

Launchpad defines two permissions that are always defined for all
objects with a hard-coded set of users.

-  **zope.Public**: Everybody has this permission.

-  **launchpad.AnyPerson**: All authenticated users have this
   permission.

Then there is a set of basic permissions that have a common semantic,
but which the users granted it will differ based on the object type.

-  **launchpad.View**: Permission required to access attributes,
   objects, and views.

-  **launchpad.Append**: Permission required to add information to an
   object for example, to comment on an object.

-  **launchpad.Edit**: Permission required to modify attributes and objects.


-  **launchpad.Moderate**: Permission required to approve, reject,
   review an object.

-  **launchpad.Admin**: Permission required to do administrative task on
   the object.

These permissions are also layered, in the sense that having an higher
permission usually implies the one below. (For example, launchpad.Admin
implies Edit, Append, View, etc.) The only exception to this rule is for
launchpad.Moderate which implies View, but not necessarily Edit nor
Append.

Launchpad defines and use a couple of special permissions that are less
generic and don't fit in this layered model. We should refrain from
adding these as they make understanding the model more complex.

Assigning permissions
---------------------

zcml directives assign permissions to the attributes of interface
implementations. This means that a user may have permission to access an
attribute, without actually being able to.

SecurityProxy
-------------

The ``SecurityProxy`` is a wrapper that enforces these requirements. It
does not apply to classes that are constructed directly. If no
permission is assigned to a given attribute, attempting to access it is
**forbidden**. If there is a permission assigned to it, and the current
user does not have that permission, attempting it is **unauthorized**.
If the current user has the correct permission, then that attribute will
behave almost exactly the same as it would on an unproxied object. The
main difference is that any return values may be wrapped in a
SecurityProxy as well.

ForbiddenAttribute
------------------

There are several possible causes:

-  The attribute does not exist. (This would normally cause an
   AttributeError.)
-  The attribute is present in the database class, but not in the
   relevant interface class.

-  The attribute is not named in the relevant ZCML file. This does not
   apply if the entire interface is allowed.

-  There *is* no corresponding interface.

This is not the same as Unauthorized. Unauthorized means that an
authorization regime has been properly set up, but the current user is
not authorized.
