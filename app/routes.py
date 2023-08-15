from app import app
from flask import render_template, url_for, redirect
from app.forms import SignUpForm
# Add a route
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        username = form.username.data
        email= form.email.data
        password=form.password.data
        print(first_name, last_name, username, email, password)
        return redirect(url_for('index'))
    else:
        print('wrong password dummy')
    return render_template('signup.html', form=form)

