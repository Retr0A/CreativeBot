import discord
import os

class account():
    def __init__(self, username, mention):
        self.username = username
        self.mention = mention
        self.cash = 0

    def addMoney(self, cashtoAdd):
        self.cash += cashtoAdd

class account1(account):
    def __init__(self):
        account.__init__(self, 'Retr0A', '@Retr0A-Server Dev')