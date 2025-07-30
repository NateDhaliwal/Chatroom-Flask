from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    username = StringField("username", validators=[DataRequired(message="Username cannot be blank"), Length(min=1, max=15, message="Username must be be between 1 and 15 characters long")])
    password = PasswordField("password", validators=[DataRequired(message="Password cannot be blank"), Length(min=8, message="Password to short (minimum 8 characters)")])

class SignupForm(FlaskForm):
    username = StringField("username", validators=[DataRequired(message="Username cannot be blank"), Length(min=1, max=15, message="Username must be be between 1 and 15 characters long")])
    password = PasswordField