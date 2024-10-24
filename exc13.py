sentinel: int = 0
l1: list[int] = []
while True:
    num: int = int(input("Enter a number: "))
    if num == sentinel:
        break
    if num < 1:
        print("Number must be positive")
    else:
        if num == 1:
            print("1 is not prime number")
        else:
            divider: int = 2
            while divider < num:
                if num % divider == 0:
                    break
                divider += 1
            if divider < num:
                print(f"{num} is not prime")
            else:
                l1.append(num)

print(f"there are {l1.__len__()} prime numbers") if l1.__len__() > 1 else print(
    f"there is only {l1.__len__()} prime number")
