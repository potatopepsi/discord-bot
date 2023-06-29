import json

#if they say !attack or !defend auto update current.json

def clear():
    with open('current.json', 'r+') as file:
        existing_data = json.load(file)
    
    file.close()
    #print(existing_data['us[0])
    for x in range(len(existing_data)):
        existing_data.pop(0)

    open("current.json", "w").write(
    json.dumps(existing_data))


def collect(username, move):
    with open('current.json', 'r+') as file:
        existing_data = json.load(file)
    #print(len(existing_data))
    file.close()
    for x in range(len(existing_data)):
        if(existing_data[x]['name']==username):
            existing_data.pop(x)
            break
    open("current.json", "w").write(
    json.dumps(existing_data))


    move_of_player = {
        "name":username,
        "move": move
    }
 
    # Serializing json
    json_object = json.dumps(move_of_player, indent=4)


    with open('current.json', 'r+') as file:
        existing_data = json.load(file)

        existing_data.append(move_of_player)

        file.seek(0)

        json.dump(existing_data, file, indent = 4)
    file.close()

def main():
    # collect("sleep")
    #print("hi")
    collect(123,"attack")
    collect(123,"attack")
    collect(123,"attack")
    collect(123,"attack")
    collect(123,"defend")
    #clear()


if __name__ == "__main__":
    main()