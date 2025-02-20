class Father:
    def BHK1(self):
        print("1 BHK")

class Shivam(Father):
    def BHK2(self):
        print("2 BHK")

class Dharinee(Father):
    def BHk5(self):
        print("5 BHK")

shivam = Shivam()
shivam.BHK1()

dharinee = Dharinee()
dharinee.BHK1()
dharinee.BHk5()
# dharinee.BHK2() # not possible, this belog to Shivam