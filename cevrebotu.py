import discord
import random
import asyncio
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='.', intents=intents)

tavsiye = [
    "Bugün plastik poşet yerine bez çanta kullanmaya ne dersiniz?",
    "Bisiklet sürmek hem sağlıklı hem çevre dostu!",
    "Bugün enerji tasarrufu için ışıkları kapatmayı unutmayın!"
]

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith(".uzayda görevi biten araçları ne yapmalıyız?"):
        await message.channel.send("Görevi biten araçlar kendini imha edebilir.") 

    if message.content.startswith(".İnsanlar çevresini nasıl temiz tutar?"):
        await message.channel.send("Çöpleri çöpe, diğer atıkları geri dönüşüme atmalıyız.")

    if message.content.startswith(".çevreyi kirleten birini gördüğümüzde ne yapmalıyız?"):
        await message.channel.send("Kirleten kişiyi nazikçe uyarıp doğrusunu göstermeliyiz.")

    if message.content.startswith(".fosil yakıt kullanımına nasıl dikkat edebiliriz?"):
        await message.channel.send("Yenilenebilir enerji kaynaklarının kullanımı artırmak fosil yakıt kullanımını azaltmak.")

    if message.content.startswith(".deniz ve okyanus kirliliği için ne yapabiliriz?"):
        await message.channel.send("Deniz temizleyici robotlar kullanılmalı ve kirletmemeye dikkat edilmeli.")

    if message.content.startswith(".hello"):
        await message.channel.send(f"Merhaba {message.author}! Ben botum.")
    
    await bot.process_commands(message)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba {ctx.author}! Ben çevre dostu bir botum!')
    await asyncio.sleep(1)
    await ctx.send(f'Haydi biraz konuşalım!')

@bot.command()
async def günlüktavsiye(ctx):
    await bot.wait_until_ready()
    channel = bot.get_channel(1258856990994858179)  
    if channel:
        bilgi = random.choice(tavsiye)
        await channel.send(f'Günün tavsiyesi: {bilgi}')
    else:
        await ctx.send("Kanal bulunamadı.")

@bot.command()
async def sohbet(ctx):
    await ctx.send(f'Merhaba! Ne hakkında konuşalım?')

@bot.command()
async def cevreöneri(ctx):
    await ctx.send(f"eğer 18 yaşından küçükseniz '.cevrekucuk' yazınız eğer 18 yaşından büyük iseniz '.cevrebuyuk' yazın")

# Küçükler için
@bot.command()
async def cevrekucuk(ctx):
    await ctx.send(f'Çevre ve kirlilik hakkında bir şey yapmak istiyorsanız `.oneriev1` veya `.oneridısarı1` komutunu kullanın!')

@bot.command()
async def oneriev1(ctx):
    await ctx.send(f'Geri dönüşüm ve hangi malzemelerin geri dönüştürülebileceği hakkında bilgi edinin ve günlük yaşamınızda geri dönüştürülebilir malzemeleri kullanın.')
    await asyncio.sleep(1)
    await ctx.send(f'Gereksiz ısıkları açık bırakmayın.')
    await asyncio.sleep(1)
    await ctx.send(f'Evinizde ısı yalıtımına sahip olun.')

@bot.command()
async def oneridısarı1(ctx):
    await ctx.send(f'Toplu taşıma kullanalım.')
    await asyncio.sleep(1)
    await ctx.send(f'Yerleri çöp atmayalım.')
    await asyncio.sleep(1)
    await ctx.send(f'Atık pilleri çöpe değil atık pil kutusuna atalım.')
    await asyncio.sleep(1)
    await ctx.send(f'Tek kullanımlık tabak bardak çatal yerine seramik veya metal olarak kullanalım.')
    await asyncio.sleep(1)
    await ctx.send(f'Naylon poşet kullanımını azaltın.')

# Büyükler için
@bot.command()
async def cevrebuyuk(ctx):
    await ctx.send(f'Çevre ve kirlilik hakkında bir şey yapmak istiyorsanız `.oneriev`, `.oneridısarı` veya `.oneritoplum` komutunu kullanın!')

@bot.command()
async def oneriev(ctx):
    await ctx.send(f'Geri dönüşüm ve hangi malzemelerin geri dönüştürülebileceği hakkında bilgi edinin ve günlük yaşamınızda geri dönüştürülebilir malzemeleri kullanın.')
    await asyncio.sleep(1)
    await ctx.send(f'Kullanılmış yağları lavaboya dökmeyin.')
    await asyncio.sleep(1)
    await ctx.send(f'Gereksiz ısıkları açık bırakmayın.')
    await asyncio.sleep(1)
    await ctx.send(f'Evinizde ısı yalıtımına sahip olun.')

@bot.command()
async def oneridısarı(ctx):
    await ctx.send(f'Toplu taşıma kullanalım.')
    await asyncio.sleep(1)
    await ctx.send(f'Yerleri çöp atmayalım.')
    await asyncio.sleep(1)
    await ctx.send(f'Atık pilleri çöpe değil atık pil kutusuna atalım.')
    await asyncio.sleep(1)
    await ctx.send(f'Tek kullanımlık tabak bardak çatal yerine seramik veya metal olarak kullanalım.')
    await asyncio.sleep(1)
    await ctx.send(f'Naylon poşet kullanımını azaltın.')

@bot.command()
async def yazitura(ctx):
    para = random.randint(0, 1)
    if para == 0:
        await ctx.send("YAZI")
    else:
        await ctx.send("TURA")

@bot.command()
async def image(ctx):
    with open(r'fotolar\hava-kirliliginin-etkileri-810x810.webp', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)

@bot.command()
async def resim(ctx):
    with open(r'fotolar\air-pollution.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    await asyncio.sleep(1)
    await ctx.send(f'Hep birlikte tercih ve alışkanlıklarımızı değiştirerek çevre kirliliği sorununu çözmeye çalışalım ve dünyamızı temiz tutalım.')


# Bot token'ınızı buraya ekleyin
bot.run("")
