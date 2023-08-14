from app import app
# Add a route
@app.route("/")
def index():
    return "<p>Hello, World!</p>"

@app.route("/new")
def new():
    return "this is a new route, how are you today, we woooooo, this is a cool change"
