from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# Create an instance of the flask application 
app = Flask(__name__)

# configure our app with the values from the Config class
app.config.from_object(Config)

# create an instance of SQLALCHEMY to represent our db
db = SQLAlchemy(app)

# create an instance of Migrate to handle the database migrations of our flask app
migrate = Migrate(app, db)

# create an instance of login manager to handle authenitcation
login = LoginManager(app)
# Customize login process
login.login_view = 'login'
login.login_message='You need to be logged in for that that!'
login.login_message_category = 'info'

# register api blueprint with our app
from app.blueprints.api import api
app.register_blueprint(api)

# import all of the routes file into the current package
from app import routes,models
# must be imported at the bottom of the file