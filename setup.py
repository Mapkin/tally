#!/usr/bin/env python
"""
Tally
======

Tally is a simple daily counter API.
"""


from setuptools import setup, find_packages

import os
import subprocess


# If setup.py is being run from within the git repository (instead of a
# tarball, for instance) append the first 10 digits of the head commmit.
tally_version = "0.0.1"
if os.path.exists(".git"):
    commit = subprocess.check_output(["git", "rev-parse", "HEAD"])
    tally_version += "({0})".format(commit[:10])


install_requires = [
    'Django==1.4.1',
    'django-tastypie==0.9.11',
    'gevent==0.13.7',
    'gunicorn==0.14.6',
    'psycopg2==2.4.5',
    'py-bcrypt==0.2',
    'yajl==0.3.5',
    'South==0.7.6',
]

setup(
    name='Tally',
    version=tally_version,
    author='Mapkin',
    author_email='dev@mapkin.co',
    url='https://github.com/Mapkin/tally.git',
    description='A simple daily counter.',
    long_description=__doc__,
    packages=find_packages(),
    zip_safe=False,
    install_requires=install_requires,
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'tally = tally.manage:main',
        ],
    },
    classifiers=[
        'Framework :: Django',
        'Indended Audience :: Developers',
        'Indended Audience :: System Administrators',
        'Operating System :: Unix',
        'Topic :: Software Development'
    ],
)
