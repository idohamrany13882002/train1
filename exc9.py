num: int = int(input("Enter a positive number: "))

for i in range(1, num + 1):
    if i % 7 == 0:
        print(i, end=" ")
