# fyp-api

[![Build Status](https://travis-ci.org/FixYourPlants/fyp-api.svg?branch=master)](https://travis-ci.org/FixYourPlants/fyp-api)
[![Built with](https://img.shields.io/badge/Built_with-Cookiecutter_Django_Rest-F7B633.svg)](https://github.com/agconti/cookiecutter-django-rest)

API for the project Fix Yours Plants. Check out the project's [documentation](http://FixYourPlants.github.io/fyp-api/).

# Prerequisites

- [Docker](https://docs.docker.com/docker-for-mac/install/)

# Initialize the project

Start the dev server for local development:

```bash
docker-compose up
```

Create a superuser to login to the admin:

```bash
docker-compose run --rm web ./manage.py createsuperuser
```
