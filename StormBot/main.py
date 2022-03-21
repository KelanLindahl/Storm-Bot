from operator import contains
import random
from tokenize import String
from nextcord.ext import commands
import os
import time
import json
from dotenv import load_dotenv
import nextcord

load_dotenv()
token = os.getenv('KEY')

artistsf=open('artists.json',)
artistlist=json.load(artistsf)

headscount=0
tailscount=0

#This sets the command prefix to !. I.e !add will run the add function.
bot = commands.Bot(command_prefix='!')

#The channel ID for the target channel where the bot will post logging functions
loggingchannel=795460193763983401

#Add function for the bot w/ error catching
@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a+b)
@add.error
async def add_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('Cannot compute! Please follow the format "!add num1 num2"')

#Subtraction function
@bot.command()
async def subtract(ctx, a: int, b: int):
    await ctx.send(a-b)
@subtract.error
async def subtract_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('Cannot compute! Please follow the format "!subtract num1 num2"')

 #Multiplication function       
@bot.command()
async def mult(ctx, a: int, b: int):
    await ctx.send(a*b)
@mult.error
async def mult_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('Cannot compute! Please follow the format "!mult num1 num2"')
#Division Function
@bot.command()
async def div(ctx, a: int, b: int):
    await ctx.send(a/b)
@div.error
async def div_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('Cannot compute! Please follow the format "!div num1 num2"')


@bot.command()
async def coinflip(ctx):
    flip=random.randint(0,1)
    if flip==0:
        await ctx.send('Flipping...')
        time.sleep(1)
        await ctx.send('Flipping...')
        time.sleep(1)
        await ctx.send('Flipping...')
        time.sleep(1)
        await ctx.send('Heads!')
        headscount=+1
    else:
        await ctx.send('Flipping...')
        time.sleep(1)
        await ctx.send('Flipping...')
        time.sleep(1)
        await ctx.send('Flipping...')
        time.sleep(1)
        await ctx.send('Tails!')
        tailscount=+1
@bot.command()
async def coincount(ctx):
    totalcount=headscount+tailscount
    await ctx.send(f'The coin has been flipped {totalcount} times! Heads has won {headscount} times! Tails has won {tailscount} times!')   

@bot.command()
async def test(ctx):
    await ctx.send(ctx.author)

#Artist guessing game
@bot.command()
async def atgame(ctx):
    artistpick=random.randint(1, 11)
    await ctx.send('Who sings this lyric?!')
    time.sleep(.5)
    await ctx.send(artistlist[f'{artistpick}'][0]['Lyrics'])
    
    artname=artistlist[f'{artistpick}'][0]['Artist']
    artname=artname.lower()

    artsong=artistlist[f'{artistpick}'][0]['Song']
    
    guess=await bot.wait_for('message')
    ans=guess.content
    ans=ans.lower()
 
    while (guess.author != ctx.author):
        await ctx.send("Please wait your turn!")
        guess=await bot.wait_for('message')
        ans=guess.content
        ans=ans.lower()
    if (guess.author == ctx.author):
        if artname in ans:
            await ctx.send(f"Correct! The song is {artistlist[f'{artistpick}'][0]['Song']} by {artname}!") 
            print(guess, artname)
        else:   
            await ctx.send(f"Wrong! Do !atgame to try again!")
            print(guess, artname)
        


#------Events--------
# Posts a message in target channel whenever a message is deleted.
@bot.event
async def on_message_delete(message):
    logging=bot.get_channel(loggingchannel)
    embed = nextcord.Embed(title=f"Deleted Message")
    embed.add_field(name="Author:", value=f"{message.author.name}", inline=False)
    embed.add_field(name="Channel:", value=f"{message.channel}", inline=False)
    embed.add_field(name="Contents:", value=f"{message.content}", inline=False)
    await logging.send(embed=embed)

@bot.event
async def on_message_edit(message_before, message_after):
    logging=bot.get_channel(loggingchannel)
    embed=nextcord.Embed(title=f"Edited Message")
    embed.add_field(name="Author:", value=f"{message_before.author}", inline=False)
    embed.add_field(name="Before Edit:", value=f"{message_before.content}", inline=False)
    embed.add_field(name="After Edit:", value=f"{message_after.content}", inline=False)
    await logging.send(embed=embed)

#Run argument
bot.run(token)
artistsf.close()