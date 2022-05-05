# Internship Portal Web App
# views.py for API


'''
Clients: Dr. Joseph Anderson, Dr. Giulia Franchi
Team: Blaine Mason, Jacob Duncan, Justin Ventura, Margaret Finnegan
'''


# Flask Imports:
from flask import render_template, Blueprint
from flask import session

# Create views blueprint:
views = Blueprint('views', __name__)

# ------------------------------------------------------------------------
#                                 ROUTES
# ------------------------------------------------------------------------


# Root page route:
@views.route('/')
def root():
    '''Root page view route.
    This function runs whenever the root page (url below) is requested.
        ex) -> localhost:5000/
    Returns the root page: which renders index.html (landing page)
    '''
    return render_template('index.html', page_title='Internship Web \
        Portal Homepage')


# Admin view route:
@views.route('/admin')
def admin():
    '''Admin page view route.
    This function runs whenver the admin page ('/admin') is requested.
        ex) -> localhost:5000/admin
    Returns the admin page: which renders admin.html (admin dashboard)
    '''
    if 'username' in session:
        return render_template('admin/admin.html', page_title='Admin\
             Dashboard')
    else:
        # NOTE: Do we want to return to homepage or somewhere else?
        return root()


# Admin Listings view route:
@views.route('/admin/listings')
def admin_listings():
    '''Admin Listings page view route.
    This function runs whenver the admin page ('/admin/listings')
    is requested.
        ex) -> localhost:5000/admin/listings
    '''
    if 'username' in session:
        return render_template('admin/admin_listings.html', page_title='Admin\
             Dashboard | Listings')
    else:
        # NOTE: Do we want to return to homepage or somewhere else?
        return root()


@views.route('/listing')
def listing():
    '''View individual listing page.
    This function runs whenever the client page ('/listing') is requested.
        ex) -> localhost:5000/listing
    '''
    return render_template('listing.html', page_title='Listing Page')


@views.route('/browse')
def browse():
    '''Browse listings for students.
    This function runs whenver the client page ('/browse') is requested.
        ex) -> localhost:5000/browse
    '''
    return render_template('browse.html', page_title='Browse Listings')


@views.route('/admin/edit/listing')
def admin_edit_listing():
    '''Admin Edit Listing page view route.
    This function runs whenver the admin page ('/admin/edit/listing') is
    requested.
        ex) -> localhost:5000/admin/edit/listing
    '''
    if 'username' in session:
        return render_template('admin/admin_edit_listing.html',
                               page_title='Admin Dashboard | Edit Listing')
    else:
        return root()


# Renders login page for admin:
@views.route('/login', methods=['GET'])
def login():
    '''Login page for admin.
    This function runs whenver the login page ('/login') is requested.
        ex) -> localhost:5000/admin
    Returns the login page: which renders login.html (login form)
    '''
    return render_template('login.html', page_title='Admin Login')


# Renders contact page:
@views.route('/contact', methods=['GET'])
def contact():
    '''Contact page for users.
    This function runs whenver the contact page ('/contact') is requested.
        ex) -> localhost:5000/contact
    Returns the login page: which renders contact.html (contact page)
    '''
    return render_template('contact.html', page_title='Contact Us')


# Renders insert internship page:
@views.route('/insert-listing', methods=['GET'])
def insert_internship():
    '''Insert internship page for users.
    This function runs whenver the insert-listing page ('/insert-listing')
    is requested.
        ex) -> localhost:5000/insert-listing
    Returns the login page: which renders insert_listing.html (insert listing
    page)
    '''
    return render_template('insert_listing.html', page_title='Request\
         Internship Listing')


# Renders reset password form:
@views.route('/login/reset-password-auth', methods=['GET'])
def reset_password_auth():
    '''Reset Password page for users. (Pending Auth)
    This function runs whenever the reset-password page ('/reset-password')
    is requested.
        ex) -> localhost:5000/login/reset-password
    Returns the reset password page: which renders reset.html (reset form)
    '''
    return render_template('reset_password_auth.html',
                           page_title='Reset Password')


@views.route('/login/reset-password', methods=['GET'])
def reset_password():
    '''Reset Password page for users. (Pending Auth)
    This function runs whenever the reset-password page ('/reset-password')
    is requested.
        ex) -> localhost:5000/login/reset-password
    Returns the reset password page: which renders reset.html (reset form)
    '''


@views.route('/admin/contactinbox')
def admin_contact():
    '''Admin Contact Inbox page view route.
    This function runs whenver the admin page ('/admin/contactinbox')
    is requested.
        ex) -> localhost:5000/admin/contactinbox
    '''
    if 'username' in session:
        return render_template('admin/admin_inbox.html', page_title='Admin\
                Dashboard | Contact Inbox')
    else:
        return root()


@views.route('/admin/notificationpage')
def admin_notif():
    '''Admin Notification Page page view route.
    This function runs whenver the admin page ('/admin/notificationpage')
    is requested.
        ex) -> localhost:5000/admin/contactinbox
    '''
    if 'username' in session:
        return render_template('admin/admin_notif.html', page_title='Admin\
                Dashboard | Notification Page')
    else:
        return root()


@views.route('/admin/view/message')
def admin_view_message():
    '''Admin View Message page view route.
    This function runs whenver the admin page ('/admin/view/message') is
    requested.
        ex) -> localhost:5000/admin/view/message
    '''
    if 'username' in session:
        return render_template('admin/admin_view_message.html',
                               page_title='Admin Dashboard | View Message')
    else:
        return root()
