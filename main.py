import discord 
from colorama import Fore, Style, init
import os
import json
init(autoreset=True)

token = open("token.txt", "r").readline().strip()

bot = discord.Client()

@bot.event
async def on_ready():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{Fore.GREEN}{bot.user} - server leave\n")
    
    if os.path.exists("exceptions.txt"):
        with open("exceptions.txt", "r") as f:
            exceptions = [line.strip() for line in f.readlines()]
    else:
        exceptions = []

    ask = input("leave (y/n): ")
    if ask.lower() == "y":
        for guild in bot.guilds:
            if str(guild.id) not in exceptions:
                await guild.leave()
                print(f"{Fore.GREEN}left {guild.name}\n")
            else:
                print(f"{Fore.YELLOW}skipped {guild.name}\n")
    else:
        exit()

bot.run(token)