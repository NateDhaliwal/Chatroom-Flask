from flask import Blueprint, redirect, render_template, request, session
from werkzeug.security import check_password_hash, generate_password_hash

from config import execute, userdb

login_signup = Blueprint(
  'login_signup', 
  __name__, 
  static_folder='../../static', 
  template_folder='templates'
)

# Login + Signup BP
@login_signup.route("/login", methods=['POST', 'GET'])
def login():
  session['username'] = ''
  if request.method == 'POST':
    username = request.form['username']
    password = request.form['password']

    # Get data
    userdata = execute(userdb, f'''
    SELECT username, password FROM userdata
    WHERE username == '{username}'
    ''')[0] # Since there is only 1 user from the UNIQUE type of username, take the first item of the returned list (there is only 1 item anyway) #type:ignore
    
    # For this userdata tuple, item 0 is the username, and item 1 is the password (hashed)
    
    if check_password_hash(userdata[1], password):
      # Password matches, login successful
      session['username'] = username
      return redirect('/home')
  return render_template('login.html')

@login_signup.route("/signup", methods=['POST', 'GET'])
def signup():
  session['username'] = ''
  if request.method == 'POST':
    username = request.form['username']
    name = request.form['name'] if not None else username
    password = request.form['password']
    hashed_password = generate_password_hash(password, "scrypt", 16)

    # Insert into database
    execute(userdb, f'''
    INSERT INTO userdata (username, name, password) VALUES (
    "{username}", "{name}", "{hashed_password}"
    )
    ''')
    
    session['username'] = username
    return redirect('/student/home')
  return render_template('signup.html')