class MyException(Exception):
    pass

try:
    n = int(input("Enter a number:"))
    
    if n < 18:
        raise MyException("Not Eligible for voting")
    else:
        print(("Eligible for voting"))
except Exception as e:
    print(e)
    
