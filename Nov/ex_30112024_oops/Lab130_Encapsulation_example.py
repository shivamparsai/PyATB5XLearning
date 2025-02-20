# encapsulation - hide the data members (class variables, instance variables)
# by using only the methods

class car:
    def __init__(self):
        self.password = "shivam"    # public instance variable, it is available to everywhere
        self.__password1 = "pass123"    # private instance variable, it is available only in the class

    def chagepassword(self):
        print(self.password)
        print(self.__password1)

c = car()
print(c.password)
c.chagepassword()

# c.password = "dharuu"
#
# print(c.password)

#print(c.__password1)    # error-attributeError: 'car' object has no attribute '__password1'. Did you mean: 'password'?

# private variable __password1 is hidden and cant be access
# we can hide the variable by using __