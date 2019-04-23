import os

def is_owner(ctx):
    return ctx.message.author.id == int(os.environ['OWNER_ID'])
