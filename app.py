import os

from flask import Flask, render_template, redirect, url_for
from flask_login import LoginManager, current_user
from flask_socketio import SocketIO

from models import db, migrate, User

from views.login_signup import login_signup
from views.chats_parent import chats_parent
from views.chats_all import chats_all
from views.chats_main import chats_main

app = Flask(__name__, static_folder='static', template_folder="templates")

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
socketio = SocketIO(app)

login_manager.login_view = "login_signup.login"

@login_manager.user_loader
def load_user(user_id):
  return User.query.filter_by(id=user_id).first()

@app.context_processor
def inject_joined_chats():
  js_dir = os.path.join(app.static_folder, "js")
  js_files = [
      f"js/{filename}" for filename in os.listdir(js_dir)
      if filename.endswith(".js")
  ]
  if current_user.is_authenticated:
    joined_chats = current_user.joined_chats
    return dict(joined_chats=joined_chats)
  return dict(joined_chats=[])


# Index BP
@app.route('/')
def index():
  if current_user.is_authenticated:
    return redirect(url_for('chats_all.my_chats'))
  return render_template('index.html')


@app.errorhandler(404)
def not_found(error):
  return render_template('404.html'), 404

if __name__ == '__main__':
  socketio.run(app, debug=True, use_reloader=True)
