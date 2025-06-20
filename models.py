from config import chatdb, execute, userdb
from main import sqlaldb as db


def delete_database(database):
  execute(chatdb if database == "chatdb" else userdb, f'''
  DROP TABLE IF EXISTS {database};
  ''')

# Create databases, see format

# chatmessages, members and chatdata are both TEXT types to store JSON data

execute(chatdb, '''
CREATE TABLE IF NOT EXISTS chatdb (
id INTEGER PRIMARY KEY,
chatname varchar(255) UNIQUE,
chatmessages TEXT NOT NULL,
chatdata TEXT NOT NULL,
members TEXT NOT NULL
);
''')

execute(userdb, '''
CREATE TABLE IF NOT EXISTS userdb (
userid int PRIMARY KEY,
username varchar(15) UNIQUE,
name varchar(30),
password varchar(30) NOT NULL
);
''')

class User(db.Model):
  __tablename__ = "users"
  userid = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(15), nullable=False)
  name = db.Column(db.String(30))
  password = db.Column(db.String(30), nullable=False)
  
