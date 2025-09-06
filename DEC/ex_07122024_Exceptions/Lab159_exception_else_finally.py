# Important
# try:
#     num1 = int(input("enter num 1\n"))
#     num2 = int(input("enter num 2\n"))
#
#     c = num1/num2
# except Exception as e:
#     print(e)


try:
    num1 = int(input("enter num 1\n"))
    num2 = int(input("enter num 2\n"))

    c = num1 / num2


except ValueError as e:
    print(e)
    # print("provide only digits")

except ZeroDivisionError as e:
    print(e)
    # print("not divisible by 0, get lost")

else:   # if there is no error in the try block then it will execute the else block code
    # otherwise it will catch the error in the except block
    print("result is ", c)

finally:
    print("this code will always be executed")