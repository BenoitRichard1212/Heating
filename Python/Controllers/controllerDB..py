#!/usr/bin/python

import mysql.connector
from mysql.connector import Error
from Models.globalSetting import globalSetting

_db_cursor = None
_db_conn = None

def connect():
    """ Connect to MySQL database """
    try:
        _db_conn = mysql.connector.connect(host='localhost',
                                       database='Heating',
                                       user='root',
                                       password='B3nmal!gn312')
        if _db_conn.is_connected():
            print('Connected to MySQL database')
            _db_cursor = _db_conn.cursor()

def close():
    _db_conn.close()

def loadGloabalSettings(profileName):
    sql = "SELECT * FROM GlobalConfig WHERE Profile_name = %s"

    _db_cursor.execute(sql, profileName)

    result = _db_cursor.fetchall()

    gb = globalSetting()

def saveGlobalSettings(profileName, errorThreshold, seasonMode, precisionDegree):
    sql = "INSERT INTO GlobalConfig (Profile_name, Error_threshold, Season_Mode, Precision_degree) VALUES     (%s, %d, %s, %d)"
    val = (profileName, errorThreshold, seasonMode, precisionDegree)
    _db_cursor.execute(sql, val)

    _db_conn.commit()

    print(_db_cursor.rowcount, "record inserted.")

if __name__ == '__main__':
    connect()
    saveGlobalSettings()
    loadGloabalSettings()
    close()

def getAllSensor():

def getSensor(sensorName):

def getAllRelay():

def getRelay(relayName)