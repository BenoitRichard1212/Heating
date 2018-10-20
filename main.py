#!/usr/bin/python
from relay import Relay
from room import Room
import mysql.connector
from mysql.connector import Error
import RPi.GPIO as GPIO
import time
from decimal import Decimal

GPIO.setmode(GPIO.BCM)
pumpRelay = Relay("relaypump", "close", 17)
_db_cursor = None
_db_conn = None
#function get all d'initialisation

def closeRelay(p_relay):
    try:
        _db_conn = mysql.connector.connect(host='192.168.0.132',
                                           database='temperatures',
                                           user='logger',
                                           password='password')
        if _db_conn.is_connected():
            print('Connected to MySQL database')
            _db_cursor = _db_conn.cursor()
            query = "UPDATE relays SET status = 'close' WHERE name = '%s';" % (p_relay.name)
            _db_cursor.execute(query)
            _db_cursor.commit()
            _db_conn.close()

            GPIO.setup(p_relay.gpio, GPIO.OUT)
            GPIO.output(p_relay.gpio, GPIO.HIGH)
    except:
        print("Could not connect to Database")


def openRelay(p_relay):
    try:
        _db_conn = mysql.connector.connect(host='192.168.0.132',
                                           database='temperatures',
                                           user='logger',
                                           password='password')
        if _db_conn.is_connected():
            print('Connected to MySQL database')
            _db_cursor = _db_conn.cursor()
            query = "UPDATE relays SET status = 'open' WHERE name = '%s';" % (p_relay.name)
            _db_cursor.execute(query)
            _db_cursor.commit()
            _db_conn.close()
            GPIO.setup(p_relay.gpio, GPIO.OUT)
            GPIO.output(p_relay.gpio, GPIO.LOW)
    except:
        print("Could not connect to Database")


def getPumpRelayStatus():
    print("Function : getPumpRelayStatus")
    _db_conn = mysql.connector.connect(host='192.168.0.132',
                                       database='temperatures',
                                       user='logger',
                                       password='password')
    if _db_conn.is_connected():
        print('Connected to MySQL database')
        _db_cursor = _db_conn.cursor()
        query = "SELECT status FROM relays WHERE name = 'relaypump'"
        _db_cursor.execute(query)
        row = _db_cursor.fetchone()
        result = row[0]
        _db_conn.close()
        return result
    else:
        print("Could not connect to Database")


def getRelay(name):
    print("Function : getRelay")
    _db_conn = mysql.connector.connect(host='192.168.0.132',
                                       database='temperatures',
                                       user='logger',
                                       password='password')
    if _db_conn.is_connected():
        print('Connected to MySQL database')
        _db_cursor = _db_conn.cursor()
        query = "SELECT * FROM relays WHERE name = '%s'" % (name)
        _db_cursor.execute(query)
        row = _db_cursor.fetchone()
        relay = Relay(row[0], row[1], row[2])
        _db_conn.close()
        return relay
    else:
        print("Could not connect to Database")



def getAllRelays():
    print("Function : getAllRelays")
    relays = []
    _db_conn = mysql.connector.connect(host='192.168.0.132',
                                       database='temperatures',
                                       user='logger',
                                       password='password')
    if _db_conn.is_connected():
        print('Connected to MySQL database')
        _db_cursor = _db_conn.cursor()
    else:
        print("Could not connect to Database")

    query = "SELECT * FROM relays"
    _db_cursor.execute(query)
    row = _db_cursor.fetchone()
    while row is not None:
        relay = Relay(row[0], row[1], row[2])
        relays.append(relay)
        row = _db_cursor.fetchone()
    _db_conn.close()
    return relays


def getAllRooms():
    print("Function : getAllRooms")
    rooms = []
    _db_conn = mysql.connector.connect(host='192.168.0.132',
                                       database='temperatures',
                                       user='logger',
                                       password='password')
    if _db_conn.is_connected():
        print('Connected to MySQL database')
        _db_cursor = _db_conn.cursor()
    else:
        print("Could not connect to Database")

    query = "SELECT * FROM rooms"
    _db_cursor.execute(query)
    row = _db_cursor.fetchone()
    while row is not None:
        room = Room(row[0], row[1], row[2], row[3], row[4])
        rooms.append(room)
        row = _db_cursor.fetchone()
    _db_conn.close()   
    return rooms


def getSensorTemp(name):
    print("Function : getSensorTemp, name")
    print(name)
    _db_conn = mysql.connector.connect(host='192.168.0.132',
                                       database='temperatures',
                                       user='logger',
                                       password='password')
    if _db_conn.is_connected():
        print('Connected to MySQL database')
        _db_cursor = _db_conn.cursor()
    else:
        print("Could not connect to Database")

    query = "SELECT temperature FROM temperaturedata WHERE sensor = '%s'" % (name)
    _db_cursor.execute(query)
    row = _db_cursor.fetchone()
    result = row[0]
    _db_conn.close()
    return result


def openRelayLogic(p_relay):
    print("Function : openRelay, status :")
    pumpStatus = getPumpRelayStatus()
    print(pumpStatus)
    print("relay qui souvre :")
    print(p_relay.name)

    if (pumpStatus == "close"):
        openRelay(getRelay("relaypump"))
        time.sleep(2);
        openRelay(p_relay)
    else:
        openRelay(p_relay)


def closeRelayLogic(p_relay):
    print("Function : closeRelay, name :")
    print(p_relay)
    stayOpen = False
    relays = getAllRelays()
    status = getPumpRelayStatus()

#for relay in relays:
#    if (relay.name == "relaypump" and status == "open"):
#        stayOpen = True
#    if (relay.name != p_relay and status == "open"):
#        stayOpen = True
#    if (relay.name == p_relay and status == "close"):

    if (stayOpen == True):
        print("stayOpen:")
        print(stayOpen)
        closeRelay(p_relay)
    else:
        print("stayOpen:")
        print(stayOpen)
        closeRelay(getRelay("relaypump"))
        closeRelay(p_relay)


if __name__ == '__main__':
    pumpRelay = getPumpRelayStatus()
    rooms = getAllRooms()
    for room in rooms:  
        relay = getRelay(room.relay)
        status = relay.status
        if (status == "close"):
            if (getSensorTemp(room.sensor_wall) > room.temp_min):
                print("opening relay")
                openRelayLogic(getRelay(relay.name))
        else:
            if (getSensorTemp(room.sensor_wall) < room.temp_min):
                print("closing relay")
                print(relay.name)
                closeRelayLogic(getRelay(relay.name))
