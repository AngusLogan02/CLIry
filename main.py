from flask import Flask, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from forms import SignupForm, LoginForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "xwGG4jCKydJgdWcCY1KxBx7ub2xhUu6g"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = "False"
db = SQLAlchemy(app)

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
        flash(f"Account {form.username.data} created.", "success")
        return redirect(url_for("login"))

    return render_template("signup.html", form=form)