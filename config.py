import sqlite3
from sqlite3 import Cursor

userdataconn = sqlite3.connect("userdata.sqlite")
chatsconn = sqlite3.connect("chatdb.sqlite")

userdb = userdataconn.cursor()
chatdb = chatsconn.cursor()

def execute(cursor: Cursor, query: str):
  if cursor == userdb:
    if 'SELECT' in query:
      return userdb.execute(query).fetchall()
    else:
      userdataconn.commit()
      userdb.execute(query)
      return None
  elif cursor == chatdb:
    if 'SELECT' in query:
      return chatdb.execute(query).fetchall()
    else:
      chatsconn.commit()
      chatdb.execute(query)