import sqlite3
from sqlite3 import *
import datetime

def save_password(user_service,user_password):
    global connection
    global cursor
    current_time = datetime.datetime.utcnow()
    connection = sqlite3.connect('userinfo.db')
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS user_data (service text NOT NULL, username text, password text NOT NULL, date_added text NOT NULL)")
    cursor.execute(""INSERT INTO user_data VALUES (?,?,?,?)",(user_service,user_name or None,user_password,current_time"))
    connection.commit()
    connection.close()
    return None
