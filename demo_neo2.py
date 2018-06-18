#!/bin/env python3
import gex
import time

# play a little neopixel animation as a demo

with gex.Client(gex.TrxRawUSB()) as client:
    # Neopixel strip
    strip = gex.Neopixel(client, 'npx')
    # Load RGB to the strip
    strip.load([0xFF0000, 0xFFFF00, 0x00FF00, 0x0000FF, 0xFF00FF])
    
    for i in range(0,255):
        strip.load([0xFF0000+i, 0xFFFF00, 0x00FF00, 0x0000FF, 0xFF00FF])
        time.sleep(0.01)
        
    strip.clear()
