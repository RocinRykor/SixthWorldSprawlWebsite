import sys

def group_by_player(characters):
    character_dict = {}

    for character in characters:
        player = character.player_id
        if player in character_dict:
            print(character, file=sys.stdout)
        else:
            character_dict[player] = []
        
        character_dict.get(player).append(character)

    return character_dict