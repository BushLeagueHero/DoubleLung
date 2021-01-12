import json
from datetime import datetime

from discord import Member
from discord.ext.commands import Cog
from discord.ext.commands import command
from discord import Intents, Embed, File

dt = datetime.now()
dt_formatted = dt.strftime("%b %d %Y %H:%M:%S")

general_commands = ("!hunthelp","!callerhelp","!scenthelp","!weaponhelp","!ammohelp")

class General(Cog):
    def __init__(self,bot):
        self.bot = bot

    @command(name="clear")
    async def clear_messages(self, ctx, amount=100):
        await ctx.channel.purge(limit=amount)

    @command(name="commands",aliases=["command"])
    async def show_commands(self,ctx):
        embed = Embed(title="Help Commands", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)

        embed.add_field(name="Available Help Commands", value="\n".join(i for i in general_commands), inline=False)
        embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")

        await self.bot.stdout.send(embed=embed)        

    @command(name="hunthelp",aliases=["huntshelp,helphunt,helphunts"])
    async def show_hunt_commands(self,ctx):
        embed = Embed(title="Available Hunting Stats", description="Hunt commands start with the animal name (lowercase, no spaces), and then a stat value.", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)

        fields =    [("Hunt Commands","mallard, scrubhare, jackrabbit, harlequinduck, turkey, canadagoose, europeanrabbit, europeanhare, cinnamonteal, sidestripedjackal, coyote, siberianmuskdeer, redfox, feralgoat, chamois, blackbuck, springbok, axisdeer, roedeer, eurasianlynx, bighornsheep, wildboar, sikadeer, pronghorn, lesserkudu, warthog, iberianmouflon, beceiteibex, gredosibex, southeasternspanishibex, rondaibex, fallowdeer, blacktaildeer, whitetaildeer, feralpig, mountaingoat, puma, mountainlion, iberianwolf, graywolf, bluewildebeest, muledeer, reddeer, reindeer, caribou, blackbear, grizzlybear, eurasianbrownbear, gemsbok, rockymountainelk, rooseveltelk, moose, waterbuffalo, capebuffalo, lion, plainsbison, europeanbison",False),
                    ("Grouped Stats","All, General, Score, Needs, Equipment",False),
                    ("Individual Stats","Class, Difficulty, Max Weight, Silver, Gold, Diamond, Max Score, Location, Fur, Behavior, Habitat, Senses, Social, Active, Feed, Drink, Rest, Unknown, Rifle Ammo, Pistol Ammo, Shotgun Ammo, Bow Ammo, Rifles, Pistols, Shotguns, Bows, Scents, Callers",False),
                    ("Hunt Command Examples","!coyote all, !whitetaildeer max weight, !pronghorn score",False)]

        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)

        embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
        await self.bot.stdout.send(embed=embed)      

    @command(name="callerhelp",aliases=["callershelp,helpcaller,helpcallers"])
    async def show_callers(self,ctx):
        embed = Embed(title="Available Caller Stats", description="Caller commands start with !caller, and then a caller name.", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)

        fields =    [("Caller Commands","caller",False),
                    ("Caller Names","Roe Deer, Screamer, Jackrabbit, Goose, Duck, Wild Boar, Bleat, Grunt, Antlerm Rattler, Snort Wheeze, Distressed Fawn, Elk, Red Deer, Moose",False),
                    ("Caller Command Examples","!caller screamer, !caller Roe Deer, !caller Snort Wheeze",False)]

        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)

        embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
        await self.bot.stdout.send(embed=embed)       

    @command(name="scenthelp",aliases=["scentshelp,helpscent,helpscents"])
    async def show_scents(self,ctx):
        embed = Embed(title="Available Scent Commands", description="The only scent command is !scent.", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)

        embed.add_field(name="Scent Commands", value="!Scents", inline=False)

        embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
        await self.bot.stdout.send(embed=embed)      
    
    @command(name="weaponhelp",aliases=["weaponshelp,helpweapon,helpweapons"])
    async def show_weapons(self,ctx):
        embed = Embed(title="Available Weapon Stats", description="Weapon commands start with !weapon, and then a weapon or weapon group name.", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)

        fields =    [("Weapon Commands","weapon",False),
                    ("Weapon Group Names","Rifles, Shotguns, Handguns, Bows",False),
                    ("Individual Weapon Names","Docent, Ranger, Stradivarius, Huntsman, Regent, Rangemaster, Whitlock, Coachmate, Virant, King, Solokhin, Canning, Vasquez, Eckers, Martensson, Hudzik, Iwaniec, Sporter, Caversham, Cacciatore, Strecker, Nordin, Grelck, Miller, Grenkin, Focoso, Panther, Rhino, Mangiafico, Andersson, Crosspoint, Razorblack, Bearclaw, Hoyi, Hawk",False),
                    ("Weapon Command Examples","!weapon rifles, !weapon ranger",False)]

        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)

        embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
        await self.bot.stdout.send(embed=embed)       

    @command(name="ammohelp",aliases=["ammoshelp,helpammo,helpammos"])
    async def show_ammos(self,ctx):
        embed = Embed(title="Available Ammo Stats", description="Ammo commands start with !weapon, and then a weapon or weapon group name.", color=0xFF0000)
        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)

        fields =    [("Ammo Commands","caller",False),
                    ("Ammo Group Names","Rifle Ammo, Shotgun Ammo, Handgun Ammo, Arrows",False),
                    ("Individual Ammo Names","22 LR ,223 ,243 ,270 ,6.5 mm ,7 mm ,338 ,470 ,30-30 ,303 ,45-70 ,9.3 ,30-06 ,7.62 ,45 Rifle ,300 ,50 Round ,50 Minie ,357 ,44 ,45 Handgun ,454 ,410 ,10 Bird ,10 Buck ,10 Slug ,12 Bird ,12 Buck ,12 Slug ,16 Bird ,16 Buck ,16 Slug ,20 Bird ,20 Buck ,20 Slug ,300 Grain ,420 Grain ,540 Grain ,600 Grain",False),
                    ("Ammo Command Examples","!ammo rifle ammo, !ammo 223",False)]

        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)

        embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")
        await self.bot.stdout.send(embed=embed)        

    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("general")

def setup(bot):
    bot.add_cog(General(bot))