import random
import time
import json
import sys
import loot

def random_hp_normal_mob():
    return random.randint(100, 250)

def random_hp_boss_mob():
    return random.randint(200, 500)

def story():
    mobs = ["Yeti", "Frost Giant", "Winter Wolf"]
    dialogues = ["After months and months of traveling with little to no food, the morale of the group starts to dwindle.", "In the midst of a heavy blizzard, you spot a figure in the distance. Your group calls for help.", "Your group has begun to collect firewood to cook your rations tonight"]
    setting = ["the waters", "behind you", "while you were looking away", "behind a tree"]

    #Chooses random mob
    mobType = mobs[random.randint(0, len(mobs)-1)]

    #Dialogue based on random choices
    #print(dialogues[random.randint(0, 2)])
    storystring = dialogues[random.randint(0, 2)] + ("However, a " + mobType + " appears from " + setting[random.randint(0, len(setting)-1)] + ". It towers over your group, baring its claws.")
    #print("HP: ???")
    
    return storystring
def Normal_Mob():
    #Setup for mobs, dialogue, and setting
    mobs = ["Yeti", "Frost Giant", "Winter Wolf"]
    dialogues = ["After months and months of traveling with little to no food, the morale of the group starts to dwindle.", "In the midst of a heavy blizzard, you spot a figure in the distance. Your group calls for help.", "Your group has begun to collect firewood to cook your rations tonight"]
    setting = ["the waters", "behind you", "while you were looking away", "behind a tree"]

    #Chooses random mob
    mobType = mobs[random.randint(0, len(mobs)-1)]

    #Dialogue based on random choices
    print(dialogues[random.randint(0, 2)])
    print("However, a " + mobType + " appears from " + setting[random.randint(0, len(setting)-1)] + ". It towers over your group, baring its claws.")
    print("HP: ???")

    # Timer for User Interaction
    time.sleep(1)

    with open("current.json", "r") as read_file:
        players = json.load(read_file)

    #Sets Initial HP Based on amount of players
    HP = random_hp_normal_mob()
    if (HP < 150):
        tier = 1
    elif (HP < 200):
        tier = 2
    else:
        tier = 3
    HP *= len(players)

    print("The " + mobType + " targets:")
    for x in range(len(players)):
        print(str(players[x]))
    print("HP: " + str(HP))
 

    #Battle Loop (Rounds 1 through 3) starts here
    for x in range(1, 4):

        print("Round " + str(x) + " begins")

        #Change to 15 later
        time.sleep(1)

        with open("command.json", "r") as read_file:
            commands = json.load(read_file) 

        for y in range(len(commands)):
            if(commands[y].lower() == "attack" or commands[y].lower() == "atk"):
                #HP should decrease by the damage of the weapon/attack, not necessarily 200
                HP-=200
                print("The " + mobType + " now has " + str(HP) + " hp")
            elif(commands[y].lower() == "heal"):
                #heal function
                print("Heal Function")
            elif(commands[y].lower() == "defend" or commands[y].lower() == "def"):
                #defend function
                print("Defend Function")
            else:
                print("ignore")
            
            #Ends the loop if the most recent attack killed it
            if (HP <= 0):
                print("The " + mobType + " was defeated!")
                outcome = "win"
                break

        if (HP <= 0):
            break

        #If loop is never broken, outcome is default to lose
        outcome = "lose"
        
        #Chooses between single-target attack of AoE
        attackChoice = random.randint(1, 2)
        if (attackChoice == 1):
            randomPlayer = players[random.randint(0, len(players) - 1)]
            print("The " + mobType + " attacks party member " + randomPlayer)
        else:
            print("The " + mobType + " hits every member in your party!")

    if(outcome == "win"):
        #loot.loot(1)
        print("Won, LootTest")
    else:
        print("You have lost")

def Boss_Mob():
    #Setup for mobs, dialogue, and setting
    mobs = ["Frost Salamander", "Ice Troll", "White Dragon"]
    dialogues = ["After months and months of traveling with little to no food, the morale of the group starts to dwindle.", "In the midst of a heavy blizzard, you spot a figure in the distance. Your group calls for help.", "Your group has begun to collect firewood to cook your rations tonight"]
    setting = ["the waters", "behind you", "while you were looking away", "behind a tree"]

    #Chooses random mob
    mobType = mobs[random.randint(0, len(mobs)-1)]

    #Dialogue based on random choices
    print(dialogues[random.randint(0, 2)])
    print("However, a " + mobType + " appears from " + setting[random.randint(0, len(setting)-1)] + ". It towers over your group, baring its claws.")
    print("HP: ???")

    # Timer for User Interaction
    time.sleep(1)

    with open("current.json", "r") as read_file:
        players = json.load(read_file)

    #Sets Initial HP Based on amount of players
    HP = random_hp_boss_mob()
    if (HP < 350):
        tier = 4
    else:
        tier = 5
    HP *= len(players)

    print("The " + mobType + " targets:")
    for x in range(len(players)):
        print(str(players[x]))
    print("HP: " + str(HP))
 

    #Battle Loop (Rounds 1 through 5) starts here
    for x in range(1, 6):

        print("Round " + str(x) + " begins")

        #Change to 15 later
        time.sleep(1)

        with open("command.json", "r") as read_file:
            commands = json.load(read_file) 

        for y in range(len(commands)):
            if(commands[y].lower() == "attack" or commands[y].lower() == "atk"):
                #HP should decrease by the damage of the weapon/attack, not necessarily 200
                HP-=100
                print("The " + mobType + " now has " + str(HP) + " hp")
            elif(commands[y].lower() == "heal"):
                #heal function
                print("Heal Function")
            elif(commands[y].lower() == "defend" or commands[y].lower() == "def"):
                #defend function
                print("Defend Function")
            else:
                print("ignore")
            
            #Ends the loop if the most recent attack killed it
            if (HP <= 0):
                print("The " + mobType + " was defeated!")
                outcome = "win"
                break

        if (HP <= 0):
            break

        #If loop is never broken, outcome is default to lose
        outcome = "lose"
        
        #Chooses between single-target attack of AoE
        attackChoice = random.randint(1, 2)
        if (attackChoice == 1):
            randomPlayer = players[random.randint(0, len(players) - 1)]
            print("The " + mobType + " attacks party member " + randomPlayer)
        else:
            print("The " + mobType + " hits every member in your party!")
            print("")

    if(outcome == "win"):
        output = loot.loot(tier)
        #chooses random player to collect loot - who is going to get it
        #maybe split the money 5 ways                   
        if(output[0]=='gold'):
            #ethan split up depending on how many players are there
            print('test')
        elif(output[0]=='weapon'):
            #ethan do random of which player won
            #inventory.setWeapon(player_name, output[1])
            print('test')
        elif(output[0]=='helmet'):
            #inventory.setHead(player_name, output[1])
            print('test')
        elif(output[0]=='chestplate'):
            #inventory.setBody(player_name, output[1])
            print('test')
        elif(output[0]=='leggings'):
            #inventory.setLeg(player_name, output[1])
            print('test')
        else:
            #inventory.setBoot(player_name, output[1])
            print('test')
        #depending on weapon type, second parameter, call set item for in inventory
    else:
        print("You have lost")

def main():
    Boss_Mob()

if __name__ == "__main__":
    main()
    