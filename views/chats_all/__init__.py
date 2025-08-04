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
    
  return render_template("my_chats/my_chats.html", form=form)

@chats_all.route("/chats/all")
@login_required
def all_chats():
  all_chats_list = Chat.query.all()
  return render_template(
    "all_chats/all_chats.html",
    all_chats_list=all_chats_list
  )
