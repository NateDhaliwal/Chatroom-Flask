from datetime import datetime

from flask import Blueprint, flash, redirect, render_template, request, session, url_for

from models import Chat, ChatMember, ChatMessage, User, db
from forms import CreateChatForm, CreateChatMessageForm
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
    chat_owner_id = current_user.id

    chat_id = len(Chat.query.all()) + 1
    # Create chat
    new_chat = Chat(
      id=chat_id,
      chat_name=chat_name,
      chat_description=chat_description,
      chat_owner=chat_owner_id
    )

    db.session.add(new_chat)
    db.session.commit()

    chat_member_id = len(ChatMember.query.all()) + 1
    # Create member
    new_member = ChatMember(
      id=chat_member_id,
      chat_id=chat_id,
      user_id=chat_owner_id
    )

    db.session.add(new_member)
    db.session.commit()

    return redirect(url_for('chats_main.chat_page', chat_name=chat_name))
  return redirect(url_for('chats_main.chat_page', chat_name=chat_name))

@chats_main.route('/chat/<string:chat_name>')
@login_required
def chat_page(chat_name):
  form = CreateChatMessageForm()
  chat = Chat.query.filter_by(chat_name=chat_name).first()
  chat_members = ChatMember.query.filter_by(chat_id=chat.id).all()
  chat_messages = ChatMessage.query.filter_by(chat_id=chat.id).all()
  return render_template('chat_page/chat_page.html', User=User, form=form, chat=chat, chat_members=chat_members, chat_messages=chat_messages)

@chats_main.route('/chat/<string:chat_name>/create_message', methods=['POST'])
@login_required
def create_message(chat_name):
  form = CreateChatMessageForm()
  if form.validate_on_submit():
    message_content = form.message.data
    new_message_id = len(ChatMessage.query.all()) + 1
    chat_id = Chat.query.filter_by(chat_name=chat_name).first().id
    new_message = ChatMessage(id=1, message_poster=current_user.id, message_content=message_content, chat_id=chat_id)
    db.session.add(new_message)
    db.session.commit()
    return redirect(url_for('chats_main.chat_page', chat_name=chat_name))
  return redirect(url_for('chats_main.chat_page', chat_name=chat_name))
