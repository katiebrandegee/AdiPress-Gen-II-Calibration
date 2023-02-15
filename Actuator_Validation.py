#!/usr/bin/env python3 

# In real system, actuator shaft moving up results in plunger moving down 

import RPi.GPIO as GPIO
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import time as time


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

i2c = busio.I2C(board.SCL, board.SDA)
ads3V = ADS.ADS1115(i2c)

# pwm max setting is 100% duty cycle --> 100, set frequency to 1000

def encoderTrig(channel):
    global encoderVal
    encoderVal = encoderVal+1



DOWN_EN = 6 
UP_EN = 5
UP_PWM = 13
DOWN_PWM = 12

goButton = 4 
endPin = 23  # (actuator fully extended)
homePin = 24 #(actuator fully retracted)
encoderPin = 16
encoderVal = 0

currentSensor = AnalogIn(ads3V, ADS.P0)
downCurrentSensor = AnalogIn(ads3V, ADS.P1)
upCurrentSensor = AnalogIn(ads3V, ADS.P2)

GPIO.setup(UP_EN, GPIO.OUT)
GPIO.setup(DOWN_EN, GPIO.OUT)
GPIO.setup(UP_PWM, GPIO.OUT)
GPIO.setup(DOWN_PWM, GPIO.OUT)

GPIO.setup(goButton, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(goButton, GPIO.FALLING, callback = goButtonPressed, bouncetime = 150)

GPIO.setup(endPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(homePin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    
GPIO.setup(encoderPin, GPIO.IN)
GPIO.add_event_detect(encoderPin, GPIO.FALLING, callback = encoderTrig, bouncetime = 1)


GPIO.output(UP_EN, GPIO.HIGH)
GPIO.output(DOWN_EN, GPIO.HIGH)


pwmUp = GPIO.PWM(UP_PWM, 1500) # goes from extended to retracted) (Note this seems to vary for different actuatators)
pwmDown = GPIO.PWM(DOWN_PWM, 1500) # goes from retracted to extended)

pwmUp.start(0)
pwmDown.start(0)

print('endPin: ', GPIO.input(endPin))
print('homePin: ',  GPIO.input(homePin))


def main():
    while True:
        if (GPIO.input(goButton) == GPIO.LOW and GPIO.input(endPin)):
            print('Encoder Val: ', encoderVal)
            pwmDown.start(70)
            time.sleep(.2)
            while (GPIO.input(endPin) == GPIO.HIGH and GPIO.input(goButton) == GPIO.HIGH):
                x =2
            pwmDown.stop()
            print('Encoder Val: ', encoderVal)

        
        if (GPIO.input(goButton) == GPIO.LOW and GPIO.input(homePin)):
            print('Encoder Val: ', encoderVal)
            pwmUp.start(70)
            time.sleep(.2)
            while (GPIO.input(homePin) == GPIO.HIGH and GPIO.input(goButton) == GPIO.HIGH):
                print(currentSensor.value)
            pwmUp.stop()
            print('Encoder Val: ', encoderVal)


if __name__ == "__main__":
    main()

    
    


    
  


