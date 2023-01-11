from math import sqrt, ceil

n = int(input("Please input number:"))
if n==1:
    print(f"{n} is a prime number.")
for i in range(2,ceil(sqrt(n))):
    if n % i == 0:
        print(f"{n} is NOT a prime number.")
        break
    else:
        print("1 is NOT a prime number.")
