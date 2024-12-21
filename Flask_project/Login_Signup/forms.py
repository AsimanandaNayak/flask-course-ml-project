from flask_wtf import FlaskForm
from wtforms import StringField, SelectField ,PasswordField,SubmitField
from wtforms.validators import DataRequired , Length , Email , optional , EqualTo


class SignupPage(FlaskForm):
    username = StringField(
        "Username",
        validators=[DataRequired(), Length(3,50)]
    )

    email = StringField(
        "Email",
        validators=[DataRequired() , Email()]
    )

    age = SelectField(
        "Age",
        choices=["Male","Female","Other"],
        validators=[optional()]
    )

    password = PasswordField(
        "Password",
        validators=[DataRequired() ,Length(5,30)]
    )

    confirm_password = PasswordField(
        "Confirm Password",
        validators=[DataRequired() ,Length(5,30),EqualTo("password")]
    )

    submit = SubmitField("Signup")

class LoginPage(FlaskForm):
    email = StringField(
        "Email",
        validators=[DataRequired(),Email()]
    )

    password = PasswordField(
        "Password",
        validators=[DataRequired(),Length(5,30)]
    )

    submit = SubmitField("Login")