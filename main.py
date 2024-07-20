import discord
from discord.ext import commands
import os
import config

@bot.event()
async def on_ready():
    print("Bot Is Ready")
    await bot.load_extension(cogs.extension)
    print("Mod extension Loaded")


bot.run(config.TOKEN)


