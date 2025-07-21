## Important

from abc import ABC, abstractmethod

class GearBox(ABC):

    @abstractmethod
    def set_gear(self):
        pass

class Engine(GearBox):

    @abstractmethod
    def starEngine(self):
        # super().set_gear()
        pass

    @abstractmethod
    def stopEngine(self):
        pass

class Car(Engine):
    def starEngine(self):
        print("Engine Start")

    def stopEngine(self):
        print("Stop Engine")

    def set_gear(self):
        print("gear box is ready")

    def drive(self):
        self.starEngine()
        self.stopEngine()

car = Car()
car.drive()
car.set_gear()