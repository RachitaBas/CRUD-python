import sqlite3
db_instance = "crud_database.db" #creating varaibale
conn = sqlite3.connect(db_instance)  # connect to sqlite database
cursor = conn.cursor() 

cursor.execute("UPDATE managers SET address = 'palpa' WHERE address = 'bhundol'") #UPDATE COLUMN
cursor.execute("UPDATE managers SET salary = 3000 WHERE salary = 800")
conn.commit()
conn.close()