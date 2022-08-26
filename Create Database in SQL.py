import pymysql
def c_database(): #Function to create Database as per users choice
 try:
    dname=input("Enter Database Name:")
    c.execute("create database {}".format(dname))
    c.execute("use {}".format(dname))
    print("Database created successfully")
 except Exception as a:
    print("Database Error",a)

db=pymysql.connect(host="localhost",user="root",password="root")
c=db.cursor()
while True:
 print("MENU\n1. Create Database")
 choice=int(input("Enter your choice<1-1>:"))
 if choice==1:
    c_database()
