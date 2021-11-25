import discord
from discord.ext  import commands

class Example(commands.Cog):
    def _init_(self,client):
        self.client=client


    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot is onine")

    @commands.command()
    async def ping(self,ctx):
        await ctx.send("Pong!")
        await ctx.send('Your message is {} characters long.'.format(ctx.message.content))
    
def setup(client):
    client.add_cog(Example(client))
