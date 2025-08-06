from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, EmailField
from wtforms.validators import DataRequired, Length, Email

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(message="Username cannot be blank"), Length(min=1, max=15, message="Username must be be between 1 and 15 characters long")])
    password = PasswordField("Password", validators=[DataRequired(message="Password cannot be blank"), Length(min=8, message="Password to short (minimum 8 characters)")])
    remember_me = BooleanField(label="Remember Me")

class SignupForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(message="Username cannot be blank"), Length(min=1, max=15, message="Username must be be between 1 and 15 characters long")])
    password = PasswordField("Password", validators=[DataRequired(message="Password cannot be blank"), Length(min=8, message="Password to short (minimum 8 characters)")])
    name = StringField("Name", validators=[Length(max=30, message="Name cannot exceed 30 characters")])
    email = EmailField("Email", validators=[DataRequired(message="Email cannot be blank"), Email(message="Please enter a valid email address")])
    remember_me = BooleanField(label="Remember Me")

class CreateChatForm(FlaskForm):
    name = StringField("Chat name", validators=[DataRequired(message="Chat name cannot be blank"), Length(min=1, max=20, message="Chat name must be between 1 and 20 characters")])
    description = TextAreaField("Chat description (optional)", validators=[Length(max=200, message="Chat description cannot 200 characters")])

class CreateChatMessageForm(FlaskForm):
    content = TextAreaField("Send a message", validators=[DataRequired("Please input a message")])
