# tools.py -- functions needed by all of our modules.
#
# Author:  Daniel Choo
# Date:    10/19/20
# URL:     https://www.github.com/kyoogoo/komorebi

import sys
import json
from pathlib import Path, PurePath
from discord import Message
from discord.ext import commands
from discord.utils import get


class Tools(commands.Cog, name="tools"):
    def __init__(self, komorebi):
        """ __init__(self):

            Return(s):    None [None]
        """
        # Initialize variables in object.
        self.komorebi = komorebi
        self.y_respond = ["y", "yes", "Yes"]
        self.n_respond = ["n", "no", "No"]
        self.mp = PurePath(Path("").absolute(), Path("etc/muted.json"))

        # Check if the file exists. Initialize muted dict
        if Path(self.mp).exists():
            self.muted = self.read_file(self.mp)
        else:
            self.muted = []
            self.write_file(self.mp, self.muted)

        # @startup: Abort if we cannot read in our JSON.
        if self.rw_check(self.muted):
            sys.exit(-1)

    def pretty_print(self):
        """ pretty_print(self):
            Literally just prints a new line... I just didn't want ugly print()'s at
            the end of every function.

            Return(s):  None [None]
        """
        print()

    def rw_check(self, rw):
        """ rw_check(self, rw (dict/int)):
            If rw is evaluated to be

            Return(s):    T/F [bool]
        """
        if isinstance(rw, list):
            return False
        else:
            return True

    def mute_check(self, id):
        """ mute_check(self, id):
            Ternary operator that returns boolean if the id is in our muted list.

            Return(s):    T/F [Bool]
        """
        return True if id in self.muted else False

    async def affirm(self, channel):
        """ affirm(channel [discord.Context.Channel]):
            Literally just confirms if the user typed in yes or no (y/n)

            Return(s):    msg [discord.Message]
        """
        def affirm_check(msg):
            """ affirm_check (msg):
                Checks if the response is formatted properly.

                Return(s):    T/F [Bool]
            """
            return (msg.content in self.y_respond or msg.content in self.n_respond) and msg.channel == channel
        
        msg = await self.komorebi.wait_for('message', check=affirm_check)
        return msg

    def read_file(self, f):
        """ read_file(self, f (dict)):
            Reads from a JSON file!

            Return(s):     Dict [Str] or -1 [int: fail]
        """
        # Attempt to read the file in.
        try:
            with open(f, "r") as file:
                return json.load(file)

        # Else, don't try to do it.
        except Exception as e:
            print(e)
            return -1

    def write_file(self, f, contents):
        """ write_file(self, f (dict)):
            Will write the dictionary as a JSON to the folder!

            Return(s):    0/-1 [int: success/fail]
        """
        # Lets try to write the file to our path.
        try:
            with open(f, "w+") as file:
                file.write(json.dumps(contents, indent=2))

            return 0

        # Else, print out the error message.
        except Exception as e:
            print(e)
            return -1


def setup(komorebi):
    """ setup():
        Required for Discord Cogs.

        Return(s):    None [None]
    """
    # Adding our WeirdChamp cog to komorebi
    komorebi.add_cog(Tools(komorebi))
