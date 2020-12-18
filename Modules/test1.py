import discord
import Utils

HELP = Utils.Help()


async def __main__(client: discord.Client, message: discord.Message):

    await message.channel.send(f"test1")
