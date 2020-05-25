#!/usr/bin/python
class Room:
  def __init__(self, name, temp_min, sensor_floor, sensor_wall, relay, relay_second, mode):
    self.name = name
    self.temp_min = temp_min
    self.sensor_floor = sensor_floor
    self.sensor_wall = sensor_wall
    self.relay = relay
    self.relay_second = relay_second
    self.mode = mode
