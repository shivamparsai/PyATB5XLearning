import math

# def power(num):
#     return math.pow(num, 2)
#
# print(power(8))

# lambda expression

# power1 = lambda num : math.pow(num, 2)
# print((power1(7)))

#or
#n = int(input("enter a num\n"))
op2 = lambda : math.pow((int(input("enter number\n"))), 2)
#op2 = lambda num : math.pow(num, 2)
print(op2())

