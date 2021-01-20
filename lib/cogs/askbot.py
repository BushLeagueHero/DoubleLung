import json
from lib.cogs import hunt
from difflib import get_close_matches as matches
from datetime import datetime

from discord import Member
from discord.ext.commands import Cog
from discord.ext.commands import command
from discord import Intents, Embed, File

dt = datetime.now()
dt_formatted = dt.strftime("%b %d %Y %H:%M:%S")

class Askbot(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command(name="askbot")
    async def parse_question(self,ctx,*,question):
        hunt_array = json.load(open('./lib/db/hunt.json'))
        hunt_list = json.load(open("./lib/db/hunt_check.json"))
        stat_list = json.load(open("./lib/db/stat_check.json"))

        if question[-1].isalpha()==True:
            q_split=question.split()
        else:
            q_split=question[:-1].split()
        print(q_split)

        hunt_check = []
        stat_check = []

        for i in q_split:
            m=matches(i,hunt_list['hunt_keywords'],n=1,cutoff=0.9)
            if len(m)>0:
                if m[0] not in hunt_check:
                    hunt_check.append(m[0])

        print(hunt_check)

        hunt_check = "".join(hunt_check)
        print(hunt_check)

        hunt_match=False
        hunt_check=matches(hunt_check,hunt_list['hunt_commands'],n=1,cutoff=0.6)
        print(hunt_check)
        if len(hunt_check)>0:
            hunt_match=True
            print(hunt_match)

        if hunt_match==True:
            for i in q_split:
                n=matches(i,stat_list['stat_keywords'],n=1,cutoff=0.9)
                if len(n)>0:
                    if n[0] not in stat_check:
                        stat_check.append(n[0])

            print(stat_check)

            stat_check = "".join(stat_check)
            print(stat_check)

            stat_match=False
            stat_check=matches(stat_check,stat_list['stat_commands'],n=1,cutoff=0.6)
            print(stat_check)
            if len(stat_check)>0:
                stat_match=True
                print(stat_match)

            if stat_match==True:
                for i in stat_list['general']:
                    if stat_check[0]==i:
                        stat_attr="general"
                        print(stat_attr)
                for i in stat_list['need']:
                    if stat_check[0]==i:
                        stat_attr="need"
                        print(stat_attr)
                for i in stat_list['score']:
                    if stat_check[0]==i:
                        stat_attr="score"
                        print(stat_attr)
                for i in stat_list['equipment']:
                    if stat_check[0]==i:
                        stat_attr="equipment"
                        print(stat_attr)

                print(f"{hunt_check[0]} {stat_attr}")
        
                await ctx.invoke(self.bot.get_command(hunt_check[0]), stat=stat_attr)
            else:
                await self.bot.stdout.send("There may be an issue with the stat for which you are searching.  Please double check your stat request and try again. You can use !hunthelp for a list and spelling of available stats.")
                await self.bot.stdout.send("If you believe you have typed your question in correctly, try asking it a different way. I may be able to understand what you are asking better.")
                await self.bot.stdlog.send(f"Message Stat Error: {question}")
        else:
            await self.bot.stdout.send("There may be an issue with the animal for which you are searching.  Please double check your animal and try again. You can use !hunthelp for a list and spelling of available animals.")
            await self.bot.stdout.send("If you believe you have typed your question in correctly, try asking it a different way. I may be able to understand what you are asking better.")
            await self.bot.stdlog.send(f"Message Hunt Error: {question}")

    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("askbot")

def setup(bot):
    bot.add_cog(Askbot(bot))