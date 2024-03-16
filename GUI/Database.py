import sqlite3
from sqlite3 import *
import datetime
import os

global path
current_path = os.getcwd()
database_path = current_path + "\\userinfo.db"

def create_connection(db_file):
    global conn
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)

def save_or_update_password(input_service,input_name,input_password):
    global connection
    global cursor

    create_connection(database_path)
    current_time = str(datetime.datetime.utcnow())

    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS user_data (service text NOT NULL, username text, password text NOT NULL, date_added text NOT NULL)")
    cursor.execute("SELECT * FROM user_data WHERE service = ? AND username = ?", (input_service, input_name or None)) # Check if Service and Username already in database
    conn.commit()
    res = cursor.fetchall()
    print(len(res))

    if res is not None: # There is at least one entry from past that's same with new inputs
        cursor.execute("UPDATE user_data SET password = ?, username = ?, date_added = ? WHERE service = ?", (input_password, input_name or None, current_time, input_service))
        print("Data updated")
    else:
        cursor.execute("INSERT INTO user_data (service, username, password, date_added) VALUES (?,?,?,?)", (input_service, input_name or None, input_password, current_time))
        print("Data inserted")

    conn.commit()
    conn.close()

# Update works fine but does not save new entries
# LINE 28 COULD BE PROBLEMATIC
