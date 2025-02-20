class GrandFather:
    gold = "2KGGold"

    def BHK1(self):
        print("1 BHK")

class Father(GrandFather):
    diamond = "Diamonds"

    def BHK2(self):
        print("2 BHK")

class Son(Father):
    currency = "20000$"

    def BHK5(self):
        print("5 BHK")

son = Son()
print(son.gold)
print(son.currency)

father = Father()
father.BHK1()
print(father.diamond)

