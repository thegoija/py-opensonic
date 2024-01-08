#!/usr/bin/env python3

"""
This file is part of py-opensonic.

py-sonic is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

py-opensonic is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with py-opensonic.  If not, see <http://www.gnu.org/licenses/>
"""

import os
from setuptools import setup,find_packages

req_file = os.path.join(os.path.dirname(__file__), 'requirements.txt')
with open(req_file, encoding="utf-8") as file:
    requirements = [line for line in file if line]

setup(name='py-opensonic',
    version='1.0.0',
    author='Eric B. Munson',
    author_email='eric@munsonfam.org',
    url='https://github.com/khers/py-opensonic',
    description='A python wrapper library for the Open Subsonic REST API.  '
        'https://opensubsonic.netlify.app/',
    long_description='This is a basic wrapper library for the Open Subsonic '
        'REST API. This will allow you to connect to your server and retrieve '
        'information and have it returned in basic Python types.',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    install_requires=requirements,
    python_requires='>=3',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: System :: Systems Administration',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries',
        'Topic :: System',
    ]
)
