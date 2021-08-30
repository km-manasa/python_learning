n = int(input("Enter the number to check"))
for i in range(2, n):
    if (n % i == 0):
        print("The given number is not a prime")
        break
else:
    print("The given number is a prime")
