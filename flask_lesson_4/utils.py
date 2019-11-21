from functools import wraps

from flask import session


def check_login(f):
    """
    This decorator will check your logged_in parameter from session
    if it false you will see msg "You must login to see this page"
    if it true you will see the content of your page

    """
    @wraps(f)
    def wrapper(*args, **kwargs):
        if session.get("logged_in"):
            func = f(*args, **kwargs)
        else:
            return "You must login to see this page"
        return func

    return wrapper
