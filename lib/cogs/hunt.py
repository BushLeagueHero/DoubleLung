import json
import logging

from difflib import get_close_matches as matches
from datetime import datetime

from discord import Member
from discord.ext.commands import Cog
from discord.ext.commands import command
from discord import Intents, Embed, File

logger = logging.getLogger(f"doublelung.{__name__}")

hunt_array = json.load(open("./lib/db/hunt.json"))

def formatted_date():
    dt = datetime.now()
    dt_formatted = dt.strftime("%b %d %Y %H:%M:%S")
    return dt_formatted

class Hunt(Cog):
    def __init__(self, bot):
        self.bot = bot

    def __get_stats_embeds(self,ctx,title,user_hunt,user_stat):
        logger.debug(f"loading hunt stats for {user_hunt}, showing {user_stat}")
        embeds = []
        statkeys = self.__determine_stat_keys(user_stat)
        logger.debug(f"populating embeds for the following stats: {statkeys}")
        for stat in statkeys:
            embed = Embed(title=title,color=0xFF0000)
            embed.set_author(name="DoubleLung Bot")
            embed.set_thumbnail(url=ctx.message.guild.icon_url)
            
            self.__add_user_stat(embed,user_hunt,stat)
            embed.set_footer(text=f"{ctx.author.display_name}; {formatted_date()}")
            
            embeds.append(embed)

            logger.debug(f"added embed for stat {stat}")

        logger.debug(f"returning {len(embeds)} stat embeds")
        return embeds

    def __add_user_stat(self,embed,hunt,stat):
        logger.debug(f"populating data for {stat} using hunt {hunt}")
        for statkey in hunt_stats[stat]:
            stat_data = hunt_array[hunt][statkey]
            embed.add_field(name=hunt_stats[stat][statkey][0],value="\n".join(i for i in stat_data), inline=hunt_stats[stat][statkey][1])

    def __determine_stat_keys(self,user_stat):
        logger.debug(f"determining stat keys for stat {user_stat}")
        keys = []
        if user_stat == "all":
            for keyname in hunt_stats:
                keys.append(keyname)

        elif user_stat in hunt_stats:
            keys.append(user_stat)
        
        elif user_stat == "scores": keys.append("score")
        elif user_stat == "needs" or user_stat == "zone" or user_stat == "zones": keys.append("need")
        elif user_stat == "item" or user_stat == "items": keys.append("equipment")

        else: keys.append(user_stat)

        logger.debug(f"stat keys are {keys}")
        return keys

    @command(name="mallard")
    async def get_mallard(self,ctx,*,stat):
        embeds = self.__get_stats_embeds(ctx,"Mallard","mallard",stat.lower().replace(" ",""))
        for embed in embeds:
            await self.bot.command_embed_response(ctx,embed)

    @command(name="scrubhare")
    async def get_scrubhare(self,ctx,*,stat):
        embeds = self.__get_stats_embeds(ctx,"Scrub hare","scrubhare",stat.lower().replace(" ",""))
        for embed in embeds:
            await self.bot.command_embed_response(ctx,embed)

    @command(name="jackrabbit")
    async def get_jackrabbit(self,ctx,*,stat):
        embeds = self.__get_stats_embeds(ctx,"Jackrabbit","jackrabbit",stat.lower().replace(" ",""))
        for embed in embeds:
            await self.bot.command_embed_response(ctx,embed)

    @command(name="harlequinduck")
    async def get_harlequinduck(self,ctx,*,stat):
        embeds = self.__get_stats_embeds(ctx,"Harlequin Duck","harlequinduck",stat.lower().replace(" ",""))
        for embed in embeds:
            await self.bot.command_embed_response(ctx,embed)

    @command(name="turkey")
    async def get_turkey(self,ctx,*,stat):
        embeds = self.__get_stats_embeds(ctx,"Turkey","turkey",stat.lower().replace(" ",""))
        for embed in embeds:
            await self.bot.command_embed_response(ctx,embed)

    @command(name="canadagoose")
    async def get_canadagoose(self,ctx,*,stat):
        embeds = self.__get_stats_embeds(ctx,"Canada Goose","canadagoose",stat.lower().replace(" ",""))
        for embed in embeds:
            await self.bot.command_embed_response(ctx,embed)

    @command(name="europeanrabbit")
    async def get_europeanrabbit(self,ctx,*,stat):
        embeds = self.__get_stats_embeds(ctx,"European Rabbit","europeanrabbit",stat.lower().replace(" ",""))
        for embed in embeds:
            await self.bot.command_embed_response(ctx,embed)

    @command(name="europeanhare")
    async def get_europeanhare(self,ctx,*,stat):
        embeds = self.__get_stats_embeds(ctx,"European Hare","europeanhare",stat.lower().replace(" ",""))
        for embed in embeds:
            await self.bot.command_embed_response(ctx,embed)

    @command(name="cinnamonteal")
    async def get_cinnamonteal(self,ctx,*,stat):
        embeds = self.__get_stats_embeds(ctx,"Cinnamon Teal","cinnamonteal",stat.lower().replace(" ",""))
        for embed in embeds:
            await self.bot.command_embed_response(ctx,embed)
        
    @command(name="sidestripedjackal",aliases=["sidestripedjackals","side-stripedjackal","side-stripedjackals","stripedjackal","stripedjackals","jackal","jackals"])
    async def get_sidestripedjackal(self,ctx,*,stat):
        embeds = self.__get_stats_embeds(ctx,"Side-striped Jackal","sidestripedjackal",stat.lower().replace(" ",""))
        for embed in embeds:
            await self.bot.command_embed_response(ctx,embed)

    @command(name="coyote")
    async def get_coyote(self,ctx,*,stat):
        embeds = self.__get_stats_embeds(ctx,"Coyote","coyote",stat.lower().replace(" ",""))
        for embed in embeds:
            await self.bot.command_embed_response(ctx,embed)

    @command(name="siberianmuskdeer")
    async def get_siberianmuskdeer(self,ctx,*,stat):
        embeds = self.__get_stats_embeds(ctx,"Siberian Muskdeer","siberianmuskdeer",stat.lower().replace(" ",""))
        for embed in embeds:
            await self.bot.command_embed_response(ctx,embed)

    @command(name="redfox")
    async def get_redfox(self,ctx,*,stat):
        embeds = self.__get_stats_embeds(ctx,"Red Fox","redfox",stat.lower().replace(" ",""))
        for embed in embeds:
            await self.bot.command_embed_response(ctx,embed)

    @command(name="feralgoat")
    async def get_feralgoat(self,ctx,*,stat):
        embeds = self.__get_stats_embeds(ctx,"Feral Goat","feralgoat",stat.lower().replace(" ",""))
        for embed in embeds:
            await self.bot.command_embed_response(ctx,embed)

    @command(name="chamois")
    async def get_chamois(self,ctx,*,stat):
        embeds = self.__get_stats_embeds(ctx,"Chamois","chamois",stat.lower().replace(" ",""))
        for embed in embeds:
            await self.bot.command_embed_response(ctx,embed)  

    @command(name="blackbuck")
    async def get_blackbuck(self,ctx,*,stat):
        embeds = self.__get_stats_embeds(ctx,"Blackbuck","blackbuck",stat.lower().replace(" ",""))
        for embed in embeds:
            await self.bot.command_embed_response(ctx,embed)    

    @command(name="springbok")
    async def get_springbok(self,ctx,*,stat):
        embeds = self.__get_stats_embeds(ctx,"Springbok","springbok",stat.lower().replace(" ",""))
        for embed in embeds:
            await self.bot.command_embed_response(ctx,embed)   

    @command(name="axisdeer")
    async def get_axisdeer(self,ctx,*,stat):
        embeds = self.__get_stats_embeds(ctx,"Axis Deer","axisdeer",stat.lower().replace(" ",""))
        for embed in embeds:
            await self.bot.command_embed_response(ctx,embed)  

    @command(name="roedeer")
    async def get_roedeer(self,ctx,*,stat):
        embeds = self.__get_stats_embeds(ctx,"Roe Deer","roedeer",stat.lower().replace(" ",""))
        for embed in embeds:
            await self.bot.command_embed_response(ctx,embed)

    @command(name="eurasianlynx")
    async def get_eurasianlynx(self,ctx,*,stat):
        embeds = self.__get_stats_embeds(ctx,"Eurasian Lynx","eurasianlynx",stat.lower().replace(" ",""))
        for embed in embeds:
            await self.bot.command_embed_response(ctx,embed)   

    @command(name="bighornsheep")
    async def get_bighornsheep(self,ctx,*,stat):
        embeds = self.__get_stats_embeds(ctx,"Bighorn Sheep","bighornsheep",stat.lower().replace(" ",""))
        for embed in embeds:
            await self.bot.command_embed_response(ctx,embed)

    @command(name="wildboar")
    async def get_wildboar(self,ctx,*,stat):
        embeds = self.__get_stats_embeds(ctx,"Wild Boar","wildboar",stat.lower().replace(" ",""))
        for embed in embeds:
            await self.bot.command_embed_response(ctx,embed)

    @command(name="sikadeer")
    async def get_sikadeer(self,ctx,*,stat):
        embeds = self.__get_stats_embeds(ctx,"Sika Deer","sikadeer",stat.lower().replace(" ",""))
        for embed in embeds:
            await self.bot.command_embed_response(ctx,embed)    

    @command(name="pronghorn")
    async def get_pronghorn(self,ctx,*,stat):
        embeds = self.__get_stats_embeds(ctx,"Pronghorn","pronghorn",stat.lower().replace(" ",""))
        for embed in embeds:
            await self.bot.command_embed_response(ctx,embed)   

    @command(name="lesserkudu")
    async def get_lesserkudu(self,ctx,*,stat):
        embeds = self.__get_stats_embeds(ctx,"Lesser Kudu","lesserkudu",stat.lower().replace(" ",""))
        for embed in embeds:
            await self.bot.command_embed_response(ctx,embed)  

    @command(name="warthog")
    async def get_warthog(self,ctx,*,stat):
        embeds = self.__get_stats_embeds(ctx,"Warthog","warthog",stat.lower().replace(" ",""))
        for embed in embeds:
            await self.bot.command_embed_response(ctx,embed)     

    @command(name="iberianmouflon")
    async def get_iberianmouflon(self,ctx,*,stat):
        embeds = self.__get_stats_embeds(ctx,"Iberian Mouflon","iberianmouflon",stat.lower().replace(" ",""))
        for embed in embeds:
            await self.bot.command_embed_response(ctx,embed)     

    @command(name="beceiteibex")
    async def get_beceiteibex(self,ctx,*,stat):
        embeds = self.__get_stats_embeds(ctx,"Beceite Ibex","beceiteibex",stat.lower().replace(" ",""))
        for embed in embeds:
            await self.bot.command_embed_response(ctx,embed)     

    @command(name="gredosibex")
    async def get_gredosibex(self,ctx,*,stat):
        embeds = self.__get_stats_embeds(ctx,"Gredos Ibex","gredosibex",stat.lower().replace(" ",""))
        for embed in embeds:
            await self.bot.command_embed_response(ctx,embed)     

    @command(name="southeasternspanishibex", aliases=["spanishibex"])
    async def get_southeasternspanishibex(self,ctx,*,stat):
        embeds = self.__get_stats_embeds(ctx,"Southeastern Spanish Ibex","southeasternspanisibex",stat.lower().replace(" ",""))
        for embed in embeds:
            await self.bot.command_embed_response(ctx,embed)     

    @command(name="rondaibex")
    async def get_rondaibex(self,ctx,*,stat):
        embeds = self.__get_stats_embeds(ctx,"Ronda Ibex","rondaibex",stat.lower().replace(" ",""))
        for embed in embeds:
            await self.bot.command_embed_response(ctx,embed)       

    @command(name="fallowdeer")
    async def get_fallowdeer(self,ctx,*,stat):
        embeds = self.__get_stats_embeds(ctx,"Fallow Deer","fallowdeer",stat.lower().replace(" ",""))
        for embed in embeds:
            await self.bot.command_embed_response(ctx,embed)

    @command(name="blacktaildeer")
    async def get_blacktaildeer(self,ctx,*,stat):
        embeds = self.__get_stats_embeds(ctx,"Blacktail Deer","blacktaildeer",stat.lower().replace(" ",""))
        for embed in embeds:
            await self.bot.command_embed_response(ctx,embed)      

    @command(name="whitetaildeer")
    async def get_whitetaildeer(self,ctx,*,stat):
        embeds = self.__get_stats_embeds(ctx,"Whitetail Deer","whitetaildeer",stat.lower().replace(" ",""))
        for embed in embeds:
            await self.bot.command_embed_response(ctx,embed)

    @command(name="feralpig")
    async def get_feralpig(self,ctx,*,stat):
        embeds = self.__get_stats_embeds(ctx,"Feral Pig","feralpig",stat.lower().replace(" ",""))
        for embed in embeds:
            await self.bot.command_embed_response(ctx,embed)     

    @command(name="mountaingoat")
    async def get_smountaingoat(self,ctx,*,stat):
        embeds = self.__get_stats_embeds(ctx,"Mountain Goat","mountaingoat",stat.lower().replace(" ",""))
        for embed in embeds:
            await self.bot.command_embed_response(ctx,embed)     

    @command(name="puma",aliases=["pumas", "pew-muh"])
    async def get_spuma(self,ctx,*,stat):
        embeds = self.__get_stats_embeds(ctx,"Puma","puma",stat.lower().replace(" ",""))
        for embed in embeds:
            await self.bot.command_embed_response(ctx,embed)     

    @command(name="mountainlion",aliases=["mountainlions", "mountainloin", "cliffkitty", "angrymeow"])
    async def get_mountainlion(self,ctx,*,stat):
        embeds = self.__get_stats_embeds(ctx,"Mountain Lion","mountainlion",stat.lower().replace(" ",""))
        for embed in embeds:
            await self.bot.command_embed_response(ctx,embed)    

    @command(name="iberianwolf",aliases=["iberianwolves", "iberianwouflon"])
    async def get_iberianwolf(self,ctx,*,stat):
        embeds = self.__get_stats_embeds(ctx,"Iberian Wolf","iberianwolf",stat.lower().replace(" ",""))
        for embed in embeds:
            await self.bot.command_embed_response(ctx,embed)

    @command(name="graywolf",aliases=["graywolves", "greywolf", "graywoof" ])
    async def get_graywolf(self,ctx,*,stat):
        embeds = self.__get_stats_embeds(ctx,"Gray Wolf","graywolf",stat.lower().replace(" ",""))
        for embed in embeds:
            await self.bot.command_embed_response(ctx,embed)       

    @command(name="bluewildebeest")
    async def get_bluewildebeest(self,ctx,*,stat):
        embeds = self.__get_stats_embeds(ctx,"Blue Wildebeest","bluewildebeest",stat.lower().replace(" ",""))
        for embed in embeds:
            await self.bot.command_embed_response(ctx,embed)     

    @command(name="muledeer")
    async def get_muledeer(self,ctx,*,stat):
        embeds = self.__get_stats_embeds(ctx,"Mule Deer","muledeer",stat.lower().replace(" ",""))
        for embed in embeds:
            await self.bot.command_embed_response(ctx,embed)    

    @command(name="reddeer")
    async def get_reddeer(self,ctx,*,stat):
        embeds = self.__get_stats_embeds(ctx,"Red Deer","reddeer",stat.lower().replace(" ",""))
        for embed in embeds:
            await self.bot.command_embed_response(ctx,embed)      

    @command(name="reindeer")
    async def get_reindeer(self,ctx,*,stat):
        embeds = self.__get_stats_embeds(ctx,"Reindeer","reindeer",stat.lower().replace(" ",""))
        for embed in embeds:
            await self.bot.command_embed_response(ctx,embed)     

    @command(name="caribou")
    async def get_caribou(self,ctx,*,stat):
        embeds = self.__get_stats_embeds(ctx,"Caribou","caribouk",stat.lower().replace(" ",""))
        for embed in embeds:
            await self.bot.command_embed_response(ctx,embed)   

    @command(name="blackbear")
    async def get_blackbear(self,ctx,*,stat):
        embeds = self.__get_stats_embeds(ctx,"Black Bear","blackbear",stat.lower().replace(" ",""))
        for embed in embeds:
            await self.bot.command_embed_response(ctx,embed)    

    @command(name="grizzlybear",aliases=["grizzly","grizzlybears","grizzlies", "grizz", "grizzledbear", "skingrizz"])
    async def get_grizzlybear(self,ctx,*,stat):
        embeds = self.__get_stats_embeds(ctx,"Grizzly Bear","grizzlybear",stat.lower().replace(" ",""))
        for embed in embeds:
            await self.bot.command_embed_response(ctx,embed)

    @command(name="eurasianbrownbear", aliases=["brownbear"])
    async def get_eurasianbrownbear(self,ctx,*,stat):
        embeds = self.__get_stats_embeds(ctx,"Eurasian Brown Bear","eurasianbrownbear",stat.lower().replace(" ",""))
        for embed in embeds:
            await self.bot.command_embed_response(ctx,embed)     

    @command(name="gemsbok",aliases=["gemsboks", "southafricanoryx"])
    async def get_gemsbok(self,ctx,*,stat):
        embeds = self.__get_stats_embeds(ctx,"Gemsbok","gemsbok",stat.lower().replace(" ",""))
        for embed in embeds:
            await self.bot.command_embed_response(ctx,embed)     

    @command(name="rockymountainelk",aliases=["mountainelk","rockymountainelks","mountainelks", "rme"])
    async def get_rockymountainelk(self,ctx,*,stat):
        embeds = self.__get_stats_embeds(ctx,"Rocky Mountain Elk","rockymountainelk",stat.lower().replace(" ",""))
        for embed in embeds:
            await self.bot.command_embed_response(ctx,embed)    

    @command(name="rooseveltelk",aliases=["rooseveltelks", "roosy"])
    async def get_rooseveltelk(self,ctx,*,stat):
        embeds = self.__get_stats_embeds(ctx,"Roosevelt Elk","rooseveltelk",stat.lower().replace(" ",""))
        for embed in embeds:
            await self.bot.command_embed_response(ctx,embed)    

    @command(name="moose",aliases=["mooses", "meese"])
    async def get_moose(self,ctx,*,stat):
        embeds = self.__get_stats_embeds(ctx,"Moose","moose",stat.lower().replace(" ",""))
        for embed in embeds:
            await self.bot.command_embed_response(ctx,embed)    

    @command(name="waterbuffalo",aliases=["waterbuffalos", "hydro-moo", "water-moo", "hydro-cow"])
    async def get_waterbuffalo(self,ctx,*,stat):
        embeds = self.__get_stats_embeds(ctx,"Water Buffalo","waterbuffalo",stat.lower().replace(" ",""))
        for embed in embeds:
            await self.bot.command_embed_response(ctx,embed)   

    @command(name="capebuffalo")
    async def get_capebuffalo(self,ctx,*,stat):
        embeds = self.__get_stats_embeds(ctx,"Cape Buffalo","capebuffalo",stat.lower().replace(" ",""))
        for embed in embeds:
            await self.bot.command_embed_response(ctx,embed)     

    @command(name="lion")
    async def get_lion(self,ctx,*,stat):
        embeds = self.__get_stats_embeds(ctx,"Lion","lion",stat.lower().replace(" ",""))
        for embed in embeds:
            await self.bot.command_embed_response(ctx,embed) 

    @command(name="plainsbison",aliases=["plainsbisons", "plainsboi"])
    async def get_plainsbison(self,ctx,*,stat):
        embeds = self.__get_stats_embeds(ctx,"Plains Bison","plainsbison",stat.lower().replace(" ",""))
        for embed in embeds:
            await self.bot.command_embed_response(ctx,embed)

    @command(name="europeanbison")
    async def get_europeanbison(self,ctx,*,stat):
        embeds = self.__get_stats_embeds(ctx,"European Bison","europeanbison",stat.lower().replace(" ",""))
        for embed in embeds:
            await self.bot.command_embed_response(ctx,embed) 

    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("hunt")

def setup(bot):
    bot.add_cog(Hunt(bot))