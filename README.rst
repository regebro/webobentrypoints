===============================
WebOb Entry points
===============================

.. image:: https://badge.fury.io/py/webobentrypoints.png
    :target: http://badge.fury.io/py/webobentrypoints

.. image:: https://travis-ci.org/regebro/webobentrypoints.png?branch=master
        :target: https://travis-ci.org/regebro/webobentrypoints

.. image:: https://pypip.in/d/webobentrypoints/badge.png
        :target: https://pypi.python.org/pypi/webobentrypoints


**PasteDeploy entry points for WebOb WSGI apps**

* Free software: BSD license
* Documentation: https://webobentrypoints.readthedocs.org.

Features
--------

WebOb includes several WSGI apps that you can use as a part of your
application. However, it does not include ready to use entry points for usage
in PasteDeploy ini files, for usage with for example
[Gearbox](https://pypi.python.org/pypi/gearbox)

This module provides these entry points and the small wrappers needed.

The entry points provided are:

egg:webobentrypoints#staticdir


Example usage
-------------

Here is an example of a ini file configuration using the staticdir and the proxy apps::

    [server:main]
    use = egg:gearbox#wsgiref
    host = 0.0.0.0
    port = 5000

    [composite:main]
    use = egg:rutter#urlmap
    /static = static
    / = content

    # Serve the /static directory from local disk
    [app:static]
    use = egg:webobentrypoints#staticdir
    path = %(here)s/theme

    # Otherwise display http://webob.org/ as the content
    [app:content]
    use = egg:webobentrypoints#proxy
    address = http://webob.org/
    suppress_http_headers = accept-encoding connection
