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

    print(
        "There Was A Error Importing The Lib(s) We Are Fixing The Problems On Our End!"
    )

    run(['pip', 'install', 'discord'])
    run(['pip', 'install', 'random'])
    run(['pip', 'install', 'time'])
    run(['pip', 'install', 'urllib3'])

client = commands.Bot(command_prefix="?", intents=disnake.Intents.all())

status = cycle(["Servers..", "You.."])

@tasks.loop(seconds=5)
async def changeStatus():
    await client.change_presence(status=disnake.Status.dnd, activity=disnake.Activity(type=disnake.ActivityType.watching, name=next(status)))

@client.event
async def on_ready():
    try:
        changeStatus.start()
        print(
            "Our Website: https://us-developers.org/"
        )

        print(
            "-----------------------------------------"
        )

        print(
            "Our Server: https://discord.gg/us-developers"
        )
    except Exception as exception:
        Bot_Management.log_error(__error__=exception)

def __welcome__Screen_():
    try:
        print(
            str(
                "Our Website: https://us-developers.org/"
            )
        )
        print(
            str(
                "------------------------------------------------"
            )
        )

        print(
            str(
                "Our Server: https://discord.gg/us-developers"
            )
        )
    except Exception as exception:
        Bot_Management.log_error(__error__=exception)

__welcome__Screen_()


@commands.slash_command(name="ban", description="Ban(s) A Member From The Server!")
async def ban(ctx: disnake.Message, user: disnake.Member, *, _reason_ = None):
    try:
        if _reason_ is None:
            embed = disnake.Embed(title=f"{user}", description=f"You Have Been Banned From: {ctx.guild} For Reason: {_reason_}", color=disnake.Color.random())
            embed.set_thumbnail(url='https://yt3.ggpht.com/a/AATXAJwuK9jRhUIEeBxYcOE3OnIIgMroXo-E_Ny2_A=s900-c-k-c0xffffffff-no-rj-mo')
            embed.set_footer(icon_url='https://yt3.ggpht.com/a/AATXAJwuK9jRhUIEeBxYcOE3OnIIgMroXo-E_Ny2_A=s900-c-k-c0xffffffff-no-rj-mo', text='𝓑𝔂 𝓥𝓟𝓢-𝓢𝓮𝓻𝓿𝓮𝓻 | 𝓒𝓸𝓭𝓲𝓷𝓰 - 𝓣𝓮𝓪𝓶')
            await user.send(embed=embed)
            await user.ban(reason=_reason_)
            sleep(
                0.4
            )
            __newEmbed__ = disnake.Embed(title=f"{user}", description=f"{user.mention} Has Been Banned At: {time.ctime()}-UTC For: {_reason_}", color=disnake.Color.random())
            __newEmbed__.set_thumbnail(url='https://yt3.ggpht.com/a/AATXAJwuK9jRhUIEeBxYcOE3OnIIgMroXo-E_Ny2_A=s900-c-k-c0xffffffff-no-rj-mo')
            __newEmbed__.set_footer(icon_url='https://yt3.ggpht.com/a/AATXAJwuK9jRhUIEeBxYcOE3OnIIgMroXo-E_Ny2_A=s900-c-k-c0xffffffff-no-rj-mo', text='𝓑𝔂 𝓥𝓟𝓢-𝓢𝓮𝓻𝓿𝓮𝓻 | 𝓒𝓸𝓭𝓲𝓷𝓰 - 𝓣𝓮𝓪𝓶')
            await ctx.channel.send(embed=__newEmbed__)
        else:
            if _reason_ != None:
                try:
                    embed = disnake.Embed(title=f"{user}", description=f"You Have Been Banned From: {ctx.guild} For Reason: {_reason_}", color=disnake.Color.random())
                    embed.set_thumbnail(url='https://yt3.ggpht.com/a/AATXAJwuK9jRhUIEeBxYcOE3OnIIgMroXo-E_Ny2_A=s900-c-k-c0xffffffff-no-rj-mo')
                    embed.set_footer(icon_url='https://yt3.ggpht.com/a/AATXAJwuK9jRhUIEeBxYcOE3OnIIgMroXo-E_Ny2_A=s900-c-k-c0xffffffff-no-rj-mo', text='𝓑𝔂 𝓥𝓟𝓢-𝓢𝓮𝓻𝓿𝓮𝓻 | 𝓒𝓸𝓭𝓲𝓷𝓰 - 𝓣𝓮𝓪𝓶')
                    await user.send(embed=embed)
                    await user.ban(reason=_reason_)
                    __newEmbed__ = disnake.Embed(title=f"{user}", description=f"{user.mention} Has Been Banned At: {time.ctime()}-UTC For: {_reason_}", color=disnake.Color.random())
                    __newEmbed__.set_thumbnail(url='https://yt3.ggpht.com/a/AATXAJwuK9jRhUIEeBxYcOE3OnIIgMroXo-E_Ny2_A=s900-c-k-c0xffffffff-no-rj-mo')
                    __newEmbed__.set_footer(icon_url='https://yt3.ggpht.com/a/AATXAJwuK9jRhUIEeBxYcOE3OnIIgMroXo-E_Ny2_A=s900-c-k-c0xffffffff-no-rj-mo', text='𝓑𝔂 𝓥𝓟𝓢-𝓢𝓮𝓻𝓿𝓮𝓻 | 𝓒𝓸𝓭𝓲𝓷𝓰 - 𝓣𝓮𝓪𝓶')
                    await ctx.channel.send(embed=__newEmbed__)
                except Exception as en:
                    Bot_Management.log_error(__error__=exception)
    except Exception as exception:
        Bot_Management.log_error(__error__=exception)

