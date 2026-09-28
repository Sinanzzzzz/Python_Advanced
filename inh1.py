class Parent:
    def m1(self):
        print("In Parent Class Method m1")
        
    def m2(self):
        print("In Parent Class Method m2")
        
class Child(Parent):
    def m1(self):                       # Method Overriding
        super().m1()                  # super() - parent il ninnum call aakaaan m1 inu vendi
        print("In Child Class Method m1") 
    def m3(self):                       # own attribute
        print("In Child Class Method m3")
        
c=Child()
c.m1()    
c.m3()
c.m2()