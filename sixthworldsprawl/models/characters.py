from .db import data_base as db
from sixthworldsprawl.utils import character_utils

class Character(db.Model):
    """
    | id:           The primary key for the player
    | player_id:    Link to an existing user
    | name:         A string containing the character's name
    | bio:          A short description of the player
    | race:         Character Race
    | gender:       Character's gender
    | status:       A short description of the character's in-game status
    """
    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    name = db.Column(db.String(32))
    bio = db.Column(db.String(2048))
    race = db.Column(db.String(32))
    gender = db.Column(db.String(32))
    status = db.Column(db.String(64))
    portrait_filename = db.Column(db.String(64))
    portrait_id = db.Column(db.Integer, db.ForeignKey('portrait.id'))

    def get_img_url(self):
        return character_utils.get_img(self.portrait_id, self.portrait_filename)

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
            "portrait_id": self.portrait_id,
            "portrait_filename": self.portrait_filename,
        }


class Portrait(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(64))

    def jsonify(self):
        return {
            "id": self.id,
            "filename": self.filename,
        }


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(32))
    category = db.Column(db.String(32))
    description = db.Column(db.String(2048))

    def jsonify(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "category": self.category,
        }


class PortraitTagLinker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    portrait_id = db.Column(db.Integer, db.ForeignKey('portrait.id'))
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'))