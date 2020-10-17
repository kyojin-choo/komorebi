# File:       komorebi.py
# Author:     Daniel Choo
# URL:        https://www.github.com/kyoogoo/komorebi

import json
import discord
from discord.ext import commands
from discord.utils import get, find
from secret import BOT_TOKEN

# Initializing komorebi
komorebi = commands.Bot(command_prefix='>')
muted = {}

@komorebi.event
async def on_message(message):
    """ on_message(): 

        Return(s): 
    """
    # Initialize variables.
    channel = message.channel
    
    if message.content.startswith('donkey'):
        print("Donkey has been activated.")
        await channel.send('Send me that 👍 reaction, mate')
        
    elif message.content.startswith('josh'):
        await channel.send('OmegaLUL josh')

    # If I don't do this, then no other commands can be processed...
    await komorebi.process_commands(message)


@komorebi.command()
async def peg(ctx, members: commands.Greedy[discord.Member]):
    """ peg(ctx, members):
        Why am I creating this function...

        Return(s):  print statement (str)
    """
    # Initialize variables
    author = ctx.message.author.mention
    # Check if the role exists; if not: create it. (needs improvement)
#    if "Pegged" not in server_role:
 #       await ctx.send("The role 'Pegged' does not exist in this server.")

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
            await ctx.send(member.mention + " has been pegged by " + author, file=discord.File("peg.gif"))
            #await ctx.send(file=discord.File("peg.gif"))
            

@komorebi.command()
async def unpeg(ctx, members: commands.Greedy[discord.Member]):
    """ peg(ctx, members)
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
            
    
@komorebi.command()
async def clear(ctx, amount=100):
    print(">clear has been invoked.")
    channel = ctx.message.channel
    if ctx.message.author.guild_permissions.administrator:
        await channel.purge(limit=amount,check=None,bulk=True)
    else:
        await ctx.send("You can't use that command, you are not an administrator!")

@komorebi.command()
@commands.is_owner()
async def mute(ctx):
    """ mute(ctx):
        Disallow the bot from talking in this channel.

        Return(s):  None [None]
    """
    # Initialize variables
    curr = ctx.message.channel.id
    
    # Don't talk in this channel anymore :(
    muted[curr] = None
    
    # 

    # :(
    await ctx.send("I wont talk in this channel anymore :(")


@komorebi.command()
async def ping(ctx):
    """ ping(ctx):
        Returns the latency of the bot.

        Return(s):  Print (str)
    """
    latency = komorebi.latency
    await ctx.send("The latency of the bot is " + str(latency) + "ms.")
    

@komorebi.event
async def on_ready():
    """ on_ready():
        bootstrapping the bot

        Return(s): donkey
    """
    # Printing credidentials
    print("Logged in as")
    print(komorebi.user.name)
    print(komorebi.user.id)
    print("-------------")

    # Read in JSON file tracking disabled channels


    # Set komorebi's status
    await komorebi.change_presence(activity=discord.Game(name="Daniel is a headass"), status=discord.Status.idle)

# Initialize the bot
komorebi.run(BOT_TOKEN)
