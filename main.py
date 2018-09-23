import mysql.connector
from mysql.connector import Error

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

def loadGloabalSettings():
    _db_cursor.execute("SELECT * FROM GlobalConfig")

    result = _db_cursor.fetchall()

    for x in result:
        print(x)

def saveGlobalSettings():
    sql = "INSERT INTO GlobalConfig (Profile_name, Error_threshold, Season_Mode, Precision_degree) VALUES     (%s, %d, %s, %d)"
    val = ("Maison", 1, "Hiver", 1)
    _db_cursor.execute(sql, val)

    _db_conn.commit()

    print(_db_cursor.rowcount, "record inserted.")

if __name__ == '__main__':
    connect()
    saveGlobalSettings()
    loadGloabalSettings()
    close()
