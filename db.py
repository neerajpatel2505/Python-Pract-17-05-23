import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user = 'root',
    password = 'root',
)

mucursor = mydb.cursor()
mycursor.execute("CREATE DATABASE testdb")