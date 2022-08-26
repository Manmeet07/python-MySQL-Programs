import pymysql
def c_database():     #Function to create Database as per users choice
 try:
    dname=input("Enter Database Name:")
    c.execute("create database {}".format(dname))
    c.execute("use {}".format(dname))
    print("Database created successfully")
 except Exception as a:
    print("Database Error",a)
def d_database():     #Function to Drop Database as per users choice
 try:
    dname=input("Enter Database Name to be dropped:")
    c.execute("drop database {}".format(dname))
    print("Database deleted sucessfully")
 except Exception as a:
    print("Database Drop Error",a)

db=pymysql.connect(host="localhost",user="root",password="root")
c=db.cursor()
while True:
 print("MENU\n1. Create Database\n2. Drop Database ")
 choice=int(input("Enter your choice<1-2>:"))
 if choice==1:
    c_database()
 elif choice==2:
    d_database()
