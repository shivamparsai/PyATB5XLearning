class Person:
    id = None
    name = None
    age = None
    email = None
    height = None
    gender = None
    mob_no = None
    address = None

    def talk(self): # no returning no arg, self will be 1st arg
        print("I can talk")

    def sleep(self, name):  # arg with no return
        print("I am a method")
        print("sleep", name)

    def sleep2(self, name): # arg with return
        print("I am a method")
        return None

    def walk(self):
        print("I am walking")

    def walk_return(self): # no arg with return
        return "I am waling"

# create an object of a class
# objectRef = ClassName() -> Object

geeta = Person()
geeta.name = "Geeta Sharma"
geeta.gender = "Female"
