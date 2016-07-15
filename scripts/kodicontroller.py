
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import requests
import json

class KodiController(object):
    __serverconf = None

    def __init__(self, serverconf):
        self.__serverconf = serverconf

    def post(self,command):
        url = "http://" + self.__serverconf["hostname"] +  ":" + str(self.__serverconf["port"]) + "/jsonrpc"
        headers = {"Content-Type": "application/json"}
        r = requests.post(
            url,
            data=json.dumps(command),
            headers=headers,
            auth=(self.__serverconf["user"], self.__serverconf["password"]))
        return r.json()
