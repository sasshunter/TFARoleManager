import discord
from discord.ext import commands
from DBHandler import DBHandler

class RMMExt(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.db = DBHandler("tfa.db")
        

    @commands.command(name="addskill")
    async def addskill(self, ctx, user: str, skillname: str):
        """<user> can tag the user or just their nickname - autocompletion will be attempted
        <skillname> should be something like INFMEDIC, VICPILOTFIXEDWING, etc"""
        print("addskill")
        await ctx.send("WIP")

    @commands.command(name="ping")
    async def ping(self, ctx):
        '''
        Responds pong with latency in milliseconds
        '''

        # Get the latency of the bot
        latency = int(self.bot.latency*1000)  # Included in the Discord.py library
        # Send it to the user
        await ctx.send("_Pong!_ " + str(latency) + "ms")


def setup(bot):
    bot.add_cog(RMMExt(bot))