#
# Flask Skeleton
# Copyright (c) Ryan Kadwell <ryan@riaka.ca>
#
# Custom config class to allow different value access methods and to load
# from a yml file
#
# Author: Ryan Kadwell <ryan@riaka.ca>
#

import os
import yaml
from flask import Config

class SkeletonConfig(Config):

   def from_yaml(self, filename):
      """Reads the given yml file and imports all values"""
      if not os.path.exists(filename):
         raise Exception('Config file \"{}\" does not exist'.format(filename))

      with open(filename) as f:
         ymlconf = yaml.load(f)

      ymlconf = upper_keys(ymlconf)
      for key in ymlconf:
         self[key] = ymlconf[key]

   def get(self, value_name, default=None):
      """Access config values using a dot notation.

      This method takes the name of a config value in dot notation::

         app.config.get('db.host', 'localhost')

      would return the value of app.config['DB']['HOST'] if it exists otherwise
      it will return the string 'localhost'.
      """
      data = self
      # need to oppercase the value name since config values are stored in
      # uppercase
      for key in value_name.upper().split("."):
         if key in data:
            data = data[key]
         else:
            return default

      return data

def upper_keys(x):
   if isinstance(x, list):
      return [upper_keys(v) for v in x]
   if isinstance(x, dict):
      return dict((k.upper(), upper_keys(v)) for k, v in x.iteritems())
   return x
