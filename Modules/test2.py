import discord
import Utils

HELP = Utils.Help("Comment 2!")


async def __main__(client: discord.Client, message: discord.Message):

    await message.channel.send("test2")
