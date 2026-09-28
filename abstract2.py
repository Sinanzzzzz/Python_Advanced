# Create an abstract class Employee with an abstract method calculate_salary()
# create two subclasses
# -FullTimeEmployee
# -PartTimeEmployee
# Each class should calculate salary differently.

from abc import ABC,abstractmethod

class Employee(ABC):
    
    def __init__(self):
        self.empid=int(input("Enter the Employee id:"))
        self.name=input("Enter the name :")
        self.age=int(input("Enter the age :")) 
            
    @abstractmethod
    def calculate_salary(self):
        pass   
    
class FullTimeEmployee(Employee):
    
    def __init__(self):
        print("Enter the Full time employee details")
        super().__init__()
        self.monthly_salary=int(input("Enter the monthly salary:"))
        
    # def display_detils(self):
    #     print("Employee id :",self.empid)
    #     print("Employee name",self.empid)
    #     print("Age :",self.empid)
        
    def calculate_salary(self):
        print("Salary =",self.monthly_salary)
        
class PartTimeEmployee(Employee):
    
    def __init__(self):
        print("Enter the Part time employee details")
        super().__init__()
        self.salary=int(input("Enter the hours worked:"))
        self.rate=int(input("Enter the rate per hours:"))
        
    def calculate_salary(self):
        print("Salary =",self.salary*self.rate)
        
f = FullTimeEmployee()
f.calculate_salary()

p = PartTimeEmployee()
p.calculate_salary()