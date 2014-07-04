#
# Flask Skeleton
# Copyright (c) Ryan Kadwell <ryan@riaka.ca>
#
# Controllers for the frontend application
#
# Author: Ryan Kadwell <ryan@riaka.ca>
#

from flask import Blueprint, render_template

frontend = Blueprint('frontend', __name__, template_folder="templates")

@frontend.route('/')
def homepage_route():
   """Display the homepage"""
   return render_template('index.html')
