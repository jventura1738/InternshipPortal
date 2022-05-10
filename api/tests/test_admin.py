# Justin Ventura

'''
This module contains the tests for the Admin routes.

How to test: `python3 -m pytest -s api/tests/test_admin.py`
OR
`python3 -m pytest -s api/tests/`
'''

# Database:
from api.models import (
    db, UsersModel, ListingsModel, ClientsModel,
    TagsModel, Listings_TagsModel, CoursesModel, Listings_CoursesModel
)

# Constants:
from api.constants import OK, BAD_REQUEST, FORBIDDEN

# From other tests:
from conftest import db_reset
from test_auth import login, logout
from testing_data import (
    tags, courses, hash,
    usersInfo, adminListingInfo, clientsInfo
)

# -----------------------------------------------------------------
#                        Admin Tests
# -----------------------------------------------------------------


# Prepare the database:
def initialize_data():
    '''This is a function to add:

    Admin info
    listing with courses & tags.
    '''
    db_reset()
    # Admin:
    user = UsersModel(username=usersInfo[0]['username'],
                      email=usersInfo[0]['email'],
                      password=hash(usersInfo[0]['password']),
                      is_admin=usersInfo[0]['is_admin'])
    db.session.add(user)
    db.session.commit()

    amazon = ClientsModel(**clientsInfo[0])
    db.session.add(amazon)
    db.session.commit()

    listing = ListingsModel(**adminListingInfo[0])
    db.session.add(listing)
    db.session.commit()

    tag1, tag2, tag3 = TagsModel(tags[0]), TagsModel(
        tags[1]), TagsModel(tags[2])
    db.session.add(tag1)
    db.session.add(tag2)
    db.session.add(tag3)
    db.session.commit()

    course1, course2 = CoursesModel(**courses[0]), CoursesModel(**courses[1])
    db.session.add(course1)
    db.session.add(course2)
    db.session.commit()

    listing_tag = Listings_TagsModel(l_id=1, t_id=1)
    listing_course = Listings_CoursesModel(l_id=1, c_id=1)
    db.session.add(listing_tag)
    db.session.add(listing_course)
    db.session.commit()


# Test the star listing route:
def test_star_listing(client):
    '''
    This test checks that the star listing form works correctly.

    Routes:
        /admin/star-listing
    '''
    # ------------------------------ TEST 1 ------------------------------
    invalid_put1 = client.put('/admin/star-listing/1')
    assert invalid_put1.status_code == FORBIDDEN, 'Non-admin succeeded.'

    # ------------------------------ TEST 2 ------------------------------
    initialize_data()
    valid_put1 = login(client, usersInfo[0]
                       ['username'], usersInfo[0]['password'])
    assert valid_put1.status_code == OK, 'Login failed.'

    # Data for the PUT request:
    data = {
        'listing_id': 1
    }

    # Make the request to star:
    response = client.put('/admin/star-listing/1',
                          json=data,
                          follow_redirects=True)
    assert response.status_code == OK, 'Star listing failed.'
    assert response.json['listing']['starred'] is True, 'Star listing failed.'

    # Unstar listing:
    data = {
        'listing_id': 1
    }
    response = client.put('/admin/star-listing/1',
                          json=data,
                          follow_redirects=True)
    assert response.status_code == OK, 'Unstar listing failed.'
    assert response.json['listing']['starred'] is False, 'Unstar listing failed.'

    # Logout:
    logout(client)


# Test the edit listing route:
def test_edit_listing(client):
    '''Test to be sure that the edit listing route works.

    Modify the current listing from adminListingInfo[0] to
    adminListingInfo[1].'''
    # ------------------------------ TEST 1 ------------------------------
    invalid_put1 = client.put('/admin/edit-listing/1')
    assert invalid_put1.status_code == FORBIDDEN, 'Non-admin succeeded.'

    # ------------------------------ TEST 2 ------------------------------
    initialize_data()
    valid_get1 = login(client, usersInfo[0]
                       ['username'], usersInfo[0]['password'])
    assert valid_get1.status_code == OK, 'Login failed.'

    # Data for the PUT request:
    data = adminListingInfo[1]
    valid_put = client.put('/admin/edit-listing/1',
                           json=data,
                           follow_redirects=True)
    assert valid_put.status_code == OK, 'Edit listing failed.'
    assert valid_put.json['listing']['status'] == data['status'], 'Edit listing failed.'


# Test to ensure that courses in database work:
def test_get_all_courses(client):
    '''Use the admin/get-all-courses route to ensure that the two
    courses pop up:
        - COSC425, COSC426
    '''
    # ------------------------------ TEST 1 ------------------------------
    invalid_get1 = client.get('/admin/get-all-courses')
    assert invalid_get1.status_code == FORBIDDEN, 'Non-admin succeeded.'

    # ------------------------------ TEST 2 ------------------------------
    initialize_data()
    valid_get1 = login(client, usersInfo[0]
                       ['username'], usersInfo[0]['password'])
    assert valid_get1.status_code == OK, 'Login failed.'

    response = client.get('/admin/get-all-courses')
    assert response.status_code == OK, 'Get all courses failed.'
    assert len(response.json['courses']) == 2, 'Get all courses failed.'
    assert response.json['courses'][0]['course_num'] == courses[0]['course_num'], 'Get all courses failed 1.'
    assert response.json['courses'][1]['course_num'] == courses[1]['course_num'], 'Get all courses failed 2.'


# Test to ensure that tags in database work:
def test_get_all_tags(client):
    '''Use the admin/get-all-tags route to ensure that the three
    tags pop up:
        - Python, JavaScript, PostgreSQL'''
    # ------------------------------ TEST 1 ------------------------------
    invalid_get1 = client.get('/admin/get-all-tags')
    assert invalid_get1.status_code == FORBIDDEN, 'Non-admin succeeded.'

    # ------------------------------ TEST 2 ------------------------------
    initialize_data()
    valid_get1 = login(client, usersInfo[0]
                       ['username'], usersInfo[0]['password'])
    assert valid_get1.status_code == OK, 'Login failed.'

    response = client.get('/admin/get-all-tags')
    assert response.status_code == OK, 'Get all tags failed.'
    assert len(response.json['tags']) == 3, 'Get all tags failed.'
    assert response.json['tags'][0] == tags[0], 'Get all tags failed 1.'
    assert response.json['tags'][1] == tags[1], 'Get all tags failed 2.'
    assert response.json['tags'][2] == tags[2], 'Get all tags failed 3.'
