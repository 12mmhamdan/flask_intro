from flask import Flask
# Create an instance of the flask application 
app = Flask(__name__)

# Add a route
@app.route("/")
def index():
    return "<p>Hello, World!</p>"

@app.route("/new")
def new():
    return "this is a new route, how are you today, we woooooo, this is a cool change"
