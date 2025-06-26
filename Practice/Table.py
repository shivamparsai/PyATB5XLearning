import time
class Table:
    def multiply(self):
        number = int(input("Enter the Number\n"))
        for i in range(1,11):
            if i < 11:
                mul = number*i
                time.sleep(1.7)
                print(i, end="-> ")
                print(mul)

table = Table()
table.multiply()