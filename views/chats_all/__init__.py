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
  # A list
  joined_chats = ChatMember.query.filter_by(username=session['username']).all()
  return render_template("my_chats.html", joined_chats=joined_chats)

@my_chats.route("/chats/all")
def all_chats():
  # A list
  joined_chats = ChatMember.query.filter_by(username=session['username']).all()
  unjoined_chats = [
    chat for chat in Chat.query.all()
    if all(chat.chat_name != joinedChat.chat_name for joinedChat in joined_chats)
  ]
  return render_template("all_chats.html", joined_chats=joined_chats, unjoined_chats=unjoined_chats)


# # Room chat BP (child of above above)
# @app.route('/chats/room/<chatname>')
# def chatroom(chatname):
#   return chatname
#
# # DM chat BP (child of above above above)
# @app.route('/chats/direct/<username>')
# def direct_chat(username):
#   return username
