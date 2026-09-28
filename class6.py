# 2. Create a class named Account with attributes acctnumber, acctname, and balance.
# Initialize these values using a constructor by taking input from the user.
# Define the following methods:
#
# withdraw() - to withdraw an amount from the account and update the balance.
# deposit() - to deposit an amount into the account and update the balance.
# showbalance() - to display the current balance of the account.
#
# Create an object of the class and call the methods to perform withdrawal
# and deposit operations and display the updated balance.

class Account:
    
    def __init__(self):
        self.acctname=input("Enter the account name:")
        self.acctnumber=int(input("Enter the account number:"))
        self.balance=int(input("Enter the balance:"))
        
    def showbalance(self):
        print("Current Balance:",self.balance)
        
    def withdraw(self):
        amount=int(input("Enter the amount to withdraw:"))
        if amount<=self.balance:
            self.balance -= amount
            print("Amount successfuly withdrawn")
        else:
            print("Insufficient balance")
        self.showbalance()
        
    def deposit(self):
        amount=int(input("Enter the amount to deposit:"))
        self.balance += amount
        print("Amount successfuly deposited")
        self.showbalance()

a1 = Account()
a2 = Account()
a1.showbalance()
a1.withdraw()
a1.deposit()

l = [a1,a2]                 # l = [a1,a2] stores multiple objects in a list
for i in l:                 # for i in l accesses each object one by one
    print(i.acctname)       # instead of calling a1.showbalance(),a2.showbalance() separately
    i.showbalance()         # we can use i.showbalance() to call the method for every object