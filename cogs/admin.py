from twitchio.ext import commands
import traceback
from cogs.utils import checks


class Admin(commands.AutoCog):
    def __init__(self, bot):
        self.bot = bot

    def _admin__unload(self):
        pass

    def _prepare(self, bot):
        pass

    def breakdown(self):
        pass

    @commands.command(name='unload')
    @commands.check(checks.is_owner)
    async def unload(self, ctx, *, module):
        try:
            self.bot.unload_module(module)
        except Exception as e:
            await ctx.send(f'Cound not unload \'{module}\'. Check console for details')
            print(traceback.format_exc())
        else:
            await ctx.send(f'\'{module}\' unloaded')


    @commands.command(name='load')
    @commands.check(checks.is_owner)
    async def load(self, ctx, *, module):
        try:
            self.bot.load_module(module)
        except Exception as e:
            await ctx.send(f'Cound not load \'{module}\'. Check console for details')
            print(traceback.format_exc())
        else:
            await ctx.send(f'\'{module}\' loaded')


    @commands.command(name='reload')
    @commands.check(checks.is_owner)
    async def _reload(self, ctx, *, module):
        try:
            self.bot.unload_module(module)
            self.bot.load_module(module)
        except Exception as e:
            await ctx.send(f'Cound not reload \'{module}\'. Check console for details')
            print(traceback.format_exc())
        else:
            await ctx.send(f'\'{module}\' reloaded')


    @commands.command(name='restart')
    @commands.check(checks.is_owner)
    async def _restart(self, ctx):
        try:
            await ctx.send('Goodbye for now o/')
            # I can't find a better way to make it exit
            # but that's probably because I'm retarded
            # I've checked the WebSocketConnection.teardown()
            # and nothing ;-;
            raise SystemExit(2)
        except Exception as e:
            await ctx.send(f'Whoops, I couldn\'t actually restart. Please check console for details {ctx.author.name}')
            print(traceback.format_exc())


def prepare(bot):
    bot.add_cog(Admin(bot))

def breakdown(bot):
    pass
