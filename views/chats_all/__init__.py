from flask import render_template, 

# All chats BP (child of above)
@app.route('/chats/all')
def all_chats():
  return 'All chats'

# Room chat BP (child of above above)
@app.route('/chats/room/<chatname>')
def chatroom(chatname):
  return chatname

# DM chat BP (child of above above above)
@app.route('/chats/direct/<username>')
def direct_chat(username):
  return username
