# Header Imports
import json

# Function Defintions

# getters: Input(user) Output(string of item)
def getWeapon(user):
    with open('user.json', 'r+') as file:
        existing_data = json.load(file)
    #print(existing_data['users'])
    user_array = existing_data['users']
    user_index = None
    for x in range(len(user_array)):
        if(existing_data['users'][x]['user']==user):
            user_index = x
            break

    file.close()
    return (existing_data['users'][x]['weapon']['weapon_name'])
def getHelmet(user):
    with open('user.json', 'r+') as file:
        existing_data = json.load(file)
    #print(existing_data['users'])
    user_array = existing_data['users']
    user_index = None
    for x in range(len(user_array)):
        if(existing_data['users'][x]['user']==user):
            user_index = x
            break
    file.close()
    return (existing_data['users'][x]['armor']['helmet']['helmet_name'])
def getChestplate(user):
    with open('user.json', 'r+') as file:
        existing_data = json.load(file)
    #print(existing_data['users'])
    user_array = existing_data['users']
    user_index = None
    for x in range(len(user_array)):
        if(existing_data['users'][x]['user']==user):
            user_index = x
            break
    file.close()
    return (existing_data['users'][x]['armor']['chestplate']['chestplate_name'])
def getLeggings(user):
    with open('user.json', 'r+') as file:
        existing_data = json.load(file)
    #print(existing_data['users'])
    user_array = existing_data['users']
    user_index = None
    for x in range(len(user_array)):
        if(existing_data['users'][x]['user']==user):
            user_index = x
            break
    file.close()
    return (existing_data['users'][x]['armor']['leggings']['leggings_name'])
def getBoots(user):
    with open('user.json', 'r+') as file:
        existing_data = json.load(file)
    #print(existing_data['users'])
    user_array = existing_data['users']
    user_index = None
    for x in range(len(user_array)):
        if(existing_data['users'][x]['user']==user):
            user_index = x
            break
    file.close()
    return (existing_data['users'][x]['armor']['boots']['boots_name'])

# setters: Input(user, string of item to set) Output void
def totalDefense(user):
    with open('user.json', 'r+') as file:
        existing_data = json.load(file)
    file.close()
    user_array = existing_data['users']
    user_index = None
    for x in range(len(user_array)):
        if(existing_data['users'][x]['user']==user):
            user_index = x
            break
        
    existing_data['users'][user_index]['defense'] = existing_data['users'][user_index]['armor']['helmet']['defense'] + existing_data['users'][user_index]['armor']['chestplate']['defense'] + existing_data['users'][user_index]['armor']['leggings']['defense'] + existing_data['users'][user_index]['armor']['boots']['defense']
    json.dump(existing_data, open('user.json', 'w'), indent=4)

    return

def setWeapon(user, weapon):
    with open('user.json', 'r+') as file:
        existing_data = json.load(file)
    file.close()
    user_array = existing_data['users']
    user_index = None
    for x in range(len(user_array)):
        if(existing_data['users'][x]['user']==user):
            user_index = x
            break
        
    existing_data['users'][user_index]['weapon']['weapon_name'] = weapon
    
    with open('../loot/all_items.json', 'r+') as file:
        data = json.load(file)
    file.close()
    damage = None
    num_of_items = len(list(data.values())[0])
    for x in range(num_of_items):
        if((list(data.values())[0][x]['Name']) == weapon ):
            damage = (list(data.values())[0][x]['Damage'])

    existing_data['users'][user_index]['weapon']['weapon_damage'] = damage
    json.dump(existing_data, open('user.json', 'w'), indent=4)

    return
def setHead(user, helmet):
    with open('user.json', 'r+') as file:
        existing_data = json.load(file)
    file.close()
    user_array = existing_data['users']
    user_index = None
    for x in range(len(user_array)):
        if(existing_data['users'][x]['user']==user):
            user_index = x
            break
        
    existing_data['users'][user_index]['armor']['helmet']['helmet_name'] = helmet
    
    with open('../loot/all_items.json', 'r+') as file:
        data = json.load(file)
    file.close()
    defense = None

    num_of_items = len(list(data.values())[2])
    for x in range(num_of_items):
        if((list(data.values())[2][x]['Name']) == helmet ):
            defense = (list(data.values())[2][x]['Defense'])
