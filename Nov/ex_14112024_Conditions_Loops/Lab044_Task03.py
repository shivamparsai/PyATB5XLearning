# take user age and let him know whether he/she can vote or not
from Nov.ex_09112024_Literals_Variables.Lab029_Task1 import value2

age = int(input("What is your age\n"))
print("Your age is ", age)

if age > 18:
    print("You can vote")
else:
    print("You can not vote")

# age cases
# 1.negative value
# 2.alphabates, special char.
# 3.Valid age real time ex. (age >130)

# Optimize the code