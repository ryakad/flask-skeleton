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

> NOTE: The config.yml file is ignored by git by default so that you can keep
> your secrets secret. When making changes to it you should consider whether
> those changes should also be made in the config.yml.dist which IS commited
> by git.

To run the development server you can then use: `python bin/manage.py runserver`.
I have also setup a dev target in the uwsgi.ini incase you want to test running
with that that you can run with `uwsgi --ini uwsgi.ini:dev`.
