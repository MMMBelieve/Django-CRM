# Installed My sql on my computer
# https://dev.mysql.com/downloads/installer/
# pip instal mysql
# pip install mysql-connector
# pip install mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Renpy7.04!)'

)

# prepare a cursor object
cursorObject = dataBase.cursor()

#Create a database

cursorObject.execute("CREATE DATABASE elderco")

print("All Done!")