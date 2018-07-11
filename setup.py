#!/usr/bin/env python3

import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='nationstates',
    version='0.0.1',
    author='Aran',
    author_email='aran@ermarian.net',
    description='A NationStates API client.',
    install_requires=['urllib3'],
    long_description='''
This client accesses the [NationStates](https://www.nationstates.net/) API to download
information about nations or regions. It has a simple command-line interface, but its full
set of features is used by importing it in Python.
''',
    url='https://github.com/arancaytar/nationstates',
    packages=setuptools.find_packages(),
    classifiers=(
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ),
    scripts=['bin/nationstates']
)