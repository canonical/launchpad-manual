Running Launchpad with Chameleon Template Engine
================================================

.. include:: ../includes/important_out_of_date.rst

- Uncomment ``<include package="z3c.ptcompat" />`` in ``zcml/zopeapp.zcml``
  to enable ``z3c.pt``.


Useful environment options for ``z3c.pt``::

  # in debug-mode, templates on disk are reloaded if they're modified
  CHAMELEON_DEBUG (default: false)

  # disable disk-cache to prevent the compiler from caching on disk
  CHAMELEON_CACHE (default: true)

  # if eager parsing is enabled, templates are parsed upon
  # instantiation, rather than when first called upon; this mode is
  # useful for verifying validity of templates across a project
  CHAMELEON_EAGER (default: false)

  # in strict mode, filled macro slots must exist in the macro that's
  # being used.
  CHAMELEON_STRICT (default: false)

  # when validation is enabled, dynamically inserted content is
  # validated against the XHTML standard
  CHAMELEON_VALIDATE (default: false)
