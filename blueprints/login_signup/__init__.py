from flask import Blueprint, redirect, render_template

login_signup = Blueprint(
  'login_signup', 
  __name__, 
  static_folder='../../static', 
  template_folder='templates'
)

# Login + Signup BP
@login_signup.route('/login', methods=['GET', 'POST'])
def login():
  return render_template('login/login.html')

@login_signup.route('/signup', methods=['GET', 'POST'])
def signup():
  return render_template('signup/signup.html')