from turtle import title
import discord
from discord.ext import commands
import asyncio

from setuptools import Command

client = commands.Bot(command_prefix = "-_-")

# event

@client.event
async def on_ready():
    General_channel = client.get_channel(952253203519504424)
    await General_channel.send("I'm Online ✅")
    print("Milky Way online")

# commands

@client.command(description="Invite")
async def invite(ctx):
    embed=discord.Embed(title="Invite")
    embed.add_field(name="invite", value="https://discord.com/oauth2/authorize?client_id=952252442219790356&scope=bot&permissions=1099511627775")
    await ctx.send(embed=embed)
    print ("invite elküldve!")

@client.command(description="Beszéd a bot nevében.")
async def say(ctx, *, text):
    message = ctx.message
    await message.delete()
    await ctx.send(f"{text}")



@client.command(description="Küldj egy privát üzenetet valakinek")
@commands.has_role("Teszt")
async def st(ctx, sendto: discord.Member, *, text):
    embed=discord.Embed(title="Üzenet")
    embed.add_field(name=f"{ctx.author} ezt küldte neked:", value=text)
    message = ctx.message
    await message.delete()
    await sendto.send(embed=embed)
    await ctx.send(f"Elküldve! neki: ||{sendto.display_name}||")

@st.error()
async def st_error(ctx, error):
    print(error)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Helyes sorrendben / helyes adatokat adj meg!")
    elif isinstance(error, commands.MissingRole):
        await ctx.send("Nincs erre jogosultségod!")

@client.command()
async def alma(ctx):
    embed=discord.Embed(title="Alma")
    embed.add_field(name="Alma", value="nagyon finom", inline=False)
    embed.add_field(name="Körte", value="ez is", inline=False)




#@client.event
# async def on_message(message):
#    if message.content == 'Hello':
#        await message.channel.send('Hello!')

@client.command()
async def timer(ctx, seconds):
    try:
        secondint = int(seconds)
        if secondint > 300:
            await ctx.send("Ne írj számot 300 fölött")
            raise BaseException
        if secondint <= 0:
            await ctx.send("Ne írj be negatív számot")
            raise BaseException
        message = await ctx.send("Timer: {seconds}")
        while True:
            secondint -= 1
            if secondint == 0:
                await message.edit(content="Lejárt!")
                break
            await message.edit(content=f"Timer: {secondint}")
            await asyncio.sleep(1)
        await ctx.send(f"{ctx.author.mention} Lejárt a visszaszámlálód!")
    except ValueError:
        await ctx.send("SZámot írj be!")


client.run('OTUyMjUyNDQyMjE5NzkwMzU2.YizUMg.64nP1OXc4xv1oWTomSrci1Mfwb0')
