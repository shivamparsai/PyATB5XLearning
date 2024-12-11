def decorator1(func):
    def wrapper():
        print("Dacorator1")
        func()
    return wrapper

def decorator2(func):
    def wrapper():
        print("Dacorator2")
        func()
    return wrapper

@decorator1
@decorator2
def sayHello():
    print("Hello")

sayHello()