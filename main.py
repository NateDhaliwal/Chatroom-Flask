import sqlite3
from sqlite3 import Cursor

from flask import Flask, redirect, render_template, url_for

app = Flask(__name__)

# Register all Blueprints

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
