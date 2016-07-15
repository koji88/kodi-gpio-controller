#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import kodicontroller as KodiController
import requests
import json

class KodiPlayer(KodiController.KodiController):
    __playerid = 0

    def __init__(self, serverconf , playerid = 0):
        super(KodiPlayer, self).__init__(serverconf)
        self.__playerid = playerid

    def do(self,name):
        method = getattr(self, name)
        method()        
        
    def playPause(self):
        command = {
            "jsonrpc": "2.0",
            "method": "Player.PlayPause",
            "params": {
                "playerid": self.__playerid,
            },
            "id": 1
        }
        return super(KodiPlayer, self).post(command)

    def stop(self):
        command = {
            "jsonrpc": "2.0",
            "method": "Player.Stop",
            "params": {
                "playerid": self.__playerid,
            },
            "id": 1
        }
        return super(KodiPlayer, self).post(command)

    def next(self):
        command = {
            "jsonrpc": "2.0",
            "method": "Player.GoTo",
            "params": {
                "playerid": self.__playerid,
                "to" : "next"
            },
            "id": 1
        }
        return super(KodiPlayer, self).post(command)

    def previous(self):
        command = {
            "jsonrpc": "2.0",
            "method": "Player.GoTo",
            "params": {
                "playerid": self.__playerid,
                "to" : "previous"
            },
            "id": 1
        }
        return super(KodiPlayer, self).post(command)
        
