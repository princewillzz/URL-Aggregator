


from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError

import requests

class LinkAddForm(FlaskForm):

    title = StringField(validators=[InputRequired(), Length(min=2, max=100)], render_kw={"placeholder": "Title"})

    link = StringField(validators=[InputRequired(), Length(min=4, max=100)], render_kw={"placeholder": "Link"})

    submit = SubmitField("Add Link")


    def validate_link(self, link):

        try:
            res = requests.get(link.data)
            if res.status_code >= 400:
                raise ValidationError('Invalid Link!!')

        except Exception as e:
            raise ValidationError('Invalid Link!!')

