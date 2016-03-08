#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


setup(
    name='pytest-timebox',
    version='0.1.0',
    author='Andrei Coman',
    author_email='comandrei@gmail.com',
    maintainer='Andrei Coman',
    maintainer_email='comandrei@gmail.com',
    license='BSD-3',
    url='https://github.com/comandrei/pytest-timebox',
    description='py.test plugin to timebox your test suite',
    long_description=read('README.rst'),
    py_modules=['pytest_timebox'],
    install_requires=['pytest>=2.8.1'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
    ],
    entry_points={
        'pytest11': [
            'timebox = pytest_timebox',
        ],
    },
)
