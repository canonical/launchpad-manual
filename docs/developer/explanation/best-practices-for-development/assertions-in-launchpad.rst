.. _assertions-in-launchpad:

Assertions in Launchpad
=======================

Assertions are part of good programming practice, and they should be used in 
Launchpad code.

Rules
-----

Although assertions are good, they shouldn't be used everywhere. These are the 
rules that should be followed when using them in Launchpad:

-   If the error is one that should be handled by clients of the code, it 
    should be a checked exception rather than an assert, and be documented 
    in the method or interface operation's docstring.
-   If the error is one that clients of the code shouldn't handle (e.g. when 
    preconditions are not met), an assert should be used. In this case, there 
    are two possible scenarios:

    -   If the docstring says something like "don't do such-and-such", then an
        assert statement should be used (recalling asserts will disappear if
        optimization is turned on so they should never be used to prevent bad 
        behaviour, such as returning the wrong value).
    -   If the docstring says something like "if you do such-and-such an 
        AssertionError will be raised", a "raise AssertionError()" statement 
        should be used.

-   Assertions should always have a conditional expression, and a string 
    explaining the rationale. The rationale makes it easier to scan the OOPS 
    report, for example.
-   No code should catch AssertionError: It is wrong to use a try-except block 
    to catch AssertionError. AssertionError is meant to highlight programmers' 
    errors and stop execution of the program.

As an example, we have the method ``bugTasksWithSharedInterest()`` in 
PersonView, which is meant to be called only when the user is logged in. This 
method is used only in one template, and protected by a tal:condition to 
make sure the user is logged in. In this case, it's reasonable to use an 
assertion, because calling this method without a logged in user is something 
that should not happen. This is the code::

    def bugTasksWithSharedInterest(self):
        assert self.user is not None, 'This method should not be called without a logged in user'

Here is an example of a function that does not need an assertion. In this case, 
we should be raising an error, instead::

    def marryPersons(self, person1, person2):
        assert person1 is not None
        assert person2 is not None

It is interesting to note what Tim Peters thinks of assertions.

http://mail.python.org/pipermail/python-dev/2000-November/010670.html

Testing your asserts
--------------------

As with any other code, asserts should be documented and tested to make sure 
misbehaving programmers will be caught. However, the documentation and test of 
asserts should not be part of the :spellexception:`API's` main documentation because they are not 
actually part of the API. For this reason, the test of asserts also should be 
either in a separate file or in a separate section of the same file.