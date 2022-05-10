# Justin Ventura

"""
This module is for the database models.
"""

# Imports for database ORM:
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

# Import constants:
from .constants import MAX_CREDENTIAL_LEN, DEFAULT_LISTING_STATUS as DEFAULT

# Prepare for wrapping:
db = SQLAlchemy()


# Users Models Class:
class UsersModel(db.Model, SerializerMixin):
    """This is the model for users in the database.

    For now, this only contains admin information.
    """
    __tablename__ = 'users'

    # Serialization rules:
    serialize_only = ('id', 'username', 'email', 'is_admin')
    serialize_rules = ('-password')

    # Table attributes:
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(MAX_CREDENTIAL_LEN))
    email = db.Column(db.String(MAX_CREDENTIAL_LEN))
    password = db.Column(db.String(MAX_CREDENTIAL_LEN))
    is_admin = db.Column(db.Boolean, default=False)

    # Constructor:
    def __init__(self, username: str, email: str, password: str,
                 is_admin: bool = False):
        self.username = username
        self.email = email
        self.password = password
        self.is_admin = is_admin

    # Readable representation:
    def __str__(self):
        return f'User {self.username}'

    # Representation for debugging:
    def __repr__(self):
        return f'<User ({self.id}) {self.username} is_admin: {self.is_admin}\
            email: {self.email}, \
            password hash: {self.password}>'


# Courses Models Class:
class CoursesModel(db.Model, SerializerMixin):
    """This is the model for the courses."""
    __tablename__ = 'courses'

    # Serialization rules:
    serialize_only = ('id', 'course_num', 'course_title')

    # Table attributes:
    id = db.Column(db.Integer, primary_key=True)
    course_num = db.Column(db.String(10))
    course_title = db.Column(db.String(255))

    def __init__(self, course_num: str, course_title: str):
        self.course_num = course_num
        self.course_title = course_title

    def __repr__(self):
        return f'<Course {self.course_num}, \
            title: {self.course_title}>'


# Model for linking courses to listings.
class Listings_CoursesModel(db.Model, SerializerMixin):
    """This is the model for the courses."""
    __tablename__ = 'listings_courses'

    # Serialization rules:
    serialize_only = ('id', 'listing_id', 'course_id')

    # Table attributes:
    id = db.Column(db.Integer, primary_key=True)
    listing_id = db.Column(db.Integer, db.ForeignKey('listings.id'))
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'))

    def __init__(self, l_id: int, c_id: str):
        self.listing_id = l_id
        self.course_id = c_id

    def __repr__(self):
        return f'<Course {self.course_id}>'


# Clients Models Class:
class ClientsModel(db.Model, SerializerMixin):
    """This is the model for the clients."""
    __tablename__ = 'clients'

    # Serialization rules:
    serialize_only = ('id', 'client_name', 'client_addr', 'client_email')

    # Table attributes:
    id = db.Column(db.Integer, primary_key=True)

    # General Client information:
    client_name = db.Column(db.String(MAX_CREDENTIAL_LEN))
    client_addr = db.Column(db.String(MAX_CREDENTIAL_LEN))
    client_email = db.Column(db.String(MAX_CREDENTIAL_LEN))

    # Constructor:
    def __init__(self, client_name: str, client_addr: str = 'NA',
                 client_email: str = None):
        self.client_name = client_name
        self.client_addr = client_addr
        self.client_email = client_email

    # Representation for debugging:
    def __repr__(self):
        return f'<Client ({self.id}) {self.client_name}>'


