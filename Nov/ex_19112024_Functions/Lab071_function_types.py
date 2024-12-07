# user defined functions types
# 1.They cannot return anything - non return
# 2.They can return something
# 3.They have parameters/arg
# 4.They do not have parameters/arg

# 1.They cannot return anything - non return
#a. no return type and no parameters/arg

def greet():
    print("Hello")

greet()

# 1.They cannot return anything - non return
#b. no return type but with parameters/arg

def sayHello(name):
    print("Hello", name)

sayHello("test")

# 1.They cannot return anything - non return
#c. no return type but with default parameters/arg (positional arg)

def sayHelloDefaultArg(name = "Shivammmm"):
    print("Hello", name)

sayHelloDefaultArg("Dharuu")

# multiple arg

def multipleArg(name1 = "Shivam", name2 = "parsai"):
    print("hellooo", name1, name2)

multipleArg("A1", "B1")
multipleArg("ShivamDharinee")
multipleArg(name2 = "Amit")

# 2.return type + arg

def sumOfTwo(a,b):
    return a+b

r = sumOfTwo(2, 2)
print(r)

print("===================================")

def sumOfTwoWithDefault(num1 = 10, num2 = 20):
    return num1+num2
r1 = sumOfTwoWithDefault(50, 50)
print(r1)