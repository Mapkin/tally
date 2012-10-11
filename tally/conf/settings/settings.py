# Created by John Watson on 2012-10-10.
# Copyright (c) 2012 Eightyone Labs, Inc. All rights reserved.
#
# Django settings for tally.
# Shamelessly stolen from http://justcramer.com/2011/01/13/settings-in-django/
#

import os

# Import our global defaults.
from tally.conf.settings.default import *


# Inherit from environment specific config.
DJANGO_CONF = os.environ.get('DJANGO_CONF', 'default')
if DJANGO_CONF != 'default':
    module = __import__(DJANGO_CONF, globals(), locals(), ['*'])
    for k in dir(module):
        locals()[k] = getattr(module, k)

# Import local settings
try:
    from local_settings import *
except ImportError:
    import sys, traceback
    sys.stderr.write("Warning: Can't find the file 'local_settings.py' "
                     "in the directory containing %r." % __file__)
    sys.stderr.write("\nFor debugging purposes, the exception was:\n\n")
    traceback.print_exc()

# Remove disabled apps.
if 'DISABLED_APPS' in locals():
    INSTALLED_APPS = [k for k in INSTALLED_APPS if k not in DISABLED_APPS]

    MIDDLEWARE_CLASSES = list(MIDDLEWARE_CLASSES)

    for a in DISABLED_APPS:
        for x, m in enumerate(MIDDLEWARE_CLASSES):
            if m.startswith(a):
                MIDDLEWARE_CLASSES.pop(x)
