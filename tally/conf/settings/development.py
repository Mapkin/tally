#!/usr/bin/env python
#
# Created by John Watson on 2012-10-10.
# Copyright (c) 2012 Eightyone Labs, Inc. All rights reserved.
#


from tally.conf.settings.default import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'tally',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}
