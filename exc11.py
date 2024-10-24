sentinel: int = 0
sum1: int = 0

while True:
    num: int = int(input("Enter a number: "))
    if num == sentinel:
        break
    if num < 0:
        sum1 += num

print(sum1)
