from typing import *

try:
    from NewClass import AttrDict
except ImportError:
    import AttrDict


Branch = AttrDict({
    "on_connect":                       0,  # argument(s) --> client: discord.Client
    "on_shard_connect":                 1,  # argument(s) --> client: discord.Client, shard_id: int
    "on_disconnect":                    2,  # argument(s) --> client: discord.Client
    "on_shard_disconnect":              3,  # argument(s) --> client: discord.Client, shard_id: int
    "on_ready":                         4,  # argument(s) --> client: discord.Client
    "on_shard_ready":                   5,  # argument(s) --> client: discord.Client, shard_id: int
    "on_resumed":                       6,  # argument(s) --> client: discord.Client
    "on_shard_resumed":                 7,  # argument(s) --> client: discord.Client, shard_id: int
    "on_error":                         8,  # argument(s) --> client: discord.Client, event: str, *args, **kwargs
    "on_socket_raw_receive":            9,  # argument(s) --> client: discord.Client, msg: Union[bytes, str]
    "on_socket_raw_send":              11,  # argument(s) --> client: discord.Client, payload: Union[bytes, str]
    "on_typing":                       12,  # argument(s) --> client: discord.Client, channel: discord.abc.Messageable, user: Union[discord.User, discord.Member], when: datetime.datetime
    "on_message":                      13,  # argument(s) --> client: discord.Client, message: discord.Message
    "on_message_delete":               14,  # argument(s) --> client: discord.Client, message: discord.Message
    "on_bulk_message_delete":          15,  # argument(s) --> client: discord.Client, messages: List[discord.Message]
    "on_raw_message_delete":           16,  # argument(s) --> client: discord.Client, payload: discord.RawMessageDeleteEvent
    "on_message_edit":                 17,  # argument(s) --> client: discord.Client, before: discord.Message, after: discord.Message
    "on_raw_message_edit":             18,  # argument(s) --> client: discord.Client, payload: discord.RawMessageUpdateEvent
    "on_reaction_add":                 19,  # argument(s) --> client: discord.Client, reaction: discord.Reaction, user: Union[discord.Member, discord.User]
    "on_raw_reaction_add":             20,  # argument(s) --> client: discord.Client, payload: discord.RawReactionActionEvent
    "on_reaction_remove":              21,  # argument(s) --> client: discord.Client, reaction: discord.Reaction, user: Union[discord.Member, discord.User]
    "on_raw_reaction_remove":          22,  # argument(s) --> client: discord.Client, payload: discord.RawReactionActionEvent
    "on_reaction_clear":               23,  # argument(s) --> client: discord.Client, message: discord.Message, reactions: List[discord.Reaction]
    "on_raw_reaction_clear":           24,  # argument(s) --> client: discord.Client, payload: discord.RawReactionClearEvent
    "on_reaction_clear_emoji":         25,  # argument(s) --> client: discord.Client, reaction: discord.Reaction
    "on_raw_reaction_clear_emoji":     26,  # argument(s) --> client: discord.Client, payload: discord.RawReactionClearEmojiEvent
    "on_private_channel_delete":       27,  # argument(s) --> client: discord.Client, channel: discord.abc.PrivateChannel
    "on_private_channel_create":       28,  # argument(s) --> client: discord.Client, channel: discord.abc.PrivateChannel
    "on_private_channel_update":       29,  # argument(s) --> client: discord.Client, before: discord.GroupChannel, after: discord.GroupChannel
    "on_private_channel_pins_update":  30,  # argument(s) --> client: discord.Client, channel: discord.abc.PrivateChannel, last_pin: Optional[datetime.datetime]
    "on_guild_channel_delete":         31,  # argument(s) --> client: discord.Client, channel: discord.abc.GuildChannel
    "on_guild_channel_create":         32,  # argument(s) --> client: discord.Client, channel: discord.abc.GuildChannel
    "on_guild_channel_update":         33,  # argument(s) --> client: discord.Client, before: discord.GroupChannel, after: discord.GroupChannel
    "on_guild_channel_pins_update":    34,  # argument(s) --> client: discord.Client, channel: discord.abc.PrivateChannel, last_pin: Optional[datetime.datetime]
    "on_guild_integrations_update":    35,  # argument(s) --> client: discord.Client, guild: discord.Guild
    "on_webhooks_update":              36,  # argument(s) --> client: discord.Client, channel: discord.abc.GuildChannel
    "on_member_join":                  37,  # argument(s) --> client: discord.Client, member: discord.Member
    "on_member_remove":                38,  # argument(s) --> client: discord.Client, member: discord.Member
    "on_member_update":                39,  # argument(s) --> client: discord.Client, before: discord.Member, after: discord.Member
    "on_user_update":                  40,  # argument(s) --> client: discord.Client, before: discord.User, after: discord.User
    "on_guild_join":                   41,  # argument(s) --> client: discord.Client, guild: discord.Guild
    "on_guild_remove":                 42,  # argument(s) --> client: discord.Client, guild: discord.Guild
    "on_guild_update":                 43,  # argument(s) --> client: discord.Client, before: discord.Guild, after: discord.Guild
    "on_guild_role_create":            44,  # argument(s) --> client: discord.Client, role: discord.Role
    "on_guild_role_delete":            45,  # argument(s) --> client: discord.Client, role: discord.Role
    "on_guild_role_update":            46,  # argument(s) --> client: discord.Client, before: discord.Role, after: discord.Role
    "on_guild_emojis_update":          47,  # argument(s) --> client: discord.Client, guild: discord.Guild, before: Sequence[discord.Emoji], after: Sequence[discord.Emoji]
    "on_guild_available":              48,  # argument(s) --> client: discord.Client, guild: discord.Guild
    "on_guild_unavailable":            49,  # argument(s) --> client: discord.Client, guild: discord.Guild
    "on_voice_state_update":           50,  # argument(s) --> client: discord.Client, member: discord.Member, before: discord.VoiceState, after: discord.VoiceState
    "on_member_ban":                   51,  # argument(s) --> client: discord.Client, guild: discord.Guild, user: Union[discord.User, discord.Member]
    "on_member_unban":                 52,  # argument(s) --> client: discord.Client, guild: discord.Guild, user: discord.User
    "on_invite_create":                53,  # argument(s) --> client: discord.Client, invite: discord.Invite
    "on_invite_delete":                54,  # argument(s) --> client: discord.Client, invite: discord.Invite
    "on_group_join":                   55,  # argument(s) --> client: discord.Client, channel: discord.GroupChannel, user: discord.User
    "on_group_remove":                 56,  # argument(s) --> client: discord.Client, channel: discord.GroupChannel, user: discord.User
    "on_relationship_add":             57,  # argument(s) --> client: discord.Client, relationship: discord.Relationship
    "on_relationship_remove":          58,  # argument(s) --> client: discord.Client, relationship: discord.Relationship
    "on_relationship_update":          59,  # argument(s) --> client: discord.Client, before: discord.Relationship, after: discord.Relationship
})


class Help(object):
    def __init__(self, _help: Optional[str] = None):
        self.help = _help

    def __str__(self):
        return self.help if self.supports() else "There is no help set!"

    def supports(self):
        return False if self.help is None else True
