class calc:
    def __init__(self):
        print("DC")

    def sum(self, a, b):
        sum = a + b
        return print("Sum is ", sum)

    def sub(self, a, b):
        sub = a - b
        return print("Sub is ", sub)

    def mul(self, a,b):
        mul = a * b
        return print("mul is ", mul)

    def div(self, a,b):
        div = a / b
        return print("div is ", div)

cal = calc()

value = int(input("Enter the value1\n"))
value1 = int(input("Enter the value2\n"))

cal.sum(value, value1)
cal.sub(value,value1)
cal.mul(value,value1)
cal.div(value,value1)

# calc.sum(None,2,3)
