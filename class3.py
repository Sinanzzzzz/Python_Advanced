# Define a class named Employee with attributes empid,name,age,salary,designation
# and methods getsalary() and showpersonaldetails()
# create an object of Employee class and call the methods

class Employee:
    
    def __init__(self):
        self.empid=int(input("Enter employee id:"))
        self.name=input("Enter the name:")
        self.age=int(input("Enter the age:"))
        self.salary=int(input("Enter the salary:"))
        self.designation=input("Enter the designation:")
        
    def showpersonaldetails(self):
        print("Employee Name",self.name,"Age",self.age)
    
    def getsalary(self):
        print("Salary",self.salary)
        
e = Employee()
e.showpersonaldetails()
e.getsalary()
