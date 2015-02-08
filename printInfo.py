#!/usr/bin/env python

from blinkstick import blinkstick

for bstick in blinkstick.find_all():
    print "Fround device:"
    print "  Manufacturer: " + bstick.get_manufacturer()
    print "  Description: " + bstick.get_description()
    print "  Serial: " + bstick.get_serial()
    print "  Color: " + bstick.get_color(color_format="hex")
    print "  Info Block 1: " + bstick.get_info_block1()
    print "  Info Block 2: " + bstick.get_info_block2()
