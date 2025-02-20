from abc import ABC, abstractmethod

class ExcelReader(ABC):
    @abstractmethod
    def readFromExcel(self):
        pass

class Browser(ExcelReader):
     @abstractmethod
     def startBrowser(self):
         pass

     @abstractmethod
     def stopBrowser(self):
         pass

class TC1(Browser):
    def startBrowser(self):
        print("Start browser")

    def stopBrowser(self):
        print("stop browser")

    def readFromExcel(self):
        print("reading from excel")

    def runTC1(self):
        self.startBrowser()
        self.stopBrowser()
        self.readFromExcel()

tc1 = TC1()
tc1.runTC1()
