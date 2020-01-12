import discord
from discord.ext import commands
from .DBHandler import DBHandler

class RMMExt(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.db = DBHandler("tfa.db")
        self.ecount = 0
      
    def get_user_by_name(self, ctx:commands.Context, name:str):
        print("Trying to find user " + name)
        uid = None
        if "@" in name:
            uid = name.strip("@!<>")
        else:
            mem = self.db.get_member_by_name(name)
            if mem:
                uid = mem[0]
            else:
                mem = ctx.message.guild.get_member_named(name)
                if mem:
                    uid = mem.id
        return uid

    @commands.command(name="addskill")
    async def addskill(self, ctx: commands.Context, skillname: str, username: str):
        """<skillname> should be something like INFMEDIC, VICPILOTFIXEDWING, etc
        <user> can tag the user or just their nickname - autocompletion will be attempted"""
        print("Trying to add skill " + skillname + " to user " + username)
        await ctx.send(("Trying to add skill " + skillname + " to user " + username))
        userid = self.get_user_by_name(ctx, username)
        print(userid)
        if(userid not in (False , None)):
            skill = self.db.get_skill_by_easyname(skillname)
            role = discord.utils.get(ctx.message.guild.roles, name=skill[1])
            if(role != None):
                member = await ctx.message.guild.get_member(int(userid)).add_roles(role, reason = "addskill "+ skill[2] + "by "+str(ctx.message.author))
                self.db.create_member_skill(userid, skill[0])
                await ctx.send("Added skill " + skillname + " to " + username)
            else:
                await ctx.send("**E:** Skill could not be found.")
        elif(userid == False):
            await ctx.send("**E:** Ambiguous name provided, please be more specific.")
        else:
            await ctx.send("**E:** Could not find user.")

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