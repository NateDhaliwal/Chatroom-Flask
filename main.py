from flask import Flask, render_template

from blueprints.login_signup import login_signup

app = Flask(__name__, static_folder='static')

app.secret_key = __import__("secrets").token_hex(16)

# Register all Blueprints
app.register_blueprint(login_signup)


# Index BP
@app.route('/')
def index():
  return render_template('index.html')

# All chats BP (child of above)
@app.route('/chats/all')
def all_chats():
  return 'All chats'

# Room chat BP (child of above above)
@app.route('/chats/room/<chatname>')
def chatroom(chatname):
  return chatname

# DM chat BP (child of above above above)
@app.route('/chats/direct/<username>')
def direct_chat(username):
  return username

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)
