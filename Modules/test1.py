import discord
import Utils

HELP = Utils.Help()
Branch = Utils.Branch.on_ready


async def __main__(client: discord.Client):

    print(f"{client.user} is online!")
