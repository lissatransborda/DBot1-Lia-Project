import discord
from discord.ext import commands, tasks
import datetime

bot = commands.Bot("!")


@bot.event
async def on_ready():
    channel = bot.get_channel(1023995162973708301)
    await channel.send('Olá, seja bem vindo!')
    await channel.send('Eu sou o DBot1.')
    current_time.start()


@tasks.loop(hours=1)
async def current_time():
    now = datetime.datetime.now()
    now = now.strftime("%d/%m/%Y às %H:%M:%S")
    channel = bot.get_channel(1023995162973708301)
    await channel.send("Data e hora: " + now)

# @bot.command(name="data")
# async def current_time():
#     now = datetime.datetime.now()
#     now = now.strftime("%d/%m/%Y às %H:%M:%S")
#     channel = bot.get_channel(1023995162973708301)
#     await channel.send("Data e hora: " + now)

bot.run('MTAyNDA3NjY5NzI4MjI4MTU0Mg.GITZe8.i_5GAvFe4Uof3Mxr-yw-CHPO4wSeZFDDZHuvwQ')
