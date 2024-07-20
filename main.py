import discord
from discord.ext import commands
import os
import config

@bot.event()
async def on_ready():
    print("Bot Is Ready")


bot.run(config.TOKEN)


