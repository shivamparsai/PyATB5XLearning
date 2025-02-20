# Direct method overloading is not supported in python, we need to give default parameters then only
# it is supported
# Python does not support the method overloading in the traditional sense how it should be

class MathUtil:
    def add(self, a=2, b=3):
        return a + b

    def add(self, a=3, b=2, c=8):
        return a + b + c

    def add(self, a=0, b=1, c=8, d=0):
        return a + b + c + d

math = MathUtil()
q = math.add(2, 3)
print(q)
q1 = math.add(1, 1)
print(q1)
q2 = math.add(0, 0)
print(q2)