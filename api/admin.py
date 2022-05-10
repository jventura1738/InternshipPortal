# Justin Ventura

"""
This module contains routes specifically for the admin.  This
means that the admin must be logged in (session is active) in
order to access these routes.  The requester must of course be
that logged in admin.
"""

# Flask imports:
from flask import Blueprint, request

from .models import CoursesModel, Listings_CoursesModel, Listings_TagsModel, db, ListingsModel, ContactFormMessage, TagsModel
from .constants import LISTING_STATUSES
from .constants import OK, BAD_REQUEST, FORBIDDEN
from .helpers import admin_session


admin = Blueprint('admin', __name__, url_prefix='/admin')


# ------------------------------------------------------------------------
#          ADMIN ROUTES: these routes are all for the admin
# ------------------------------------------------------------------------

# Ensure that client is in admin session:
@admin.before_request
def _admin_session():
    """Runs before all admin routes to check session."""
    if admin_session() is False:
        return {'err_msg': 'ACCESS DENIED.'}, FORBIDDEN


# Route for (un)starring listings.
@admin.route('star-listing/<listing_id>', methods=['PUT'])
def star_listing(listing_id: int):
    """Star a listing

    If a listing is unstarred, star it.
    If a listing is starred, unstar it.
    """
    response = dict()

    # Check if listing is in database, then update and return to Jake:
    if listing := ListingsModel.query.filter_by(id=listing_id).first():
        listing.starred = True if listing.starred is False else False
        db.session.commit()
        response['listing'] = listing.to_dict()
        code = OK

    # Otherwise, return an error message:
    else:
        response['err_msg'] = f'Listing with id {listing_id}\
                                not found in database'
        code = BAD_REQUEST

    return response, code


# Route for editing listings.
@admin.route('edit-listing/<id>', methods=['PUT'])
def edit_listing(id: int) -> None:
    """Edit a listing.

    Replace the existing listing data with the data
    passed in with the request."""
    response = dict()
    data = request.json

    assert data is not None, 'No listing information in PUT request.'

    # If the listing is already in the database:
    if listing := ListingsModel.query.filter_by(id=id).first():

        # Listing information:
        listing.position = data['position_title']
        listing.pos_responsibility = data['pos_responsibility']
        listing.min_qualifications = data['min_qualifications']
        listing.pref_qualifications = data['pref_qualifications']
        listing.additional_info = data['additional_info']
        listing.duration = data['duration']
        listing.app_open = data['app_open']
        listing.app_close = data['app_close']
        listing.app_link = data['app_link']
        listing.status = data['status']

        # Tags:
        tags = data['tags']
        t_ids = []
        for tag in tags:
            t = TagsModel.query.filter_by(tag_title=tag).first()
            t_ids.append(t.id)

        tags_in_db = Listings_TagsModel.query.filter_by(listing_id=id).all()
        # Clear Tags
        for tag in tags_in_db:
            if tag.tag_id not in t_ids:
                db.session.delete(tag)

        # Add Tags
        for t_id in t_ids:
            if t_id not in [t.tag_id for t in tags_in_db]:
                t = Listings_TagsModel(l_id=id, t_id=t_id)
                db.session.add(t)

        # Courses:
        courses = data['su_courses']
        c_ids = []
        for course in courses:
            course = course.split(' - ')[0]
            c = CoursesModel.query.filter_by(course_num=course).first()
            c_ids.append(c.id)

        courses_in_db = Listings_CoursesModel.query.filter_by(
            listing_id=id).all()

        # Clear Courses
        for course in courses_in_db:
            if course.course_id not in c_ids:
                db.session.delete(course)

        # Add Courses
        for c_id in c_ids:
            if c_id not in [c.course_id for c in courses_in_db]:
                c = Listings_CoursesModel(l_id=id, c_id=c_id)
                db.session.add(c)

        # Update the database.
        db.session.commit()
        response['listing'] = listing.to_dict()
        code = OK

    # Invalid listing id:
    else:
        response['err_msg'] = f'Listing with id {id}\
                                not found in database'
        code = BAD_REQUEST

    return response, code


# Route to get all courses.
@admin.route('get-all-courses', methods=['GET'])
def get_all_courses():
    """
    Admin route for receiving all courses
    """

    response = dict()
    courses = []

    for course in CoursesModel.query.all():
        courses.append(course.to_dict())

    response['courses'] = courses
    return response, OK


# Route for getting all tags
@admin.route('get-all-tags', methods=['GET'])
def get_all_tags():
    """
    Admin route for receiving all tags
    """
    response = dict()
    tags = []

    for tag in TagsModel.query.all():
        tags.append(tag.tag_title)

    response['tags'] = tags
    return response, OK


# Route for getting all messages
@admin.route('get-messages/<message_filter>', methods=['GET'])
def get_messages(message_filter: str = 'all'):
    """
    Admin route for receiving messages

    TODO: Test this route and ensure that it works with front end.
    """
    response = dict()
    messages = list()

    # For querying all messages:
    if message_filter == 'all':
        messages = ContactFormMessage.query.order_by(ContactFormMessage.was_seen == True).all()

    # For querying just messages labelled as unseen.
    elif message_filter == 'unseen':
        messages = ContactFormMessage.query.filter_by(was_seen='f').all()

    # Catch incorrect requests.
    else:
        response['err_msg'] = 'Invalid contact form message request'
        return response, BAD_REQUEST

    # Return messages, if there are any.
    if messages is not None:
        code = OK

        for i, message in enumerate(messages):

            response[i] = message.to_dict()

    else:
        response['err_msg'] = 'No messages found.'
        code = OK

    return response, code


# Route to get a singular message with given id.
@admin.route('/get-message/<message_id>', methods=['GET'])
def get_message(message_id: int):
    """Get a singular message with the given id

    JSON payload format:
    {
        "response": {
            'message': {
                'id': message.id,
                'name': message.name,
                'email': message.email,
                'message': message.message,

            }
        }
    }
    }
    """
    response = dict()

    # If the message exists, create a payload:
    if message := ContactFormMessage.query.filter_by(id=message_id).first():
        response['message'] = message.to_dict()
        code = OK

    else:
        response['err_msg'] = f'Message with id: {message_id}\
                                not found in database.'
        code = BAD_REQUEST

    return response, code


# Route for seen/unseen messages
@admin.route('seen_message/<message_id>', methods=['PUT'])
def seen_message(message_id: int):
    """Mark a message as seen

    If a message has been seen, remove dot.
    """
    response = dict()

    # Check if message is in database, if so change the was_seen status to seen
    if message := ContactFormMessage.query.filter_by(id=message_id).first():
        message.was_seen = True
        db.session.commit()
        response['message'] = message.to_dict()
        code = OK

    # Otherwise, return an error message:
    else:
        response['err_msg'] = f'Message with id {message_id}\
                                not found in database'
        code = BAD_REQUEST

    return response, code


@admin.route('delete_message/<message_id>', methods=['DELETE'])
def delete_message(message_id: int):
    """Delete message from database
    """
    response = dict()

    # Check if message is in database, if so delete message
    if message := ContactFormMessage.query.filter_by(id=message_id).first():

        db.session.delete(message)
        db.session.commit()
        response['success_msg'] = f'Message with id {message_id}\
                                removed from database'
        code = OK

    # Otherwise, return an error message:
    else:
        response['err_msg'] = f'Message with id {message_id}\
                                not found in database'
        code = BAD_REQUEST

    return response, code
