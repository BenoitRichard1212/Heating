#!/usr/bin/python
from w1thermsensor import W1ThermSensor

sensor = W1ThermSensor()
temperature_in_celsius = sensor.get_temperature()
humidity = sensor.get_humidity()
temperature_in_fahrenheit = sensor.get_temperature(W1ThermSensor.DEGREES_F)
temperature_in_all_units = sensor.get_temperatures([
    W1ThermSensor.DEGREES_C,
    W1ThermSensor.DEGREES_F,
    W1ThermSensor.KELVIN])

print(temperature_in_celsius)
print(humidity)


#Get the data of one sensor, now we need to identify each sensor by it's ID.
#create an array of sensor keyed to their name
#get the temp for each ID and then update the table with the proper name


#Need to find how to grab the humidy

#https://gpiozero.readthedocs.io/en/v1.3.1/api_pins.html