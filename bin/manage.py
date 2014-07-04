#! /usr/bin/env python
#
# Flask Skeleton
# Copyright (c) Ryan Kadwell <ryan@riaka.ca>
#
#
#
# Author: Ryan Kadwell <ryan@riaka.ca>
#

import os
import sys
from flask.ext.script import Manager

dirname = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.realpath(dirname + "/.."))

from skeleton import get_app

manager = Manager(get_app())

@manager.command
def hello():
   print "Hey there!"

if __name__ == "__main__":
   manager.run()
