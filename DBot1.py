
import discord
import discord.ext
from discord.ext import commands, tasks
import datetime
import requests
import numpy as np

'''
Versões instaladas:
discord-ext-bot==1.0.1
discord.py==1.7.3
numpy==1.23.3
requests==2.27.1
Python 3.10.4
'''

bot = commands.Bot("!")

@bot.event
async def on_ready():
    channel = bot.get_channel(1023995162973708301)
    print(f"Estou pronto {bot.user}")
    await channel.send('Olá, eu sou o DBot1.')

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
async def send_time(ctx):
    now = datetime.datetime.now()
    now = now.strftime("%H:%M:%S")
    response = "Horário atual: " + now
    await ctx.send(response)

@bot.command(name="mega")
async def send_game(ctx):
    game = np.random.randint(1,60,6)
    response = f"Os número para jogar na Mega Sena são {game}"
    await ctx.send(response)

@bot.command(name="db1")
async def send_db1(ctx):
    response = "O Grupo DB1 é formado por empresas de tecnologia, com sede em Maringá – PR – com 3 operações no Brasil, uma na Argentina e uma nos Estados Unidos. Tem 20 anos de experiência no mercado de tecnologia da informação e oferece software e serviços de desenvolvimento para empresas (B2B). A DB1 Global Software representa 50% do grupo, o prestigiando com clientes nacionais e internacionais. O Grupo DB1 nasceu DB1 Global Software, sendo essa a primeira marca e o core do negócio. Ainda hoje, esse legado de ter tecnologia no DNA se reflete em cada nova empresa do grupo. Sempre com posicionamento de produtos e serviços “premium” e de alta qualidade as empresas do grupo são líderes de mercado como ANYMARKET, Consignet, DB1 Global Software, Koncili, EIVE, Predize e o robô Tinbot." 
    await ctx.send(response)

@bot.command("cotacao")
async def binance(ctx):
    response = requests.get(
        f"https://api.binance.com/api/v3/ticker/price?symbol=USDTBRL"
    )
    data = response.json()
    pricestr = data.get("price")
    price = float(pricestr)
    await ctx.send(f"No momento US$ 1.00 vale R$ {price:.2f}")


def get_nested(data, *args):
    if args and data:
        element  = args[0]
        if element:
            value = data.get(element)
            return value if len(args) == 1 else get_nested(value, *args[1:])


@bot.command("advice")
async def advice(ctx):
    response = requests.get(f"https://api.adviceslip.com/advice")
    data = response.json()
    advice = get_nested(data, "slip", "advice")
    await ctx.send(f"{advice}")


# @tasks.loop(seconds=3)
# async def advice(ctx):
#     response = requests.get(
#         f"https://api.adviceslip.com/advice"
#     )
#     data = response.json()
#     advice = data.get("advice")
#     await ctx.send(f"Sorte de hoje: {advice}")




bot.run('MTAyNDA3NjY5NzI4MjI4MTU0Mg.G3XgRN.ZIwBR8dpX7v4A11eRuJws-qinpIo0hB07HsnsI')


