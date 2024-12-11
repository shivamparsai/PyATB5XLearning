global_a = 10       # global variable can be used anywhere

def myFunction():
    local_b = 15       # local variable can only be used within the function or block only
    print(local_b)
    print(global_a)

myFunction()

# print(local_b)    # can not be used outside of the function because it is defined in the function