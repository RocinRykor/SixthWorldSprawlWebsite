from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, PasswordField
from wtforms import BooleanField
from wtforms.validators import InputRequired, Length, EqualTo
from wtforms.widgets import TextArea


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired(),
                                                   Length(max=30)])
    password = PasswordField("Password", validators=[InputRequired(),
                                                     Length(min=12)])
    submit = SubmitField("Login")

class UserForm(FlaskForm):
    name = StringField("Display", validators=[InputRequired(),
                                               Length(max=30)])
    password = PasswordField("Password", validators=[InputRequired(),
                                                     Length(min=12)])
    confirmation = PasswordField(
                    "Password Confirmation",
                    validators=[InputRequired(),
                                Length(min=12),
                                EqualTo("password",
                                message="Must match password")])
    is_admin = BooleanField("Admin?")
    submit = SubmitField("Sign Up")

class EditUserForm(FlaskForm):
    name = StringField("Display", validators=[InputRequired(),
                                               Length(max=30)])
    submit = SubmitField("Change Display Name")

class CharacterForm(FlaskForm):
    name = StringField("Name", validators=[InputRequired(), Length(max=32)])
    bio = StringField("Bio", validators=[InputRequired(), Length(max=2048)])
    race = StringField("Race", validators=[InputRequired(), Length(max=32)])
    gender = StringField("Gender", validators=[InputRequired(), Length(max=32)])
    status = StringField("Status", validators=[InputRequired(), Length(max=64)])

    submit = SubmitField("Add Character")                                       