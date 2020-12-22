from json import load
from typing import *

import datetime
import discord
import Modules
import Utils

try:
    from NewClass import AttrDict
except ImportError:
    import AttrDict

__version__ = "0.1.4"


client = discord.Client()
CONFIGS = AttrDict(load(open("Configs.json")))
TOKEN = CONFIGS.CONSTANTS.Token
Prefix = CONFIGS.CONSTANTS.Prefix


'''
You can see all the events in the following URL:
https://discordpy.readthedocs.io/en/latest/api.html#event-reference
'''


@client.event
async def on_connect():

    for module in Modules.Modules:
        if Modules.libs[module].Branch == Utils.Branch.on_connect:

            await Modules.libs[module].__main__(client)


@client.event
async def on_shard_connect(shard_id: int):

    for module in Modules.Modules:
        if Modules.libs[module].Branch == Utils.Branch.on_shard_connect:

            await Modules.libs[module].__main__(client, shard_id)


@client.event
async def on_disconnect():

    for module in Modules.Modules:
        if Modules.libs[module].Branch == Utils.Branch.on_disconnect:

            await Modules.libs[module].__main__(client)


@client.event
async def on_shard_disconnect(shard_id: int):

    for module in Modules.Modules:
        if Modules.libs[module].Branch == Utils.Branch.on_shard_disconnect:

            await Modules.libs[module].__main__(client, shard_id)


@client.event
async def on_ready():

    for module in Modules.Modules:
        if Modules.libs[module].Branch == Utils.Branch.on_ready:

            await Modules.libs[module].__main__(client)


@client.event
async def on_shard_ready(shard_id: int):

    for module in Modules.Modules:
        if Modules.libs[module].Branch == Utils.Branch.on_shard_ready:

            await Modules.libs[module].__main__(client, shard_id)


@client.event
async def on_resumed():

    for module in Modules.Modules:
        if Modules.libs[module].Branch == Utils.Branch.on_resumed:

            await Modules.libs[module].__main__(client)


@client.event
async def on_shard_resumed(shard_id: int):

    for module in Modules.Modules:
        if Modules.libs[module].Branch == Utils.Branch.on_shard_resumed:

            await Modules.libs[module].__main__(client, shard_id)


@client.event
async def on_error(event: str, *args, **kwargs):

    for module in Modules.Modules:
        if Modules.libs[module].Branch == Utils.Branch.on_error:

            await Modules.libs[module].__main__(client, event, *args, **kwargs)


@client.event
async def on_socket_raw_receive(msg: Union[bytes, str]):

    for module in Modules.Modules:
        if Modules.libs[module].Branch == Utils.Branch.on_socket_raw_receive:

            await Modules.libs[module].__main__(client, msg)


@client.event
async def on_socket_raw_send(payload: Union[bytes, str]):

    for module in Modules.Modules:
        if Modules.libs[module].Branch == Utils.Branch.on_socket_raw_send:

            await Modules.libs[module].__main__(client, payload)


@client.event
async def on_typing(channel: discord.abc.Messageable, user: Union[discord.User, discord.Member], when: datetime.datetime):

    for module in Modules.Modules:
        if Modules.libs[module].Branch == Utils.Branch.on_typing:

            await Modules.libs[module].__main__(client, channel, user, when)


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

                        await Modules.libs[module].__main__(client, message)

    elif message.content.replace("!", "") == client.user.mention:
        await message.channel.send(f"My Prefix is `{Prefix}`.")


@client.event
async def on_message_delete(message: discord.Message):

    for module in Modules.Modules:
        if Modules.libs[module].Branch == Utils.Branch.on_message_delete:

            await Modules.libs[module].__main__(client, message)


@client.event
async def on_bulk_message_delete(messages: List[discord.Message]):

    for module in Modules.Modules:
        if Modules.libs[module].Branch == Utils.Branch.on_bulk_message_delete:

            await Modules.libs[module].__main__(client, messages)


@client.event
async def on_raw_message_delete(payload: discord.RawMessageDeleteEvent):

    for module in Modules.Modules:
        if Modules.libs[module].Branch == Utils.Branch.on_raw_message_delete:

            await Modules.libs[module].__main__(client, payload)


@client.event
async def on_message_edit(before: discord.Message, after: discord.Message):

    for module in Modules.Modules:
        if Modules.libs[module].Branch == Utils.Branch.on_message_edit:

            await Modules.libs[module].__main__(client, before, after)


@client.event
async def on_raw_message_edit(payload: discord.RawMessageUpdateEvent):

    for module in Modules.Modules:
        if Modules.libs[module].Branch == Utils.Branch.on_raw_message_edit:

            await Modules.libs[module].__main__(client, payload)


@client.event
async def on_reaction_add(reaction: discord.Reaction, user: Union[discord.Member, discord.User]):

    for module in Modules.Modules:
        if Modules.libs[module].Branch == Utils.Branch.on_reaction_add:

            await Modules.libs[module].__main__(client, reaction, user)


@client.event
async def on_raw_reaction_add(payload: discord.RawReactionActionEvent):

    for module in Modules.Modules:
        if Modules.libs[module].Branch == Utils.Branch.on_raw_reaction_add:

            await Modules.libs[module].__main__(client, payload)


