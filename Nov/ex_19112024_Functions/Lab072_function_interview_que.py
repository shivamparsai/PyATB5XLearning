# # create a prog to sum of 3 no.from the user i/p, if user doesnt provide the vale then take default
# as 100, 200 and 300

def sumOfThreeNum(num1 = 100, num2 = 200, num3 = 300):
    r = num1 + num2 + num3
    print("Sum of ", num1, num2, "and ", num3, " is ", r)

a = float(input("Enter number 1"))
b = float(input("Enter number2"))
c = float(input("Enter number3"))

sumOfThreeNum()
sumOfThreeNum(2,3,4)
sumOfThreeNum(5,5)