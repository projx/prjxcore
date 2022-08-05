import time
from timeit import default_timer as timer
from datetime import timedelta

### An old implementation ...
# class QTimer():
#     time_list = {}
#
#     @classmethod
#     def add(cls, name):
#         cls.time_list[name] = time.perf_counter()
#
#     @classmethod
#     def get_time(cls, name):
#         elapsed_time = time.perf_counter() - float(cls.time_list[name])
#         return format(elapsed_time, '.4f')


class AppTimer(object):
    timers = {}
    records = {}

    def __init__(self):
        pass

    @classmethod
    def add(cls, name):
        cls.timers[name] = timer()

    @classmethod
    def get_time_formatted(cls, name, record=False):
        return timedelta(seconds=cls.get_milliseconds(name, record))

    @classmethod
    def get_milliseconds(cls, name, record=False):
        time = timer() - cls.timers[name]
        if record:
            cls.records[name] = time
        return time

    @classmethod
    def get_time(cls, name, record=False):
        return cls.get_milliseconds(name, record)

    @classmethod
    def remove(cls, name):
        del cls.timers[name]