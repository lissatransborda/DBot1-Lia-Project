import discord
import os


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        if message.content == '?regras':
            await message.channel.send(f'{message.author.name} Regras: {os.linesep} NÃO HÁ REGRAS')
        elif message.content == '?privado':
            await message.author.send(f'Mensagem Privada')

    async def on_member_join(self, member):
        guild = member.guild
        if guild.system.channel is not None:
            mensagem = f'Um(a) tal de {member.mention} entrou no {guild.name}!'
            await guild.system_channel.send(mensagem)


intents = discord.Intents.default()
intents.members = True

client = MyClient(intents=intents)
client.run('MTAyNDAwMTg3OTc3ODI2MzE4MQ.Gw04Hw.XIbIx94-ZOxR_Fl9WF07D6FohXl7-hRwCg_2ZQ')