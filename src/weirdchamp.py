# weirdchamp.py - misc. things that friends asked me to implement
#
# Author: Daniel Choo
# Date:   10/18/20
# URL:    https://www.github.com/kyoogoo/komorebi


import sys
import random
import discord
import requests
from discord import File
from discord.utils import get
from discord.ext import commands
from bs4 import BeautifulSoup as Soup


class WeirdChamp(commands.Cog, name="misc"):
    def __init__(self, komorebi):
        """ __init__(self, komorebi):
            The meat of the class.

            Return(s):   None [None]
        """
        self.komorebi = komorebi
        

    @commands.command()
    async def peg(self, ctx, members: commands.Greedy[discord.Member]):
        """ peg(ctx, members):
            ･ﾟ✧ Courtesy of Eggie ✧･ﾟ
            Why am I creating this function...

            Return(s):  print statement (str)
        """
        # Initialize variables
        author = ctx.message.author.mention
        auth_check = ctx.message.author.guild_permissions.administrator
        channel = ctx.message.channel
        tools = self.komorebi.get_cog('tools')

        # Check if the role exists; if not: create it.
        if not get(ctx.guild.roles, name="Pegged"):
            # If the user is an admin, they can create the role.
            if auth_check:
                await ctx.send("Sorry, Pegged is not a role in the server. Would you like to create it? (y/n)")

                # Confirm proper input from user.
                msg = await tools.affirm(channel)

                # If they want to create it, prepare for suffering...
                if msg.content in tools.y_respond:
                    await ctx.send("**Prepare for the Peggening...**")
                    await ctx.guild.create_role(name="Pegged")

                # Else, they have saved themselves.
                else:
                    await ctx.send("*Prevented chaos.. Wise choice.*")
                    return

            # If the user is not an admin, then they should not be able to create role.
            else:
                await ctx.send("Sorry, the `Pegged` role does not exist on the server. \nPlease contact the admin to create the role or to run this command again.")

        # Iterate through all of the arguements
        for member in members:
            # Initialize variables...
            role = discord.utils.get(member.guild.roles, name="Pegged")

            # Check if they have the peg role...
            if role in member.roles:
                await ctx.send("This member has already been pegged")

            # If not, then lets peg em'
            else:
                # Let's scrape our album
                embed = discord.Embed()
                url = "https://ibb.co/album/1JPjtN"
                html = requests.get(url)
                soup = Soup(html.text, "lxml")
                imgs = [img["src"] for img in soup.find_all("img")]
                embed.set_image(url=imgs[random.randint(0, len(imgs)-1)])

                await ctx.send(member.mention + " has been pegged by " + author, embed=embed)
                await member.add_roles(role)


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


def setup(komorebi):
    """ setup():
        Required for Discord Cogs.
        
        Return(s):    None [None]
    """
    # Adding our WeirdChamp cog to komorebi
    komorebi.add_cog(WeirdChamp(komorebi))