URL Traversal
=============

.. include:: ../includes/important_not_revised.rst

Launchpad does two forms of traversal

1. from a URL to a view
2. from an Interface to a URL

These are not symmetrical (you don't go from a view to a URL or from a
URL to an Interface).

Interface to URL
----------------

This is provided via the

::

   canonical.launchpad.webapp.canonical_url

function.

Pure ZCML style
~~~~~~~~~~~~~~~

If possible, use the ZCML browser:url directive to configure the URL
traversal

::

       <browser:url
           for="canonical.launchpad.interfaces.ICodeReviewMessage"
           attribute_to_parent="branch_merge_proposal"
           path_expression="string:comments/${id}"
           rootsite="code" />

This specifies:

1. We are defining a url for the ICodeReviewMessage interface
2. attribute_to_parent defines the attribute of this interface that
   refers to the parent interface. Remember, we are starting from a
   leaf, and working back to the root URL.
3. We are adding comments/${id} to the path of the parent Interface.
   Where id is the id field of the instance.
4. rootsite is the subdomain this URL should be rooted at

Test cases for each URL type should be added to

::

   lib/canonical/launchpad/doc/canonical_url_examples.txt

CanonicalUrlData
~~~~~~~~~~~~~~~~

Registering an ICanonicalUrlData adapter gives you more control, but is
more verbose:

First, you need some ZCML:

::

     <adapter
         factory="lp.code.model.branchtarget.get_canonical_url_data_for_target"/>

This specifies the adapter function that will convert an IBranchTarget
to an ICanonicalUrlData.

Next, you need to implement the factory:

::

   from zope.interface import implementer
   from zope.component import adapts

   @adapts(IBranchTarget)
   @implementer(ICanonicalUrlData)
   def get_canonical_url_data_for_target(branch_target):
       """Return the `ICanonicalUrlData` for an `IBranchTarget`."""
       return ICanonicalUrlData(branch_target.context)

The function decorators helps reduce the ZCML needed for registration,
they specify:

1. The interface that the adapter will provide: ``ICanonicalUrlData``.
2. The objects that the adapter works with: ``IBranchTarget``.

Note that this is using the context of the view to get the
ICanonicalUrlData. If it were only using the view, you'd get infinite
recursion.

URL to View
-----------

The parent interface should have a

::

   Navigation

subclass.

For example:

::

   class BranchMergeProposalNavigation(Navigation):

       usedfor = IBranchMergeProposal

       @stepthrough('comments')
       def traverse_comment(self, id):
           try:
               id = int(id)
           except ValueError:
               return None
           return self.context.getMessage(id)

This specifies

1. This Navigation subclass is for the IBranchMergeProposal interface.
2. It provides one set of sub-urls: 'comments/id', where id is used to
   retrieve the actual content object that will be viewed.

The alternative is @stepto, which describes a specific navigation
element. It provides navigation directly to the specified item.

The

::

   Navigation

must be registered:

::

     <browser:navigation
         module="canonical.launchpad.browser"
         classes="BranchMergeProposalNavigation" />

A view object must be provided for the view.

::

       class CodeReviewMessageView(LaunchpadView):
           pass

It should derive from either LaunchpadView or LaunchpadFormView

The view object must be registered for the appropriate interface:

::

       <browser:defaultView
           for="canonical.launchpad.interfaces.ICodeReviewMessage"
           name="+index" />
       <browser:page
           name="+index"
           facet="branches"
           for="canonical.launchpad.interfaces.ICodeReviewMessage"
           class="canonical.launchpad.browser.CodeReviewMessageView"
           permission="zope.Public"
           template="../templates/codereviewmessage-index.pt"
           />

This specifies that

1. The default view for
   canonical.launchpad.interfaces.ICodeReviewMessage is named +index
2. The pages we're configuring are for
   canonical.launchpad.interfaces.ICodeReviewMessage
3. The pages we're configuring use
   canonical.launchpad.browser.CodeReviewMessageView
4. The branches facet should be used. This controls certain aspects of
   display.
5. The zope.Public permission is required to view the view
6. The +index view name is associated with the template
   ../templates/codereviewmessage-index.pt