@commands.slash_command(name="kick", description="Kick(s) A Member From The Server!")
async def kick(ctx: disnake.Message, user: disnake.Member, *, _reason_ = None):
    try:
        if _reason_ is None:
            embed = disnake.Embed(title=f"{user}", description=f"You Have Been Kicked From: {ctx.guild} For Reason: {_reason_}", color=disnake.Color.random())
            embed.set_thumbnail(url='https://yt3.ggpht.com/a/AATXAJwuK9jRhUIEeBxYcOE3OnIIgMroXo-E_Ny2_A=s900-c-k-c0xffffffff-no-rj-mo')
            embed.set_footer(icon_url='https://yt3.ggpht.com/a/AATXAJwuK9jRhUIEeBxYcOE3OnIIgMroXo-E_Ny2_A=s900-c-k-c0xffffffff-no-rj-mo', text='𝓑𝔂 𝓥𝓟𝓢-𝓢𝓮𝓻𝓿𝓮𝓻 | 𝓒𝓸𝓭𝓲𝓷𝓰 - 𝓣𝓮𝓪𝓶')
            await user.send(embed=embed)
            await user.kick(reason=_reason_)
            sleep(
                0.4
            )
            __newEmbed__ = disnake.Embed(title=f"{user}", description=f"{user.mention} Has Been Kicked At: {time.ctime()}-UTC For: {_reason_}", color=disnake.Color.random())
            __newEmbed__.set_thumbnail(url='https://yt3.ggpht.com/a/AATXAJwuK9jRhUIEeBxYcOE3OnIIgMroXo-E_Ny2_A=s900-c-k-c0xffffffff-no-rj-mo')
            __newEmbed__.set_footer(icon_url='https://yt3.ggpht.com/a/AATXAJwuK9jRhUIEeBxYcOE3OnIIgMroXo-E_Ny2_A=s900-c-k-c0xffffffff-no-rj-mo', text='𝓑𝔂 𝓥𝓟𝓢-𝓢𝓮𝓻𝓿𝓮𝓻 | 𝓒𝓸𝓭𝓲𝓷𝓰 - 𝓣𝓮𝓪𝓶')
            await ctx.channel.send(embed=__newEmbed__)
        else:
            if _reason_ != None:
                try:
                    embed = disnake.Embed(title=f"{user}", description=f"You Have Been Kicked From: {ctx.guild} For Reason: {_reason_}", color=disnake.Color.random())
                    embed.set_thumbnail(url='https://yt3.ggpht.com/a/AATXAJwuK9jRhUIEeBxYcOE3OnIIgMroXo-E_Ny2_A=s900-c-k-c0xffffffff-no-rj-mo')
                    embed.set_footer(icon_url='https://yt3.ggpht.com/a/AATXAJwuK9jRhUIEeBxYcOE3OnIIgMroXo-E_Ny2_A=s900-c-k-c0xffffffff-no-rj-mo', text='𝓑𝔂 𝓥𝓟𝓢-𝓢𝓮𝓻𝓿𝓮𝓻 | 𝓒𝓸𝓭𝓲𝓷𝓰 - 𝓣𝓮𝓪𝓶')
                    await user.send(embed=embed)
                    await user.kick(reason=_reason_)
                    __newEmbed__ = disnake.Embed(title=f"{user}", description=f"{user.mention} Has Been Kicked At: {time.ctime()}-UTC For: {_reason_}", color=disnake.Color.random())
                    __newEmbed__.set_thumbnail(url='https://yt3.ggpht.com/a/AATXAJwuK9jRhUIEeBxYcOE3OnIIgMroXo-E_Ny2_A=s900-c-k-c0xffffffff-no-rj-mo')
                    __newEmbed__.set_footer(icon_url='https://yt3.ggpht.com/a/AATXAJwuK9jRhUIEeBxYcOE3OnIIgMroXo-E_Ny2_A=s900-c-k-c0xffffffff-no-rj-mo', text='𝓑𝔂 𝓥𝓟𝓢-𝓢𝓮𝓻𝓿𝓮𝓻 | 𝓒𝓸𝓭𝓲𝓷𝓰 - 𝓣𝓮𝓪𝓶')
                    await ctx.channel.send(embed=__newEmbed__)
                except Exception as exception:
                    Bot_Management.log_error(__error__=exception)
    except Exception as exception:
        Bot_Management.log_error(__error__=exception)
