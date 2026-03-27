import os
import discord
import random
from discord.ext import commands
from passgen import gen_pass
import asyncio
import requests
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
async def about(ctx):
    await ctx.send("""
$hello - Menyapa
$heh - tertawa sebanyak number
$gacha - random pahlawan indonesia
$genpass - password random
$guess - Menebak angka 1 - 10  
$mem - generate meme image
$duck - generate random duck picture
$howto - kasih informasi mengenai polusi kendaraan (mobil, motor, pesawat)
""")

@bot.command()
async def howto(ctx, perintah):
    if perintah == "mobil":
        await ctx.send("""Mobil yang ada di jalanan merupakan penyumbang utama polusi jakarta melepaskan emisi karbon monoksida, nitrogen dioksida. 
                       Dampaknya meliputi penyakit pernapasan, kardiovaskular, dan risiko kesehatan reproduksi, serta mencemari udara dalam kabin mobil
                       """)
    elif perintah == "motor":
        await ctx.send(""" Motor yang sering kita pakai untuk kegiatan sehari-hari merupakan penyumbang utama polusi kota besar melepaskan emisi karbon monoksida, nitrogen oksida
                       polusi ini menyumbang penyakit pernafasan dan pemanasan global """)
    elif perintah == "pesawat":
        await ctx.send(""" Pesawat juga penyumbang polusi akan tetapi dampak nya tergantung jenis pesawat. Pesawat kormesial sekitar 2% polusi
                       dan Pesawat private 10X lipat dampak polusi dan menyumbang global warming paling banyak dan jenis masalah pernafasan              
""")
    else:
        await ctx.send("tidak ada di database ketik lain")

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
@bot.command()
async def mem(ctx):
    image_name = random.choice(os.listdir('images'))
    with open('images/' + image_name, 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    '''Setelah kita memanggil perintah bebek (duck), program akan memanggil fungsi get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def rarememe(ctx):
    """
    Mengirim meme dengan tingkat kelangkaan:
    - Common (60%)
    - Rare (25%)
    - Epic (10%)
    - Legendary (5%)
    """
    rarity_tiers = {
        'common': 0.60,
        'rare': 0.25,
        'epic': 0.10,
        'legendary': 0.05
    }

    tier = random.choices(
        population=list(rarity_tiers.keys()),
        weights=list(rarity_tiers.values()),
        k=1
    )[0]
    folder_path = f'images/{tier}'
    if not os.path.exists(folder_path) or not os.listdir(folder_path):
        await ctx.send(f"Folder untuk meme {tier} belum tersedia atau kosong. Tambahkan gambar ke folder `{folder_path}`.")
        return
    
    image_name = random.choice(os.listdir(folder_path))
    image_path = os.path.join(folder_path, image_name)

    with open(image_path, 'rb') as f:
        picture = discord.File(f)

    await ctx.send(f"** Meme {tier.capitalize()} **")
    await ctx.send(file=picture)

bot.run("Token")
