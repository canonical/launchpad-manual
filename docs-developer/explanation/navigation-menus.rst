Navigation menus
================

.. include:: ../includes/important_not_revised.rst

When linking different views in Launchpad page templates it is recommend
to use the NavigationMenu attached to each facet of that object.

The NavigationMenus are defined in the *browser* code.

An object can have multiple *facets*. For example IPerson has a 'code',
'overview', 'translation' .. etc facets.

Here is a definition of the IPerson navigation menu for *translations*
facet.

::

   class IPersonTranslationsMenu(NavigationMenu):

       usedfor = IPerson
       facet = 'translations'
       links = ['translations', 'imports']

       def translations(self):
           return Link('', 'Overview')

       @enabled_with_permission('launchpad.Edit')
       def imports(self):
           return Link('+imports', 'Import queue', icon='edit')

An

::

   Link('', 'Some text')

will only return the text without the anchor tag.

From withing a page template, you can use the following TAL expression to
generate a link:

::

   person_object/menu:translations/imports/render

or you can get only the URL using

::

   person_object/menu:translations/imports/url

In the current codebase you may encounter the following code which is
not recommended:

::

         <div tal:condition="context/required:launchpad.Edit">
           <a href="+imports" class="edit sprite">Import queue</a>
         </div>

Instead you should use:

::

         <div tal:condition="context/required:launchpad.Edit">
           <a tal:attributes="href context/menu:navigation/imports/url" class="edit sprite">Import queue</a>
         </div>

Or better:

::

           <a tal:replace="structure context/menu:navigation/imports/render" />

In the above code you can use either **context/menu:navigation/imports**
or **context/menu:translations/imports**. *menu:navigation* is using the
same facet associated with the current view.
