import json
from datetime import datetime

from discord import Member
from discord.ext.commands import Cog
from discord.ext.commands import command
from discord import Intents, Embed, File

hunt_array = json.load(open("./lib/db/hunt.json"))
stat_description = {"class"         :       "Class",
                    "difficulty"    :       "Max Difficulty",
                    "maxweight"     :       "Maximum Weight",
                    "silver"        :       "Minimum Silver Score",
                    "gold"          :       "Minimum Gold Score",
                    "diamond"       :       "Minimum Diamond Score",
                    "maxscore"      :       "Maximum Score",
                    "location"      :       "Location",
                    "fur"           :       "Fur Types",
                    "behavior"      :       "Behavior Traits",
                    "habitat"       :       "Habitat",
                    "senses"        :       "Senses Qualities",
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
                    "rifles"         :       "Usable Rifles",
                    "pistols"        :       "Usable Pistols",
                    "shotguns"       :       "Usable Shotguns",
                    "bows"           :       "Usable Bows and Crossbows",
                    "scents"         :       "Scents Available",
                    "callers"        :       "Effective Callers"}
general_stats = {   "class"         :       ["Class",False],
                    "location"      :       ["Location",True],
                    "fur"           :       ["Fur Types",True],
                    "behavior"      :       ["Behavior Traits",False],
                    "habitat"       :       ["Habitat",False],
                    "senses"        :       ["Senses Qualities",False],
                    "social"        :       ["Social Traits",False],
                    "active"        :       ["High Activity Level",False]}
score_stats = {     "difficulty"    :       ["Max Difficulty",True],
                    "maxweight"     :       ["Maximum Weight",True],
                    "maxscore"      :       ["Max Score",False],
                    "silver"        :       ["Min Silver",True],
                    "gold"          :       ["Min Gold",True],
                    "diamond"       :       ["Min Diamond",True]}
need_stats = {      "feed"          :       ["Feed Times",False],
                    "drink"         :       ["Drink Times",False],
                    "rest"          :       ["Rest Times",False],
                    "unknown"       :       ["Unkown Need Zone Times",False]}
equiptment_stats = {"rifleammo"     :       ["Rifle Ammo",False],
                    "rifles"         :       ["Usable Rifles",True],
                    "pistolammo"    :       ["Pistol Ammo",False],
                    "pistols"        :       ["Usable Pistols",True],
                    "shotgunammo"   :       ["Shotgun Ammo",False],
                    "shotguns"       :       ["Usable Shotguns",True],
                    "bowammo"       :       ["Arrow and Bolt ",False],
                    "bows"           :       ["Usable Bows and Crossbows",False],
                    "scents"         :       ["Scents Available",False],
                    "callers"        :       ["Effective Callers",False]}

dt = datetime.now()
dt_formatted = dt.strftime("%b %d %Y %H:%M:%S")

