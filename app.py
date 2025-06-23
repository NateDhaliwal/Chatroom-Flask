from flask import Flask, render_template
from models import db, migrate

from views.login_signup import login_signup
from views.chats_parent import chats_parent

app = Flask(__name__, static_folder='static')

app.secret_key = __import__("secrets").token_hex(16)

# Register all Blueprints
app.register_blueprint(login_signup)
app.register_blueprint(chats_parent)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sqlalchemy.db"

db.init_app(app)
migrate.init_app(app, db)

# Index BP
@app.route('/')
def index():
  return render_template('index.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)
