from app import app
from flask import render_template
# Add a route
@app.route("/")
def index():
    return render_template('index.html', name = 'Moataz Hamdan')

@app.route("/new")
def new():
    name = 'Moataz' + ' ' + 'Hamdan'
    return f"This is a new route, how are you today {name}"

