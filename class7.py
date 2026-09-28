class Account:
    
    def __init__(self):
        self.acctname=input("Enter the account name:")
        self.acctnumber=int(input("Enter the account number:"))
        self.balance=int(input("Enter the balance:"))

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
        
    def showbalance(self):
        print("Current Balance:",self.balance)

l=[]                                        #for storing acc as a list
while(1):
    print("1.Create an account")
    print("2.Withdraw")
    print("3.Deposit")
    print("4.Show balance")
    print("5.Exit")
    
    ch = int(input("Enter your choice:"))
    
    if ch==1:
        a=Account()
        l.append(a)
        
    elif ch==2:
        number=int(input("Enter the account number"))
        for i in l:
            if i.acctnumber == number:
                i.withdraw()
                break
        else:                       # We used for else allnekil eppozhum if case il acc does not 
            print("Account does not exist")        #exit print aakum
            
    elif ch==3:
        number=int(input("Enter the account number"))
        for i in l:
            if i.acctnumber == number:
                i.deposit()
                break
        else:
            print("Account does not exist")
    elif ch==4:
        number=int(input("Enter the account number"))
        for i in l:
            if i.acctnumber == number:
                i.showbalance()
                break
        else:
            print("Account does not exist")
    else:
        exit()