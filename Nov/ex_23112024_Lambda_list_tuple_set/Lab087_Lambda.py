## Important

 #Lambda function or expression
# A lambda is an anonymous function that returns some form of data
# Lambda expression always returns a function
# Syntax:
#   lambda parameters : expression
# parameters or arguments - like a normal function, a lambda function can accept any number of arguments
# but must have only one expression.
# Expression - the expression is executed and the result is returned when the lambda function is called.

def power(num):
    return num ** 3

result = power(2)
print(result)

# with lambda function

result1 = lambda num : num ** 3
print(result1(2))

