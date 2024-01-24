===============
CSS style guide
===============

This page documents conventions for our Launchpad CSS and SCSS files.
Following the principles outlined in this document will minimize comments
related to CSS conventions from reviewers.


Class Names
-----------

Overall, for naming a class we use lower case words separated by hyphens
(``-``). For example:

.. code-block:: html

    # Good
    <div class="social-accounts">...</div>

    # Bad
    <div class="social_accounts">...</div>
    <div class="socialaccounts">...</div>
    <div class="SocialAccounts">...</div>

When it comes to naming classes, for new components we follow the `BEM
convention <https://getbem.com/naming/>`_, which is also used by the `Vanilla
framework <https://vanillaframework.io/docs>`_.


BEM
===

When creating a new component or section with nested elements that have no
standalone meaning, the nested elements should have the name of the parent
block class, followed by two underscores (``__``), followed by the element
name. For example:

.. code-block:: html

    # Good
    <div class="social-accounts">
        <div class="social-accounts__item">...</div>
    </div>

    # Bad
    <div class="social-accounts">
        <div class="social-accounts-item">...</div>
        <div class="item-social-account">...</div>
    </div>

See `Vanilla accordions <https://vanillaframework.io/docs/patterns/accordion>`_
as another example.

When it comes to modifiers for a class (classes to change appearance, behaviour
or state), you should use the name of the original class, followed by
two hyphens (``--``), followed by the modifier name. For example:

.. code-block:: html

    # Good
    <div class="message">...</div>
    <div class="message--error">...</div>
    <div class="message--success">...</div>

    # Bad
    <div class="message error">...</div>
    <div class="error-message">...</div>

See `Vanilla buttons <https://vanillaframework.io/docs/patterns/buttons>`_
as another example.


CSS and SCSS
------------

In general, SCSS files are preferred over CSS files.

When adding CSS styling to a new block/section/component, one should create a
new SCSS file in the `lib/canonical/launchpad/icing/css/components` directory
named after the new component, and add it to the `_index.scss` file in the
same directory.

Nesting class styles can be used when writing SCSS when it makes
sense and as long as its nesting is kept to a level or two. For example:

.. code-block:: scss

    .social-accounts {
        padding: 1em;
        color: grey;

        a {
            color: black;
        }
    }
