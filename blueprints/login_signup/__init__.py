from flask import Blueprint, redirect, render_template, session
from werkzeug.security import generate_password_hash, check_password_hash

login_signup = Blueprint(
  'login_signup', 
  __name__, 
  static_folder='../../static', 
  template_folder='templates'
)

# Login + Signup BP
@login_signup.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    username = request.form['username']
    password = request.form['password']
    hashed_password_from_user = execute()
    if check_password_hash(password, hashed_password_from_user):
      session['username'] = username
      return redirect("/chats/all")
    else:
      return render_template('login/login.html'), flash('danger|Password is incorrect.')
  return render_template('login/login.html')

@login_signup.route('/signup', methods=['GET', 'POST'])
def signup():
  return render_template('signup/signup.html')
