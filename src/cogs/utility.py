import discord
from discord.ext import commands

class Utility(commands.Cog, name="utils"):
    def __init__(self, komorebi):
        self.komorebi = komorebi

    @commands.command()
    async def clear(self, ctx, amount=100):
        print(">clear has been invoked.")
        channel = ctx.message.channel
        if ctx.message.author.guild_permissions.administrator:
            await channel.purge(limit=amount,check=None,bulk=True)
        else:
            await ctx.send("You can't use that command, you are not an administrator!")

    @commands.command()
    @commands.is_owner()
    async def mute(self, ctx):
        """ mute(ctx):
            Disallow the bot from talking in this channel.

            Return(s):  None [None]
        """
        # Initialize variables
        curr = ctx.message.channel.id

        # Don't talk in this channel anymore :(
        #    muted[curr] = None

        # :(
        await ctx.send("I wont talk in this channel anymore :( " + str(curr))


    @commands.command()
    async def ping(self, ctx):
        """ ping(ctx):
            Returns the latency of the bot.

            Return(s):  Print (str)
        """
        latency = self.komorebi.latency
        await ctx.send("The latency of the bot is " + str(latency) + "ms.")


def setup(komorebi):
    komorebi.add_cog(Utility(komorebi))
