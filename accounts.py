import discord
import os

class Account():
    def __init__(self, username, mention):
        self.username = username
        self.mention = mention
        self.cash = 0

    def addCash(self, cashtoAdd):
        self.cash += cashtoAdd

account1 = Account('Retr0A', '@Retr0A-Server Dev')