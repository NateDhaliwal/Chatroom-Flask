from flask import render_template, session, redirect, flash, Blueprint
from models import Chat, ChatMember
from utils import login_required

chats_all = Blueprint(
  'chats_all',
  __name__,
  static_folder='../../static',
  template_folder='templates'
)

@login_required
@chats_all.route('/chats/my')
def my_chats():
  print(session['username'])
  # A list
  joined_chats_name = [chatname.chat_name for chatname in ChatMember.query.filter_by(username=session['username']).all()]
  joined_chats = []
  for joinedchat in joined_chats_name:
    chat = Chat.query.filter_by(chat_name=joinedchat).first()
    print(chat.chat_name)
    joined_chats.append(chat)
    
  print(len(joined_chats))
  return render_template("my_chats/my_chats.html", len=len, joined_chats=joined_chats)

@login_required
@chats_all.route("/chats/all")
def all_chats():
  # A list
  joined_chats_names = [
    chatname.chat_name for chatname in ChatMember.query.filter_by(username=session['username']).all()
  ]
  all_chats_list = Chat.query.all()
  return render_template(
    "all_chats/all_chats.html",
    len=len,
    joined_chats_names=joined_chats_names,
    all_chats_list=all_chats_list
  )
