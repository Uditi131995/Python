def calculator(num1, num2, type):
    if type == '+':
        return num1 + num2
    elif type == '-':
        if num1 > num2:
            return num1 - num2
        else:
            return num2 - num1
    elif type == '*':
        return num1 * num2
    else:
        if num1 > num2:
            return num1/num2
        else:
            return num2 / num1


num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
type = input("Enter the type of operation you wanna do:")

result = calculator(int(num1), int(num2), type)
print(result)
