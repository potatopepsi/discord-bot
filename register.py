import json
 
def appendJson(new):
    with open('user.json', 'r+') as file:
        existing_data = json.load(file)

        existing_data["users"].append(new)

        file.seek(0)

        json.dump(existing_data, file, indent = 4)

def new_user(id, name):
    # ADD IN HP 

    #Fix helmet, body, leg, boot into weapon format
    #Do defense of each item
    #after each item is set in inventory then update total defense by re-adding all the defense
    new_user_data = {
        "id": id,
        "user": name,
            "weapon": {
                "weapon_name":"none",
                "weapon_damage": 0
            },
            "armor": {
                "helmet":{
                    "helmet_name": "none",
                    "defense": 0
                },
                "chestplate":{
                    "chestplate_name": "none",
                    "defense": 0
                },
                "leggings":{
                    "leggings_name": "none",
                    "defense": 0
                },
                "boots":{
                    "boots_name": "none",
                    "defense": 0
                }
            },
            "defense": 0,
            "class":"none",
            "hp":100,
            "backpack":[],
            "currency": 0,
            "level": 1,
            "exp": 0
    }
    appendJson(new_user_data)

def main():
    new_user(0,'sleep')

if __name__ == "__main__":
    main()
