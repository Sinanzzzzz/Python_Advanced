class Person:
    
    def __init__(self,n,a):  #constructor method
                            #used to initialize object properties
        self.name=n
        self.age=a
        
    def show(self):  #self keyword used to refer current object
        print(self.name,self.age)
        
p1 = Person("Kohli",37)  #creates object p1
                         #calls __init__ function defined inside Class Person
p1.show()

p2 = Person("Dhoni",41)  #creates object p2
                         #calls __init__ function defined inside Class Person
p2.show()