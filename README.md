Tally - A Simple Daily Counter
==============================

Tally is used to count things. The count resets every day. This is useful
if you consume an API with a daily rate limit, and they don't give you any
way to check it.

Installation
------------

First, create a virtualenv and install the package.

    $ virtualenv --distribute /www/tally
    $ source /www/tally/bin/activate
    $ git clone git@github.com:Mapkin/tally.git
    $ cd tally
    $ pip install -e .

Migrate the database, and make sure you add a superuser for the admin
interface.

    $ tally syncdb --migrate

If you're running Ubuntu, you can set Tally up as an Upstart service.

    $ vim extra/tally.conf
    $ sudo cp extra/tally.conf /etc/init
    $ sudo ln -s /lib/init/upstart-job /etc/init.d/tally
    $ sudo service tally start

Setup
-----

The Django admin interface is used to create API clients and counters.

API
---

Tally uses basic access authentication over SSL. Pass your API key as the
`username` field, and leave the `password` field blank.

To increment a counter:

    $ curl -X PATCH \
           -u 8ZrTSskX1UPHqUJeqXwN: \
           https://tally.example.com/api/v1/counters/TestCounter

To read a counter:

    $ curl -X GET \
           -u 8ZrTSskX1UPHqUJeqXwN: \
           https://tally.example.com/api/v1/counters/TestCounter
