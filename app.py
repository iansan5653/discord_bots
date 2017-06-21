import discord
import asyncio
import requests
import random
import praw
import datetime
import string

token = "MjcyOTkyMjI1NzE2MzM4Njg4.C2fBew.EvdYa4lYWforBVGEebCnBuXETm4"

reddit = praw.Reddit(client_id='gZYW4noix22UQA',
                     client_secret="-HsFfCrXNm59gONekaqD-qugkP4",
                     user_agent='Discord:com.theNerds.discordBot:v0 (by /u/iansan5653)')

# Adds a prefix to the trigger for testing
trigPref = ""

client = discord.Client()


@client.event
@asyncio.coroutine on_ready():
    print('Logged in')

# SCPBotCode


@client.event
@asyncio.coroutine on_message(message):
    trigMessage = message.content.lower()
# ScpBotCode
    SCPCodes = [t for t in trigMessage.split() if t.startswith('scp-') or t.startswith('SCP-') or t.startswith('Scp-')]
    if SCPCodes:
        yield from client.send_typing(message.channel)
        msg = SCPCodes[0].split('-', 1)[1]

        if len(msg) <= 4 and len(msg) >= 3 and msg.isdigit():
            tmp_msg = yield from client.send_message(message.channel, '**Link:** http://www.scp-wiki.net/scp-' + msg + ' *Checking for existence...*')
            scp = requests.get('http://www.scp-wiki.net/scp-' + msg)
            if scp.status_code == 200:
                # yield from client.send_typing(message.channel)
                yield from client.edit_message(tmp_msg, '**Link:** http://www.scp-wiki.net/scp-' + msg + ' *SCP exists!*')

                # Someday images may get sent. Not today.
                # tree = BeautifulSoup(scp.text, "lxml")
                # img_link = tree.find_all('div', class_="scp-image-block")[0].img.get('src')
                # yield from client.send_file(message.channel, img_link, filename='SCP-' + msg + '_img', content=None, tts=False)

            elif scp.status_code == 404:
                yield from client.edit_message(tmp_msg, '~~**Link:** http://www.scp-wiki.net/scp-' + msg + '~~ *SCP does not exist.*')
            else:
                yield from client.edit_message(tmp_msg, '**Link:** http://www.scp-wiki.net/scp-' + msg + ' *Unable to determine if this SCP exists.*')

        else:
            yield from client.send_message(message.channel, 'SCP must be a 3 or 4 digit number. Example: `SCP-1175`')
# AyyLmaoBotCode
    elif trigMessage.startswith(trigPref + 'ayy'):
        yield from client.send_message(message.channel, 'lmao')
# StarWarsTitleBotCode
    elif trigMessage.startswith(trigPref + 'sw'):
        msg = message.content.split(' ', 1)[1]
        if len(msg) == 1 and msg.isdigit() and int(msg) >= 0 and int(msg) <= 9:
            titles = {
                1: 'The Phantom Menace',
                2: 'Attack of the Clones',
                3: 'Revenge of the Sith',
                4: 'A New Hope',
                5: 'The Empire Strikes Back',
                6: 'Return of the Jedi',
                7: 'The Force Awakens',
                8: 'The Last Jedi',
                9: '[TBA]'
            }
            yield from client.send_message(message.channel, 'That Star Wars movie is called *' + titles[int(msg)] + '*.')
# LoadingBarBotCode
    elif trigMessage.startswith(trigPref + '!load'):
        x = random.randrange(0, 10)
        loading = yield from client.send_message(message.channel, '`0%   -------------------`')
        yield from asyncio.sleep(x)
        yield from client.edit_message(loading, '`10%  ||------------------`')
        yield from asyncio.sleep(x)
        yield from client.edit_message(loading, '`20%  ||||----------------`')
        yield from asyncio.sleep(x)
        yield from client.edit_message(loading, '`30%  ||||||--------------`')
        yield from asyncio.sleep(x)
        yield from client.edit_message(loading, '`40%  ||||||||------------`')
        yield from asyncio.sleep(x)
        yield from client.edit_message(loading, '`50%  ||||||||||----------`')
        yield from asyncio.sleep(x)
        yield from client.edit_message(loading, '`60%  ||||||||||||--------`')
        yield from asyncio.sleep(x)
        yield from client.edit_message(loading, '`70%  ||||||||||||||------`')
        yield from asyncio.sleep(x)
        yield from client.edit_message(loading, '`80%  ||||||||||||||||----`')
        yield from asyncio.sleep(x)
        yield from client.edit_message(loading, '`90%  ||||||||||||||||||--`')
        yield from asyncio.sleep(x)
        yield from client.edit_message(loading, '`95%  |||||||||||||||||||-`')
        yield from asyncio.sleep(x)
        yield from client.edit_message(loading, '`100% ||||||||||||||||||||`')
        yield from client.send_message(message.channel, 'Loading Complete!')
