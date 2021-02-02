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

class Species(Cog):
    def __init__(self, bot):
        self.bot = bot
    
    #get speciesID
    def __get_speciesid(self,species):
        for i in range(0,len(data["species"])):
            if data["species"][i]["speciesid"] == species:
                species_data_set = data["species"][i]

        return species_data_set

    #determine keys to use
    def __determine_embed_keys(self,group):
        embed_keys = []
        for i in range(0,len(cmd_set["stats"])):
            if cmd_set["stats"][i]["group"] == group:
                embed_keys.append(cmd_set["stats"][i]["id"])
    
        return embed_keys

    #determine data for each key
    def __pull_key_data(self,embed_keys,species):
        key_data = []
        for key in embed_keys:
            data = species[key]
            key_data.append({key:data})
        
        return key_data

    #add each stat from group in embed
    def __add_stat_to_embed(self,stat,data_set):
        for i in range(0,len(cmd_set["stats"])):
            if cmd_set["stats"][i]["id"] == stat:
                stat_conf = cmd_set["stats"][i]

        name = stat_conf["description"]
        value_obj = []
        if search("lol_",stat):
            if stat == "lol_location":
                for n in range(0,len(data_set[stat])):
                    value_obj.append(data_set[stat][n][0])
                values = "\n".join(i for i in value_obj)
            else:
                stat_list = {}
                for loc in range(len(data_set["lol_location"])):
                    for s in data_set[stat][loc]:
                        if s not in stat_list:
                            stat_list[s] = []
                        stat_list[s].append(data_set["lol_location"][loc][0])
                
                for key,value in stat_list.items():
                    value_obj.append(f"{key} ({', '.join(i for i in value)})")
                
                values = "\n".join(i for i in value_obj)
        else:
            values = "\n".join(i for i in data_set[stat])

        inline = stat_conf["inline"]
        
        embed.add_field(name=name,value=values, inline=inline)

    def __build_embed(self,ctx,species,group):
        data_set = (self.__get_speciesid(species))  
        key_group = self.__determine_embed_keys(group)
        data = self.__pull_key_data(key_group,data_set)

        embeds=[]

        for stat in key_group:
            embed = Embed(title=data_set["species"],color=0xFF0000)
            # embed.set_author(name="DoubleLung Bot")
            # embed.set_thumbnail(url=ctx.message.guild.icon_url)

            # self.__add_stat_to_embed(stat,data_set)

            # embed.set_footer(text=f"{ctx.author.display_name}; {formatted_date()}")
            
            embeds.append(embed)

            logger.debug(f"added embed for stat {stat}")

        logger.debug(f"returning {len(embeds)} stat embeds")
        return embeds

    @command(name="species")
    async def get_species(self,ctx,species,group):
        embeds = self.__build_embed(ctx,species,group)
        for embed in embeds:
            await self.bot.command_embed_response(ctx,embed)

    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("species")

def setup(bot):
    bot.add_cog(Species(bot))