django-encrypted-json
=====================

Some simple encrypted JSON fields for use with Django.

Test status: [![Circle CI](https://circleci.com/gh/LucasRoesler/django-encrypted-json.svg?style=svg)](https://circleci.com/gh/LucasRoesler/django-encrypted-json)

## Requirements

**Minimum Versions:**
* Python 3.10+
* Django 5.2+
* PostgreSQL 14+

**Dependencies:**
* cryptography
* django-pgjson
* psycopg2-binary

### System Requirements

On Ubuntu you need to install `libffi-dev` and `libpq-dev`:

    $ sudo apt-get install libffi-dev libpq-dev

## Installation

    $ pip install -r requirements.txt

## Testing

The test requirements are found in `requirements.txt`

    $ pip install -r requirements.txt

### Run tests locally:

    $ cd tests
    $ python manage.py test test_app

Or use the test script:

    $ ./runtests.sh

### Run tests with Docker:

    $ docker-compose up --abort-on-container-exit

## Upgrade Notes

**Upgraded to Django 5.2.10 and Python 3.10** - See [UPGRADE_GUIDE.md](UPGRADE_GUIDE.md) for complete details.

### Key Changes:
- ✅ Removed Python 2 compatibility (six library)
- ✅ Updated to Django 5.2 APIs
- ✅ Modernized migrations to use BigAutoField
- ✅ Added Docker support (Python 3.10 + PostgreSQL 14)
