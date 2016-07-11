#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import requests
import json

class KodiController:
    __serverconf = None
    __playlistid = 0

    def __init__(self, serverconf , playlistid = 0):
        self.__serverconf = serverconf
        self.__playlistid = playlistid

    def __post(self,command):
        url = "http://" + self.__serverconf["hostname"] +  ":" + str(self.__serverconf["port"]) + "/jsonrpc"
        headers = {"Content-Type": "application/json"}
        r = requests.post(
            url,
            data=json.dumps(command),
            headers=headers,
            auth=(self.__serverconf["user"], self.__serverconf["password"]))
        return r.json()

    def clearPlaylist(self):
        command = {
            "jsonrpc": "2.0",
            "method": "Playlist.Clear",
            "params": {
                "playlistid": self.__playlistid
            },
            "id": 1
        }
        return self.__post(command)

    def addFileToPlaylist(self, filename):
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
        return self.__post(command)
        
    def playPlaylist(self, position = 0 , repeat = "one"):
        command = {
            "jsonrpc": "2.0",
            "method": "Player.Open",
            "params": {
                "item": {
                    "playlistid" : self.__playlistid,
                    "position" : position
                },
                "options" : {
                    "repeat" : "one"
                }
            },
            "id": 1
        }
        return self.__post(command)
