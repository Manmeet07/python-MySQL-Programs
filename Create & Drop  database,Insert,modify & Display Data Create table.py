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
def c_table():          #Function to create Table
 try:
    c.execute('''create table testing(rollno integer,stname char(20));''')
    print("Table created successfully")
 except Exception as a:
    print("Create Table Error",a)

def e_data():     #Function to Insert Data
 try:
    while True:
       rno=int(input("Enter student rollno:"))
       name=input("Enter student name:")
       c.execute("insert into testing values({},'{}')".format(rno,name))
       choice=input("Do you want to add more record<y/n>:")
       if choice in "Nn":
           break
 except Exception as a:
    print("Insert Record Error",a)
def d_data():     #Function to Display Data
 try:
    c.execute("select * from testing")
    data=c.fetchall()
    for i in data:
       print(i)
 except Exception as a:
    print("Display Record Error",a)
def m_data():     #Function to Modify Data
 try:
    rno=int(input("Enter the roll whose name to be updated:"))
    c.execute("update testing set stname='PQR' where rollno={}".format(rno))
    print("Data Upadted Sucessfully")
 except Exception as a:
    print("Display Record Error",a)
db=pymysql.connect(host="localhost",user="root",password="root")
c=db.cursor()
while True:
 print("MENU\n1. Create Database\n2. Drop Database \n3. Create Table\n4. Insert Record \n5. Display Entire Data\n6.Modify Data \n7. Exit")
 choice=int(input("Enter your choice<1-6>:"))
 if choice==1:
    c_database()
 elif choice==2:
    d_database()
 elif choice==3:
    c_table()
 elif choice==4:
    e_data()
 elif choice==5:
    d_data()
 elif choice==6:
    m_data()
 elif choice==7:
    break
