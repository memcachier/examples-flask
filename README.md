# MemCachier and Flask on Elastic Beanstalk tutorial

This is an example Flask task list app that uses
the [MemCachier](https://www.memcachier.com) on
[Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/).

Detailed instructions for developing this app are available
[here](https://blog.memcachier.com/flask-elastic-beanstalk-and-memcache).

## Deploy to Elastic Beanstalk

You can deploy this app yourself to Elastic Beanstalk to deploy it yourself.

```bash
$ eb init -p python-3.6 flask-memcache --region us-east-2
$ eb create flask-env -db.engine postgres
# pick a username/password for your database.
```

Then add MemCachier environment variables to your Elastic Beanstalk environment:

```bash
(venv) $ eb setenv MEMCACHIER_USERNAME=<username>\
  MEMCACHIER_PASSWORD=<password>\
  MEMCACHIER_SERVERS=<servers>\
```

Finally, deploy to Elastic Beanstalk.

```bash
$ eb deploy
```

## Running Locally

Run the following commands to get started running this app locally:

```sh
$ git clone https://github.com/memcachier/examples-flask.git
$ cd examples-flask
$ mkdir instance
$ python -m venv venv
$ source venv/bin/activate
(venv) $ pip install -r requirements.txt
(venv) $ FLASK_APP=application.py flask db upgrade
(venv) $ FLASK_APP=application.py FLASK_ENV=development flask run
```

Then visit `http://localhost:5000` to play with the app.

## Get involved!

We are happy to receive bug reports, fixes, documentation enhancements,
and other improvements.

Please report bugs via the
[github issue tracker](http://github.com/memcachier/examples-flask/issues).

Master [git repository](http://github.com/memcachier/examples-flask):

* `git clone git://github.com/memcachier/examples-flask.git`
* `git checkout elastic-beanstalk`

## Licensing

This example is open-sourced software licensed under the
[MIT license](https://opensource.org/licenses/MIT).
