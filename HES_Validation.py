# HES validation protocol
import RPi.GPIO as GPIO
import busio
import board
import adafruit_ads1x15.ads1115 as ADS 
from adafruit_ads1x15.analog_in import AnalogIn
import time

i2c = busio.I2C(board.SCL, board.SDA)
ads5V = ADS.ADS1115(i2c, mode =0,address=0x49)
HES0 = AnalogIn(ads5V, ADS.P0)
HES1 = AnalogIn(ads5V, ADS.P1)
HES2 = AnalogIn(ads5V, ADS.P2)

while True:
#    Magnet facing first way: ~32767
#    Magnet facing other way: ~106
    print('HES 0: ', HES0.value)
#     print('HES 1: ', HES1.value)
#     print('HES 2: ', HES2.value)



