## Important

# write the prog to calculate the area of a circle given its radius using the formula
# are = pi*r^2, pi=3.14

# Logic building formula

# Step 1
# figure out the i/p and o/p
# i/p - r - data type - float
# pi = 3.14
# power - pow or **, anyone
# o/p - float, area,print area

# step 2
# rough logic - area = 3.14*pow(r,2)
# note - * is mul and ** is power

# Step 3
# actual code

radius = float(input("Provide radius of the circle\n"))
area = 3.14345567789709 * (radius ** 2)
# or
# area = 3.14*pow(radius,2)

print("area of the circle is ", area)
# or
# print(f"Area of the circle is {area}")

# Note - f called formatting, we can specify the decimal value, for ex pi=3.14566879870

print(f"area of the circle is (area) {area:.2f}")

# or
print("------------------------------------------")

import math

print(math.pi)
print(math.pow(radius, 2))
area = math.pi * math.pow(radius, 2)
print("circle area is", area)

# or - only one line code, but not suggested

print(3.14 * (float(input("Provide radius of the circle\n")) ** 2))

# print(math.sin(90))
# print(math.tan(90))
# print(math.cos(90))