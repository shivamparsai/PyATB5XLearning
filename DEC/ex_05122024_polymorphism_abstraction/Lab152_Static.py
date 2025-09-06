
# static method, variables - that belongs to class rather than an instance
# static variables - class level variables shared by all instances of the class
# Defined within the class but outside any method
# static method - can be called by class name(no obj creation)

class Test:
    @staticmethod
    def sum(a,b):
        return a+b

    def sub(self,a,b):
        return a-b

print(Test.sum(2, 3))

# t = test()
# r = t.sub(4,4)
# print(r)

# print(t.sum(3,5))

print(Test.sub(1,3,2))