class Hunt(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command(name="commands")
    async def show_commands(self,ctx):
        embed = Embed(title="Available Stats", description="Hunt commands start with the animal name (no spaces), and then a stat value.", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)

        fields =    [("Hunt Commands","mallard, scrubhare, jackrabbit, harlequinduck, turkey, canadagoose, europeanrabbit, europeanhare, cinnamonteal, sidestripedjackal, coyote, siberianmuskdeer, redfox, feralgoat, chamois, blackbuck, springbok, axisdeer, roedeer, eurasianlynx, bighornsheep, wildboar, sikadeer, pronghorn, lesserkudu, warthog, iberianmouflon, beceiteibex, gredosibex, southeasternspanishibex, rondaibex, fallowdeer, blacktaildeer, whitetaildeer, feralpig, mountaingoat, puma, mountainlion, iberianwolf, graywolf, bluewildebeest, muledeer, reddeer, reindeer, caribou, blackbear, grizzlybear, eurasianbrownbear, gemsbok, rockymountainelk, rooseveltelk, moose, waterbuffalo, capebuffalo, lion, plainsbison, europeanbison",False),
                    ("Grouped Stats","All, General, Score, Needs, Equiptment",False),
                    ("Individual Stats","Class, Difficulty, Max Weight, Silver, Gold, Diamond, Max Score, Location, Fur, Behavior, Habitat, Senses, Social, Active, Feed, Drink, Rest, Unknown, Rifle Ammo, Pistol Ammo, Shotgun Ammo, Bow Ammo, Rifles, Pistols, Shotguns, Bows, Scents, Callers",False),
                    ("Hunt Command Examples","!coyote all, !whitetaildeer max weight, !pronghorn score",False)]

        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)

        embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
        await self.bot.stdout.send(embed=embed)

        await ctx.message.delete()

    @command(name="mallard")
    async def get_mallard(self,ctx,*,stat):
        user_hunt = "mallard"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Mallard", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
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
            
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)
            embed.clear_fields()

        elif user_stat=="general":
            for key in general_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=general_stats[key][0], value="\n".join(i for i in stat_data), inline=general_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="score":
            embed = Embed(title="Mallard", color=0xFF0000)
            embed.set_author(name="DoubleLung Bot")
            embed.set_thumbnail(url=self.bot.guild.icon_url)

            for key in score_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=score_stats[key][0], value="\n".join(i for i in stat_data), inline=score_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="needs":
            for key in need_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=need_stats[key][0], value="\n".join(i for i in stat_data), inline=need_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="equiptment":
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        else:
            stat_data = hunt_array[user_hunt][0][user_stat]

            embed.add_field(name=stat_description[user_stat], value="\n".join(i for i in stat_data), inline=True)
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        await ctx.message.delete()

    @command(name="scrubhare")
    async def get_scrubhare(self,ctx,*,stat):
        user_hunt = "scrubhare"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Scrub Hare", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
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
            
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)
            embed.clear_fields()

        elif user_stat=="general":
            for key in general_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=general_stats[key][0], value="\n".join(i for i in stat_data), inline=general_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="score":
            embed = Embed(title="Mallard", color=0xFF0000)
            embed.set_author(name="DoubleLung Bot")
            embed.set_thumbnail(url=self.bot.guild.icon_url)

            for key in score_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=score_stats[key][0], value="\n".join(i for i in stat_data), inline=score_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="needs":
            for key in need_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=need_stats[key][0], value="\n".join(i for i in stat_data), inline=need_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="equiptment":
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        else:
            stat_data = hunt_array[user_hunt][0][user_stat]

            embed.add_field(name=stat_description[user_stat], value="\n".join(i for i in stat_data), inline=True)
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        await ctx.message.delete()

    @command(name="jackrabbit")
    async def get_jackrabbit(self,ctx,*,stat):
        user_hunt = "jackrabbit"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Jackrabbit", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
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
            
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)
            embed.clear_fields()

        elif user_stat=="general":
            for key in general_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=general_stats[key][0], value="\n".join(i for i in stat_data), inline=general_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="score":
            embed = Embed(title="Mallard", color=0xFF0000)
            embed.set_author(name="DoubleLung Bot")
            embed.set_thumbnail(url=self.bot.guild.icon_url)

            for key in score_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=score_stats[key][0], value="\n".join(i for i in stat_data), inline=score_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="needs":
            for key in need_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=need_stats[key][0], value="\n".join(i for i in stat_data), inline=need_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="equiptment":
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        else:
            stat_data = hunt_array[user_hunt][0][user_stat]

            embed.add_field(name=stat_description[user_stat], value="\n".join(i for i in stat_data), inline=True)
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        await ctx.message.delete()

    @command(name="harlequinduck")
    async def get_harlequinduck(self,ctx,*,stat):
        user_hunt = "harlequinduck"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Harlequin Duck", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
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
            
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)
            embed.clear_fields()

        elif user_stat=="general":
            for key in general_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=general_stats[key][0], value="\n".join(i for i in stat_data), inline=general_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="score":
            embed = Embed(title="Mallard", color=0xFF0000)
            embed.set_author(name="DoubleLung Bot")
            embed.set_thumbnail(url=self.bot.guild.icon_url)

            for key in score_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=score_stats[key][0], value="\n".join(i for i in stat_data), inline=score_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="needs":
            for key in need_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=need_stats[key][0], value="\n".join(i for i in stat_data), inline=need_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="equiptment":
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        else:
            stat_data = hunt_array[user_hunt][0][user_stat]

            embed.add_field(name=stat_description[user_stat], value="\n".join(i for i in stat_data), inline=True)
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        await ctx.message.delete()

    @command(name="turkey")
    async def get_turkey(self,ctx,*,stat):
        user_hunt = "turkey"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Turkey", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
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
            
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)
            embed.clear_fields()

        elif user_stat=="general":
            for key in general_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=general_stats[key][0], value="\n".join(i for i in stat_data), inline=general_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="score":
            embed = Embed(title="Mallard", color=0xFF0000)
            embed.set_author(name="DoubleLung Bot")
            embed.set_thumbnail(url=self.bot.guild.icon_url)

            for key in score_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=score_stats[key][0], value="\n".join(i for i in stat_data), inline=score_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="needs":
            for key in need_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=need_stats[key][0], value="\n".join(i for i in stat_data), inline=need_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="equiptment":
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        else:
            stat_data = hunt_array[user_hunt][0][user_stat]

            embed.add_field(name=stat_description[user_stat], value="\n".join(i for i in stat_data), inline=True)
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        await ctx.message.delete()

    @command(name="canadagoose")
    async def get_canadagoose(self,ctx,*,stat):
        user_hunt = "canadagoose"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Canada Goose", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
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
            
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)
            embed.clear_fields()

        elif user_stat=="general":
            for key in general_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=general_stats[key][0], value="\n".join(i for i in stat_data), inline=general_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="score":
            embed = Embed(title="Mallard", color=0xFF0000)
            embed.set_author(name="DoubleLung Bot")
            embed.set_thumbnail(url=self.bot.guild.icon_url)

            for key in score_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=score_stats[key][0], value="\n".join(i for i in stat_data), inline=score_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="needs":
            for key in need_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=need_stats[key][0], value="\n".join(i for i in stat_data), inline=need_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="equiptment":
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        else:
            stat_data = hunt_array[user_hunt][0][user_stat]

            embed.add_field(name=stat_description[user_stat], value="\n".join(i for i in stat_data), inline=True)
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        await ctx.message.delete()

    @command(name="europeanrabbit")
    async def get_europeanrabbit(self,ctx,*,stat):
        user_hunt = "europeanrabbit"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="European Rabbit", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
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
            
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)
            embed.clear_fields()

        elif user_stat=="general":
            for key in general_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=general_stats[key][0], value="\n".join(i for i in stat_data), inline=general_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="score":
            embed = Embed(title="Mallard", color=0xFF0000)
            embed.set_author(name="DoubleLung Bot")
            embed.set_thumbnail(url=self.bot.guild.icon_url)

            for key in score_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=score_stats[key][0], value="\n".join(i for i in stat_data), inline=score_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="needs":
            for key in need_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=need_stats[key][0], value="\n".join(i for i in stat_data), inline=need_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="equiptment":
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        else:
            stat_data = hunt_array[user_hunt][0][user_stat]

            embed.add_field(name=stat_description[user_stat], value="\n".join(i for i in stat_data), inline=True)
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        await ctx.message.delete()

    @command(name="europeanhare")
    async def get_europeanhare(self,ctx,*,stat):
        user_hunt = "europeanhare"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="European Hare", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
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
            
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)
            embed.clear_fields()

        elif user_stat=="general":
            for key in general_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=general_stats[key][0], value="\n".join(i for i in stat_data), inline=general_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="score":
            embed = Embed(title="Mallard", color=0xFF0000)
            embed.set_author(name="DoubleLung Bot")
            embed.set_thumbnail(url=self.bot.guild.icon_url)

            for key in score_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=score_stats[key][0], value="\n".join(i for i in stat_data), inline=score_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="needs":
            for key in need_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=need_stats[key][0], value="\n".join(i for i in stat_data), inline=need_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="equiptment":
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        else:
            stat_data = hunt_array[user_hunt][0][user_stat]

            embed.add_field(name=stat_description[user_stat], value="\n".join(i for i in stat_data), inline=True)
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        await ctx.message.delete()

    @command(name="cinnamonteal")
    async def get_cinnamonteal(self,ctx,*,stat):
        user_hunt = "cinnamonteal"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Cinnamon Teal", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
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
            
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)
            embed.clear_fields()

        elif user_stat=="general":
            for key in general_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=general_stats[key][0], value="\n".join(i for i in stat_data), inline=general_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="score":
            embed = Embed(title="Mallard", color=0xFF0000)
            embed.set_author(name="DoubleLung Bot")
            embed.set_thumbnail(url=self.bot.guild.icon_url)

            for key in score_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=score_stats[key][0], value="\n".join(i for i in stat_data), inline=score_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="needs":
            for key in need_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=need_stats[key][0], value="\n".join(i for i in stat_data), inline=need_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="equiptment":
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        else:
            stat_data = hunt_array[user_hunt][0][user_stat]

            embed.add_field(name=stat_description[user_stat], value="\n".join(i for i in stat_data), inline=True)
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        await ctx.message.delete()

    @command(name="sidestripedjackal")
    async def get_sidestripedjackal(self,ctx,*,stat):
        user_hunt = "sidestripedjackal"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Side-Striped Jackal", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
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
            
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)
            embed.clear_fields()

        elif user_stat=="general":
            for key in general_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=general_stats[key][0], value="\n".join(i for i in stat_data), inline=general_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="score":
            embed = Embed(title="Mallard", color=0xFF0000)
            embed.set_author(name="DoubleLung Bot")
            embed.set_thumbnail(url=self.bot.guild.icon_url)

            for key in score_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=score_stats[key][0], value="\n".join(i for i in stat_data), inline=score_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="needs":
            for key in need_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=need_stats[key][0], value="\n".join(i for i in stat_data), inline=need_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="equiptment":
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        else:
            stat_data = hunt_array[user_hunt][0][user_stat]

            embed.add_field(name=stat_description[user_stat], value="\n".join(i for i in stat_data), inline=True)
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        await ctx.message.delete()

    @command(name="coyote")
    async def get_coyote(self,ctx,*,stat):
        user_hunt = "coyote"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Coyote", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
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
            
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)
            embed.clear_fields()

        elif user_stat=="general":
            for key in general_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=general_stats[key][0], value="\n".join(i for i in stat_data), inline=general_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="score":
            embed = Embed(title="Mallard", color=0xFF0000)
            embed.set_author(name="DoubleLung Bot")
            embed.set_thumbnail(url=self.bot.guild.icon_url)

            for key in score_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=score_stats[key][0], value="\n".join(i for i in stat_data), inline=score_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="needs":
            for key in need_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=need_stats[key][0], value="\n".join(i for i in stat_data), inline=need_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="equiptment":
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        else:
            stat_data = hunt_array[user_hunt][0][user_stat]

            embed.add_field(name=stat_description[user_stat], value="\n".join(i for i in stat_data), inline=True)
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        await ctx.message.delete()

    @command(name="siberianmuskdeer")
    async def get_siberianmuskdeer(self,ctx,*,stat):
        user_hunt = "siberianmuskdeer"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Siberian Muskdeer", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
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
            
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)
            embed.clear_fields()

        elif user_stat=="general":
            for key in general_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=general_stats[key][0], value="\n".join(i for i in stat_data), inline=general_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="score":
            embed = Embed(title="Mallard", color=0xFF0000)
            embed.set_author(name="DoubleLung Bot")
            embed.set_thumbnail(url=self.bot.guild.icon_url)

            for key in score_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=score_stats[key][0], value="\n".join(i for i in stat_data), inline=score_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="needs":
            for key in need_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=need_stats[key][0], value="\n".join(i for i in stat_data), inline=need_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="equiptment":
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        else:
            stat_data = hunt_array[user_hunt][0][user_stat]

            embed.add_field(name=stat_description[user_stat], value="\n".join(i for i in stat_data), inline=True)
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        await ctx.message.delete()

    @command(name="redfox")
    async def get_redfox(self,ctx,*,stat):
        user_hunt = "redfox"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Red Fox", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
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
            
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)
            embed.clear_fields()

        elif user_stat=="general":
            for key in general_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=general_stats[key][0], value="\n".join(i for i in stat_data), inline=general_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="score":
            embed = Embed(title="Mallard", color=0xFF0000)
            embed.set_author(name="DoubleLung Bot")
            embed.set_thumbnail(url=self.bot.guild.icon_url)

            for key in score_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=score_stats[key][0], value="\n".join(i for i in stat_data), inline=score_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="needs":
            for key in need_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=need_stats[key][0], value="\n".join(i for i in stat_data), inline=need_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="equiptment":
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        else:
            stat_data = hunt_array[user_hunt][0][user_stat]

            embed.add_field(name=stat_description[user_stat], value="\n".join(i for i in stat_data), inline=True)
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        await ctx.message.delete()

    @command(name="feralgoat")
    async def get_feralgoat(self,ctx,*,stat):
        user_hunt = "feralgoat"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Feral Goat", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
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
            
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)
            embed.clear_fields()

        elif user_stat=="general":
            for key in general_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=general_stats[key][0], value="\n".join(i for i in stat_data), inline=general_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="score":
            embed = Embed(title="Mallard", color=0xFF0000)
            embed.set_author(name="DoubleLung Bot")
            embed.set_thumbnail(url=self.bot.guild.icon_url)

            for key in score_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=score_stats[key][0], value="\n".join(i for i in stat_data), inline=score_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="needs":
            for key in need_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=need_stats[key][0], value="\n".join(i for i in stat_data), inline=need_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="equiptment":
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        else:
            stat_data = hunt_array[user_hunt][0][user_stat]

            embed.add_field(name=stat_description[user_stat], value="\n".join(i for i in stat_data), inline=True)
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        await ctx.message.delete()

    @command(name="chamois")
    async def get_chamois(self,ctx,*,stat):
        user_hunt = "chamois"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Chamois", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
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
            
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)
            embed.clear_fields()

        elif user_stat=="general":
            for key in general_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=general_stats[key][0], value="\n".join(i for i in stat_data), inline=general_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="score":
            embed = Embed(title="Mallard", color=0xFF0000)
            embed.set_author(name="DoubleLung Bot")
            embed.set_thumbnail(url=self.bot.guild.icon_url)

            for key in score_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=score_stats[key][0], value="\n".join(i for i in stat_data), inline=score_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="needs":
            for key in need_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=need_stats[key][0], value="\n".join(i for i in stat_data), inline=need_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="equiptment":
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        else:
            stat_data = hunt_array[user_hunt][0][user_stat]

            embed.add_field(name=stat_description[user_stat], value="\n".join(i for i in stat_data), inline=True)
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        await ctx.message.delete()

    @command(name="blackbuck")
    async def get_blackbuck(self,ctx,*,stat):
        user_hunt = "blackbuck"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Blackbuck", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
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
            
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)
            embed.clear_fields()

        elif user_stat=="general":
            for key in general_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=general_stats[key][0], value="\n".join(i for i in stat_data), inline=general_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="score":
            embed = Embed(title="Mallard", color=0xFF0000)
            embed.set_author(name="DoubleLung Bot")
            embed.set_thumbnail(url=self.bot.guild.icon_url)

            for key in score_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=score_stats[key][0], value="\n".join(i for i in stat_data), inline=score_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="needs":
            for key in need_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=need_stats[key][0], value="\n".join(i for i in stat_data), inline=need_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="equiptment":
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        else:
            stat_data = hunt_array[user_hunt][0][user_stat]

            embed.add_field(name=stat_description[user_stat], value="\n".join(i for i in stat_data), inline=True)
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        await ctx.message.delete()

    @command(name="springbok")
    async def get_springbok(self,ctx,*,stat):
        user_hunt = "springbok"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Springbok", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
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
            
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)
            embed.clear_fields()

        elif user_stat=="general":
            for key in general_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=general_stats[key][0], value="\n".join(i for i in stat_data), inline=general_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="score":
            embed = Embed(title="Mallard", color=0xFF0000)
            embed.set_author(name="DoubleLung Bot")
            embed.set_thumbnail(url=self.bot.guild.icon_url)

            for key in score_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=score_stats[key][0], value="\n".join(i for i in stat_data), inline=score_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="needs":
            for key in need_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=need_stats[key][0], value="\n".join(i for i in stat_data), inline=need_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="equiptment":
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        else:
            stat_data = hunt_array[user_hunt][0][user_stat]

            embed.add_field(name=stat_description[user_stat], value="\n".join(i for i in stat_data), inline=True)
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        await ctx.message.delete()

    @command(name="axisdeer")
    async def get_axisdeer(self,ctx,*,stat):
        user_hunt = "axisdeer"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Axis Deer", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
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
            
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)
            embed.clear_fields()

        elif user_stat=="general":
            for key in general_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=general_stats[key][0], value="\n".join(i for i in stat_data), inline=general_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="score":
            embed = Embed(title="Mallard", color=0xFF0000)
            embed.set_author(name="DoubleLung Bot")
            embed.set_thumbnail(url=self.bot.guild.icon_url)

            for key in score_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=score_stats[key][0], value="\n".join(i for i in stat_data), inline=score_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="needs":
            for key in need_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=need_stats[key][0], value="\n".join(i for i in stat_data), inline=need_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="equiptment":
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        else:
            stat_data = hunt_array[user_hunt][0][user_stat]

            embed.add_field(name=stat_description[user_stat], value="\n".join(i for i in stat_data), inline=True)
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        await ctx.message.delete()

    @command(name="roedeer")
    async def get_roedeer(self,ctx,*,stat):
        user_hunt = "roedeer"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Roe Deer", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
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
            
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)
            embed.clear_fields()

        elif user_stat=="general":
            for key in general_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=general_stats[key][0], value="\n".join(i for i in stat_data), inline=general_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="score":
            embed = Embed(title="Mallard", color=0xFF0000)
            embed.set_author(name="DoubleLung Bot")
            embed.set_thumbnail(url=self.bot.guild.icon_url)

            for key in score_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=score_stats[key][0], value="\n".join(i for i in stat_data), inline=score_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="needs":
            for key in need_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=need_stats[key][0], value="\n".join(i for i in stat_data), inline=need_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="equiptment":
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        else:
            stat_data = hunt_array[user_hunt][0][user_stat]

            embed.add_field(name=stat_description[user_stat], value="\n".join(i for i in stat_data), inline=True)
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        await ctx.message.delete()

    @command(name="eurasianlynx")
    async def get_eurasianlynx(self,ctx,*,stat):
        user_hunt = "eurasianlynx"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Eurasian Lynx", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
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
            
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)
            embed.clear_fields()

        elif user_stat=="general":
            for key in general_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=general_stats[key][0], value="\n".join(i for i in stat_data), inline=general_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="score":
            embed = Embed(title="Mallard", color=0xFF0000)
            embed.set_author(name="DoubleLung Bot")
            embed.set_thumbnail(url=self.bot.guild.icon_url)

            for key in score_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=score_stats[key][0], value="\n".join(i for i in stat_data), inline=score_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="needs":
            for key in need_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=need_stats[key][0], value="\n".join(i for i in stat_data), inline=need_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="equiptment":
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        else:
            stat_data = hunt_array[user_hunt][0][user_stat]

            embed.add_field(name=stat_description[user_stat], value="\n".join(i for i in stat_data), inline=True)
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        await ctx.message.delete()

    @command(name="bighornsheep")
    async def get_bighornsheep(self,ctx,*,stat):
        user_hunt = "bighornsheep"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Bighorn Sheep", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
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
            
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)
            embed.clear_fields()

        elif user_stat=="general":
            for key in general_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=general_stats[key][0], value="\n".join(i for i in stat_data), inline=general_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="score":
            embed = Embed(title="Mallard", color=0xFF0000)
            embed.set_author(name="DoubleLung Bot")
            embed.set_thumbnail(url=self.bot.guild.icon_url)

            for key in score_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=score_stats[key][0], value="\n".join(i for i in stat_data), inline=score_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="needs":
            for key in need_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=need_stats[key][0], value="\n".join(i for i in stat_data), inline=need_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="equiptment":
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        else:
            stat_data = hunt_array[user_hunt][0][user_stat]

            embed.add_field(name=stat_description[user_stat], value="\n".join(i for i in stat_data), inline=True)
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        await ctx.message.delete()

    @command(name="wildboar")
    async def get_wildboar(self,ctx,*,stat):
        user_hunt = "wildboar"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Wild Boar", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
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
            
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)
            embed.clear_fields()

        elif user_stat=="general":
            for key in general_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=general_stats[key][0], value="\n".join(i for i in stat_data), inline=general_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="score":
            embed = Embed(title="Mallard", color=0xFF0000)
            embed.set_author(name="DoubleLung Bot")
            embed.set_thumbnail(url=self.bot.guild.icon_url)

            for key in score_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=score_stats[key][0], value="\n".join(i for i in stat_data), inline=score_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="needs":
            for key in need_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=need_stats[key][0], value="\n".join(i for i in stat_data), inline=need_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="equiptment":
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        else:
            stat_data = hunt_array[user_hunt][0][user_stat]

            embed.add_field(name=stat_description[user_stat], value="\n".join(i for i in stat_data), inline=True)
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        await ctx.message.delete()

    @command(name="sikadeer")
    async def get_sikadeer(self,ctx,*,stat):
        user_hunt = "sikadeer"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Sika Deer", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
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
            
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)
            embed.clear_fields()

        elif user_stat=="general":
            for key in general_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=general_stats[key][0], value="\n".join(i for i in stat_data), inline=general_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="score":
            embed = Embed(title="Mallard", color=0xFF0000)
            embed.set_author(name="DoubleLung Bot")
            embed.set_thumbnail(url=self.bot.guild.icon_url)

            for key in score_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=score_stats[key][0], value="\n".join(i for i in stat_data), inline=score_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="needs":
            for key in need_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=need_stats[key][0], value="\n".join(i for i in stat_data), inline=need_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="equiptment":
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        else:
            stat_data = hunt_array[user_hunt][0][user_stat]

            embed.add_field(name=stat_description[user_stat], value="\n".join(i for i in stat_data), inline=True)
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        await ctx.message.delete()

    @command(name="pronghorn")
    async def get_pronghorn(self,ctx,*,stat):
        user_hunt = "pronghorn"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Pronghorn", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
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
            
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)
            embed.clear_fields()

        elif user_stat=="general":
            for key in general_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=general_stats[key][0], value="\n".join(i for i in stat_data), inline=general_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="score":
            embed = Embed(title="Mallard", color=0xFF0000)
            embed.set_author(name="DoubleLung Bot")
            embed.set_thumbnail(url=self.bot.guild.icon_url)

            for key in score_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=score_stats[key][0], value="\n".join(i for i in stat_data), inline=score_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="needs":
            for key in need_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=need_stats[key][0], value="\n".join(i for i in stat_data), inline=need_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="equiptment":
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        else:
            stat_data = hunt_array[user_hunt][0][user_stat]

            embed.add_field(name=stat_description[user_stat], value="\n".join(i for i in stat_data), inline=True)
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        await ctx.message.delete()

    @command(name="lesserkudu")
    async def get_lesserkudu(self,ctx,*,stat):
        user_hunt = "lesserkudu"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Lesser Kudu", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
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
            
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)
            embed.clear_fields()

        elif user_stat=="general":
            for key in general_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=general_stats[key][0], value="\n".join(i for i in stat_data), inline=general_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="score":
            embed = Embed(title="Mallard", color=0xFF0000)
            embed.set_author(name="DoubleLung Bot")
            embed.set_thumbnail(url=self.bot.guild.icon_url)

            for key in score_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=score_stats[key][0], value="\n".join(i for i in stat_data), inline=score_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="needs":
            for key in need_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=need_stats[key][0], value="\n".join(i for i in stat_data), inline=need_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="equiptment":
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        else:
            stat_data = hunt_array[user_hunt][0][user_stat]

            embed.add_field(name=stat_description[user_stat], value="\n".join(i for i in stat_data), inline=True)
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        await ctx.message.delete()

    @command(name="warthog")
    async def get_warthog(self,ctx,*,stat):
        user_hunt = "warthog"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Warthog", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
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
            
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)
            embed.clear_fields()

        elif user_stat=="general":
            for key in general_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=general_stats[key][0], value="\n".join(i for i in stat_data), inline=general_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="score":
            embed = Embed(title="Mallard", color=0xFF0000)
            embed.set_author(name="DoubleLung Bot")
            embed.set_thumbnail(url=self.bot.guild.icon_url)

            for key in score_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=score_stats[key][0], value="\n".join(i for i in stat_data), inline=score_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="needs":
            for key in need_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=need_stats[key][0], value="\n".join(i for i in stat_data), inline=need_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="equiptment":
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        else:
            stat_data = hunt_array[user_hunt][0][user_stat]

            embed.add_field(name=stat_description[user_stat], value="\n".join(i for i in stat_data), inline=True)
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        await ctx.message.delete()

    @command(name="iberianmouflon")
    async def get_iberianmouflon(self,ctx,*,stat):
        user_hunt = "iberianmouflon"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Iberian Mouflon", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
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
            
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)
            embed.clear_fields()

        elif user_stat=="general":
            for key in general_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=general_stats[key][0], value="\n".join(i for i in stat_data), inline=general_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="score":
            embed = Embed(title="Mallard", color=0xFF0000)
            embed.set_author(name="DoubleLung Bot")
            embed.set_thumbnail(url=self.bot.guild.icon_url)

            for key in score_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=score_stats[key][0], value="\n".join(i for i in stat_data), inline=score_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="needs":
            for key in need_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=need_stats[key][0], value="\n".join(i for i in stat_data), inline=need_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="equiptment":
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        else:
            stat_data = hunt_array[user_hunt][0][user_stat]

            embed.add_field(name=stat_description[user_stat], value="\n".join(i for i in stat_data), inline=True)
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        await ctx.message.delete()

    @command(name="beceiteibex")
    async def get_beceiteibex(self,ctx,*,stat):
        user_hunt = "beceiteibex"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Beceite Ibex", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
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
            
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)
            embed.clear_fields()

        elif user_stat=="general":
            for key in general_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=general_stats[key][0], value="\n".join(i for i in stat_data), inline=general_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="score":
            embed = Embed(title="Mallard", color=0xFF0000)
            embed.set_author(name="DoubleLung Bot")
            embed.set_thumbnail(url=self.bot.guild.icon_url)

            for key in score_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=score_stats[key][0], value="\n".join(i for i in stat_data), inline=score_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="needs":
            for key in need_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=need_stats[key][0], value="\n".join(i for i in stat_data), inline=need_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="equiptment":
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        else:
            stat_data = hunt_array[user_hunt][0][user_stat]

            embed.add_field(name=stat_description[user_stat], value="\n".join(i for i in stat_data), inline=True)
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        await ctx.message.delete()

    @command(name="gredosibex")
    async def get_gredosibex(self,ctx,*,stat):
        user_hunt = "gredosibex"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Gredos Ibex", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
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
            
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)
            embed.clear_fields()

        elif user_stat=="general":
            for key in general_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=general_stats[key][0], value="\n".join(i for i in stat_data), inline=general_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="score":
            embed = Embed(title="Mallard", color=0xFF0000)
            embed.set_author(name="DoubleLung Bot")
            embed.set_thumbnail(url=self.bot.guild.icon_url)

            for key in score_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=score_stats[key][0], value="\n".join(i for i in stat_data), inline=score_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="needs":
            for key in need_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=need_stats[key][0], value="\n".join(i for i in stat_data), inline=need_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="equiptment":
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        else:
            stat_data = hunt_array[user_hunt][0][user_stat]

            embed.add_field(name=stat_description[user_stat], value="\n".join(i for i in stat_data), inline=True)
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        await ctx.message.delete()

    @command(name="southeasternspanishibex", aliases=["spanishibex"])
    async def get_southeasternspanishibex(self,ctx,*,stat):
        user_hunt = "southeasternspanishibex"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Southeastern Spanish Ibex", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
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
            
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)
            embed.clear_fields()

        elif user_stat=="general":
            for key in general_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=general_stats[key][0], value="\n".join(i for i in stat_data), inline=general_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="score":
            embed = Embed(title="Mallard", color=0xFF0000)
            embed.set_author(name="DoubleLung Bot")
            embed.set_thumbnail(url=self.bot.guild.icon_url)

            for key in score_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=score_stats[key][0], value="\n".join(i for i in stat_data), inline=score_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="needs":
            for key in need_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=need_stats[key][0], value="\n".join(i for i in stat_data), inline=need_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="equiptment":
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        else:
            stat_data = hunt_array[user_hunt][0][user_stat]

            embed.add_field(name=stat_description[user_stat], value="\n".join(i for i in stat_data), inline=True)
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        await ctx.message.delete()

    @command(name="rondaibex")
    async def get_rondaibex(self,ctx,*,stat):
        user_hunt = "rondaibex"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Ronda Ibex", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
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
            
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)
            embed.clear_fields()

        elif user_stat=="general":
            for key in general_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=general_stats[key][0], value="\n".join(i for i in stat_data), inline=general_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="score":
            embed = Embed(title="Mallard", color=0xFF0000)
            embed.set_author(name="DoubleLung Bot")
            embed.set_thumbnail(url=self.bot.guild.icon_url)

            for key in score_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=score_stats[key][0], value="\n".join(i for i in stat_data), inline=score_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="needs":
            for key in need_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=need_stats[key][0], value="\n".join(i for i in stat_data), inline=need_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="equiptment":
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        else:
            stat_data = hunt_array[user_hunt][0][user_stat]

            embed.add_field(name=stat_description[user_stat], value="\n".join(i for i in stat_data), inline=True)
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        await ctx.message.delete()

    @command(name="fallowdeer")
    async def get_fallowdeer(self,ctx,*,stat):
        user_hunt = "fallowdeer"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Fallow Deer", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
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
            
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)
            embed.clear_fields()

        elif user_stat=="general":
            for key in general_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=general_stats[key][0], value="\n".join(i for i in stat_data), inline=general_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="score":
            embed = Embed(title="Mallard", color=0xFF0000)
            embed.set_author(name="DoubleLung Bot")
            embed.set_thumbnail(url=self.bot.guild.icon_url)

            for key in score_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=score_stats[key][0], value="\n".join(i for i in stat_data), inline=score_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="needs":
            for key in need_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=need_stats[key][0], value="\n".join(i for i in stat_data), inline=need_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="equiptment":
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        else:
            stat_data = hunt_array[user_hunt][0][user_stat]

            embed.add_field(name=stat_description[user_stat], value="\n".join(i for i in stat_data), inline=True)
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        await ctx.message.delete()

    @command(name="blacktaildeer")
    async def get_blacktaildeer(self,ctx,*,stat):
        user_hunt = "blacktaildeer"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Blacktail Deer", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
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
            
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)
            embed.clear_fields()

        elif user_stat=="general":
            for key in general_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=general_stats[key][0], value="\n".join(i for i in stat_data), inline=general_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="score":
            embed = Embed(title="Mallard", color=0xFF0000)
            embed.set_author(name="DoubleLung Bot")
            embed.set_thumbnail(url=self.bot.guild.icon_url)

            for key in score_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=score_stats[key][0], value="\n".join(i for i in stat_data), inline=score_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="needs":
            for key in need_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=need_stats[key][0], value="\n".join(i for i in stat_data), inline=need_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="equiptment":
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        else:
            stat_data = hunt_array[user_hunt][0][user_stat]

            embed.add_field(name=stat_description[user_stat], value="\n".join(i for i in stat_data), inline=True)
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        await ctx.message.delete()

    @command(name="whitetaildeer")
    async def get_whitetaildeer(self,ctx,*,stat):
        user_hunt = "whitetaildeer"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Whitetail Deer", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
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
            
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)
            embed.clear_fields()

        elif user_stat=="general":
            for key in general_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=general_stats[key][0], value="\n".join(i for i in stat_data), inline=general_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="score":
            embed = Embed(title="Mallard", color=0xFF0000)
            embed.set_author(name="DoubleLung Bot")
            embed.set_thumbnail(url=self.bot.guild.icon_url)

            for key in score_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=score_stats[key][0], value="\n".join(i for i in stat_data), inline=score_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="needs":
            for key in need_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=need_stats[key][0], value="\n".join(i for i in stat_data), inline=need_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="equiptment":
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        else:
            stat_data = hunt_array[user_hunt][0][user_stat]

            embed.add_field(name=stat_description[user_stat], value="\n".join(i for i in stat_data), inline=True)
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        await ctx.message.delete()

    @command(name="feralpig")
    async def get_feralpig(self,ctx,*,stat):
        user_hunt = "feralpig"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Feral Pig", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
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
            
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)
            embed.clear_fields()

        elif user_stat=="general":
            for key in general_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=general_stats[key][0], value="\n".join(i for i in stat_data), inline=general_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="score":
            embed = Embed(title="Mallard", color=0xFF0000)
            embed.set_author(name="DoubleLung Bot")
            embed.set_thumbnail(url=self.bot.guild.icon_url)

            for key in score_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=score_stats[key][0], value="\n".join(i for i in stat_data), inline=score_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="needs":
            for key in need_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=need_stats[key][0], value="\n".join(i for i in stat_data), inline=need_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="equiptment":
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        else:
            stat_data = hunt_array[user_hunt][0][user_stat]

            embed.add_field(name=stat_description[user_stat], value="\n".join(i for i in stat_data), inline=True)
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        await ctx.message.delete()

    @command(name="mountaingoat")
    async def get_smountaingoat(self,ctx,*,stat):
        user_hunt = "mountaingoat"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Mountain Goat", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
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
            
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)
            embed.clear_fields()

        elif user_stat=="general":
            for key in general_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=general_stats[key][0], value="\n".join(i for i in stat_data), inline=general_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="score":
            embed = Embed(title="Mallard", color=0xFF0000)
            embed.set_author(name="DoubleLung Bot")
            embed.set_thumbnail(url=self.bot.guild.icon_url)

            for key in score_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=score_stats[key][0], value="\n".join(i for i in stat_data), inline=score_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="needs":
            for key in need_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=need_stats[key][0], value="\n".join(i for i in stat_data), inline=need_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="equiptment":
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        else:
            stat_data = hunt_array[user_hunt][0][user_stat]

            embed.add_field(name=stat_description[user_stat], value="\n".join(i for i in stat_data), inline=True)
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        await ctx.message.delete()

    @command(name="puma")
    async def get_spuma(self,ctx,*,stat):
        user_hunt = "puma"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Puma", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
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
            
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)
            embed.clear_fields()

        elif user_stat=="general":
            for key in general_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=general_stats[key][0], value="\n".join(i for i in stat_data), inline=general_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="score":
            embed = Embed(title="Mallard", color=0xFF0000)
            embed.set_author(name="DoubleLung Bot")
            embed.set_thumbnail(url=self.bot.guild.icon_url)

            for key in score_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=score_stats[key][0], value="\n".join(i for i in stat_data), inline=score_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="needs":
            for key in need_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=need_stats[key][0], value="\n".join(i for i in stat_data), inline=need_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="equiptment":
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        else:
            stat_data = hunt_array[user_hunt][0][user_stat]

            embed.add_field(name=stat_description[user_stat], value="\n".join(i for i in stat_data), inline=True)
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        await ctx.message.delete()

    @command(name="mountainlion")
    async def get_mountainlion(self,ctx,*,stat):
        user_hunt = "mountainlion"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Mountain Lion", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
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
            
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)
            embed.clear_fields()

        elif user_stat=="general":
            for key in general_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=general_stats[key][0], value="\n".join(i for i in stat_data), inline=general_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="score":
            embed = Embed(title="Mallard", color=0xFF0000)
            embed.set_author(name="DoubleLung Bot")
            embed.set_thumbnail(url=self.bot.guild.icon_url)

            for key in score_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=score_stats[key][0], value="\n".join(i for i in stat_data), inline=score_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="needs":
            for key in need_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=need_stats[key][0], value="\n".join(i for i in stat_data), inline=need_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="equiptment":
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        else:
            stat_data = hunt_array[user_hunt][0][user_stat]

            embed.add_field(name=stat_description[user_stat], value="\n".join(i for i in stat_data), inline=True)
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        await ctx.message.delete()

    @command(name="iberianwolf")
    async def get_iberianwolf(self,ctx,*,stat):
        user_hunt = "iberianwolf"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Iberian Wolf", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
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
            
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)
            embed.clear_fields()

        elif user_stat=="general":
            for key in general_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=general_stats[key][0], value="\n".join(i for i in stat_data), inline=general_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="score":
            embed = Embed(title="Mallard", color=0xFF0000)
            embed.set_author(name="DoubleLung Bot")
            embed.set_thumbnail(url=self.bot.guild.icon_url)

            for key in score_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=score_stats[key][0], value="\n".join(i for i in stat_data), inline=score_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="needs":
            for key in need_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=need_stats[key][0], value="\n".join(i for i in stat_data), inline=need_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="equiptment":
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        else:
            stat_data = hunt_array[user_hunt][0][user_stat]

            embed.add_field(name=stat_description[user_stat], value="\n".join(i for i in stat_data), inline=True)
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        await ctx.message.delete()

    @command(name="graywolf")
    async def get_graywolf(self,ctx,*,stat):
        user_hunt = "graywolf"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Gray Wolf", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
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
            
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)
            embed.clear_fields()

        elif user_stat=="general":
            for key in general_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=general_stats[key][0], value="\n".join(i for i in stat_data), inline=general_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="score":
            embed = Embed(title="Mallard", color=0xFF0000)
            embed.set_author(name="DoubleLung Bot")
            embed.set_thumbnail(url=self.bot.guild.icon_url)

            for key in score_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=score_stats[key][0], value="\n".join(i for i in stat_data), inline=score_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="needs":
            for key in need_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=need_stats[key][0], value="\n".join(i for i in stat_data), inline=need_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="equiptment":
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        else:
            stat_data = hunt_array[user_hunt][0][user_stat]

            embed.add_field(name=stat_description[user_stat], value="\n".join(i for i in stat_data), inline=True)
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        await ctx.message.delete()

    @command(name="bluewildebeest")
    async def get_bluewildebeest(self,ctx,*,stat):
        user_hunt = "bluewildebeest"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Blue Wildebeest", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
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
            
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)
            embed.clear_fields()

        elif user_stat=="general":
            for key in general_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=general_stats[key][0], value="\n".join(i for i in stat_data), inline=general_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="score":
            embed = Embed(title="Mallard", color=0xFF0000)
            embed.set_author(name="DoubleLung Bot")
            embed.set_thumbnail(url=self.bot.guild.icon_url)

            for key in score_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=score_stats[key][0], value="\n".join(i for i in stat_data), inline=score_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="needs":
            for key in need_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=need_stats[key][0], value="\n".join(i for i in stat_data), inline=need_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="equiptment":
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        else:
            stat_data = hunt_array[user_hunt][0][user_stat]

            embed.add_field(name=stat_description[user_stat], value="\n".join(i for i in stat_data), inline=True)
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        await ctx.message.delete()

    @command(name="muledeer")
    async def get_muledeer(self,ctx,*,stat):
        user_hunt = "muledeer"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Mule Deer", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
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
            
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)
            embed.clear_fields()

        elif user_stat=="general":
            for key in general_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=general_stats[key][0], value="\n".join(i for i in stat_data), inline=general_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="score":
            embed = Embed(title="Mallard", color=0xFF0000)
            embed.set_author(name="DoubleLung Bot")
            embed.set_thumbnail(url=self.bot.guild.icon_url)

            for key in score_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=score_stats[key][0], value="\n".join(i for i in stat_data), inline=score_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="needs":
            for key in need_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=need_stats[key][0], value="\n".join(i for i in stat_data), inline=need_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="equiptment":
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        else:
            stat_data = hunt_array[user_hunt][0][user_stat]

            embed.add_field(name=stat_description[user_stat], value="\n".join(i for i in stat_data), inline=True)
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        await ctx.message.delete()

    @command(name="reddeer")
    async def get_reddeer(self,ctx,*,stat):
        user_hunt = "reddeer"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Red Deer", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
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
            
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)
            embed.clear_fields()

        elif user_stat=="general":
            for key in general_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=general_stats[key][0], value="\n".join(i for i in stat_data), inline=general_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="score":
            embed = Embed(title="Mallard", color=0xFF0000)
            embed.set_author(name="DoubleLung Bot")
            embed.set_thumbnail(url=self.bot.guild.icon_url)

            for key in score_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=score_stats[key][0], value="\n".join(i for i in stat_data), inline=score_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="needs":
            for key in need_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=need_stats[key][0], value="\n".join(i for i in stat_data), inline=need_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="equiptment":
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        else:
            stat_data = hunt_array[user_hunt][0][user_stat]

            embed.add_field(name=stat_description[user_stat], value="\n".join(i for i in stat_data), inline=True)
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        await ctx.message.delete()

    @command(name="reindeer")
    async def get_reindeer(self,ctx,*,stat):
        user_hunt = "reindeer"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Reindeer", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
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
            
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)
            embed.clear_fields()

        elif user_stat=="general":
            for key in general_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=general_stats[key][0], value="\n".join(i for i in stat_data), inline=general_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="score":
            embed = Embed(title="Mallard", color=0xFF0000)
            embed.set_author(name="DoubleLung Bot")
            embed.set_thumbnail(url=self.bot.guild.icon_url)

            for key in score_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=score_stats[key][0], value="\n".join(i for i in stat_data), inline=score_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="needs":
            for key in need_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=need_stats[key][0], value="\n".join(i for i in stat_data), inline=need_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="equiptment":
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        else:
            stat_data = hunt_array[user_hunt][0][user_stat]

            embed.add_field(name=stat_description[user_stat], value="\n".join(i for i in stat_data), inline=True)
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        await ctx.message.delete()

    @command(name="caribou")
    async def get_caribou(self,ctx,*,stat):
        user_hunt = "caribouk"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Caribou", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
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
            
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)
            embed.clear_fields()

        elif user_stat=="general":
            for key in general_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=general_stats[key][0], value="\n".join(i for i in stat_data), inline=general_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="score":
            embed = Embed(title="Mallard", color=0xFF0000)
            embed.set_author(name="DoubleLung Bot")
            embed.set_thumbnail(url=self.bot.guild.icon_url)

            for key in score_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=score_stats[key][0], value="\n".join(i for i in stat_data), inline=score_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="needs":
            for key in need_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=need_stats[key][0], value="\n".join(i for i in stat_data), inline=need_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="equiptment":
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        else:
            stat_data = hunt_array[user_hunt][0][user_stat]

            embed.add_field(name=stat_description[user_stat], value="\n".join(i for i in stat_data), inline=True)
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        await ctx.message.delete()

    @command(name="blackbear")
    async def get_blackbear(self,ctx,*,stat):
        user_hunt = "blackbear"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Black Bear", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
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
            
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)
            embed.clear_fields()

        elif user_stat=="general":
            for key in general_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=general_stats[key][0], value="\n".join(i for i in stat_data), inline=general_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="score":
            embed = Embed(title="Mallard", color=0xFF0000)
            embed.set_author(name="DoubleLung Bot")
            embed.set_thumbnail(url=self.bot.guild.icon_url)

            for key in score_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=score_stats[key][0], value="\n".join(i for i in stat_data), inline=score_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="needs":
            for key in need_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=need_stats[key][0], value="\n".join(i for i in stat_data), inline=need_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="equiptment":
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        else:
            stat_data = hunt_array[user_hunt][0][user_stat]

            embed.add_field(name=stat_description[user_stat], value="\n".join(i for i in stat_data), inline=True)
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        await ctx.message.delete()

    @command(name="grizzlybear")
    async def get_grizzlybear(self,ctx,*,stat):
        user_hunt = "grizzlybear"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Grizzly Bear", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
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
            
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)
            embed.clear_fields()

        elif user_stat=="general":
            for key in general_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=general_stats[key][0], value="\n".join(i for i in stat_data), inline=general_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="score":
            embed = Embed(title="Mallard", color=0xFF0000)
            embed.set_author(name="DoubleLung Bot")
            embed.set_thumbnail(url=self.bot.guild.icon_url)

            for key in score_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=score_stats[key][0], value="\n".join(i for i in stat_data), inline=score_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="needs":
            for key in need_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=need_stats[key][0], value="\n".join(i for i in stat_data), inline=need_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="equiptment":
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        else:
            stat_data = hunt_array[user_hunt][0][user_stat]

            embed.add_field(name=stat_description[user_stat], value="\n".join(i for i in stat_data), inline=True)
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        await ctx.message.delete()

    @command(name="eurasianbrownbear", aliases=["brownbear"])
    async def get_eurasianbrownbear(self,ctx,*,stat):
        user_hunt = "eurasianbrownbear"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Eurasian Brown Bear", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
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
            
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)
            embed.clear_fields()

        elif user_stat=="general":
            for key in general_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=general_stats[key][0], value="\n".join(i for i in stat_data), inline=general_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="score":
            embed = Embed(title="Mallard", color=0xFF0000)
            embed.set_author(name="DoubleLung Bot")
            embed.set_thumbnail(url=self.bot.guild.icon_url)

            for key in score_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=score_stats[key][0], value="\n".join(i for i in stat_data), inline=score_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="needs":
            for key in need_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=need_stats[key][0], value="\n".join(i for i in stat_data), inline=need_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="equiptment":
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        else:
            stat_data = hunt_array[user_hunt][0][user_stat]

            embed.add_field(name=stat_description[user_stat], value="\n".join(i for i in stat_data), inline=True)
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        await ctx.message.delete()

    @command(name="gemsbok")
    async def get_gemsbok(self,ctx,*,stat):
        user_hunt = "gemsbok"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Gemsbok", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
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
            
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)
            embed.clear_fields()

        elif user_stat=="general":
            for key in general_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=general_stats[key][0], value="\n".join(i for i in stat_data), inline=general_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="score":
            embed = Embed(title="Mallard", color=0xFF0000)
            embed.set_author(name="DoubleLung Bot")
            embed.set_thumbnail(url=self.bot.guild.icon_url)

            for key in score_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=score_stats[key][0], value="\n".join(i for i in stat_data), inline=score_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="needs":
            for key in need_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=need_stats[key][0], value="\n".join(i for i in stat_data), inline=need_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="equiptment":
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        else:
            stat_data = hunt_array[user_hunt][0][user_stat]

            embed.add_field(name=stat_description[user_stat], value="\n".join(i for i in stat_data), inline=True)
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        await ctx.message.delete()

    @command(name="rockymountainelk")
    async def get_rockymountainelk(self,ctx,*,stat):
        user_hunt = "rockymountainelk"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Rockymountain Elk", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
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
            
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)
            embed.clear_fields()

        elif user_stat=="general":
            for key in general_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=general_stats[key][0], value="\n".join(i for i in stat_data), inline=general_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="score":
            embed = Embed(title="Mallard", color=0xFF0000)
            embed.set_author(name="DoubleLung Bot")
            embed.set_thumbnail(url=self.bot.guild.icon_url)

            for key in score_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=score_stats[key][0], value="\n".join(i for i in stat_data), inline=score_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="needs":
            for key in need_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=need_stats[key][0], value="\n".join(i for i in stat_data), inline=need_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="equiptment":
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        else:
            stat_data = hunt_array[user_hunt][0][user_stat]

            embed.add_field(name=stat_description[user_stat], value="\n".join(i for i in stat_data), inline=True)
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        await ctx.message.delete()

    @command(name="rooseveltelk")
    async def get_rooseveltelk(self,ctx,*,stat):
        user_hunt = "rooseveltelk"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Roosevelt Elk", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
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
            
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)
            embed.clear_fields()

        elif user_stat=="general":
            for key in general_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=general_stats[key][0], value="\n".join(i for i in stat_data), inline=general_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="score":
            embed = Embed(title="Mallard", color=0xFF0000)
            embed.set_author(name="DoubleLung Bot")
            embed.set_thumbnail(url=self.bot.guild.icon_url)

            for key in score_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=score_stats[key][0], value="\n".join(i for i in stat_data), inline=score_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="needs":
            for key in need_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=need_stats[key][0], value="\n".join(i for i in stat_data), inline=need_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="equiptment":
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        else:
            stat_data = hunt_array[user_hunt][0][user_stat]

            embed.add_field(name=stat_description[user_stat], value="\n".join(i for i in stat_data), inline=True)
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        await ctx.message.delete()

    @command(name="moose")
    async def get_moose(self,ctx,*,stat):
        user_hunt = "moose"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Moose", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
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
            
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)
            embed.clear_fields()

        elif user_stat=="general":
            for key in general_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=general_stats[key][0], value="\n".join(i for i in stat_data), inline=general_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="score":
            embed = Embed(title="Mallard", color=0xFF0000)
            embed.set_author(name="DoubleLung Bot")
            embed.set_thumbnail(url=self.bot.guild.icon_url)

            for key in score_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=score_stats[key][0], value="\n".join(i for i in stat_data), inline=score_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="needs":
            for key in need_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=need_stats[key][0], value="\n".join(i for i in stat_data), inline=need_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="equiptment":
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        else:
            stat_data = hunt_array[user_hunt][0][user_stat]

            embed.add_field(name=stat_description[user_stat], value="\n".join(i for i in stat_data), inline=True)
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        await ctx.message.delete()

    @command(name="waterbuffalo")
    async def get_waterbuffalo(self,ctx,*,stat):
        user_hunt = "waterbuffalo"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Water Buffalo", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
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
            
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)
            embed.clear_fields()

        elif user_stat=="general":
            for key in general_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=general_stats[key][0], value="\n".join(i for i in stat_data), inline=general_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="score":
            embed = Embed(title="Mallard", color=0xFF0000)
            embed.set_author(name="DoubleLung Bot")
            embed.set_thumbnail(url=self.bot.guild.icon_url)

            for key in score_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=score_stats[key][0], value="\n".join(i for i in stat_data), inline=score_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="needs":
            for key in need_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=need_stats[key][0], value="\n".join(i for i in stat_data), inline=need_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="equiptment":
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        else:
            stat_data = hunt_array[user_hunt][0][user_stat]

            embed.add_field(name=stat_description[user_stat], value="\n".join(i for i in stat_data), inline=True)
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        await ctx.message.delete()

    @command(name="capebuffalo")
    async def get_capebuffalo(self,ctx,*,stat):
        user_hunt = "capebuffalo"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Cape Buffalo", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
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
            
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)
            embed.clear_fields()

        elif user_stat=="general":
            for key in general_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=general_stats[key][0], value="\n".join(i for i in stat_data), inline=general_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="score":
            embed = Embed(title="Mallard", color=0xFF0000)
            embed.set_author(name="DoubleLung Bot")
            embed.set_thumbnail(url=self.bot.guild.icon_url)

            for key in score_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=score_stats[key][0], value="\n".join(i for i in stat_data), inline=score_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="needs":
            for key in need_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=need_stats[key][0], value="\n".join(i for i in stat_data), inline=need_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="equiptment":
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        else:
            stat_data = hunt_array[user_hunt][0][user_stat]

            embed.add_field(name=stat_description[user_stat], value="\n".join(i for i in stat_data), inline=True)
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        await ctx.message.delete()

    @command(name="lion")
    async def get_lion(self,ctx,*,stat):
        user_hunt = "lion"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Lion", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
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
            
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)
            embed.clear_fields()

        elif user_stat=="general":
            for key in general_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=general_stats[key][0], value="\n".join(i for i in stat_data), inline=general_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="score":
            embed = Embed(title="Mallard", color=0xFF0000)
            embed.set_author(name="DoubleLung Bot")
            embed.set_thumbnail(url=self.bot.guild.icon_url)

            for key in score_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=score_stats[key][0], value="\n".join(i for i in stat_data), inline=score_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="needs":
            for key in need_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=need_stats[key][0], value="\n".join(i for i in stat_data), inline=need_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="equiptment":
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        else:
            stat_data = hunt_array[user_hunt][0][user_stat]

            embed.add_field(name=stat_description[user_stat], value="\n".join(i for i in stat_data), inline=True)
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        await ctx.message.delete()

    @command(name="plainsbison")
    async def get_plainsbison(self,ctx,*,stat):
        user_hunt = "plainsbison"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="Plains Bison", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
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
            
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)
            embed.clear_fields()

        elif user_stat=="general":
            for key in general_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=general_stats[key][0], value="\n".join(i for i in stat_data), inline=general_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="score":
            embed = Embed(title="Mallard", color=0xFF0000)
            embed.set_author(name="DoubleLung Bot")
            embed.set_thumbnail(url=self.bot.guild.icon_url)

            for key in score_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=score_stats[key][0], value="\n".join(i for i in stat_data), inline=score_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="needs":
            for key in need_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=need_stats[key][0], value="\n".join(i for i in stat_data), inline=need_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="equiptment":
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        else:
            stat_data = hunt_array[user_hunt][0][user_stat]

            embed.add_field(name=stat_description[user_stat], value="\n".join(i for i in stat_data), inline=True)
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        await ctx.message.delete()

    @command(name="europeanbison")
    async def get_europeanbison(self,ctx,*,stat):
        user_hunt = "europeanbison"
        user_stat = stat.lower().replace(" ","")

        embed = Embed(title="European Bison", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        
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
            
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)
            embed.clear_fields()

        elif user_stat=="general":
            for key in general_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=general_stats[key][0], value="\n".join(i for i in stat_data), inline=general_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="score":
            embed = Embed(title="Mallard", color=0xFF0000)
            embed.set_author(name="DoubleLung Bot")
            embed.set_thumbnail(url=self.bot.guild.icon_url)

            for key in score_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=score_stats[key][0], value="\n".join(i for i in stat_data), inline=score_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="needs":
            for key in need_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=need_stats[key][0], value="\n".join(i for i in stat_data), inline=need_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        elif user_stat=="equiptment":
            for key in equiptment_stats:
                stat_data = hunt_array[user_hunt][0][key]

                embed.add_field(name=equiptment_stats[key][0], value="\n".join(i for i in stat_data), inline=equiptment_stats[key][1])
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        else:
            stat_data = hunt_array[user_hunt][0][user_stat]

            embed.add_field(name=stat_description[user_stat], value="\n".join(i for i in stat_data), inline=True)
            embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
            
            await self.bot.stdout.send(embed=embed)

        await ctx.message.delete()

    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("hunt")

def setup(bot):
    bot.add_cog(Hunt(bot))