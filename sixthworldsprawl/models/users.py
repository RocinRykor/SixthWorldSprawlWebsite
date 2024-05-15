from .db import data_base as db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash

class User(db.Model, UserMixin):
    """
    | id:            The primary key for the user
    | username:      A string containing the user's login name
    | password:      A password hashed with werkzeug.generate_password_hash
    | email:         A string containing the user's email address
    | is_admin:      A boolean determining whether the user is an admin
    | authenticated: Whether the user has logged in.
    | display_name:  The name that will show up for the user in situations like player info
    | bio:  A Short description of the player
    | characters:    Links a user to their characters
    """

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32))
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False)
    authenticated = db.Column(db.Boolean, default=False)
    display_name = db.Column(db.String(32))
    bio = db.Column(db.String(2048))
    characters = db.relationship('Character', backref='user', lazy=True)

    def is_authenticated(self):
        return self.authenticated

    @property
    def is_active(self):
        return True

    @property
    def password(self):
        return self.password_hash

    def get_id(self):
        return self.id

    def set_password(self, to_set):
        self.password_hash = generate_password_hash(to_set, method='pbkdf2:sha256',
                                                    salt_length=24)

    def jsonify(self):
        """
        Returns the user as a JSON object

        -> JSON Object
        """

        return {
            "id": self.id,
            "username": self.username,
            "display_name": self.display_name,
            "characters": [character.jsonify() for character in self.characters],
        }
