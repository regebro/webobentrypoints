#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import os

from paste.deploy import appconfig, loadwsgi

class TestWebobentrypoints(unittest.TestCase):

    def test_staticdir(self):
        conf = loadwsgi.appconfig('egg:webobentrypoints#staticdir')
        res = conf.context.object(conf.global_conf,
                                  path=os.path.dirname(__file__),
                                  index_page='index.html',
                                  hide_index_with_redirect=False)


    def test_proxy(self):
        conf = loadwsgi.appconfig('egg:webobentrypoints#proxy')
        res = conf.context.object(conf.global_conf,
                                  address='http://webob.org/',
                                  suppress_http_headers=None)

if __name__ == '__main__':
    unittest.main()
