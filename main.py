import sqlite3
from sqlite3 import Cursor

from flask import Flask
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

'''
@app.route('/')
def index():
    return 'Hello from Flask!'

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
'''
