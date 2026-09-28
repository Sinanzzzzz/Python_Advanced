class Person:
    def __init__(self):
        self.name = input("Enter the name:")
        self.age = int(input("Enter the age:"))
    def show(self):
        print("Name =",self.name)
        print("Age =",self.age)
        
class Student(Person):
    def __init__(self):
        super().__init__()   #To call the functionality of __init__() from parent(so both are initilazied)
        self.rollno = int(input("Enter the rollno:"))
        self.mark = int(input("Enter the mark:"))
    
    def show(self):
        super().show()      #To call the functionality of show()from parent
        print("Roll no:",self.rollno,"Mark:",self.mark)
    def updatemark(self):
        self.mark = int(input("Enter the mark:"))
        
s = Student()
s.show()
s.updatemark()
s.show()