#!/usr/bin/env python
#
# Created by John Watson on 2012-10-10.
# Copyright (c) 2012 Eightyone Labs, Inc. All rights reserved.
#


from tally.conf.settings.development import *

import getpass
import urlparse


DEBUG = True

# Don't log to Sentry.
DISABLED_APPS = (
    'raven.contrib.django',
)

# Assumes all databases are running on the local machine, and are accessed
# as the current user.
DATABASE_PREFIX = ''
DATABASE_USER = getpass.getuser()
DATABASE_PASSWORD = ''
DATABASE_HOST = 'localhost'
DATABASE_PORT = None

for k, v in DATABASES.iteritems():
    DATABASES[k].update({
        'NAME': DATABASE_PREFIX + v['NAME'],
        'HOST': DATABASE_HOST,
        'PORT': DATABASE_PORT,
        'USER': DATABASE_USER,
        'PASSWORD': DATABASE_PASSWORD,
        'OPTIONS': {
            'autocommit': False
        }
    })

# django-devserver: http://github.com/dcramer/django-devserver
# This gives us a lot of nice debugging information.
try:
    import devserver
except ImportError:
    pass
else:
    INSTALLED_APPS = INSTALLED_APPS + (
        'devserver',
    )

    DEVSERVER_DEFAULT_ADDR = '0.0.0.0'
    DEVSERVER_DEFAULT_PORT = '8000'
    DEVSERVER_IGNORED_PREFIXES = ['/media', '/uploads']
    DEVSERVER_MODULES = (
        # SQLRealTimeModule can get a little noisy, so comment that out
        # if you want.
        'devserver.modules.sql.SQLRealTimeModule',
        'devserver.modules.sql.SQLSummaryModule',
        'devserver.modules.profile.ProfileSummaryModule',
        'devserver.modules.request.SessionInfoModule',
        'devserver.modules.profile.MemoryUseModule',
        'devserver.modules.profile.LeftOversModule',
        'devserver.modules.cache.CacheSummaryModule',
    )
