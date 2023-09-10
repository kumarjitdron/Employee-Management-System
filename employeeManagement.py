import mysql.connector as a
from art import logo
mydb=a.connect(
	host="localhost",
	user="root",
	password="Password",#Enter your Mysql Password Here!!
	database="employeeM")
cur=mydb.cursor()
def npersonal():
	e=input("Enter Employee Name: ")
	c=input("Enter city: ")
	d=input("Enter date of birth: ")
	p=input("Enter Phone No.: ")
	data=(e,c,d,p)
	sql="insert into personal values(%s,%s,%s,%s)"
	cur.execute(sql,data)
	print("Data Entered Sucessfully!!!")
	main()
def personal():
	sql="select * from personal"
	cur.execute(sql)
	d=cur.fetchall()
	for i in d:
		print(i)
	main()
def noffice():
	i=int(input("Enter Employee Id: "))
	e=input("Enter Employee Name: ")
	c=input("Enter Employee post: ")
	d=input("Enter Joining Date: ")
	p=int(input("Enter Employee Basic Pay: "))
	data=(i,e,c,d,p)
	sql="insert into office values(%s,%s,%s,%s,%s)"
	cur.execute(sql,data)
	mydb.commit()
	print("Data Entered Sucessfully!!!")
	main()
def office():
	sql="select * from office"
	cur.execute(sql)
	d=cur.fetchall()
	for i in d:
		print(i)
	main()
def nsalary():
	i=int(input("Enter Employee Id: "))
	e=input("Enter Employee Name: ")
	c=input("Enter Employee year: ")
	d=input("Enter month: ")
	p=int(input("Enter Employee worked days: "))
	q=int(input("Enter Employee Final pay: "))
	data=(i,e,c,d,p,q)
	sql="insert into salary values(%s,%s,%s,%s,%s,%s)"
	cur.execute(sql,data)
	mydb.commit()
	print("Data Entered Sucessfully!!!")
	main()
def salary():
	sql="select * from salary"
	cur.execute(sql)
	d=cur.fetchall()
	for i in d:
		print(i)
	main()
def main():
	print('''
		1.Add New Employee Personal Details
		2.Display Employees Personal Details
		3.Add New Employee Office Details
		4.Display Employees Office Details
		5.Enter Salary Details of Employee
		6.Display Salary Details of Employee
		''')
	choice=int(input("Enter Choice: "))
	while True:
		if choice==1:
			npersonal()
		elif choice==2:
			personal()
		elif choice==3:
			noffice()
		elif choice==4:
			office()
		elif choice==5:
			nsalary()
		elif choice==6:
			salary()
		else:
			print("Enter Correct Choice!!")
			main()
print(logo)
main()






