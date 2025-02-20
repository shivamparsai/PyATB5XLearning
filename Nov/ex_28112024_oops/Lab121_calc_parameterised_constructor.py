class calc:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def sum(self):
        sum = self.a + self.b
        return print("Sum is ", sum)

    # def sum(self,q,w):
    #     sum = q + w
    #     return print("Sum is ", sum)

    def sub(self):
        sub = self.a - self.b
        return print("Sub is ", sub)

    def mul(self):
        mul = self.a * self.b
        return print("mul is ", mul)

    def div(self):
        div = self.a / self.b
        return print("div is ", div)

calc1 = calc(1,1)
calc2 = calc(3,4)

calc1.sum()
calc1.sub()
calc2.sub()

# calc1.sum(2,3)