# D-PackageBackend

[![Build Status](https://travis-ci.com/ebar0n/D-PackageBackend.svg?token=DY8zmJsbUNWWXjfwiUs8&branch=master)](https://travis-ci.com/ebar0n/D-PackageBackend)

## Requirements

### Install and configure Docker

1. Install docker. [Docker](https://docker.github.io/engine/installation/)

1. Intall docker-compose. [Compose](https://docs.docker.com/compose/install/)

### Set Var Environment

1. Copy to `env.example` into `.env`

        cp env.example .env

1. Edit values in `.env`

        nano .env

1. Config domain

        echo "127.0.0.1 dev.api.d-packagebackend.com" | sudo tee -a /etc/hosts > /dev/null

## BackEnd

1. Start container DB

        docker-compose up -d postgres

1. Apply migrations

        docker-compose run --rm api python manage.py migrate

1. Run Django Project

        docker-compose up -d

1. Open API on browser in Dev

* [dev.api.d-packagebackend.com:8000](http://dev.api.d-packagebackend.com:8000)

### Django Admin

1. Create superuser (Execute command and follow the steps)

        docker-compose run --rm api python manage.py createsuperuser

1. Access to django admin [dev.api.d-packagebackend.com:8000/admin/](http://dev.api.d-packagebackend.com:8000/admin/)

### Run tests to code

1. Exit instantly on first error or failed test

        docker-compose run --rm -e TEST=true api py.test -x

1. Activate the Python Debugger

        docker-compose run --rm -e TEST=true api py.test --pdb

1. Run all the tests

        docker-compose run --rm -e TEST=true api py.test

### Run tests to style

1. Run tests isort

        docker-compose run --rm api isort

### Django Internationalization

1. Execute this command to runs over the entire source tree of the current directory and pulls out all strings marked for translation.

        docker-compose run --rm api python manage.py makemessages --no-location -l es

1. Edit file public/locale/es/LC_MESSAGES/django.po and add a translation.

        msgid "Hello world"
        msgstr "Hola mundo"

1. Compiles .po files to .mo files for use with builtin gettext support.

        docker-compose run --rm api python manage.py compilemessages

### Run the project for Production

1. Build

        docker-compose -f docker-compose-production.yml build

1. Initialize

        docker-compose -f docker-compose-production.yml up -d postgres
        docker-compose -f docker-compose-production.yml run --rm api python manage.py migrate --noinput
        docker-compose -f docker-compose-production.yml run --rm api python manage.py collectstatic --noinput
        docker-compose -f docker-compose-production.yml run --rm api python manage.py compilemessages

1. Run Django server

        docker-compose -f docker-compose-production.yml up -d

1. Visit API [api.d-packagebackend.edwarbaron.me/](http://api.d-packagebackend.edwarbaron.me/)

### Automatic deploy using `fabric`

1. On Linux

        pip install fabric
        ~/.local/bin/fab deploy_dev

1. On macOS

        pip install --user fabric
        ~/Library/Python/2.7/bin/fab deploy_dev

1. Other taks

    1. fab test
