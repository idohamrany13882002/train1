import statistics

l1: list[int] = []
for _ in range(5):
    num: int = int(input("Enter a number: "))
    l1.append(num)

print(statistics.mean(l1))
for i in l1:
    print(i, end=", ") if i > statistics.mean(l1) else print("", end="")
