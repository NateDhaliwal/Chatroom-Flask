from functools import wraps

from flask import flash, redirect, session, url_for


def login_required(function):
  @wraps(function)
  def wrapper(*args, **kwargs):
    # Check if user is logged in
    if 'username' not in session:
      flash("danger|Please log in to access this page")
      return redirect(url_for('login_signup.login'))
    return function(*args, **kwargs)
  return wrapper