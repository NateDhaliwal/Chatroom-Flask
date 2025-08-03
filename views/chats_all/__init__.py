from flask import render_template, redirect, flash, Blueprint
from models import Chat, ChatMember
from forms import CreateChatForm
from flask_login import login_required, current_user

chats_all = Blueprint(
  'chats_all',
  __name__,
  static_folder='../../static',
  template_folder='templates'
)

@chats_all.route('/chats/my')
@login_required
def my_chats():
  form = CreateChatForm()
  # A list
  joined_chats_name = [chatname.chat_name for chatname in ChatMember.query.filter_by(username=current_user.username).all()]
  joined_chats = []
  for joinedchat in joined_chats_name:
    chat = Chat.query.filter_by(chat_name=joinedchat).first()
    joined_chats.append(chat)
    
  return render_template("my_chats/my_chats.html", len=len, joined_chats=joined_chats, form=form)

@chats_all.route("/chats/all")
@login_required
def all_chats():
  joined_chats_names = [
    chatname.chat_name for chatname in ChatMember.query.filter_by(username=current_user.username).all()
  ]
  joined_chats = []
  for joinedchat in joined_chats_name:
    chat = Chat.query.filter_by(chat_name=joinedchat).first()
    joined_chats.append(chat)
    
  all_chats_list = Chat.query.all()
  return render_template(
    "all_chats/all_chats.html",
    len=len,
    joined_chats_names=joined_chats_names,
    all_chats_list=all_chats_list,
    joined_chats=joined_chats
  )
