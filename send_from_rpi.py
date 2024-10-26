#!/usr/bin/env python3

# see joan's posts from https://forums.raspberrypi.com/viewtopic.php?t=117893
# this .py must be in vw.py's folder from pigpio EXAMPLE's folder (pigpiod running)
# https://github.com/joan2937/pigpio/blob/master/EXAMPLES/Python/VIRTUAL_WIRE/vw.py
# pigpio uses BCM pinout (BCM14 = wiringpi15 = livolo home-automation)

import time
import pigpio
import vw

pi = pigpio.pi()

if not pi.connected:
   exit(0)

tx = vw.tx(pi, 14, 300) # Set pigpio instance, TX module GPIO pin and baud rate

msg = "42"

tx.put(msg)
while tx.pi.wave_tx_busy():
    time.sleep(0.1)

#tx.waitForReady()

tx.cancel()
pi.stop()