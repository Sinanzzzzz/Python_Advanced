#Ask the user to enter an amount and if the amount<balance ,raise customException
#InsuffientBalanceError with the message("Not Enough Balance.Transaction Failed")

class InsufficientBalanceError(Exception):
    pass


try:
    n = int(input("Enter the amount"))
    balance = 60000

    if n > balance:
        raise InsufficientBalanceError("Not Enough Balance.Transaction Failed")
    else:
        print(n)

except InsufficientBalanceError as e:
    print(e)