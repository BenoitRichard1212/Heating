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

def connect():
    """ Connect to MySQL database """
    try:
        _db_conn = mysql.connector.connect(host='localhost',
                                           database='temperature',
                                           user='root',
                                           password='B3nmal!gn312')
        if _db_conn.is_connected():
            print('Connected to MySQL database')
            _db_cursor = _db_conn.cursor()
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
    else:
        print("Could not connect to Database")

    query = "SELECT status FROM relays WHERE name = 'relaypump'"
    _db_cursor.execute(query)
    row = _db_cursor.fetchone()
    result = row[0]
    _db_conn.close()
    return result


def getRelay(name):
    print("Function : getRelay")
    _db_conn = mysql.connector.connect(host='192.168.0.132',
                                       database='temperatures',
                                       user='logger',
                                       password='password')
    if _db_conn.is_connected():
        print('Connected to MySQL database')
        _db_cursor = _db_conn.cursor()
    else:
        print("Could not connect to Database")

    query = "SELECT * FROM relays WHERE name = '%s'" % (name)
    _db_cursor.execute(query)
    row = _db_cursor.fetchone()
    relay = Relay(row[0], row[1], row[2])
    _db_conn.close()
    return relay


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
    return relays
    _db_conn.close()


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
    return rooms
    _db_conn.close()


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



def openPumpRelay():
    print("Function : openPumpRelay")
    _db_conn = mysql.connector.connect(host='192.168.0.132',
                                       database='temperatures',
                                       user='logger',
                                       password='password')
    if _db_conn.is_connected():
        print('Connected to MySQL database')
        _db_cursor = _db_conn.cursor()
    else:
        print("Could not connect to Database")

    query = "UPDATE relays SET status = 'open' WHERE name = 'relaypump';"
    print(query)
    _db_cursor.execute(query)
    _db_conn.commit()
    _db_conn.close()
    GPIO.setup(17, GPIO.OUT)
    GPIO.output(17, GPIO.LOW)


def closePumpRelay():
    print("Function : closePumpRelay")
    _db_conn = mysql.connector.connect(host='192.168.0.132',
                                       database='temperatures',
                                       user='logger',
                                       password='password')
    if _db_conn.is_connected():
        print('Connected to MySQL database')
        _db_cursor = _db_conn.cursor()
    else:
        print("Could not connect to Database")

    query = "UPDATE relays SET status = 'close' WHERE name = 'relaypump';"
    _db_cursor.execute(query)
    _db_conn.commit()   
    _db_conn.close()
    GPIO.setup(17, GPIO.OUT)
    GPIO.output(17, GPIO.HIGH)


def openRelay(relay):
    print("Function : openRelay, status :")
    pumpStatus = getPumpRelayStatus()
    print(pumpStatus)
    
    if (pumpStatus == "close"):
        openPumpRelay()
        time.sleep(2);
        GPIO.setup(relay.gpio, GPIO.OUT)
        GPIO.output(relay.gpio, GPIO.LOW)
        _db_conn = mysql.connector.connect(host='192.168.0.132',
                                       database='temperatures',
                                       user='logger',
                                       password='password')
        if _db_conn.is_connected():
            print('Connected to MySQL database')
            _db_cursor = _db_conn.cursor()
        else:
            print("Could not connect to Database")

        query = "UPDATE relays SET status = 'open' WHERE name = '%s';" % (relay.name)
        print(query)
        _db_cursor.execute(query)
        _db_conn.commit()
        _db_conn.close()
    else:
        GPIO.setup(relay.gpio, GPIO.OUT)
        GPIO.output(relay.gpio, GPIO.LOW)
        _db_conn = mysql.connector.connect(host='192.168.0.132',
                                       database='temperatures',
                                       user='logger',
                                       password='password')
        if _db_conn.is_connected():
            print('Connected to MySQL database')
            _db_cursor = _db_conn.cursor()
        else:
            print("Could not connect to Database")

        query = "UPDATE relays SET status = 'open' WHERE name = '%s';" % (relay.name)
        _db_cursor.execute(query)
        _db_conn.commit()
        _db_conn.close()


def closeRelay(p_relay):
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
        GPIO.setup(relay.gpio, GPIO.OUT)
        GPIO.output(relay.gpio, GPIO.HIGH)
        _db_conn = mysql.connector.connect(host='192.168.0.132',
                                       database='temperatures',
                                       user='logger',
                                       password='password')
        if _db_conn.is_connected():
            print('Connected to MySQL database')
            _db_cursor = _db_conn.cursor()
        else:
            print("Could not connect to Database")

        query = "UPDATE relays SET status = 'close' WHERE name = '%s';" % (p_relay)
        _db_cursor.execute(query)
        _db_conn.commit()
        _db_conn.close()
    else:
        print("stayOpen:")
        print(stayOpen)
        closePumpRelay()
        GPIO.setup(relay.gpio, GPIO.OUT)
        GPIO.output(relay.gpio, GPIO.HIGH)
        _db_conn = mysql.connector.connect(host='192.168.0.132',
                                       database='temperatures',
                                       user='logger',
                                       password='password')
        if _db_conn.is_connected():
            print('Connected to MySQL database')
            _db_cursor = _db_conn.cursor()
        else:
            print("Could not connect to Database")

        query = "UPDATE relays SET status = 'close' WHERE name = '%s';" % (p_relay)
        print(query)
        _db_cursor.execute(query)
        _db_conn.commit()
        _db_conn.close()


if __name__ == '__main__':
    pumpRelay = getPumpRelayStatus()
    rooms = getAllRooms()
    for room in rooms:
        print("In main, room temp min:")
        print(room.temp_min)
        print("sensor current temp :")
        print(getSensorTemp(room.sensor_wall))
	relay = getRelay(room.relay)
        print("A VERIFIER ! ICI NAME !")
        print(relay.name)
	status = relay.status
        if (status == "close"):
            if (getSensorTemp(room.sensor_wall) > room.temp_min):
                print("opening relay")
                openRelay(getRelay(relay.name))
        else:
            if (getSensorTemp(room.sensor_wall) < room.temp_min):
                print("closing relay")
		print(relay.name)
                closeRelay(getRelay(relay.name))
