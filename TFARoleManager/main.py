import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix="rm.")

@bot.event
async def on_ready():
    # TODO: query all members & update db
    print("on_ready")
    bot.load_extension("rmm.rmm")
    print("loaded extension")
    await bot.change_presence(status=discord.Status.online, activity=discord.Activity(name="Testing", type=discord.ActivityType.watching))
    print("updated status")

@bot.command()
async def reload_ext(ctx):
    await ctx.send("**Reloading extensions...**")
    bot.reload_extension("rmm.rmm")
    await ctx.send("**Finished reloading!**")

@bot.command()
async def estop(ctx):
    await ctx.send("Stopping...")
    exit(0)

bot.run(os.getenv("DISCORD_TOKEN_TFA_SRM"))