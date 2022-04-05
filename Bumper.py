import asyncio, discord, random, time, json
from discord.ext import commands

bot = commands.Bot(command_prefix="!", self_bot=True)

@bot.command(pass_context=True)
async def bump(ctx):
    await ctx.message.delete()
    while True:
        await ctx.send('!d bump')
        time.sleep(random.randint(7263, 7500))

bot.run('discordtokenfromyou', bot=False)
