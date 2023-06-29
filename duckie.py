import discord
import sys
import json
import mobs
import register
import current
import stats
import inventory


#work on webhook integration
intents = discord.Intents().default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('poopy'):
        await message.channel.send('STINKY')
        print('poopy has been registered')

    if message.content.startswith('fry'):
        await message.channel.send('FRY IS BEST STREAMER')

    if message.content.startswith('ffxiv'):
        await message.channel.send('Final Fantasy is currently the best game')

    '''
    Commands is listed below
    !fightinfo - for Battle info
    !charinfo - for Character Info
    '''
    if message.content.startswith('!commands'):
        embedVar = discord.Embed(title="Mochi Dungeon Adventures", description="Type in the following commands for more information.", color=0xffffff)
        embedVar.add_field(name="Battle Information", value="`!fightinfo`", inline=True)
        embedVar.add_field(name="Character Information", value="`!charinfo` or `!register`", inline=True)
        
        embedVar.add_field(name="Bank", value="`!bank`", inline=True)
        embedVar.add_field(name="Equipments", value="`!equipsinfo`", inline=True)
        embedVar.add_field(name="Inventory", value="`!backpack`", inline=True)
        
        embedVar.add_field(name="Store", value="`!storeinfo`", inline=True)
        embedVar.add_field(name="Trade", value="`!tradeinfo`", inline=True)
        
        await message.channel.send(embed=embedVar)

    # Information Board for Fighting
    if message.content.startswith('!fightinfo'):
        fightInfo = discord.Embed(title="Fight Commands", color=0x000000)
        fightInfo.add_field(name="Commands", value="`!battle` - to spawn monster \n `!attack` - to attack monster for that round \n `!defend` - to minimze damage taken from monster")
        
        await message.channel.send(embed=fightInfo)

    # Fighting Story is Called
    if message.content.startswith('!battle'):
        fightEmbed = discord.Embed(title="Fight Begins", description="", color=0xffffff)
        story = mobs.story()
        fightEmbed.add_field(name="Story:", value=story, inline=True)
        await message.channel.send(embed=fightEmbed)

    # !attack, !defend, !heal
    if message.content.startswith('!attack'):
        current.collect(message.author.id, "attack")
        await message.add_reaction("<a:snor:933831667615940698>")

    if message.content.startswith('!defend'):
        current.collect(message.author.id, "defend")
        await message.add_reaction("<a:snor:933831667615940698>")

    if message.content.startswith('!heal'):
        current.collect(message.author.id, "heal")
        await message.add_reaction("<a:snor:933831667615940698>")

    #Character Info Commands
    if message.content.startswith('!charinfo'):
        statInfo = discord.Embed(title="Commands", color=0x000000)
        statInfo.add_field(name="Stat Commands", value="`!stats` - to view current stats")
        statInfo.add_field(name="Class Commands", value="`!classes` - to view different classes \n `!myclass` - to view your current class")
        await message.channel.send(embed=statInfo)
    #Showing stats of character
    if message.content.startswith('!stats'):
        statsi = discord.Embed(title="Your Stats", color = 0xffffff)
        stat_data = stats.showstats(message.author.id)
        statsi.add_field(name="Weapon Damage", value = str(stat_data[0]))
        statsi.add_field(name="Total Defense", value = str(stat_data[1]))
        statsi.add_field(name="Helmet Damage", value = str(stat_data[2]))
        statsi.add_field(name="Chestplate Damage", value = str(stat_data[3]))
        statsi.add_field(name="Leggings Damage", value = str(stat_data[4]))
        statsi.add_field(name="Boots Damage", value = str(stat_data[5]))
        statsi.add_field(name="HP", value = str(stat_data[6]))
        statsi.add_field(name="Level", value = str(stat_data[7]))
        statsi.add_field(name="Exp", value = str(stat_data[8]))
        await message.channel.send(embed=statsi)

    if message.content.startswith('!classes'):
        classInfo = discord.Embed(title="Classes", color=0x000000)
        classInfo.add_field(name="View", value="`!Healer` - No attack damage, buff stats, and heal party \n`!Mage` - Magic Damage \n `!Warrior` - Attack Damage \n `!Assassin` - Probability to attack twice \n `!Monk` - Fist Damage Increased \n `!Lancer` - Spear Damage Increased \n `!Archer` - Ranged Damage, 50% Dodge Chance \n `!Berserker` - Attack Damage")
        
        await message.channel.send(embed=classInfo)

    if message.content.startswith('!myclass'):
        with open('user.json', 'r+') as file:
            existing_data = json.load(file)
        file.close()
        user_array = existing_data['users']
        user_index = None
        for x in range(len(user_array)):
            if(existing_data['users'][x]['id']==message.author.id):
                user_index = x
                break

        showmyclass = discord.Embed(title="Your Class", color = 0xffffff)
        showmyclass.add_field(name="View", value=(existing_data['users'][user_index]['class']))

        await message.channel.send(embed=showmyclass)

    if message.content.startswith('!register'):
        blank = ""
        with open('user.json', 'r+') as file:
            existing_data = json.load(file)
        for x in range (len(existing_data['users'])):
            if(existing_data['users'][x]['id']==message.author.id):
                blank = "already registered"
            else:
                blank = "registered"

        if (blank=="registered"):
            register.new_user(message.author.id, message.author.name)
        await message.channel.send("User is " + blank)

    #Equip Info Commands
    if message.content.startswith('!equipsinfo'):
        equipsinfo = discord.Embed(title="Equip Commands", color=0x000000)
        equipsinfo.add_field(name="Commands", value="`!equip <item>` - equip an item from backpack \n `!unequip <item> <item_type>` - to unequip an item")
        await message.channel.send(embed=equipsinfo)

    #work on how to get user input


    if message.content.startswith('!backpack'):
        backpackInfo = discord.Embed(title="Backpack Commands", color=0x000000)
        backpackInfo.add_field(name="View", value="`!inventory` - to check inventory \n `!delinventory <item>` - to trash an item from inventory")

        await message.channel.send(embed=backpackInfo)

    if message.content.startswith('!inventory'):
        inventoryembed = discord.Embed(title="Your Backpack", color = 0xffffff)
        invendata = inventory.getBackpack(message.author.id)
        for x in range(len(invendata)):
            inventoryembed.add_field(name="Item", value=invendata[x])
        await message.channel.send(embed=inventoryembed)
    
    if message.content.startswith('!bank'):
        with open('user.json', 'r+') as file:
            existing_data = json.load(file)
        file.close()
        user_array = existing_data['users']
        user_index = None
        for x in range(len(user_array)):
            if(existing_data['users'][x]['id']==message.author.id):
                user_index = x
                break

        showmymoney = discord.Embed(title="Currency", color = 0xffffff)
        showmymoney.add_field(name="View", value=str(existing_data['users'][user_index]['currency']))

        await message.channel.send(embed=showmymoney)

    if message.content.startswith('!storeinfo'):
        storeInfo = discord.Embed(title="Store Commands", color=0x000000)
        storeInfo.add_field(name="View", value="`!shop` - to see what's in the shop \n `!buy <item>` - to buy item \n `!sell <item>` - to sell item in backpack")

        await message.channel.send(embed=storeInfo)
    #shop
    if message.content.startswith('!shop'):
        shop = discord.Embed(title='Shop', color = 0xffffff)

        with open('store.json', 'r+') as file:
            store_data = json.load(file)
        file.close()

        for x in range (len(store_data['Store'])):
            shop.add_field(name="Potion Name", value=store_data['Store'][x]['Item'])
            shop.add_field(name="Value of Healing", value=store_data['Store'][x]['Value'])
            shop.add_field(name="Price", value=store_data['Store'][x]['Price'])

        await message.channel.send(embed=shop)

    if message.content.startswith('!tradeinfo'):
        tradeInfo = discord.Embed(title="Trade Commands", color=0x000000)
        tradeInfo.add_field(name="View", value="`!trade <user> <their_item> <your_item>` - to trade items with user \n `!trade <user> <their_item> <gold_amount>` - to trade item for gold \n `!give <gold>` - to give your gold to another player")

        await message.channel.send(embed=tradeInfo)


    



client.run('MTAzMzQ1OTkyODI0Mjg2MDEyMw.GRutQn.G_4fzOoJcaTkuxzcDN0jPyiMQ8_YC_s1YVhaxU')