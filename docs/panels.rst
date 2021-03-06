Panels
======

The Django Debug Toolbar ships with a series of built-in panels. In addition,
several third-party panels are available.

Default built-in panels
-----------------------

The following panels are enabled by default.

Version
~~~~~~~

Path: ``debug_toolbar.panels.versions.VersionsPanel``

Shows versions of Python, Django, and installed apps if possible.

Timer
~~~~~

Path: ``debug_toolbar.panels.timer.TimerPanel``

Request timer.

Settings
~~~~~~~~

Path: ``debug_toolbar.panels.settings.SettingsPanel``

A list of settings in settings.py.

Headers
~~~~~~~

Path: ``debug_toolbar.panels.headers.HeadersPanel``

This panels shows the HTTP request and response headers, as well as a
selection of values from the WSGI environment.

Note that headers set by middleware placed before the debug toolbar middleware
in ``MIDDLEWARE_CLASSES`` won't be visible in the panel. The WSGI server
itself may also add response headers such as ``Date`` and ``Server``.

Request
~~~~~~~

Path: ``debug_toolbar.panels.request.RequestPanel``

GET/POST/cookie/session variable display.

SQL
~~~

Path: ``debug_toolbar.panels.sql.SQLPanel``

SQL queries including time to execute and links to EXPLAIN each query.

Template
~~~~~~~~

Path: ``debug_toolbar.panels.templates.TemplatesPanel``

Templates and context used, and their template paths.

Static files
~~~~~~~~~~~~

Path: ``debug_toolbar.panels.staticfiles.StaticFilesPanel``

Used static files and their locations (via the staticfiles finders).

Cache
~~~~~

Path: ``debug_toolbar.panels.cache.CachePanel``

Cache queries.

Signal
~~~~~~

Path: ``debug_toolbar.panels.signals.SignalsPanel``

List of signals, their args and receivers.

Logging
~~~~~~~

Path: ``debug_toolbar.panels.logging.LoggingPanel``

Logging output via Python's built-in :mod:`logging` module.

Redirects
~~~~~~~~~

Path: ``debug_toolbar.panels.redirects.RedirectsPanel``

When this panel is enabled, the debug toolbar will show an intermediate page
upon redirect so you can view any debug information prior to redirecting. This
page will provide a link to the redirect destination you can follow when
ready.

Since this behavior is annoying when you aren't debugging a redirect, this
panel is included but inactive by default. You can activate it by default with
the ``INTERCEPT_REDIRECTS`` configuration option.


Non-default built-in panels
---------------------------

The following panels are disabled by default. You must add them to the
``DEBUG_TOOLBAR_PANELS`` setting to enable them.

Profiling
~~~~~~~~~

Path: ``debug_toolbar.panels.profiling.ProfilingPanel``

Profiling information for the view function.

Third-party panels
------------------

.. note:: Third-party panels aren't officially supported!

    The authors of the Django Debug Toolbar maintain a list of third-party
    panels, but they can't vouch for the quality of each of them. Please
    report bugs to their authors.

If you'd like to add a panel to this list, please submit a pull request!

Haystack
~~~~~~~~

URL: https://github.com/streeter/django-haystack-panel

Path: ``haystack_panel.panel.HaystackDebugPanel``

See queries made by your Haystack_ backends.

.. _Haystack: http://haystacksearch.org/

HTML Tidy/Validator
~~~~~~~~~~~~~~~~~~~

URL: https://github.com/joymax/django-dtpanel-htmltidy

Path: ``debug_toolbar_htmltidy.panels.HTMLTidyDebugPanel``

HTML Tidy or HTML Validator is a custom panel that validates your HTML and
displays warnings and errors.

Inspector
~~~~~~~~~

URL: https://github.com/santiagobasulto/debug-inspector-panel

Path: ``inspector_panel.panels.inspector.InspectorPanel``

Retrieves and displays information you specify using the ``debug`` statement.
Inspector panel also logs to the console by default, but may be instructed not
to.

Line Profiler
~~~~~~~~~~~~~

URL: https://github.com/dmclain/django-debug-toolbar-line-profiler

Path: ``debug_toolbar_line_profiler.panel.ProfilingPanel``

This package provides a profiling panel that incorporates output from
line_profiler_.

.. _line_profiler: http://pythonhosted.org/line_profiler/

Memcache
~~~~~~~~

URL: https://github.com/ross/memcache-debug-panel

Path: ``memcache_toolbar.panels.memcache.MemcachePanel`` or ``memcache_toolbar.panels.pylibmc.PylibmcPanel``

This panel tracks memcached usage. It currently supports both the pylibmc and
memcache libraries.

MongoDB
~~~~~~~

URL: https://github.com/hmarr/django-debug-toolbar-mongo

Path: ``debug_toolbar_mongo.panel.MongoDebugPanel``

Adds MongoDB debugging information.

Neo4j
~~~~~

URL: https://github.com/robinedwards/django-debug-toolbar-neo4j-panel

Path: ``neo4j_panel.Neo4jPanel``

Trace neo4j rest API calls in your django application, this also works for neo4django and neo4jrestclient, support for py2neo is on its way.

Sites
~~~~~

URL: https://github.com/elvard/django-sites-toolbar

Path: ``sites_toolbar.panels.SitesDebugPanel``

Browse Sites registered in ``django.contrib.sites`` and switch between them.
Useful to debug project when you use `django-dynamicsites
<https://bitbucket.org/uysrc/django-dynamicsites/src>`_ which sets SITE_ID
dynamically.

Template Timings
~~~~~~~~~~~~~~~~

URL: https://github.com/orf/django-debug-toolbar-template-timings

Path: ``template_timings_panel.panels.TemplateTimings.TemplateTimings``

Displays template rendering times for your Django application.

User
~~~~

URL: https://github.com/playfire/django-debug-toolbar-user-panel

Path: ``debug_toolbar_user_panel.panels.UserPanel``

Easily switch between logged in users, see properties of current user.

API for third-party panels
--------------------------

Third-party panels must subclass :class:`~debug_toolbar.panels.Panel`,
according to the public API described below. Unless noted otherwise, all
methods are optional.

Panels can ship their own templates, static files and views. They're no public
CSS or JavaScript API at this time, but they can assume jQuery is available.

.. autoclass:: debug_toolbar.panels.Panel(*args, **kwargs)

    .. autoattribute:: debug_toolbar.panels.Panel.nav_title

    .. autoattribute:: debug_toolbar.panels.Panel.nav_subtitle

    .. autoattribute:: debug_toolbar.panels.Panel.has_content

    .. autoattribute:: debug_toolbar.panels.Panel.title

    .. autoattribute:: debug_toolbar.panels.Panel.template

    .. autoattribute:: debug_toolbar.panels.Panel.content

    .. automethod:: debug_toolbar.panels.Panel.get_urls

    .. automethod:: debug_toolbar.panels.Panel.enable_instrumentation

    .. automethod:: debug_toolbar.panels.Panel.disable_instrumentation

    .. automethod:: debug_toolbar.panels.Panel.record_stats

    .. automethod:: debug_toolbar.panels.Panel.get_stats

    .. automethod:: debug_toolbar.panels.Panel.process_request

    .. automethod:: debug_toolbar.panels.Panel.process_view

    .. automethod:: debug_toolbar.panels.Panel.process_response
