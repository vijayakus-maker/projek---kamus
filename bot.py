import discord
import random
from discord.ext import commands
from passgen import gen_pass
import asyncio
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')
@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def gacha(ctx, count_heh = 5):
    pahlawan = ['sudirman', 'sukarno', 'moh hatta']
    await ctx.send(random.choice(pahlawan))

@bot.command()
async def genpass(ctx, length = 5):
    await ctx.send(gen_pass(length))  
@bot.command()
async def guess(ctx):
    """Guess a number between 1 and 10."""
    await ctx.send('Guess a number between 1 and 10.')

    def is_correct(m):
        return m.author == ctx.author and m.content.isdigit()

    answer = random.randint(1, 10)

    try:
        guess_msg = await bot.wait_for('message', check=is_correct, timeout=5.0)
    except asyncio.TimeoutError:
        await ctx.send(f'Sorry, you took too long. It was {answer}.')
        return

    if int(guess_msg.content) == answer:
        await ctx.send('You are right!')
    else:
        await ctx.send(f'Oops. It is actually {answer}.')
bot.run("Token")
