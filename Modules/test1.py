import discord
import Utils

HELP = Utils.Help("Comment 2!")
EVENT = [Utils.EVENT.on_ready]


async def __main__(client: discord.Client, _event: int):

    print("READY!!!")
