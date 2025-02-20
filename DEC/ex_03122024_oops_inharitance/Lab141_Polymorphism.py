# objects - has many forms
# Behaviour is different based on who is calling
# polymorphism allows objects of different classes to be treated as objects of a common superclass.
# method overriding
# method overloading

# Method Overloading


class Dog:

    def bark(self, breed="chow"):
        print(f"dog with {breed} is barking")


    def bark(self, height, age):
        print(f"Dog with {height} and {age} height is barking")



dog = Dog()
dog.bark()