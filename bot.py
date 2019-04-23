import os
import datetime
import logging
import traceback

from twitchio.ext import commands
from twitchio.ext.commands.errors import CommandNotFound

import environment


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(module)s %(name)s.%(funcName)s +%(lineno)s: %(levelname)-8s [%(process)d] %(message)s',
                    )
initial_extensions = (
    'cogs.admin',
    'cogs.basic',
    'cogs.mod',
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
        self.log = logging

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
        if message.author.name.lower() == self.nick.lower():
            user_prefix = '[Bot] '
        return user_prefix


    async def event_ready(self):
        ready_string = f'Ready: {self.nick}'
        # print(ready_string)
        # print('-'*len(ready_string))
        self.log.info(ready_string)


    async def event_command_error(self, ctx, error):
        self.log.error(f'Error running command: {error} for {ctx.message.author.name}')


    async def event_message(self, message):
        user_prefix = self.get_author_prefix(message)
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # print('{2} | #{0.channel} | {1}{0.author.name} | {3}'.format(message, user_prefix, timestamp, message.content))
        self.log.info(f'#{message.channel} - {user_prefix}{message.author.name} - {message.content}')

        if message.author.name.lower() != self.nick.lower():
            await self.handle_commands(message)


if __name__ == '__main__':
    nick = os.environ['BOT_NICK']
    irc_token = os.environ['BOT_TOKEN']
    client_id = os.getenv('BOT_CLIENTID', None)

    initial_channels = [nick, 'bsquidwrd']
    bot = Bot(irc_token=irc_token, client_id=client_id, nick=nick, initial_channels=initial_channels)
    bot.run()
