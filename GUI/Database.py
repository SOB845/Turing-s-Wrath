import sqlite3
from sqlite3 import *
import datetime
import os

global path
current_path = os.getcwd()
database_path = current_path + "\\userinfo.db"

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
