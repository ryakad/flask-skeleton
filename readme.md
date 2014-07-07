Flask Skeleton
==============

Here is my flask skeleton application. I have set this application in the
way that I find easiest, and least cumbersome, to work with. If you have any
ideas on how it could be better let me know!


Installation
------------

Instalation is simple. I use a makefile for installing all required dependencies
and compiling all required assets. If you have npm and virtualenv on your path
you can set everythin up with a simple `make`. This basically sets up virtual
environments in `.virtualenv/2.7` and `.virtualenv/3.3` and installs all
required python dependencies and then installs frontend and development
dependencies from node and bower. If you want more details as to exactly what
is going on have a look at the `makefile`.

Once the makefile is done you will want to check the defaults set in your
`config.yml` file.

To run the development server you can then use: `python bin/manage.py runserver`.
I have also setup a dev target in the uwsgi.ini. If you want to test running
with that that you can use the command `uwsgi --ini uwsgi.ini:dev`.


Conventions
-----------

### configuration

I prefer using yml files for my config and so have extended the default flask
config object to make this possible. As mentioned above I use a file named
`config.yml` to store all configurations. The config.yml is ignored by git
and so we use a config.dist.yml to distribute the changes. This allows us to
keep our secret and machine specific configurations only on that machine in
the `config.yml` and then set sensible default in the `config.dist.yml`.

Another change to the config handline made is how values are accessed in the
application. I prefer using a dot notation rather than accessing by keys in
dictionary. This is more just a personal preference but I find it looks much
cleaner. I have also set the ability to use a default value should the config
not have a value specified. Values are accessed through a `get` method on the
config object. To see a quick example have a look at the following config file:

```yml
database:
   host: localhost
```

To access the host for the database we will use dots to seperate the different
levels of nesting so the host becomes the value stored at `database.host`. If
`database.host` is not defined we can use `localhost` by default with the
following code:

```python
from flask import current_app
host = current_app.config.get('database.host', 'SOME DEFAULT')
```

This will set the variable host to localhost. If database.host is not defined
it will be set to "SOME DEFAULT". IF the default is not set it will be set to
`None`.

### scripts

Raw JavaScript and Less files are stored in the `scripts` directory. This
makes it simple for us to compile them into the web root; minifying them in
the process. Less is compiled with `lessc` and JavaScript with the
`yuicompressor`. Both of these commands are installed using `npm` during the
initial `make`. Compiled files are stored in `skeleton/static/c` denoting
that they are compiled. Files in this directory are ignored in the `.gitignore`
so you are only distributing the raw source.

To simplify the compiling of these scripts I use the `makefile` to define what
needs to be compiled. I then use `bin/watch.sh` to monitor the filesystem for
changes and compile these files automatically while I am developing. The
command for this is:

```sh
./bin/manage.py scripts make scripts
```

> For more information on any part of this project please see the source code
> that was distributed with this readme file.

License
-------

This project is licensed under the MIT license located in the file
`license.txt` that was distributed with this source.
