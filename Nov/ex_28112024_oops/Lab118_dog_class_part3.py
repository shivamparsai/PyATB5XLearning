class Dog:
    name = None
    breed = None
    height = None

    # Parameterized constructor __init__(self,name,breed)

    def __init__(self,name,breed):
        print("I am parameterized constructor")
        self.name = name
        self.breed = breed

    def bark(self):
        print("Barking")

    def sleep(self):
        print("who is sleeping", self.name)

# object reference

dog1 = Dog("shadow", "dachshund")
dog2 = Dog("max", "lab")
# Dog() - object
# chow - obj ref

print(dog1.name)
print(dog1.breed)
print(dog2.name)
print(dog2.breed)

dog1.sleep()
dog2.sleep()

print(id(dog1)) # address of the reference
print(id(dog2))

# Dog()   # this is 3rd obj but no ref