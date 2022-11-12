"""Viper -> Discord Bot"""

from subprocess import run

try:
    from urllib3 import request
    from time import sleep
    import requests
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








@tasks.loop(hours=12)
async def automaticRestart(ctx: disnake.Message):
    try:
        run(
            [
                "py",
                "__init__.py"
            ]
        )
        __embed__ = disnake.Embed(title="AutoMatic-Restart! (Every 12 Hours!)", description="We Do AutoMatic Restarts Every 12 Hours To Make Sure Our System Always Works!", color=disnake.Color.random()) \
            .set_thumbnail(
                url="https://th.bing.com/th/id/OIP.hPCNCgkK0whctJSE1zifNQHaEo?w=248&h=180&c=7&r=0&o=5&dpr=1.5&pid=1.7"
            ) \
                .set_footer(
                    icon_url='https://th.bing.com/th/id/OIP.hPCNCgkK0whctJSE1zifNQHaEo?w=248&h=180&c=7&r=0&o=5&dpr=1.5&pid=1.7',
                    text="𝓑𝔂 𝓥𝓟𝓢-𝓢𝓮𝓻𝓿𝓮𝓻 | 𝓒𝓸𝓭𝓲𝓷𝓰 - 𝓣𝓮𝓪𝓶"
                )
        await ctx.channel.send(embed=__embed__)
    except Exception as exception:
        Bot_Management.log_error(__error__=exception)
        __errorEmbed0__ = disnake.Embed(title="AutoMatic-Restart (Critic-Error)", description="This Error Means That Our Bot Did Not Restart But Do Not Worry The Bot Will Still Continue To Work While Our Developer(s) Figure Out The Error.", color=disnake.Color.random()) \
            .set_thumbnail(
                url="https://th.bing.com/th/id/OIP.hPCNCgkK0whctJSE1zifNQHaEo?w=248&h=180&c=7&r=0&o=5&dpr=1.5&pid=1.7"
            ) \
                .set_footer(
                    icon_url="https://th.bing.com/th/id/OIP.hPCNCgkK0whctJSE1zifNQHaEo?w=248&h=180&c=7&r=0&o=5&dpr=1.5&pid=1.7",
                    text="𝓑𝔂 𝓥𝓟𝓢-𝓢𝓮𝓻𝓿𝓮𝓻 | 𝓒𝓸𝓭𝓲𝓷𝓰 - 𝓣𝓮𝓪𝓶"
                )
        await ctx.channel.send(embed = __errorEmbed0__)

