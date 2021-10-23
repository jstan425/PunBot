from disnake.ext import commands

async def check_is_owner(inter):
    return await inter.bot.is_owner(inter.author)

async def check_is_co_owner(inter):
    if await check_is_owner(inter):
        return True
    if inter.author.id in inter.bot.co_owners:
        return True
    return False

async def check_is_guildowner(inter):
    if await check_is_co_owner(inter):
        return True
    if inter.author.id == inter.guild.owner.id:
        return True
    return False

async def check_is_admin(inter):
    if await check_is_guildowner(inter):
        return True
    if inter.author.guild_permissions.manage_guild:
        return True
    return False

async def check_is_mod(inter):
    if await check_is_admin(inter):
        return True
    if inter.author.permissions_in(inter.channel).manage_messages:
        return True
    return False

def is_owner():
    return commands.check(check_is_owner)

def is_co_owner():
    return commands.check(check_is_co_owner)

def is_guildowner():
    return commands.check(check_is_guildowner)

def is_admin():
    return commands.check(check_is_admin)

def is_mod():
    return commands.check(check_is_mod)
