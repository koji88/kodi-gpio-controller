#!/usr/bin/env python
# -*- coding:utf-8

from __future__ import print_function

import sys
import argparse
import kodicontroller as KodiController
import gpiocontroller as GPIOController
import config as Configure
from twisted.internet import reactor

isQuiet = False

def myprint(f):
    if not isQuiet:
        print(f)

def main():
    p = argparse.ArgumentParser(description='Kodi remote controller by GPIO')
    p.add_argument('-c','--conf',help="configuration yaml filename")
    p.add_argument('--quiet',action='store_true',help="quiet mode")
    args = p.parse_args()

    if not args.conf:
        print("No configuration file")
        return

    isQuiet = args.quiet

    conf = Configure.Configure(args.conf)
    
    kodi = KodiController.KodiController(conf.getServerConf())
    kodi.clearPlaylist()

    option = conf.getOption()
    files  = conf.getFiles()
    pinmap = []
    
    for k,v in files.items():
        kodi.addFileToPlaylist(v)

    if option["autostart"] in files:
        kodi.playPlaylist(repeat = option["repeat"])

    def sw_pressed(gpiopin):
        pos = files.keys().index(gpiopin)
        myprint("gpio {0} pressed play {1}".format(gpiopin,files[gpiopin]))
        kodi.playPlaylist(position = pos, repeat = option["repeat"])
        

    gpio = GPIOController.GPIOController(files.keys(),sw_pressed)
    
    reactor.run()

if __name__ == "__main__":
    main()
