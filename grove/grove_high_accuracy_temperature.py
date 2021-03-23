#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The MIT License (MIT)
# Copyright (C) 2018  Seeed Technology Co.,Ltd.
#
# This is the library for Grove Base Hat
# which used to connect grove sensors for Raspberry Pi.
'''
This is the code for
    - `Grove - I2C High Accuracy Temperature Sensor(MCP9808) <https://www.seeedstudio.com/Grove-I2C-High-Accuracy-Temperature-Sensor-MCP980-p-3108.html>`_

Examples:
    .. code-block:: python
    import sys
    import time
    from grove.factory import Factory
    from grove.temperature import Temper

    print("Insert Grove - I2C-High-Accuracy-Temperature")
    print("  to Grove-Base-Hat any I2C slot")

    sensor = Factory.getTemper("MCP9808-I2C")
    sensor.resolution(Temper.RES_1_16_CELSIUS)

    print('Detecting temperature...')
    while True:
        print('{} Celsius'.format(sensor.temperature))
        time.sleep(1)
'''
import sys
import time
from grove.factory import Factory
from grove.temperature import Temper

import argparse

#metadata
__version__     = "0.0.2d"
__author__      = "Sebastien COUDERT"

__all__ = ['Temper']

def main():
  #CLI option
  parser = argparse.ArgumentParser(description='get temperature on Grove High Accuracy device on I2C bus'
  + ' (%(prog)s v'+__version__+')'
  , epilog="examples: %(prog)s --help"
  )
  ##version
  parser.add_argument('-v', '--version'
  , action="store_true", default=False
  , help='show version (default: False) currently v'+__version__)
  ##integer
  parser.add_argument('-n', '--number'
  , default=-2
  , help='number of iteration')

  ##parse
  args=parser.parse_args()
  version=args.version
  nb=int(args.number)+1
  #}CLI option

  if(version):
    print __version__
    quit()



  print("Insert Grove - I2C-High-Accuracy-Temperature")
  print("  to Grove-Base-Hat any I2C slot")

  sensor = Factory.getTemper("MCP9808-I2C", address=0x19)
  sensor.resolution(Temper.RES_1_16_CELSIUS)

  print("resolution=",sensor._resolution)

  print('Detecting temperature...')
  if(nb<0):
    while True:
      print('{} Celsius'.format(sensor.temperature))
      time.sleep(1)
    #}endless loop
  else:
    for i in range(1,nb):
      print('{} Celsius'.format(sensor.temperature))
      time.sleep(1)
    #}i loop

if __name__ == '__main__':
    main()
