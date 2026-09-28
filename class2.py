class Person:
    
    print("Enter the details")
    def __init__(self):
        self.name=input("Enter the name:")
        self.age=int(input("Enter the age:"))
        
    def show(self):
        print(self.name,self.age)
        
p1 = Person()
p1.show()

p2 = Person()
p2.show()