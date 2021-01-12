import json
from datetime import datetime

from discord import Member
from discord.ext.commands import Cog
from discord.ext.commands import command
from discord import Intents, Embed, File

caller_array = json.load(open("./lib/db/caller.json"))

dt = datetime.now()
dt_formatted = dt.strftime("%b %d %Y %H:%M:%S")

caller_description = {"name": ["Caller Name", False]}
caller_stats = {"level"     :   ["Level",False],
                "range"     :   ["Range",True],
                "duration"  :   ["Duration",True],
                "strength"  :   ["Strength",True],
                "hunt"      :   ["Hunt",False]}

class Caller(Cog):
    def __init__(self,bot):
        self.bot = bot

    @command(name="caller", aliases=["callers"])
    async def show_caller(self,ctx,*,caller):
        user_caller = "caller"
        user_stat = caller.lower().replace(" ","")
        
        caller_name = caller_array[user_stat][0]['name']
        embed = Embed(title="\n".join(i for i in caller_name), color=0xFF0000)
        
        for key in caller_stats: 
            stat_data = caller_array[user_stat][0][key]
            embed.add_field(name=caller_stats[key][0], value="\n".join(i for i in stat_data), inline=caller_stats[key][1])

        embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")       
        
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)

        await self.bot.stdout.send(embed=embed)

    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("caller")

def setup(bot):
    bot.add_cog(Caller(bot))
            
