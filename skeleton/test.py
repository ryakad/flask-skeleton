#
# Flask Skeleton
# Copyright (c) Ryan Kadwell <ryan@riaka.ca>
#
# Test case for flask
#
# Author: Ryan Kadwell <ryan@riaka.ca>
#

import unittest
from .app import create_app

class SkeletonTestCase(unittest.TestCase):

   def setUp(self):
      self.app = create_app(config="config_test.yml")
      self.client = self.app.test_client()
