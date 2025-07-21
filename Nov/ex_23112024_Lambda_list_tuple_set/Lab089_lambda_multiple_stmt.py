## Important

# write a prog to calculate even and odd

def findEvenOdd(num):
    if num % 2 == 0:
        print(num, " is even")
    else:
        print(num, " is odd")

findEvenOdd(5)


# with lambda functions

n = int(input("Enter a number\n"))
checkEvenOdd = lambda num : (num,  "is Even") if num % 2 == 0 else (num, ' is Odd')
print(checkEvenOdd(n))

# If we have multiple statements then Lambda expression is not recommended