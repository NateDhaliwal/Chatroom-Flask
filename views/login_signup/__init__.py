from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash

from models import User, db
from forms import LoginForm

from flask_login import login_user, logout_user

login_signup = Blueprint(
  'login_signup', 
  __name__, 
  static_folder='../../static', 
  template_folder='templates'
)

# Login + Signup BP
@login_signup.route("/login", methods=['POST', 'GET'])
def login():
  login_form = LoginForm()
  # If user is already signed in
  if 'username' in session:
    print(session['username'])
    return redirect(url_for('chats_all.my_chats'))

  if login_form.validate_on_submit():
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
      login_user(User.query.filter_by(username=username).first())
      flash("success|Log in successful!")
      return redirect(url_for('chats_all.my_chats'))
    else:
      flash("danger|Username or password incorrect")
      return render_template('login/login.html', form=login_form)
  return render_template('login/login.html', form=login_form)

@login_signup.route("/signup", methods=['POST', 'GET'])
def signup():
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
    return redirect(url_for('chats_all.my_chats'))
  return render_template('signup/signup.html')
