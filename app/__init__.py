from flask import Flask
# Create an instance of the flask application 
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hello'

# import all of the routes file into the current package
from app import routes
# must be imported at the bottom of the file