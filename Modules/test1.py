import discord
import Utils


EVENT = [Utils.EVENT.on_ready]


async def __main__(client: discord.Client, _event: int):

    print("READY!!!")
