import discord
import Utils
from NewClass import AttrDict
from json import load

HELP = Utils.Help("displays the credits")
EVENTS = [Utils.EVENT.on_message]


async def __main__(client: discord.Client, _event: int, message: discord.Message):

    configs = AttrDict(load(open("Configs.json")))
    author = configs.Author

    await message.channel.send(embed=discord.Embed(description=f"The Author is {author}\nModular Code: [here](https://github.com/AlbertUnruh/ModularDiscordPyBot)"))
