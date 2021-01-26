import json
from datetime import datetime

from discord import Member
from discord.ext.commands import Cog
from discord.ext.commands import command
from discord import Intents, Embed, File

weapon_array = json.load(open("./lib/db/weapon.json"))

dt = datetime.now()
dt_formatted = dt.strftime("%b %d %Y %H:%M:%S")

weapon_description =    {"weaponname"    :   ["Weapon Name",False]}
weapon_stats =          {"weapontype"    :   ["Weapon Type",False],
                        "accuracy"       :   ["Accuracy",True],
                        "recoil"         :   ["Recoil",True],
                        "reloadspeed"    :   ["Reload Speed",True],
                        "hipshot"        :   ["Hip Shot",True],
                        "magazinesize"   :   ["Magazine Size",True],
                        "useableammo"    :   ["Usable Ammo",True]}
hunts =                 {"hunt"          :   ["Available Hunts",False]}

class Weapon(Cog):
    def __init__(self,bot):
        self.bot = bot

    @command(name="weapon", aliases=["weapons"])
    async def show_caller(self,ctx,*,weapon):
        user_weapon = "weapon"
        user_stat = weapon.lower().replace(" ","")

        if user_stat=="rifles" or user_stat=="rifle":
            embed = Embed(title="All Rifles", color=0xFF0000)

            rifle_command=[]
            rifle_list=[]
            rifle_ammo_list=[]

            for weapon_dict in weapon_array:
                rifles = weapon_array[weapon_dict][0]['weapontype'][0]

                if rifles=="Rifle":
                    command_name = weapon_dict
                    rifle_name = weapon_array[weapon_dict][0]['weaponname'][0]
                    ammo_type = weapon_array[weapon_dict][0]['useableammo']

                    rifle_command.append(command_name)
                    rifle_list.append(rifle_name)
                    rifle_ammo_list.append(", ".join(i for i in ammo_type))

            embed.add_field(name="Command",value="\n".join(i for i in rifle_command),inline=True)
            embed.add_field(name="Rifle Name",value="\n".join(i for i in rifle_list),inline=True)
            embed.add_field(name="Usable Ammo",value="\n".join(i for i in rifle_ammo_list),inline=True)
        elif user_stat=="shotguns" or user_stat=="shotgun":
            embed = Embed(title="All Shotguns", color=0xFF0000)

            shotgun_command=[]
            shotgun_list=[]
            shotgun_ammo_list=[]

            for weapon_dict in weapon_array:
                shotguns = weapon_array[weapon_dict][0]['weapontype'][0]

                if shotguns=="Shotgun":
                    command_name = weapon_dict
                    shotgun_name = weapon_array[weapon_dict][0]['weaponname'][0]
                    ammo_type = weapon_array[weapon_dict][0]['useableammo']

                    shotgun_command.append(command_name)
                    shotgun_list.append(shotgun_name)
                    shotgun_ammo_list.append(", ".join(i for i in ammo_type))

            embed.add_field(name="Command",value="\n".join(i for i in shotgun_command),inline=True)
            embed.add_field(name="Shotgun Name",value="\n".join(i for i in shotgun_list),inline=True)
            embed.add_field(name="Usable Ammo",value="\n".join(i for i in shotgun_ammo_list),inline=True)
        elif user_stat=="handguns" or user_stat=="pistols" or user_stat=="handgun" or user_stat=="pistol":
            embed = Embed(title="All Handguns", color=0xFF0000)

            handgun_command=[]
            handgun_list=[]
            handgun_ammo_list=[]

            for weapon_dict in weapon_array:
                handguns = weapon_array[weapon_dict][0]['weapontype'][0]

                if handguns=="Handgun":
                    command_name = weapon_dict
                    handgun_name = weapon_array[weapon_dict][0]['weaponname'][0]
                    ammo_type = weapon_array[weapon_dict][0]['useableammo']

                    handgun_command.append(command_name)
                    handgun_list.append(handgun_name)
                    handgun_ammo_list.append(", ".join(i for i in ammo_type))

            embed.add_field(name="Command",value="\n".join(i for i in handgun_command),inline=True)
            embed.add_field(name="Handgun Name",value="\n".join(i for i in handgun_list),inline=True)
            embed.add_field(name="Usable Ammo",value="\n".join(i for i in handgun_ammo_list),inline=True)
        elif user_stat=="bows" or user_stat=="crossbows" or user_stat=="bow" or user_stat=="crossbow":
            embed = Embed(title="All Bows(Crossbows)", color=0xFF0000)

            bow_command=[]
            bow_list=[]
            bow_ammo_list=[]

            for weapon_dict in weapon_array:
                bows = weapon_array[weapon_dict][0]['weapontype'][0]

                if bows=="Bow" or bows=="Crossbow":
                    command_name = weapon_dict
                    bow_name = weapon_array[weapon_dict][0]['weaponname'][0]
                    ammo_type = weapon_array[weapon_dict][0]['useableammo']

                    bow_command.append(command_name)
                    bow_list.append(bow_name)
                    bow_ammo_list.append(", ".join(i for i in ammo_type))

            embed.add_field(name="Command",value="\n".join(i for i in bow_command),inline=True)
            embed.add_field(name="Bow Name",value="\n".join(i for i in bow_list),inline=True)
            embed.add_field(name="Usable Ammo",value="\n".join(i for i in bow_ammo_list),inline=True)
        else:
            weapon_name = weapon_array[user_stat][0]['weaponname']
            embed = Embed(title="\n".join(i for i in weapon_name), color=0xFF0000)
            
            for stat in weapon_stats: 
                stat_data = weapon_array[user_stat][0][stat]
                embed.add_field(name=weapon_stats[stat][0], value="\n".join(i for i in stat_data), inline=weapon_stats[stat][1])
            
            for key in hunts: 
                stat_data = weapon_array[user_stat][0][key]
                embed.add_field(name=hunts[key][0], value=", ".join(i for i in stat_data), inline=hunts[key][1])

        embed.set_author(name="DoubleLung Bot")
        embed.set_thumbnail(url=ctx.message.guild.icon_url)
        embed.set_footer(text=f"{ctx.author.display_name}; {dt_formatted}")

        if ctx.response_channel is not None:
            await ctx.response_channel.send(embed=embed)

    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("weapon")

def setup(bot):
    bot.add_cog(Weapon(bot))
            
