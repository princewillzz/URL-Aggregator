
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length


class LoginForm(FlaskForm):

    email = StringField(validators=[InputRequired(), Length(min=4, max=100)], render_kw={"placeholder": "Email"})

    password = PasswordField(validators=[InputRequired(), Length(min=4, max=100)], render_kw={"placeholder": "Password"})

    submit = SubmitField("Login")
