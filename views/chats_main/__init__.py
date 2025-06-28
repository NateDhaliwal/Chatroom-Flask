from flask import render_template, session, redirect, flash, Blueprint, request, url_for
from models import Chat, ChatMember, ChatMessage, db
from utils import login_required
from datetime import datetime

chats_main = Blueprint(
  'chats_main',
  __name__,
  static_folder='../../static',
  template_folder='templates'
)

@login_required
@chats_main.route('/create-chat', methods=['POST'])
def create_chat():
    # Fetch form fields
    chat_name = request.form.get('chat_name')
    chat_description = request.form.get('chat_description')
    chat_owner = session['username']
    chat_date_made = datetime.now()

    # Create chat
    new_chat = Chat(
        chat_name=chat_name,
        chat_description=chat_description,
        chat_owner=chat_owner,
        chat_date_made=chat_date_made
    )

    db.session.add(new_chat)
    db.session.commit()

    # Create member
    new_member = ChatMember(
        chat_name=chat_name,
        username=chat_owner
    )

    db.session.add(new_member)
    db.session.commit()

    return redirect(url_for('chats_main.chat_page', chat_name=chat_name))

@login_required
@chats_main.route('/chat/<string:chat_name>')
def chat_page(chat_name):
    chat = Chat.query.filter_by(chat_name=chat_name)
    chat_members = ChatMember.query.filter_by(chat_name=chat_name).all()
    chat_messages = ChatMessage.query.filter_by(belongs_to_chat=chat_name).all()
    return render_template('chat_page/chat_page.html', chat=chat, chat_members=chat_members, chat_messages=chat_messages)
