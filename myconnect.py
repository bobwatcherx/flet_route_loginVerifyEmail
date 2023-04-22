import mysql.connector
mydb = mysql.connector.connect(
  host="172.17.0.2",
  user="root",
  password="PRIVATE",
  database="dbcustomer"
)

mycursor = mydb.cursor()