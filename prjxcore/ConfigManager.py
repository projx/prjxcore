# -*- coding: utf-8 -*-
# Author:       Kelvin W
# Date:         2020
# Description:  Stores configuration information for scripts, which it can load and same from a yaml file(s)... It
#               can load multiple yaml files, these are loaded as "sections".
# Note:         All calls are Static

import yaml
import json
import os
from prjxcore.utils import *


class ConfigManager():
    """
    Stores configuration information for scripts, which it can load and same from a yaml file(s)... It
    can load multiple yaml files, these are loaded as "sections".
    """
    format = ""
    config = dict()
    config_path = ""
    format = "yml"

    @classmethod
    def __serialise(cls, section=False):
        """
        Serialise the config to a string, either in YAML or JSON format, depending on the format set with ConfigManager.set_format()
        :param config:
        :param section: 
        :return: 
        """
        data = {}
        if section!=False:
            data[section] = cls.config[section]
        else:
            data = cls.config

        if cls.format == "yml":
            return yaml.dump(data, default_flow_style=False)
        elif cls.format == "json":
            return json.dumps(data, indent=4)
        else:
            print("No config format specified")

    @classmethod
    def __unserialise(cls, input):

        if cls.format == "yml":
            return yaml.load(input, Loader=yaml.FullLoader)
        elif cls.format == "json":
            return json.loads(input)
        else:
            print("No format specified")

    @classmethod
    def set_section(cls, section, data):
        """
        Set the value of a section
        :param section: the section to set
        :param data: the data to set in the section
        :return: None
        """
        cls.config[section] = data

    @classmethod
    def get_section(cls, section):
        """
        Get the value of a section
        :param section: the section to get
        :return: the value of the section
        """
        return cls.config[section]

    @classmethod
    def get_value(cls, section, value):
        """
        Get the value of a specific key in a section
        :param section: the section to get
        :param value: the key to get
        :return: the value of the key
        """
        return cls.config[section][value]

    @classmethod
    def get(cls, section, value):
        """
        Get the value of a specific key in a section
        :param section: the section to get
        :param value: the key to get
        :return: the value of the key
        """
        return cls.config[section][value]

    @classmethod
    def get_all(cls):
        """
        Get the entire config
        :return: the entire config
        """
        return cls.config

    @classmethod
    def has(cls, section, value):
        """
        Check if a key exists in a section
        :param section: the section to check
        :param value: the key to check
        :return: True if the key exists, False otherwise
        """
        if value in cls.config[section]:
            return True
        else:
            return False

    @classmethod
    def __get_os_path(cls):
        """
        Get the path to the current file
        :return: the path to the current file
        """
        dir_path = os.path.dirname(os.path.realpath(__file__))
        return dir_path

    @classmethod
    def get_config_path(cls):
        """
        Get the path to the config file
        :return: the path to the config file
        """
        return cls.config_path

    @classmethod
    def set_config_path(cls, path):
        """
        Set the path to the config file
        :param path: the path to the config file
        :return: None
        """
        cls.config_path = path

    @classmethod
    def save_to_file(cls, config_path=False, section=False):
        """
        Save the config to a file
        :param config_path: the path to the file to save to
        :param section: the section to save
        :return: None
        """
        if config_path:
            cls.config_path = config_path
        else:
            config_path = cls.get_config_path()

        output = cls.__serialise(section)
        with open(config_path, 'w') as filehandle:
            filehandle.write(output)

    @classmethod
    def merge(cls, data):
        """
        Merge the given data into the existing config
        :param data: the data to merge
        :return: None
        """
        cls.config = merge_nested_dicts(cls.config, data)
    
    @classmethod
    def load_to_dict(cls, config_path = False):
        """
        Load the config from a file and return it as a dictionary
        :param config_path: the path to the file to load from
        :return: the config as a dictionary
        """
        if config_path:
            cls.config_path = config_path
        else:
            config_path = cls.get_config_path()

        with open(config_path, 'r') as filehandle:
            filecontent = filehandle.read()

        conf = cls.__unserialise(filecontent)
        return conf

    @classmethod
    def load(cls, config_path = False):
        """
        Load the config from a file and set it as the current config
        :param config_path: the path to the file to load from
        :return: None
        """
        conf = cls.load_to_dict(config_path)
        for key, item in conf.items():
            cls.config[key] = item

    @classmethod
    def set_all(cls, data : dict):
        """
        Set the entire config
        :param data: the new config
        :return: None
        """
        cls.config = data

    @classmethod
    def clear_all(cls):
        """
        Clear the entire config
        :return: None
        """
        cls.config = dict()