# try and the except block is basically used to catch error
# the best practise is to mention the error you are catching
try:
    value = 10 / 0
    number = int(input("Enter a number"))
    print(number)
except ZeroDivisionError as err:
    print(err)
    print("A number cannot be divided by zero")
except ValueError:
    print("Invalid Input")
