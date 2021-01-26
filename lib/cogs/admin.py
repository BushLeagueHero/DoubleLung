import discord
import json
import logging
import re

from discord import Member
from discord.ext.commands import Cog
from discord.ext.commands import command
from discord import Intents, Embed, File

from enum import Enum

logger = logging.getLogger(f"doublelung.{__name__}")
class AdminError(Enum):
    NoError = 0
    ChannelPerms = 1
    UserPerms = 2
    InvalidSyntax = 3

# errors that can occur while processing administrative commands
error_dict = {
    AdminError.ChannelPerms: "Administration commands cannot be used in this channel",
    AdminError.UserPerms: "You do not have the permissions to set policies",
    AdminError.InvalidSyntax: "Invalid command syntax"
}

# look up table for allowed argument values (positional arguments)
allowed_argument_values = {
    "policy-name": ["channel","role","user"],
    "policy-value": ["enable", "disable"],
    "permission-name": {
        "channel": ["listen","respond","admin"],
        "role": ["commands","admin"],
        "user": ["commands","admin"]
    },
    "permission-value": ["allow","deny"]
}

class Admin(Cog):
    def __init__(self,bot):
        self.bot = bot
        self.Error = Enum('Error', 'channelperms userperms')

    async def __send_response(self,channel,data):
        await channel.send(data)

    async def __send_error_response(self,ctx,channel,error,extended_msg=""):
        guild = ctx.message.guild
        member = ctx.message.author
        errmsg = error_dict[error]

        response = Embed(title="Administrator command error",color=0xFF0000)
        response.add_field(name=f"command: {ctx.command}",value=f"An error occurred while processing the command {ctx.command}\n{errmsg}",inline=False)
        if extended_msg != "":
            response.add_field(name="additional info",value=extended_msg,inline=False)

        response.add_field(name=f"Extended information",value=f"Guild: {guild.name} ({guild.id})\nChannel: {channel.name} ({channel.id})\nUser: {member.name} ({member.id})",inline=False)

        await channel.send(embed=response)

    @command(name="config-channel")
    async def configure_channel(self,ctx,*,channel_data):
        await self.__configure_object(ctx,channel_data,"channel")

    @command(name="set-policy")
    async def set_policy(self,ctx,*,policy_data):
        await self.__set_policy(ctx,policy_data)

    @command(name="clear-policies")
    async def clear_all_policies(self,ctx):
        await self.__clear_config_elements(ctx,"channel",False)
        await self.__clear_config_elements(ctx,"role",False)
        await self.__clear_config_elements(ctx,"user",False)

        await self.__send_response(ctx.message.channel,f"All custom policies have been cleared. Check permissions and reconfigure if necessary.")

    @command(name="remove-policy")
    async def clear_policy(self,ctx,*,policy_data):
        await self.__remove_policy_object(ctx,policy_data)

    @command(name="enable-channel")
    async def enable_channel(self,ctx,*,channel_data):
        guild = ctx.message.guild
        msg_channel = ctx.message.channel

        # #enable-channel #general
        args = require_arguments(channel_data,1," ")
        set_policy_string = f"channel {args[0]} enable"
        target_channel = string_to_object(args[0],guild,"channel")

        logger.debug(f"setting policy using string : {set_policy_string}")

        error = await self.__set_policy(ctx,set_policy_string,False)
        if error != AdminError.NoError:
            await self.__send_error_response(ctx,msg_channel,error)
        else:
            await self.__send_response(msg_channel, f"Channel {target_channel.name} was enabled")
            await self.__send_response(target_channel,f"Commands will now be accepted in this channel")

    @command(name="disable-channel")
    async def disable_channel(self,ctx,*,channel_data):
        guild = ctx.message.guild
        msg_channel = ctx.message.channel

        # #enable-channel #general
        args = require_arguments(channel_data,1," ")
        set_policy_string = f"channel {args[0]} disable"
        target_channel = string_to_object(args[0],guild,"channel")

        error = await self.__set_policy(ctx,set_policy_string,False)
        if error != AdminError.NoError:
            await self.__send_error_response(ctx,msg_channel,error)
        else:
            await self.__send_response(msg_channel, f"Channel {target_channel.name} was disabled")
            await self.__send_response(target_channel, "Commands will no longer be accepted in this channel")

    @command(name="set-channel-default")
    async def set_channel_default(self,ctx,*,channel_setting):
        await self.__set_default_policy(ctx,f"channel {channel_setting}")

    @command(name="set-role-default")
    async def set_role_default(self,ctx,*,role_setting):
        await self.__set_default_policy(ctx,f"role {role_setting}")

    @command(name="set-user-default")
    async def set_user_default(self,ctx,*,user_setting):
        await self.__set_default_policy(ctx,f"user {user_setting}")

    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("admin")

    async def __set_default_policy(self,ctx,policy_data,send_response=True):
        guild = ctx.message.guild
        msg_channel = ctx.message.channel
        member = ctx.message.author

        error = self.__check_command_permission(guild,msg_channel,member) 
        if error != AdminError.NoError:
            if send_response:
                await self.__send_error_response(ctx,msg_channel,error)
            return error

        args = require_arguments(policy_data,2," ")
        policy_name = args[0]
        policy_value = args[1]

        allowed_policy_names = allowed_argument_values["policy-name"]
        if policy_name not in allowed_policy_names:
            logger.debug(f"The policy name {policy_name} does not exist. Valid policies are {allowed_policy_names}")
            if send_response:
                await self.__send_error_response(ctx,msg_channel,AdminError.InvalidSyntax,extended_msg=f"The policy name {policy_name} does not exist. Valid policies are {allowed_policy_names}")
            return AdminError.InvalidSyntax

        allowed_policy_values = allowed_argument_values["policy-value"]
        if policy_value not in allowed_policy_values:
            logger.debug(f"The policy value {policy_value} does not exist. Valid policies are {allowed_policy_values}")
            if send_response:
                await self.__send_error_response(ctx,msg_channel,AdminError.InvalidSyntax,extended_msg=f"The policy name {policy_value} does not exist. Valid policies are {allowed_policy_values}")
            return AdminError.InvalidSyntax

        allow = ("deny","allow")[policy_value == "enable"]
        self.bot.guild_configuration.set_default_permission(guild.id,policy_name,allow)

        await self.__send_response(msg_channel,f"{policy_name}s are now {policy_value}d by default")

    async def __set_policy(self, ctx, policy_data,send_response=True):
        guild = ctx.message.guild
        msg_channel = ctx.message.channel
        member = ctx.message.author

        # can we run admin commands?
        error = self.__check_command_permission(guild,msg_channel,member) 
        if error != AdminError.NoError:
            if send_response:
                await self.__send_error_response(ctx,msg_channel,error)
            return error
        
        args = require_arguments(policy_data,3," ")

        policy_name = args[0]           # the name of the policy to set (channel or role, user later)
        policy_target = args[1]         # the target of the policy (either a channel or role ID)
        policy_value = args[2]          # the new value of the policy (enable or disable)

        if policy_name not in allowed_argument_values["policy-name"]:
            allowed_vals = allowed_argument_values["policy-name"]
            if send_response == True:
                logger.debug(f"The policy name {policy_name} does not exist. Valid values are {allowed_vals}")
                await self.__send_error_response(ctx,msg_channel,AdminError.InvalidSyntax,extended_msg=f"The policy name {policy_name} does not exist. Valid values are {allowed_vals}")
            return AdminError.InvalidSyntax

        if policy_value not in allowed_argument_values["policy-value"]:
            allowed_vals = allowed_argument_values["policy-value"]
            if send_response == True:
                logger.debug(f"The policy value {policy_value} does not exist. Valid values are {allowed_vals}")
                await self.__send_error_response(ctx,msg_channel,AdminError.InvalidSyntax,extended_msg=f"The policy value {policy_value} does not exist. Valid values are {allowed_vals}")
            return AdminError.InvalidSyntax

        value = ("deny", "allow")[policy_value == "enable"]
        target_object = string_to_object(policy_target, guild, policy_name)

        if policy_name == "channel":
            listen_string = f"{policy_target} listen {value}"
            respond_string = f"{policy_target} respond {value}"

            error = await self.__configure_object(ctx,listen_string,policy_name,False) 
            if error != AdminError.NoError:
                logger.error(f"encountered error setting policy: {error}")
                if send_response:
                    await self.__send_error_response(ctx,msg_channel,error)
                return error

            error = await self.__configure_object(ctx,respond_string,policy_name,False)
            if error != AdminError.NoError:
                if send_response:
                    await self.__send_error_response(ctx,msg_channel,error)
                return error
        else:
            command_string = f"{policy_target} commands {value}"
            error = await self.__configure_object(ctx,command_string,policy_name,False)
            if error != AdminError.NoError:
                logger.error(f"encoutered error setting policy: {error}")
                if send_response:
                    await self.__send_error_response(ctx,msg_channel,error)
                return error

        if send_response:
            await self.__send_response(msg_channel, f"{policy_name} {target_object.name} was {policy_value}d")

        return AdminError.NoError

    async def __remove_policy_object(self,ctx,policy_data,send_response=True):
        guild = ctx.message.guild
        msg_channel = ctx.message.channel
        member = ctx.message.author

        error = self.__check_command_permission(guild,msg_channel,member)
        if error != AdminError.NoError:
            if send_response == True:
                await self.__send_error_response(ctx,msg_channel,error)
            return error

        # two arguments expected: the type of policy and the channel name
        args = require_arguments(policy_data,2," ")

        config_type = args[0]
        object_id = args[1]

        if config_type not in allowed_argument_values["policy-name"]:
            if send_response == True:
                await self.__send_error_response(ctx,msg_channel,AdminError.InvalidSyntax)
            return AdminError.InvalidSyntax

        target_object = string_to_object(object_id, guild, config_type)
        if target_object is not None:
            self.bot.guild_configuration.remove_policy_object(guild.id,target_object.id,config_type)
            if send_response:
                response = f"Removed policy for {config_type} {target_object.name} ({target_object.id})"
                await self.__send_response(msg_channel, response)

        return AdminError.NoError
            
    async def __clear_config_elements(self,ctx,policy_type,send_response=True):
        guild = ctx.message.guild
        msg_channel = ctx.message.channel
        member = ctx.message.author

        error = self.__check_command_permission(guild,msg_channel,member)
        if error != AdminError.NoError:
            if send_response == True:
                await self.__send_error_response(ctx,msg_channel,error)
            return error

        # two arguments expected: the type of policy and the channel name
        args = require_arguments(policy_type,1," ")
        config_type = args[0]

        if config_type not in allowed_argument_values["policy-name"]:
            if send_response == True:
                await self.__send_error_response(ctx,msg_channel,AdminError.InvalidSyntax)
            return AdminError.InvalidSyntax

        self.bot.guild_configuration.remove_all_policies_of_type(guild.id,config_type)
        if send_response:
            response = f"Removed all {config_type} policies for guild {guild.name} ({guild.id}))"
            await self.__send_response(msg_channel, response)

        return AdminError.NoError

    async def __configure_object(self,ctx,object_data,object_type,send_response=True):
        guild = ctx.message.guild
        msg_channel = ctx.message.channel
        member = ctx.message.author

        # can we run admin commands?
        error = self.__check_command_permission(guild,msg_channel,member) 
        if error != AdminError.NoError:
            if send_response == True:
                await self.__send_error_response(ctx,msg_channel,error)
            return error

        # this command expects three arguments
        args = require_arguments(object_data,3," ")

        if object_type not in allowed_argument_values["policy-name"]:
            if send_response == True:
                await self.__send_error_response(ctx,msg_channel,AdminError.InvalidSyntax)
            return AdminError.InvalidSyntax

        set_object = string_to_object(args[0],guild,object_type) # (channel | role | user)
        permission = args[1]
        policy = args[2]

        if permission not in allowed_argument_values["permission-name"][object_type]:
            if send_response:
                await self.__send_error_response(ctx,msg_channel,AdminError.InvalidSyntax)
            return AdminError.InvalidSyntax
        
        if policy not in allowed_argument_values["permission-value"]:
            if send_response:
                await self.__send_error_response(ctx,msg_channel,AdminError.InvalidSyntax)
            return AdminError.InvalidSyntax

        gf = self.bot.guild_configuration
        set_method = ((gf.set_user_policy, gf.set_role_policy)[object_type == "role"],gf.set_channel_policy)[object_type == "channel"]

        logger.debug(f"configuring {object_type} {set_object.name} ({set_object.id})")
        set_method(guild.id,set_object.id,permission,policy)
        logger.debug(f"admin configured guild {guild.name} ({guild.id}) to {policy} the {permission} permission on {object_type} {set_object.name} ({set_object.id})")

        if send_response == True:
            await self.__send_response(msg_channel, f"{object_type} {set_object.name} was updated to {policy} the bot the permission {permission}")
        
        return AdminError.NoError

    def __check_command_permission(self,guild,channel,member):
        if member.guild_permissions.administrator:
            return AdminError.NoError

        if not self.bot.guild_configuration.channel_is_admin(guild.id,channel.id):
            logger.error(f"admin commands cannot be used in channel {channel.name} ({channel.id}) - user {member.name} ({member.id})")
            return AdminError.ChannelPerms
        if not self.__user_can_administer_bot(member,guild.id):
            logger.error(f"the user {member.name} ({member.id}) does not have sufficient permission to run administrator commands")
            return AdminError.UserPerms
        return AdminError.NoError

    def __user_can_administer_bot(self,member,guild):
        # any user who is allowed to administer the server can set bot options
        if member.guild_permissions.administrator == True:
            return True

        # see if the user is explicitly allowed to administer the bot
        if self.bot.guild_configuration.user_can_administer_bot(guild,member.id):
            return True
        
        # check if this user has any role that can administer the bot
        for role in member.roles:
            if self.bot.guild_configuration.role_can_administer_bot(guild,role.id):
                return True

        return False

    def __get_command_error(self,enumtype,message):
        return {
            "success": False,
            "message": message,
            "errtype": enumtype
        }

