import discord
import os

import accounts

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('//spam'):

        while 1 == 1:
          await message.channel.send("@Bubble Clan | xxx")

    # convertedMessage = '{0.author.mention}`s cash is: 1000$'.format(message) 

    if message.content.startswith('//cash Retr0A'):
        #await message.channel.send(accounts.account1.username + '`s cash is: ' + accounts.account1.money)

        accountName = accounts.account1.username
        accountCash = accounts.account1.cash

        await message.channel.send(f'{accountName}`s cash is: {accountCash}')

        # await message.channel.send(convertedMessage)
      
    if message.content.startswith('//rob'):
        await message.channel.send("You robbed somone :)")

    if message.content.startswith('//help'):
      embed=discord.Embed(title="Help Command", description="The prefix of CreativeBot is $.", color=0x00FF85)
      embed.set_thumbnail(url="https://www.memesmonkey.com/images/memesmonkey/6f/6fa2b13f83413c7294eab3060e054573.jpeg");
      
      embed.add_field(name="Cash", value="-cash - See your current cash.\n-rob - Rob someone(Legal).", inline=False)

      embed.add_field(name="Fun", value="-fuckyou - DON`T TRY THIS!", inline=False)

      embed.add_field(name="Server", value="-rules - Writes the rules in case you forgot them", inline=False)

      embed.set_footer(text="Information requested by: {}".format(message.author.display_name))

      await message.channel.send(embed=embed)

    if message.content.startswith('//rules'):
      embed=discord.Embed(title="RULES Command", description="The rules are very important to know.", color=0xc80000)
      embed.set_thumbnail(url="https://th.bing.com/th/id/R.1931ea674c875a53c30ec59b598b9ed3?rik=4ZKzGXf4B1NTmg&riu=http%3a%2f%2fimages.memes.com%2fmeme%2f664153&ehk=kmWqbWmpDHNPIlLt65RF1ShWgbn%2blZ9NjDZIYA1VRho%3d&risl=&pid=ImgRaw&r=0");
      
      embed.add_field(name="RULES", value="NSFW - Do not post nsfw!This is not good.\n\nHARASSING - This server is only for literate people.\n\nRACISM - This is not good!", inline=False)

      embed.set_footer(text="Information requested by: {}".format(message.author.display_name))

      await message.channel.send(embed=embed)
client.run(os.getenv('DISCORD_TOKEN'))
