# Justin Ventura

'''This module is for testing the view routes'''


# Test the root of the website:
def test_root(client):
    '''
    This test checks that the root route works correctly.
    '''
    # Send the request:
    response = client.get('/')

    # Check the response:
    assert response.status_code == 200


# Test the admin route:
def test_admin(client):
    '''
    This test checks that the admin route works correctly.
    '''
    # Send the request:
    response = client.get('/admin')

    # Check the response:
    assert response.status_code == 200


# Test the admin listings route:
def test_admin_listings(client):
    '''
    This test checks that the admin listings route works correctly.
    '''
    # Send the request:
    response = client.get('/admin/listings')

    # Check the response:
    assert response.status_code == 200


# Test the listing route:
def test_listing(client):
    '''
    This test checks that the listing route works correctly.
    '''
    # Send the request:
    response = client.get('/listing')

    # Check the response:
    assert response.status_code == 200


# Test the browse route:
def test_route_browse(client):
    '''
    This test checks that the browse route works correctly.
    '''
    # Send the request:
    response = client.get('/browse')

    # Check the response:
    assert response.status_code == 200


# Test the admin edit listing route:
def test_admin_edit_listing(client):
    '''
    This test checks that the admin edit listing route works correctly.
    '''
    # Send the request:
    response = client.get('/admin/edit/listing')

    # Check the response:
    assert response.status_code == 200


# Test the login route:
def test_login(client):
    '''
    This test checks that the login route works correctly.
    '''
    # Send the request:
    response = client.get('/login')

    # Check the response:
    assert response.status_code == 200


# Test the contact route:
def test_contact(client):
    '''
    This test checks that the contact route works correctly.
    '''
    # Send the request:
    response = client.get('/contact')

    # Check the response:
    assert response.status_code == 200


# Test the insert listing route:
def test_insert_listing(client):
    '''
    This test checks that the insert listing route works correctly.
    '''
    # Send the request:
    response = client.get('/insert-listing')

    # Check the response:
    assert response.status_code == 200


# Test the reset password auth route:
def test_reset_password_auth(client):
    '''
    This test checks that the reset password auth route works correctly.
    '''
    # Send the request:
    response = client.get('/login/reset-password-auth')

    # Check the response:
    assert response.status_code == 200


# Test the reset password route:
def test_reset_password(client):
    '''
    This test checks that the reset password route works correctly.
    '''
    # Send the request:
    response = client.get('/login/reset-password')

    # Check the response:
    assert response.status_code == 200


# Test the admin contact inbox route:
def test_admin_contact_inbox(client):
    '''
    This test checks that the admin contact inbox route works correctly.
    '''
    # Send the request:
    response = client.get('/admin/contactinbox')

    # Check the response:
    assert response.status_code == 200


# Test the admin notification page route:
def test_admin_notification_page(client):
    '''
    This test checks that the admin notification page route works correctly.
    '''
    # Send the request:
    response = client.get('/admin/notificationpage')

    # Check the response:
    assert response.status_code == 200


# Test the admin view message route:
def test_admin_view_message(client):
    '''
    This test checks that the admin view message route works correctly.
    '''
    # Send the request:
    response = client.get('/admin/view/message')

    # Check the response:
    assert response.status_code == 200
