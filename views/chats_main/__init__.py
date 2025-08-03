from datetime import datetime

from flask import Blueprint, flash, redirect, render_template, request, session, url_for

from models import Chat, ChatMember, ChatMessage, db
from forms import CreateChatForm
from flask_login import login_required, current_user

chats_main = Blueprint(
  'chats_main',
  __name__,
  static_folder='../../static',
  template_folder='templates'
)

@chats_main.route('/create-chat', methods=['POST'])
@login_required
def create_chat():
  form = CreateChatForm()
  if form.validate_on_submit():
    # Fetch form fields
    chat_name = form.name.data
    chat_description = form.description.data
    chat_owner = current_user.username

    chat_id = len(Chat.query.all()) + 1
    # Create chat
    new_chat = Chat(
      id=chat_id,
      chat_name=chat_name,
      chat_description=chat_description,
      chat_owner=chat_owner
    )

    db.session.add(new_chat)
    db.session.commit()

    chat_member_id = len(ChatMember.query.all()) + 1
    # Create member
    new_member = ChatMember(
      id=chat_member_id,
      chat_id=chat_id,
      username=chat_owner
    )

    db.session.add(new_member)
    db.session.commit()

    return redirect(url_for('chats_main.chat_page', chat_name=chat_name))
  return redirect(url_for('chats_main.chat_page', chat_name=chat_name))

@chats_main.route('/chat/<string:chat_name>')
@login_required
def chat_page(chat_name):
    chat = Chat.query.filter_by(chat_name=chat_name).first()
    chat_members = ChatMember.query.filter_by(chat_id=chat.id).all()
    chat_messages = ChatMessage.query.filter_by(chat_id=chat.id).all()
    return render_template('chat_page/chat_page.html', chat=chat, chat_members=chat_members, chat_messages=chat_messages)
