#!/bin/sh

./manage.py sqlclear gtdb taggit contenttypes | ./manage.py dbshell
./manage.py syncdb
./manage.py importhp
./manage.py rebuild_index --noinput
./manage.py runserver
