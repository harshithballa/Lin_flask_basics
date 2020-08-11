
from flask import Flask

def create_app(test_config=None):
    app =  Flask(__name__)
    app.secret_key = 'haegaoegan23afjag44agaj'

    from . import urlshort                #  .  current dir  .. parent dir ...grand parent dir
    app.register_blueprint(urlshort.bp)
    return app
