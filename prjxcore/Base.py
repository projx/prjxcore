# -*- coding: utf-8 -*-
# Author:       Kelvin W
# Date:         2022
# Description:  Base class with a few useful functions



class Base():

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        from pprint import pformat
        return pformat(vars(self), indent=4, width=1)
