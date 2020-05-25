#!/usr/bin/python
from relay import Relay
from room import Room
from globalSetting import GlobalSetting
import mysql.connector
from mysql.connector import Error
import RPi.GPIO as GPIO
import time
from decimal import Decimal
import datetime
import logging

GPIO.setmode(GPIO.BCM)
variable_check = 1
pumpRelay = Relay("relay_pump", "close", 17, "utility")
logging.basicConfig(filename="/var/log/Heating/sensors_log.txt", level=logging.INFO)

def connect():
    _db_conn = mysql.connector.connect(host='192.168.2.34',
                                       database='temperatures',
                                       user='logger',
                                       password='password')
    if _db_conn.is_connected():
        logging.info('Connected to MySQL database')
        _db_cursor = _db_conn.cursor()
    else:
        logger.error("Could not connect to Database closeRelay")


def closeRelay(p_relay):
    _db_conn = mysql.connector.connect(host='192.168.2.34',
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
    _db_conn = mysql.connector.connect(host='192.168.2.34',
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
    _db_conn = mysql.connector.connect(host='192.168.2.34',
                                       database='temperatures',
                                       user='logger',
                                       password='password')
    if _db_conn.is_connected():
        print('Connected to MySQL database getPumpRelayStatus')
        _db_cursor = _db_conn.cursor()
        query = "SELECT status FROM relays WHERE name = 'relay_pump';"
        _db_cursor.execute(query)
        row = _db_cursor.fetchone()
        result = row[0]
        _db_conn.close()
        return result
    else:
        print("Could not connect to Database getPumpRelayStatus")


def getRelay(name):
    _db_conn = mysql.connector.connect(host='192.168.2.34',
                                       database='temperatures',
                                       user='logger',
                                       password='password')
    if _db_conn.is_connected():
        print('Connected to MySQL database getRelay')
        _db_cursor = _db_conn.cursor()
        query = "SELECT * FROM relays WHERE name = '%s';" % (name)
        _db_cursor.execute(query)
        row = _db_cursor.fetchone()
        relay = Relay(row[0], row[1], row[2], row[3])
        _db_conn.close()
        return relay
    else:
        print("Could not connect to Database getRelay")



def getAllRelays():
    relays = []
    _db_conn = mysql.connector.connect(host='192.168.2.34',
                                       database='temperatures',
                                       user='logger',
                                       password='password')
    if _db_conn.is_connected():
        print('Connected to MySQL database getAllRelays')
        _db_cursor = _db_conn.cursor()
        query = "SELECT * FROM relays;"
        _db_cursor.execute(query)
        row = _db_cursor.fetchone()
        while row is not None:
            relay = Relay(row[0], row[1], row[2], row[3])
            relays.append(relay)
            row = _db_cursor.fetchone()
        _db_conn.close()
        return relays
    else:
        print("Could not connect to Database getAllRelays")


def getAllRooms():
    rooms = []
    _db_conn = mysql.connector.connect(host='192.168.2.34',
                                       database='temperatures',
                                       user='logger',
                                       password='password')
    if _db_conn.is_connected():
        print('Connected to MySQL database getAllRooms')
        _db_cursor = _db_conn.cursor()
        query = "SELECT * FROM rooms;"
        _db_cursor.execute(query)
        row = _db_cursor.fetchone()
        while row is not None:
            room = Room(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
            rooms.append(room)
            row = _db_cursor.fetchone()
        _db_conn.close()   
        return rooms
    else:
        print("Could not connect to Database getAllRooms")

def getAllGlobalSettings():
    globalSettings = []
    _db_conn = mysql.connector.connect(host='192.168.2.34',
                                       database='temperatures',
                                       user='logger',
                                       password='password')
    if _db_conn.is_connected():
        print('Connected to MySQL database getAllGlobalSettings')
        _db_cursor = _db_conn.cursor()
        query = "SELECT * FROM global_settings;"
        _db_cursor.execute(query)
        row = _db_cursor.fetchone()
        while row is not None:
            globalSetting = GlobalSetting(row[0], row[1])
            globalSettings.append(globalSetting)
            row = _db_cursor.fetchone()
        _db_conn.close()   
        return globalSettings
    else:
        print("Could not connect to Database getAllGlobalSettings")

def getGlobalSetting(name):
    _db_conn = mysql.connector.connect(host='192.168.2.34',
                                       database='temperatures',
                                       user='logger',
                                       password='password')
    if _db_conn.is_connected():
        print('Connected to MySQL database getGloablSetting')
        _db_cursor = _db_conn.cursor()
        query = "SELECT * FROM global_settings WHERE name = '%s';" % (name)
        _db_cursor.execute(query)
        row = _db_cursor.fetchone()
        globalSetting = GlobalSetting(row[0], row[1])
        _db_conn.close()
        return globalSetting
    else:
        print("Could not connect to Database getRelay")

def setPower():
    _db_conn = mysql.connector.connect(host='192.168.2.34',
                                       database='temperatures',
                                       user='logger',
                                       password='password')
    if _db_conn.is_connected():
        print('Connected to MySQL database getGloablSetting')
        _db_cursor = _db_conn.cursor()
        query = "UPDATE global_settings SET value = 0 WHERE name = 'power';"
        _db_cursor.execute(query)
        _db_conn.commit()
        _db_conn.close()
    else:
        print("Could not connect to Database getRelay")

def setShutDownInit():
    _db_conn = mysql.connector.connect(host='192.168.2.34',
                                       database='temperatures',
                                       user='logger',
                                       password='password')
    if _db_conn.is_connected():
        print('Connected to MySQL database getGloablSetting')
        _db_cursor = _db_conn.cursor()
        query = "UPDATE global_settings SET value = 0 WHERE name = 'power_shutoff';"
        _db_cursor.execute(query)
        _db_conn.commit()
        _db_conn.close()
    else:
        print("Could not connect to Database getRelay")


def getSensorTemp(name):
    _db_conn = mysql.connector.connect(host='192.168.2.34',
                                       database='temperatures',
                                       user='logger',
                                       password='password')
    if _db_conn.is_connected():
        print('Connected to MySQL database getSensorTemp')
        _db_cursor = _db_conn.cursor()

        query = "SELECT temperature FROM temperaturedata WHERE sensor = '%s';" % (name)
        _db_cursor.execute(query)
        row = _db_cursor.fetchone()
        result = row[0]
        _db_conn.close()
        return result
    else:
        print("Could not connect to Database getSensorTemp")

def getDeviceTemp(name):
    _db_conn = mysql.connector.connect(host='192.168.2.34',
                                       database='temperatures',
                                       user='logger',
                                       password='password')
    if _db_conn.is_connected():
        print('Connected to MySQL database getSensorTemp')
        _db_cursor = _db_conn.cursor()

        query = "SELECT temperature FROM temperaturedata WHERE sensor = '%s';" % (name)
        _db_cursor.execute(query)
        row = _db_cursor.fetchone()
        result = row[0]
        _db_conn.close()
        return result
    else:
        print("Could not connect to Database getDeviceTemp")        


def openRelayLogic(p_relay):
    anotherIsOpen = checkSystemRelayOpen(p_relay)
    if (anotherIsOpen == False):
        openRelay(p_relay)
        time.sleep(2);
        openRelay(getRelay("relay_pump"))
    else:
        openRelay(p_relay)

def openRelayLogicCooling(p_relay, p_relay_second):
    isAnotherOpen = checkSystemRelayOpen(p_relay)
    
    openRelay(p_relay)
    time.sleep(1);    
    openRelay(p_relay_second)
    
    if (isAnotherOpen == False):
        openRelay(getRelay("relay_pump"))
        time.sleep(2);

def pumpOnlyOpen():
    closePump = True
    relays = getAllRelays()
    for relay in relays:
        if (relay.name != "relay_pump" and relay.status == "open"):
            logging.info(' Pump relay is not the only one opened, staying open for the other relays.')
            closePump = False
    return closePump

def checkIfPumpRelayOpen():
    pump_status = False
    relays = getAllRelays()
    for relay in relays:
        if (relay.name == "relay_pump" and relay.status == "open"):
            pump_status = True
    return pump_status    


def closeRelayLogic(p_relay):
    isAnotherOpen = checkSystemRelayOpen(p_relay)

    if (isAnotherOpen == True):
        closeRelay(p_relay)
    else:
        closeRelay(getRelay("relay_pump"))
        time.sleep(2);
        closeRelay(p_relay)

def closeRelayLogicCooling(p_relay, p_relay_second):
    isAnotherOpen = checkSystemRelayOpen(p_realy)

    if (isAnotherOpen == False):
        closeRelay(getRelay("relay_pump"))
        time.sleep(2);
    
    closeRelay(p_relay)
    time.sleep(1);
    closeRelay(p_relay_second)

def checkSystemRelayOpen(p_relay):
    relays = getAllRelays()
    status = False
    for relay in relays:
        if (relay.type == "system" and relay.name != p_relay.name and relay.status == "open"):
            status = True
    return status

def systemShutdown():
    #La function de setGlobalSettings va changer pour etre plus versatile, on la reutilisera ici.
    setPower()
    setShutDownInit()

def loggerCheck(p_room_name, p_sensor_temp, p_desired_temp):
    logging.info('Treating room : ' + p_room_name)
 #   logging.info('Status of the pump to the room : ' + p_status)
 #   if (p_status == "close"):
    if (p_sensor_temp > p_desired_temp):
        logging.info(' Status of the room is CLOSED, temps are HIGHER then desired temp. Relays should be OPENING.')
    else:
        logging.info(' Status of the room is CLOSED, temps are within normal parameters. Relays should stay the SAME')
 #   else:
    if (p_sensor_temp < p_desired_temp):
        logging.info(' Status of the room is OPENED, temps are LOWER then desired temp. Relays should be CLOSING.')
    else:
        logging.info(' Status of the room is OPENED, temps are within normal parameters, Relays should stay the SAME.')


if __name__ == '__main__':
    power_shutoff = getGlobalSetting("power_shutoff")
    modeClim = getGlobalSetting("modeClim")
    #piscine = getGlobalSetting("modePiscine")
    modePiscine = 0
    #Check pour sequence de fermeture.
    if (power_shutoff == 1):
        if (checkIfPumpRelayOpen() == True):
            closeRelay(getRelay("relay_pump"))

        for room in rooms:  
                relay = getRelay(room.relay)
                status = relay.status
                temperatureCheck = room.temp_min - variable_check
                loggerCheck(room.name, room.sensor_floor, temperatureCheck)
                closeRelay(getRelay(room.relay))
                if (room.mode == "cool"):
                    closeRelay(getRelay(room.relay_second))

        systemShutdown()

    power = getGlobalSetting("power")

    #CLIMATISATION.
    if (power == 1):
        if (modeClim == 1):
            print("Mode clim")  
            pumpRelay = getPumpRelayStatus()
            rooms = getAllRooms()
            for room in rooms:  
                relay = getRelay(room.relay)
                relay_second = getRelay(room.relay_second)
                status = relay.status
                temperatureCheck = room.temp_min - variable_check
                loggerCheck(room.name, room.sensor_wall, temperatureCheck)
                #Inverting logic for cooling system. Swapped openRelay/closeRelay function for Cooling.
                if (room.mode == "cool"):
                    if (getDeviceTemp(room.sensor_wall) > temperatureCheck):
                        if (status == "close"):
                            openRelayLogicCooling(getRelay(room.relay), getRelay(room.relay_second))
                    else:
                        if (status == "open"):
                            closeRelayLogicCooling(getRelay(room.relay), getRelay(room.relay_second))                                      
        else:
            #CHAUFFAGE
            print("Mode chauffage")
            pumpRelay = getPumpRelayStatus()
            rooms = getAllRooms()
            for room in rooms:  
                relay = getRelay(room.relay)
                status = relay.status
                temperatureCheck = room.temp_min - variable_check
                if (room.mode == "heat"):
                    if (getDeviceTemp(room.sensor_floor) < temperatureCheck):
                        if (status == "close"):
                            openRelayLogic(getRelay(room.relay))
                    else:
                        if (status == "open"):
                            closeRelayLogic(getRelay(room.relay))