#fix register_py + user_json before continuing this.
#after this i set, needs to call a diff function to adjust total_defense
    existing_data['users'][user_index]['armor']['helmet']['defense'] = defense
    json.dump(existing_data, open('user.json', 'w'), indent=4)
    totalDefense(user)
    return
def setBody(user, chestplate):
    with open('user.json', 'r+') as file:
        existing_data = json.load(file)
    file.close()
    user_array = existing_data['users']
    user_index = None
    for x in range(len(user_array)):
        if(existing_data['users'][x]['user']==user):
            user_index = x
            break
        
    existing_data['users'][user_index]['armor']['chestplate']['chestplate_name'] = chestplate
    
    with open('../loot/all_items.json', 'r+') as file:
        data = json.load(file)
    file.close()
    defense = None

    num_of_items = len(list(data.values())[3])
    for x in range(num_of_items):
        if((list(data.values())[3][x]['Name']) == chestplate ):
            defense = (list(data.values())[3][x]['Defense'])
#fix register_py + user_json before continuing this.
#after this i set, needs to call a diff function to adjust total_defense
    existing_data['users'][user_index]['armor']['chestplate']['defense'] = defense
    json.dump(existing_data, open('user.json', 'w'), indent=4)
    totalDefense(user)
    return
def setLeg(user, leggings):
    with open('user.json', 'r+') as file:
        existing_data = json.load(file)
    file.close()
    user_array = existing_data['users']
    user_index = None
    for x in range(len(user_array)):
        if(existing_data['users'][x]['user']==user):
            user_index = x
            break
        
    existing_data['users'][user_index]['armor']['leggings']['leggings_name'] = leggings
    
    with open('../loot/all_items.json', 'r+') as file:
        data = json.load(file)
    file.close()
    defense = None

    num_of_items = len(list(data.values())[4])
    for x in range(num_of_items):
        if((list(data.values())[4][x]['Name']) == leggings ):
            defense = (list(data.values())[4][x]['Defense'])
#fix register_py + user_json before continuing this.
#after this i set, needs to call a diff function to adjust total_defense
    existing_data['users'][user_index]['armor']['leggings']['defense'] = defense
    json.dump(existing_data, open('user.json', 'w'), indent=4)
    totalDefense(user)
    return 
def setBoot(user, boots):
    with open('user.json', 'r+') as file:
        existing_data = json.load(file)
    file.close()
    user_array = existing_data['users']
    user_index = None
    for x in range(len(user_array)):
        if(existing_data['users'][x]['user']==user):
            user_index = x
            break
        
    existing_data['users'][user_index]['armor']['boots']['boots_name'] = boots
    
    with open('../loot/all_items.json', 'r+') as file:
        data = json.load(file)
    file.close()
    defense = None

    num_of_items = len(list(data.values())[5])
    for x in range(num_of_items):
        if((list(data.values())[5][x]['Name']) == boots ):
            defense = (list(data.values())[5][x]['Defense'])
#fix register_py + user_json before continuing this.
#after this i set, needs to call a diff function to adjust total_defense
    existing_data['users'][user_index]['armor']['boots']['defense'] = defense
    json.dump(existing_data, open('user.json', 'w'), indent=4)
    totalDefense(user)
    return

#currency manipulation: Input(user, int: amount of money to add) Output void
def addCurrency(user, money):
    with open('user.json', 'r+') as file:
        existing_data = json.load(file)
    file.close()
    user_array = existing_data['users']
    user_index = None
    for x in range(len(user_array)):
        if(existing_data['users'][x]['user']==user):
            user_index = x
            break
        
    existing_data['users'][user_index]['currency'] = existing_data['users'][user_index]['currency'] + money

    json.dump(existing_data, open('user.json', 'w'), indent=4)
    return

# Backpack manipulation
def getBackpack(id):
    with open('user.json', 'r+') as file:
        existing_data = json.load(file)
    #print(existing_data['users'])
    user_array = existing_data['users']
    user_index = None
    for x in range(len(user_array)):
        if(existing_data['users'][x]['id']==id):
            user_index = x
            break

    file.close()
    return (existing_data['users'][x]['backpack'])
