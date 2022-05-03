# Justin Ventura

"""
Routes module for general routes in api.
"""

from flask import Blueprint, request

from .models import CoursesModel, Listings_TagsModel, ListingsModel, ClientsModel, TagsModel
from .models import db, ListingsStatisticsModel, Listings_CoursesModel
from .constants import LISTING_STATUSES
from .constants import OK, BAD_REQUEST, NOT_FOUND

routes = Blueprint('routes', __name__)

# ------------------------------------------------------------------------
#          ADMIN ROUTES: these routes are all for the admin
# ------------------------------------------------------------------------


# Route to get statistics on a given listing:
@routes.route('/get-statistics/<listing_id>', methods=['GET'])
def get_listing_stats(listing_id: int):
    """
    Route to get statistics on a given listing.
    """
    # Get the listing:
    response = dict()

    listing_stats = ListingsStatisticsModel.query.filter_by(listing_id=listing_id)\
        .first()

    # If the listing doesn't exist, return 404:
    if not listing_stats:
        response['err_msg'] = 'Listing not found.'
        code = NOT_FOUND
        return response, code

    # Return the statistics for the listing:
    response['views'] = listing_stats.views
    response['applications'] = listing_stats.applications
    code = OK
    return response, code


# Route to modify the statistics on a given listing:
@routes.route('/modify-statitics/<listing_id>', methods=['PUT'])
def modify_listing_stats(listing_id: int):
    """
    Route to modify the statistics on a given listing.
    """
    # Get the listing:
    response = dict()
    data = request.json
    listing_stats = ListingsStatisticsModel.query.filter_by(id=listing_id)\
        .first()

    # If the listing doesn't exist, return 404:
    if not listing_stats:
        response['err_msg'] = 'Listing not found.'
        code = NOT_FOUND
        return response, code

    # Get the new values:
    statistic_to_increment = data['statistic']

    if statistic_to_increment == 'views':
        listing_stats.views += 1

    elif statistic_to_increment == 'applications':
        listing_stats.applications += 1

    else:
        response['err_msg'] = 'Invalid statistic.'
        code = BAD_REQUEST
        return response, code

    # Save the changes:
    db.session.commit()

    # Return the statistics for the listing:
    code = OK
    return response, code


# Route to get all listings with the given status.
@routes.route('/get-listings/<status>', methods=['GET'])
def get_listings(status: str = 'all'):
    """Route returns json payload of all <status> listings:

    JSON payload format:
    {
        'i': {
            'client': client_name,
            'listing': {
                'id': listing.id,
                'client_id': client_id,
                'position': position,
                'pos_responsibility': pos_responsibility,
                'min_qualifications': min_qualifications,
                'pref_qualifications': pref_qualifications,
                'additional_info': additional_info,
                'status': status,
                'starred': starred,
            }
            'tags': [tag1, tag2, ...],
            'courses': [course1, course2, ...]
        }
    }
    """
    response = dict()

    # Handle possible listing statuses:
    listings = list()

    # All statuses:
    if status == 'all':
        listings = ListingsModel.query.order_by(ListingsModel.status)

    # Query for one of the four statuses:
    elif status in LISTING_STATUSES:
        listings = ListingsModel.query.filter_by(status=status).all()

    # Invalid listings request:
    else:
        response['err_msg'] = 'Invalid listings request.'
        return response, BAD_REQUEST

    # Valid listing request:
    if listings is not None:
        code = OK
        # For all pending listings, create a payload for each one:
        for i, listing in enumerate(listings):

            # Use foreign key to get client name via client_id:
            client = ClientsModel.query.filter_by(id=listing.client_id).first()
            client_name = client.client_name

            # Use foreign key to get tags via listing_id:
            listings_tags = Listings_TagsModel.query.\
                filter_by(listing_id=listing.id).all()

            listings_courses = Listings_CoursesModel.query.\
                filter_by(listing_id=listing.id).all()

            # Create a list of tags using Listings_Tags Relation:
            tags = list()
            for listings_tag in listings_tags:
                tag = TagsModel.query.filter_by(id=listings_tag.tag_id)\
                    .first()
                tags.append(tag.tag_title)

            # Create a list of tags using Listings_Courses Relation:
            courses = list()
            for listings_course in listings_courses:
                course = CoursesModel.query.filter_by(id=listings_course.id).\
                    first()
                courses.append(course.course_num)

            # Create payload for each listing:
            response[i] = {
                'client': client_name,
                'listing': listing.to_dict(),
                'tags': tags,
                'courses': courses,
            }

    # No listings found.
    else:
        response['err_msg'] = 'No listings found.'
        code = OK

    return response, code


# Route to get a singular listing with given id.
@routes.route('/get-listing/<id>', methods=['GET'])
def get_listing(id: int):
    """Get a singular listing with the given id

    JSON payload format:
        'listing': {
            'id': listing.id,
            'client_id': client_id,
            'position': position,
            'pos_responsibility': pos_responsibility,
            'min_qualifications': min_qualifications,
            'pref_qualifications': pref_qualifications,
            'additional_info': additional_info,
            'status': status,
            'starred': starred,
        }
        'tags': [tag1, tag2, ...],
        'courses': [course1, course2, ...]
    }
    """
    response = dict()

    # If the listing exists, create a payload:
    if listing := ListingsModel.query.filter_by(id=id).first():

        # Use foreign key to get tags via listing_id:
        listings_tags = Listings_TagsModel.query.\
            filter_by(listing_id=listing.id).all()

        listings_courses = Listings_CoursesModel.query.\
            filter_by(listing_id=listing.id).all()

        # Create a list of tags using Listings_Tags Relation:
        tags = list()
        for listings_tag in listings_tags:
            tag = TagsModel.query.filter_by(id=listings_tag.tag_id).first()
            tags.append(tag.tag_title)

        # Create a list of tags using Listings_Courses Relation:
        courses = list()
        for listings_course in listings_courses:
            course = CoursesModel.query.filter_by(id=listings_course.id).\
                first()
            courses.append(course.course_num)

        # Create payload for the listing:
        response['listing'] = listing.to_dict()
        response['tags'] = tags
        response['course'] = courses
        code = OK

    # If the listing does not exist, return a 404:
    else:
        response['err_msg'] = f'Listing with id: {id} not found.'
        code = NOT_FOUND  # Error NOT_FOUND so we can add a page for this.

    return response, code


# Route to get client information
@routes.route('/get-client/<id>', methods=['GET'])
def get_client(id: int):
    """Get a singular client with the given id"""
    response = dict()

    # If the client exists, create a payload:
    if client := ClientsModel.query.filter_by(id=id).first():
        response['client'] = client.to_dict()
        code = OK

    # If the client does not exist, return a 404:
    else:
        response['err_msg'] = f'Client with id: {id} not found.'
        code = NOT_FOUND  # Error NOT_FOUND so we can add a page for this.

    return response, code
