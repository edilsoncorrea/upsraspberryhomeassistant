#!/usr/bin/python

import struct
import smbus
import sys
import time
import RPi.GPIO as GPIO
import json


def readVoltage(bus):
        "This function returns as float the voltage from the Raspi UPS Hat via the provided SMBus object"
        address = 0x36
        read = bus.read_word_data(address, 0X02)
        swapped = struct.unpack("<H", struct.pack(">H", read))[0]
        voltage = swapped * 1.25 /1000/16
        return voltage

        "This function returns as a float the remaining capacity of the battery$
        address = 0x36
        read = bus.read_word_data(address, 0X04)
        swapped = struct.unpack("<H", struct.pack(">H", read))[0]
        #capacity = min(swapped/256 * 0.96899, 100)
        capacity = min(swapped / 256, 100)
        return capacity
        
def readCapacity(bus):
        "This function returns as a float the remaining capacity of the battery$
        address = 0x36
        read = bus.read_word_data(address, 0X04)
        swapped = struct.unpack("<H", struct.pack(">H", read))[0]
        #capacity = min(swapped/256 * 0.96899, 100)
        capacity = min(swapped / 256, 100)
        return capacity

def QuickStart(bus):
        address = 0x36
        bus.write_word_data(address, 0x06,0x4000)

def PowerOnReset(bus):
        address = 0x36
        bus.write_word_data(address, 0xfe,0x0054)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(4,GPIO.IN)

bus = smbus.SMBus(1)  # 0 = /dev/i2c-0 (port I2C0), 1 = /dev/i2c-1 (port I2C1)

Dictionary = {"estado": 'on' if (GPIO.input(4) == GPIO.LOW) else 'off', "capacidade": readCapacity(bus), "voltagem": readVoltage(bus)}


#Dictionary = {"estado": 'on', "capacidade": readCapacity(), "voltagem": readVoltage()}

arquivoUps = open("/dev/ups/ups", mode="w", encoding="utf-8")