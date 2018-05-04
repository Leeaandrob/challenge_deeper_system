#!/bin/sh
cp .env.docker project/.env.docker
cd /repo && cd project && python manage.py makemigrations
cd /repo && cd project && python manage.py migrate
exec "$@"
