import sqlite3
from sqlite3 import Cursor

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