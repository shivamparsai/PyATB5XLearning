# You can add an Annotation to the function (to perform the extra tasks)
# for ex - before running the function I want to do something (use Dacorators)

# Dacorators in Python are very powerful and flexible tool that allows you to modify the behavior of the function
# or methods without changing their actual code.
# They are essentially functions that take another function as an argument and extend or alter its behavior

def addSafty(func):    # this parameter/arg name can be anything name func is recommended or industry standards
    def wrapper():     # wrapper() name can be anything but name wrapper() is recommended or industry standards
        print("This is called before the function")
        print("Helmet", "Gloves", "Fuel check", "knee guard")
        func()  # calling driveScooty() method
        print("This is called after the function")
        print("End ride")
    return wrapper()

@addSafty       # Dacorator name can be anything
def driveScooty():
    print("This is driveScooty() running")
    print("I am driving the scooty")

@addSafty
def olaRide():
    print("Ola ola cab")