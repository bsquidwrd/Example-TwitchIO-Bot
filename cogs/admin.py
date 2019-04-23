from twitchio.ext import commands
import traceback


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
    async def unload(self, ctx, *, module):
        try:
            self.bot.unload_module(module)
        except Exception as e:
            await ctx.send(f'Cound not unload \'{module}\'. Check console for details')
            print(traceback.format_exc())
        else:
            await ctx.send(f'\'{module}\' unloaded')


    @commands.command(name='load')
    async def load(self, ctx, *, module):
        try:
            self.bot.load_module(module)
        except Exception as e:
            await ctx.send(f'Cound not load \'{module}\'. Check console for details')
            print(traceback.format_exc())
        else:
            await ctx.send(f'\'{module}\' loaded')


    @commands.command(name='reload')
    async def _reload(self, ctx, *, module):
        try:
            self.bot.unload_module(module)
            self.bot.load_module(module)
        except Exception as e:
            await ctx.send(f'Cound not reload \'{module}\'. Check console for details')
            print(traceback.format_exc())
        else:
            await ctx.send(f'\'{module}\' reloaded')


def prepare(bot):
    bot.add_cog(Admin(bot))

def breakdown(bot):
    pass
