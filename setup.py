#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='webobentrypoints',
    version='0.2.0.dev0',
    description='PasteDeploy entry points for WebOb WSGI apps and filters.',
    long_description=readme + '\n\n' + history,
    author='Lennart Regebro',
    author_email='regebro@gmail.com',
    url='https://github.com/regebro/webobentrypoints',
    packages=[
        'webobentrypoints',
    ],
    package_dir={'webobentrypoints':
                 'webobentrypoints'},
    include_package_data=True,
    install_requires=[
        'WebOb',
        'PasteDeploy',
        ],
    license="BSD",
    zip_safe=False,
    keywords='webobentrypoints',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=[
        'gearbox',
    ],
    entry_points = """
        [paste.app_factory]
        staticdir = webobentrypoints:make_staticdir
        proxy = webobentrypoints:Proxy
        """,
)
