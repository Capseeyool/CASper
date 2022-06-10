import discord
import os

from dotenv import load_dotenv

PREFIX = '.'

class Bot(discord.Client):
    async def on_ready(self):
        await self.change_presence(status=discord.Status.online)
        print(f'Logged in as {self.user}!')

    async def on_message(self, message):
        msg = message.content.split(' ')

        if msg[0] == f'{PREFIX}ping':
            await message.channel.send('pong')

if __name__ == '__main__':
    client = Bot()
    client.run(TOKEN)