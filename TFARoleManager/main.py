import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix="rm.")

@bot.event
async def on_ready():
    # TODO: query all members & update db
    bot.load_extension("rmm.rmm")
    print("ready")
    pass

@bot.command()
async def reload_ext(ctx):
    await ctx.send("**Reloading extensions...**")
    bot.reload_extension("rmm.rmm")
    await ctx.send("**Finished reloading!**")

bot.run(os.getenv("DISCORD_TOKEN_TFA_SRM"))