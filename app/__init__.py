import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import BASE_DIR, SQLALCHEMY_DATABASE_URI

db = SQLAlchemy()

def create_database(app):
    if not os.path.exists(os.path.join(BASE_DIR, 'app.db')):
        db.create_all(app=app)
        print('Created Database')


# Define the WSGI application object
app = Flask(__name__)


# Configurations
app.config.from_object('config')
app.url_map.strict_slashes = False

db.init_app(app)

from app.models import User

create_database(app)

# import modules
from app.admin.views import mod_admin as admin_module
from app.auth.views import mod_auth as auth_module

app.register_blueprint(admin_module)
app.register_blueprint(auth_module)

