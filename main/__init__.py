from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt, bcrypt

app = Flask(__name__)
app.config["SECRET_KEY"] = "xwGG4jCKydJgdWcCY1KxBx7ub2xhUu6g"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = "False"
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from main import routes