from sqlalchemy import func

from sixthworldsprawl.app import db, Character


def create_character(character_json):
    """
    Creates a Character from the JSON data passed in

    JSON Keys:
    ==========
    name: String (32)
    bio: String (2048)
    race: String (32)
    gender: String (32)
    status: String (64)

    -> Character()
    """
    name = character_json['name']
    bio = character_json['bio']
    race = character_json['race']
    gender = character_json['gender']
    status = character_json['status']

    character = Character(name=name, bio=bio, race=race, gender=gender, status=status)

    db.session.add(character)
    db.session.commit()

    return character


def get_character(character_id):
    """
    Gets a single Character from the database specified by the character_id

    Parameters:
    ===========
    character_id: int

    -> Character or None
    """

    character = Character.query.filter_by(id=character_id).first()

    return character


def edit_character(character_id, character_json):
    """
    Edits the Character to match the character_json

    Parameters:
    ===========
    character_id: int

    JSON Keys:
    ==========
    name: String (32)
    bio: String (2048)
    race: String (32)
    gender: String (32)
    status: String (64)

    -> Character or None
    """

    character = get_character(character_id)
    if not character:
        return None

    character.name = json_helper(character_json, "name", character.name)
    character.bio = json_helper(character_json, "bio", character.bio)
    character.race = json_helper(character_json, "race", character.race)
    character.gender = json_helper(character_json, "gender", character.gender)
    character.status = json_helper(character_json, "status", character.status)

    db.session.commit()

    return character


def delete_character(character_id):
    """
    Deletes the Character passed in specified by the character_id

    Parameters:
    ==========
    character_id: int

    -> None
    """

    character = get_character(character_id)

    db.session.delete(character)
    db.session.commit()


def random_character():
    """
    Gets a random Character from the database

    -> Character
    """

    return Character.query.order_by(func.random()).first()


def json_helper(json, key, default):
    try:
        return json[key]
    except KeyError:
        return default


def get_bulk(character_limit):
    """
    Creates a multi character object that has x amount of characters in it.
    Currently starts at the beginning of the database;

    Parameters
    ==========
    characer_limit: int

    -> Character(s) JSON
    """
    characters = Character.query.order_by(Character.id.asc).yield_per(character_limit)
    return characters


def get_all():
    """
    Creates a multi character object that has all the characters in the database

    -> Character(s) JSON
    """
    characters = Character.query.all()
    return characters
