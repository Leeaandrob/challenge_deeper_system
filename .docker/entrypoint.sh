#!/bin/sh
mv .env.docker project
cd /repo && cd project && python manage.py makemigrations
cd /repo && cd project && python manage.py migrate
exec "$@"
