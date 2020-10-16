# File:       komorebi.py
# Author:     Daniel Choo
# URL:        https://www.github.com/kyoogoo/komorebi

import discord
from discord.ext.commands import Bot
import random
import asyncio
import time
from secret import BOT_TOKEN
import os, json
import threading

komorebi = discord.Client()

#def set_interval(func, sec):
#	def func_wrapper():
#		set_interval(func, sec) 
#		func()  
#	t = threading.Timer(sec, func_wrapper)
#	t.start()
#	return t


#def start_spam():
#	komorebi.send_message(message.channel, 'New Promo! Get 1000 Diamonds for free!! Go to link: youtube.com/user/kyoogoo')


@komorebi.event
async def on_ready():
	print("Logged in as")
	print(komorebi.user.name)
	print(komorebi.user.id)
	print("-------------")

@komorebi.event
async def on_message(message):

	if message.content.startswith('is the server cool?'):
		await komorebi.send_message(message.channel, 'Of course.')

	if message.content.startswith('!spam'):
#		spam = set_interval(start_spam, 60)
#		print("Starting spam")
		await komorebi.send_message(message.channel, 'New Promo! Get 1000 Diamonds for free!! Go to link: youtube.com/user/kyoogoo')
		
	if message.content.startswith('!stopspam'):
		spam.cancel()
    
	# fsadf
	if message.content.startswith('!flip'):
		flip = random.choice(['(╯°□°）╯︵  Heads', '(╯°□°）╯︵  Tails'])
		await komorebi.send_message(message.channel, flip)

			  
#@komorebi.command(pass_context=True)
#async def purge(context, number : int):
#    deleted = await bot.purge_from(context.message.channel, limit=number)
#    await bot.send_message(context.message.channel, 'Deleted {} message(s)'.format(len(deleted)))
komorebi.run(BOT_TOKEN)
