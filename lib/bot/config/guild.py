import json
import logging
import os.path
import traceback

from os import path
from discord import Intents, Embed, File
from discord.ext.commands import Context

logger = logging.getLogger(f"doublelung.{__name__}")

def get_object_value(obj,key):
    """
        Use dot-separated keys when trying to access certain configuration options in the object
    """
    keys = key.split(".", 1)

    if (len(keys) > 0 and (keys[0] not in obj)):
        return None
    elif len(keys) == 1 and keys[0] in obj:
        return obj[key]
    elif len(keys) == 2 and keys[0] in obj:
        return get_object_value(obj[keys[0]], keys[1])
    else:
        raise Exception("This is an unforseen branch!")

def set_object_value(obj,key,value):
    """
        Same as get_object_value(). Use a dot-separated list of keys to specify the config option to change

        Example
        -------

        Before set_object_value:
        .. code-block:: json
            "testobj": {
                "setting": {
                    "key": "my-string"
                }
            }
        .. code-block:: python3

            set_object_value(object,"testobj.setting.key","test-string")
        
        After set_object_value:
        .. code-block:: json
            "testobj": {
                "setting": {
                    "key": "test-string"
                }
            }

    """
    keys = key.split(".", 1)

    if (len(keys) > 0 and (keys[0] not in obj)):
        return None
    elif len(keys) == 1:
        obj[key] = value
    elif len(keys) == 2 and keys[0] in obj:
        set_object_value(obj[keys[0]],keys[1],value)
    elif len(keys) == 2 and keys[0] not in obj:
        obj[keys[0]] = {}
        set_object_value(obj[keys[0]],keys[1],value)
    else:
        raise Exception("Could not set value on object due to unforseen error")

