#
# Flask Skeleton
# Copyright (c) Ryan Kadwell <ryan@riaka.ca>
#
# setup wsgi application for site
#
# Author: Ryan Kadwell <ryan@riaka.ca>
#

import sys
import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))

# activate virtualenv
activate_this = os.path.join(BASEDIR, ".virtualenv/2.7/bin/activate_this.py")
execfile(activate_this, dict(__file__=activate_this))

if BASEDIR not in sys.path:
   sys.path.append(BASEDIR)

from skeleton import get_app

# set the wsgi application
application = get_app()
