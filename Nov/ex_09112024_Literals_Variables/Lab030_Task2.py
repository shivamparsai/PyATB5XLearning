# Take 2 input user and print the Quotient and Remainder

value1 = int(input("Enter 1st value\n"))
value2 = int(input("Enter 2nd value\n"))

q = value1 // value2
r = value1 % value2

print(f"quotient -> {q}")
print(f"remainder -> {r}")

# print("The quotient is ", value1 // value2)
# print("The Remainder is ", value1 % value2)
#
# # OR
#
# print("The quotient and remainder is", divmod(value1, value2))
