from flask import render_template, flash, redirect, url_for
from main.forms import SignupForm, LoginForm
from main import app, db, bcrypt
from main.models import User, Post


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == 'angus' and form.password.data == 'password':
            return redirect(url_for("index"))
        else:
            flash("Login unsuccessful. Please check username and password.", "fail")
    return render_template("login.html", form=form)

@app.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        flash(f"Account {form.username.data} created. Log in.", "success")
        return redirect(url_for("login"))

    return render_template("signup.html", form=form)