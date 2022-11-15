
from nextcord.ext import commands



class Cmds(commands.Cog, name="PrefixCommands"):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="ping")
    async def ping(self, ctx: commands.Context):
        
        await ctx.reply(f"🏓 Pong {round(self.bot.latency * 1000)}ms")

      
        



def setup(bot: commands.Bot):
    bot.add_cog(Cmds(bot))
