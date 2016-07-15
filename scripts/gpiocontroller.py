#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from sysfs.gpio import Controller, OUTPUT, INPUT, BOTH

class GPIOController:
    def __init__(self, gpiopins):
        Controller.available_pins = gpiopins

    def allocate(self, gpiopins, pressed_callback = None):
        def inputChanged(number,state):
            if state == 1:
                pressed_callback(number)
        
        for pin in gpiopins:
            Controller.alloc_pin(pin, INPUT, inputChanged if pressed_callback else None, BOTH)
            
    def getState(self,number):
        return Controller.get_pin_state(number)

    def getBinary(self,gpion):
        n = 0
        for i,v in enumerate(gpion[::-1]):
            if self.getState(v):
                n |= (1<<i)
        return n
    