@client.event
async def on_reaction_remove(reaction: discord.Reaction, user: Union[discord.Member, discord.User]):

    for module in Modules.Modules:
        if Modules.libs[module].Branch == Utils.Branch.on_reaction_remove:

            await Modules.libs[module].__main__(client, reaction, user)


@client.event
async def on_raw_reaction_remove(payload: discord.RawReactionActionEvent):

    for module in Modules.Modules:
        if Modules.libs[module].Branch == Utils.Branch.on_raw_reaction_remove:

            await Modules.libs[module].__main__(client, payload)


@client.event
async def on_reaction_clear(message: discord.Message, reactions: List[discord.Reaction]):

    for module in Modules.Modules:
        if Modules.libs[module].Branch == Utils.Branch.on_reaction_clear:

            await Modules.libs[module].__main__(client, message, reactions)


@client.event
async def on_raw_reaction_clear(payload: discord.RawReactionClearEvent):

    for module in Modules.Modules:
        if Modules.libs[module].Branch == Utils.Branch.on_raw_reaction_clear:

            await Modules.libs[module].__main__(client, payload)


@client.event
async def on_reaction_clear_emoji(reaction: discord.Reaction):

    for module in Modules.Modules:
        if Modules.libs[module].Branch == Utils.Branch.on_reaction_clear_emoji:

            await Modules.libs[module].__main__(client, reaction)


@client.event
async def on_raw_reaction_clear_emoji(payload: discord.RawReactionClearEmojiEvent):

    for module in Modules.Modules:
        if Modules.libs[module].Branch == Utils.Branch.on_raw_reaction_clear_emoji:

            await Modules.libs[module].__main__(client, payload)


@client.event
async def on_private_channel_delete(channel: discord.abc.PrivateChannel):

    for module in Modules.Modules:
        if Modules.libs[module].Branch == Utils.Branch.on_private_channel_delete:

            await Modules.libs[module].__main__(client, channel)


@client.event
async def on_private_channel_create(channel: discord.abc.PrivateChannel):

    for module in Modules.Modules:
        if Modules.libs[module].Branch == Utils.Branch.on_private_channel_create:

            await Modules.libs[module].__main__(client, channel)


@client.event
async def on_private_channel_update(before: discord.GroupChannel, after: discord.GroupChannel):

    for module in Modules.Modules:
        if Modules.libs[module].Branch == Utils.Branch.on_private_channel_update:

            await Modules.libs[module].__main__(client, before, after)


@client.event
async def on_private_channel_pins_update(channel: discord.abc.PrivateChannel, last_pin: Optional[datetime.datetime]):

    for module in Modules.Modules:
        if Modules.libs[module].Branch == Utils.Branch.on_private_channel_pins_update:

            await Modules.libs[module].__main__(client, channel, last_pin)


@client.event
async def on_guild_channel_delete(channel: discord.abc.GuildChannel):

    for module in Modules.Modules:
        if Modules.libs[module].Branch == Utils.Branch.on_guild_channel_delete:

            await Modules.libs[module].__main__(client, channel)


@client.event
async def on_guild_channel_create(channel: discord.abc.GuildChannel):

    for module in Modules.Modules:
        if Modules.libs[module].Branch == Utils.Branch.on_guild_channel_create:

            await Modules.libs[module].__main__(client, channel)


@client.event
async def on_guild_channel_update(before: discord.GroupChannel, after: discord.GroupChannel):

    for module in Modules.Modules:
        if Modules.libs[module].Branch == Utils.Branch.on_guild_channel_update:

            await Modules.libs[module].__main__(client, before, after)


@client.event
async def on_guild_channel_pins_update(channel: discord.abc.PrivateChannel, last_pin: Optional[datetime.datetime]):

    for module in Modules.Modules:
        if Modules.libs[module].Branch == Utils.Branch.on_guild_channel_pins_update:

            await Modules.libs[module].__main__(client, channel, last_pin)


@client.event
async def on_guild_integrations_update(guild: discord.Guild):

    for module in Modules.Modules:
        if Modules.libs[module].Branch == Utils.Branch.on_guild_integrations_update:

            await Modules.libs[module].__main__(client, guild)


@client.event
async def on_webhooks_update(channel: discord.abc.GuildChannel):

    for module in Modules.Modules:
        if Modules.libs[module].Branch == Utils.Branch.on_webhooks_update:

            await Modules.libs[module].__main__(client, channel)


@client.event
async def on_member_join(member: discord.Member):

    for module in Modules.Modules:
        if Modules.libs[module].Branch == Utils.Branch.on_member_join:

            await Modules.libs[module].__main__(client, member)


@client.event
async def on_member_remove(member: discord.Member):

    for module in Modules.Modules:
        if Modules.libs[module].Branch == Utils.Branch.on_member_remove:

            await Modules.libs[module].__main__(client, member)


@client.event
async def on_member_update(before: discord.Member, after: discord.Member):

    for module in Modules.Modules:
        if Modules.libs[module].Branch == Utils.Branch.on_member_update:

            await Modules.libs[module].__main__(client, before, after)


