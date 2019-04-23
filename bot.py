import os
import datetime
import traceback

from twitchio.ext import commands
from twitchio.ext.commands.errors import CommandNotFound

import environment


initial_extensions = (
    'cogs.admin',
    'cogs.basic',
)


class Bot(commands.Bot):
    def __init__(self, irc_token, nick, client_id='test', initial_channels=[]):
        params = {
            'irc_token': irc_token,
            'client_id': client_id,
            'nick': nick,
            'prefix': '!',
            'initial_channels': initial_channels,
        }
        super().__init__(**params)

        for extension in initial_extensions:
            try:
                self.load_module(extension)
            except Exception as e:
                print(f'Failed to load extension {extension}.')
                traceback.print_exc()


    def get_author_prefix(self, message):
        user_prefix = ''
        if message.author.is_subscriber:
            user_prefix = '[Subscriber] '
        if message.author.is_mod:
            user_prefix = '[Moderator] '
        # if message.tags['room-id'] == message.author.id:
        #     user_prefix = '[Streamer] '
        return user_prefix


    async def event_ready(self):
        ready_string = f'Ready: {self.nick}'
        print(ready_string)
        print('-'*len(ready_string))


    async def event_command_error(self, ctx, error):
        print("Error running command: {}".format(error))


    async def event_message(self, message):
        user_prefix = self.get_author_prefix(message)
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print('{2} | #{0.channel} | {1}{0.author.name} | {3}'.format(message, user_prefix, timestamp, message.content))
        await self.handle_commands(message)


if __name__ == '__main__':
    initial_channels = ['bsquidwrd']
    bot = Bot(irc_token=os.environ['BOT_TOKEN'], nick=os.environ['BOT_NICK'], initial_channels=initial_channels)
    bot.run()
