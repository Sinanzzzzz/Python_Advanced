try:
    n1=int(input("Enter a number"))
    n2=int(input("Enter a number"))
    
    result = n1 / n2
    
except ValueError:
    print("Value error")
    
except ZeroDivisionError:
    print("Zero Division error")
    
except:
    print("Error")
    
else:
    print("Result",result)
    
finally:
    print("Done")