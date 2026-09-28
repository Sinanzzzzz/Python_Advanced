# write a program that takes a number as input from user and finds the factorial of that number
# using math.factorial().use a try -except block to handle the value error if user inputs a
# number/character input

import math
while True:
    try:
        n = int(input("Enter a number:"))
        fact = math.factorial(n)
        print("Factorial :",fact)
        break

    except ValueError:
        print("Value error")

# OR        
# import math
# def factorial():
#     try:
#         n = int(input("Enter a number:"))
#         fact = math.factorial(n)
#         print("Factorial :",fact)

#     except ValueError:
#         print("Value error")
#         fact()        # Recursion
        
#     else:
#         pass
# fact()