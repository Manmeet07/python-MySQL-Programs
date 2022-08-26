import mysql.connector

def Rec_Insert():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="GHPS")
    mycursor=mydb.cursor()
    print("Database Connected")
    R=[]
    reg=int(input("Enter Regn No. :"))
    R.append(reg)
    nm=input("Enter Name :")
    R.append(nm)
    cl=int(input("Enter Class :"))
    R.append(cl)
    gen=input("Enter Gender M/F :")
    R.append(gen)
    mycursor.execute('''create table STUDENT(REGN,Name,Class,Gender));''')
    NEWR=(R)
    Q="INSERT INTO STUDENT(REGN, NAME, CLASS, GENDER)VALUES(%s,%s,%s,%s)"
    mycursor.execute(Q,NEWR)
    mydb.commit()
    print("insertion completed")
Rec_Insert()
