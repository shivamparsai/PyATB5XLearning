from abc import ABC, abstractmethod

class PC:
    def __init__(self):
        print("PC")

class MotherBoard(ABC):
    @abstractmethod
    def startMotherBoard(self):
        pass
class RAM(MotherBoard):
    @abstractmethod
    def startRAM(self):
        pass
class Procecssor(RAM):
    @abstractmethod
    def startProcessor(self):
        pass
class Storage(Procecssor):
    @abstractmethod
    def storageData(self):
        pass

    @staticmethod
    def loadOS():
        print("OS is loading")

    def startMouse(self):
        print("Mouse is starting")

    def useHeadPhone(self):
        print("Use HeadPhone")

class StartPC(Storage):
    def startMotherBoard(self):
        print("MotherBoard")

    def startRAM(self):
        print("RAM")

    def startProcessor(self):
        print("Processor")

    def storageData(self):
        print("Memory loading")

        # self.loadOS()
        self.startMouse()
        self.useHeadPhone()

pc = StartPC()
pc.startMotherBoard()
pc.startProcessor()
pc.storageData()
pc.startRAM()

Storage.loadOS()