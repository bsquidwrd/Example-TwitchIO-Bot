from twitchio.ext import commands


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
    async def getid_command(self, ctx):
        if ctx.channel.name == self.bot.nick:
            await ctx.send(f'{ctx.author.name}, your ID is {ctx.author.id}!')


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
