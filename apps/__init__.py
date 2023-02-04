from flask import Flask
from .config import db
from importlib import import_module

def register_blueprints(app):
    for module_name in ('authentication', 'home'):
        module = import_module('apps.{}.routes'.format(module_name))
        app.register_blueprint(module.blueprint)

def create_app(config):
    app = Flask(__name__)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{}:{}@127.0.0.1:3306/{}'\
        .format('client','7362','custumer_review')

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    register_blueprints(app)

    return app
