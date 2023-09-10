import mysql.connector as a
mydb=a.connect(
	host="localhost",
	user="root", #Enter Your mysql Username Here!!!!
	password="Password" #Enter Your Mysql Password Here!!!!
	)
cur=mydb.cursor()
s="create database employeeM"
cur.execute(s)
s0="use employeeM;"
cur.execute(s0)
s1="create table personal(name varchar(20),city varchar(20),dob date,phone varchar(15))"
cur.execute(s1)
s2="create table office(e_id int,name varchar(20),post varchar(30),joining varchar(15),basicpay integer(15))"
cur.execute(s2)
s3="create table salary(e_id int,name varchar(20),year varchar(10),month varchar(10),worked_days integer(10),finalpay integer(10))"
cur.execute(s3)
mydb.commit()
