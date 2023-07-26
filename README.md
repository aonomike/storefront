# STOREFRONT

Storefront is an online shop that enables buyers to:

    - View products available for purchase
    - Add items to a cart
    - Submit order items

This repo is meant for a demonstration of understanding in django api development and testing. It implements the api for accessing the resources of the online shop

# Requirements

- Python 3.10 is recommended
- Postgress SQL database (You can use MySQL, Oracle, MSSQL Server or Oracle as long as you set it up in your settings file)

You can either run this application using docker or on bear metal setup. Follow the guides below to get set up

## Getting started

- Clone/Fork and clone this repo into your working environment

```
git clone git@github.com:aonomike/storefront.git storefront
```

- Get setup with your virtual environment, please follow [this link to get set up with pipenv](https://pipenv.pypa.io/en/latest/) (Recommended) or [this link](https://www.geeksforgeeks.org/python-virtual-environment/) to get set up with your virtual env

- Change directory into the storefront directory

```
$> cd storefront
```

- Activate the virtual environment

```
$> pipenv shell
```

- Install the dependencies

```
$> pipenv install
```

- Create your `.env` file and ensure you have the following variables added. You could copy from the `.env.example` already provided in the repo

```
$> cp .env.example .env
```

The variables to be updated are as  listed below

```
SECRET_KEY=your_django_secret_key
POSTGRES_DB_USER=your_db_user
POSTGRES_DB_PASSWORD=your_db_password
POSTGRES_DB_HOST=your_db_host
POSTGRES_DB_PORT=your_db_port
```

- Run migrations

```
$> python manage.py migrate
```

- Run the application by running the command below

```
$> python manage.py runserver
```

## Using Docker and Docker compose

To be updated as soon as docker is set up

## Running unit tests

Tests in the are written using the PyTest library. To run the tests, run tthe command below

```
$> pytest
```
