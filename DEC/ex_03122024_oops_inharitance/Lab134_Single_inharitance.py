class Parent:
    gold = "2KG"
    print(gold)

    def BHK2(self):
        print("2BHK")

class Child(Parent):
    dimond = "Dimonds"
    # print(dimond)

    def BHK3(self):
        print("3BHK")

parent = Parent()
# parent.gold
child = Child()