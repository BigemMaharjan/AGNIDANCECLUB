import mysql.connecter

mydb = mysql.connector.connect(
	host="127.0.0.1",
	user="root",
	password="",
	database="agnidanceclub"
	)

mycursor = mydb.cursor()

