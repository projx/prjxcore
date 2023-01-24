# -*- coding: utf-8 -*-
# Author:       Kelvin W
# Date:         2022
# Description:  Class for sending WebHook reports to Utime Kuna, the Manager Manager allows multiple objects to be registered
# Note:         All calls are Static

import time
from abc import ABC, abstractmethod
import requests
from prjxcore.AppTimer import AppTimer
from pprint import pprint
### https://kuma.prjx.uk/api/push/cc0gz3IGAd?status=up&msg=ASDASDASDASD&ping=40

class Hook(object):
    url = None
    use_timer = None
    logs = []

class HookSender(Hook):


    def __init__(self, url, use_timer=False):
        self.logs = []
        self.url = url
        self.use_timer = use_timer
        if self.use_timer:
            AppTimer.add(self.url)
        else:
            self.use_timer = False

    def log(self, msg):
        self.logs.append(msg)

    def send(self, status, msg, ping):
        if self.use_timer:
           ping = AppTimer.get_time(self.url)
           ping = round(ping*1000)
           self.log("Ping in MS: {}".format(ping))


        self.log("Ping time is {}".format(ping))
        url = self.url + "?status={}&msg={}&ping={}".format(status, msg, ping)
        self.log("Sending to {}".format(url))
        r = requests.get(url, verify=False)
        self.log(r.text)
        if r.status_code == 200:
            return True
        else:
            return False

class HookManager(object):
    hooks = dict()

    def register(self, name, hook : Hook):
        self.hooks[name] = hook

    def get(self, name : str):
        return self.hooks[name]

    def get_all(self):
        return self.hooks

    def send(self, name, status, msg, ping):
        hook = self.get(name)
        hook.send(status, msg, ping)

    def send_list(self, names, status, msg, ping):
        for name in names:
            self.send(name, status, msg, ping)
