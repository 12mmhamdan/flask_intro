from app import app
from flask import render_template
# Add a route
@app.route("/")
def index():
    countries = [ 'United States', 'Canada', 'Mexico', 'France', 'Egypt', 'China']
    return render_template('index.html', name = 'Moataz Hamdan', countries=countries)

@app.route("/new")
def new():
    name = 'Moataz' + ' ' + 'Hamdan'
    return f"This is a new route, how are you today {name}"

