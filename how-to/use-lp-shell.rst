=====================
How to Use lp-shell
=====================

lp-shell is a CLI tool in the form of an interactive Python shell that
provides API functionality over Launchpad for the developers and users in a
quick and easy way. It is especially useful for providing support to users,
as well as to automate and fasten various Launchpad tasks and it is practically
necessary for some features that do not provide a UI alternative, especially
when they are early in their life-cycle.

Installation
------------

The way to install lp-shell is pretty straight forward. Only package needed is
“lptools”: 

.. code-block:: shell-session

    $ sudo apt install lptools

“lp-shell” resides in lptools, so this is all we need to connect to Launchpad.

[Optional, Recommended] Install IPython
_______________________________________

If we enter the lp-shell now, we will see that it is a python interpreter
environment. As a result, we can ease its use with some classic python tools
like IPython. This will provide command history, auto-fill and easier
exploration when inside the lp-shell.

.. code-block:: shell-session

    $ sudo apt install ipython3

How to Connect
--------------

After installation, we can enter into lp-shell using:

.. code-block:: shell-session

    $ lp-shell production devel

Thus, we are in, and free to do whatever we want as long as we have the
permissions.

.. note::

    When it is your first time entering into lp-shell, depending on whether you
    authorized your computer previously on Launchpad for other tasks or not, it
    may ask for an authorization which should promptly and automatically open a
    Browser tab for it.

    If it doesn't login automatically, we can use “lp.login_with()” method to
    manually trigger the authorization. Once done, the launchpad will cache
    the authorization information for future use.

All the resources open to API can be found in the `API Documentation 
<https://launchpad.net/+apidoc/>`_.

.. note::
    Currently, only devel is in use. (Which is why we used
    the “devel” argument on the lp-shell command.)

Special object: “lp”
____________________
lp-shell provides a built-in, out-of-the-box object to connect to Launchpad
called “lp”. It is the main Launchpad object we use as a base for all further
operations within the shell.

.. code-block:: text

    In [1]: lp

    Out[1]: <launchpadlib.launchpad.Launchpad at ...>


Special object: “lp.me”
_______________________
Another built-in object, residing in “lp". As a shortcut, it stores the user's
own account Person object. Making it easier to acquire the user account or use
it on other parts of the API.

.. code-block:: text

    In [1]: lp.me
    
    Out[1]: <person at https://api.launchpad.net/devel/~[YOUR-USERNAME]>

Special method: “lp.load()”
___________________________
lp.load() accepts a URL as its parameter. It accepts both absolute and
relative paths. But we recommend the use of relative paths, that come after 
“launchpad.net/”, as the absolute paths the API accepts are easy to mess, with
no discernible difference from relative path approach even when done correctly.

When the method is triggered, it returns an object that represents whatever
object is stored in that URL.

.. code-block:: text

    In [1]: lp.load('ubuntu')
    Out [1]: <distribution at https://api.launchpad.net/devel/ubuntu>

    In [2]: lp.load('launchpad/+bug/102455')
    Out [2]: <bug_task at https://api.launchpad.net/devel/launchpad/+bug/102455>

    In [3]: lp.load('~launchpad')
    Out [3]: <team at https://api.launchpad.net/devel/~launchpad>

How to navigate lp-shell
------------------------


While there are multiple ways to navigate and explore around lp-shell some of
the most useful are:

Using ``dir(object)``
_____________________

This is a standard python way to check the properties and the methods of 
objects, and is especially useful if we are unsure of what can we do or 
see with any given Launchpad object.

As a result, it will also show us the other exploration paths we can take.

.. code-block:: text

    In [1]: dir(lp)
    Out [1]: [...]

    In [2]:dir(lp.me)
    Out [2]: [...]

Using Special LP Object Entries
_______________________________

In the resultant list, we can find some of the more readily useful exploration
tools/attributes that every object on lp-shell have:

- lp_attributes: Name this resource's scalar attributes.
- lp_collections: Name the collections this resource links to..
- lp_entries: Name the entries this resource links to.
- lp_operations: Name all of this resource's custom operations.

.. note::
    These will return property lists of the original object. If we wish to
    reach into one of the elements of these lists, we must call it on the
    object that we called the above lists from.

.. code-block:: text

    In [1]: project = lp.load("lpci")

    In [2]: project.lp_attributes

    Out [2]: [
                …
                'reviewer_whiteboard',
                'screenshots_url',
                'sourceforge_project',
                'specification_sharing_policy',
                'summary',
                'title',
                'translationpermission',
                'translations_usage',
                …
             ]

    In [3]: project.summary

    Out [3]: 'Runner for Launchpad CI jobs.'

Saving changes
______________

If we make any changes to the entries of Launchpad, it is best to save them
manually using lp_save()

.. code-block:: text

    In [1]: lp.me.lp_save()

[Optional] IPython commands to know
___________________________________

If you decide to use lp-shell with IPython (which is recommended). Some
IPython commands that will be immensely useful are:

.. code-block:: text

    In [1]: object?

Details about the object. The name, parameters and the docstring. 

.. note::

    Methods, callables to be specific, need to be called without their parentheses.

For example: lp?, lp.me?, lp.me.lp_save?

.. code-block:: text

    In [1]: object??

Verbose details about the object. Includes the code as well.

For example: lp??, lp.me??, lp.me.lp_save??

.. code-block:: text
    
    In [1]: ?

Introduction and overview of IPython features.

.. code-block:: text

    In [1]: %quickref

Quick Reference Card of IPython.


