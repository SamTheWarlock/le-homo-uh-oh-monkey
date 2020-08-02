import json
import discord
client = discord.Client()
import random
import asyncio
authAdmins = []
@client.event
async def on_ready():
    mcount = 1
    for guild in client.guilds:
        for member in guild.members:
            mcount = mcount + 1
            print(guild)
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="over " + str(mcount) + " members | red is nerd"))
    print('We have logged in as {0.user}'.format(client))
    

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    msg = message.content.lower()
    if msg.startswith('un!info'):
        if msg == "un!info" or msg == "un!info ":
            await message.channel.send("Must include full command. \n\nExample usage: **un!info :flag_us:** or **un!info United States**")
        else:
            country = msg[9:1000]
            with open("database.txt", "r") as openedFile:
                lines = openedFile.readlines()
                for lein in lines:
                    lin = json.loads(lein)
                    line = lin["name"]
                    print("working")
                    if country.startswith(":flag"):
                        if lin["flag"].lower() == country:
                            print("working")
                            countryinfo = discord.Embed(title="**Information about " + line + ":**", description="**Name: **" + line + "\n**Flag: **" + lin["flag"] + "\n**Leader: **" + lin["leader"], color=0x3498db)
                            await message.channel.send(embed=countryinfo)
                        else:
                            print("working")
                            await message.channel.send(":exclamation: That country doesn't exist or hasn't been added to the system yet. If you think this is an error, contact PensiveBread.")
                    else:
                        if country == line:
                            countryinfo = discord.Embed(title="**Information about " + line + ":**", description="**Name: **" + line + "\n**Flag: **" + lin["flag"] + "\n**Leader: **" + lin["leader"], color=0x3498db)

    elif msg.startswith("un!suggest"):
        con = message.content[11:100000000]
        suggestrec = client.get_user(363773759095701507)
        await suggestrec.send(con)
        await message.channel.send(":thumbsup: Sent!")
        
    elif msg.startswith("un!diagnose"):
        import time
        egg = await message.channel.send("**__Diagnosing Bot...__**")
        lol = await message.channel.send(":orange_circle: **Decrypting Diagnostic Information*...***")
        time.sleep(2)
        await lol.edit(content=":green_circle: **Decrypted*!***")
        epic = await message.channel.send(":orange_circle: **Parsing Information...**")
        time.sleep(3)
        await epic.edit(content=":green_circle: Information Parsed into ``'information'`` variable")
        embedshout = discord.Embed(title="Information", description=":green_circle: Bot Online \n:green_circle: **No Errors**\n:green_circle: Web server **online**", color=0x3498db)
        await message.channel.send(embed=embedshout)
    elif msg.startswith("un!rules"):
        message.channel.send(":thumbsup: The rules have been sent in your DM's!")
        rules = """
        lel
        noob
        noob
        """
        embedrs = discord.Embed(title="Rules", description=AssignedDesc, color=0x3498db)
        await message.author.send(embed=embedrs)
client.run('e')
