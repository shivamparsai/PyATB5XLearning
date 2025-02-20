# hide the details and show what os required

from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def makeSound(self):
        pass

class Dog(Animal):
    def makeSound(self):
        print("Bark")

dog = Dog("MAx")
dog.makeSound()