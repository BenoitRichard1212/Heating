#!/usr/bin/python
import RPi.GPIO as GPIO
import time

class Relay:
  def __init__(self, relayName, relayStatus, relayGpio):
    self.relayName = relayName
    self.relayStatus = relayStatus
    self.relayGpio = relayGpio

  def openRelay(self):
    self.relayStatus = "Open"
    GPIO.output(self.relayGpio, GPIO.LOW)

  def openRelay(self):
    self.relayStatus = "Close"
    GPIO.output(self.relayGpio, GPIO.HIGH)
