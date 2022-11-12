"""Viper -> Discord Bot"""

from subprocess import run

try:
    from urllib3 import request
    from time import sleep
    import random as rn
    import disnake
    import Bot_Management
    from disnake.ext import commands, tasks
    from itertools import cycle
    import time


except:
    print("There Was A Error Importing The Lib(s) We Are Fixing The Problems On Our End!")
    run(['pip', 'install', 'discord'])
    run(['pip', 'install', 'random'])
    run(['pip', 'install', 'time'])
    run(['pip', 'install', 'urllib3'])

client = commands.Bot(command_prefix="?", intents=disnake.Intents.all())

status = cycle(["Servers..", "You.."])


@tasks.loop(seconds=5)
async def changeStatus():
    await client.change_presence(status=disnake.Status.dnd,
                                 activity=disnake.Activity(type=disnake.ActivityType.watching, name=next(status)))


@client.event
async def on_ready():
    try:
        changeStatus.start()
        print("Our Website: https://us-developers.org/\n"
              "-----------------------------------------\n"
              "Our Server: https://discord.gg/us-developers")

    except Exception as exception:
        Bot_Management.log_error(__error__=exception)


def __welcome__Screen_():
    try:
        print("Our Website: https://us-developers.org/\n"
              "------------------------------------------------\n"
              "Our Server: https://discord.gg/us-developers")

    except Exception as exception:
        Bot_Management.log_error(__error__=exception)


@client.slash_command(name="ban", description="Bans A Member From The Server!")
async def ban_user(inter, user: disnake.Member, *, _reason_=None):
    try:
        _reason_ = _reason_ or "No Reason Provided!"
        if _reason_ is None:
            embed = disnake.Embed(title=f"{user}",
                                  description=f"You Have Been Banned From: {inter.guild} For Reason: {_reason_}",
                                  color=disnake.Color.random()) \
                .set_thumbnail(
                url='https://yt3.ggpht.com/a/AATXAJwuK9jRhUIEeBxYcOE3OnIIgMroXo-E_Ny2_A=s900-c-k-c0xffffffff-no-rj-mo') \
                .set_footer(
                icon_url='https://yt3.ggpht.com/a/AATXAJwuK9jRhUIEeBxYcOE3OnIIgMroXo-E_Ny2_A=s900-c-k-c0xffffffff-no-rj-mo',
                text='𝓑𝔂 𝓥𝓟𝓢-𝓢𝓮𝓻𝓿𝓮𝓻 | 𝓒𝓸𝓭𝓲𝓷𝓰 - 𝓣𝓮𝓪𝓶')

            await user.send(embed=embed)
            await user.ban(reason=_reason_)

            __newEmbed__ = disnake.Embed(title=f"{user}",
                                         description=f"{user.mention} Has Been Banned At: {time.ctime()}-UTC For: {_reason_}",
                                         color=disnake.Color.random()) \
                .set_thumbnail(
                url='https://yt3.ggpht.com/a/AATXAJwuK9jRhUIEeBxYcOE3OnIIgMroXo-E_Ny2_A=s900-c-k-c0xffffffff-no-rj-mo') \
                .set_footer(
                icon_url='https://yt3.ggpht.com/a/AATXAJwuK9jRhUIEeBxYcOE3OnIIgMroXo-E_Ny2_A=s900-c-k-c0xffffffff-no-rj-mo',
                text='𝓑𝔂 𝓥𝓟𝓢-𝓢𝓮𝓻𝓿𝓮𝓻 | 𝓒𝓸𝓭𝓲𝓷𝓰 - 𝓣𝓮𝓪𝓶')

            await inter.response.send_message(embed=__newEmbed__)
    except Exception as exception:
        Bot_Management.log_error(__error__=exception)


@client.slash_command(name="kick", description="Kick(s) A Member From The Server!")
async def kick_user(inter, user: disnake.Member, *, _reason_=None):
    try:
        _reason_ = _reason_ or "No Reason Provided!"
        if _reason_ is None:
            embed = disnake.Embed(title=f"{user}",
                                  description=f"You Have Been Kicked From: {inter.guild} For Reason: {_reason_}",
                                  color=disnake.Color.random())
            embed.set_thumbnail(
                url='https://yt3.ggpht.com/a/AATXAJwuK9jRhUIEeBxYcOE3OnIIgMroXo-E_Ny2_A=s900-c-k-c0xffffffff-no-rj-mo')
            embed.set_footer(
                icon_url='https://yt3.ggpht.com/a/AATXAJwuK9jRhUIEeBxYcOE3OnIIgMroXo-E_Ny2_A=s900-c-k-c0xffffffff-no-rj-mo',
                text='𝓑𝔂 𝓥𝓟𝓢-𝓢𝓮𝓻𝓿𝓮𝓻 | 𝓒𝓸𝓭𝓲𝓷𝓰 - 𝓣𝓮𝓪𝓶')
            await user.send(embed=embed)
            await user.kick(reason=_reason_)
            sleep(0.4)

            __newEmbed__ = disnake.Embed(title=f"{user}",
                                         description=f"{user.mention} Has Been Kicked At: {time.ctime()}-UTC For: {_reason_}",
                                         color=disnake.Color.random()) \
                .set_thumbnail(
                url='https://yt3.ggpht.com/a/AATXAJwuK9jRhUIEeBxYcOE3OnIIgMroXo-E_Ny2_A=s900-c-k-c0xffffffff-no-rj-mo') \
                .set_footer(
                icon_url='https://yt3.ggpht.com/a/AATXAJwuK9jRhUIEeBxYcOE3OnIIgMroXo-E_Ny2_A=s900-c-k-c0xffffffff-no-rj-mo',
                text='𝓑𝔂 𝓥𝓟𝓢-𝓢𝓮𝓻𝓿𝓮𝓻 | 𝓒𝓸𝓭𝓲𝓷𝓰 - 𝓣𝓮𝓪𝓶')
            await inter.response.send_message(embed=__newEmbed__)


    except Exception as exception:
        Bot_Management.log_error(__error__=exception)

client.run(' token ')
