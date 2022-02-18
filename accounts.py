import discord
import os

class Account():
    def __init__(self, username, mention):
        self.username = username
        self.mention = mention
        self.cash = 0

    def addMoney(self, cashtoAdd):
        self.cash += cashtoAdd

class Account1(Account):
    def __init__(self):
        Account.__init__(self, 'Retr0A', '@Retr0A-Server Dev')

account1 = Account1()