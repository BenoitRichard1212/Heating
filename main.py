#!/usr/bin/python

//CHECK ALL IF ADD THE ":" 
from Models.relay import Relay
from Models.room import Room
import mysql.connector
from mysql.connector import Error
import RPi.GPIO as GPIO
import time

pumpRelay = new Relay("relaypump", "close", 1);
_db_cursor = None
_db_conn = None


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
    connect()
    query = "SELECT status FROM relays WHERE name = '%s'" % (pumpRelay.name)
    _db_cursor.execute(query)
    result = mycursor.fetchall()
    _db_conn.close()
    return result


def getRelay(name):
    connect()
    query = "SELECT * FROM relays WHERE name = '%s'" % (name)
    _db_cursor.execute(query)
    row = mycursor.fetchall()
    relay = New Relay(row[0], row[1], row[2])
    _db_conn.close()
    return relay

//REDO FUNCTION WITH NEW SHIT
def getAllRelays():
    relays = []
    connect()
    query = "SELECT * FROM relays"
    cursor.execute(sql)
    rcount = int(cursor.rowcount)
    for r in rcount:
        row = cursor.fetchone()
        relay = New Relay(row[0], row[1], row[2])
        relays.append(relay)
    return relays

//REDO FUNCTION WITH NEW SHIT
def getAllRooms():
    rooms = []
    connect()
    query = "SELECT * FROM rooms"
    cursor.execute(sql)
    rcount = int(cursor.rowcount)
    for r in rcount:
        row = cursor.fetchone()
        room = New Room(row[0], row[1], row[2], row[3], row[4])
        rooms.append(room)
    return rooms


def getSensorTemp(name):
    connect()
    query = "SELECT temperature FROM temperauredata WHERE sensorName = '%s'" % (name)
    _db_cursor.execute(query)
    result = mycursor.fetchall()
    _db_conn.close()
    return result


def openPumpRelay():
    connect()
    query = "UPDATE relays SET status = 'open' WHERE name = '%s';" % (pumpRelay.name)
    _db_cursor.execute(query)
    _db_conn.close()
    GPIO.output(pumpRelay.gpio, GPIO.LOW)


def closePumpRelay():
    connect()
    query = "UPDATE relays SET status = 'close' WHERE name = '%s';" % (pumpRelay.name)
    _db_cursor.execute(query)    
    _db_conn.close()
    GPIO.output(pumpRelay.gpio, GPIO.HIGH)

def openRelay(relay):
    pumpStatus = getPumpRelayStatus()
    
    if (pumpStatus == "close"):
        openPumpRelay()
        sleep(2)
        GPIO.output(relay.gpio, GPIO.LOW)
        connect()
        query = "UPDATE relays SET status = 'open' WHERE name = '%s';" % (relay.name)
        _db_cursor.execute(query)
        _db_conn.close()
    else:
        GPIO.output(relay.gpio, GPIO.LOW)
        connect()
        query = "UPDATE relays SET status = 'open' WHERE name = '%s';" % (relay.name)
        _db_cursor.execute(query)
        _db_conn.close()

def closeRelay(p_relay):
    stayOpen = False
    relays = getAllRelays()
    
    for relay in relays
        if (relay.name != pumpRelay.name and relay.name != p_relay.name and pumpRelay.status == "open")
            stayOpen = True

    if (stayOpen == True)
        GPIO.output(relay.gpio, GPIO.HIGH)
        connect()
        query = "UPDATE relays SET status = 'close' WHERE name = '%s';" % (p_relay.name)
        _db_cursor.execute(query)
        _db_conn.close()
    else
        closePumpRelay()
        GPIO.output(relay.gpio, GPIO.HIGH)
        connect()
        query = "UPDATE relays SET status = 'close' WHERE name = '%s';" % (p_relay.name)
        _db_cursor.execute(query)
        _db_conn.close()


if __name__ == '__main__':
    pumpRelay = getPumpRelayStatus()
    rooms = getAllRooms()
    for room in rooms
        if (room.relay == "close")
            if (getSensorTemp(room.sensor_wall) > room.temp_min)
                openRelay(room.relay)
        else
            if (getSensorTemp(room.sensor_wall) < room.temp_min)
                closeRelay(room.relay)
