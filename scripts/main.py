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

    gpiomap= conf.getGPIOMap()
    gpion  = conf.getGPION()
    option = conf.getOption()
    files  = conf.getFiles()
    command= conf.getCommand()

    playlist.clear()    
    for k,v in files.items():
        playlist.addFile(v)

    if option["autostart"]:
        playlist.play(repeat = option["repeat"])

    gpio = GPIOController.GPIOController(gpiomap.keys() + gpion, pullup = option["pullup"])
        
    def sw_pressed(gpiopin):
        num = gpiomap[gpiopin]
        if num == "ntri":
            num = gpio.getBinary(gpion)
            
        myprint("gpio {0} is pressed: funcnum {1}".format(gpiopin,num))
        if option["exit"] == num:
            reactor.stop()
            return

        if num in command:
            player.do(command[num])
            return

        if num in files:
            pos = files.keys().index(num)
            playlist.play(position = pos, repeat = option["repeat"])
        

    gpio.allocate(gpiomap.keys(),sw_pressed)
    gpio.allocate(gpion)
    
    reactor.run()

if __name__ == "__main__":
    main()
