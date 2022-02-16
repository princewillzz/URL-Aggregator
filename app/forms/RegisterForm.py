from pydoc import render_doc
from sys import prefix
from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError

from app import db
from app.models.User import User

class RegisterForm(FlaskForm):

    email = StringField(validators=[InputRequired(), Length(min=4, max=100)], render_kw={"placeholder": "Email"})

    password = PasswordField(validators=[InputRequired(), Length(min=4, max=50)], render_kw={"placeholder": "Password"})

    username = StringField(validators=[InputRequired(), Length(min=4, max=50)], render_kw={"placeholder": "Public Username"})

    submit = SubmitField("Register")

    def validate_email(self, email):
        existing_user_email = User.query.filter_by(
            email=email.data
        ).first()

        if existing_user_email:
            raise ValidationError("The email already exists!!")


    def validate_username(self, username):
        existing_user_username = User.query.filter_by(
            username=username.data
        ).first()

        if existing_user_username:
            raise ValidationError("The username already exists!!")
