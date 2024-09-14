from flask_wtf import FlaskForm
from wtforms import BooleanField
from wtforms import StringField, TextAreaField, SubmitField, PasswordField, IntegerField,SelectField
from wtforms.validators import InputRequired, Length, EqualTo, DataRequired, NumberRange, Optional


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
    bio = TextAreaField("Bio", validators=[InputRequired(), Length(max=2048)])
    submit = SubmitField("Edit User")


class CharacterForm(FlaskForm):
    name = StringField("Name", validators=[InputRequired(), Length(max=32)])
    bio = TextAreaField("Bio", validators=[InputRequired(), Length(max=2048)])
    race = StringField("Race", validators=[InputRequired(), Length(max=32)])
    gender = StringField("Gender", validators=[InputRequired(), Length(max=32)])
    status = StringField("Status", validators=[InputRequired(), Length(max=64)])
    portrait_id = StringField("Portrait ID", validators=[InputRequired(), Length(max=8)])
    portrait_filename = StringField("Portrait filename", validators=[InputRequired(), Length(max=64)])

    submit = SubmitField("Add Character")


class MatrixHostForm(FlaskForm):
    hostname = StringField('Hostname', validators=[DataRequired(), Length(max=11)])
    provider = SelectField('Provider', choices=["Public",
                                                "Ares Macrotechnology",
                                                "Renraku Computer Systems",
                                                "Saeder-Krupp",
                                                "Transys Neuronet",
                                                "Aztechnology",
                                                "Cross Applied Technologies",
                                                "Novatech Incorperated",
                                                "Microdeck Industries",
                                                "Shiawase",
                                                "Mitsuhama Computer Technologies",
                                                "NeuroTech Computing",
                                                "Unknown"], validators=[DataRequired(), Length(max=64)])
    security_code = SelectField('Security Code', choices=["Blue",
                                                "Green",
                                                "Orange",
                                                "Red"], validators=[DataRequired(), Length(max=16)])
    system_rating = IntegerField('System Rating', validators=[DataRequired(), NumberRange(min=1)])
    access_rating = IntegerField('Access Rating', validators=[DataRequired(), NumberRange(min=1)])
    control_rating = IntegerField('Control Rating', validators=[DataRequired(), NumberRange(min=1)])
    file_rating = IntegerField('File Rating', validators=[DataRequired(), NumberRange(min=1)])
    index_rating = IntegerField('Index Rating', validators=[DataRequired(), NumberRange(min=1)])
    slave_rating = IntegerField('Slave Rating', validators=[DataRequired(), NumberRange(min=1)])
    paydata_points = IntegerField('Paydata Points', validators=[DataRequired(), NumberRange(min=0)])

    submit = SubmitField("Save Host")
