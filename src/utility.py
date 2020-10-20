# utility.py -- commands to make your life better.
#
# Author:       Daniel Choo
# Date:         10/17/20
# URL:          https://www.github.com/kyoogoo/komorebi
# 
# Description:  PogChamp

import sys
import json
import discord
from discord.ext import commands


class Utility(commands.Cog, name="utils"):
    def __init__(self, komorebi):
        """ __init__(self, komorebi):
            Initializes our bot and its utility commands.

            Return(s):    None [None]
        """
        self.komorebi = komorebi


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def clear(self, ctx, amount=100):
        """ clear(self, ctx (discord.Context), amount (int)):
            Will clear 100 messages from the discord channel.

            Return(s):    None [None]
        """        
        # Initialize variables
        channel = ctx.message.channel
        tools = self.komorebi.get_cog('tools')
        print(">clear has been invoked.")
        await ctx.send("Are you sure you want to purge 100 messages? (y/n)")

        # Confirm proper input from user.
        msg = await tools.affirm(channel)

        # If they say "lets do it", lets do it.
        if msg.content in tools.y_respond:
            await channel.purge(limit=amount,check=None,bulk=True)

        # On second thought, lets not do it.
        else:
            await ctx.send("Okay; I won't purge these messages.")


    @commands.command()
    @commands.is_owner()
    async def mute(self, ctx):
        """ mute(ctx):
            Disallow the bot from talking in this channel.

            Return(s):  None [None]
        """
        # Initialize variables
        curr = ctx.message.channel.id
        print(">mute has been invoked.")
        
        

    @commands.command()
    async def ping(self, ctx):
        """ ping(ctx):
            Returns the latency of the bot.

            Return(s):  Print (str)
        """
        latency = self.komorebi.latency
        await ctx.send("The latency of the bot is " + str(latency) + "ms.")


def setup(komorebi):
    """ setup():
        Required for Discord Cogs.
        
        Return(s):    None [None]
    """
    komorebi.add_cog(Utility(komorebi))
