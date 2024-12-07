# find the ax between 3 numbers

num1 = int(input("Enter num1\n"))
num2 = int(input("Enter num2\n"))
num3 = int(input("Enter num3\n"))

if num1 > num2 and num1 > num3:
    print(num1, " is greatest")
elif num2 > num1 and num2 > num3:
    print(num2, " is greatest")
else:
    print(num3, " is greatest")