# PizzaOrderBotCode
    elif trigMessage.startswith(trigPref + '`sudo order pizza`'):
        yield from client.send_message(message.channel, ':pizza:')
# RandomNumberGenCode
    elif trigMessage.startswith(trigPref + '!rand'):
        msgsplit = message.content.split(' ', 3)
        minval = msgsplit[1]
        maxval = msgsplit[2]

        if minval.isdigit() and maxval.isdigit():
            value = random.randrange(int(minval), int(maxval))
            yield from client.send_message(message.channel, 'Your number is: **' + str(value) + '**.')
        else:
            yield from client.send_message(message.channel, 'Invalid command, use syntax `!rand minimum maximum`.')
# RedditBotCode
    elif trigMessage.startswith(trigPref + 'r '):
        subreddit = message.content.split(' ', 1)[1]
        yield from client.send_message(message.channel, 'https://www.reddit.com/r/' + subreddit)

    elif trigMessage.startswith(trigPref + 'u '):
        user = message.content.split(' ', 1)[1]
        yield from client.send_message(message.channel, 'https://www.reddit.com/u/' + user)
        r_user = reddit.redditor(user)
        print(r_user.submissions.new())
        yield from client.send_message(message.channel, 'Link Karma: **' + str(r_user.link_karma) + '**')
        yield from client.send_message(message.channel, 'Comment Karma: **' + str(r_user.comment_karma) + '**')
# RandomIntegerSpam
    elif trigMessage.startswith(trigPref + '!numberspam'):
        loop = 1
        while loop == 1:
            y = random.randrange(1, 100)
            yield from client.send_message(message.channel, y)
# PasswordGen
    elif trigMessage.startswith(trigPref + '!p'):
        passsplit = message.content.split(' ', 1)
        passlen = int(passsplit[1])
        randtextstr = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(passlen))
        yield from client.send_message(message.channel, 'Your password is: ' + randtextstr)
# LennyCode
    elif trigMessage.startswith(trigPref + 'lenny'):
        yield from client.send_message(message.channel, '( ͡° ͜ʖ ͡°)')
# DiceRoll
    elif trigMessage.startswith(trigPref + '!roll'):
            dieRoll = random.randrange(1, 20)
            yield from client.send_message(message.channel, dieRoll)
# WikipediaSearch
    elif trigMessage.startswith(trigPref + 'wiki'):
        wikiSplit = message.content.split(' ')
        wikiSplit.pop(0)
        wikiLink = 'https://en.wikipedia.org/wiki/'
        wiki = "_".join(wikiSplit)
        yield from client.send_message(message.channel, wikiLink + wiki)
# Magic8Ball
    elif trigMessage.startswith(trigPref + 'magic8ball'):
        yield from client.send_message(message.channel, 'To use the Magic 8 Ball, type !8ball and your question...')
    elif trigMessage.startswith(trigPref + '!8ball'):
        answers = ['It is certain',
                   'It is decidedly so',
                   'Without a doubt',
                   'Yes, definitely',
                   'You may rely on it',
                   'As I see it, yes',
                   'Most likely',
                   'Outlook is good',
                   'Yes',
                   'Signs point towards yes',
                   'My vision is hazy, please try again',
                   "I don't want to answer that...",
                   'It would be better to tell you that information at a later date...',
                   'I have no idea',
                   'Concentrate harder, and ask again',
                   "Don't count on it",
                   'I see "no"',
                   '*(counter-terrorist voice)* Negative',
                   'Outlook is bleak at best',
                   'I am very doubtful',
                   "Ha, don't kid yourself"]
        chosenans = random.choice(answers)
        yield from client.send_message(message.channel, chosenans)
# RandomIntegerSpam
    elif trigMessage.startswith(trigPref + '!test'):
        loop = 1
        while loop == 1:
            yield from client.send_message(message.channel, 'PLAYERUNKNOWNS BATTLEGROUNDS')
# Error
    elif trigMessage.startswith(trigPref + 'help'):
        yield from client.send_message(message.channel, 'ERROR CANNOT PROCESS FUNCTION REPORT TO AN ADMINISTRATOR IMMEDIATELY')
# No problem
    elif trigMessage == 'thank you':
        yield from client.send_message(message.channel, 'You\'re welcome.')
client.run(token)
