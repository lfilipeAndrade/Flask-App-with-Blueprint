from flask import Flask
from .config import db
from importlib import import_module

def register_blueprints(app):

    blueprints_list = ['authentication', 'home']

    for module_name in blueprints_list:
        module = import_module('apps.{}.routes'.format(module_name))
        app.register_blueprint(module.blueprint)

def create_app(config):
    app = Flask(__name__)

    # Building a connection with your mysql database using SQLalchemy
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{}:{}@127.0.0.1:3306/{}'\
        .format('database_user','database_pwd','database_name')

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    register_blueprints(app)

    return app
