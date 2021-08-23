#!/usr/bin/python3
# bot.py
import os
import random
import pygame
#import ffmpeg

pygame.mixer.init()

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='93', help='Prints a random Crowley quote')
async def ninetythree(ctx):
    pranayama_quotes = [
        'O my God! One is Thy Beginning! One is Thy Spirit, and Thy Permutation One!',
        'And these twelve rays are one.',
        'To Me!',
        'Do what thou wilt shall be the whole of the law',
        'I spit on your crapulous creed!',
        'In His Victory I pursued His enemies; yea I drave them down the steep; I thundered after them into the utmost abyss; yea, therein I partook of the glory of my Lord.',
        'Democracy dodders.',
        'There is little danger that any student, however idle or stupid, will fail to get some result; but there is great danger that he will be led astray, obsessed and overwhelmed by his results, even though it be by those which it is necessary that he should attain. Too often, moreover, he mistaketh the first resting-place for the goal, and taketh off his armour as if he were a victor ere the fight is well begun.',

    ]

    response = random.choice(pranayama_quotes)
    await ctx.send(response)

@bot.command(name='roll_dice', help='Simulates rolling dice.')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))

@bot.command(name='meditate', help="Metronome timer for breathing.\nDuration is measured in minutes, while Inhale, Hold, and Exhale are measured in seconds.\nExample: '!meditate 1 1 1 1' would create a 60 second meditation with 1 second each of inhale, hold, and exhale.\nYou can enter a 0 for Hold but the others must be non-zero integers. No decimals.")
async def meditate(ctx, duration: int, inhale: int, hold: int, exhale: int):
    await ctx.send(f"93, {ctx.author.mention}!\nYou are now meditating for "+str(duration)+" minutes with a "+str(inhale)+" second inhale breath, a "+str(hold)+" second hold, and a "+str(exhale)+" second exhale.")
    nohold = False
    if hold == 0:
        nohold = True
    def pranayama(duration):
        duration = duration * 60
        while duration > 0:
            pygame.mixer.music.load("inhalebeep.wav")
            pygame.mixer.music.play()
            pygame.time.delay(int(inhale)*1000)

            if not nohold:
                pygame.mixer.music.load("holdbeep.wav")
                pygame.mixer.music.play()
                pygame.time.delay(int(hold)*1000)
        
            pygame.mixer.music.load("exhalebeep.wav")
            pygame.mixer.music.play()
            pygame.time.delay(int(exhale)*1000)
        
            if not nohold:
                pygame.mixer.music.load("holdbeep.wav")
                pygame.mixer.music.play()
                pygame.time.delay(int(hold)*1000)
            duration = duration - (inhale+hold+exhale+hold)
            #return (str(duration)+" seconds remain")
            countdown = (str(duration)+" seconds remain")
            print(countdown)
            #await ctx.send(countdown)

    await ctx.send(pranayama(duration))


'''
@client.command(
    name='vuvuzela',
    description='Plays an awful vuvuzela in the voice channel',
    pass_context=True,
)
async def vuvuzela(context):
    # grab the user who sent the command
    user=context.message.author
    voice_channel=user.voice.voice_channel
    channel=None
    # only play music if user is in a voice channel
    if voice_channel!= None:
        # grab user's voice channel
        channel=voice_channel.name
        await client.say('User is in channel: '+ channel)
        # create StreamPlayer
        vc= await client.join_voice_channel(voice_channel)
        player = vc.create_ffmpeg_player('beep.mp3', after=lambda: print('done'))
        player.start()
        while not player.is_done():
            await asyncio.sleep(1)
        # disconnect after the player has finished
        player.stop()
        await vc.disconnect()
    else:
        await client.say('User is not in a channel.')
'''

bot.run(TOKEN)

#fart