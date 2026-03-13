import discord
from discord.ext import commands
from passgen import gen_pass
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
bot.run("Token")
