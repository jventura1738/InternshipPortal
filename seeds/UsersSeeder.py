from flask_seeder import Seeder
from api.models import db, UsersModel
import hashlib  # Using for password hashing (SHA-256)


# All seeders inherit from Seeder
class UsersSeeder(Seeder):
    """
    This is the seeder for the users.  This basically just generates
    data for admins at this point.
    """

    # run() will be called by Flask-Seeder
    def run(self):
        # Create a new Faker and tell it how to create User objects

        admins = [
            {
                'username': 'jventura3',
                'email': 'jventura3@gulls.salisbury.edu',
                'password': self.password_hash('justinventura426'),
                'is_admin': True
            },
            {
                'username': 'jduncan5',
                'email': 'jduncan5@gulls.salisbury.edu',
                'password': self.password_hash('jacobduncan426'),
                'is_admin': True
            },
            {
                'username': 'bmason3',
                'email': 'bmason3@gulls.salisbury.edu',
                'password': self.password_hash('blainemason426'),
                'is_admin': True
            },
            {
                'username': 'jtanderson',
                'email': 'jtanderson@gulls.salisbury.edu',
                'password': self.password_hash('joeanderson426'),
                'is_admin': True
            },
            {
                'username': 'gfranchi',
                'email': 'gfranchi@gulls.salisbury.edu',
                'password': self.password_hash('guliafranchi426'),
                'is_admin': True
            },
            {
                'username': 'mfinnegan1',
                'email': 'mfinnegan1@gulls.salisbury.edu',
                'password': self.password_hash('megfinnegan426'),
                'is_admin': True
            }
        ]
        for admin in admins:
            db.session.add(UsersModel(**admin))
        db.session.commit()

    @staticmethod
    def password_hash(password: str):
        """Returns the hashed password"""
        return hashlib.sha256(password.encode()).hexdigest()
