from discord.ext import commands
import dat_ctf
import discord
lst=[]



dictionary={}
def store(name,flag):
    dictionary[name]=flag
def clear():
    dictionary.clear()
def show():
    return dictionary
def show(name):
    return dictionary[name]


class flag_holder(commands.Cog):
    def _init_(self,client):
        self.client=client   
    
        
    @commands.command()
    async def flag(self,ctx):
        lst=ctx.message.content.split(" ")
        dictionary[lst[lst.index("-n")+1]]=lst[lst.index("-f")+1]
        await ctx.message.add_reaction("✅")
    @commands.command()
    async def clear_flag(self,ctx):
        dictionary.clear()
        await ctx.message.add_reaction("✅")
        await ctx.send("Ready for next ctf with new flags....")
    @commands.command()
    async def show_flags(self,ctx):
        embed=discord.Embed(title='Flags', colour=discord.Colour.blue())#description='This is a description',
        embed.set_thumbnail(url=r"https://d19ta9rijs3cxg.cloudfront.net/wp-content/uploads/2019/05/Nulab-Capture-the-Flag-CTF-Challenge-Blog.png")
        embed.set_image(url=r"https://d19ta9rijs3cxg.cloudfront.net/wp-content/uploads/2019/05/Nulab-Capture-the-Flag-CTF-Challenge-Blog.png")
        for i in range(0,len(dictionary)):
            embed.add_field(name=str(list(dictionary)[i]),value =dictionary[list(dictionary)[i]],inline=True)
        if(len(ctx.message.content.split(" "))==1):
            await ctx.send(embed=embed)
        else:
            await ctx.send(dictionary[ctx.message.content.split(" ")[1]])


def setup(client):
    client.add_cog(flag_holder(client))                                                                                                                                                                                          