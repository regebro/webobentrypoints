# -*- coding: utf-8 -*-
from webob.client import SendRequest
from webob.static import DirectoryApp

try:
    from urlparse import urlparse
except ImportError:
    from urllib.parse import urlparse

def make_staticdir(global_conf, path, index_page='index.html',
                   hide_index_with_redirect=False):
    """
    Return a WSGI application that serves a directory (configured
    with path)
    """
    return DirectoryApp(path=path, index_page='index.html',
                        hide_index_with_redirect=False)


class Proxy(object):
    """
    Make a WSGI application that proxies to another address:

    ``address``
        the full URL ending with a trailing ``/``
    """

    def __init__(self, global_conf, address, suppress_http_headers=None):

        parts = urlparse(address)
        self.scheme = parts[0]
        if ':' in parts[1]:
            self.server, self.port = parts[1].split(':')
        else:
            self.server, self.port = parts[1], 80

        filtered_headers = SendRequest.filtered_headers
        if suppress_http_headers is not None:
            filtered_headers += tuple(suppress_http_headers.split())

        self.proxy = SendRequest()
        self.proxy.filtered_headers = filtered_headers

    def __call__(self, environ, start_response):
        environ['wsgi.url_scheme'] = self.scheme
        environ['HTTP_HOST'] = self.server
        environ['SERVER_NAME'] = self.server
        environ['SERVER_PORT'] = self.port
        return self.proxy(environ, start_response)

