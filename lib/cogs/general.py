import json
from datetime import datetime

from discord import Member
from discord.ext.commands import Cog
from discord.ext.commands import command
from discord import Intents, Embed, File

dt = datetime.now()
dt_formatted = dt.strftime("%b %d %Y %H:%M:%S")

class General(Cog):
    def __init__(self,bot):
        self.bot = bot

    @command(name="clear")
    async def clear_messages(self, ctx, amount=100):
        await ctx.channel.purge(limit=amount)

    @command(name="command",aliases=["commands","info","information"])
    async def show_commands(self,ctx):
        pass       

    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("general")

def setup(bot):
    bot.add_cog(General(bot))