l1: list[int] = []

for _ in range(10):
    num: int = int(input("Enter a number: "))
    l1.append(num)

l1.sort()
print(l1[-1::-1])
