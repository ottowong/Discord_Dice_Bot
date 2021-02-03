import discord
from random import randint

# These are set so that Harry doesn't roll millions of dice with millions of sides and crash the bot
maxModifier = 1000
maxNumberOfRolls = 10
maxNumberOfDice = 10
maxSides = 1000

helpstring = ("""
format your messages in the format:
```!r[number of dice]d[number of sides]```
for example:
```!r1d20```
you can also add a modifier or roll multiple dice by adding:
```+[number]```
or
```+[number of dice]d[number of sides]```
to the end of your message. If you want to subtract you will have to do "+-". e.g.
```!r1d20+2d6+-5```
do not roll more than """+str(maxNumberOfRolls)+""" dice with more than """+str(maxSides)+""" sides with a modifier greater than """+str(maxModifier)+""" or more than """+str(maxNumberOfDice)+""" different dice.
""")


client = discord.Client()
@client.event
# whenever a message is sent this will run
async def on_message(message):
    # if the sender of the message is the bot, don't do anything
    if (message.author == client.user):
        return


    counter = 0
    invalid = False
    # jesus christ what a mess, this shit is unreadable
    if(str.lower(str(message.content).replace(" ","")) == "!rhelp"):
        await message.channel.send(helpstring)
    elif(str.lower(message.content).startswith("!r")):
        try:
            messagestring = str.lower(message.content)
            if(messagestring == "!r"):
                messagestring = "!r1d20"
            rollstring = (str(message.author)[:-5]+" rolled: ")
            rollsList = messagestring[2:].split("+")
            for i in range(0,len(rollsList)):
                rollsList[i] = rollsList[i].split("d")
            if(len(rollsList) > maxNumberOfDice):
                invalid = True
            else:
                for i in range(0,len(rollsList)):
                    if(len(rollsList[i]) == 2):
                        if(int(rollsList[i][0]) <= maxNumberOfRolls and int(rollsList[i][1]) <= maxSides):
                            rollstring += "\n"+str(rollsList[i][0])+" d"+str(rollsList[i][1])+":"
                            for a in range(0, int(rollsList[i][0])):

                                rando = (randint(1, int(rollsList[i][1])))
                                counter += rando
                                if (a != 0):
                                    rollstring += ","
                                rollstring += " "+str(rando)
                        else:
                            invalid = True
                    elif(len(rollsList[i]) == 1):
                        if (int(rollsList[i][0]) > maxModifier):
                            invalid = True
                        else:
                            counter += int(rollsList[i][0])
                            rollstring += "\n+ "+str(rollsList[i][0])
            if(invalid == False):
                rollstring += "\nresulting in: **"+str(counter)+"**"
                await message.channel.send(rollstring)
            else:
                await message.channel.send("invalid input\nType:\n```!r help```\nfor help")
        except Exception as e:
            await message.channel.send("invalid input: "+str(e)+"\nType:\n```!r help```\nfor help")

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='!r help for how to use'))
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

# your bot token will be roughly this length with some .s in it:
# aaaaaaaaaaaaaaaaaaaaaaaa.aaaaaa.aaaaaaaaaaaaaaaaaaaaaaaaaaa
# token should be on this page:
# discordapp.com/developers/applications/[your bot]/bots

client.run('TOKEN')
