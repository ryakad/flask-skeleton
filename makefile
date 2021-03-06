#
# Flask Skeleton
# Copyright (c) Ryan Kadwell <ryan@riaka.ca>
#
# Make file for compiling and configuring parts of the application
#
# Author: Ryan Kadwell <ryan@riaka.ca>
#

# THe name of the module that our app is contained in
modulename = skeleton

# Find the path to the python binaries that we are using.
python33 = `which python3.3`
python27 = `which python2.7`


.PHONY: js css scripts pip

all: pip scripts config.yml

config.yml:
	cp config.dist.yml config.yml

.virtualenv/2.7:
	virtualenv --python=$(python27) .virtualenv/2.7
.virtualenv/3.3:
	virtualenv --python=$(python33) .virtualenv/3.3

.virtualenv: .virtualenv/2.7 .virtualenv/3.3

pip: .virtualenv
	# Install all python dependencies into both environments
	.virtualenv/2.7/bin/pip install -r requirements.txt
	.virtualenv/3.3/bin/pip install -r requirements.txt

node:
	npm install

bower: node
	./node_modules/.bin/bower install

scripts: css js

css: node bower
	if ! [ -d $(modulename)/static/c/css ]; then mkdir -p $(modulename)/static/c/css; fi
	./node_modules/.bin/lessc --compress scripts/less/init.less $(modulename)/static/c/css/skeleton.css

js: node bower
	if ! [ -d $(modulename)/static/c/js ]; then mkdir -p $(modulename)/static/c/js; fi
	# For unminified script files you should compress them using the yuicompressor:
	# ./node_modules/.bin/yuicompressor [SOURCE_FILE] > $(modulename)/static/c/js/[DESTINATION_FILE]
	cp bower_components/jquery/dist/jquery.min.js $(modulename)/static/c/js/jquery.min.js
	cp bower_components/jquery/dist/jquery.min.map $(modulename)/static/c/js/jquery.min.map
	./node_modules/.bin/yuicompressor bower_components/underscore/underscore.js > $(modulename)/static/c/js/underscore.js
	./node_modules/.bin/yuicompressor scripts/js/skeleton.js > $(modulename)/static/c/js/skeleton.js

clean:
	rm -Rf node_modules
	rm -Rf bower_components
	rm -Rf skeleton/static/c
	rm -Rf .virtualenv
	echo "WARNING: not removing config.yml! You can do this yourself if you want a full clean."
