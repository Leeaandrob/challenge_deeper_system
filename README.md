# Youtube Theme Trends 
A project to analyze trends of theme.

## Prerequisites

* Django >= 2.0.3
* Docker installed [instructions](https://github.com/Leeaandrob/challenge_deeper_system.git/blob/master/DOCKER.md).

## Installing

    $ git clone https://github.com/Leeaandrob/challenge_deeper_system.git
    $ cd project

## Testing
First you need to install the depedencies

    $ pip install dev-requirements.txt

To run unit tests without docker:

    $ python manage.py test 

For run specific tests:

    $ python manage.py test **application_name**


## Development
It project has been made using a Macbook Pro 2013 computer, OS X operating system, Vim editor

**To start the application you can write down this.**

    $ docker-compose up

The application can be visited at `http://localhost:8000`

Entering on shell of django:

    $ docker exec -it youtube_theme_trends /bin/bash
    $ python manage.py shell

Creating super user:

    $ docker exec -it youtube_theme_trends /bin/bash
    $ python manage.py createsuperuser

### Using pdb
Its possible to use the pdb follow this intructions:

    $ docker ps
    $ docker attach <container_id>

## Deploy

We are using heroku:

    $ git add .
    $ git commit -m "message"
    $ heroku create {{ project_name }}
    $ heroku config:set SECRET_KEY='{{ secret_key }}'
    $ heroku config:set DEBUG=False
    $ heroku config:set FORCE_SSL=False
    $ heroku config:set RAVEN_URL={{ SENTRY DSN URL }}
    $ heroku config:set ROOT_HANDLER='stderr'
    $ heroku config:set ALLOWED_HOSTS=*
    $ heroku git:remote --app {{ project_name }}
    $ heroku config:add DISABLE_COLLECTSTATIC=0
    $ git push heroku master
    $ heroku run python manage.py migrate
    $ heroku run python manage.py createsuperuser
