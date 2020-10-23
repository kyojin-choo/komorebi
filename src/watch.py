# watch.py -- I'm watchin ya ;)
#
# Author:  Daniel Choo
# Date:    10/23/20
# URL:     https://www.github.com/kyoogoo/komorebi

from discord import Guild
from discord import Streaming
from discord.ext import tasks
from discord.ext import commands
from discord.utils import get

class Watch(commands.Cog, name="watch"):
    def __init__(self, komorebi):
        """ __init__(self, komorebi):
            Initializing class member variables.

            Return(s):  None [None]
        """
        self.komorebi = komorebi
    #    self.is_live.start()

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        # Initialize variables.
        live = "🔴 Now Live"
        
        if before.activity.type != after.activity.type:
            return

        else:
            # Initialize variables.
            role = get(after.guild.roles, name=live)
            member = after.id

            # 
            if not isinstance(before.activity, Streaming):
                await before.remove_role(role)
            
            elif isinstance(after.activity, Streaming):
                await after.add_role(role)
                
            
            


    """
    REALLY INTERESTING; see if we can do anything with this.
    
    @tasks.loop(seconds=60.0)
    async def is_live(self):
        print("Checking if people are live on Twitch, YouTube, etc...")
        pass
        
    @is_live.before_loop
    async def before_live(self):
        before_live(self):
            One time preprocessing to check if the role 'Now Live' exists.
        
            Return(s):  None [None]        
            
        # Initialize variable.
        role = "🔴 Now Live"
        
        # Check if the live now role exists.
        for guild in self.komorebi.guilds:
            print(guild)
            if not get(self.komorebi.guild.roles, name=role):
                guild.role_create("🔴 Now Live")

        await self.komorebi.wait_until_ready()"""


def setup(komorebi):
    komorebi.add_cog(Watch(komorebi))