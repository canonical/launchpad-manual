Handling security policies
==========================

Zope 3 is a security-aware framework that makes it possible to develop complex
applications with security policies that closely resemble the reality that the
system is trying to model.

This document is about security policy in Launchpad.

Defining Permissions in Launchpad
---------------------------------

.. note::

    A new permission should only be defined if absolutely necessary, and it
    should be considered thoroughly in a code review.

Occasionally, you'll find yourself in a situation where the existing
permissions in Launchpad aren't enough for what you want. For example, when
privacy support was first being added to Launchpad, it required a permission
to provide policy for who can view a thing, called ``launchpad.View``.

A new permission (see the note above) is defined in Launchpad in the file
``lib/lp/permissions.zcml``. So, to define the permission
``launchpad.View``, we'd add a line like this to that file:

.. code-block:: xml

    <permission
      id="launchpad.View" title="Viewing something" access_level="read" />


Defining Authorization Policies for Permissions
-----------------------------------------------

Once you've defined a permission, you'll probably want to define some logic
somewhere to express the authorization policy for that permission on a certain
interface.

In Launchpad, an authorization policy is expressed through a security adapter.
To define a security adapter for a given permission on an interface:

1. Define the adapter in the corresponding package's `security.py`. Create
   the file, if it doesn't exist already. Here's a simple example of
   an adapter that authorizes only an object owner for the
   ``launchpad.Edit`` permission on objects that implement the ``IHasOwner``
   interface:

.. code-block:: python

    class EditByOwner(AuthorizationBase):
        permission = "launchpad.Edit"
        usedfor = IHasOwner

        def checkAuthenticated(self, user):
            """Authorize the object owner."""
            return user.isOwner(self.obj)

Read the ``IAuthorization`` interface to ensure that you've defined the
adapter appropriately.

2. Declare the permission on a given interface in a ZCML file. So, for the
   above adapter, here's how it might be hooked up to ``IProduct``, where
   ``IProduct`` is protected with the ``launchpad.Edit`` permission:

.. code-block:: xml

    <class
        class="lp.registry.model.product.Product">
        <allow
          interface="lp.registry.interfaces.product.IProductPublic"/>
        <require
          permission="launchpad.Edit"
          interface="lp.registry.interfaces.product.IProductEditRestricted"/>
        <require
          permission="launchpad.Edit"
          set_attributes="commercial_subscription description"/>
    </class>

In this example, the ``EditByOwner`` adapter's ``checkAuthenticated`` method
will be called to determine if the currently authenticated user is
authorized to access whatever is protected by ``launchpad.Edit`` on an
``IProduct``.

The available permission directives are not well-documented by
``zope.security``, so here's a summary:

``<allow interface="..."/>``
    The attributes and methods of this class that appear in the listed
    interface may be publicly accessed.

``<allow attributes="..."/>``
    The named attributes and methods of this class may be publicly accessed.

``<require permission="..." interface="..."/>``
    The attributes and methods of this class that appear in the listed
    interface may be accessed by users with the given permission.

``<require permission="..." attributes="..."/>``
    The named attributes and methods of this class may be accessed by users
    with the given permission.

``<require permission="..." set_schema="..."/>``
    The attributes of this class that appear in the listed interface may be
    modified by users with the given permission.

``<require permission="..." set_attributes="..."/>``
    The named attributes of this class may be modified by users with the
    given permission.

Note that "accessed" means ``getattr()``, while "modified" means
``setattr()``.  The process of calling a method starts by using ``getattr()``
to fetch the method from the object, so methods should be declared in
``interface`` or ``attributes`` even if they modify the object.

3. Ensure that there is an ``<lp:authorizations />`` directive in the
   package's top-level ``configure.zcml`` file that specifies the package's
   security module. If it isn't there already, add one like:

.. code-block:: xml

    <lp:authorizations module=".security" />

To make the ``lp:`` namespace prefix work, the ``<configure />`` tag at the
top of the file should include the attribute
``xmlns:lp="http://namespaces.canonical.com/lp"``.
