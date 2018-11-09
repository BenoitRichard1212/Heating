#!/usr/bin/python
from relay import Relay
from room import Room
import mysql.connector
from mysql.connector import Error
from w1thermsensor import W1ThermSensor
import RPi.GPIO as GPIO
import time
from decimal import Decimal

GPIO.setmode(GPIO.BCM)
pumpRelay = Relay("relaypump", "close", 17)

def checkTemperature():
    _db_conn = mysql.connector.connect(host='192.168.0.131',
                                       database='temperatures',
                                       user='logger',
                                       password='password')
    if _db_conn.is_connected():
        print('Connected to MySQL database getAllRelays')
        _db_cursor = _db_conn.cursor()
        query = "SELECT * FROM relays"
        _db_cursor.execute(query)
        row = _db_cursor.fetchone()
        while row is not None:
            relay = Relay(row[0], row[1], row[2])
            relays.append(relay)
            row = _db_cursor.fetchone()
        _db_conn.close()
        return relays
    else:
    	print('Could not connect to database')


def getSensorsID():
    for sensor in W1ThermSensor.get_available_sensors():
        print("Sensor %s has temperature %.2f" % (sensor.id, sensor.get_temperature()))

if __name__ == '__main__':
	sensor = W1ThermSensor()
    temperature_in_celsius = sensor.get_temperature()
    temperature_in_fahrenheit = sensor.get_temperature(W1ThermSensor.DEGREES_F)
    temperature_in_all_units = sensor.get_temperatures([
        W1ThermSensor.DEGREES_C,
        W1ThermSensor.DEGREES_F,
        W1ThermSensor.KELVIN])

