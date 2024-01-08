import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Daniel1234",
)

print(mydb)
