# a = int(input("enter num1"))    # value error can come
# b = int(input("enter num2"))    # value error can come
#
# c = a/b # zeroiviionerror can come
#
# print(c)

# to handle the exception we use try and except
# try:
#   try this code, if error
#except:
#   execute me if try has any error

try:
    a = int(input("enter num1"))    # value error can come
    b = int(input("enter num2"))    # value error can come

    c = a/b # zeroiviionerror can come

    print(c)

except Exception as e:
    print(e)




