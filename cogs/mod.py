from twitchio.ext import commands
from twitchio import dataclasses
from cogs.utils import checks


class Mod(commands.AutoCog):
    """
    Generic Mod commands
    """
    def __init__(self, bot):
        self.bot = bot


    def _prepare(self, bot):
        # I don't know why this is here
        # but it's required to have a cog
        # so keep it as a pass
        pass

    
    @commands.command(name='ban')
    @commands.check(checks.is_mod)
    async def ban_command(self, ctx, user : dataclasses.User, *, reason : str = ''):
        await ctx.channel.ban(user, reason)


    @commands.command(name='unban')
    @commands.check(checks.is_mod)
    async def unban_command(self, ctx, user : dataclasses.User):
        await ctx.channel.unban(user, reason)


    @commands.command(name='clear')
    @commands.check(checks.is_mod)
    async def clear_command(self, ctx):
        await ctx.channel.clear()


    @commands.command(name='slow')
    @commands.check(checks.is_mod)
    async def slow_command(self, ctx):
        await ctx.channel.slow()
        await ctx.send(f'Slow mode activated by {ctx.author.name}')

    
    @commands.command(name='unslow')
    @commands.check(checks.is_mod)
    async def unslow_command(self, ctx):
        await ctx.channel.unslow()


    @commands.command(name='timeout')
    @commands.check(checks.is_mod)
    async def timeout_command(self, ctx, user : dataclasses.User, duration : int = 600, *, reason : str = ''):
        await ctx.channel.timeout(user, duration, reason)


    @commands.command(name='say')
    @commands.check(checks.is_mod)
    async def say_command(self, ctx, *, message : str = None):
        content = message or f'What? You don\'t want me to say anything {ctx.author.name}?'
        await ctx.channel.send_me(content)


def prepare(bot):
    # Module is being loaded
    # Prepare anything you need
    # then add the cog
    bot.add_cog(Mod(bot))


def breakdown(bot):
    # Incase you wanna do something
    # when the Module is getting unloaded?
    pass
