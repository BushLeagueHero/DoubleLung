import json
import logging

from difflib import get_close_matches as matches
from datetime import datetime
from re import search

from discord import Member
from discord.ext.commands import Cog
from discord.ext.commands import command
from discord import Intents, Embed, File

logger = logging.getLogger(f"doublelung.{__name__}")

data = json.load(open('./lib/db/object.json'))
cmd_set = json.load(open('./lib/db/stat.json'))


def formatted_date():
    dt = datetime.now()
    dt_formatted = dt.strftime("%b %d %Y %H:%M:%S")
    return dt_formatted

class Weapon(Cog):
    def __init__(self, bot):
        self.bot = bot
    
    #get speciesID
    def __get_weaponid(self,weapon):
        for i in range(0,len(data["weapon"])):
            if data["weapon"][i]["weaponid"] == weapon:
                weapon = data["weapon"][i]

        return weapon

    #determine keys to use
    def __determine_embed_keys(self,group):
        embed_keys = []
        for n in range(0,15):
            for i in range(0,len(cmd_set["stats"])):
                if cmd_set["stats"][i]["group"] == group and cmd_set["stats"][i]["order"] == n:
                    embed_keys.append(cmd_set["stats"][i]["id"])
    
        return embed_keys

    #determine data for each key
    def __pull_key_data(self,embed_keys,weapon):
        key_data = []
        for key in embed_keys:
            data = weapon[key]
            key_data.append({key:data})
        
        return key_data

    #add each stat from group in embed
    def __add_stat_to_embed(self,stat,data_set):
        for i in range(0,len(cmd_set["stats"])):
            if cmd_set["stats"][i]["id"] == stat and cmd_set["stats"][i]["cmd_set"] == "weapon":
                stat_conf = cmd_set["stats"][i]

        name = stat_conf["description"]
        if stat == "weaponspecies":
            values = ", ".join(i for i in sorted(data_set[stat]))
        else:
            values = "\n".join(i for i in sorted(data_set[stat]))

        inline = stat_conf["inline"]
        
        field_values = {"name":[name],"values":[values],"inline":[inline]}

        return field_values

    def __build_embed(self,ctx,weapon):
        data_set = (self.__get_weaponid(weapon))  
        key_group = self.__determine_embed_keys("WEAPON")
        data = self.__pull_key_data(key_group,data_set)

        embed = Embed(title=data_set["weaponname"][0],color=0xD8771B)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=ctx.message.guild.icon_url)

        fields=[]

        for stat in key_group:
            field = self.__add_stat_to_embed(stat,data_set)
            fields.append(field)
            logger.debug(f"added embed for stat {stat}")

        for i in range(0,len(fields)):
            embed.add_field(name=fields[i]["name"][0],value=fields[i]["values"][0],inline=fields[i]["inline"][0])
        embed.set_footer(text=f"{ctx.author.display_name}; {formatted_date()}")

        logger.debug(f"returning {len(fields)} stat embeds")
        return embed

    @command(name="weapon")
    async def get_species(self,ctx,*,weapon):
        embeds = self.__build_embed(ctx,weapon)
        await ctx.message.channel.send(embed=embeds)

    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("weapon")

def setup(bot):
    bot.add_cog(Weapon(bot))