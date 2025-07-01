import sqlite3
from sqlite3 import *
import datetime
import os

global path
current_path = os.getcwd()
database_path = current_path + "\\userinfo.db"
mainpass_loc = current_path + "\\mainpass.db"

def create_connection():
    global conn
    conn = None
    try:
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()
        print(sqlite3.version)
    except Error as e:
        print(e)

    cursor.execute("CREATE TABLE IF NOT EXISTS user_data (service text NOT NULL, username text, password text NOT NULL, date_added text NOT NULL)")
    conn.commit()
    conn.close()

def save_or_update_password(input_service,input_name,input_password):
    global connection
    global cursor

    create_connection()
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    current_time = datetime.datetime.utcnow()

    cursor.execute("INSERT INTO user_data (service, username, password, date_added) VALUES (?,?,?,?)", (input_service,input_name or None,input_password,current_time))

    conn.commit()
    conn.close()

def create_mainpass_database(MainPass, Recovery_Word):
    global mainpass_loc
    global conn
    global cursor

    conn = sqlite3.connect(mainpass_loc)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS main_password (id INTEGER PRIMARY KEY AUTOINCREMENT, Pass text NOT NULL, Recovery text NOT NULL)")
    cursor.execute("INSERT INTO main_password (Pass,Recovery) VALUES (?,?)", (MainPass, Recovery_Word))
    conn.commit()
    conn.close()
