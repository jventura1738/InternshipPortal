# Internship Portal Web App
# auth.py for API


"""
Clients: Dr. Joseph Anderson, Dr. Giulia Franchi
Team: Blaine Mason, Jacob Duncan, Justin Ventura, Margaret Finnegan
"""


# Flask Imports:
from flask import Blueprint, request

# Helper imports:
from .helpers import correct_login, admin_session
from .constants import OK, FORBIDDEN, BAD_REQUEST
from flask import session
import hashlib  # Using for password hashing (SHA-256)


# Create auth blueprint:
auth = Blueprint('auth', __name__)

# ------------------------------------------------------------------------
#          AUTH ROUTES: these routes are all for authentication
# ------------------------------------------------------------------------


# Handles the login form post requests:
@auth.route('/login-submit', methods=['POST'])
def login_submit():
    """Login submission route.
    This function handles the login submission attempts.

    Expects json from post request with the form:
    {
        "username": <username>,
        "password": <password>
    }

    If login success, returns 'admin.html' and OK status.
    Else, returns error message.
    """
    response = dict()
    login_data = request.json
    username, password = login_data['username'], login_data['password']

    # Ensure both username and password are provided.
    if not username or not password:
        response['err_msg'] = 'Missing username or password.'
        code = FORBIDDEN
    else:
        # Hash password with SHA-256.
        pass_hash = hashlib.sha256(password.encode()).hexdigest()

        # Check against the database for correct/incorrect login info:
        if correct_login(username=username, password=pass_hash):
            response['redirect'] = 'admin.html'
            code = OK

            # Create session:
            session['username'] = username

        # Incorrect login credentials:
        else:
            response['err_msg'] = 'Invalid admin username or password.'
            code = FORBIDDEN

    return response, code


# Handles the logout for the admins:
@auth.route('/logout', methods=['GET'])
def logout():
    """Logout handling route.
    This function handles the logout request.

    If username is set in the session, we pop from the session object and
    send response of the username that was in the session and status code OK
    Else, we return a error message stating the user was not logged in and
    status code FORBIDDEN
    """
    response = dict()

    # Only logout if in current session:
    if admin_session():
        response['username'] = session['username']
        session.pop('username', default=None)
        code = OK
        return response, code

    # Cannot logout if not logged in:
    else:
        response['err_msg'] = 'Not logged in'
        code = BAD_REQUEST
        return response, code
