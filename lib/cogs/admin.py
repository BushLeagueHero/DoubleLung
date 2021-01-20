import json

from discord import Member
from discord.ext.commands import Cog
from discord.ext.commands import command
from discord import Intents, Embed, File

class Admin(Cog):
    def __init__(self,bot):
        self.bot = bot

    