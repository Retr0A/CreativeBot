import discord
import os

class account():
    def __init__(self, username, mention):
        self.username = username
        self.mention = mention
        self.money = 0

    def addMoney(self, moneytoAdd):
        self.money += moneytoAdd

class account1(account):
    def __init__(self):
        account.__init__(self, 'Retr0A', '@Retr0A-Server Dev')