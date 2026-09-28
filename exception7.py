#Ask the user to enter a password.if its length is less than 8 characters ,raise
#a customexception InvalidPasswordError with the message ("Password should be 8 
# characters")

class InvalidPasswordError(Exception):
    pass

try:
    n = input("Enter a password:")
    
    if len(n) < 8:
        raise InvalidPasswordError("Password should be 8 characters")
    else:
        print(n)
except InvalidPasswordError as e:  
    print(e)