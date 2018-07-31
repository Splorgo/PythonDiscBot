import discord
import random
import logging
from discord.ext import commands

'''init'''
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


bot = commands.Bot(command_prefix='loli ', description ='Hmm, what do you want?')
bot.remove_command('help')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

client = discord.Client()
print(client.user)


'''Need to use definitions to smooth stuff out'''
def RandomTrap():
    '''very low effort randomiser, pls no hate
        Why the fuck did i do this            '''
    
    num1 = random.randint(0,15)

    if num1 == 0:
        URL = "https://vignette.wikia.nocookie.net/anime-traps/images/7/7f/49537.jpg/revision/latest?cb=20121116151345"

    if num1 == 1:
        URL = "https://vignette.wikia.nocookie.net/anime-traps/images/6/6c/Rider_of_Black1.png/revision/latest?cb=20170827051830"

    if num1 == 2:
        URL = "https://vignette.wikia.nocookie.net/anime-traps/images/6/6d/Pico.jpg/revision/latest?cb=20140314004056"

    if num1 == 3:
        URL = "https://vignette.wikia.nocookie.net/anime-traps/images/d/df/Mizuho.png/revision/latest?cb=20130528024617"

    if num1 == 4:
        URL = "https://vignette.wikia.nocookie.net/anime-traps/images/1/16/Kotori_chan_by_catgirl0926-d55ae2z.jpg/revision/latest?cb=20130601034521"

    if num1 == 5:
        URL = "https://vignette.wikia.nocookie.net/anime-traps/images/9/92/340715.jpg/revision/latest?cb=20180728205320"

    if num1 == 6:
        URL = "https://vignette.wikia.nocookie.net/anime-traps/images/0/0b/AoiHyoudouLoli.jpg/revision/latest?cb=20180729220129"

    if num1 == 7:
        URL = "https://vignette.wikia.nocookie.net/anime-traps/images/c/c3/Ruka_Urushibara.jpg/revision/latest?cb=20130918003922"

    if num1 == 8:
        URL = "https://vignette.wikia.nocookie.net/anime-traps/images/b/b4/NagisaAnime.jpg/revision/latest?cb=20151112034501"

    if num1 == 9:
        URL = "https://vignette.wikia.nocookie.net/anime-traps/images/8/84/Gasper_Vladi.png/revision/latest?cb=20160615023718"

    if num1 == 10:
        URL = "https://vignette.wikia.nocookie.net/anime-traps/images/0/06/Ryuunosuke_Akasaka.jpg/revision/latest?cb=20130918032800"

    if num1 == 11 or num1 == 12:
        URL = "https://vignette.wikia.nocookie.net/anime-traps/images/6/6e/Cute_Hitoshi.png/revision/latest?cb=20170923222338"

    if num1 == 13:
        URL = "https://vignette.wikia.nocookie.net/anime-traps/images/3/3f/Damn%2Bright%2Btequila%2Bjoseph%2Bis%2Bbest%2Bgirl%2B_1c991a79ac29ad85b3ed40314a83e8dd.png/revision/latest?cb=20180227195717"

    if num1 == 14:
        URL = "https://vignette.wikia.nocookie.net/anime-traps/images/6/64/MareBelloFiore_%28komuzuka%29.png/revision/latest?cb=20180125024353"

    if num1 == 15:
        URL = "https://pbs.twimg.com/profile_images/465548645568221184/wtR3VCbp_400x400.jpeg"
    return URL



'''commands'''

@bot.command()
async def lenny(ctx):
    await ctx.send("( ͡° ͜ʖ ͡°)")

@bot.command()
async def noods(ctx):
    await ctx.send("https://i.kym-cdn.com/photos/images/original/001/301/366/7c1.jpg")

@bot.command()
async def greet(ctx):
    await ctx.send(":smiley: :wave: Henlo ugly!")

@bot.command()
async def girl(ctx):
    await ctx.send(RandomTrap())


@bot.command()
async def info(ctx):
    embed = discord.Embed(title="Piece 'o shit bot",
                          description="Really just trash, a shitpost of epic proportions.", color=0xeee657)
    
    embed.add_field(name="Author", value="Splorg")

    embed.add_field(name="Number of idiots who've installed it", value=f"{len(bot.guilds)}")

    embed.add_field(name="Don't click", value="https://discordapp.com/api/oauth2/authorize?client_id=473536005446828032&permissions=6144&scope=bot")

    await ctx.send(embed=embed)

    
@bot.command()
async def help(ctx):
    
    embed = discord.Embed(title="A retarded, waste of time bot", description="Does random stupid shit I thought of after not sleeping for over a day", color=0xe57fef)

    embed.add_field(name= "loli lenny" ,value= "Does a thing", inline = False)
    embed.add_field(name= "loli noods" ,value= "Sends noods ( ͡° ͜ʖ ͡°)", inline = False)
    embed.add_field(name= "loli greet" ,value= "A friendly hello", inline = False)
    embed.add_field(name= "loli girl" ,value= "Gives a random \"girl\"", inline = False)
    embed.add_field(name= "loli info" ,value= "Tells you what you need to know", inline = False)
    embed.add_field(name= "loli help" ,value= "Is unhelpfuly helpful", inline = False)
    
    await ctx.send(embed=embed)
    


'''end'''
bot.run("")     #key goes here
