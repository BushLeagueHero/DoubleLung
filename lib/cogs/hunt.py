import json
from difflib import get_close_matches as matches
from datetime import datetime

from discord import Member
from discord.ext.commands import Cog
from discord.ext.commands import command
from discord import Intents, Embed, File

hunt_array = json.load(open("./lib/db/hunt.json"))
stat_description = {"class"         :       "Class",
                    "difficulty"    :       "Max Difficulty",
                    "maxweight"     :       "Maximum Weight",
                    "silverscore"   :       "Minimum Silver Score",
                    "goldscore"     :       "Minimum Gold Score",
                    "diamondscore"  :       "Minimum Diamond Score",
                    "maxscore"      :       "Maximum Score",
                    "location"      :       "Location",
                    "fur"           :       "Fur Types",
                    "behavior"      :       "Behavior Traits",
                    "habitat"       :       "Habitat",
                    "detection"     :       "Detection Traits",
                    "social"        :       "Social Traits",
                    "active"        :       "Activity Cycle",
                    "feed"          :       "Feed Times",
                    "drink"         :       "Drink Times",
                    "rest"          :       "Rest Times",
                    "unknown"       :       "Unkown Need Zone Times",
                    "rifleammo"     :       "Rifle Ammo",
                    "pistolammo"    :       "Pistol Ammo",
                    "shotgunammo"   :       "Shotgun Ammo",
                    "bowammo"       :       "Arrow and Bolt",
                    "rifle"         :       "Usable Rifles",
                    "pistol"        :       "Usable Pistols",
                    "shotgun"       :       "Usable Shotguns",
                    "bow"           :       "Usable Bows and Crossbows",
                    "scent"         :       "Scents Available",
                    "caller"        :       "Effective Callers"}
general_stats =    {"class"         :       ["Class",False],
                    "location"      :       ["Location",True],
                    "fur"           :       ["Fur Types",True],
                    "behavior"      :       ["Behavior Traits",False],
                    "habitat"       :       ["Habitat",False],
                    "detection"     :       ["Detection Traits",False],
                    "social"        :       ["Social Traits",False],
                    "active"        :       ["High Activity Level",False]}
score_stats =      {"difficulty"    :       ["Max Difficulty",True],
                    "maxweight"     :       ["Maximum Weight",True],
                    "maxscore"      :       ["Max Score",True],
                    "silverscore"   :       ["Min Silver",True],
                    "goldscore"     :       ["Min Gold",True],
                    "diamondscore"  :       ["Min Diamond",True]}
need_stats =       {"feed"          :       ["Feed Times",True],
                    "drink"         :       ["Drink Times",True],
                    "rest"          :       ["Rest Times",True],
                    "unknown"       :       ["Unkown Need Zone Times",False]}
equipment_stats =  {"rifleammo"     :       ["Rifle Ammo",True],
                    "rifle"         :       ["Usable Rifles",True],
                    "break1"        :       ["\u200b",True],
                    "pistolammo"    :       ["Pistol Ammo",True],
                    "pistol"        :       ["Usable Pistols",True],
                    "break2"        :       ["\u200b",True],
                    "shotgunammo"   :       ["Shotgun Ammo",True],
                    "shotgun"       :       ["Usable Shotguns",True],
                    "break3"        :       ["\u200b",True],
                    "bowammo"       :       ["Arrow and Bolt ",True],
                    "bow"           :       ["Usable Bows and Crossbows",True],
                    "break4"        :       ["\u200b",True],
                    "caller"        :       ["Effective Callers",True],
                    "scent"         :       ["Scents Available",True],
                    "break5"        :       ["\u200b",True]}

dt = datetime.now()
dt_formatted = dt.strftime("%b %d %Y %H:%M:%S")

