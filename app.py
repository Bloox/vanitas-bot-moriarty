import random
import time
import discord
from discord import app_commands
from discord.ext import commands
from discord.ext import tasks

import requests as r



token="MTEwMTU5NDI1ODcwOTk0MjQ2NA.GnuN6Q.Sfr9OWaqtQhKBwaugrKqUnzpHaYcKJyTEyiW9A"

class Molnir(commands.Bot):
    async def on_ready(self):
        try:
            synced = await self.tree.sync()
            print(f"Synced {len(synced)} command(s)")
        except Exception as e:
            print(e)

bot= Molnir("$",intents=discord.Intents.all())



forum=1101822617213730837

@bot.tree.command(name="ch",description="generate daily challenges")
async def ch(ctx: discord.Interaction):
    with open("lib.py",'w',encoding="utf-8") as f:
        lib_ = r.get("https://raw.githubusercontent.com/Bloox/vanitas-quests/main/lib.py").text
        f.write(lib_)
    lib=__import__('lib')
    del lib_
    forum_ch:discord.ForumChannel = ctx.guild.get_channel(forum)
    name_=time.strftime("%d.%m.%Y")
    print(name_)
    qe=random.choice(lib.quests_e).generate()
    qh=random.choice(lib.quests_h).generate()
    await forum_ch.create_thread(name=name_,embeds=[qe,qh])
    await ctx.response.defer()
    del lib
@bot.tree.command(name="test_quest",description="test display of an quest with given index")
@app_commands.describe(diffic = "e/h",index="index of an quest")
async def tq(ctx: discord.Interaction,index:int,diffic:str='h'):
    with open("lib.py",'w',encoding="utf-8") as f:
        lib_ = r.get("https://raw.githubusercontent.com/Bloox/vanitas-quests/main/lib.py").text
        #print(lib_)
        f.write(lib_)
    lib=__import__('lib')
    del lib_
    print(lib.version)
    if diffic=='e':
        embed=lib.quests_e[index].generate()
    else:
        embed=lib.quests_h[index].generate()
    await ctx.response.send_message(embed=embed)
    del lib
bot.run(token)