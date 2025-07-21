## Important

class Calc:
    def sum(self, *args):       # *args - multiple arguments -  can be of different data types
        for a in args:
            print(a)

calc = Calc()
calc.sum(1,2)
calc.sum(3,4,"asas")