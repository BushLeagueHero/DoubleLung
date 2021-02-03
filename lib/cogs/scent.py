import json
from datetime import datetime

from discord import Member
from discord.ext.commands import Cog
from discord.ext.commands import command
from discord import Intents, Embed, File

dt = datetime.now()
dt_formatted = dt.strftime("%b %d %Y %H:%M:%S")

scent_types = ["Blacktail Deer","Roe Deer","Roosevelt Elk","Moose","Red Deer","Whitetail Deer","Wild Boar","Musk Deer","Mule Deer"]

class Scent(Cog):
    def __init__(self,bot):
        self.bot = bot

    @command(name="scents", aliases=["scent"])
    async def get_scents(self,ctx):

        fields = [("Scent Type", "\n".join(i for i in sorted(scent_types)), False),("Range","200m",True),("Duration","300s",True),("Strength",50,True),("Units per Canister",10,False)]

        embed = Embed(title="Available Scents",description="All scent type stats are identicle",color=0xE3E300)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=ctx.message.guild.icon_url)

        for name,value,inline in fields:
            embed.add_field(name=name,value=value,inline=inline)

        embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
        if ctx.response_channel is not None:
            await ctx.response_channel.send(embed=embed)

    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("scent")

def setup(bot):
    bot.add_cog(Scent(bot))