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
    format = ""
    config = dict()
    config_path = ""
    format = "yml"

    @classmethod
    def __serialise(cls, section=False):
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
        cls.config[section] = data

    @classmethod
    def get_section(cls, section):
        return cls.config[section]

    @classmethod
    def get_value(cls, section, value):
        return cls.config[section][value]

    @classmethod
    def get(cls, section, value):
        return cls.config[section][value]

    @classmethod
    def has(cls, section, value):
        if value in cls.config[section]:
            return True
        else:
            return False

    @classmethod
    def __get_os_path(cls):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        return dir_path

    @classmethod
    def get_config_path(cls):
        return cls.config_path

    @classmethod
    def set_config_path(cls, path):
        cls.config_path = path

    @classmethod
    def save_to_file(cls, config_path=False, section=False):
        if config_path:
            cls.config_path = config_path
        else:
            config_path = cls.get_config_path()

        output = cls.__serialise(section)
        with open(config_path, 'w') as filehandle:
            filehandle.write(output)

    
    @classmethod
    def merge(cls, data):
        cls.config = merge_nested_dicts(cls.config, data)
    
    @classmethod
    def load_to_dict(cls, config_path = False):
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
        conf = cls.load_to_dict(config_path)
        for key, item in conf.items():
            cls.config[key] = item

    @classmethod
    def set_all(cls, data : dict):
        cls.config = data

    @classmethod
    def clear_all(cls):
        cls.config = dict()