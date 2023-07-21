from time import sleep
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='>', self_bot=True)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

async def send_message():
    await bot.wait_until_ready()
    channel = bot.get_channel(1)

    while not bot.is_closed():
        await sleep(43200)  # task runs every X seconds
        message = await channel.send("MSG")

bot.loop.create_task(send_message())
bot.run('token')
