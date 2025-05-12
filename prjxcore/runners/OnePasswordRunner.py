import subprocess,os
import sys
import re
import dotenv
import json
from pprint import pprint,pformat
# from typing import LiteralString as str
from prjxcore.Runner import BaseCMD, CMDRunner
from pathlib import Path
from prjxcore.AppLog import applog

"""
This is a collection of classes and function for working with the 1Password CLI tool... Note it requires a service
account to be configured, and a token _generated for that account. The token is then set via environment variable:

export OP_SERVICE_ACCOUNT_TOKEN=xxxxxxxx

To create an service account, 
1) log into 1Paswword website
2) Goto Integrations 
3) under "Infrastructure Secret Mgt", click "Other"
4) Click "Create a new service account"

For details, see:
https://developer.1password.com/docs/service-accounts/get-started/
https://1password.community/discussion/140375/how-to-use-service-accounts-and-regular-accounts-in-the-same-environment

"""


# os.environ['OP_SERVICE_ACCOUNT_TOKEN']=OP_SERVICE_ACCOUNT_TOKEN

# x = 'op read "op://servers etc/vCenter - 1. WEB UI/password"'
# x1 = "op read op://servers etc/vCenter - 1. WEB UI/password"
# x2 = "op read 'op://zKUBE - MGT/test/password'"
# op item get --vault="zKUBE - MGT" "test"  --fields label=username,password --format=json
# "op://zKUBE - MGT/test/password"
# "op read 'op://zKUBE - MGT/test/password'"
# "op read 'op://zKUBE - MGT/test/password'"
# cmd1='echo $OP_SERVICE_ACCOUNT_TOKEN'

"""
Private dictionary, provides a runtime for responses from 1Password
@todo: Implement encrypted file system storage
"""
__RESPONSE_CACHE__ = {}

def init_1password_env(env_path : str) -> bool:
    if not Path(env_path).exists():
        raise Exception("env file does not exist ({})".format(env_path))
    else:
        dotenv.load_dotenv(dotenv_path=env_path)


class BaseOnePasswordCMD(BaseCMD):
    regex = ""
    format = "json"

    """
    Base class for 1Password commands
    """
    def __init__(self):
        super().__init__()
        applog.debug("IN PARENT __INIT__")
        self.format = "json"
        if(self.check_token() == False):
            raise Exception("OP_SERVICE_ACCOUNT_TOKEN environment variable not set")

    def set_vault(self, vault: str):
        """Set the 1Password vault that contains the item to be retrieved """
        self.vault = vault

    def set_format(self, format="json"):
        """
        Set the format of the output from the 1Password CLI, options are json or csv
        """
        self.format = format

    def get_format(self) -> str:
        """
        Return the format of the output from the 1Password CLI
        """
        return "--format={}".format(self.format)

    def check_token(self) -> bool:
        """
        Check to see if the 1Password service account auth token is set as an environment variable
        :return: True if the OP_SERVICE_ACCOUNT_TOKEN environment variable is set
        """
        if "OP_SERVICE_ACCOUNT_TOKEN" not in os.environ:
            return False
        else:
            return True

    def get_template(self) -> str:
        """
        Return the template for the 1Password CLI command
        :return:
        """
        return "op '{}' get "

    def from_json(self, results : str):
        """
        Convert the json output from the 1Password CLI into a dictionary
        :param results:
        :return:
        """
        data = json.loads(results)

        # If only 1 field was requested, it returns a single-list
        if isinstance(data, dict) and "fields" not in data:
            applog.debug("BaseOnePasswordCMD > fron_json: Single field returned")
            self.data[data["label"]] = data
            return

        # Full object requested, it return dict, with a "fields" key, which is a list of dicts
        if isinstance(data, dict) and "fields" in data:
            applog.debug("BaseOnePasswordCMD > fron_json: Full object returned")
            for field_entry in data["fields"]:
                self.data[field_entry["label"]] = field_entry

        # If multiple fields were requested, it returns a LIST of dictionaries
        elif isinstance(data, list):
            applog.debug("BaseOnePasswordCMD > fron_json: Multiple fields returned (but not ALL")
            for val in data:
                self.data[val["label"]] = val

        else:
            applog.error("BaseOnePasswordCMD > fron_json: Unknown data type returned from 1Password {}".format(type(data)))
            raise Exception("Unknown data type returned from 1Password")

    def get_value(self, field: str) -> str:
        """
        Return the value of a field from the 1Password CLI output
        :param field:
        :return:
        """
        
        applog.debug("Getting Field Lookup: " + field)
        applog.debug("*++ IN BaseOnePasswordCMD > get_value, {} *******************************".format(field))
        applog.debug(pformat(self.data))
        applog.debug("Getting Value: " + self.data[field]["value"])
        return self.data[field]["value"]

    def from_regex(self, val: str) -> BaseCMD:
        """
        Parse a string that contains a 1Password reference
        :param val:
        :return:
        """
        raise NotImplementedError("fromRegex() not implemented")


