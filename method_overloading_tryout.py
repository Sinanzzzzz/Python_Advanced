class A:
    def f(self):
        print("In first function f")
    def f(self,a):
        print("In second function f")
    def f(self,a,b):
        print("In third function f")
        
a=A()
# a.f()
# a.f(10)
a.f(20,30)      #only this will work(last function maathram kaanullu same name aanenkil,baaki ellam replaced by new fn)