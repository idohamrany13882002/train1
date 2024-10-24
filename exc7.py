num1: int = int(input("Enter a number: "))
num2: int = int(input("Enter a number: "))

if num1 > num2:
    if num2 % 2 == 0:
        for i in range(num2, num1 + 2, 2):
            print(i, end=" ")
    else:
        for i in range(num2 + 1, num1 + 1, 2):
            print(i, end=" ")
else:
    if num1 % 2 == 0:
        for i in range(num1, num2 + 2, 2):
            print(i, end=" ")
    else:
        for i in range(num1 + 1, num2 + 1, 2):
            print(i, end=" ")