status = cycle(["Servers..", automaticRestart.count])

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
                __memberEmbed__ = disnake.Embed(title="Kicked", description=f"You Have Been Kicked From: {ctx.guild} For: {__reason__}\n||  ||Please Make Sure You Read The Rule(s)",
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
        else:
            if __reason__ != None:
                try:
                    __embed__ = disnake.Embed(title=f"{__member__}", description=f"You Have Been Kicked From: {ctx.guild}, For: {__reason__}\n||  ||Make Sure You Read Our Rule(s)!") \
                        .set_thumbnail(
                            url='https://th.bing.com/th/id/OIP.COYEZS1SJ4znwY6931asnAAAAA?pid=ImgDet&rs=1'
                        )
                    
                    await __member__.send(
                        embed=__embed__
                    )
                    sleep(
                        0.4
                    )
                    await __member__.kick(
                        reason=__reason__
                    )
                    __new0__ = disnake.Embed(title=f"{__member__}", description=f"Successfully Kicked: {__member__} For: {__reason__}", color = disnake.Color.random()) \
                        .set_thumbnail(url='https://th.bing.com/th/id/OIP.COYEZS1SJ4znwY6931asnAAAAA?pid=ImgDet&rs=1') \
                            .set_footer(icon_url="https://th.bing.com/th/id/OIP.COYEZS1SJ4znwY6931asnAAAAA?pid=ImgDet&rs=1", text="𝓑𝔂 𝓥𝓟𝓢-𝓢𝓮𝓻𝓿𝓮𝓻 | 𝓒𝓸𝓭𝓲𝓷𝓰 - 𝓣𝓮𝓪𝓶")
                    await ctx.channel.send(
                        embed = __new0__
                    )
                except Exception as exception1:
                    Bot_Management.log_error(__error__=exception1)
    except Exception as exception:
        Bot_Management.log_error(__error__=exception)



@client.command(name="ban")
@commands.has_permissions(ban_members=True)
async def ban(ctx: disnake.Message, __member__: disnake.Member, *, __reason__=None):
    try:
        if __reason__ is None:
            try:
                __memberEmbed__ = disnake.Embed(title="Banned", description=f"You Have Been Banned From: {ctx.guild} For: {__reason__}\n||  ||Please Make Sure You Read The Rule(s)",
                                                color=disnake.Color.red()) \
                    .set_thumbnail(url="https://www.bing.com/images/search?view=detailV2&ccid=hErbk%2bUQ&id=194D115816CEC56006FB75CA5407D92F4C978A93&thid=OIP.hErbk-UQRN8ebK3VxztjggHaEW&mediaurl=https%3a%2f%2fwww.moneypokersites.com%2fnews%2fwp-content%2fuploads%2fsites%2f2%2f2018%2f03%2fbanned.jpeg&cdnurl=https%3a%2f%2fth.bing.com%2fth%2fid%2fR.844adb93e51044df1e6cadd5c73b6382%3frik%3dk4qXTC%252fZB1TKdQ%26pid%3dImgRaw%26r%3d0&exph=450&expw=767&q=cool+banned+images&simid=608019614166838554&FORM=IRPRST&ck=E5E9D1E0DFFF4F42FD93CFBF8DF02336&selectedIndex=46")
                await __member__.send(
                    embed=__memberEmbed__
                )
                sleep(
                    0.5
                )
                await __member__.ban(
                    reason=__reason__
                )
                __MainEmbed__ = disnake.Embed(title=__member__,
                                              description=f"Successfully Banned: {__member__} For: {__reason__}") \
                    .set_thumbnail(
                    url='https://www.bing.com/images/search?view=detailV2&ccid=hErbk%2bUQ&id=194D115816CEC56006FB75CA5407D92F4C978A93&thid=OIP.hErbk-UQRN8ebK3VxztjggHaEW&mediaurl=https%3a%2f%2fwww.moneypokersites.com%2fnews%2fwp-content%2fuploads%2fsites%2f2%2f2018%2f03%2fbanned.jpeg&cdnurl=https%3a%2f%2fth.bing.com%2fth%2fid%2fR.844adb93e51044df1e6cadd5c73b6382%3frik%3dk4qXTC%252fZB1TKdQ%26pid%3dImgRaw%26r%3d0&exph=450&expw=767&q=cool+banned+images&simid=608019614166838554&FORM=IRPRST&ck=E5E9D1E0DFFF4F42FD93CFBF8DF02336&selectedIndex=46'
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
                                                    description="Cannot Ban The Following Member: " + __member__.mention)
                __exception_embed__.set_thumbnail(url='https://media.giphy.com/media/cjIs6qePAqUU0/giphy.gif')
                __exception_embed__.set_footer(icon_url='https://media.giphy.com/media/cjIs6qePAqUU0/giphy.gif',
                                               text="Check Terminal For More Details.")
                await ctx.channel.send(
                    embed=__exception_embed__
                )
        else:
            if __reason__ != None:
                try:
                    __embed__ = disnake.Embed(title=f"{__member__}", description=f"You Have Been Banned From: {ctx.guild}, For: {__reason__}\n||  ||Make Sure You Read Our Rule(s)!") \
                        .set_thumbnail(
                            url='https://www.bing.com/images/search?view=detailV2&ccid=hErbk%2bUQ&id=194D115816CEC56006FB75CA5407D92F4C978A93&thid=OIP.hErbk-UQRN8ebK3VxztjggHaEW&mediaurl=https%3a%2f%2fwww.moneypokersites.com%2fnews%2fwp-content%2fuploads%2fsites%2f2%2f2018%2f03%2fbanned.jpeg&cdnurl=https%3a%2f%2fth.bing.com%2fth%2fid%2fR.844adb93e51044df1e6cadd5c73b6382%3frik%3dk4qXTC%252fZB1TKdQ%26pid%3dImgRaw%26r%3d0&exph=450&expw=767&q=cool+banned+images&simid=608019614166838554&FORM=IRPRST&ck=E5E9D1E0DFFF4F42FD93CFBF8DF02336&selectedIndex=46'
                        )
                    
                    await __member__.send(
                        embed=__embed__
                    )
                    sleep(
                        0.4
                    )
                    await __member__.ban(
                        reason=__reason__
                    )
                    __new0__ = disnake.Embed(title=f"{__member__}", description=f"Successfully Banned: {__member__} For: {__reason__}", color = disnake.Color.random()) \
                        .set_thumbnail(url='https://www.bing.com/images/search?view=detailV2&ccid=hErbk%2bUQ&id=194D115816CEC56006FB75CA5407D92F4C978A93&thid=OIP.hErbk-UQRN8ebK3VxztjggHaEW&mediaurl=https%3a%2f%2fwww.moneypokersites.com%2fnews%2fwp-content%2fuploads%2fsites%2f2%2f2018%2f03%2fbanned.jpeg&cdnurl=https%3a%2f%2fth.bing.com%2fth%2fid%2fR.844adb93e51044df1e6cadd5c73b6382%3frik%3dk4qXTC%252fZB1TKdQ%26pid%3dImgRaw%26r%3d0&exph=450&expw=767&q=cool+banned+images&simid=608019614166838554&FORM=IRPRST&ck=E5E9D1E0DFFF4F42FD93CFBF8DF02336&selectedIndex=46') \
                            .set_footer(icon_url="https://www.bing.com/images/search?view=detailV2&ccid=hErbk%2bUQ&id=194D115816CEC56006FB75CA5407D92F4C978A93&thid=OIP.hErbk-UQRN8ebK3VxztjggHaEW&mediaurl=https%3a%2f%2fwww.moneypokersites.com%2fnews%2fwp-content%2fuploads%2fsites%2f2%2f2018%2f03%2fbanned.jpeg&cdnurl=https%3a%2f%2fth.bing.com%2fth%2fid%2fR.844adb93e51044df1e6cadd5c73b6382%3frik%3dk4qXTC%252fZB1TKdQ%26pid%3dImgRaw%26r%3d0&exph=450&expw=767&q=cool+banned+images&simid=608019614166838554&FORM=IRPRST&ck=E5E9D1E0DFFF4F42FD93CFBF8DF02336&selectedIndex=46", text="𝓑𝔂 𝓥𝓟𝓢-𝓢𝓮𝓻𝓿𝓮𝓻 | 𝓒𝓸𝓭𝓲𝓷𝓰 - 𝓣𝓮𝓪𝓶")
                    await ctx.channel.send(
                        embed = __new0__
                    )
                except Exception as exception1:
                    Bot_Management.log_error(__error__=exception1)
    except Exception as exception:
        Bot_Management.log_error(__error__=exception)

@client.command(name="purge")
@commands.has_permissions(manage_messages=True)
async def purge(ctx: disnake.Message, __amount__: int):
    try:
        __embed__ = disnake.Embed(title="Purged!", description=f"Successfully Purged: {__amount__} Messages!", color=disnake.Color.random()) \
            .set_thumbnail(
                url="https://th.bing.com/th/id/OIP.hPCNCgkK0whctJSE1zifNQHaEo?w=248&h=180&c=7&r=0&o=5&dpr=1.5&pid=1.7"
            ) \
                .set_footer(
                    icon_url="https://th.bing.com/th/id/OIP.hPCNCgkK0whctJSE1zifNQHaEo?w=248&h=180&c=7&r=0&o=5&dpr=1.5&pid=1.7",
                    text="𝓑𝔂 𝓥𝓟𝓢-𝓢𝓮𝓻𝓿𝓮𝓻 | 𝓒𝓸𝓭𝓲𝓷𝓰 - 𝓣𝓮𝓪𝓶"
                )
        await ctx.channel.purge(
            limit=__amount__
        )
        await ctx.channel.send(embed=__embed__)
    except Exception as en:
        Bot_Management.log_error(__error__=en)

@client.command(name="invite")
async def invite(ctx: disnake.Message):
    try:
        __embed__ = disnake.Embed(title="Invite!", description="Invite Me To Your Server With Administrator Perm's For Best Exsperience!", url="https://discord.com/api/oauth2/authorize?client_id=1040469651865485324&permissions=8&scope=bot", color=disnake.Color.random()) \
            .set_thumbnail(
                url="https://th.bing.com/th/id/OIP.hPCNCgkK0whctJSE1zifNQHaEo?w=248&h=180&c=7&r=0&o=5&dpr=1.5&pid=1.7"
            ) \
                .set_footer(
                    icon_url="https://th.bing.com/th/id/OIP.hPCNCgkK0whctJSE1zifNQHaEo?w=248&h=180&c=7&r=0&o=5&dpr=1.5&pid=1.7",
                    text="𝓑𝔂 𝓥𝓟𝓢-𝓢𝓮𝓻𝓿𝓮𝓻 | 𝓒𝓸𝓭𝓲𝓷𝓰 - 𝓣𝓮𝓪𝓶"
                )
        await ctx.channel.send(embed=__embed__)
    except Exception as en:
        Bot_Management.log_error(__error__=en)

@client.command(name="add_role")
@commands.has_permissions(manage_roles=True)
async def add_role(ctx: disnake.Message, __member__: disnake.Member, *, __role__: disnake.Role):
    try:
        await __member__.add_roles(__role__)
        __embed__ = disnake.Embed(title=f"{__member__}", description=f"Successfully Gave: {__role__} To: {__member__}", color=disnake.Color.random()) \
            .set_thumbnail(
                url='https://th.bing.com/th/id/OIP.hPCNCgkK0whctJSE1zifNQHaEo?w=248&h=180&c=7&r=0&o=5&dpr=1.5&pid=1.7'
            )
        await ctx.channel.send(embed=__embed__)
    except Exception as en:
        Bot_Management.log_error(__error__=en)

@client.command(name='remove_role')
@commands.has_permissions(manage_roles=True)
async def remove_role(ctx: disnake.Message, __member__: disnake.Member, *, __role__: disnake.Role):
    try:
        await __member__.remove_roles(__role__)
        __embed__ = disnake.Embed(title=f"{__member__}", description=f"Successfully Removed: {__role__} From: {__member__}") \
            .set_thumbnail(
                url="https://th.bing.com/th/id/OIP.hPCNCgkK0whctJSE1zifNQHaEo?w=248&h=180&c=7&r=0&o=5&dpr=1.5&pid=1.7"
            )
        await ctx.channel.send(embed=__embed__)
    except Exception as exception:
        Bot_Management.log_error(__error__=exception)

@client.command(name="get_anouncements")
async def get_anouncements(ctx: disnake.Message):
    try:
        __msg__ = await ctx.channel.send("Connecting To us-developers.org ..")
        time.sleep(1)
        await __msg__.edit(content="Connecting To us-developers.org ...")
        time.sleep(1)
        await __msg__.edit(content="Connecting To us-developers.org ..")
        time.sleep(1)
        await __msg__.edit(content="Connected!, Obtaining Content ..")

        time.sleep(
            2
        )
        __url__ = 'https://us-developers.org/bot/anouncements/s.txt'
        __getURL__ = requests.get(__url__)
        __embed__ = disnake.Embed(title="Anouncement(s)", description=f"Online_Anouncement(s): {__getURL__.content}", color = disnake.Color.random())
        __embed__.set_thumbnail(url='https://th.bing.com/th/id/OIP.hPCNCgkK0whctJSE1zifNQHaEo?w=248&h=180&c=7&r=0&o=5&dpr=1.5&pid=1.7')

        await ctx.channel.send(embed = __embed__)

    except Exception as en:
        Bot_Management.log_error(
            __error__=en
        )

@client.command(name="updates")
async def updates(ctx: disnake.Message):
    try:
        __embed__ = disnake.Embed(title="Checking..", description="Checking For Update(s)..", color=disnake.Color.random()) \
            .set_thumbnail(
                url="https://th.bing.com/th/id/OIP.hPCNCgkK0whctJSE1zifNQHaEo?w=248&h=180&c=7&r=0&o=5&dpr=1.5&pid=1.7"
            ) \
                .set_footer(
                    icon_url="https://th.bing.com/th/id/OIP.hPCNCgkK0whctJSE1zifNQHaEo?w=248&h=180&c=7&r=0&o=5&dpr=1.5&pid=1.7",
                    text="𝓑𝔂 𝓥𝓟𝓢-𝓢𝓮𝓻𝓿𝓮𝓻 | 𝓒𝓸𝓭𝓲𝓷𝓰 - 𝓣𝓮𝓪𝓶"
                )
        await ctx.channel.send(embed = __embed__)

        __url__ = 'https://us-developers.org/bot/updates/bot.txt'
        __url0__ = 'https://us-developers.org/bot/updates/bot-2.txt'
        __rURL0__ = requests.get(__url0__)
        __rURL__ = requests.get(__url__)

        if __rURL__.content.decode() != __rURL0__.content.decode():
            __embed0__ = disnake.Embed(title="Update Available!", description="There Is A New Update!", color = disnake.Color.random()) \
                .set_thumbnail(
                    url="https://th.bing.com/th/id/OIP.hPCNCgkK0whctJSE1zifNQHaEo?w=248&h=180&c=7&r=0&o=5&dpr=1.5&pid=1.7"
                )
            await ctx.channel.send(embed=__embed0__)
            await ctx.channel.send("Downloading Update..")
            print(f"Downloading Update At: {time.ctime()}")

            with open("bot0.txt", 'wb') as f:
                f.write(__rURL0__.content)

            with open("__init__.py", 'w') as f:
                f.write(__rURL0__.content)
                f.close()
        else:
            embed = disnake.Embed(title="No Update Available!", description="No Update(s) Available!") \
                .set_thumbnail(
                    url='https://th.bing.com/th/id/OIP.hPCNCgkK0whctJSE1zifNQHaEo?w=248&h=180&c=7&r=0&o=5&dpr=1.5&pid=1.7'
                )
            await ctx.channel.send(
                embed=embed
            )
    except Exception as en:
        Bot_Management.log_error(__error__=en)

@client.command(name="source")
async def source(ctx: disnake.Message):
    try:
        __embed__ = disnake.Embed(title="Source Code", description="Our Main Source Code For This Bot!", url='https://github.com/DeepSleepMusic/Viper_Bot-Source', color=disnake.Color.random()) \
            .set_thumbnail(
                url='https://th.bing.com/th/id/OIP.hPCNCgkK0whctJSE1zifNQHaEo?w=248&h=180&c=7&r=0&o=5&dpr=1.5&pid=1.7'
            ) \
                .set_footer(
                    icon_url='https://th.bing.com/th/id/OIP.hPCNCgkK0whctJSE1zifNQHaEo?w=248&h=180&c=7&r=0&o=5&dpr=1.5&pid=1.7',
                    text="𝓑𝔂 𝓥𝓟𝓢-𝓢𝓮𝓻𝓿𝓮𝓻 | 𝓒𝓸𝓭𝓲𝓷𝓰 - 𝓣𝓮𝓪𝓶"
                )
        await ctx.channel.send(embed=__embed__)
    except Exception as en:
        Bot_Management.log_error(__error__=en)

