#!/usr/bin/python
from relay import Relay
from room import Room
import mysql.connector
from mysql.connector import Error
import RPi.GPIO as GPIO
import time
from decimal import Decimal

GPIO.setmode(GPIO.BCM)
pumpRelay = Relay("relay_pump", "close", 17)

def connect():
    _db_conn = mysql.connector.connect(host='192.168.0.131',
                                       database='temperatures',
                                       user='logger',
                                       password='password')
    if _db_conn.is_connected():
        print('Connected to MySQL database')
        _db_cursor = _db_conn.cursor()
    else:
        print("Could not connect to Database closeRelay")


def closeRelay(p_relay):
    _db_conn = mysql.connector.connect(host='192.168.0.131',
                                       database='temperatures',
                                       user='logger',
                                       password='password')
    if _db_conn.is_connected():
        print('Connected to MySQL database closeRelay')
        _db_cursor = _db_conn.cursor()
        query = "UPDATE relays SET status = 'close' WHERE name = '%s';" % (p_relay.name)
        _db_cursor.execute(query)
        _db_conn.commit()
        _db_conn.close()
        GPIO.setup(p_relay.gpio, GPIO.OUT)
        GPIO.output(p_relay.gpio, GPIO.HIGH)
    else:
        print("Could not connect to Database closeRelay")


def openRelay(p_relay):
    _db_conn = mysql.connector.connect(host='192.168.0.131',
                                       database='temperatures',
                                       user='logger',
                                       password='password')
    if _db_conn.is_connected():
        print('Connected to MySQL database openRelay')
        _db_cursor = _db_conn.cursor()
        query = "UPDATE relays SET status = 'open' WHERE name = '%s';" % (p_relay.name)
        _db_cursor.execute(query)
        _db_conn.commit()
        _db_conn.close()
        GPIO.setup(p_relay.gpio, GPIO.OUT)
        GPIO.output(p_relay.gpio, GPIO.LOW)
    else:
        print("Could not connect to Database openRelay")


def getPumpRelayStatus():
    _db_conn = mysql.connector.connect(host='192.168.0.131',
                                       database='temperatures',
                                       user='logger',
                                       password='password')
    if _db_conn.is_connected():
        print('Connected to MySQL database getPumpRelayStatus')
        _db_cursor = _db_conn.cursor()
        query = "SELECT status FROM relays WHERE name = 'relay_pump'"
        _db_cursor.execute(query)
        row = _db_cursor.fetchone()
        result = row[0]
        _db_conn.close()
        return result
    else:
        print("Could not connect to Database getPumpRelayStatus")


def getRelay(name):
    _db_conn = mysql.connector.connect(host='192.168.0.131',
                                       database='temperatures',
                                       user='logger',
                                       password='password')
    if _db_conn.is_connected():
        print('Connected to MySQL database getRelay')
        _db_cursor = _db_conn.cursor()
        query = "SELECT * FROM relays WHERE name = '%s'" % (name)
        _db_cursor.execute(query)
        row = _db_cursor.fetchone()
        relay = Relay(row[0], row[1], row[2])
        _db_conn.close()
        return relay
    else:
        print("Could not connect to Database getRelay")



def getAllRelays():
    relays = []
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
        print("Could not connect to Database getAllRelays")


def getAllRooms():
    rooms = []
    _db_conn = mysql.connector.connect(host='192.168.0.131',
                                       database='temperatures',
                                       user='logger',
                                       password='password')
    if _db_conn.is_connected():
        print('Connected to MySQL database getAllRooms')
        _db_cursor = _db_conn.cursor()
        query = "SELECT * FROM rooms"
        _db_cursor.execute(query)
        row = _db_cursor.fetchone()
        while row is not None:
            room = Room(row[0], row[1], row[2], row[3], row[4])
            rooms.append(room)
            row = _db_cursor.fetchone()
        _db_conn.close()   
        return rooms
    else:
        print("Could not connect to Database getAllRooms")


def getSensorTemp(name):
    _db_conn = mysql.connector.connect(host='192.168.0.131',
                                       database='temperatures',
                                       user='logger',
                                       password='password')
    if _db_conn.is_connected():
        print('Connected to MySQL database getSensorTemp')
        _db_cursor = _db_conn.cursor()

        query = "SELECT temperature FROM temperaturedata WHERE sensor = '%s'" % (name)
        _db_cursor.execute(query)
        row = _db_cursor.fetchone()
        result = row[0]
        _db_conn.close()
        return result
    else:
        print("Could not connect to Database getSensorTemp")

def getDeviceTemp(name):
    _db_conn = mysql.connector.connect(host='192.168.0.131',
                                       database='temperatures',
                                       user='logger',
                                       password='password')
    if _db_conn.is_connected():
        print('Connected to MySQL database getSensorTemp')
        _db_cursor = _db_conn.cursor()

        query = "SELECT temperature FROM temperaturedata WHERE sensor = '%s'" % (name)
        _db_cursor.execute(query)
        row = _db_cursor.fetchone()
        result = row[0]
        _db_conn.close()
        return result
    else:
        print("Could not connect to Database getDeviceTemp")        


def openRelayLogic(p_relay):
    pumpStatus = getPumpRelayStatus()

    if (pumpStatus == "close"):
        openRelay(getRelay("relay_pump"))
        time.sleep(2);
        openRelay(p_relay)
    else:
        openRelay(p_relay)


def pumpOnlyOpen():
    closePump = True
    relays = getAllRelays()
    for relay in relays:
        if (relay.name != "relay_pump" and relay.status == "open"):
            closePump = False
    return closePump


def closeRelayLogic(p_relay):
    relays = getAllRelays()
    status = getPumpRelayStatus()

    closeRelay(p_relay)

    if (pumpOnlyOpen() == True):
        closeRelay(getRelay("relay_pump"))


if __name__ == '__main__':
    pumpRelay = getPumpRelayStatus()
    rooms = getAllRooms()
    for room in rooms:  
        relay = getRelay(room.relay)
        status = relay.status
        print(room.name)
        print(room.sensor_floor)
        print(getDeviceTemp(room.sensor_floor))
        print(room.relay)
        print(status)
        if (status == "close"):
            if (getDeviceTemp(room.sensor_floor) < room.temp_min):
                openRelayLogic(getRelay(room.relay))
        else:
            if (getDeviceTemp(room.sensor_floor) > room.temp_min):
                closeRelayLogic(getRelay(room.relay))
