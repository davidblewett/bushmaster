#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
    # TODO: put package requirements here
    'pycurl',
    'requests',
    'requests-oauthlib',
    'tornado',
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='bushmaster',
    version='0.1.0',
    description="Efficient interface to Amazon Cloud Drive",
    long_description=readme + '\n\n' + history,
    author="David Blewett",
    author_email='david@dawninglight.net',
    url='https://github.com/davidblewett/bushmaster',
    packages=[
        'bushmaster',
    ],
    package_dir={'bushmaster':
                 'bushmaster'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='bushmaster',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
