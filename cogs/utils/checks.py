import os

def is_owner(ctx):
    return ctx.message.author.id == int(os.environ['OWNER_ID'])

def is_mod(ctx):
    return ctx.message.author.is_mod == 1
