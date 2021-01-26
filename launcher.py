import logging
import logging.config
import os

from lib.bot import bot

data_dirs = [ "./data/logs", "./data/guilds" ]
for directory in data_dirs:
    if not os.path.isdir(directory):
        os.mkdir(directory)

# configure the logger
logging.config.fileConfig("./data/config/logger.conf")

VERSION = "1.0.1"

# write out a logger startup message
messages = [ f"####################################",
             f"# DoubleLung Bot v{VERSION}",
             f"####################################" ]

for msg in messages:
    logging.getLogger(f"doublelung.{__name__}").info(msg)

bot.run(VERSION)