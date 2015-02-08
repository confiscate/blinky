#!/usr/bin/env python

from blinkstick import blinkstick

for bstick in blinkstick.find_all():
    bstick.set_color(channel=0, index=0, name="red")
    bstick.set_color(channel=0, index=1, name="blue")
    bstick.set_color(channel=0, index=2, name="yellow")
    bstick.set_color(channel=0, index=3, name="lemonchiffon")
    bstick.set_color(channel=0, index=4, name="orange")
    bstick.set_color(channel=0, index=5, name="maroon")
    bstick.set_color(channel=0, index=6, hex="#eeeeee")
    bstick.set_color(channel=0, index=7, hex="#333333")
