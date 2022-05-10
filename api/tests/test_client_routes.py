# Justin Ventura

'''
This module contains the tests for the client routes.

How to test: `python3 -m pytest -s api/tests/test_client_routes.py`
OR
`python3 -m pytest -s api/tests/`
'''

# Imports for database:
from api.constants import OK, BAD_REQUEST, NOT_FOUND

# Imports for database:
from api.models import db, ClientsModel
from testing_data import clientsInfo
from conftest import db_reset


# Add a client to the database:
def add_client_to_database(_client):
    '''
    This helper function to add a client to the database.
    '''
    _client = ClientsModel(**_client)
    db.session.add(_client)
    db.session.commit()


# -----------------------------------------------------------------
#                        Clients Tests
# -----------------------------------------------------------------

# Test the get client by ID
def test_get_client_by_id(client):
    '''
    This test checks that the client get route works correctly.
    '''
    db_reset()
    # Test that this route works correctly:
    # ------------------------------ TEST 1 ------------------------------
    for id, clientInfo in enumerate(clientsInfo):
        add_client_to_database(clientInfo)
        valid_get = client.get(f'/get-client/{id+1}')
        assert valid_get.status_code == OK, 'Valid client failed.'
