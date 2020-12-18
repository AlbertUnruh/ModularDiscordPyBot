from json import load

import discord
import Modules

try:
    from NewClass import AttrDict
except ImportError:
    import AttrDict


client = discord.Client()
CONFIGS = AttrDict(load(open("Configs.json")))
TOKEN = CONFIGS.CONSTANTS.Token
Prefix = CONFIGS.CONSTANTS.Prefix


@client.event
async def on_ready():
    print(client.user.name)


@client.event
async def on_message(message: discord.Message):
    if message.content.startswith(Prefix):
        if message.content.split(" ")[0] == f"{Prefix}help":
            help_message = "**__Help__**\n\n"

            for module in Modules.Modules:
                help_message += f"_{Prefix}{module}_\n"
                help_message += f"{Modules.libs[module].HELP}\n\n"

            await message.channel.send(help_message)

        else:
            for module in Modules.Modules:
                if message.content.split(" ")[0] == f"{Prefix}{module}":

                    await Modules.libs[module].__main__(client=client, message=message)

    elif message.content.replace("!", "") == client.user.mention:
        await message.channel.send(f"My Prefix is `{Prefix}`.")


client.run(TOKEN)
