import json
import logging

from difflib import get_close_matches as matches
from datetime import datetime
from re import search

from discord import Member
from discord.ext.commands import Cog
from discord.ext.commands import command
from discord import Intents, Embed, File

import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer=LancasterStemmer()
from nltk.tokenize import word_tokenize as wt
nltk.download('punkt')

import numpy
import tflearn
import tensorflow as tf
from tensorflow.python.framework import ops


import random
import pickle

from lib.ai.training.cmd_training import AICommands
from lib.ai.training.species_training import AISpecies
from lib.ai.training.stats_training import AIStats

logger = logging.getLogger(f"doublelung.{__name__}")

class AskBot(Cog):
    def __init__(self,bot):
        self.bot = bot

    def run_model(self,modelClass,question):
        results = modelClass.model.predict([self.conversion_to_command(question, modelClass.words)])
        results_index = numpy.argmax(results)
        tag = modelClass.labels[results_index]

        for t in modelClass.model_data["intents"]:
            if t["tag"] == tag:
                response = t["response"]

        return response

    def conversion_to_command(self,question,words):
        user_bag = [0 for _ in range(len(words))]

        user_words = nltk.word_tokenize(question)
        user_words = [stemmer.stem(w.lower()) for w in user_words]

        for s in user_words:
            for i,w in enumerate(words):
                if w == s:
                    user_bag[i] = 1

        return numpy.array(user_bag)

    @command(name="askbot")
    async def askBot(self,ctx,*,message):
        question = message

        cmd_response = self.run_model(AICommands,question)
        print(cmd_response)

        cmd_question = f"{cmd_response[0]}command {message}"
        print(cmd_question)

        if cmd_response[0] == "species":
            spcs_response = self.run_model(AISpecies,cmd_question)
            print(spcs_response)
        
        stats_response = self.run_model(AIStats,cmd_question)
        print(stats_response)

        if cmd_response[0] == "species":
            await ctx.invoke(self.bot.get_command(cmd_response[0]),species=spcs_response[0],group=stats_response[0])
        elif cmd_response[0] == "scent":
            await ctx.invoke(self.bot.get_command(cmd_response[0]))
        else:
            await ctx.invoke(self.bot.get_command(cmd_response[0]),group=stats_response[0])

    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("askbot")

def setup(bot):
    bot.add_cog(AskBot(bot))