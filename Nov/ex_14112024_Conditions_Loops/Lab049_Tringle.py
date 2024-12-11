# Write a program that classifies a triangle based on its side lengths.
# Given three input values representing the lengths of the sides,
# determine if the triangle is equilateral (all sides are equal), isosceles (exactly two sides are equal),
# or scalene (no sides are equal). Use an if-else statement to classify the triangle.

tringleLength1 = float(input("Enter Triangle side 1 length\n"))
tringleLength2 = float(input("Enter Triangle side 2 length\n"))
tringleLength3 = float(input("Enter Triangle side 3 length\n"))

if tringleLength1 > 0 and tringleLength2 > 0 and tringleLength3 > 0:
    if tringleLength1 == tringleLength2 == tringleLength3:
        print("Triangle is equilateral")
    elif tringleLength1 == tringleLength2 or tringleLength2 == tringleLength3 or tringleLength1 == tringleLength3:
        print("Triangle is isosceles")
    else:
        print("Triangle is scalene")
else:
    print("not a valid length")
