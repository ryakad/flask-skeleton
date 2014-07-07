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
from flask import Flask, render_template
from .frontend import frontend
from .config import SkeletonConfig

__all__ = ["get_app"]

DEFAULT_BLUEPRINTS = [
   frontend
]

MODULE_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.abspath(MODULE_DIR + "/..")

# Overwrite the Flask application to set the default config object to our
# skeleton config
class SkeletonFlask(Flask):
   def make_config(self, instance_relative=False):
      root_path = self.root_path
      if instance_relative:
         root_path = self.instance_path

      return SkeletonConfig(root_path, self.default_config)


def create_app(config=None, app_name=None, blueprints=None):
   """Returns a flask application"""
   app = SkeletonFlask(__name__)

   if blueprints is None:
      blueprints = DEFAULT_BLUEPRINTS

   # Load config first as we may need access to config values in later setup
   # steps
   app.config.from_yaml(os.path.join(BASE_DIR, "config.yml"))

   load_error_handlers(app)
   load_blueprints(app, blueprints)

   return app

def load_blueprints(app, blueprints):
   """Register an array of blueprints with the provided application"""
   for blueprint in blueprints:
      app.register_blueprint(blueprint)

def load_error_handlers(app):
   """Setup any custom error handlers."""

   @app.errorhandler(404)
   def error_handler(e):
      return render_template('error/404.html'), 404

   @app.errorhandler(500)
   def error_handler(e):
      return render_template('error/500.html'), 500
