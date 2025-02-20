class Father:
    def home(self):
        print("2BHK")

class Son(Father):
    def home(self):
        print("4BHK")

son = Son()
son.home()

father = Father()
father.home()