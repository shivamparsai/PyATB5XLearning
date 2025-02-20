class Home:
    def __init__(self):
        self.public_var = "father"
        self.__private_var = "child"

    def mom(self):
        print(self.__private_var)
        self.__mobile()

    def __mobile(self):
        print("This is private method")


home = Home()
print(home.public_var)

# print(home.__private_var)   # cant access private variable

home.mom()