try:    
    n1 =int(input("Enter a number:"))
    n2 =int(input("Enter a number:"))
    
    r = n1 + n2
    print(r)
    
except ValueError as v:
    print(v)
    print(type(v))
    
except ZeroDivisionError as z:
    print(z)

except Exception as e:
    print(e)