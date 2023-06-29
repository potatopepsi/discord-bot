# Header Imports
import json
import random

# Function Definitions

# Helper Function - Input (item category, tier), Output (string of item name)
def index_loot(item, tier):

    # Either sets num for the json dict based on item category, or return gold based on tier

    if(item=='weapon'):
        num = 0
    elif(item=='helmet'):
        num = 2
    elif(item=='chestplate'):
        num = 3
    elif(item=='leggings'):
        num = 4
    elif(item=='boots'):
        num = 5
    else:
        if(tier==1):
            return '100 gold'
        elif(tier==2):
            return '200 gold'
        elif(tier==3):
            return '300 gold'
        elif(tier==4):
            return '400 gold'
        else:
            return '500 gold'

    # loads up entire json file of items
    f = open('all_items.json')
    data = json.load(f)
    f.close()
    '''
    This section is for separating the JSON file into tiers
    '''
    
    num_of_items = len(list(data.values())[num])
    tier_one = []
    tier_two = []
    tier_three = []
    tier_four = []
    tier_five = []

    # Based off of item type, iterate through json file and append to correct array

    for x in range(num_of_items):
        if(list(data.values())[num][x]['Tier']==1):
            tier_one.append ( (list(data.values())[num][x]) )
        elif(list(data.values())[num][x]['Tier']==2):
            tier_two.append ( (list(data.values())[num][x]) )
        elif(list(data.values())[num][x]['Tier']==3):
            tier_three.append ( (list(data.values())[num][x]) )
        elif(list(data.values())[num][x]['Tier']==4):
            tier_four.append ( (list(data.values())[num][x]) )
        elif(list(data.values())[num][x]['Tier']==5):
            tier_five.append ( (list(data.values())[num][x]) )


    # Output a random item from the tier
    
    if(tier==1):
        output = random.randint(0,len(tier_one)-1)
        return tier_one[output]['Name']
    elif(tier==2):
        output = random.randint(0,len(tier_two)-1)
        return tier_two[output]['Name']
    elif(tier==3):
        output = random.randint(0,len(tier_three)-1)
        return tier_three[output]['Name']
    elif(tier==4):
        output = random.randint(0,len(tier_four)-1)
        return tier_four[output]['Name']
    else:
        output = random.randint(0,len(tier_five)-1)
        return tier_five[output]['Name']


# Loot Function - Input (Tier of Mob), Output [Type of Item, Item from Json]
def loot(tier):

    # Based on Tier, Weights are affected of what loot is given
    # If Armor is chosen, another random choice is evenly distributed between helmet, chestplate, and leggings
    # Then, index_loot is called

    choices = ['weapon', 'armor', 'gold']
    
    if(tier==1):
        tier_one_random = random.choices(choices, weights =(10,10,80), k=1)    
        if(tier_one_random[0] == 'armor'):
            choice = ['helmet', 'chestplate', 'leggings','boots']
            item = random.choices(choice, weights = (25,25,25,25), k=1) 
            output = index_loot(item[0], tier)
            return [item[0],output]
        else:
            output = index_loot(tier_one_random[0],tier)
            return [tier_one_random[0], output]

    elif(tier==2):
        tier_two_random = random.choices(choices, weights =(9,9,82), k=1)
        if(tier_two_random[0] == 'armor'):
            choice = ['helmet', 'chestplate', 'leggings','boots']
            item = random.choices(choice, weights = (25,25,25,25), k=1)  
            output = index_loot(item[0], tier)
            return [item[0],output]
        else:
            output = index_loot(tier_two_random[0],tier)
            return [tier_two_random[0], output]

    elif(tier==3):
        tier_three_random = random.choices(choices, weights = (8,8,84), k=1)
        if(tier_three_random[0] == 'armor'):
            choice = ['helmet', 'chestplate', 'leggings','boots']
            item = random.choices(choice, weights = (25,25,25,25), k=1)
            output = index_loot(item[0], tier)
            return [item[0],output]
        else:
            output = index_loot(tier_three_random[0],tier)
            return [tier_three_random[0], output]
    elif(tier==4):
        tier_four_random = random.choices(choices, weights = (6,6,88), k=1)
        if(tier_four_random[0] == 'armor'):
            choice = ['helmet', 'chestplate', 'leggings','boots']
            item = random.choices(choice, weights = (25,25,25,25), k=1)
            output = index_loot(item[0], tier)
            return [item[0],output]
        else:
            output = index_loot(tier_four_random[0],tier) 
            return [tier_four_random[0], tier]
    elif(tier==5):
        tier_five_random = random.choices(choices, weights = (2,2,96), k=1)
        if(tier_five_random[0] == 'armor'):
            choices = ['helmet', 'chestplate', 'leggings','boots']
            item = random.choices(choices, weights = (25,25,25,25), k=1) 
            output = index_loot(item[0], tier)
            return [item[0],output]
        else:
            output = index_loot(tier_five_random[0],tier)
            # Takes item from index_loot and returns it
            return [tier_five_random[0],output]
        

    
        

    


def main():
    output = loot(5)
    print(output)

if __name__ == "__main__":
    main()
