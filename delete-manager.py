import sqlite3
db_instance = "crud_database.db" #creating varaibale
conn = sqlite3.connect(db_instance)  # connect to sqlite database
cursor = conn.cursor() 
cursor.execute("DELETE FROM managers WHERE fullname = 'firstname lastname'")
cursor.execute("DELETE FROM managers WHERE age IN (123,3)")
cursor.execute("DELETE FROM managers WHERE fullname = 'ramesh basnet'")

conn.commit()
conn.close()








# cursor.execute("SELECT * FROM managers") #select all recordshow to add
# rows = cursor.fetchall()
# for row in rows:
#     print(row)