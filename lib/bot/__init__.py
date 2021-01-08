import os
from glob import glob
from asyncio import sleep

from apscheduler.schedulers.asyncio import AsyncIOScheduler

from discord import Intents, Embed, File
from discord.ext.commands import Bot as BotBase
from discord.ext.commands import Context
from discord.ext.commands import CommandNotFound


PREFIX = ("!", ".", "+")
OWNER_IDS = [371811001319948288]
COGS = [path.split("\\")[-1][:-3] for path in glob("./lib/cogs/*.py")]

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
        self.scheduler = AsyncIOScheduler()

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

    async def process_commands(self, message):
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

    async def on_error(self, err, *args, **kwargs):
        if err == "on_command_error":
            await args[0].send("A command error has occurred.")

        channel = self.get_channel(796850946809921569)
        await channel.send("A general error has occurred.")

        raise

    async def on_command_error(self, ctx, exc):
        if isinstance(exc, CommandNotFound):
            pass
        elif hasattr(exc, "original"):
            raise exc.original
        else:
            raise exc
 
    async def on_ready(self):
        if not self.ready:
            self.guild = self.get_guild(654351662370127874)
            self.stdout = self.get_channel(796850946809921569)

            while not self.cogs_ready.all_ready():
                await sleep(0.5)

            await self.stdout.send("Status: Online")
            self.ready = True
            print("Status: Ready")
        else:
            print("Status: Reconnected")

    async def on_message(self, message):
        if not message.author.bot:
            await self.process_commands(message)
    
bot = Bot()
