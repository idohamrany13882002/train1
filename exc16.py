num: int = int(input("Enter a three digits number:"))
sum1: int = 0

if not 100 < num < 999:
    print("not in range")
else:
    sum1 += num % 10
    num1 = num // 10
    sum1 += num1 % 10
    num2 = num1 // 10
    sum1 += num2 % 10

print(f"the sum of {num} is divisible by 3") if sum1 % 3 == 0 else print(f"the sum of {num} isn't divisible by 3")
