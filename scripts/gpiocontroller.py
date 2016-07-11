#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from sysfs.gpio import Controller, OUTPUT, INPUT, BOTH

class GPIOController:
    def __init__(self, gpiopins, pressed_callback):
        Controller.available_pins = gpiopins

        def inputChanged(number,state):
            if state == 1:
                pressed_callback(number)
        
        for pin in gpiopins:
            Controller.alloc_pin(pin, INPUT, inputChanged, BOTH)

