import discord
import Utils


EVENTS = [Utils.EVENT.on_ready]


async def __main__(client: discord.Client, _event: int):

    print("READY!!!")
