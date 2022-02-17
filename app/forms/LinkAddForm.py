


from pydoc import render_doc
from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError

from app import db

class LinkAddForm(FlaskForm):

    title = StringField(validators=[InputRequired(), Length(min=4, max=100)], render_kw={"placeholder": "Title"})

    link = StringField(validators=[InputRequired(), Length(min=4, max=100)], render_kw={"placeholder": "Link"})

    submit = SubmitField("Add Link")
