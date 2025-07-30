from flask import Flask, render_template
from flask_login import LoginManager
from models import db, migrate, User

from views.login_signup import login_signup
from views.chats_parent import chats_parent
from views.chats_all import chats_all
from views.chats_main import chats_main

app = Flask(__name__, static_folder='static')

app.secret_key = "a very secret key" # __import__("secrets").token_hex(16)

# Register all Blueprints
app.register_blueprint(login_signup)
app.register_blueprint(chats_parent)
app.register_blueprint(chats_all)
app.register_blueprint(chats_main)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sqlalchemy.db"

login_manager = LoginManager()

db.init_app(app)
migrate.init_app(app, db)
login_manager.init_app(app)

login_manager.login_view = "login_signup.login"

@login_manager.user_loader
def load_user(user_id):
  return User.query.filter_by(id=user_id).first()

# Index BP
@app.route('/')
def index():
  return render_template('index.html')
