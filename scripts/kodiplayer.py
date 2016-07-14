#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import kodicontroller as KodiController
import requests
import json

class KodiPlayer(KodiController.KodiController):

    def __init__(self, serverconf , Playerid = 0):
        super(KodiPlayer, self).__init__(serverconf)

    def Do(self,name):
        method = getattr(self, name)
        method()        
        
    def PlayPause(self):
        command = {
            "jsonrpc": "2.0",
            "method": "Player.PlayPause",
            "params": {
                "playerid": 0,
            },
            "id": 1
        }
        return super(KodiPlayer, self).Post(command)

    def Stop(self):
        command = {
            "jsonrpc": "2.0",
            "method": "Player.Stop",
            "params": {
                "playerid": 0,
            },
            "id": 1
        }
        return super(KodiPlayer, self).Post(command)

    def Next(self):
        command = {
            "jsonrpc": "2.0",
            "method": "Player.GoTo",
            "params": {
                "playerid": 0,
                "to" : "next"
            },
            "id": 1
        }
        return super(KodiPlayer, self).Post(command)

    def Previous(self):
        command = {
            "jsonrpc": "2.0",
            "method": "Player.GoTo",
            "params": {
                "playerid": 0,
                "to" : "previous"
            },
            "id": 1
        }
        return super(KodiPlayer, self).Post(command)
        
