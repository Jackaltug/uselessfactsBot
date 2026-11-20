import discord
from discord.ext import commands
import requests
import pyttsx3

intents = discord.Intents.default()
intents.message_content = True

#Botun komutlarını aktive edebilmek için kullanılması gereken işaret '!'
bot = commands.Bot(command_prefix='!', intents=intents)

#When the bot is determined that activated bot is ready it displays a text in terminal
@bot.event
async def on_ready():
    print('Bot is ready')


#When command is used, it will greet the person.
@bot.command()
async def Greeting(ctx):
    await ctx.send('I am a Discord bot programmed to give you useless facts that u wont need to know, totally Worth it')

#The Place where 'useless information' is retrieved, When failed to work it will give an error message.
def useless_fact():
    base_url = f"https://uselessfacts.jsph.pl/random.json"
    response = requests.get(base_url)
    if response.status_code ==200:
        return response.json()['text']
    else:
        return 'UselessFact Machine is having problems, Try again in a while.'

#Converts Specified words into spoken words
def speak(text):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()

#Conveys the 'useless information' verbally
@bot.command()
async def usfact(ctx):
    useless_infos = useless_fact()
    await ctx.send(useless_infos)
    speak(useless_infos)


bot.run('BOT_TOKEN')