class GuildConfig():
    """
    This class deals with guild configuration information.
    It is responsible for finding per-guild settings like available channels
    and bot administration options.
    """
    def __init__(self,guildpath):
        self.guildpath = guildpath
        logger.info(f"guild configuration manager path is {self.guildpath}")

    def get_guild_alias(self,guild_id):
        guild = str(guild_id)
        self.__create_guild_if_not_exists(guild)

        if self.__guild_is_configured(guild):
            return self.__load_guild_setting(guild,"alias")

    def can_listen_on_channel(self,guild_id,channel_id):
        guild = str(guild_id)       # just in case we are passed an integer. the json config uses strings
        channel = str(channel_id)   # same
        self.__create_guild_if_not_exists(guild)

        listen = self.__load_channel_setting(guild,channel,"listen")
        # we may add additional cases later, but for now this will work
        if listen is not None and listen == "allow":
            return True
        elif listen is None:
            default_policy = self.__load_guild_setting(guild,"channels-config.default-policy.listen")
            if default_policy is not None and default_policy == "allow":
                return True

        # if none of the above conditions allow listen, don't listen!
        return False

    def can_respond_on_channel(self,guild_id,channel_id):
        guild = str(guild_id)
        channel = str(channel_id)
        self.__create_guild_if_not_exists(guild)

        respond = self.__load_channel_setting(guild,channel,"respond")
        if respond is not None and respond == "allow":
            return True
        elif respond is None:
            default_policy = self.__load_guild_setting(guild,"channels-config.default-policy.respond")
            if default_policy is not None and default_policy == "allow":
                return True
        return False

    def channel_is_admin(self,guild_id,channel_id):
        guild = str(guild_id)
        channel = str(channel_id)
        self.__create_guild_if_not_exists(guild)

        admin = self.__load_channel_setting(guild,channel,"admin")
        if admin is not None and admin == "allow":
            return True
        elif admin is None:
            default_policy = self.__load_guild_setting(guild,"channels-config.default-policy.admin")
            if default_policy is not None and default_policy == "allow":
                return True
        return False

    def role_can_administer_bot(self,guild_id,role_id):
        guild = str(guild_id)
        role = str(role_id)

        self.__create_guild_if_not_exists(guild)
        admin_role = self.__load_role_setting(guild,role,"admin")
        if admin_role is not None and admin_role == "allow":
            return True
        elif admin_role is None:
            default_policy = self.__load_guild_setting(guild,"roles-config.default-policy.admin-commands")
            if default_policy is not None and default_policy == "allow":
                return True

        return False
 
    def user_can_administer_bot(self,guild_id,user_id):
        guild = str(guild_id)
        user = str(user_id)

        self.__create_guild_if_not_exists(guild)
        admin_role = self.__load_user_setting(guild,user,"admin")
        if admin_role is not None and admin_role == "allow":
            return True
        elif admin_role is None:
            default_policy = self.__load_guild_setting(guild,"users-config.default-policy.admin-commands")
            if default_policy is not None and default_policy == "allow":
                return True

        return False

    def user_can_send_commands(self,guild_id,user_id,role_ids):
        guild = str(guild_id)
        user = str(user_id)
        roles = list(map(lambda role: str(role), role_ids))

        self.__create_guild_if_not_exists(guild)
        allowed = self.__load_user_setting(guild,user,"commands")
        if allowed is not None and allowed == "allow":
            return True
        elif allowed is not None and allowed == "deny":
            return False

        allow = False
        for role in roles:
            allowed = self.__load_role_setting(guild,role,"commands")
            if allowed is not None and allowed == "deny":
                # if any assigned role is deny, deny access from here
                return False
            elif allowed is not None and allowed == "allow":
                # we may be able to allow them through at this point, so set our sentinel
                allow = True
        
        if allow:
            return True

        # does the default user policy let this user through?
        allowed = self.__load_guild_setting(guild,"users-config.default-policy")
        if allowed is not None and allowed == "allow":
            return True
        if allowed is not None and allowed == "deny":
            return False

        # does the default roles policy let this user through?
        allowed = self.__load_guild_setting(guild,"roles-config.default-policy")
        if allowed is not None and allowed == "allow":
            return True
        if allowed is not None and allowed == "deny":
            return False

        # no option that allows the user through is configured
        return False

    def set_default_permission(self,guild_id,policy,allow):
        guild = str(guild_id)
        self.__create_guild_if_not_exists(guild)

        settings = [ f"{policy}s-config.default-policy" ]
        if (policy == "channel"):
            settings = [ f"{policy}s-config.default-policy.listen", f"{policy}s-config.default-policy.respond" ]
        
        for setting in settings:
            self.__change_guild_setting(guild,setting,allow)

    def set_channel_policy(self,guild_id,channel_id,policy,allow):
        guild = str(guild_id)
        channel = str(channel_id)
        self.__create_guild_if_not_exists(guild)
        self.__change_channel_setting(guild,channel,policy,allow)

    def set_role_policy(self,guild_id,role_id,policy,allow):
        guild = str(guild_id)
        role = str(role_id)
        self.__create_guild_if_not_exists(guild)
        self.__change_role_setting(guild,role,policy,allow)

    def set_user_policy(self,guild_id,user_id,policy,allow):
        guild = str(guild_id)
        user = str(user_id)
        self.__create_guild_if_not_exists(guild)
        self.__change_user_setting(guild,user,policy,allow)

    def remove_policy_object(self,guild_id,object_id,config_type):
        guild = str(guild_id)
        self.__create_guild_if_not_exists(guild)
        self.__remove_config_element(guild,object_id,config_type)

    def remove_all_policies_of_type(self,guild_id,config_type):
        guild = str(guild_id)
        self.__create_guild_if_not_exists(guild)
        self.__clear_config_element_list(guild,config_type)

    """
        All the methods from here down are private (internal) methods
    """
    def __load_guild_setting(self,guild,setting):
        config_data = self.__get_guild_config_object(guild)
        if config_data is not None:
            return get_object_value(config_data,setting)
        else:
            return None

    def __load_channel_setting(self,guild,channel,setting):
        config_data = self.__get_guild_config_object(guild)
        if config_data is not None:
            channel_configs = config_data['channels-config']['channels']
            if channel in channel_configs:
                return get_object_value(channel_configs[channel], setting)
            else:
                return None

        return None

    def __load_role_setting(self,guild,role,setting):
        config_data = self.__get_guild_config_object(guild)
        if config_data is not None:
            role_configs = config_data['roles-config']['roles']
            if role in role_configs:
                return get_object_value(role_configs[role], setting)
            else:
                return None

        return None

    def __load_user_setting(self,guild,user,setting):
        config_data = self.__get_guild_config_object(guild)
        if config_data is not None:
            user_configs = config_data['users-config']['users']
            if user in user_configs:
                return get_object_value(user_configs[user], setting)
            else:
                return None

        return None

    def __change_guild_setting(self,guild,setting,value):
        config_data = self.__get_guild_config_object(guild)
        if config_data is not None:
            set_object_value(config_data,setting,value)
            self.__store_guild_config_object(guild,config_data)
            return True

        return False

    def __change_channel_setting(self,guild,channel,setting,value):
        config_data = self.__get_guild_config_object(guild)
        if config_data is not None:
            channel_configs = config_data['channels-config']['channels']
            if channel not in channel_configs:
                listen_default = self.__load_guild_setting(guild,"channels-config.default-policy.listen")
                respond_default = self.__load_guild_setting(guild,"channels-config.default-policy.respond")
                channel_configs[channel] = {
                    "listen": listen_default,
                    "respond": respond_default,
                    "admin": "deny"
                }

            set_object_value(channel_configs[channel],setting,value)
            self.__store_guild_config_object(guild,config_data)
            return True

        return False

    def __change_role_setting(self,guild,role,setting,value):
        config_data = self.__get_guild_config_object(guild)
        if config_data is not None:
            role_configs = config_data['roles-config']['roles']
            # just create the role in the object if it doesn't exist
            if role not in role_configs:
                default = self.__load_guild_setting(guild,"roles-config.default-policy")
                role_configs[role] = {
                    "commands": default,
                    "admin": "deny"
                }

            set_object_value(role_configs[role],setting,value)
            self.__store_guild_config_object(guild,config_data)
            return True

        return False

    def __change_user_setting(self,guild,user,setting,value):
        config_data = self.__get_guild_config_object(guild)
        if config_data is not None:
            user_configs = config_data['users-config']['users']
            # just create the role in the object if it doesn't exist
            if user not in user_configs:
                default = self.__load_guild_setting(guild,"users-config.default-policy")
                user_configs[user] = {
                    "commands": default,
                    "admin": "deny"
                }

            set_object_value(user_configs[user],setting,value)
            self.__store_guild_config_object(guild,config_data)
            return True

        return False

    def __clear_config_element_list(self,guild,itemtype):
        config_data = self.__get_guild_config_object(guild)
        if config_data is not None:
            type_configs = config_data[f"{itemtype}s-config"][f"{itemtype}s"]
            keylist = list(type_configs.keys())
            for key in keylist:
                logger.debug(f"removed config element: {type_configs.pop(str(key), None)}")

        self.__store_guild_config_object(guild,config_data)

    def __remove_config_element(self,guild,element,itemtype):
        config_data = self.__get_guild_config_object(guild)
        if config_data is not None:
            type_configs = config_data[f"{itemtype}s-config"][f"{itemtype}s"]
            logger.debug(f"removed element: {type_configs.pop(str(element), None)}")

        self.__store_guild_config_object(guild,config_data)
    
    def __create_guild_if_not_exists(self,guild):
        logger.debug(f"checking to see if guild {guild} exists in configuration")
        if not self.__guild_is_configured(guild):
            logger.info(f"guild {guild} is not configured; adding new configuration")
            self.__write_new_guild_configuration(guild)

    def __get_guild_config_object(self,guild):
        guildfile = f"{self.guildpath}/{guild}.json"
        with open(guildfile, "r", encoding="utf-8") as gf:
            config_data = json.load(gf)
            if (config_data):
                return config_data
        
        return None

    def __store_guild_config_object(self,guild, config_object):
        guildfile = f"{self.guildpath}/{guild}.json"
        with open(guildfile, "w") as gf:
            json.dump(config_object,gf,indent=4)

    def __write_new_guild_configuration(self, guild, default_policy="allow"):
        guildfile = f"{self.guildpath}/{guild}.json"
        with open(guildfile, "w") as gf:
            new_config = self.__get_empty_guild_config(default_policy)
            logger.debug(new_config)
            json.dump(new_config, gf, indent=4)

    def __guild_is_configured(self, guild):
        guildfile = f"{self.guildpath}/{guild}.json"
        if not path.exists(guildfile):
            return False
        
        with open(guildfile, "r", encoding="utf-8") as gf:
            json_data = json.load(gf)
            if not json_data:
                return False

        return True

    def __get_empty_guild_config(self, default_policy="allow"):
        return {
            "alias": "",
            "channels-config": {
                "default-policy": {
                    "listen": default_policy,
                    "respond": default_policy
                },
                "channels": {}
            },
            "roles-config": {
                "default-policy": "allow",
                "admin-commands": "deny",
                "roles": {}
            },
            "users-config": {
                "default-policy": "allow",
                "admin-commands": "deny",
                "users": {}
            }
        }