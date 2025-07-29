#from config import chatdb, execute, userdb
#from sqlalchemy.dialects.sqlite import json
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()
migrate = Migrate()

# def delete_database(database):
#   execute(chatdb if database == "chatdb" else userdb, f'''
#     DROP TABLE IF EXISTS {database};
#   ''')

# Create databases, see format

# chatmessages, members and chatdata are both TEXT types to store JSON data

# execute(chatdb, '''
#   CREATE TABLE IF NOT EXISTS chatdb (
#   id INTEGER PRIMARY KEY,
#   chatname varchar(255) UNIQUE,
#   chatmessages TEXT NOT NULL,
#   chatowner varchar(15) UNIQUE,
#   members TEXT NOT NULL,
#   FOREIGN KEY (chatowner) REFERENCES userdb (username)
#   );
# ''')

# execute(userdb, '''
#   CREATE TABLE IF NOT EXISTS userdb (
#   userid int PRIMARY KEY,
#   username varchar(15) UNIQUE,
#   name varchar(30),
#   password varchar(30) NOT NULL
#   );
# ''')


class User(db.Model, UserMixin):
  __tablename__ = "users"

  user_id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(15), nullable=False, unique=True)
  name = db.Column(db.String(30))
  hashed_password = db.Column(db.String(30), nullable=False)
  
class Chat(db.Model):
  __tablename__ = "chats"

  chat_id = db.Column(db.Integer, primary_key=True)
  chat_name = db.Column(db.String(20), nullable=False, unique=True)
  chat_description = db.Column(db.String(100))
  chat_owner = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
  chat_date_made = db.Column(db.Date, nullable=False)

class ChatMessage(db.Model):
  __tablename__ = "chat_messages"

  message_id = db.Column(db.Integer, primary_key=True)
  message_poster = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
  message_content = db.Column(db.Text, nullable=False)
  message_date_made = db.Column(db.DateTime, nullable=False)
  belongs_to_chat = db.Column(db.Integer, db.ForeignKey("chats.chat_id"), nullable=False)

class ChatMember(db.Model):
  __tablename__ = 'chat_members'

  chat_member_id = db.Column(db.Integer, primary_key=True)
  chat_name = db.Column(db.Integer, db.ForeignKey('chats.chat_id'), nullable=False)
  username = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
