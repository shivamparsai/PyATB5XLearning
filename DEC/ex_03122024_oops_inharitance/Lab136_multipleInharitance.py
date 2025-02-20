class Father:
    def home(self):
        return "This is from the Father"

    def fatherMoney(self):
        return 5

class Mother:
    def home(self):
        return "This is from Mother"

    def motherMoney(self):
        return 2

class Son(Father,Mother):
    def info(self):
        print("son")

son = Son()
print(son.fatherMoney())
print(son.motherMoney())

print(son.home())   # If we have same method name in both the clss and upon calling that method

# whichever class is inherited 1st (In this case Father, line no. 15)

