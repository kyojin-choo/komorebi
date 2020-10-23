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
        curr = ctx.message.channel.id
        tools = self.komorebi.get_cog('tools')
        print(">clear has been invoked.", end=" ")

        # Check if we're muted in this channel.
        if tools.mute_check(curr):
            print("Muted in this channel ({}, {}).\n".format(ctx.message.channel.name, curr))
            return

        # We're muted :(
        else:
            channel = ctx.message.channel
            await ctx.send("Are you sure you want to purge 100 messages? (y/n)")

            # Confirm proper input from user.
            msg = await tools.affirm(channel)

            # If they say "lets do it", lets do it.
            if msg.content in tools.y_respond:
                print("Purging 100 messages...")
                await channel.purge(limit=amount,check=None,bulk=True)

            # On second thought, lets not do it.
            else:
                print("Aborted purge.")
                await ctx.send("Okay, I won't purge these messages.")

        tools.pretty_print()
        
    @commands.command()
    @commands.is_owner()
    async def mute(self, ctx):
        """ mute(ctx):
            Disallow the bot from talking in this channel.

            Return(s):  None [None]
        """
        # Initialize variables
        curr = ctx.message.channel.id
        tools = self.komorebi.get_cog('tools')
        print(">mute has been invoked.", end=" ")
        
        # We can't talk in here already
        if tools.mute_check(curr):
            #tools.DM(ctx.message.author, "This channel has already been muted.")
            print("Muted in this channel ({}, {}).\n".format(ctx.message.channel.name, curr))
            return

        # We can't talk in here anymore :(
        else:
            # Add it to our list.
            tools.muted.append(curr)
            check = tools.write_file(tools.mp, tools.muted)

            # Upon successful write, we won't talk anymore.
            if check == 0:
                print("Now muted in: " + str(curr))
                await ctx.send("I won't talk in here anymore :(")

            # Else, we messed up
            else:
                await ctx.send("We made a fucky wucky.")
        
        tools.pretty_print()

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
        print(tools.muted)
        print(">unmute has been invoked.")
        
        # If we are muted, lets unmute ourselves.
        if tools.mute_check(curr):
            temp = tools.muted.index(curr)
            tools.muted.pop(temp)
            check = tools.write_file(tools.mp, tools.muted)

            # Upon successful write, we won't talk anymore.
            if check == 0:
                await ctx.send("I'm free!")
            else:
                await ctx.send("We made a fucky wucky.")

        # Can't be unmuted if im not muted.
        else:
            await ctx.send("I'm not muted in here!")

        tools.pretty_print()
        
    @commands.command()
    async def ping(self, ctx):
        """ ping(ctx):
            Returns the latency of the bot.

            Return(s):  Print (str)
        """
        curr = ctx.message.channel.id
        tools = self.komorebi.get_cog('tools')
        print(">ping has been invoked.", end=" ")
                
        # If we are muted, lets unmute ourselves.
        if tools.mute_check(curr):
            print("Muted in this channel ({}, {}).\n".format(ctx.message.channel.name, curr))
            return

        else:
            latency = self.komorebi.latency
            tools.pretty_print()
            await ctx.send("The latency of the bot is " + str(latency) + "ms.")

def setup(komorebi):
    """ setup():
        Required for Discord Cogs.
        
        Return(s):    None [None]
    """
    komorebi.add_cog(Utility(komorebi))
