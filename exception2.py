# Write a Python program to create a simple calculator that performs addition, subtraction, multiplication,
# and division based on user choice. Handle invalid inputs and division by zero using exception handling.

while(True):
    try:
        print("Calculator")
        print("Select an option:")
        print("1.Addition:")
        print("2.Subtraction:")
        print("3.Multiplication:")
        print("4.Division:")
        print("5.Exit")

        ch = int(input("Enter your choice:"))
        if ch == 5:
            print("Exiting")
            break
        
        a = int(input("Enter the first number:"))
        b = int(input("Enter the second number:"))
        
        if ch == 1:
            print("Result = ",a+b)
        elif ch == 2:
            print("Result = ",a-b)
        elif ch == 3:
            print("Result = ",a*b)
        elif ch == 4:
            print("Result = ",a/b)
            
    except ValueError:
        print("Value Error:Invalid Input")
        
    except ZeroDivisionError:
        print("Zero Division Error")
    
    except:
        print("Error")
        
# OR
# while True:
#     try:
#         print('1.Addition')
#         print('2.Subtraction')
#         print('3.multiplication')
#         print('4.Division')
#         print('5.exit')

#         n = int(input("Enter choice"))
#         if n in [1,2,3,4]:
#             n1 = int(input("Enter number"))
#             n2 = int(input("Enter number"))

#             s=n1+n2
#             d=n1-n2
#             m=n1*n2
#             q=n1/n2
#     except ZeroDivisionError:
#         print("Zero Division Error")
#     except ValueError:
#         print("Invalid Input")
#     except:
#         print("Error")
#     else:

#         if n == 1:
#                 print('Result', s)
#         elif n == 2:
#                 print("Result", d)
#         elif n == 3:
#                 print("Result", m)
#         elif n == 4:
#                 print("Result", q)
#         else:
#             exit()