# Listings Models Class:
class ListingsModel(db.Model, SerializerMixin):
    """This is the model for the listings."""
    __tablename__ = 'listings'

    # Serialization rules:
    serialize_only = ('id', 'client_id', 'position', 'pos_responsibility',
                      'min_qualifications', 'pref_qualifications',
                      'additional_info', 'status', 'starred', 'duration',
                      'app_open', 'app_close', 'app_link')

    # Table attributes:
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'))
    position = db.Column(db.String(MAX_CREDENTIAL_LEN))
    pos_responsibility = db.Column(db.Text)
    min_qualifications = db.Column(db.Text)
    pref_qualifications = db.Column(db.Text)
    additional_info = db.Column(db.Text)
    duration = db.Column(db.Integer)
    app_open = db.Column(db.Text)
    app_close = db.Column(db.Text)
    app_link = db.Column(db.Text)

    # Status: pending, active, inactive
    status = db.Column(db.String(MAX_CREDENTIAL_LEN))

    # Starred: True or False
    starred = db.Column(db.Boolean, default=False)

    # Constructor:
    def __init__(self, client_id: int, position: str = 'NA',
                 pos_responsibility: str = 'NA',
                 min_qualifications: str = 'NA',
                 pref_qualifications: str = 'NA',
                 additional_info: str = None, status: str = DEFAULT,
                 starred: bool = False, duration: int = 0,
                 app_open: str = None, app_close: str = None, app_link: str = None):
        self.client_id = client_id
        self.position = position
        self.pos_responsibility = pos_responsibility
        self.min_qualifications = min_qualifications
        self.pref_qualifications = pref_qualifications
        self.additional_info = additional_info
        self.status = status
        self.starred = starred
        self.duration = duration  # In weeks.
        self.app_open = app_open
        self.app_close = app_close
        self.app_link = app_link

    # Readable representation:
    def __str__(self):
        return f'Listing {self.id}: {self.position}'

    # Representation for debugging:
    def __repr__(self):
        return f'<Listing {self.id}: {self.position}\
        status: {self.status}, starred: {self.starred}>'


# Model for listings tags.
class TagsModel(db.Model):
    """This is the model for the listing tags"""
    __tablename__ = 'tags'

    # Serialization rules:
    serialize_only = ('id', 'tag_title')

    id = db.Column(db.Integer, primary_key=True)
    tag_title = db.Column(db.String)

    def __init__(self, title: str):
        self.tag_title = title


# Model for linking tags to listings.
class Listings_TagsModel(db.Model):
    """This is the model for listing-tag match table."""
    __tablename__ = 'listings_tags'

    # Serialization rules:
    serialize_only = ('id', 'listing_id', 'tag_id')

    id = db.Column(db.Integer, primary_key=True)
    listing_id = db.Column(db.Integer, db.ForeignKey('listings.id'))
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'))

    def __init__(self, l_id: int, t_id: int):
        self.listing_id = l_id
        self.tag_id = t_id


class ResetTokensModel(db.Model, SerializerMixin):
    """This is the model for tokens in the database"""
    __tablename__ = 'reset_tokens'

    # Serialization rules:
    serialize_only = ('id', 'username', 'email', 'token')

    # Table attributes:
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(MAX_CREDENTIAL_LEN))
    email = db.Column(db.String(MAX_CREDENTIAL_LEN))
    token = db.Column(db.String(MAX_CREDENTIAL_LEN))

    def __init__(self, username: str, email: str,
                 token: str):
        self.username = username
        self.email = email
        self.token = token

    def __repr__(self):
        return f'<ResetToken {self.token}>'


# Model for the Contact Form Messages.
class ContactFormMessage(db.Model, SerializerMixin):
    """This is the model for a contact form messages"""
    __tablename__ = 'contact_form_messages'

    serialize_only = ('id', 'name', 'email', 'message', 'was_seen')

    # Table attributes:
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(MAX_CREDENTIAL_LEN))
    email = db.Column(db.String(MAX_CREDENTIAL_LEN))
    message = db.Column(db.Text)
    was_seen = db.Column(db.Boolean, default=False)

    def __init__(self, name: str, email: str, message: str,
                 was_seen: bool = False):
        self.name = name
        self.email = email
        self.message = message
        self.was_seen = was_seen

    def __repr__(self):
        repr = f'<Message from {self.email} ({self.name}) {self.message}.\
        Seen: {self.was_seen}>'

        return repr


# Database model fo the listings statistics.
class ListingsStatisticsModel(db.Model, SerializerMixin):
    """This is the model for statistics corresponding to the Listings"""

    serialize_only = ('id', 'listing_id', 'views', 'applications')

    # Table attributes:
    id = db.Column(db.Integer, primary_key=True)
    listing_id = db.Column(db.Integer, db.ForeignKey('listings.id'))
    views = db.Column(db.Integer, default=0)  # Listings clicks.
    applications = db.Column(db.Integer, default=0)  # Apply button clicks.

    def __init__(self, listing_id: int, views: int = 0,
                 applications: int = 0):
        self.listing_id = listing_id
        self.views = views
        self.applications = applications

    def __repr__(self):
        repr = f'<ListingStatistics {self.listing_id}>'
        return repr