@client.event
async def on_user_update(before: discord.User, after: discord.User):

    for module in Modules.Modules:
        if Modules.libs[module].Branch == Utils.Branch.on_user_update:

            await Modules.libs[module].__main__(client, before, after)


@client.event
async def on_guild_join(guild: discord.Guild):

    for module in Modules.Modules:
        if Modules.libs[module].Branch == Utils.Branch.on_guild_join:

            await Modules.libs[module].__main__(client, guild)


@client.event
async def on_guild_remove(guild: discord.Guild):

    for module in Modules.Modules:
        if Modules.libs[module].Branch == Utils.Branch.on_guild_remove:

            await Modules.libs[module].__main__(client, guild)


@client.event
async def on_guild_update(before: discord.Guild, after: discord.Guild):

    for module in Modules.Modules:
        if Modules.libs[module].Branch == Utils.Branch.on_guild_update:

            await Modules.libs[module].__main__(client, before, after)


@client.event
async def on_guild_role_create(role: discord.Role):

    for module in Modules.Modules:
        if Modules.libs[module].Branch == Utils.Branch.on_guild_role_create:

            await Modules.libs[module].__main__(client, role)


@client.event
async def on_guild_role_delete(role: discord.Role):

    for module in Modules.Modules:
        if Modules.libs[module].Branch == Utils.Branch.on_guild_role_delete:

            await Modules.libs[module].__main__(client, role)


@client.event
async def on_guild_role_update(before: discord.Role, after: discord.Role):

    for module in Modules.Modules:
        if Modules.libs[module].Branch == Utils.Branch.on_guild_role_update:

            await Modules.libs[module].__main__(client, before, after)


@client.event
async def on_guild_emojis_update(guild: discord.Guild, before: Sequence[discord.Emoji], after: Sequence[discord.Emoji]):

    for module in Modules.Modules:
        if Modules.libs[module].Branch == Utils.Branch.on_guild_emojis_update:

            await Modules.libs[module].__main__(client, guild, before, after)


@client.event
async def on_guild_available(guild: discord.Guild):

    for module in Modules.Modules:
        if Modules.libs[module].Branch == Utils.Branch.on_guild_available:

            await Modules.libs[module].__main__(client, guild)


@client.event
async def on_guild_unavailable(guild: discord.Guild):

    for module in Modules.Modules:
        if Modules.libs[module].Branch == Utils.Branch.on_guild_unavailable:

            await Modules.libs[module].__main__(client, guild)


@client.event
async def on_voice_state_update(member: discord.Member, before: discord.VoiceState, after: discord.VoiceState):

    for module in Modules.Modules:
        if Modules.libs[module].Branch == Utils.Branch.on_voice_state_update:

            await Modules.libs[module].__main__(client, member, before, after)


@client.event
async def on_member_ban(guild: discord.Guild, user: Union[discord.User, discord.Member]):

    for module in Modules.Modules:
        if Modules.libs[module].Branch == Utils.Branch.on_member_ban:

            await Modules.libs[module].__main__(client, guild, user)


@client.event
async def on_member_unban(guild: discord.Guild, user: discord.User):

    for module in Modules.Modules:
        if Modules.libs[module].Branch == Utils.Branch.on_member_unban:

            await Modules.libs[module].__main__(client, guild, user)


@client.event
async def on_invite_create(invite: discord.Invite):

    for module in Modules.Modules:
        if Modules.libs[module].Branch == Utils.Branch.on_invite_create:

            await Modules.libs[module].__main__(client, invite)


@client.event
async def on_invite_delete(invite: discord.Invite):

    for module in Modules.Modules:
        if Modules.libs[module].Branch == Utils.Branch.on_invite_delete:

            await Modules.libs[module].__main__(client, invite)


@client.event
async def on_group_join(channel: discord.GroupChannel, user: discord.User):

    for module in Modules.Modules:
        if Modules.libs[module].Branch == Utils.Branch.on_group_join:

            await Modules.libs[module].__main__(client, channel, user)


@client.event
async def on_group_remove(channel: discord.GroupChannel, user: discord.User):

    for module in Modules.Modules:
        if Modules.libs[module].Branch == Utils.Branch.on_group_remove:

            await Modules.libs[module].__main__(client, channel, user)


@client.event
async def on_relationship_add(relationship: discord.Relationship):

    for module in Modules.Modules:
        if Modules.libs[module].Branch == Utils.Branch.on_relationship_add:

            await Modules.libs[module].__main__(client, relationship)


@client.event
async def on_relationship_remove(relationship: discord.Relationship):

    for module in Modules.Modules:
        if Modules.libs[module].Branch == Utils.Branch.on_relationship_remove:

            await Modules.libs[module].__main__(client, relationship)


@client.event
async def on_relationship_update(before: discord.Relationship, after: discord.Relationship):

    for module in Modules.Modules:
        if Modules.libs[module].Branch == Utils.Branch.on_relationship_update:

            await Modules.libs[module].__main__(client, before, after)


client.run(TOKEN)
