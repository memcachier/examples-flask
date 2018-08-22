import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_caching import Cache
import pylibmc
from flask_session import Session

cache = Cache()
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev_key',
        SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
            'sqlite:///' + os.path.join(app.instance_path, 'task-list.sqlite'),
        SQLALCHEMY_TRACK_MODIFICATIONS = False
    )

    db.init_app(app)
    migrate.init_app(app, db)

    cache_servers = os.environ.get('MEMCACHIER_SERVERS')
    if cache_servers == None:
        cache.init_app(app, config={'CACHE_TYPE': 'simple'})
    else:
        cache_user = os.environ.get('MEMCACHIER_USERNAME') or ''
        cache_pass = os.environ.get('MEMCACHIER_PASSWORD') or ''
        cache.init_app(app,
            config={'CACHE_TYPE': 'saslmemcached',
                    'CACHE_MEMCACHED_SERVERS': cache_servers.split(','),
                    'CACHE_MEMCACHED_USERNAME': cache_user,
                    'CACHE_MEMCACHED_PASSWORD': cache_pass,
                    'CACHE_OPTIONS': { 'behaviors': {
                        # Faster IO
                        'tcp_nodelay': True,
                        # Keep connection alive
                        'tcp_keepalive': True,
                        # Timeout for set/get requests
                        'connect_timeout': 2000, # ms
                        'send_timeout': 750 * 1000, # us
                        'receive_timeout': 750 * 1000, # us
                        '_poll_timeout': 2000, # ms
                        # Better failover
                        'ketama': True,
                        'remove_failed': 1,
                        'retry_timeout': 2,
                        'dead_timeout': 30}}})
        app.config.update(
            SESSION_TYPE = 'memcached',
            SESSION_MEMCACHED =
                pylibmc.Client(cache_servers.split(','), binary=True,
                               username=cache_user, password=cache_pass,
                               behaviors={
                                     # Faster IO
                                     'tcp_nodelay': True,
                                     # Keep connection alive
                                     'tcp_keepalive': True,
                                     # Timeout for set/get requests
                                     'connect_timeout': 2000, # ms
                                     'send_timeout': 750 * 1000, # us
                                     'receive_timeout': 750 * 1000, # us
                                     '_poll_timeout': 2000, # ms
                                     # Better failover
                                     'ketama': True,
                                     'remove_failed': 1,
                                     'retry_timeout': 2,
                                     'dead_timeout': 30,
                               })
        )
    Session(app)

    from . import models

    from . import task_list
    app.register_blueprint(task_list.bp)

    return app
