# -*- coding: utf-8 -*-
# Author:       Kelvin W
# Date:         2020
# Description:  Wrapper for python logging, specifically for logging to console and file,
#               note all calls are Static

import logging
import sys

class applog:
    loggingEnabled = False
    debugEnabled = False
    infoEnabled = False
    initialised = False
    path = ""
    name = ""
    handler = None
    formatter = None
    categories = dict()

    def __init__(cls):
        if cls.initialised == False:
            cls.setup()

    @classmethod
    def setup(cls, to_console = True, to_file = False, name = "LOCAL"):
        cls.handler = logging.getLogger()
        cls.handler.setLevel(logging.DEBUG)
        ###cls.formatter = logging.Formatter('[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s')
        cls.formatter = logging.Formatter('[%(asctime)s] [{}] [%(levelname)s] %(message)s'.format(name))

        ## Setup Console Logging..
        if to_console == True:
            cls.set_console_handler()

        if to_file != False:
            cls.set_file_handler(to_file)

    @classmethod
    def set_console_handler(cls):
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(cls.formatter)
        cls.handler.addHandler(console_handler)


    @classmethod
    def set_file_handler(cls, path):
        file_handler = logging.FileHandler(path)
        file_handler.setFormatter(cls.formatter)
        cls.handler.addHandler(file_handler)


    @classmethod
    def set_syslog_handler(cls, host, port, socket_type):
        handler = logging.handlers.SysLogHandler(address=(host, port), socktype=socket_type) ## socktype=socket.SOCK_STREAM or SOCK_DGRAM
        handler.setFormatter(cls.formatter)
        cls.handler.addHandler(handler)


    @classmethod
    def set_enabled(cls, status):
        cls.loggingEnabled = status


    @classmethod
    def set_debug(cls, status):
        cls.debugEnabled = status
        cls.handler.setLevel(logging.DEBUG)


    @classmethod
    def set_info(cls, status):
        cls.infoEnabled = status
        cls.handler.setLevel(logging.INFO)


    @classmethod
    def debug(cls, str):
        if cls.loggingEnabled: ## and cls.debugEnabled:
            cls.handler.debug(str)


    @classmethod
    def info(cls, str):
        if cls.loggingEnabled: ### and cls.infoEnabled:
            cls.handler.info(str)


    @classmethod
    def error(cls, str):
        if cls.loggingEnabled:
            cls.handler.error(str)