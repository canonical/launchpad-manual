Launchpad API Docs generation
=============================

The Launchpad API documentation portal is available at
`<https://api.launchpad.net/>`_. It contains summaries of the different
web service versions, and links to version-specific documents.

To define our web resources we are using the 
`lazr.restful <https://lazrrestful.readthedocs.io/en/latest/webservice-declarations.html>`_ 
decorators and capabilities. These decorators are also responsible to generate
the related documentation for the exported field.

We can build Api Docs using ``make apidoc`` command: this command will 
generate the documentation under ``lib/canonical/launchpad/apidoc``. 
Note that we should delete the aforementioned folder in order to generate
fresh docs. 

The command above is responsible to call the 
``utilities/create-lp-wadl-and-apidoc.py`` script and generate the related
documentation using the ``lp.services.webservice.wadl`` module utilities.

This scripts will create the related ``wadl`` and then it will translated to
``HTML``. During this process ``generate_html`` function will be called: this
function is responsible to map ``wadl`` entries to ``HTML``.
To do that we use as template the file called ``wadl-to-refhtml.xsl``: in 
this file we can also apply patches to fix not-well generated entry points
for given ``wadl`` entries.

Example
~~~~~~~

For example for the ``SocialAccount`` webservice we used the
``@exported_as_webservice_entry("social_account", as_of="beta")`` decorator.
Thanks to that the ``social_account`` entry is created.
We can use the aforementioned id to refer this ``wadl`` entry in the ``wadl-to-refhtml.xls`` file.

Let's say that we want to change the entry URL
from ``URL: https://api.launchpad.net/beta/``
to ``URL: https://api.launchpad.net/beta/<person.name>/+socialaccount/<id>``:
we should create an entry inside the ``find-entry-uri`` template inside the 
``wadl-to-refhtml.xls`` file and we should search our ``wadl`` entry using the 
``social_account`` id. After that we can write ``xls`` code that will append the
right string to the ``$base`` URL:

..  code-block:: html
    
    <xsl:template name="find-entry-uri">
        <xsl:value-of select="$base"/>
        <xsl:choose>
            <xsl:when test="@id = 'social_account'">
                <xsl:text>/</xsl:text>
                <var>&lt;person.name&gt;</var>
                <xsl:text>/+socialaccount/</xsl:text>
                <var>&lt;id&gt;</var>
            </xsl:when>
        </xsl:choose>
    </xsl:template>

The resulting URL will be: ``URL: https://api.launchpad.net/beta/<person.name>/+socialaccount/<id>``
