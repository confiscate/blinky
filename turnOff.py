#!/usr/bin/env python

from blinkstick import blinkstick

for bstick in blinkstick.find_all():
    bstick.set_color(channel=0, index=0)
    bstick.set_color(channel=0, index=1)
    bstick.set_color(channel=0, index=2)
    bstick.set_color(channel=0, index=3)
    bstick.set_color(channel=0, index=4)
    bstick.set_color(channel=0, index=5)
    bstick.set_color(channel=0, index=6)
    bstick.set_color(channel=0, index=7)
