


from pydoc import render_doc
from wsgiref.validate import validator
from flask_login import current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError

import requests

from app.forms.RegisterForm import RegisterForm
from app.models.User import User

class UserDetailsForm(FlaskForm):

    password = PasswordField(render_kw={"placeholder": "Password"})

    username = StringField(validators=[InputRequired(), Length(min=4, max=50)], render_kw={"placeholder": "Public Username"})

    bio = StringField(validators=[Length(min=4, max=100)], render_kw={"placeholder": "Bio"})

    submit = SubmitField("Save Details")


    def validate_username(self, username):
        if not username.data == current_user.username:
            existing_user_username = User.query.filter_by(
                username=username.data
            ).first()

            if existing_user_username:
                raise ValidationError("The username already exists!!")
