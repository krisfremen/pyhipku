#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

import hipku


try:
    import pypandoc
    long_description = pypandoc.convert('README.md','rst')
except (IOError, ImportError):
    with open('README.md') as f:
        long_description = f.read()


setup(
    name='hipku',
    version=hipku.__version__,
    url='http://github.com/lord63/hipku.py/',
    license='MIT',
    author='lord63',
    author_email='lord63.j@gmail.com',
    description='Encode any IP address as a haiku',
    long_description=long_description,
    packages=['hipku'],
    include_package_data=True,
    keywords='ip haiku',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)