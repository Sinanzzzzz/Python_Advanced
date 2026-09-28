#Ask the user to enter a number.if the number is less than or equal to 0,
# raise a ValueError with the message "Number must be Positive"

try:
    n = int(input("Enter a number:"))
    
    if n <= 0:
        raise ValueError("Number must be Positive")
    else:
        print("The number is positive")
except ValueError as e:
    print(e)