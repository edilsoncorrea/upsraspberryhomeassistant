# upsraspberryhomeassistant
Criar arquivo json a partir de leituras no UPS para disponibilizar para o Home Assistant versão Supervised


sudo crontab -e


sudo chmod +x ups_18650_lite.py

sudo /home/pi/scripts/executarpythonuos.sh

@reboot mkdir /dev/ups
@reboot touch /dev/ups/ups
@reboot chmod +rw /dev/ups/ups
* * * * *  /home/pi/scripts/executarpythonups.sh
* * * * * sleep 20; /home/pi/scripts/executarpythonups.sh
* * * * * sleep 40; /home/pi/scripts/executarpythonups.sh


>#!/bin/bash
>python3 /home/pi/scripts/ups_18650_lite.py





>#!/usr/bin/python
>
>import struct
>import smbus
>import sys
>import time
>import RPi.GPIO as GPIO
>import json
>
>
>def readVoltage(bus):
>        "This function returns as float the voltage from the Raspi UPS Hat via $
>        address = 0x36
>        read = bus.read_word_data(address, 0X02)
>        swapped = struct.unpack("<H", struct.pack(">H", read))[0]
>        voltage = swapped * 1.25 /1000/16
>        return voltage

