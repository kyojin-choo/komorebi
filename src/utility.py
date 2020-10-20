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
    async def DM(self, ctx, user:discord.User, *, message=None):
        """ DM(ctx, user [discord.User], message [None]):
            Will DM the user a specified message passed in from the parameter.

            Return(s):    None [None]
        """
        message = message or "Donkey"
        await user.send(message)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def clear(self, ctx, amount=100):
        """ clear(self, ctx (discord.Context), amount (int)):
            Will clear 100 messages from the discord channel.

            Return(s):    None [None]
        """        
        # Initialize variables
        tools = self.komorebi.get_cog('tools')
        curr = ctx.message.channel.id        

        # Check if we're muted in this channel.
        if not tools.mute_check(curr):
            channel = ctx.message.channel
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

        # We're muted :(
        else:
            return

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
        tools = self.komorebi.get_cog('tools')        

        # We can't talk in here already
        if tools.mute_check(curr):
            self.DM(ctx.message.author, "This channel has already been muted.")

        # We can't talk in here anymore :(
        else:
            # Add it to our dictionary.
            tools.muted[curr] = None
            check = tools.write_file(tools.p, tools.muted)

            # Upon successful write, we won't talk anymore.
            if check == 1:
                await ctx.send("I won't talk in here anymore :(")
            # Else, we messed up
            else:
                await ctx.send("We made a fucky wucky.")

    @commands.command()
    @commands.is_owner()
    async def unmute(self, ctx):
        """ mute(ctx):
            Disallow the bot from talking in this channel.

            Return(s):  None [None]
        """
        # Initialize variables
        curr = ctx.message.channel.id
        tools = self.komorebi.get_cog('tools')
        print(">unmute has been invoked.")
        
        # If we are muted, lets unmute ourselves.
        if tools.mute_check(curr):
            del tools[curr]
            check = tools.write_file(tools.p, tools.muted)
            
            # Upon successful write, we won't talk anymore.
            if check == 1:
                await ctx.send("I'm free!")
            # Else, we messed up
            else:
                await ctx.send("We made a fucky wucky.")

        # Can't be unmuted if im not muted.
        else:
            await ctx.send("I'm not muted in here!")
        
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
