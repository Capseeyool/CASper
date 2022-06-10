import discord
import os
from dotenv import load_dotenv

class Bot(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user}!')

    async def on_message(self, message):
        msg = message.content.split(' ')

        if msg[0] == f'{PREFIX}ping':
            await message.channel.send('pong')

if __name__ == '__main__':
    a = Bot()
    a.run(os.environ['TOKEN'])