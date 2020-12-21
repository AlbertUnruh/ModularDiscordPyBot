import discord
import Utils
from json import load

try:
    from NewClass import AttrDict
except ImportError:
    import AttrDict


HELP = Utils.Help("displays the credits")
Branch = Utils.Branch.on_message


async def __main__(client: discord.Client, message: discord.Message):

    configs = AttrDict(load(open("Configs.json")))
    author = configs.Author

    await message.channel.send(embed=discord.Embed(description=f"The Author is {author}\nModular Code: [here](https://github.com/AlbertUnruh/ModularDiscordBot)"))
