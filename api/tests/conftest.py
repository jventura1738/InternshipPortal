# Justin Ventura


'''
This module is for configuring the testing client.
'''


# Python imports:
import pytest

# Import for env file:
from os.path import join, dirname
from dotenv import load_dotenv

# Import the app creation method:
from api import create_app
from api.models import db

# Load in the env file with variables:
dotenv_path = join(dirname(__file__), '../../.env')
load_dotenv(dotenv_path)


# This is to create the test app as client:
@pytest.fixture(autouse=False)
def client():
    '''Create the test client'''
    app = create_app()
    app.app_context().push()
    db_reset()
    return app.test_client()


# Reset the database:
def db_reset():
    '''Reset the database'''
    databases = [
        'users', 'courses', 'listings_courses',
        'clients', 'listings', 'tags', 'listings_tags',
        'reset_tokens', 'contact_form_messages', 'listings_statistics_model'
    ]
    try:
        for database in databases:
            db.session.execute(
                f'TRUNCATE TABLE {database} RESTART IDENTITY CASCADE;')
            db.session.commit()
    except:
        db.session.rollback()
