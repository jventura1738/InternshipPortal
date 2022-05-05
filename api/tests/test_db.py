# Justin Ventura


'''
This module contains the tests for database seeding that
do not have a route.

How to test: `python3 -m pytest -s api/tests/test_db.py`
OR
`python3 -m pytest -s api/tests/`
'''


# Import for the test app:
from testing_data import hash, usersInfo, clientsInfo, listingsInfo


# We will need literally everything from models:
from api.models import db, UsersModel, ClientsModel, ListingsModel

from conftest import db_reset


# -----------------------------------------------------------------
#                        UsersModel Tests
# -----------------------------------------------------------------


# Add a user to the database:
def add_user_to_database(userInfo):
    '''
    This helper function adds a user to the database.

    userInfo is a dictionary with the following keys:
    'username', 'email', 'password'
    '''
    user = UsersModel(**userInfo)
    db.session.add(user)
    db.session.commit()


# Test that users can be added to the database correctly:
def test_users_model_create():
    '''
    This test checks that the UsersModel can be created.
    '''
    db_reset()
    # Create users in database and query them:
    for userInfo in usersInfo:
        add_user_to_database(userInfo)

    for userInfo in usersInfo:
        user = UsersModel.query.filter_by(
            username=userInfo['username']).first()

        # Check that the user was created correctly:
        username_fail_msg = f'{userInfo["username"]} not found in db'
        email_fail_msg = f'{userInfo["email"]} doesn\'t match in db'
        password_fail_msg = f'{userInfo["password"]} doesn\'t match in db'
        admin_fail_msg = f'{userInfo["is_admin"]} doesn\'t match in db'

        # Tests:
        assert user.username == userInfo['username'], username_fail_msg
        assert user.email == userInfo['email'], email_fail_msg
        assert user.password == userInfo['password'], password_fail_msg
        assert user.is_admin == userInfo['is_admin'], admin_fail_msg


# Test that users can be updated from the database correctly:
def test_users_model_update():
    '''
    This test checks that the UsersModel can be updated.

    Assumes that the database is already populated.
    Relies on 'joejoejoe' being in the database.
    '''
    db_reset()
    # Add joejoejoe to the database:
    add_user_to_database(usersInfo[2])

    # Grab the user to be updated
    user = UsersModel.query.filter_by(username='joejoejoe').first()
    assert user is not None, 'joejoejoe not found in db'

    # Update the password:
    user.password = hash('new_password')
    db.session.commit()

    # Check that the password was updated:
    user = UsersModel.query.filter_by(username='joejoejoe').first()
    assert user.password == hash('new_password'), 'Password not updated'


# -----------------------------------------------------------------
#                        ClientsModel Tests
# -----------------------------------------------------------------


# Add a client to the database:
def add_client_to_database(clientInfo):
    '''
    This helper function adds a client to the database.

    clientInfo is a dictionary with the following keys:
    'name', 'address', 'email'
    '''
    client = ClientsModel(**clientInfo)
    db.session.add(client)
    db.session.commit()


# Test that clients can be added to the database correctly:
def test_clients_model_create(client):
    '''
    This test checks that the ClientsModel can be created.
    '''
    db_reset()
    # Create clients in database and query them:
    for clientInfo in clientsInfo:
        add_client_to_database(clientInfo)

    for clientInfo in clientsInfo:
        client = ClientsModel.query.filter_by(
            client_name=clientInfo['client_name']).first()
        assert client is not None, 'Client not found in db.'

        # Check that the client was created correctly:
        name_fail_msg = f'{clientInfo["client_name"]} not found in db'
        addr_fail_msg = f'{clientInfo["client_addr"]} doesn\'t match in db'
        em_fail_msg = f'{clientInfo["client_email"]} doesn\'t match in db'

        # Tests:
        assert client.client_name == clientInfo['client_name'], name_fail_msg
        assert client.client_addr == clientInfo['client_addr'], addr_fail_msg
        assert client.client_email == clientInfo['client_email'], em_fail_msg


# -----------------------------------------------------------------
#                        ListingsModel Tests
# -----------------------------------------------------------------


# Add a listing to the database:
def add_listing_to_database(listingInfo):
    '''
    This helper function adds a listing to the database.

    listingInfo is a dictionary with the following keys:
    'client_id', 'listing_name', 'listing_addr', 'listing_email'
    '''
    listing = ListingsModel(**listingInfo)
    db.session.add(listing)
    db.session.commit()


# Test that listings can be added to the database correctly:
def test_listings_model_create():
    '''
    This test checks that the ListingsModel can be created.
    '''
    db_reset()

    # Create clients in database and query them:
    for clientInfo in clientsInfo:
        add_client_to_database(clientInfo)

    # Create listings in database and query them:
    for listingInfo in listingsInfo:
        add_listing_to_database(listingInfo)

    for listingInfo in listingsInfo:
        listing = ListingsModel.query.filter_by(
            client_id=listingInfo['client_id']).first()

        # Check that the listing was created correctly:
        for key in listingInfo:
            fail_msg = f'{listingInfo["position"]} doesn\'t match in db'
            assert listingInfo[key] == getattr(listing, key), fail_msg
