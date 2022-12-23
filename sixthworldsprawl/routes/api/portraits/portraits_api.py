from sixthworldsprawl.app import db, Portrait
from flask_login import current_user
from sqlalchemy import func

def create_portrait(portrait_json):
    """
    JSON Keys:
    ==========
    filename: String (64)

    -> Portrait()
    """

    portrait = Portrait(filename=filename)

    db.session.add(portrait)
    db.session.commit()

    return portrait

def get_portrait(portrait_id):
    """
    Gets a single portrait from the database specified by the portrait_id

    Parameters:
    ===========
    portrait_id: int

    -> portrait or None
    """

    portrait = Portrait.query.filter_by(id=portrait_id).first()
    
    return portrait

def get_all():
    """
    Creates a multi portrait object that has all the portraits in the database

    -> portrait(s) JSON
    """
    portraits = Portrait.query.all()
    return portraits