import mysql.connector
from mysql.connector import Error

db_cursor = None
db_conn = None
Profile_name = None
 
def connect():
    """ Connect to MySQL database """
    try:
        db_conn = mysql.connector.connect(host='localhost',
                                       database='Heating',
                                       user='root',
                                       password='B3nmal!gn312')
        if db_conn.is_connected():
            print('Connected to MySQL database')
             db_cursor = db_conn.cursor()
 
    except Error as e:
        print(e)

def close():
    finally:
        db_conn.close()

def loadGloabalSettings():

    db_cursor.execute("SELECT * FROM GlobalConfig")

    result = db_cursor.fetchall()

    for x in result:
        print(x)

def saveGlobalSettings():

    sql = "INSERT INTO GlobalConfig (Profile_name, Error_threshold, Season_Mode, Precision_degree) VALUES (%s, %d, %s, %d)"
    val = ("Maison", 1, "Hiver", 1)
    db_cursor.execute(sql, val)

    db_conn.commit()

    print(db_cursor.rowcount, "record inserted.")
 
 
if __name__ == '__main__':
    connect()
    saveGlobalSettings()
    loadGloabalSettings()
    close()
x
