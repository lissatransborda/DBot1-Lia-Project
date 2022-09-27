
import discord
import discord.ext
from discord.ext import commands, tasks
import datetime

bot = commands.Bot("!")



@bot.event
async def on_ready():
    channel = bot.get_channel(1023995162973708301)
    print(f"Estou pronto {bot.user}")
    await channel.send('Olá, seja bem vindo!')
    await channel.send('Eu sou o DBot1.')


@bot.command(name="oi")
async def send_hello(ctx):
    name = ctx.author.name
    response = "Olá, " + name + "!"
    await ctx.send(response)  

@bot.command(name="data")
async def send_date(ctx):
    now = datetime.datetime.now()
    now = now.strftime("%d/%m/%Y")
    response = "Hoje é " + now
    await ctx.send(response)

@bot.command(name="hora")
async def send_date(ctx):
    now = datetime.datetime.now()
    now = now.strftime("%H:%M:%S")
    response = "Horário atual: " + now
    await ctx.send(response)




# @bot.command(name="data")
# async def current_time():
#     now = datetime.datetime.now()
#     now = now.strftime("%d/%m/%Y às %H:%M:%S")
#     channel = bot.get_channel(1023995162973708301)
#     await channel.send("Data e hora: " + now)

bot.run('MTAyNDA3NjY5NzI4MjI4MTU0Mg.Gba5Yq.UghIsIEGbUonxxEywbCDnWTGwoX3VrMh69KgJ8')


