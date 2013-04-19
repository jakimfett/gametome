#!/bin/sh

./manage.py sqlclear gtdb taggit contenttypes auth | ./manage.py dbshell
./manage.py syncdb --noinput
./manage.py importhp
./manage.py rebuild_index --noinput
./manage.py runserver