def addToBackpack(user, item):
    with open('user.json', 'r+') as file:
        existing_data = json.load(file)
    #print(existing_data['users'])
    user_array = existing_data['users']
    user_index = None
    for x in range(len(user_array)):
        if(existing_data['users'][x]['user']==user):
            user_index = x
            break

    file.close()
    (existing_data['users'][x]['backpack']).append(item)
    json.dump(existing_data, open('user.json', 'w'), indent=4)
    return

#add diff kind of trade
#giving
def trade(user, item, user2, item2 ):
    with open('user.json', 'r+') as file:
        existing_data = json.load(file)
    #print(existing_data['users'])
    user_array = existing_data['users']
    user_index = None
    user2_index = None
    for x in range(len(user_array)):
        if(existing_data['users'][x]['user']==user):
            user_index = x
            break
    for y in range(len(user_array)):
        if(existing_data['users'][y]['user']==user2):
            user2_index = y
            break

    file.close()
    (existing_data['users'][user_index]['backpack']).append(item2)
    (existing_data['users'][user2_index]['backpack']).remove(item2)
    (existing_data['users'][user2_index]['backpack']).append(item)
    (existing_data['users'][user_index]['backpack']).remove(item)
    json.dump(existing_data, open('user.json', 'w'), indent=4)
    return
def equip():
    print('test')
def unequip(id, item):
    with open('user.json', 'r+') as file:
        existing_data = json.load(file)
    user_array = existing_data['users']
    user_index = None
    for x in range(len(user_array)):
        if(existing_data['users'][x]['id']==id):
            user_index = x
            break
    file.close()

    

    if(item=='weapon'):
        (existing_data)['users'][user_index]['backpack'].append( (existing_data)['users'][user_index]['weapon']['weapon_name'] )
        (existing_data)['users'][user_index]['weapon']={
                "weapon_name":"none",
                "weapon_damage": 0
            }
    elif(item=='helmet'):
        (existing_data)['users'][user_index]['backpack'].append( (existing_data)['users'][user_index]['armor']['helmet']['helmet_name'] )
        (existing_data)['users'][user_index]['weapon']['armor']['helmet']={
                "helmet_name": "none",
                "defense": 0
            }
    elif(item=='chestplate'):
        (existing_data)['users'][user_index]['backpack'].append( (existing_data)['users'][user_index]['armor']['chestplate']['chestplate_name'] )
        (existing_data)['users'][user_index]['weapon']['armor']['chestplate']={
                "chestplate_name": "none",
                "defense": 0
            }
    elif(item=='leggings'):
        (existing_data)['users'][user_index]['backpack'].append( (existing_data)['users'][user_index]['armor']['leggings']['leggings_name'] )
        (existing_data)['users'][user_index]['weapon']['armor']['leggings']={
                "leggings_name": "none",
                "defense": 0
            }
    else:
        (existing_data)['users'][user_index]['backpack'].append( (existing_data)['users'][user_index]['armor']['boots']['boots_name'] )
        (existing_data)['users'][user_index]['weapon']['armor']['boots']={
                "boots_name": "none",
                "defense": 0
            }
    json.dump(existing_data, open('user.json', 'w'), indent=4)
    return

#def delete_from_backpack

    

def main():
    # print(getWeapon('dummy'))
    # print(getHelmet('dummy'))
    # print(getChestplate('dummy'))
    # print(getLeggings('dummy'))
    # print(getBoots('dummy'))

    # setWeapon('dummy', 'Frost Sword')

    #setHead('dummy', 'Dragon Skin Helmet')
    #setBody('dummy', 'Dragon Skin Chestplate')
    #setLeg('dummy', 'Dragon Skin Leggings')
    #setBoot('dummy', 'Dragon Skin Boots')

    #addCurrency('dummy', 100)

    #print(getBackpack('dummy'))
    #addToBackpack('dummy','test4')
    #trade('dummy', 'test1', 'dummy2', 'test5')
    #unequip('dummy', 'weapon')
    print('test')

if __name__ == "__main__":
    main()