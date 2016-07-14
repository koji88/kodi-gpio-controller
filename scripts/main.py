#!/usr/bin/env python
# -*- coding:utf-8

from __future__ import print_function

import sys
import argparse
import gpiocontroller as GPIOController
import config as Configure
from twisted.internet import reactor

import kodiplaylist as KodiPlaylist
import kodiplayer as KodiPlayer

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
        print("configuration file is not supplied")
        return

    isQuiet = args.quiet

    conf = Configure.Configure(args.conf)
    
    player   = KodiPlayer.KodiPlayer(conf.getServerConf())
    playlist = KodiPlaylist.KodiPlaylist(conf.getServerConf())
    
    option = conf.getOption()
    files  = conf.getFiles()
    command= conf.getCommand()

    playlist.Clear()    
    for k,v in files.items():
        playlist.AddFile(v)

    if option["autostart"]:
        playlist.Play(repeat = option["repeat"])

    def sw_pressed(gpiopin):
        if option["exit"] == gpiopin:
            myprint("gpio {0} is pressed: exit".format(gpiopin))
            reactor.stop()
            return

        if gpiopin in command:
            myprint("gpio {0} is pressed: do {1}".format(gpiopin,command[gpiopin]))
            player.Do(command[gpiopin])
            return
        
        pos = files.keys().index(gpiopin)
        myprint("gpio {0} is pressed: play {1}".format(gpiopin,files[gpiopin]))
        playlist.Play(position = pos, repeat = option["repeat"])
        

    pins = command.keys() + files.keys()
    if option["exit"]:
        pins.append(option["exit"])
        
    gpio = GPIOController.GPIOController(pins,sw_pressed)
    
    reactor.run()

if __name__ == "__main__":
    main()
