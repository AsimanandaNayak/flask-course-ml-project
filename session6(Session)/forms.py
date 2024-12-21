from flask_wtf import FlaskForm
from wtforms import StringField , PasswordField , SubmitField
from wtforms.validators import DataRequired , length

class LoginForm(FlaskForm):
    username = StringField(
        "Username",
        validators=[DataRequired(), length(5,50)]
    )

    password = PasswordField(
        "Password",
        validators=[DataRequired(),length(5,15)]
    )

    submit = SubmitField("Login")