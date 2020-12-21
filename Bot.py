from json import load

import discord
import Modules
import Utils

try:
    from NewClass import AttrDict
except ImportError:
    import AttrDict

__version__ = "0.1.0"


client = discord.Client()
CONFIGS = AttrDict(load(open("Configs.json")))
TOKEN = CONFIGS.CONSTANTS.Token
Prefix = CONFIGS.CONSTANTS.Prefix


@client.event
async def on_ready():
    print(client.user.name)

    for module in Modules.Modules:
        if Modules.libs[module].Branch == Utils.Branch.on_ready:

            await Modules.libs[module].__main__(client=client)


@client.event
async def on_message(message: discord.Message):

    if message.content.startswith(Prefix):
        if message.content.split(" ")[0] == f"{Prefix}help":

            embed = discord.Embed()
            embed.title = "**__help__**"
            embed.set_footer(text=f"requested by {message.author}", icon_url=message.author.avatar_url)

            for module in Modules.Modules:
                if Modules.libs[module].Branch == Utils.Branch.on_message:
                    embed.add_field(name=f"_{Prefix}{module}_", value=f"{Modules.libs[module].HELP}\n\n")

            await message.channel.send(embed=embed)

        else:
            for module in Modules.Modules:
                if Modules.libs[module].Branch == Utils.Branch.on_message:
                    if message.content.split(" ")[0] == f"{Prefix}{module}":

                        await Modules.libs[module].__main__(client=client, message=message)

    elif message.content.replace("!", "") == client.user.mention:
        await message.channel.send(f"My Prefix is `{Prefix}`.")


client.run(TOKEN)
