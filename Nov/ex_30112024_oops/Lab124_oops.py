
a = 10  # global variable

class person:

    b = 11  # Instance variable - belong to class

    def print_info(self):

        c = 20  # Local variable

        print(c)    # Local variable can be accessed directly
        print(self.b)   # Instance variable can be accessed by using self word
        global a
        print(a)

        a = "Hello"
        print(a)


# Local variable will have higher preference as compared to global variable

person = person()

person.print_info()