num: int = int(input("Enter a positive number: "))

while num <= 0:
    print("Num must be positive")
    num: int = int(input("Enter a positive number: "))

for i in range(1, num + 1):
    if i % 3 == 0 or i % 5 == 0:
        print(i, end=" ")
