from discord.ext import commands
import requests
import discord
from datetime import *
class ctftime(commands.Cog):
    def _init_(self,client):
        self.client=client
    @commands.command()
    async def ctfs(self,ctx):
        now = datetime.utcnow()
        unix_now = int(now.replace(tzinfo=timezone.utc).timestamp())
        headers = {
                'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0',
                }
        upcoming = 'https://ctftime.org/api/v1/events/'
        limit = '5' # Max amount I can grab the json data for
        response = requests.get(upcoming, headers=headers, params=limit)
        jdata = response.json()
        info=[]
        print("##################################################")
        for num,i in enumerate(jdata):
            ctf_title=jdata[num]['title']
            (ctf_start,ctf_end)=(jdata[num]['start'].replace('T', ' ').split('+', 1)[0], jdata[num]['finish'].replace('T', ' ').split('+', 1)[0])
            #(unix_start, unix_end) = (int(ctf_start.replace(tzinfo=timezone.utc).timestamp()), int(ctf_end.replace(tzinfo=timezone.utc).timestamp()))
            dur_dict = jdata[num]['duration']
            (ctf_hours, ctf_days) = (str(dur_dict['hours']), str(dur_dict['days']))
            ctf_link = jdata[num]['url']
            ctf ={
                'name': ctf_title,
                'start': ctf_start,
                'end': ctf_end,
                'dur': ctf_days+' days, '+ctf_hours+' hours',
                'url': str(ctf_link),
                }
            info.append(ctf)
        print("############################################")
        
        embed=discord.Embed(title='Ctf-Time!', colour=discord.Colour.blue())#description='This is a description',
        embed.set_thumbnail(url=r"https://d19ta9rijs3cxg.cloudfront.net/wp-content/uploads/2019/05/Nulab-Capture-the-Flag-CTF-Challenge-Blog.png")
        embed.set_image(url=r"https://d19ta9rijs3cxg.cloudfront.net/wp-content/uploads/2019/05/Nulab-Capture-the-Flag-CTF-Challenge-Blog.png")
        for element in info:
            embed.add_field(name=str(element["name"]),value=str(element["dur"]))
            embed.add_field(name=str('start time'),value=element["start"])
            embed.add_field(name=str('end time'),value=element["end"])
            '''await ctx.send(str(element["name"]))
            await ctx.send(str("    start:"+element["start"]))
            await ctx.send(str("    end:"+element["end"]))
            await ctx.send(str("    duration:"+element["end"]))'''
            await ctx.send(embed=embed)
            
            #await ctx.send(str(element))
            print(element)
            await ctx.send("-------------------------------------------")
        
def setup(client):
    client.add_cog(ctftime(client))