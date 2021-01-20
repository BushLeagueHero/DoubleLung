import os
import json
from glob import glob
from asyncio import sleep
import json

from apscheduler.schedulers.blocking import BlockingScheduler
from pytz import utc

from discord import Intents, Embed, File
from discord.ext.commands import Bot as BotBase
from discord.ext.commands import Context
from discord.ext.commands import CommandNotFound

OWNER_IDS = [371811001319948288]
if os.name=="nt":
    COGS = [path.split("\\")[-1][:-3] for path in glob("./lib/cogs/*.py")]
else:
    COGS = [path.split("/")[-1][:-3] for path in glob("./lib/cogs/*.py")]
with open("./lib/bot/prefix.0", "r", encoding = "utf-8") as pf:
    CHANNEL_PREFIX = tuple(pf.read())      
PREFIX = CHANNEL_PREFIX

class Ready(object):
    def __init__(self):
        for cog in COGS:
            setattr(self, cog, False)

    def ready_up(self, cog):
        setattr(self, cog, True)
        print(f"{cog} Status: Ready")

    def all_ready(self):
        return all([getattr(self, cog) for cog in COGS])

class Bot(BotBase):
    def __init__(self):
        self.PREFIX = PREFIX
        self.ready = False
        self.cogs_ready = Ready()
        self.guild = None
        self.scheduler = BlockingScheduler(timezone=utc)

        super().__init__(
            command_prefix = PREFIX, 
            owner_ids = OWNER_IDS,
            intents = Intents.all()
        )

    def setup(self):
        for cog in COGS:
            self.load_extension(f"lib.cogs.{cog}")
            print(f"{cog}: Loaded")

        print("Status: Setup Complete")

    def run(self, version):
        self.VERSON = version

        print("Status: Running Setup")
        self.setup()

        with open("./lib/bot/token.0", "r", encoding = "utf-8") as tf:
            self.TOKEN = tf.read()

        print("Stauts: Initializing")
        super().run(self.TOKEN, reconnect = True)

    async def process_commands(self,message):
        ctx = await self.get_context(message, cls=Context)

        if ctx.command is not None and ctx.guild is not None:
            if not self.ready:
                await ctx.send("I am not ready to recieve commands.  Please try again in a few moments.")     
            else:
                await self.invoke(ctx)
            
    async def on_connect(self):
        print("Status: Online")
    
    async def on_disconnect(self):
        print("Status: Offline")

    async def on_error(self,err,*args,**kwargs):
        await args[0].send("There was an error in your command. Please check spelling, punctuation and usage. For assistance use the !commands command.")

        raise

    async def on_command_error(self, ctx, exc):
        if isinstance(exc, CommandNotFound):
            pass
        elif hasattr(exc, "original"):
            pass
        else:
            raise exc

    async def on_ready(self):
        if not self.ready:
            with open("./lib/bot/guild.0", "r", encoding = "utf-8") as gf:
                self.GUILD = int(gf.read())

            self.guild = self.get_guild(self.GUILD)
            
            with open("./lib/bot/channel.0", "r", encoding = "utf-8") as cf:
                self.CHANNEL = int(cf.read())

            with open("./lib/db/guilds.json", "r", encoding = "utf-8") as guilds:
                self.guild_config = json.load(guilds)
                print(self.guild_config)

            self.stdout = self.get_channel(self.CHANNEL)
            self.stdlog = self.get_channel(self.CHANNEL)
            
            while not self.cogs_ready.all_ready():
                await sleep(0.5)

            await self.stdlog.send("Status: Online")
            self.ready = True
            print("Status: Ready")
        else:
            print("Status: Reconnected")

    async def on_message(self, message):
        if not message.author.bot:
            await self.process_commands(message)

    
    def get_response_channel(self, ctx):
        """
            This function will look in the guild configuration to find an appropriate response channel.
            If no channel can be located, an error is thrown
        """
        print("Looking for response channel")
        print(self.guild_config)
        guild_id = f"{ctx.message.guild.id}"

        if guild_id in self.guild_config:
            print("guild exists in config")
            # check the channel policy to see what happens by default with channel traffic
            print(self.guild_config[guild_id]['channel_policy']['default'])
            if self.guild_config[guild_id]['channel_policy']['default'] == "allow":
                print("Channel policy is allow")
                # if the channel is in the list, it is on a blacklist for either listen or respond. ignore it
                if f"{ctx.message.channel.id}" in self.guild_config[guild_id]['channel_policy']['channels']:
                    return None
                else:
                    return ctx.message.channel
            else:
                return None
        else:
            # create a new guild entry
            print(f"Writing new guild entry for non-existant guild {ctx.message.guild.name} ({ctx.message.guild.id})")
            self.guild_config[guild_id] = self.create_guild_entry(ctx.message.guild.name)
            # write the json config back, then reload the guild config
            with open("./lib/db/guilds.json", "w") as config:
                json.dump(self.guild_config, config)
            
            with open("./lib/db/guilds.json", "r", encoding="utf-8") as config:
                self.guild_config = json.load(config)

            print(f"New guild configuration: {self.guild_config}")
            return self.get_response_channel(ctx)

    def create_guild_entry(self,guild_name):
        return {
            "alias": guild_name,
            "channel_policy": {
                "default": "allow",
                "channels": {}
            }
        }

bot = Bot()