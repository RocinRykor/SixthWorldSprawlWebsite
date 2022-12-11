from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash

db = SQLAlchemy()

class User(db.Model, UserMixin):
    """
    | id:            The primary key for the user
    | username:      A string containing the user's login name
    | password:      A password hashed with werkzeug.generate_password_hash
    | email:         A string containing the user's email address
    | is_admin:      A boolean determining whether or not the user is an admin
    | authenticated: Whether or not the user has logged in.
    | display_name:  The name that will show up for the user in situations like player info
    | bio:           User's customizable bio
    | characters:    Links a user to their characters
    """

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32))
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False)
    authenticated = db.Column(db.Boolean, default=False)
    display_name = db.Column(db.String(32))
    characters = db.relationship('Character', back_populates='user', lazy=True)

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

class Character(db.Model):
    """
    | id:           The primary key for the player
    | player_id:    Link to an existing user
    | name:         A string containing the character's name
    | bio:          A short decription of the player
    | race:         Character Race
    | gender:       Character's gender
    | status:       A short decription of the character's in-game status
    """
    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    player = db.relationship("User", back_populates("characters"), lazy=True)
    name = db.Column(db.String(32))
    bio = db.Column(db.String(2048))
    race = db.Column(db.String(32))
    gender = db.Column(db.String(32))
    status = db.Column(db.String(64))

    def jsonify(self):
        """
        Returns the character as a JSON object

        -> JSON Object
        """

        return {
            "id": self.id,
            "player_id": self.player_id,
            "name": self.name,
            "bio": self.bio,
            "race": self.race,
            "gender": self.gender,
            "status": self.status,
        }

# class Request(db.Model):
#     __tablename__ = "request"
#
#     index = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     response_time = db.Column(db.Float)
#     date = db.Column(db.DateTime)
#     method = db.Column(db.String(128))
#     size = db.Column(db.Integer)
#     status_code = db.Column(db.Integer)
#     path = db.Column(db.String(128))
#     user_agent = db.Column(db.String(128))
#     remote_address = db.Column(db.String(128))
#     exception = db.Column(db.String(128))
#     referrer = db.Column(db.String(128))
#     browser = db.Column(db.String(128))
#     platform = db.Column(db.String(128))
#     mimetype = db.Column(db.String(128))
