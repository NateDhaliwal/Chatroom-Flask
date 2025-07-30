from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    username = StringField("username", validators=[DataRequired(message="Username cannot be blank"), Length(min=1, max=15, message="Username must be be between 1 and 15 characters long")])
    password = PasswordField("password", validators=[DataRequired(message="Password cannot be blank"), Length(min=8, message="Password to short (minimum 8 characters)")])
    remember_me = BooleanField(label="Remember Me")

class SignupForm(FlaskForm):
    username = StringField("username", validators=[DataRequired(message="Username cannot be blank"), Length(min=1, max=15, message="Username must be be between 1 and 15 characters long")])
    password = PasswordField("password", validators=[DataRequired(message="Password cannot be blank"), Length(min=8, message="Password to short (minimum 8 characters)")])
    name = StringField("name", validators=[Length(max=30, message="Name cannot exceed 30 characters")])
    remember_me = BooleanField(label="Remember Me")

class CreateChatForm(FlaskForm):
    name = StringField("name", validators=[DataRequired(message="Chat name cannot be blank"), Length(min=1, max=20, message="Chat name must be between 1 and 20 characters")])
    description = TextAreaField("description", validators=[Length(max=200, message="Chat description cannot 200 characters")])
