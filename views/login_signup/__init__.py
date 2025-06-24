from flask import Blueprint, redirect, render_template, request, session, flash
from werkzeug.security import check_password_hash, generate_password_hash

# from config import execute, userdb

from models import User, db

login_signup = Blueprint(
  'login_signup', 
  __name__, 
  static_folder='../../static', 
  template_folder='templates'
)

# Login + Signup BP
@login_signup.route("/login", methods=['POST', 'GET'])
def login():
  # If user is already signed in
  if 'username' in session:
    return redirect("/chats/all")

  session['username'] = ''
  if request.method == 'POST':
    username = request.form['username']
    password = request.form['password']

    # Check if user exists
    if not User.query.filter_by(username=username).first():
      flash("danger|Account doesn't exist. Please create one.")
      return render_template('login/login.html')

    # Get data
    hashed_password = User.query.filter_by(username=username).first().hashed_password
    userdata = [username, hashed_password]

    # For this userdata tuple, item 0 is the username, and item 1 is the password (hashed)
    
    if check_password_hash(userdata[1], password):
      # Password matches, login successful
      session['username'] = username
      flash("success|Log in successful!")
      return redirect('/chats/all')
    else:
      flash("danger|Username or password incorrect")
      return render_template('login/login.html')
  return render_template('login/login.html')

@login_signup.route("/signup", methods=['POST', 'GET'])
def signup():
  session['username'] = ''
  if request.method == 'POST':
    username = request.form['username']
    name = request.form['name'] if not None else username
    password = request.form['password']
    hashed_password = generate_password_hash(password, "scrypt", 16)

    # Check if user exists
    if User.query.filter_by(username=username).first():
      flash('danger|Account already exists.')
      return render_template('signup/signup.html')

    # Create instance of User class with new user's data
    new_user = User(username=username, name=name, hashed_password=hashed_password)

    # Insert into database
    db.session.add(new_user)
    db.session.commit()
    
    session['username'] = username
    return redirect('/chats/all')
  return render_template('signup/signup.html')
