from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
# from wtforms import BooleanField
from wtforms.validators import InputRequired, Length


class LoginForm(FlaskForm):
    name = StringField("Name", validators=[InputRequired(), Length(max=30)])
    password = PasswordField("Password", validators=[InputRequired(),
                                                     Length(min=12)])
    submit = SubmitField("Login")
