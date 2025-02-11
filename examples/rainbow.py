#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from usbfan import Colour, Column, Device, Message, Program, TextMessage

# We can cycle the rainbow here and fill all 144 columns
rainbow_colours = [Colour.red, Colour.yellow, Colour.green,
                   Colour.cyan, Colour.blue, Colour.magenta]
rainbow = [Column([True] * 11,
                  rainbow_colours[i % len(rainbow_colours)])
           for i in range(Message.MAX_COLUMNS)]
p = Program((
    TextMessage("Here comes the rainbow!"),
    Message(rainbow),
))

# Open the device and program
d = Device()
d.program(p)
