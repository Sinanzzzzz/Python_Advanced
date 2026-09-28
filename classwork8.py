# 1. Create a class named Circle with an attribute radius.
# Use a constructor to initialize the radius by accepting input from the user.
# Define the following methods:
# getarea() - to calculate and display the area of the circle.
# getperimeter() - to calculate and display the perimeter (circumference) of the circle.
# Create an object of the Circle class and call both methods to display the results.

class Circle:
    
    def __init__(self):
        self.radius=float(input("Enter the radius:"))
        
    def getarea(self):
        area=3.14*(self.radius**2)
        print("Area = ",area)
        
    def getperimeter(self):
        perimeter=2*3.14*self.radius
        print("Perimeter = ",perimeter)


c = Circle()
c.getarea()
c.getperimeter()

#2.
# class Account:
    
#     def __init__(self):
#         self.acctname=input("Enter the account name:")
#         self.acctnumber=int(input("Enter the account number:"))
#         self.balance=int(input("Enter the balance:"))
        
#     def showbalance(self):
#         print("Current Balance:",self.balance)
        
#     def withdraw(self):
#         amount=int(input("Enter the amount to withdraw:"))
#         if amount<=self.balance:
#             self.balance -= amount
#             print("Amount successfuly withdrawn")
#         else:
#             print("Insufficient balance")
#         self.showbalance()
        
#     def deposit(self):
#         amount=int(input("Enter the amount to deposit:"))
#         self.balance += amount
#         print("Amount successfuly deposited")
#         self.showbalance()

# a1 = Account()
# a2 = Account()
# a1.withdraw()
# a1.deposit()
# a2.withdraw()
# a2.deposit()

# l = [a1,a2]                
# for i in l:                 
#     print(i.acctname)       
#     i.showbalance()         