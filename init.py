#!/usr/bin/python
from Models.relay import Relay
from Models.room import Room
import mysql.connector
from mysql.connector import Error
import RPi.GPIO as GPIO
import time

pumpRelay = Relay("relaypump", "close", 1)
_db_cursor = None
_db_conn = None


def connect():
    """ Connect to MySQL database """
    try:
        _db_conn = mysql.connector.connect(host='192.138.0.132',
                                           database='temperature',
                                           user='root',
                                           password='B3nmal!gn312')
        if _db_conn.is_connected():
            print('Connected to MySQL database')
            _db_cursor = _db_conn.cursor()
    except:
        print("Could not connect to Database")


def getAllRelays():
    relays = []
    
    connect()
    
    query = "SELECT * FROM relays"
    
    cursor.execute(sql)
    
    rcount = int(cursor.rowcount)
    
    for r in rcount:
        row = cursor.fetchone()
        
        relay = Relay(row[0], row[1], row[2])
        
        relays.append(relay)
    
    return relays


def getPumpRelayStatus():
    connect()
    
    query = "SELECT status FROM relays WHERE name = '%s'" % (pumpRelay.name)
    
    _db_cursor.execute(query)
    
    result = mycursor.fetchall()
    
    _db_conn.close()
    
    return result


if __name__ == '__main__':
    pumpRelay = getPumpRelayStatus()
    isOpen = False
    relays = getAllRelays()
    GPIO.setmode(GPIO.BCM)

    GPIO.cleanup()

    for relay in relays:
        GPIO.setup(relay.gpio, GPIO.OUT)
        GPIO.output(relay.gpio, GPIO.HIGH)

        if relay.status == 'open' and relay.name != 'relaypump':
            GPIO.output(relay.gpio, GPIO.LOW)
            isOpen = True

    for relay in relays:
        if relay.name == 'relaypump' and isOpen == True:
            GPIO.output(pumpRelay.gpio)
