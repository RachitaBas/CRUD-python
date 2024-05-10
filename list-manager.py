import sqlite3 #imported module to interact python with sqlite datbases
db_instance = "crud_database.db" #creating varaibale 
conn = sqlite3.connect(db_instance)  # establishing connection to sqlite database
cursor = conn.cursor()  # creating cursor object to execute queries
# cursor.execute("CREATE TABLE managers (name VARCHAR(255), id INT AUTO_INCREMENT PRIMARY KEY,address varchar(255))")
cursor.execute("SELECT * FROM managers") #method of cursor obj -select all recordshow to add
rows = cursor.fetchall()  #fetch the results from db
for row in rows:           #iteratethe results and process them
    print(row)

    # cursor.execute("ALTER TABLE managers ADD COLUMN Fullname")
    # cursor.execute("ALTER TABLE managers ADD COLUMN age")
   
conn.commit()
conn.close()
