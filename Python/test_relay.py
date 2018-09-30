#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pinList = [2, 3, 17, 27, 22]

GPIO.cleanup()

for i in pinList:
        GPIO.setup(i, GPIO.OUT)
        GPIO.output(i, GPIO.HIGH)

sleepTimeL = 2


GPIO.output(2, GPIO.LOW)
print("ONE")
time.sleep(sleepTimeL);
GPIO.output(3, GPIO.LOW)
print("TWO")
time.sleep(sleepTimeL); 
GPIO.output(17, GPIO.LOW)
print("THREE")
time.sleep(sleepTimeL); 
GPIO.output(27, GPIO.LOW) 
print("FOUR")
time.sleep(sleepTimeL);
GPIO.output(22, GPIO.LOW)
print("FIVE")
time.sleep(sleepTimeL);
GPIO.cleanup()
print "CLEAN"