class Hunt(Cog):
    def __init__(self, bot):
        self.bot = bot

    async def get_stats(self,ctx,user_hunt,user_stat,embed):
        if user_stat=="all":
            for key in general_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=general_stats[key][0], value="\n".join(i for i in stat_data), inline=general_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")

            await self.bot.stdout.send(embed=embed)
            embed.clear_fields()

            for key in score_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=score_stats[key][0], value="\n".join(i for i in stat_data), inline=score_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)
            embed.clear_fields()
            
            for key in need_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=need_stats[key][0], value="\n".join(i for i in stat_data), inline=need_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)
            embed.clear_fields()
        
            for key in equipment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equipment_stats[key][0], value="\n".join(i for i in stat_data), inline=equipment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)
            embed.clear_fields()

        elif user_stat=="general":
            for key in general_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=general_stats[key][0], value="\n".join(i for i in stat_data), inline=general_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="score" or user_stat=="scores":
            for key in score_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=score_stats[key][0], value="\n".join(i for i in stat_data), inline=score_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")

            await self.bot.stdout.send(embed=embed)

        elif user_stat=="need" or user_stat=="needs" or user_stat=="zone" or user_stat=="zones":
            for key in need_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=need_stats[key][0], value="\n".join(i for i in stat_data), inline=need_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="equipment" or user_stat=="item" or user_stat=="items":
            for key in equipment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equipment_stats[key][0], value="\n".join(i for i in stat_data), inline=equipment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        else:
            stat_data = hunt_array[user_hunt][0][user_stat]

            embed.add_field(name=stat_description[user_stat], value="\n".join(i for i in stat_data), inline=True)
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

    @command(name="mallard",aliases=["mallards"])
    async def get_mallard(self,ctx,*,stat):
        user_hunt = "mallard"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Mallard", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
        await self.get_stats(ctx,user_hunt,user_stat,embed)

    @command(name="scrubhare",aliases=["scrubhares"])
    async def get_scrubhare(self,ctx,*,stat):
        user_hunt = "scrubhare"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Scrub Hare", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
        await self.get_stats(ctx,user_hunt,user_stat,embed)

    @command(name="jackrabbit",aliases=["jackrabbits"])
    async def get_jackrabbit(self,ctx,*,stat):
        user_hunt = "jackrabbit"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Jackrabbit", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
        await self.get_stats(ctx,user_hunt,user_stat,embed)

    @command(name="harlequinduck",aliases=["harlequinducks","harlequin","harlequins"])
    async def get_harlequinduck(self,ctx,*,stat):
        user_hunt = "harlequinduck"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Harlequin Duck", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
        await self.get_stats(ctx,user_hunt,user_stat,embed)  

    @command(name="turkey",aliases=["turkeys","turkies"])
    async def get_turkey(self,ctx,*,stat):
        user_hunt = "turkey"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Turkey", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
        await self.get_stats(ctx,user_hunt,user_stat,embed)  

    @command(name="canadagoose",aliases=["canadageese"])
    async def get_canadagoose(self,ctx,*,stat):
        user_hunt = "canadagoose"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Canada Goose", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
        await self.get_stats(ctx,user_hunt,user_stat,embed)  

    @command(name="europeanrabbit",aliases=["europeanrabbits"])
    async def get_europeanrabbit(self,ctx,*,stat):
        user_hunt = "europeanrabbit"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="European Rabbit", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
        await self.get_stats(ctx,user_hunt,user_stat,embed)

    @command(name="europeanhare",aliases=["europeanhareas"])
    async def get_europeanhare(self,ctx,*,stat):
        user_hunt = "europeanhare"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="European Hare", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
        await self.get_stats(ctx,user_hunt,user_stat,embed) 

    @command(name="cinnamonteal",aliases=["cinnamonteals"])
    async def get_cinnamonteal(self,ctx,*,stat):
        user_hunt = "cinnamonteal"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Cinnamon Teal", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
        await self.get_stats(ctx,user_hunt,user_stat,embed)

    @command(name="sidestripedjackal",aliases=["sidestripedjackals","side-stripedjackal","side-stripedjackals","stripedjackal","stripedjackals","jackal","jackals"])
    async def get_sidestripedjackal(self,ctx,*,stat):
        user_hunt = "sidestripedjackal"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Side-Striped Jackal", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
        await self.get_stats(ctx,user_hunt,user_stat,embed)

    @command(name="coyote",aliases=["coyotes"])
    async def get_coyote(self,ctx,*,stat):
        user_hunt = "coyote"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Coyote", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
        await self.get_stats(ctx,user_hunt,user_stat,embed)

    @command(name="siberianmuskdeer",aliases=["muskdeer","siberianmuskdeers","muskdeers"])
    async def get_siberianmuskdeer(self,ctx,*,stat):
        user_hunt = "siberianmuskdeer"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Siberian Muskdeer", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
        await self.get_stats(ctx,user_hunt,user_stat,embed)

    @command(name="redfox",aliases=["redfoxes"])
    async def get_redfox(self,ctx,*,stat):
        user_hunt = "redfox"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Red Fox", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
        await self.get_stats(ctx,user_hunt,user_stat,embed)

    @command(name="feralgoat",aliases=["feralgoats"])
    async def get_feralgoat(self,ctx,*,stat):
        user_hunt = "feralgoat"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Feral Goat", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
        await self.get_stats(ctx,user_hunt,user_stat,embed)   

    @command(name="chamois",aliases=["chamoises"])
    async def get_chamois(self,ctx,*,stat):
        user_hunt = "chamois"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Chamois", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
        await self.get_stats(ctx,user_hunt,user_stat,embed)      

    @command(name="blackbuck",aliases=["blackbucks"])
    async def get_blackbuck(self,ctx,*,stat):
        user_hunt = "blackbuck"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Blackbuck", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
        await self.get_stats(ctx,user_hunt,user_stat,embed)      

    @command(name="springbok",aliases=["springboks"])
    async def get_springbok(self,ctx,*,stat):
        user_hunt = "springbok"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Springbok", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
        await self.get_stats(ctx,user_hunt,user_stat,embed)     

    @command(name="axisdeer",aliases=["axisdeers"])
    async def get_axisdeer(self,ctx,*,stat):
        user_hunt = "axisdeer"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Axis Deer", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
        await self.get_stats(ctx,user_hunt,user_stat,embed)    

    @command(name="roedeer",aliases=["roedeers"])
    async def get_roedeer(self,ctx,*,stat):
        user_hunt = "roedeer"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Roe Deer", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
        await self.get_stats(ctx,user_hunt,user_stat,embed)      

    @command(name="eurasianlynx",aliases=["eurasianlynxes"])
    async def get_eurasianlynx(self,ctx,*,stat):
        user_hunt = "eurasianlynx"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Eurasian Lynx", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
        await self.get_stats(ctx,user_hunt,user_stat,embed)       

    @command(name="bighornsheep",aliases=["bighornsheeps","hornsheep","hornsheeps"])
    async def get_bighornsheep(self,ctx,*,stat):
        user_hunt = "bighornsheep"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Bighorn Sheep", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
        await self.get_stats(ctx,user_hunt,user_stat,embed)    

    @command(name="wildboar",aliases=["wildboars"])
    async def get_wildboar(self,ctx,*,stat):
        user_hunt = "wildboar"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Wild Boar", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
        await self.get_stats(ctx,user_hunt,user_stat,embed)

    @command(name="sikadeer",aliases=["sika","sikadeers","sikas"])
    async def get_sikadeer(self,ctx,*,stat):
        user_hunt = "sikadeer"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Sika Deer", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
        await self.get_stats(ctx,user_hunt,user_stat,embed)       

    @command(name="pronghorn",aliases=["pronghorns"])
    async def get_pronghorn(self,ctx,*,stat):
        user_hunt = "pronghorn"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Pronghorn", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
        await self.get_stats(ctx,user_hunt,user_stat,embed)       

    @command(name="lesserkudu",aliases=["kudu","lesserkudus","kudus"])
    async def get_lesserkudu(self,ctx,*,stat):
        user_hunt = "lesserkudu"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Lesser Kudu", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
        await self.get_stats(ctx,user_hunt,user_stat,embed)       

    @command(name="warthog",aliases=["warthogs"])
    async def get_warthog(self,ctx,*,stat):
        user_hunt = "warthog"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Warthog", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
        await self.get_stats(ctx,user_hunt,user_stat,embed)       

    @command(name="iberianmouflon",aliases=["mouflon","iberianmouflons","mouflons"])
    async def get_iberianmouflon(self,ctx,*,stat):
        user_hunt = "iberianmouflon"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Iberian Mouflon", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
        await self.get_stats(ctx,user_hunt,user_stat,embed)       

    @command(name="beceiteibex",aliases=["beceiteibexes"])
    async def get_beceiteibex(self,ctx,*,stat):
        user_hunt = "beceiteibex"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Beceite Ibex", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
        await self.get_stats(ctx,user_hunt,user_stat,embed)      

    @command(name="gredosibex",aliases=["gredosibexes"])
    async def get_gredosibex(self,ctx,*,stat):
        user_hunt = "gredosibex"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Gredos Ibex", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
        await self.get_stats(ctx,user_hunt,user_stat,embed)      

    @command(name="southeasternspanishibex", aliases=["spanishibex","southeasternspanishibexes","spanishibexes"])
    async def get_southeasternspanishibex(self,ctx,*,stat):
        user_hunt = "southeasternspanishibex"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Southeastern Spanish Ibex", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
        await self.get_stats(ctx,user_hunt,user_stat,embed)        

    @command(name="rondaibex",aliases=["rondaibexes"])
    async def get_rondaibex(self,ctx,*,stat):
        user_hunt = "rondaibex"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Ronda Ibex", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
        await self.get_stats(ctx,user_hunt,user_stat,embed)        

    @command(name="fallowdeer",aliases=["fallow","fallowdeers","fallows"])
    async def get_fallowdeer(self,ctx,*,stat):
        user_hunt = "fallowdeer"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Fallow Deer", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
        await self.get_stats(ctx,user_hunt,user_stat,embed)

    @command(name="blacktaildeer",aliases=["blacktail","blacktaildeers","blacktails"])
    async def get_blacktaildeer(self,ctx,*,stat):
        user_hunt = "blacktaildeer"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Blacktail Deer", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
        await self.get_stats(ctx,user_hunt,user_stat,embed)       

    @command(name="whitetaildeer",aliases=["whitetail","whitetaildeers","whitetails"])
    async def get_whitetaildeer(self,ctx,*,stat):
        user_hunt = "whitetaildeer"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Whitetail Deer", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
        await self.get_stats(ctx,user_hunt,user_stat,embed)

    @command(name="feralpig",aliases=["feralpigs"])
    async def get_feralpig(self,ctx,*,stat):
        user_hunt = "feralpig"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Feral Pig", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
        await self.get_stats(ctx,user_hunt,user_stat,embed)        

    @command(name="mountaingoat",aliases=["mountaingoats"])
    async def get_smountaingoat(self,ctx,*,stat):
        user_hunt = "mountaingoat"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Mountain Goat", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
        await self.get_stats(ctx,user_hunt,user_stat,embed)       

    @command(name="puma",aliases=["pumas"])
    async def get_spuma(self,ctx,*,stat):
        user_hunt = "puma"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Puma", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
        await self.get_stats(ctx,user_hunt,user_stat,embed)       

    @command(name="mountainlion",aliases=["mountainlions"])
    async def get_mountainlion(self,ctx,*,stat):
        user_hunt = "mountainlion"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Mountain Lion", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
        await self.get_stats(ctx,user_hunt,user_stat,embed)      

    @command(name="iberianwolf",aliases=["iberianwolves"])
    async def get_iberianwolf(self,ctx,*,stat):
        user_hunt = "iberianwolf"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Iberian Wolf", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
        await self.get_stats(ctx,user_hunt,user_stat,embed)

    @command(name="graywolf",aliases=["graywolves"])
    async def get_graywolf(self,ctx,*,stat):
        user_hunt = "graywolf"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Gray Wolf", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
        await self.get_stats(ctx,user_hunt,user_stat,embed)        

    @command(name="bluewildebeest",aliases=["wildebeest","bluewildebeests","wildebeests"])
    async def get_bluewildebeest(self,ctx,*,stat):
        user_hunt = "bluewildebeest"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Blue Wildebeest", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
        await self.get_stats(ctx,user_hunt,user_stat,embed)        

    @command(name="muledeer",aliases=["muledeers"])
    async def get_muledeer(self,ctx,*,stat):
        user_hunt = "muledeer"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Mule Deer", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
        await self.get_stats(ctx,user_hunt,user_stat,embed)       

    @command(name="reddeer",aliases=["reddeers"])
    async def get_reddeer(self,ctx,*,stat):
        user_hunt = "reddeer"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Red Deer", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
        await self.get_stats(ctx,user_hunt,user_stat,embed)        

    @command(name="reindeer",aliases=["reindeers"])
    async def get_reindeer(self,ctx,*,stat):
        user_hunt = "reindeer"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Reindeer", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
        await self.get_stats(ctx,user_hunt,user_stat,embed)       

    @command(name="caribou",aliases=["caribous"])
    async def get_caribou(self,ctx,*,stat):
        user_hunt = "caribouk"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Caribou", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
        await self.get_stats(ctx,user_hunt,user_stat,embed)      

    @command(name="blackbear",aliases=["blackbears"])
    async def get_blackbear(self,ctx,*,stat):
        user_hunt = "blackbear"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Black Bear", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
        await self.get_stats(ctx,user_hunt,user_stat,embed)      

    @command(name="grizzlybear",aliases=["grizzly","grizzlybears","grizzlies"])
    async def get_grizzlybear(self,ctx,*,stat):
        user_hunt = "grizzlybear"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Grizzly Bear", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
        await self.get_stats(ctx,user_hunt,user_stat,embed)

    @command(name="eurasianbrownbear", aliases=["brownbear","eurasianbrownbears","brownbears"])
    async def get_eurasianbrownbear(self,ctx,*,stat):
        user_hunt = "eurasianbrownbear"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Eurasian Brown Bear", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
        await self.get_stats(ctx,user_hunt,user_stat,embed)     

    @command(name="gemsbok",aliases=["gemsboks"])
    async def get_gemsbok(self,ctx,*,stat):
        user_hunt = "gemsbok"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Gemsbok", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
        await self.get_stats(ctx,user_hunt,user_stat,embed)       

    @command(name="rockymountainelk",aliases=["mountainelk","rockymountainelks","mountainelks"])
    async def get_rockymountainelk(self,ctx,*,stat):
        user_hunt = "rockymountainelk"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Rockymountain Elk", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
        await self.get_stats(ctx,user_hunt,user_stat,embed)      

    @command(name="rooseveltelk",aliases=["rooseveltelks"])
    async def get_rooseveltelk(self,ctx,*,stat):
        user_hunt = "rooseveltelk"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Roosevelt Elk", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
        await self.get_stats(ctx,user_hunt,user_stat,embed)       

    @command(name="moose",aliases=["mooses"])
    async def get_moose(self,ctx,*,stat):
        user_hunt = "moose"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Moose", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
        await self.get_stats(ctx,user_hunt,user_stat,embed)      

    @command(name="waterbuffalo",aliases=["waterbuffalos"])
    async def get_waterbuffalo(self,ctx,*,stat):
        user_hunt = "waterbuffalo"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Water Buffalo", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
        await self.get_stats(ctx,user_hunt,user_stat,embed)      

    @command(name="capebuffalo",aliases=["capebuffalos"])
    async def get_capebuffalo(self,ctx,*,stat):
        user_hunt = "capebuffalo"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Cape Buffalo", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
        await self.get_stats(ctx,user_hunt,user_stat,embed)       

    @command(name="lion",aliases=["llions"])
    async def get_lion(self,ctx,*,stat):
        user_hunt = "lion"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Lion", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
        await self.get_stats(ctx,user_hunt,user_stat,embed)      

    @command(name="plainsbison",aliases=["plainsbisons"])
    async def get_plainsbison(self,ctx,*,stat):
        user_hunt = "plainsbison"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Plains Bison", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
        await self.get_stats(ctx,user_hunt,user_stat,embed)       

    @command(name="europeanbison",aliases=["europeanbisons"])
    async def get_europeanbison(self,ctx,*,stat):
        user_hunt = "europeanbison"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="European Bison", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
        await self.get_stats(ctx,user_hunt,user_stat,embed)       

    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("hunt")

def setup(bot):
    bot.add_cog(Hunt(bot))