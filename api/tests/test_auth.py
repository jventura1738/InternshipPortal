# Justin Ventura


'''
This module contains the tests for the auth routes.

How to test: `python3 -m pytest -s api/tests/test_auth.py`
OR
`python3 -m pytest -s api/tests/`
'''


# Imports for the database:
from api.models import db, UsersModel
from api.constants import OK, BAD_REQUEST, FORBIDDEN

# Imports for the test app:
from testing_data import usersInfo
from conftest import db_reset


# Helper to login
def login(client, username, password):
    '''
    This helper function handles the login requests.
    '''
    data = {
        'username': username,
        'password': password
    }
    return client.post('/login-submit',
                       json=data,
                       follow_redirects=True)


# Helper to logout:
def logout(client):
    '''
    This helper function handles the logout requests.
    '''
    return client.get('/logout',
                      follow_redirects=True)


# Unit test for login/logout functionality:
def test_login_logout(client):
    '''
    This test checks that the login form works correctly.

    Routes:
        /login-submit
        /logout
    '''
    db_reset()
    # Add user to the database:
    user = UsersModel(username=usersInfo[0]['username'],
                      email=usersInfo[0]['email'],
                      password=usersInfo[0]['password'],
                      is_admin=usersInfo[0]['is_admin'])
    db.session.add(user)
    db.session.commit()

    # Test that the login form works correctly:
    # ------------------------------ TEST 1 ------------------------------
    valid_login = login(client, 'jventura3', 'justinventura426')
    assert valid_login.status_code == OK, 'Correct login failed.'

    valid_logout = logout(client)
    assert valid_logout.status_code == OK, 'Valid Logout failed.'

    # ------------------------------ TEST 2 -------------------------------
    invalid_login1 = login(client, 'jventura3', 'justinventura')
    invalid_login2 = login(client, 'joemomma', 'justinventura')
    invalid_login3 = login(client, None, 'justinventura')
    invalid_login4 = login(client, 'jventura3', None)

    assert invalid_login1.status_code == FORBIDDEN,\
        'Invalid password test succeeded.'
    assert invalid_login2.status_code == FORBIDDEN,\
        'Invalid username test succeeded.'
    assert invalid_login3.status_code == FORBIDDEN,\
        'Missing username test succeeded.'
    assert invalid_login4.status_code == FORBIDDEN,\
        'Missing password test succeeded.'

    # ------------------------------ TEST 3 -------------------------------
    invalid_logout = logout(client)
    assert invalid_logout.status_code == BAD_REQUEST,\
        'Invalid logout succeeded.'
