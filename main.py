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

client = commands.Bot(command_prefix="v!", intents=disnake.Intents.all())

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


@client.command(name="kick")
@commands.has_permissions(kick_members=True)
async def kick(ctx: disnake.Message, __member__: disnake.Member, *, __reason__=None):
    try:
        if __reason__ is None:
            try:
                __memberEmbed__ = disnake.Embed(title="Kicked", description=f"You Have Been Kicked For: {__reason__}",
                                                color=disnake.Color.red()) \
                    .set_thumbnail(url="https://th.bing.com/th/id/OIP.COYEZS1SJ4znwY6931asnAAAAA?pid=ImgDet&rs=1")
                await __member__.send(
                    embed=__memberEmbed__
                )
                sleep(
                    0.5
                )
                await __member__.kick(
                    reason=__reason__
                )
                __MainEmbed__ = disnake.Embed(title=__member__,
                                              description=f"Successfully Kicked: {__member__} For: {__reason__}") \
                    .set_thumbnail(
                    url='https://th.bing.com/th/id/OIP.COYEZS1SJ4znwY6931asnAAAAA?pid=ImgDet&rs=1'
                ) \
                    .set_footer(
                    icon_url='https://th.bing.com/th/id/OIP.-lq5B5ai5OKQVAIjC9VFqAHaDe?w=308&h=164&c=7&r=0&o=5&dpr=1.5&pid=1.7',
                    text="𝓑𝔂 𝓥𝓟𝓢-𝓢𝓮𝓻𝓿𝓮𝓻 | 𝓒𝓸𝓭𝓲𝓷𝓰 - 𝓣𝓮𝓪𝓶"
                )
                await ctx.channel.send(
                    embed=__MainEmbed__
                )
            except Exception as en:
                Bot_Management.log_error(__error__=en)
                __exception_embed__ = disnake.Embed(title="Exception",
                                                    description="Cannot Kick The Following Member: " + __member__.mention)
                __exception_embed__.set_thumbnail(url='https://media.giphy.com/media/cjIs6qePAqUU0/giphy.gif')
                __exception_embed__.set_footer(icon_url='https://media.giphy.com/media/cjIs6qePAqUU0/giphy.gif',
                                               text="Check Terminal For More Details.")
                await ctx.channel.send(
                    embed=__exception_embed__
                )
    except Exception as exception:
        Bot_Management.log_error(__error__=exception)


client.run("token")