def setup(bot):
    bot.add_cog(Admin(bot))

def require_arguments(string,count,delims):
    args = string.split(delims)
    if count != len(args):
        raise IndexError(f"{count} arguments were required, but {len(args)} arguments were passed in")

    return args

def get_lookup_data(guild,fetchtype):
    if (fetchtype == "channel"):
        return {
            "fetch_method": guild.get_channel,
            "iterable": guild.channels,
            "regex": "^<#([0-9]+)>"
        }
    if (fetchtype == "role"): 
        return {
            "fetch_method": guild.get_role,
            "iterable": guild.roles,
            "regex": "^<@&([0-9]+)>"
        }
    if (fetchtype == "user"):
        return {
            "fetch_method": guild.get_member,
            "iterable": guild.members,
            "regex": "^<@!([0-9]+)>"
        }

def string_to_object(string,guild,fetchtype="channel"):
    lookups = get_lookup_data(guild, fetchtype)
    
    # see if this is an id in <#id> format
    groups = re.match(lookups["regex"], string)
    if groups is not None:
        try:
            identifier = groups.group(1)
            value = lookups["fetch_method"](int(identifier))
            if value is not None:
                return value
            else:
                return None
        except IndexError:
            pass

    # maybe we were given just a regular channel id number
    groups = re.match("(^[0-9]+$)", string)
    if groups is not None:
        try:
            identifier = groups.group(1)
            logger.debug(f"matched with channel id {identifier}")
            value = lookups["fetch_method"](int(identifier))
            if value is not None:
                return value
        except IndexError:
            pass
    
    return discord.utils.get(lookups["iterable"], name=string)