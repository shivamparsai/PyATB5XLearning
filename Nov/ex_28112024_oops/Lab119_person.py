# take input and create a class in python

class Person:

    def __init__(self):
        self.name = input("enter your name\n")
        self.age = input("what is your age\n")
        self.phone = input("your mobile no.\n")
        self.occupation = input("your occupation\n")

    # name = input("enter your name\n")
    # age = input("what is your age\n")
    # phone = input("your mobile no.\n")
    # occupation = input("your occupation\n")

    def yourDetail(self):
        print(f"name is {self.name}\n",
              f"age is {self.age}\n",
              f"phone is {self.phone}\n",
              f"occupation is {self.occupation}")

person1 = Person()

person1.yourDetail()