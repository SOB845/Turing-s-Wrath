import sqlite3
import datetime

def save_password(user_service,user_password):
    current_time = datetime.datetime.utcnow()
    connection = sqlite3.connect('userinfo.db')
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS user_data (service text NOT NULL, password text NOT NULL, date_added text NOT NULL)")
    cursor.execute("INSERT INTO user_data VALUES (?,?,?)",(user_service,user_password,current_time))
    connection.commit()
    connection.close()
    return None

def find_password(Service_Name):
    connection = sqlite3.connect('userinfo.db')
    cursor = connection.cursor()
    cursor.execute("SELECT service,password,date_added FROM user_data WHERE service = (?)",(Service_Name,))
    connection.commit()
    res = cursor.fetchall()
    for row in res:
        print("Service: "+row[0]),
        print("Password: "+row[1]),
        print("Time added: "+row[2])
    connection.close()
    return res
