# komorebi.py -- beep boop
#
# Author:       Daniel Choo
# URL:          https://www.github.com/kyoogoo/komorebi
#
# Description:  The heart of our Discord bot.

import discord
from progress.bar import IncrementalBar
from discord.ext import commands
from secret import BOT_TOKEN


# Initializing akomorebi
komorebi = commands.Bot(command_prefix=">", description="Just a lil baby bot.")
extensions = ["weirdchamp", "utility", "watch","tools"]
errors = []

if __name__ == '__main__':
    """ __main__:
        The bootstrapper. Load in all of our extensions.

        Return(s):    None [None]
    """
    # Load in our extensions.
    with IncrementalBar('\nLoading modules', max=len(extensions)) as bar:
        for ext in extensions:
            # Attempt loading in our extension.
            try:
                komorebi.load_extension("src."+ext)
                bar.next()

            # Print the error if unable to.
            except Exception as e:
                errors.append(e)      
                bar.next()

                
    # Print out our errors.
    for e in errors:
        print(e)

@komorebi.event
async def on_ready():
    """ on_ready():
        3.. 2.. 1.. We have lift off.

        Return(s): donkey
    """
    # Printing credidentials
    print("\nLogged in as:")
    print(komorebi.user.name)
    print(komorebi.user.id)
    print("-------------")
    
    # Set komorebi's status
    await komorebi.change_presence(activity=discord.Game(name="PSA: stop the peg"), status=discord.Status.idle)

# Execute the bot
komorebi.run(BOT_TOKEN)
