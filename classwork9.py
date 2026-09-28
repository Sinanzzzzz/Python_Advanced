# Write a menu-driven Python program using a class Student to perform the following operations:
#
# 1Add Student(roll no,name,marks)
# 2Update Marks
# 3Display All Student Details
# 4Search Student by Roll Number
# 5Delete Student
# 6Exit
# Store student records in a list and perform all operations using the student's roll number.

class Student:
    
    def __init__(self):
        self.rollno=int(input("Enter the roll number:"))
        self.name=input("Enter the name:")
        self.marks=int(input("Enter the marks:"))
        
    def update_mark(self):
        self.mark=int(input("Enter the mark:"))
        
    def display(self):
        print("Roll no:",self.rollno)
        print("Name:",self.name)
        print("Marks:",self.marks)
    
l=[]
while(1):
    print("1.Add Student")
    print("2.Update Marks")
    print("3.Display All Student Details")
    print("4.Search Student")
    print("5.Delete Student")
    print("6.Exit")
    
    ch=int(input("Enter the choice:"))
    
    if ch == 1:
        s=Student()
        l.append(s)
    
    elif ch == 2:
        roll =int(input("Enter the roll no. of student:"))
        for i in l:
            if i.rollno==roll:
                i.update_mark()                 #OR new_marks=int(input("Enter the marks"))
                break                           # i.marks=new_marks
        else:
            print("Roll no. does not exist")
    elif ch == 3:
        for i in l:
            i.display()
            
    elif ch == 4:
        roll =int(input("Enter the roll no. of student:"))
        for i in l:
            if i.rollno==roll:
                print("Student found")
                i.display()
                break
        else:
            print("Roll no. does not exist")        
    elif ch == 5:
        roll =int(input("Enter the roll no. of student:"))
        for i in l:
            if i.rollno==roll:
                l.remove(i)
                break
        else:
            print("Roll no. does not exist")
    else:
        exit()