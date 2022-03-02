from random import random
import discord
from discord.ext import commands
import json
import os
import random

#os.chdir("C:\\Users\\Bratl\\Github\\CreativeBot")

client = discord.Client()
client = commands.Bot(command_prefix = "//")

@client.command()
async def balance(ctx):
    await open_account(ctx.author)
    user = ctx.author
    users = await get_bank_data()

    wallet_amt = users[str(user.id)]["wallet"]
    bank_amt = users[str(user.id)]["bank"]

    em = discord.Embed(title = f"{ctx.author.name}'s balance", color = discord.Color.green())
    em.add_field(name = "Wallet balance", value = wallet_amt)
    em.add_field(name = "Bank balance", value = bank_amt)
    await ctx.send(embed = em)

@client.command()
async def beg(ctx):
    await open_account(ctx.author)

    users = await get_bank_data()
    user = ctx.author

    earnings = random.randrange(101)

    await ctx.send(f"Someone gave you {earnings} coins!!")

    users[str(user.id)]["wallet"] += earnings

    with open("mainbank.json", "w") as f:
        json.dump(users, f)

async def open_account (user):
    users = await get_bank_data()

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 0
        users[str(user.id)]["bank"] = 0

    with open("bank.json", "w") as f:
        json.dump(users, f)
    return True

async def get_bank_data():
    with open("mainbank.json", "r") as f:
        users = json.load(f)

    return users

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    #if message.content.startswith('//spam'):

        #while 1 == 1:
          #await message.channel.send("@Bubble Clan | xxx")

    # convertedMessage = '{0.author.mention}`s cash is: 1000$'.format(message)

    #if message.content.startswith('//cash Retr0A'):
        #await message.channel.send(accounts.account1.username + '`s cash is: ' + accounts.account1.money)

        #accountName = accounts.account1.username
        #accountCash = accounts.account1.cash

        #await message.channel.send(f'{accountName}`s cash is: ***{accountCash}***')

        # await message.channel.send(convertedMessage)

    #if message.content.startswith('//addMoneyDebug'):
        #accounts.account1.addCash(10);

    #if message.content.startswith('//rob'):
        #await message.channel.send("You robbed somone :)")

    if message.content.startswith('//help'):
      embed=discord.Embed(title="Help Command", description="The prefix of CreativeBot is //.", color=0x00FF85)
      embed.set_thumbnail(url="https://www.memesmonkey.com/images/memesmonkey/6f/6fa2b13f83413c7294eab3060e054573.jpeg");
      
      #embed.add_field(name="Cash", value="-cash - See your current cash.\n-rob - Rob someone(Legal).", inline=False)

      embed.add_field(name="Fun", value="-fuckyou - DON`T TRY THIS!", inline=False)

      embed.add_field(name="Server", value="-rules - Writes the rules in case you forgot them", inline=False)

      embed.set_footer(text="Information requested by: {}".format(message.author.display_name))

      await message.channel.send(embed=embed)

    if message.content.startswith('//rules'):
      embed=discord.Embed(title="RULES Command", description="The rules are very important to know.", color=0xc80000)
      embed.set_thumbnail(url="https://th.bing.com/th/id/R.1931ea674c875a53c30ec59b598b9ed3?rik=4ZKzGXf4B1NTmg&riu=http%3a%2f%2fimages.memes.com%2fmeme%2f664153&ehk=kmWqbWmpDHNPIlLt65RF1ShWgbn%2blZ9NjDZIYA1VRho%3d&risl=&pid=ImgRaw&r=0");
      
      embed.add_field(name="RULES", value="1.No NSFW, warn if you post something nsfw!\n\n" +
      "2.No bullying, this counts as hate to another person and cyberbullying.\n\n" +
      "3.No racism and dark jokes, they aren't funny guys.\n\n" +
      "4.No spamming, don't spam in any of the channels.\n\n" +
      "5.No begging for roles, don't beg for roles.\n\n" +
      "6.Have kindness and respect to other people.\n\n" +
      "7.Have a fun time!\n\n\n" +
      
      "- Rules In #<947244357944246302>\n\n" +
      "1. Cant send two msgs one after another.\n\n" +
      "2. Don't spam.",
      inline=False)

      embed.set_footer(text="Information requested by: {}".format(message.author.display_name))

      await message.channel.send(embed=embed)

client.run(os.getenv('DISCORD_TOKEN'))
