from flask import flash, session, redirect
from functools import wraps

def login_required(function):
  @wraps(function)
  def wrapper(*args, **kwargs):
    # Check if user is logged in
    if 'username' not in session:
      flash("danger|Please log in to access this page")
      return redirect('/login')
    return function(*args, **kwargs)
  return wrapper