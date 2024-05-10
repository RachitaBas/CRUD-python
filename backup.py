# conn.close()
# cursor.execute("Drop TABLE student")
# cursor.execute("show tables")


managers=[     #multiple values to insert through tuples
    ('clien1',80,'usa',2000),
    ('manisha',67,'canada',100),
    ('manish',12,'bhawan',200)
]
# # for m in managers:
if "salary" not in existing_column_names:
    cursor.execute("ALTER TABLE managers ADD COLUMN salary")
# cursor.executemany("INSERT INTO managers(name,id,address,salary) VALUES (?,?,?,?)",managers)


# cursor.execute("CREATE TABLE managers (name VARCHAR(255), id INT AUTO_INCREMENT PRIMARY KEY,address varchar(255))")


cursor.execute("PRAGMA table_info(managers)")  #to check the columns in managers table
existing_columns = cursor.fetchall()
existing_column_names = [column[1] for column in existing_columns]  #iterates over each tuple from index 1 column

cursor.execute("UPDATE managers SET id=20 WHERE name = 'rachita'") #UPDATE COLUMN
cursor.execute("DELETE FROM managers WHERE id=20 AND name = 'rachita'") #deleet column
# cursor.execute("CREATE TABLE student (name VARCHAR(255), id INT AUTO_INCREMENT PRIMARY KEY,address varchar(255))")
data = [firstname, lastname, age, salary, fullname]
data_check = [bool(element) for element in data]
if all(data_check):
    print("Data insertion passed") 
else:
    print("DATA insertion failed")

    if managers:
        for manager in managers:
            fullname, age, salary = manager
            print("The full name is:", fullname)
            print("The age is:", age)
            print("The salary is:", salary)
             cursor.execute("ALTER TABLE managers DROP COLUMN name")