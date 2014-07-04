#
# Flask Skeleton
# Copyright (c) Ryan Kadwell <ryan@riaka.ca>
#
# Configuration for the flask application
#
# Author: Ryan Kadwell <ryan@riaka.ca>
#

import os
import sys
from flask import Flask
from .frontend import frontend

__all__ = ["get_app"]

DEFAULT_BLUEPRINTS = [
   frontend
]


def get_app(config=None, app_name=None, blueprints=None):
   """Returns a flask application"""
   app = Flask(__name__)

   if blueprints is None:
      blueprints = DEFAULT_BLUEPRINTS

   app.config['DEBUG'] = True
   app.config['STATIC_FOLDER'] = '/static'

   load_blueprints(app, blueprints)

   return app

def load_blueprints(app, blueprints):
   """Register an array of blueprints with the provided application"""
   for blueprint in blueprints:
      app.register_blueprint(blueprint)
