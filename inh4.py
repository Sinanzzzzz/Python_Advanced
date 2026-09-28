class Company:
    def __init__(self):
        self.company_name = input("Enter the name of the company:")
        self.location = input("Enter the location of the company:")
        
    def display_company(self):
        print("Company name :",self.company_name)
        print("Company location :",self.location)
        
class Employee(Company):
    def __init__(self):
        super().__init__()
        self.empid = int(input("Enter the employee id:"))
        self.empname = input("Enter the employee name:")
        self.salary = int(input("Enter the salary:"))
        
    def display_details(self):
        print("Employee id :",self.empid)
        print("Employee name :",self.empname)
        print("Salary :",self.salary)
        super().display_company()
        
    def update_salary(self):
        update = self.salary * 10/100
        self.salary = update + self.salary
        print("Updated Salary =",self.salary)
        
e=Employee()
e.display_company()
e.display_details()
e.update_salary()
e.display_details()