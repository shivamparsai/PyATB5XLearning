# Method overloading  is not supported in python
# we need to set the default parameter values then only it will work

class Calc:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c=3):
        return a + b + c

calc = Calc()
r = calc.add(2,3)
print(r)