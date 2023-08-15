from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# Create an instance of the flask application 
app = Flask(__name__)

# configure our app with the values from the Config class
app.config.from_object(Config)

# create an instance of SQLALCHEMY to represent our db
db = SQLAlchemy(app)

# create an instance of Migrate to handle the database migrations of our flask app
migrate = Migrate(app, db)


# import all of the routes file into the current package
from app import routes,models
# must be imported at the bottom of the file