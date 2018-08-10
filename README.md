# MemCachier and Flask on Heroku tutorial

This is an example Flask task list app that uses
the [MemCachier add-on](https://addons.heroku.com/memcachier) on
[Heroku](http://www.heroku.com/). A running version of this app can be
found [here](http://memcachier-examples-flask.herokuapp.com).

Detailed instructions for developing this app are available
[here](https://devcenter.heroku.com/articles/flask-memcache).

## Deploy to Heroku

You can deploy this app yourself to Heroku to play with.

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

## Running Locally

Run the following commands to get started running this app locally:

```sh
$ git clone https://github.com/memcachier/examples-flask.git
$ cd examples-flask
$ mkdir instance
$ python -m venv venv
$ source venv/bin/activate
(venv) $ pip install -r requirements.txt
(venv) $ FLASK_APP=task_list flask db upgrade
(venv) $ FLASK_APP=task_list FLASK_ENV=development flask run
```

Then visit `http://localhost:5000` to play with the app.

## Deploying to Heroku

Run the following commands to deploy the app to Heroku:

```sh
$ git clone https://github.com/memcachier/examples-flask.git
$ cd examples-flask
$ heroku create
Creating app... done, ⬢ rocky-chamber-17110
https://rocky-chamber-17110.herokuapp.com/ | https://git.heroku.com/rocky-chamber-17110.git
$ heroku addons:create memcachier:dev
$ heroku addons:create heroku-postgresql:hobby-dev
$ heroku config:set FLASK_APP=task_list
$ heroku config:set SECRET_KEY="`< /dev/urandom tr -dc 'a-zA-Z0-9' | head -c16`"
$ git push heroku master
$ heroku open
```

## Get involved!

We are happy to receive bug reports, fixes, documentation enhancements,
and other improvements.

Please report bugs via the
[github issue tracker](http://github.com/memcachier/examples-flask/issues).

Master [git repository](http://github.com/memcachier/examples-flask):

* `git clone git://github.com/memcachier/examples-flask.git`

## Licensing

This example is open-sourced software licensed under the
[MIT license](https://opensource.org/licenses/MIT).
