def safty(func):
    def wrapper():
        print("Petrol check")
        print("seat belt check")
        func()
        print("door lock check")
        print("take the key")
        print("====================")
    return wrapper()

@safty
def driveCar():
    print("I am driving the car")

@safty
def ola():
    print("test ola")