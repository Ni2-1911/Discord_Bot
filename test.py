import discord
from discord.ext  import commands

class testt(commands.Cog):
    def _init_(self,client):
        self.client=client
    @commands.command() 
    async def test(self,ctx):
        await ctx.send("Test")
    
def setup(client):
    client.add_cog(testt(client))
