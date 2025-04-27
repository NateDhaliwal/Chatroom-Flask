from flask import Blueprint, redirect

chats_parent = Blueprint('chats_parent', __name__)

# Chats BP: redirect (parent)
@chats_parent.route('/chats')
def chats_redirect_to_all_chats():
  return redirect('/chats/all')