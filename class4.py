# Define a class named Student with attributes rollno,name,mark1,mark2,mark3
# and method display() to display roll number and total mark of a student
# create a student object and call the methods

class Student:
    
    def __init__(self):
        self.rollno=int(input("Enter the roll number:"))
        self.name=input("Enter the name:")
        self.mark1=int(input("Enter mark1:"))
        self.mark2=int(input("Enter mark2:"))
        self.mark3=int(input("Enter mark3:"))
        
    def display(self):
        print("Roll no:",self.rollno)
        print("Total marks:",self.mark1+self.mark2+self.mark3)
        
s = Student()
s.display()