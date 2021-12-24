from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from main.models import User

class SignupForm(FlaskForm):
    username = StringField("USERNAME:", validators=[DataRequired(), Length(min=3, max=24)])
    email = StringField("EMAIL:", validators=[DataRequired(), Email()])
    password = PasswordField("PASSWORD:", validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField('CONFIRM PASSWORD:', validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField('SIGN UP')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("An account already exists with that username.")
    def validate_email(self, email):
        email = User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError("An account already exists with that email.")

class LoginForm(FlaskForm):
    username = StringField("USERNAME:", validators=[DataRequired(), Length(min=3, max=24)])
    password = PasswordField("PASSWORD:", validators=[DataRequired(), Length(min=8)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('LOG IN')