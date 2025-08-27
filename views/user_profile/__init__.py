from flask import Blueprint, flash, redirect, render_template, request, session, url_for, abort

from models import Chat, ChatMember, ChatMessage, User, db
from forms import CreateChatForm, CreateChatMessageForm
from flask_login import login_required, current_user

user_profile = Blueprint(
  'user_profile',
  __name__,
  static_folder='../../static',
  template_folder='templates'
)

@user_profile.route('/user/<str:username>/profile')
def user_profile_route(username):
    if User.query.filter_by().exists():
        pass