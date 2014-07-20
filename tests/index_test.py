#
# Flask Skeleton
# Copyright (c) Ryan Kadwell <ryan@riaka.ca>
#
# Test case for flask
#
# Author: Ryan Kadwell <ryan@riaka.ca>
#

from skeleton.test import SkeletonTestCase

class IndexTestCase(SkeletonTestCase):

   def test_is_true(self):
      """Assert that the main page contains the heading Awesome!"""
      response = self.client.get('/')
      assert '<h1>Awesome!</h1>' in response.data

