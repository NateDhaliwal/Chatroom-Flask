import sqlite3
from sqlite3 import Cursor

from flask import Flask, redirect, render_template
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)

userdataconn = sqlite3.connect("userdata.sqlite")
chatsconn = sqlite3.connect("chatdb.sqlite")

userdb = userdataconn.cursor()
chatdb = chatsconn.cursor()

def execute(cursor: Cursor, query: str):
    if cursor == userdb:
        userdb.execute(query)
        userdataconn.commit()
    elif cursor == chatdb:
        chatdb.execute(query)
        chatsconn.commit()

# Index BP
@app.route('/')
def index():
    return 'Hello from Flask!'

# Login + Signup BP
@app.route('/login')
def login():
    return 'Login'

@app.route('/signup')
def signup():
    return 'Signup'

# Chats BP: redirect (parent)
@app.route('/chats')
def chats_redirect_to_all_chats():
    return redirect('/chats/all')

# All chats BP (child of above)
@app.route('/chats/all')
def all_chats():
    return 'All chats'

# Room chat BP (child of above above)
@app.route('/chat/room/<chatname>')
def chatroom(chatname):
    return chatname

# DM chat BP (child of above above above)
@app.route('/chat/direct/<username>')
def direct_chat(username):
    return username


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)

