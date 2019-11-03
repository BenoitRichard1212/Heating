#!/usr/bin/python
class Relay:
  def __init__(self, name, status, gpio, type):
    self.name = name
    self.status = status
    self.gpio = gpio
    self.type = type
