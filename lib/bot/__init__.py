import os
import json
import logging
import traceback

from glob import glob
from asyncio import sleep

from apscheduler.schedulers.blocking import BlockingScheduler
from pytz import utc

from discord import Intents, Embed, File
from discord.ext.commands import Bot as BotBase
from discord.ext.commands import Context
from discord.ext.commands import CommandNotFound

from .config.guild import GuildConfig

OWNER_IDS = [371811001319948288]
if os.name=="nt":
    COGS = set([path.split("\\")[-1][:-3] for path in glob("./lib/cogs/*.py")]) - set(["__init__","init"])
else:
    COGS = set([path.split("/")[-1][:-3] for path in glob("./lib/cogs/*.py")]) - set(["__init__", "init" ])
with open("./lib/bot/prefix.0", "r", encoding = "utf-8") as pf:
    CHANNEL_PREFIX = tuple(pf.read())      
PREFIX = CHANNEL_PREFIX

logger = logging.getLogger(f"doublelung.{__name__}")

class Ready(object):
    def __init__(self):
        logger.info(f"loading cogs: {COGS}")
        for cog in COGS:
            setattr(self, cog, False)

    def ready_up(self, cog):
        setattr(self, cog, True)
        logger.info(f"{cog} status: ready")

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
            logger.info(f"{cog}: loaded")

        self.guild_configuration = GuildConfig("./data/guilds")
        logger.info("status: bot setup complete")

    def run(self, version):
        self.VERSON = version

        logger.info("status: running setup")
        self.setup()

        with open("./lib/bot/token.0", "r", encoding = "utf-8") as tf:
            self.TOKEN = tf.read()

        logger.info("status: initializing")
        super().run(self.TOKEN, reconnect = True)

    async def process_commands(self,message):
        ctx = await self.get_context(message, cls=Context)

        if ctx.command is not None and ctx.guild is not None:
            if not self.ready:
                await ctx.send("I am not ready to recieve commands.  Please try again in a few moments.")     
            else:
                logger.debug("attempting to find response channel")
                ctx.response_channel = self.__get_response_channel(ctx.message.author,ctx.message.guild,ctx.message.channel)
                if ctx.response_channel is None:
                    logger.debug(f"could not find response channel for message {message.id} from guild {ctx.message.guild.name} ({ctx.message.guild.id})")
                    logger.error(f"refused to process command due to channel policy")
                else:
                    await self.invoke(ctx)
            
    async def on_connect(self):
        logger.info("status: online")
    
    async def on_disconnect(self):
        logger.info("status: offline")

    async def on_error(self,err,*args,**kwargs):
        await args[0].send("There was an error in your command. Please check spelling, punctuation and usage. For assistance use the !commands command.")
        raise Exception("command error")

    async def on_command_error(self, ctx, exc):
        st = traceback.format_exception(type(exc), exc, exc.__traceback__)
        for t in st:
            logger.error(t)

        if isinstance(exc, CommandNotFound):
            pass
        elif hasattr(exc, "original"):
            pass
        else:
            logger.error("c")
            raise exc

    async def on_ready(self):
        if not self.ready:
            while not self.cogs_ready.all_ready():
                await sleep(0.5)

            #await self.stdlog.send("status: online")
            self.ready = True
            logger.info("status: ready")
        else:
            logger.info("status: reconnected")

    async def on_message(self, message):
        # only process the command if we are allowed to process on this channel (or if the user is an administrator, listen anyway)
        user_is_admin = message.author.guild_permissions.administrator
        if not message.author.bot:
            if user_is_admin or self.guild_configuration.can_listen_on_channel(message.guild.id,message.channel.id):
                roles = list(map(lambda role: role.id, message.author.roles))
                logger.debug(f"user {message.author.name} ({message.author.id}) has the following role ids: {roles}")
                if user_is_admin or self.guild_configuration.user_can_send_commands(message.guild.id,message.author.id,roles):
                    await self.process_commands(message)
                else:
                    logger.info(f"Skipped processing message {message.id} because user {message.author.name} ({message.author.id}) cannot issue bot commands")
            else:
                logger.info(f"skipped processing message {message.id} because channel {message.channel.name} ({message.channel.id}) is not configured for listen")
        else:
            logger.debug("skipped processing message")

    def __get_response_channel(self,member,guild,src_channel):
        user_is_admin = member.guild_permissions.administrator
        isstr = ("is not","is")[user_is_admin]
        logger.debug(f"the member {member.name} ({member.id}) {isstr} an administrator")
        if user_is_admin or self.guild_configuration.can_respond_on_channel(guild.id,src_channel.id):
            return src_channel
        
        return None

bot = Bot()
