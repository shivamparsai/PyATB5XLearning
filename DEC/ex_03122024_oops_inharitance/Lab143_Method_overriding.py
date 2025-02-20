class Father:
    def home(self):
        print("1BHK")

class Son(Father):
    def home(self):
        print("3BHK")

father = Father()
father.home()

son = Son()
son.home()