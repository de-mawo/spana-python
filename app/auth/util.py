"""Auth function to check authenticated Users"""

from functools import wraps
from flask import session, abort
from app.models.user import User

def isAdmin(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        """Admin authorize decorator function"""
        if "user_id" not in session:
            abort(401)  # Unauthorized
        user_id = session["user_id"]
        user = User.query.get(user_id)
        if user and user.role.value == "ADMIN":  
            return func(*args, **kwargs)
        else:
            abort(403)  # Forbidden
    return decorated_function

def isLoggedIn(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        """Function decorator to check if user is logged in"""
        if "user_id" not in session:
            abort(401)  # Unauthorized
        return func(*args, **kwargs)
    return decorated_function