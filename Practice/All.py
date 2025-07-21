from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name):
        self.name = name
        print(name)

    @abstractmethod
    def makesound(self):
        pass

class Dog(Animal):
    def makesound(self):
        print("bark")

d = Dog("dog")
d.makesound()