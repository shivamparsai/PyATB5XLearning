# Leap day occurs in each year that is a multiple of 4, except for years evenly divisible
# by 100 but not by 400

year = int(input("Enter any year\n"))
r = year % 4
r1 = year % 100
r2 = year % 400

if r == 0 and r1 != 0: