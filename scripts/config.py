#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import yaml
from collections import OrderedDict

yaml.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
    lambda loader, node: OrderedDict(loader.construct_pairs(node)))

class Configure:
    __data = None

    def __init__(self, yamlfile):
        self.__data = yaml.load(file(yamlfile))

    def getServerConf(self):
        return self.__data["kodi"]

    def getOption(self):
        return self.__data["option"]

    def getFiles(self):
        return self.__data["files"]

    def getCommand(self):
        return self.__data["command"]

    def getGPIOMap(self):
        return {v:k for k, v in self.__data["gpiomap"].items()}
        
