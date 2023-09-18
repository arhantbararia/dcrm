#after installing mysql connector in virtual env


import mysql.connector


dataBase = mysql.connector.connect(
    host= 'localhost',
    user= 'arhantbararia',
    passwd = 'arh123',

)



cursor = dataBase.cursor()

cursor.execute("CREATE DATABASE CRM_DATA")

print("DATABASE created!")