#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import kodicontroller as KodiController
import requests
import json

class KodiPlaylist(KodiController.KodiController):
    __playlistid = 0

    def __init__(self, serverconf , playlistid = 0):
        super(KodiPlaylist, self).__init__(serverconf)
        self.__playlistid = playlistid

    def clear(self):
        command = {
            "jsonrpc": "2.0",
            "method": "Playlist.Clear",
            "params": {
                "playlistid": self.__playlistid
            },
            "id": 1
        }
        return super(KodiPlaylist, self).post(command)

    def addFile(self, filename):
        command = {
            "jsonrpc": "2.0",
            "method": "Playlist.Add",
            "params": {
                "playlistid": self.__playlistid,
                "item": {
                    "file" : filename }
            },
            "id": 1
        }
        return super(KodiPlaylist, self).post(command)
        
    def play(self, position = 0 , repeat = "one"):
        command = {
            "jsonrpc": "2.0",
            "method": "Player.Open",
            "params": {
                "item": {
                    "playlistid" : self.__playlistid,
                    "position" : position
                },
                "options" : {
                    "repeat" : repeat
                }
            },
            "id": 1
        }
        return super(KodiPlaylist, self).post(command)
    
