#!/usr/bin/python
from relay import Relay
from room import Room
#from gobalSetting import GlobalSetting
import mysql.connector
from mysql.connector import Error
import RPi.GPIO as GPIO
import time
from decimal import Decimal
import datetime
import logging

GPIO.setmode(GPIO.BCM)
variable_check = 1
pumpRelay = Relay("relay_pump", "close", 17)
logging.basicConfig(filename="/var/log/Heating/sensors_log.txt", level=logging.INFO)

def connect():
    _db_conn = mysql.connector.connect(host='192.168.0.131',
                                       database='temperatures',
                                       user='logger',
                                       password='password')
    if _db_conn.is_connected():
        logging.info('Connected to MySQL database')
        _db_cursor = _db_conn.cursor()
    else:
        logger.error("Could not connect to Database closeRelay")


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

#def getAllGlobalSettings():
#    globalSettings = []
#    _db_conn = mysql.connector.connect(host='192.168.0.131',
#                                       database='temperatures',
#                                       user='logger',
#                                       password='password')
#    if _db_conn.is_connected():
#        print('Connected to MySQL database getAllGlobalSettings')
#        _db_cursor = _db_conn.cursor()
#        query = "SELECT * FROM global_settings"
#        _db_cursor.execute(query)
#        row = _db_cursor.fetchone()
#        while row is not None:
#            globalSetting = GlobalSetting(row[0], row[1])
#            globalSettings.append(globalSetting)
#            row = _db_cursor.fetchone()
#        _db_conn.close()   
#        return globalSettings
#    else:
#        print("Could not connect to Database getAllGlobalSettings")

#def getGlobalSetting(name):
#    _db_conn = mysql.connector.connect(host='192.168.0.131',
#                                       database='temperatures',
#                                       user='logger',
#                                       password='password')
#    if _db_conn.is_connected():
#        print('Connected to MySQL database getGloablSetting')
#        _db_cursor = _db_conn.cursor()
#        query = "SELECT * FROM global_settings WHERE name = '%s'" % (name)
#        _db_cursor.execute(query)
#        row = _db_cursor.fetchone()
#        globalSetting = GlobalSetting(row[0], row[1])
#        _db_conn.close()
#        return globalSetting
#    else:
#        print("Could not connect to Database getRelay")


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
        logging.info(datetime.datetime.now() + ' OPENING PUMP RELAY')
        openRelay(getRelay("relay_pump"))
        time.sleep(2);
        logging.info(datetime.datetime.now() + ' OPENING ' + p_relay)
        openRelay(p_relay)
    else:
        logging.info(datetime.datetime.now() + ' OPENING ' + p_relay)
        openRelay(p_relay)

def openRelayLogicCooling(p_relay):
    pumpStatus = getPumpRelayStatus()

    if (pumpStatus == "close"):
        logging.info(datetime.datetime.now() + ' OPENING PUMP RELAY')
        openRelay(getRelay("relay_pump"))
        time.sleep(2);
        logging.info(datetime.datetime.now() + ' OPENING ' + p_relay)
        openRelay(p_relay)
    else:
        logging.info(datetime.datetime.now() + ' OPENING ' + p_relay)
        openRelay(p_relay)


def pumpOnlyOpen():
    closePump = True
    relays = getAllRelays()
    for relay in relays:
        if (relay.name != "relay_pump" and relay.status == "open"):
            logging.info(datetime.datetime.now() + ' Pump relay is not the only one opened, staying open for the other relays.')
            closePump = False
    return closePump


def closeRelayLogic(p_relay):
    relays = getAllRelays()
    status = getPumpRelayStatus()

    if (pumpOnlyOpen() == True):
        logging.info(datetime.datetime.now() + ' CLOSING PUMP RELAY')
        closeRelay(getRelay("relay_pump"))

    closeRelay(p_relay)

