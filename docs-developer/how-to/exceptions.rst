===================
Handling exceptions
===================

Catching exceptions
===================

Never catch ``AssertionError``, ``NameError``, or ``TypeError``.

Only catch ``ValueError`` when you are trying to convert a value to a type
using the builtin "type conversion" functions such as ``int()`` and
``float()``.

.. code-block:: python
                                                                         
    try:                                                                 
        foo = int(foo_str)
    except ValueError:    
        # Handle the non-int case.

You might want to catch ``TypeError`` when converting type, when the value
may be a string or may be None.  Resist this temptation!  You should
explicitly check for a None value before doing the conversion.
   
.. code-block:: python
                                                           
    if foo_str is None:                                       
        # Handle None value.
    try:                    
        foo = int(foo_str)
    except ValueError:    
        # Handle the non-int case.

Catching all exceptions
=======================

In most cases this is a bad idea, since it means that we don't know what
exactly might happen in the code protected by ``try:``.

As a developer, think again before you use ``except Exception:``; as a
reviewer, ask the author why he thinks that it is reasonable to do that.

Most importantly, we must not hide bugs this way.  You must either
raise the exception again after doing some cleanup like calling
``transaction.abort()``, or you must log an OOPS, which you can do using
``logger.exception()``.

``KeyboardInterrupt`` and ``SystemExit`` must not be caught under any
circumstances.

If you really need to catch all exceptions, do it this way:

.. code-block:: python

    try:
        # whatever.
    except Exception:
        # do some cleanup, if necessary.
        # log an OOPS or raise the exception again.

Raising exceptions
==================

Raise ``AssertionError`` when code that calls your code has not met its part
of the contract.  Use ``AssertionError`` if your code has been passed code
of the wrong type.  Don't use ``TypeError`` for this.

The reason is that we're writing an application, not a framework, not a
general purpose library.  We live and die by the contracts between the
pieces of our application.  When the contracts are not adhered to, we need
to know that unambiguously.

Application code should never raise ``TypeError`` or ``NameError``.

There are very limited circumstances in which it's OK to raise
``ValueError``.  Usually, it's more appropriate to use a more specific
exception.  However, if you have a function which converts data from one
form to another in a way similar to ``int()`` or ``float()``, raising
``ValueError`` may be appropriate.

In general, don't make your specific exceptions derive from ``ValueError``.
``ValueError`` is an error saying something about where in the structure of
the code the error is assumed to be: in some argument to a function, or
something like that.  That assumption is often unhelpful or misleading.

We should be more interested in what condition occurred than whether the
error might have been passed as an argument to a function at some point or
other.  Reflect this in your choice of exceptions.

Breaking the rules
==================

There are some occasions when infrastructure code needs to break these
rules.  These are special cases.  They should be few, and specially
commented.
