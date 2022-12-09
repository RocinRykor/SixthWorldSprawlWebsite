from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()


class User(db.Model, UserMixin):
    """
    | id:            The primary key for the user
    | authenticated: Whether or not the user has logged in.
    | password:      A password hashed with werkzeug.generate_password_hash
    | email:         A string containing the user's email address
    | first_name:     A string containing the user's first name
    | last_name:     A string containing the user's last name
    | is_admin:      A boolean determining whether or not the user is an admin
    """
    id = db.Column(db.Integer, primary_key=True)
    authenticated = db.Column(db.Boolean, default=False)
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String(256), nullable=False)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    is_admin = db.Column(db.Boolean, default=False)
    
    def is_authenticated(self):
        return self.authenticated

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def password(self):
        return self.password_hash

    def get_id(self):
        return self.id

    def hash_password(self, password):
        """
        Hashes the password passed in and returns it to the caller.

        | Parameters:
        |     password: unhashed, cleartext string

        | Returns:
        |     password: Hashed password
        """

        password = generate_password_hash(password, method='pbkdf2:sha256',
                                          salt_length=16)

        return password

    @password.setter
    def password(self, password):
        """
        Updates the password on the user model.

        | Parameters:
        |     password: unhashed, cleartext string

        | Returns:
        |     None
        """

        # password = self.hash_password(password)
        self.password_hash = self.hash_password(password)

    def check_password(self, password):
        """
        Checks to see if the password provided matches the current password
        for the user.

        Parameters:

            password: unhashed, cleartext string

        Returns:

            None
        """

        if check_password_hash(self.password_hash, password):
            return True
        return False


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
