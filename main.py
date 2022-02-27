import discord
import random
from discord.ext import commands, tasks
from itertools import cycle
import music
from dotenv import load_dotenv
import os

load_dotenv()

cogs =[music]
client = commands.Bot(command_prefix = '-',
intents = discord.Intents.all())
status = cycle(['HENTAI ULTIMATE V','Hentai onichan','with your mom','Hentai fighting game 2'])

@client.event
async def on_ready():
    change_status.start()
    # await client.change_presence(status=discord.Status.online,activity=discord.Game('HENTAI ULTIMATE 5'))
    print('Bot is ready')
#---------------------COMMANDS FOR MUSIC---------------




for i in range(len(cogs)):
    cogs[i].setup(client)
# @client.command()
# async def play(ctx, url: str):
#     song_there 
#     voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='general')
#     voice = discord.utils.get(client.voice_clients, guild = ctx.guild)
#     if not voice.is_connected():
#         await voiceChannel.connect()

# @client.command()
# async def leave(ctx):
#     voice = discord.utils.get(client.voice_clients, guild = ctx.guild)
#     if voice.is_connected():
#         await voice.disconnect()
#     else:
#         await ctx.send("The bot is not connected to a voice channel.")

# @client.command()
# async def pause(ctx):
#     voice = discord.utils.get(client.voice_clients, guild = ctx.guild)
#     if voice.is_playing():
#         voice.pause()
#     else:
#         await ctx.send("Currently no audio is playing.")

# @client.command()
# async def resume(ctx):
#     voice = discord.utils.get(client.voice_clients, guild = ctx.guild)
#     if voice.is_paused():
#         voice.resume()
#     else:
#         await ctx.send("The audio is not paused.")


# @client.command()
# async def stop(ctx):
#     voice = discord.utils.get(client.voice_clients, guild = ctx.guild)
#     voice.stop()
#_______________________________________________________
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Invalid command used. Please use !help')


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command()
#@commands.has_permissions(menage_messages= True)
async def clear(ctx,amount:int):
    if(amount <= 0):
        amount = 1
    channel = ctx.message.channel
    deleted = await channel.purge(limit = amount)
    await channel.send('Deleted {} message(s)'.format(len(deleted)))

@clear.error
async def clear(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please specify an amount of messages to delete')

@client.command(aliases=['8ball','test'])
async def _8ball(ctx, *, question):
    responses = ["As I see it, yes.", 
                "Ask again later.", 
                "Better not tell you now.",   
                "Cannot predict now.", 
                "Concentrate and ask again.",
                "Don't count on it.", 
                "It is certain.", 
                "It is decidedly so.", 
                "Most likely.", 
                "My reply is no.", 
                "My sources say no.",
                "Outlook not so good.", 
                "Outlook good.", 
                "Reply hazy, try again.", 
                "Signs point to yes.", 
                "Very doubtful.", 
                "Without a doubt.",
                "Yes.", 
                "Yes - definitely.", 
                "You may rely on it."]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')


@client.command()
async def load(ctx, extension):
    client.load_extension()


@tasks.loop(seconds=4000)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))



client.run(os.getenv('TOKEN'))
# import discord
# import random

# TOKEN = 'OTQ3MTEwNzA4NjE1NzM3NDA1.YhoflQ.MnE0goTbWNEW6NMXWFkdePNo09A'

# client = discord.Client()

# @client.event
# async def on_ready():
#     print('We have logged in as {0.user}'.format(client))

# @client.event
# async def on_message(message):
#     username = str(message.author).split('#')[0]
#     user_message = str(message.content)
#     channel = str(message.channel.name)
#     print(f'{username}: {user_message} ({channel})')

#     if message.author == client.user:
#         return
#     if user_message.lower() == 'hello':
#         await message.channel.send(f'Hello {username}!')
#         return
#     elif user_message.lower() == 'bye':
#         await message.channel.send(f'Bye {username}!')
#         return
#     elif user_message.lower() == '!random':
#         response = f'This is your random number: {random.randrange(100)}'
#         await message.channel.send(response)


# client.run(TOKEN)