class VaultCMD(BaseOnePasswordCMD):
    """
    Generates a 1Password CLI command to retrieve details about a vault
    """

    def __init__(self, vault: str = None):
        super().__init__()
        self.vault = vault

    def get_vault(self) -> str:
        """
        Generate the 1Password CLI command to retrieve details about a vault
        :return: str
        """
        str = self.get_template().format("vault")
        str = str + " '{}' ".format(self.vault)
        str = str + self.get_format()
        return str

    def get_runnable(self) -> str:
        """
        Return the 1Password CLI command to retrieve details about a vault
        :return:
        """
        return self.get_vault()


class CredentialsCMD(BaseOnePasswordCMD):
    regex = r"1P{(?P<vault>.*)\/(?P<secret>.*)\/(?P<field>.*)}"
    all_fields = False

    """
    Generates a 1Password CLI command to retrieve credentials from a vault
    """

    def __init__(self, extract_from : str, all_fields: bool = False):
        """
        Constructor
        :param reg: A string that contains a 1Password reference
        """
        super().__init__()
        self.from_regex(extract_from)
        self.all_fields = all_fields

    # def __init__(self, vault: str,  name: str, fields: list, all_fields: bool = False):
    #     applog.info("QUITING")
    #     sys.exit(2)
    #     applog.debug("IN __INIT__ START *********")
    #     #super().__init__()
    #     self.vault = vault
    #     self.name = name
    #     self.fields = fields
    #     self.data = dict()
    #     self.all_fields = all_fields
    #     applog.debug("IN __INIT__  END *********")
    #     applog.debug("ALL FIELDS: " + str(self.all_fields))
    #     if(self.all_fields==True):
    #         raise Exception("BOLLOCKS...")

    # def setup(self, vault: str,  name: str, fields: list, all_fields: bool = False):
    #     applog.info("QUITING SETUP")
    #     sys.exit(2)
    #     applog.debug("IN __INIT__ START *********")
    #     #super().__init__()
    #     self.vault = vault
    #     self.name = name
    #     self.fields = fields
    #     self.data = dict()
    #     self.all_fields = all_fields
    #     applog.debug("IN __INIT__  END *********")
    #     applog.debug("ALL FIELDS: " + str(self.all_fields))
    #     if(self.all_fields==True):
    #         raise Exception("BOLLOCKS...")

    def get_value(self, field: str) -> str:
        """
        Return the value of a field from the 1Password CLI output
        :param field:
        :return:
        """
        
        applog.debug("Getting Field Lookup: " + field)
        applog.debug("*++ IN CredentialsCMD > get_value, {} *******************************".format(field))
        applog.debug(pformat(self.data))
        applog.debug("Getting Value: " + self.data[field]["value"])
        return self.data[field]["value"]




    def from_regex(self, val: str, all_fields: bool = False) -> BaseOnePasswordCMD:
        """
        Parse a string that contains a 1Password reference
        :param val:
        :return:
        """
        match = re.search(self.regex, val)
        if match:
            self.vault = match.group(1)
            self.name = match.group(2)
            self.fields = match.group(3).split(",")
            self.data = dict()
            self.all_fields = all_fields
        else:
            raise Exception("Invalid 1Password reference ({})".format(val))

    def get_first_field(self) -> str:
        """
        Return the first field in the list of fields
        :return:
        """
        return self.fields[0]

    def get_first_value(self) -> str:
        """
        Return the first field in the list of fields
        :return:
        """
        return self.get_value(self.get_first_field())

    def get_item(self) -> str:
        """
        Generate the 1Password CLI command to retrieve credentials from a vault
        :return:
        """
        str = self.get_template().format("item")
        str = str + " --vault='{}' ".format(self.vault)
        str = str + " '{}' ".format(self.name)
        if len(self.fields) > 0:
            applog.debug("OnePassword Fields is not empty")
            if(self.all_fields == False):
                applog.debug("OnePassword all fields is FALSE")
                str = str + " --fields '{}' ".format(",".join(self.fields))
            else:
                applog.debug("OnePassword all fields is TRUE")
        str = str + self.get_format()
        return str

    def get_runnable(self) -> str:
        """
        Return the 1Password CLI command to retrieve credentials from a vault
        :return:
        """
        return self.get_item()

    def get_cache_key(self) -> str:
        """
        Return the cache key for the credentials
        :return:
        """
        return "{}-{}".format(self.vault, self.name)


class OnePasswordRunner(CMDRunner):
        def run(self, cmd : BaseCMD, taskname : str, abort_on_error=True, is_dryrun=False) -> bool:
            """
            Run the 1Password CLI command
            :param cmd:
            :param taskname:
            :param abort_on_error:
            :param is_dryrun:
            :return:
            """
            applog.debug("Checking cache for {}".format(cmd.get_cache_key()))
            if cmd.get_cache_key() in __RESPONSE_CACHE__:
                applog.debug("Using cached response for {}".format(cmd.get_cache_key()))
                self.stdout = __RESPONSE_CACHE__[cmd.get_cache_key()]

                return self.stdout
            else:
                applog.debug("1Password object not in cache, loading for {}".format(cmd.get_cache_key()))
                applog.debug("*********************")
                applog.debug(cmd.get_runnable())
                response = super().run(cmd, taskname, abort_on_error, is_dryrun)

                if response == True:
                    __RESPONSE_CACHE__[cmd.get_cache_key()] = self.stdout
                return self.stdout
