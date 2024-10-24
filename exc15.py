num1: int = int(input("Enter a number: "))
num2: int = int(input("Enter a number: "))
counter: int = 0

if num1 == num2:
    counter += 1
elif num1 > num2:
    if num1 % num2 == 0:
        s_num1 = num1
        while num1 > 0:
            counter += 1
            num1 -= num2
        print(f"{s_num1}/{num2} = {counter}")
    else:
        print(f"{num1} can't be divided by {num2}")
else:
    if num2 % num1 == 0:
        s_num2 = num2
        while num2 > 0:
            counter += 1
            num2 -= num1
        print(f"{s_num2}/{num1} = {counter}")
    else:
        print(f"{num2} can't be divided by {num1}")
