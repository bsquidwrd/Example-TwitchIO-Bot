from twitchio.ext import commands
from twitchio import dataclasses
from cogs.utils import checks


class Basic(commands.AutoCog):
    def __init__(self, bot):
        self.bot = bot

    # def _basic__unload(self):
    #     pass

    def _prepare(self, bot):
        # I don't know why this is here
        # but it's required to have a cog
        # so keep it as a pass
        pass

    @commands.command(name='hello')
    async def hello_command(self, ctx):
        await ctx.send(f'Hello {ctx.author.name}!')

    
    @commands.command(name='getid')
    async def getid_command(self, ctx, *, user : str = None):
        if ctx.channel.name == self.bot.nick or checks.is_owner(ctx):
            if user:
                possible_users = await self.bot.get_users(user)
                if len(possible_users) == 0:
                    await ctx.send(f'{ctx.author.name}, no users found with username \'{user}\'')
                    return
                else:
                    u = possible_users[0]
            else:
                u = ctx.author
            await ctx.send(f'{ctx.author.name}, ID = {u.id}!')


    @commands.command(name='test')
    async def test_command(self, ctx):
        print(ctx.message.author.tags)


def prepare(bot):
    # Module is being loaded
    # Prepare anything you need
    # then add the cog
    bot.add_cog(Basic(bot))


def breakdown(bot):
    # Incase you wanna do something
    # when the Module is getting unloaded?
    pass
