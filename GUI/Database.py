import sqlite3
from sqlite3 import *
import datetime
import os

global path
current_path = os.getcwd() # The path where the program was run for the first time
database_path = current_path + "\\userinfo.db" # This is the path your database resides in

def create_connection(db_file):
    global conn
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)

def save_password(user_service,user_name,user_password):
    global connection
    global cursor

    create_connection(database_path)
    current_time = datetime.datetime.utcnow()

    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS user_data (service text NOT NULL, username text, password text NOT NULL, date_added text NOT NULL)")
    cursor.execute("INSERT INTO user_data VALUES (?,?,?,?)",(user_service,user_name or None,user_password,current_time))
    conn.commit()
    conn.close()
    return None
