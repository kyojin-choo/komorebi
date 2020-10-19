# weirdchamp.py - misc. things that friends asked me to implement
#
# Author: Daniel Choo
# Date:   10/18/20
# URL:    https://www.github.com/kyoogoo/komorebi

import discord
from discord import File
from discord.utils import get
from discord.ext import commands


class WeirdChamp(commands.Cog, name="misc"):
    def __init__(self, komorebi):
        """ __init__(self, komorebi):
            The meat of the class.

            Return(s):   None [None]
        """
        self.komorebi = komorebi
        self.y_respond = {"y": None, "Yes": None, 'yes': None}
        self.n_respond = {"n": None, "No": None, "no": None}


    @commands.command()
    async def peg(self, ctx, members: commands.Greedy[discord.Member]):
        """ peg(ctx, members):
            ･ﾟ✧ Courtesy of Eggie ✧･ﾟ
            Why am I creating this function...

            Return(s):  print statement (str)
        """
        # Initialize variables
        author = ctx.message.author.mention
        channel = ctx.message.channel

        # Check if the role exists; if not: create it.
        if not get(ctx.guild.roles, name="Pegged"):
            await ctx.send("Sorry, Pegged is not a role in the server. Would you like to create it? (y/n)")

            # Check for user input: yes or no.
            def check(msg):
                return (msg.content in self.y_respond or msg.content in self.n_respond) and msg.channel == channel

            # Wait for proper user input...
            msg = await self.komorebi.wait_for('message', check=check)

            # If they want to create it, prepare for suffering...
            if msg.content in self.y_respond:
                await ctx.send("**Prepare for the Peggening...**")
                await ctx.guild.create_role(name="Pegged")

            # Else, they have saved themselves.
            else:
                await ctx.send("*Prevented chaos.. Wise choice.*")
                return

        # Iterate through all of the arguements
        for member in members:
            # Initialize variables...
            role = discord.utils.get(member.guild.roles, name="Pegged")

            # Check if they have the peg role...
            if role in member.roles:
                await ctx.send("This member has already been pegged")

                # If not, then lets peg em'
            else:
                await member.add_roles(role)
                await ctx.send(member.mention + " has been pegged by " + author, file=File("peg.gif"))


    @commands.command()
    async def unpeg(self, ctx, members: commands.Greedy[discord.Member]):
        """ peg(ctx, members)
            ･ﾟ✧ Courtesy of Kyojin ✧･ﾟ
            Please save me from the pegger.

            Return(s):  Removal of the peg role, print (str)
        """
        # Initializing variables
        author = ctx.message.author.mention

        # Lets unpeg everyone ;-;
        for member in members:
            role = discord.utils.get(member.guild.roles, name="Pegged")

            if role in member.roles:
                await member.remove_roles(role)
                await ctx.send(member.mention + " has been unpegged by " + author)

            else:
                await ctx.send(member.mention + " has not been pegged yet.")


# Initialize WeirdChamp!
def setup(bot):
    bot.add_cog(WeirdChamp(bot))
