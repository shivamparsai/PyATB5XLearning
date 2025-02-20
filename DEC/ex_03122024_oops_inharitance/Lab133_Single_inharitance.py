# single inheritance

class Father:
    key = "2BHK"
    print(key)

    def car(self):
        print("Alto car")
        print(self.key)

class Son(Father):  # Single Inheritance
    key2 = "3BHK"
    print(key2)

    def car2(self):
        print("SUV")
        print(self.key2)

father = Father()
father.car()
# father.key

son = Son()
son.car2()

son.car()