def closeRelayLogicCooling(p_relay):
    relays = getAllRelays()
    status = getPumpRelayStatus()

    if (pumpOnlyOpen() == True):
        logging.info(datetime.datetime.now() + ' CLOSING PUMP RELAY')
        closeRelay(getRelay("relay_pump"))

    logging.info(datetime.datetime.now() + ' CLOSING ' + p_relay)
    closeRelay(p_relay)


def loggerCheck(p_room_name, p_sensor_temp, p_desired_temp, p_status):
    logging.info('Treating room : ' + p_room_name)
    logging.info('Status of the pump to the room : ' + p_status)
    if (p_status == "close"):
        if (p_sensor_temp > p_desired_temp):
            logging.info(datetime.datetime.now() + ' Status of the room is CLOSED, temps are HIGHER then desired temp. Relays should be OPENING.')
        else:
            logging.info(datetime.datetime.now() + ' Status of the room is CLOSED, temps are within normal parameters. Relays should stay the SAME')
    else:
        if (p_sensor_temp < p_desired_temp):
            logging.info(datetime.datetime.now() + ' Status of the room is OPENED, temps are LOWER then desired temp. Relays should be CLOSING.')
        else:
            logging.info(datetime.datetime.now() + ' Status of the room is OPENED, temps are within normal parameters, Relays should stay the SAME.')


if __name__ == '__main__':
    #CLIMATISATION
    modeClim = 0
    if (modeClim == 1):
        pumpRelay = getPumpRelayStatus()
        rooms = getAllRooms()
        for room in rooms:  
            relay = getRelay(room.relay)
            status = relay.status
            temperatureCheck = room.temp_min - variable_check;
            loggerCheck(room.name, room.sensor_floor, temperatureCheck, room.status)
            #Inverting logic for cooling system. Swapped openRelay/closeRelay function for Cooling.
            if (status == "close"):
                if (getDeviceTemp(room.sensor_floor) > temperatureCheck):
                    logging.info(datetime.datetime.now() + ' OPENING RELAYS ( TEMPERATURE > MIN. TEMP + TEMERATURE CHECK.')
                    logging.info('Current temperature : ' + room.sensor_floor)
                    logging.info('Minimum temp. : ' + room.temp_min)
                    logging.info('Variable temp check: ' + variable_check)
                    openRelayLogicCooling(getRelay(room.relay))
            else:
                if (getDeviceTemp(room.sensor_floor) < room.temp_min):
                    logging.info(datetime.datetime.now() + ' CLOSING RELAYS ( TEMPERATURE < MIN. TEMP + TEMERATURE CHECK.')
                    logging.info('Current temperature : ' + room.sensor_floor)
                    logging.info('Minimum temp. : ' + room.temp_min)
                    logging.info('Variable temp check: ' + variable_check)
                    closeRelayLogicCooling(getRelay(room.relay))
    else:
        #CHAUFFAGE
        pumpRelay = getPumpRelayStatus()
        rooms = getAllRooms()
        for room in rooms:  
            relay = getRelay(room.relay)
            status = relay.status
            temperatureCheck = room.temp_min - variable_check;
            loggerCheck(room.name, room.sensor_floor, temperatureCheck, room.status)
            if (status == "close"):
                if (getDeviceTemp(room.sensor_floor) < temperatureCheck):
                    logging.info(datetime.datetime.now() + ' OPENING RELAYS ( TEMPERATURE < MIN. TEMP + TEMERATURE CHECK.')
                    logging.info('Current temperature : ' + room.sensor_floor)
                    logging.info('Minimum temp. : ' + room.temp_min)
                    logging.info('Variable temp check: ' + variable_check)
                    openRelayLogic(getRelay(room.relay))
            else:
                if (getDeviceTemp(room.sensor_floor) > room.temp_min):
                    logging.info(datetime.datetime.now() + ' CLOSING RELAYS ( TEMPERATURE > MIN. TEMP + TEMERATURE CHECK.')
                    logging.info('Current temperature : ' + room.sensor_floor)
                    logging.info('Minimum temp. : ' + room.temp_min)
                    logging.info('Variable temp check: ' + variable_check)
                    closeRelayLogic(getRelay(room.relay))
