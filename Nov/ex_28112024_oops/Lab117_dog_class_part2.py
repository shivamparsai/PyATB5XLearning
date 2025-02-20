class Dog:
    name = "Chow"
    breed = None
    height = None

    # default constructor __init__(), it will be called automatically whenever the obj will be created

    def __init__(self):
        print("I am called automatically")

    def bark(self):
        print("Barking")

    def sleep(self):
        print("sleep")

# object reference

chow = Dog()
mow = Dog()
# Dog() - object
# chow - obj ref

print(chow.name)
print(mow.name)

# we have given the name in the class and upon creating the obj and calling, same hard coded name will be printed for every instance, we should not do like this