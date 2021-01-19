import json
from datetime import datetime

from discord import Member
from discord.ext.commands import Cog
from discord.ext.commands import command
from discord import Intents, Embed, File

ammo_array = json.load(open("./lib/db/ammo.json"))

dt = datetime.now()
dt_formatted = dt.strftime("%b %d %Y %H:%M:%S")

ammo_label =        {"caliber"      :   ["Caliber",False]}
ammo_stats =        {"variant"      :   ["Variant",False],
                    "type"          :   ["Ammo Type",True],
                    "class"         :   ["Class Integrity",True]}
expansion_stats =   {"erange"       :   ["Range",True],
                    "epenetration"  :   ["Penetration",True],
                    "eexpansion"    :   ["Expansion",True],
                    "ecost"         :   ["Cost",False]}
penetration_stats = {"prange"       :   ["Range",True],
                    "ppenetration"  :   ["Penetration",True],              
                    "pexpansion"    :   ["Expansion",True],              
                    "pcost"         :   ["Cost",False]}
compatible_stats =  {"weapon"       :   ["Compatible Weapon(s)",False],
                    "hunt"          :   ["Available Hunts",False]}

class Ammo(Cog):
    def __init__(self,bot):
        self.bot = bot

    @command(name="ammo")
    async def show_ammo(self,ctx,*,ammo):
        user_ammo = "ammo"
        user_stat = ammo.lower().replace(" ","")

        if user_stat=="rifleammo" or user_stat=="rifles" or user_stat=="rifle":
            embed = Embed(title="All Rifle Ammo", color=0xFF0000)

            rifle_ammo_command=[]
            rifle_ammo_list=[]
            rifle_list=[]

            for ammo_dict in ammo_array:
                ammo = ammo_array[ammo_dict][0]['type'][0]

                if ammo=="Rifle":
                    command_name = ammo_dict
                    ammo_name = ammo_array[ammo_dict][0]['caliber'][0]
                    rifle_name = ammo_array[ammo_dict][0]['weapon']

                    rifle_ammo_command.append(command_name)
                    rifle_ammo_list.append(ammo_name)
                    rifle_list.append(", ".join(i for i in rifle_name))

            embed.add_field(name="Command",value="\n".join(i for i in rifle_ammo_command),inline=True)
            embed.add_field(name="Ammo Caliber",value="\n".join(i for i in rifle_ammo_list),inline=True)
            embed.add_field(name="Usable Weapons",value="\n".join(i for i in rifle_list),inline=True)
        elif user_stat=="handgunammo" or user_stat=="handguns" or user_stat=="handgun":
            embed = Embed(title="All Handgun Ammo", color=0xFF0000)

            handgun_ammo_command=[]
            handgun_ammo_list=[]
            handgun_list=[]

            for ammo_dict in ammo_array:
                ammo = ammo_array[ammo_dict][0]['type'][0]

                if ammo=="Pistol":
                    command_name = ammo_dict
                    ammo_name = ammo_array[ammo_dict][0]['caliber'][0]
                    handgun_name = ammo_array[ammo_dict][0]['weapon']

                    handgun_ammo_command.append(command_name)
                    handgun_ammo_list.append(ammo_name)
                    handgun_list.append(", ".join(i for i in handgun_name))

            embed.add_field(name="Command",value="\n".join(i for i in handgun_ammo_command),inline=True)
            embed.add_field(name="Ammo Caliber",value="\n".join(i for i in handgun_ammo_list),inline=True)
            embed.add_field(name="Usable Weapons",value="\n".join(i for i in handgun_list),inline=True)
        elif user_stat=="shotgunammo" or user_stat=="shotguns" or user_stat=="shotgun":
            embed = Embed(title="All Shotgun Ammo", color=0xFF0000)

            shotgun_ammo_command=[]
            shotgun_ammo_list=[]
            shotgun_list=[]

            for ammo_dict in ammo_array:
                ammo = ammo_array[ammo_dict][0]['type'][0]

                if ammo=="Shotgun":
                    command_name = ammo_dict
                    ammo_name = ammo_array[ammo_dict][0]['caliber'][0]
                    shotgun_name = ammo_array[ammo_dict][0]['weapon']

                    if ammo_dict=="12bird" or ammo_dict=="12buck" or ammo_dict=="12slug":    
                        shotgun_ammo_command.append(f"{command_name}\n")
                        shotgun_ammo_list.append(f"{ammo_name}\n")
                    else:
                        shotgun_ammo_command.append(command_name)
                        shotgun_ammo_list.append(ammo_name)
                    shotgun_list.append(", ".join(i for i in shotgun_name))

            embed.add_field(name="Command",value="\n".join(i for i in shotgun_ammo_command),inline=True)
            embed.add_field(name="Ammo Caliber",value="\n".join(i for i in shotgun_ammo_list),inline=True)
            embed.add_field(name="Usable Weapons",value="\n".join(i for i in shotgun_list),inline=True)
        elif user_stat=="arrowammo" or user_stat=="arrows" or user_stat=="arrow":
            embed = Embed(title="All Bolts and Arrows", color=0xFF0000)

            arrows_ammo_command=[]
            arrows_ammo_list=[]
            arrows_list=[]

            for ammo_dict in ammo_array:
                ammo = ammo_array[ammo_dict][0]['type'][0]

                if ammo=="Arrow" or ammo=="Bolt":
                    command_name = ammo_dict
                    ammo_name = ammo_array[ammo_dict][0]['caliber'][0]
                    arrows_name = ammo_array[ammo_dict][0]['weapon']

                    arrows_ammo_command.append(f"{command_name}\n\n")
                    arrows_ammo_list.append(f"{ammo_name}\n\n")
                    arrows_list.append(", ".join(i for i in arrows_name))

            embed.add_field(name="Command",value="\n".join(i for i in arrows_ammo_command),inline=True)
            embed.add_field(name="Ammo Caliber",value="\n".join(i for i in arrows_ammo_list),inline=True)
            embed.add_field(name="Usable Weapons",value="\n".join(i for i in arrows_list),inline=True)
        else:
            ammo_type = ammo_array[user_stat][0]["type"][0]
            ammo_name = ammo_array[user_stat][0]["caliber"][0]
            embed = Embed(title=ammo_name,color=0xFF0000)

            if ammo_type == "Rifle" or ammo_type == "Handgun":
                for a in ammo_stats:
                    stat_data = ammo_array[user_stat][0][a]
                    embed.add_field(name=ammo_stats[a][0],value="\n".join(i for i in stat_data),inline=ammo_stats[a][1])

                embed.add_field(name="\u200b",value="Expansion Vairant Stats",inline=False)

                for e in expansion_stats:
                    stat_data = ammo_array[user_stat][0][e]
                    embed.add_field(name=expansion_stats[e][0],value="\n".join(i for i in stat_data),inline=expansion_stats[e][1])

                embed.add_field(name="\u200b",value="Penetration Vairant Stats",inline=False)

                for p in penetration_stats:
                    stat_data = ammo_array[user_stat][0][p]
                    embed.add_field(name=penetration_stats[p][0],value="\n".join(i for i in stat_data),inline=penetration_stats[p][1])

                for c in compatible_stats:
                    stat_data = ammo_array[user_stat][0][c]
                    embed.add_field(name=compatible_stats[c][0],value=", ".join(i for i in stat_data),inline=compatible_stats[c][1])

            if ammo_type == "Shotgun" or ammo_type == "Arrow":
                for a in ammo_stats:
                    stat_data = ammo_array[user_stat][0][a]
                    embed.add_field(name=ammo_stats[a][0],value="\n".join(i for i in stat_data),inline=ammo_stats[a][1])

                embed.add_field(name="\u200b",value="Variant Stats",inline=False)

                for e in expansion_stats:
                    stat_data = ammo_array[user_stat][0][e]
                    embed.add_field(name=expansion_stats[e][0],value="\n".join(i for i in stat_data),inline=expansion_stats[e][1])

                for c in compatible_stats:
                    stat_data = ammo_array[user_stat][0][c]
                    embed.add_field(name=compatible_stats[c][0],value=", ".join(i for i in stat_data),inline=compatible_stats[c][1])

        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=self.bot.guild.icon_url)
        embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")

        await self.bot.stdout.send(embed=embed)  

    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("ammo")

def setup(bot):
    bot.add_cog(Ammo(bot))