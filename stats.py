import json

def showstats(id):
    with open('user.json', 'r+') as file:
        existing_data = json.load(file)
    file.close()
    user_array = existing_data['users']
    user_index = None
    for x in range(len(user_array)):
        if(existing_data['users'][x]['id']==id):
            user_index = x
            break
        
    weapon_damage = existing_data['users'][user_index]['weapon']['weapon_damage']
    total_defense = existing_data['users'][user_index]['defense']
    helmet_defense = existing_data['users'][user_index]['armor']['helmet']['defense']
    chestplate_defense = existing_data['users'][user_index]['armor']['chestplate']['defense']
    leggings_defense = existing_data['users'][user_index]['armor']['leggings']['defense']
    boots_defense = existing_data['users'][user_index]['armor']['boots']['defense']
    hp = existing_data['users'][user_index]['hp']
    lvl = existing_data['users'][user_index]['level']
    exp = existing_data['users'][user_index]['exp']

    return [weapon_damage, total_defense, helmet_defense, chestplate_defense, leggings_defense, boots_defense, hp, lvl, exp]
