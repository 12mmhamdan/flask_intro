from app import app, db
from flask import render_template, url_for, redirect
from app.forms import SignUpForm
from app.models import User
# Add a route
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        # get the data from the form
        first_name = form.first_name.data
        last_name = form.last_name.data
        username = form.username.data
        email= form.email.data
        password=form.password.data
        print(first_name, last_name, username, email, password)

        # create a new instance of the user class with the data from the form
        new_user = User(first_name=first_name, last_name=last_name, username=username, email=email, password=password)

        # add the new user obj to the database
        db.session.add(new_user)
        db.session.commit()
        # redirect to the homepage when completed and validated
        return redirect(url_for('index'))
    else:
        print('wrong password dummy')
    return render_template('signup.html', form=form)

