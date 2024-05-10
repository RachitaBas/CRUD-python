import sqlite3
db_instance = "crud_database.db" 
conn = sqlite3.connect(db_instance)  
cursor = conn.cursor()  

firstname=input("Enter your firstname: ")
lastname=(input("enter your lastname: "))
age=int(input("enter your age: "))
address=(input("enter your address: "))
salary=float(input("enter your salary: "))
fullname=(firstname+ " " + lastname)
managers=cursor.execute("INSERT INTO managers(fullname,age,salary,address) VALUES(?,?,?,?)",(fullname,age,salary,address))


data = [firstname,lastname,address, age, salary, fullname]              #creating the list
data_check = [bool(x) for x in data]                 #check if all elements have data
if all(data_check):                              #check if all elements are true
    print("The full name is:", fullname)
    print("The age is:", age)
    print("The salary is:", salary)
    print("The address is:", address)
    print("Data insertion passed") 
else:
    print("DATA insertion failed")
    
conn.commit()
conn.close()
 